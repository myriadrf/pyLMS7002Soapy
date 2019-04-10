
from timeit import default_timer as timer
import numpy
import os, sys
from pyLMS7002Soapy import pyLMS7002Soapy as pyLMSS

if len(sys.argv) < 2:
    print("Usage: python measureVNA_900M.py measurementName [startFreq Mhz] [endFreq Mhz] [stepFreq Mhz]")
    exit(1)

startFreq =  800e6
endFreq   =  1000e6
stepFreq  =  1e6
measName = sys.argv[1]

if len(sys.argv) == 5:
  startFreq = int(float(sys.argv[2]) * 1e6)
  endFreq   = int(float(sys.argv[3]) * 1e6)
  stepFreq  = int(float(sys.argv[4]) * 1e6)

nPoints =  int( (endFreq - startFreq) / 1e6 ) + 1

print ("")
print ("Using startFreq=%i endFreq=%i stepFreq=%i (nPoints=%i)" % (startFreq, endFreq, stepFreq, nPoints) )
print ("")


#################################################
# MCU related

def mcuProgram():
    # Load MCU program
    logTxt("Loading MCU program...\t", end="")
    mcu = lms7002.mSPI
    mcu.loadHex("vna.hex")
    # Check MCU firmware
    mcu.P0 = 0
    mcu.P0 = 0xFF
    firmwareID = mcu.P1 - 0x80
    if firmwareID != 0x31:
        logTxt("Wrong firmware ID : " + str(firmwareID) + ", expected 49")
        exit(1)
    else:
        logTxt("OK (Firmware ID = " + str(firmwareID) + ")")
    mcu.P0 = 0
    lms7002.MAC = 'A'


def mcuRSSI():
    # Read averaged RSSI from MCU
    mcu = lms7002.mSPI
    mcu.SPISW_CTRL = 'MCU'
    mcu.P0 = 1
    while mcu.P1 == 0xFF:
        pass
    mcu.P0 = 0x12
    RSSI = mcu.P1 * 1.0
    mcu.P0 = 0x11
    RSSI = mcu.P1 * 1.0 + RSSI * 256.0
    mcu.P0 = 0x10
    RSSI = mcu.P1 * 1.0 + RSSI * 256.0
    mcu.SPISW_CTRL = 'BB'
    return RSSI


def mcuPhase():
    # Use MCU to determine the phase
    mcu = lms7002.mSPI
    RxTSP = lms7002.RxTSP['A']
    RxTSP.GC_BYP = 'USE'
    RxTSP.GCORRI = 0

    mcu.SPISW_CTRL = 'MCU'
    mcu.P0 = 2
    while mcu.P1 == 0xFF:
        pass
    mcu.P0 = 0x11
    phase = 1.0 * mcu.P1
    mcu.P0 = 0x10
    phase = mcu.P1 + phase * 256.0
    mcu.SPISW_CTRL = 'BB'
    if phase > 2 ** 15:
        phase = -(2 ** 16) + phase
    phase = 180.0 * phase / (1.0 * 0x6487)
    RxTSP.GC_BYP = 'BYP'
    RxTSP.GCORRI = 2047
    return phase


#################################################
# Auxiliary functions

def logTxt(text, end="\n"):
    print(text, end=end)
    sys.stdout.flush()


def userConfirmation(msg):
    userReady = 'n'
    while userReady != 'y':
        userReady = input(msg + '. Type y to continue. ')


def syncPhase(lms7002):
    TRF = lms7002.TRF['A']
    RFE = lms7002.RFE['A']
    SXT = lms7002.SX['T']
    SXT.PD_FDIV = 1
    TRF.PD_TLOBUF_TRF = 1
    RFE.PD_QGEN_RFE = 1
    TRF.PD_TLOBUF_TRF = 0
    RFE.PD_QGEN_RFE = 0
    SXT.PD_FDIV = 0


def adjustRxGain(lms7002):
    RBB = lms7002.RBB['A']
    RFE = lms7002.RFE['A']
    RxTSP = lms7002.RxTSP['A']
    TxTSP = lms7002.TxTSP['A']

    TxTSP.CMIX_BYP = 'USE'
    RxTSP.GC_BYP = 'USE'
    RxTSP.GCORRQ = 0

    pgaGain = 0
    pgaStep = 16

    if isMini:
        lnaGain = 2
    else:
        lnaGain = 3

    while pgaStep > 0:
        RBB.G_PGA_RBB = pgaGain + pgaStep
        RFE.G_LNA_RFE = lnaGain
        if mcuRSSI() < 50e3:
            pgaGain += pgaStep
        pgaStep = int(pgaStep / 2)

    RBB.G_PGA_RBB = pgaGain
    RFE.G_LNA_RFE = lnaGain

    TxTSP.CMIX_BYP = 'BYP'
    RxTSP.GC_BYP = 'BYP'
    RxTSP.GCORRQ = 2047

    I = 0x7FFF
    Q = 0x8000
    TxTSP.loadDCIQ(I, Q)
    return pgaGain, lnaGain


