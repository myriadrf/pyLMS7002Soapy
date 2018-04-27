from __future__ import print_function
from matplotlib.pyplot import *
import time
from pyLMS7002Soapy import *
import numpy as np

if len(sys.argv)!=2:
    print("Usage: python measureSNA.py measurementName")
    exit(1)

fastSweep = True

measName = sys.argv[1]

startFreq = 30e6
endFreq = 3000e6

################################
#
################################

def configureRxTx(sdr, sampleRate, cgenFrequency, rfBandwidth, rfFrequency, rxGain, txGain):

    sdr.cgenFrequency = cgenFrequency
    sdr.rxSampleRate = sampleRate
    sdr.rxBandWidth = rfBandwidth
    sdr.rxRfFreq = rfFrequency
    sdr.rxGain = rxGain

    sdr.txSampleRate = sampleRate
    sdr.txBandwidth = rfBandwidth
    sdr.txGain = txGain
    sdr.txRfFreq = rfFrequency

    rxStream = sdr.sdr.setupStream(SOAPY_SDR_RX, SOAPY_SDR_CF32, [0])
    sdr.tddMode = True  # Both Rx and Tx use Tx PLL
    sdr.testSignalDC(0x3fff, 0x3fff)
    return rxStream

    
def readSamples(sdr, rxStream, nSamples):
    buff = np.zeros(2*nSamples, np.complex64)
    sdr.sdr.activateStream(rxStream, SOAPY_SDR_END_BURST, 0, 2*nSamples)
    numElemsRequest = 2*nSamples
    while numElemsRequest > 0:
        sr = sdr.sdr.readStream(rxStream, [buff], 2*nSamples)
        numElemsRequest -= sr.ret
    sdr.sdr.deactivateStream(rxStream)
    return buff[nSamples:]

def f2s(val, decPlaces):
    tmp = round(val*10**decPlaces)
    tmp = tmp/10**decPlaces
    formatString = "%."+str(decPlaces)+"f"
    return formatString % tmp

def userConfirmation(msg):
    userReady = 'n'
    while userReady != 'y':
        userReady = raw_input(msg + '. Type y to continue. ')    

################################
#
################################

sdr = pyLMS7002Soapy(0)
sdr.configureAntenna(startFreq)


if fastSweep:
    sampleRate = 10e6
    rfBandwidth = 100e6
    cgenFrequency = 80e6 
else:
    sampleRate = 5e6
    rfBandwidth = 100e6
    cgenFrequency = 80e6 


rxGain = 20
txGain = 30
rfFrequency = startFreq

rxStream = configureRxTx(sdr, sampleRate, cgenFrequency, rfBandwidth, rfFrequency, rxGain, txGain)

nwindow = 127.0
nSamples = 8192

dncofreq = 2*sampleRate * nwindow/nSamples
ncosteps = int(sampleRate/dncofreq/4)
ncofreq = -(ncosteps+0.5)*dncofreq
sdr.txNCOFreq = ncofreq

span = endFreq - startFreq
nFreqs = 2*span/sampleRate
freqList = startFreq - ncofreq + (span/(nFreqs-1.0)) * np.arange(0, nFreqs)

measFreq = []
measPowerSHORT = []
measPowerDUT = []
txGainList = []

txGain = 0

userConfirmation("Connect SHORT")

start_time = time.time()
for j in range(0,len(freqList)):
    freq = freqList[j]
    sdr.txRfFreq = freq
    sdr.configureAntenna(freq)
    ncofreq = -1.5*dncofreq
    readSamples(sdr, rxStream, nSamples)
    readSamples(sdr, rxStream, nSamples)
    print("Measuring "+f2s((freq-ncosteps*dncofreq)/1e9,3)+" - "+f2s((freq+ncosteps*dncofreq)/1e9,3) + " GHz", end=" ")
    sdr.txNCOFreq = ncofreq
    samplePosition = int(ncofreq/sampleRate*nSamples+nSamples/2.0)

    while txGain<64:
        sdr.txGain = txGain
        buff = readSamples(sdr, rxStream, nSamples)
        spect = np.fft.fft(buff)
        spect = np.fft.fftshift(spect)
        power = 20*np.log10(abs(spect[samplePosition]))
        if power<65:
            txGain += 1
        elif power>70:
            txGain -= 1
        else:
            break

    txGainList.append(txGain)
    sdr.txGain = txGain
    readSamples(sdr, rxStream, nSamples)
    
    for i in range(-ncosteps,ncosteps+1):
        print(".", end="")
        ncofreq = (i+0.5)*dncofreq
        sdr.txNCOFreq = ncofreq
        
        measFreq.append(freq + ncofreq)
        samplePosition = int(ncofreq/sampleRate*nSamples+nSamples/2.0)
        buff = readSamples(sdr, rxStream, nSamples)

        spect = np.fft.fft(buff)
        spect = np.fft.fftshift(spect)
        measPowerSHORT.append(20*np.log10(abs(spect[samplePosition])))
    print("")

measFreq = np.array(measFreq)
measPowerSHORT = np.array(measPowerSHORT)
    
#############################
#
#############################

userConfirmation("Connect DUT")

start_time = time.time()
for j in range(0,len(freqList)):
    freq = freqList[j]
    sdr.txRfFreq = freq
    sdr.configureAntenna(freq)
    ncofreq = -1.5*dncofreq
    readSamples(sdr, rxStream, nSamples)
    readSamples(sdr, rxStream, nSamples)
    print("Measuring "+f2s((freq-ncosteps*dncofreq)/1e9,3)+" - "+f2s((freq+ncosteps*dncofreq)/1e9,3) + " GHz", end=" ")
    sdr.txNCOFreq = ncofreq
    samplePosition = int(ncofreq/sampleRate*nSamples+nSamples/2.0)

    txGain = txGainList[j]
    sdr.txGain = txGain
    readSamples(sdr, rxStream, nSamples)
    
    for i in range(-ncosteps,ncosteps+1):
        print(".", end="")
        ncofreq = (i+0.5)*dncofreq
        sdr.txNCOFreq = ncofreq

        samplePosition = int(ncofreq/sampleRate*nSamples+nSamples/2.0)
        buff = readSamples(sdr, rxStream, nSamples)

        spect = np.fft.fft(buff)
        spect = np.fft.fftshift(spect)
        measPowerDUT.append(20*np.log10(abs(spect[samplePosition])))
    print("")

measPowerDUT = np.array(measPowerDUT)

s11 = measPowerDUT-measPowerSHORT

outFileName = measName + '.s1p'
outFile = open(outFileName, 'w')
outFile.write('# Hz S DB R 50\n')
for i in range(0, len(measFreq)):
    outFile.write(str(measFreq[i])+"\t"+str(s11[i])+"\t0\n")
outFile.close()

plot(measFreq, s11)
xlabel("f [GHz]")
ylabel("S11 [dB]")
show()

