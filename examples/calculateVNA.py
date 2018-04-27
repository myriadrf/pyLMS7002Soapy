import numpy
import os, sys

if len(sys.argv)!=2 and len(sys.argv)!=3:
    print("Usage: python calculateVNA.py measurementName [plotFigures]")
    print("plotFigures is optional and can have values plot for plotting figures or save to plot and save the figures")
    exit(1)

startFreq = 2.3e9
endFreq = 2.6e9
nPoints = 101
measName = sys.argv[1]

saveFig = False
plotFig = False
if len(sys.argv)==3:
    if sys.argv[2]=="plot":
        plotFig = True
    if sys.argv[2]=="save":
        plotFig = True
        saveFig = True

if plotFig:
    from matplotlib.pyplot import *
    import smithplot
    from smithplot.smithaxes import update_scParams
    import warnings
    warnings.filterwarnings("ignore", module="matplotlib")

fMin=startFreq
fMax=endFreq

#############################################################################
# Auxiliary functions

def readFile(fileName, fMin=0, fMax=1e20):
    inFile = open(fileName, 'r')
    res = [ [], [], [] ]
    for line in inFile:
        if line[0]=="#":
            continue
        line = line.strip()
        if line=="":
            continue
        tmp = line.split()
        if float(tmp[0])<fMin or float(tmp[0])>fMax:
            continue
        res[0].append( float(tmp[0]) )
        res[1].append( float(tmp[1]) )
        res[2].append( float(tmp[2]) )
    inFile.close()
    return [ numpy.array(res[0]), numpy.array(res[1]), numpy.array(res[2]) ]

def filterData(f, data, fMin=0, fMax=1e20):
    res = []
    for i in range(0, len(f)):
        if f[i]>fMin and f[i]<fMax:
            res.append(data[i])
    return numpy.array(res)
    
def unwrap(phase):
    # Unwrap the phase
    phase_unwrap = []
    intAng = 0
    for i in range(0,len(phase)-1):
        phase_unwrap.append(phase[i]+intAng)
        dph = phase[i+1]-phase[i]

        if abs(dph)>150:
            if dph>0:
                    intAng += -180
            else:
                    intAng += 180
    phase_unwrap.append(phase[-1]+intAng)
    phase_unwrap=numpy.array(phase_unwrap)

    # Second pass
    phase_unwrap2 = []
    intAng = 0
    for i in range(0,len(phase_unwrap)-1):
        phase_unwrap2.append(phase_unwrap[i]+intAng)
        dph = phase_unwrap[i+1]-phase_unwrap[i]
        if dph<-150:
            phase_unwrap[i+1] += 180
 
        if dph>10 and dph<45:
            intAng += -45
        if dph>45 and dph<135:
            intAng += -90
        if dph>135 and dph<180:
            intAng += -180
        if dph>180:
            intAng += -360
    phase_unwrap2.append(phase_unwrap[-1]+intAng)
    phase_unwrap2=numpy.array(phase_unwrap2)
    return phase_unwrap2
#############################################################################

# Read the measurement resutls
dutFileName = 'vna_'+measName+'_DUT_'+str(startFreq)+'_'+str(endFreq)+'_'+str(nPoints)+'.txt'
shortFileName = 'vna_'+measName+'_short_'+str(startFreq)+'_'+str(endFreq)+'_'+str(nPoints)+'.txt'

dutData = readFile(dutFileName)
shortData = readFile(shortFileName)

freq = dutData[0]
f = freq

dutPhase = unwrap(dutData[2]) * numpy.pi/180
shortPhase = unwrap(shortData[2]) * numpy.pi/180

if plotFig:
    plot(numpy.array(f)/1e9,shortPhase)
    xlabel('f [GHz]')
    ylabel('Short Phase')
    grid()
    show()
    plot(numpy.array(f)/1e9,dutPhase, linewidth=1.5, aa=True)
    xlabel('f [GHz]')
    ylabel('DUT Phase')
    grid()
    show()

dutData[1] = 20.0*numpy.log10(dutData[1])
shortData[1] = 20.0*numpy.log10(shortData[1])

measGammaDut = numpy.power(10.0, dutData[1]/20) * numpy.exp(1j * dutPhase)#/2)
measGammaShort = numpy.power(10.0, shortData[1]/20) * numpy.exp(1j * shortPhase)#/2)

GammaShort = numpy.array([-1.0] * len(f)) # assume ideal short

returnLoss = dutData[1] - shortData[1]

vswr = (10**(-returnLoss/20)+1)/(10**(-returnLoss/20)-1)
if plotFig:
    plot(numpy.array(f)/1e9,vswr)
    title('VSWR')
    xlabel('f [GHz]')
    ylabel('VSWR')
    grid()
    show()

gammaMag = numpy.power(10.0, returnLoss/20.0)
dutPhase = dutPhase - shortPhase + numpy.pi
GammaDut = gammaMag * numpy.exp(1j * dutPhase)
ZDut = (1.0 + GammaDut)/(1.0 - GammaDut)

if plotFig:
    plot(numpy.array(f)/1e9, 20*numpy.log10( numpy.abs(GammaDut)), color='b', linewidth=1.5, aa=True)
    xlabel('f [GHz]')
    ylabel('S11 [dB]')
    grid()
    if saveFig:
        savefig(measName+'_s11.png')
    show()

    figure(figsize=(24, 16))
    subplot(1, 1, 1, projection='smith',grid_major_fancy=True,
                       grid_minor_fancy=True, plot_hacklines=True)
    ZDutPlot = filterData(freq, ZDut, fMin, fMax)
    plot(ZDutPlot, markevery=1, label="S11", color='b', linewidth=1.5, aa=True)
    if saveFig:
        savefig(measName+'_smith.png')
    show()

outFileName = measName + '.s1p'
outFile = open(outFileName, 'w')
outFile.write('# Hz S RI R 50\n')
for i in range(0, len(GammaDut)):
    outFile.write(str(f[i])+"\t"+str(numpy.real(GammaDut[i]))+"\t"+str(numpy.imag(GammaDut[i]))+"\n")
outFile.close()