#################################################################

logTxt("Searching for LimeSDR... ", end="")

limeSDR = pyLMSS.pyLMS7002Soapy(0)
if limeSDR.boardName == "LimeSDRMini":
    isMini = True
    lms7002 = limeSDR.LMS7002
    lms7002.fRef = 40e6
    LNA = 'LNAW'
else:
    isMini = False
    lms7002 = limeSDR.LMS7002
    lms7002.fRef = 30.72e6
    LNA = 'LNAL'

lms7002.MIMO = 'MIMO'
logTxt("FOUND")

# Initial configuration
logTxt("Tuning CGEN... ", end="")
startTime = timer()
lms7002.CGEN.setCLK(300e6)
endTime = timer()
logTxt("OK\t(" + str(float(round(float(endTime - startTime) * 10)) / 10) + " s)")

logTxt("Tuning SXT... ", end="")
startTime = timer()
lms7002.SX['T'].setFREQ(startFreq)
endTime = timer()
logTxt("OK\t(" + str(float(round(float(endTime - startTime) * 10)) / 10) + " s)")

# Make ADC and DAC clocks equal
lms7002.CGEN.EN_ADCCLKH_CLKGN = 0
lms7002.CGEN.CLKH_OV_CLKL_CGEN = 2

cal = lms7002.calibration

calThreshold = 500  # RSSI threshold to trigger RX DC calibration

RBB = lms7002.RBB['A']
TBB = lms7002.TBB['A']
if isMini:
    TBB.CG_IAMP_TBB = 5
else:
    TBB.CG_IAMP_TBB = 20

RxTSP = lms7002.RxTSP['A']
RxTSP.GCORRQ = 2047
RxTSP.GCORRI = 2047
RxTSP.AGC_MODE = 'RSSI'
RxTSP.AGC_BYP = 'USE'
RxTSP.RSSI_MODE = 'RSSI'

TxTSP = lms7002.TxTSP['A']
TxTSP.TSGMODE = 'DC'
TxTSP.INSEL = 'TEST'
TxTSP.CMIX_BYP = 'BYP'
TxTSP.GFIR1_BYP = 'BYP'
TxTSP.GFIR2_BYP = 'BYP'
TxTSP.GFIR3_BYP = 'BYP'
TxTSP.GC_BYP = 'BYP'
TxTSP.DC_BYP = 'BYP'
TxTSP.PH_BYP = 'BYP'
I = 0x7FFF
Q = 0x8000
TxTSP.loadDCIQ(I, Q)

TxNCO = lms7002.NCO["TXA"]
NCOfreq = 100e3
TxNCO.MODE = 0
TxNCO.setNCOFrequency(0, NCOfreq)
TxNCO.SEL = 0

TRF = lms7002.TRF['A']
if isMini:
    TRF.LOSS_MAIN_TXPAD_TRF = 0
else:
    TRF.LOSS_MAIN_TXPAD_TRF = 0

TRF.EN_LOOPB_TXPAD_TRF = 0
TRF.L_LOOPB_TXPAD_TRF = 0
TRF.PD_TLOBUF_TRF = 0

if isMini:
    TRF.SEL_BAND1_TRF = 0
    TRF.SEL_BAND2_TRF = 1
    limeSDR.configureAntenna(startFreq)
else:
    TRF.SEL_BAND1_TRF = 1
    TRF.SEL_BAND2_TRF = 0

RFE = lms7002.RFE['A']

lms7002.SX['R'].EN_G = 0
lms7002.SX['R'].EN_DIR = 0
lms7002.SX['T'].PD_LOCH_T2RBUF = 0  # Both RX and TX use the TX PLL

mcuProgram()  # Load the program to MCU SRAM

print("Calibrating RX path...")

lnaGain = 15
pgaGain = 31

TRF.PD_TXPAD_TRF = 1  # Turn off TXPAD while calibrating RX DC
cal.rxDCLO('A', LNA, lnaGain=lnaGain, pgaGain=pgaGain)  # Calibrate RX DC
TRF.PD_TXPAD_TRF = 0  # Turn on TXPAD

userConfirmation("Connect SHORT")

freqs = numpy.linspace(startFreq, endFreq, num=nPoints)
res = []
resPhase = []
pgaGains = []
lnaGains = []
refPhase = mcuPhase()
for i in range(0, len(freqs)):
    # Measure reference power levels and phase
    f = freqs[i]
    logTxt("f=" + str(f) + "... ", end="")
    startTime = timer()

    lms7002.verbose = 0
    lms7002.SX['T'].setFREQ(f)
    lms7002.SX['T'].PD_LOCH_T2RBUF = 0
    syncPhase(lms7002)

    pgaGain, lnaGain = adjustRxGain(lms7002)
    pgaGains.append(pgaGain)
    lnaGains.append(lnaGain)

    TRF.PD_TXPAD_TRF = 1
    calRSSI = RxTSP.RSSI
    if calRSSI > calThreshold:
        cal.rxDCLO('A', LNA, lnaGain=lnaGain, pgaGain=pgaGain)
        calRSSI = RxTSP.RSSI
    TRF.PD_TXPAD_TRF = 0

    TxTSP.CMIX_BYP = 'USE'
    RxTSP.GC_BYP = 'USE'
    RxTSP.GCORRQ = 0

    rssi = 1.0 * mcuRSSI()

    TxTSP.CMIX_BYP = 'BYP'
    RxTSP.GC_BYP = 'BYP'
    RxTSP.GCORRQ = 2047

    res.append(rssi)
    if i == 0:
        refPhase = mcuPhase()
        phase = 0.0
    else:
        phase = mcuPhase() - refPhase
    endTime = timer()
    resPhase.append(phase)
    lms7002.verbose = 1000
    logTxt("OK\t(" + str(float(round(float(endTime - startTime) * 10)) / 10) + " s)\t(" + str(i + 1) + "/" + str(
        nPoints) + ") RSSI = " + str(rssi) + " (Cal = " + str(calRSSI) + ", PGA=" + str(pgaGain) + ", LNA=" + str(
        lnaGain) + ")" + " phase = " + str(phase))

res = numpy.array(res)

# Write the data to file
outFileName = 'vna_' + measName + '_short_' + str(startFreq) + '_' + str(endFreq) + '_' + str(nPoints) + '.txt'
outFile = open(outFileName, 'w')
txtRes = "# f, coupled power\n"
for i in range(0, len(res)):
    f = freqs[i]
    y = res[i]
    phase = resPhase[i]
    txtRes += str(f) + '\t' + str(y) + '\t' + str(phase) + '\n'
outFile.write(txtRes)
outFile.close()

lms7002.verbose = 0
lms7002.SX['T'].setFREQ(startFreq)
lms7002.SX['T'].PD_LOCH_T2RBUF = 0
syncPhase(lms7002)
TRF.PD_TXPAD_TRF = 1  # Turn off TXPAD while calibrating RX DC
cal.rxDCLO('A', LNA, lnaGain=lnaGain, pgaGain=pgaGain)
calRSSI = RxTSP.RSSI
TRF.PD_TXPAD_TRF = 0  # Turn on TXPAD
refPhase = mcuPhase()

userConfirmation("Connect DUT")

freqs = numpy.linspace(startFreq, endFreq, num=nPoints)
res = []
resPhase = []
for i in range(0, len(freqs)):
    # Measure the DUT reflected power and phase
    f = freqs[i]
    logTxt("f=" + str(f) + "... ", end="")
    startTime = timer()
    pgaGain = pgaGains[i]
    lnaGain = lnaGains[i]
    RBB.G_PGA_RBB = pgaGain
    RFE.G_LNA_RFE = lnaGain
    if i != 0:
        lms7002.verbose = 0
        lms7002.SX['T'].setFREQ(f)
        lms7002.SX['T'].PD_LOCH_T2RBUF = 0
        syncPhase(lms7002)

        TRF.PD_TXPAD_TRF = 1
        calRSSI = RxTSP.RSSI
        if calRSSI > calThreshold:
            cal.rxDCLO('A', LNA, lnaGain=lnaGain, pgaGain=pgaGain)
            calRSSI = RxTSP.RSSI
        TRF.PD_TXPAD_TRF = 0

    TxTSP.CMIX_BYP = 'USE'
    RxTSP.GC_BYP = 'USE'
    RxTSP.GCORRQ = 0

    rssi = 1.0 * mcuRSSI()

    TxTSP.CMIX_BYP = 'BYP'
    RxTSP.GC_BYP = 'BYP'
    RxTSP.GCORRQ = 2047

    res.append(rssi)
    phase = mcuPhase() - refPhase
    resPhase.append(phase)
    endTime = timer()
    lms7002.verbose = 1000
    logTxt("OK\t(" + str(float(round(float(endTime - startTime) * 10)) / 10) + " s)\t(" + str(i + 1) + "/" + str(
        nPoints) + ") RSSI = " + str(rssi) + " (Cal = " + str(calRSSI) + ")" + " phase = " + str(phase))

res = numpy.array(res)

# Write the data to file
outFileName = 'vna_' + measName + '_DUT_' + str(startFreq) + '_' + str(endFreq) + '_' + str(nPoints) + '.txt'
outFile = open(outFileName, 'w')
txtRes = "# f, coupled power\n"
for i in range(0, len(res)):
    f = freqs[i]
    y = res[i]
    phase = resPhase[i]
    txtRes += str(f) + '\t' + str(y) + '\t' + str(phase) + '\n'
outFile.write(txtRes)
outFile.close()
