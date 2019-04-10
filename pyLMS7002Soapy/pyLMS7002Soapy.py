import SoapySDR
from SoapySDR import *  # SOAPY_SDR_* constants
from pyLMS7002Soapy.LMS7002 import LMS7002
from pyLMS7002Soapy.weakproxy import Proxy
from timeit import default_timer as timer
import atexit


#######################################
# Board class
#######################################


class pyLMS7002Soapy(object):
    def __init__(self, verbose=0):
        self.verbose = verbose
        SDR_ARGS = {'driver': 'lime'}
        self.sdr = SoapySDR.Device(SDR_ARGS)
        self._tdd = False
        self.fRef = 0
        if self.sdr.__str__() == "FT601:LimeSDR-Mini":
            self.boardName = "LimeSDRMini"
        elif self.sdr.__str__() == "FX3:LimeSDR-USB":
            self.boardName = "LimeSDR"
        else:
            raise ValueError("Unsupported board : " + self.boardName)
        self.LMS7002 = LMS7002(SPIwriteFn=self.LMS7002_Write, SPIreadFn=self.LMS7002_Read
                               , verbose=verbose, MCUProgram=self.MCUProgram, fRef=self.fRef)
        self.channel = 0
        self.previousBand = [None, None]

    @staticmethod
    def log(logMsg):
        print(logMsg)

    #
    # Configure antenna
    #

    def configureAntenna(self, frequency):
        """
        Select the appropriate RX and TX interfaces based on operating frequency.
        """
        if self.boardName == "LimeSDRMini":
            if frequency >= 2e9:
                band = "HIGH"
            else:
                band = "LOW"
            if self.previousBand[self.channel] == band:
                return
            else:
                self.previousBand[self.channel] = band

            if frequency >= 2e9:
                self.sdr.setAntenna(SOAPY_SDR_TX, self.channel, 'BAND1')
            else:
                self.sdr.setAntenna(SOAPY_SDR_TX, self.channel, 'BAND2')
            if frequency >= 2e9:
                self.sdr.setAntenna(SOAPY_SDR_RX, self.channel, 'LNAH')
            else:
                self.sdr.setAntenna(SOAPY_SDR_RX, self.channel, 'LNAW')
        elif self.boardName == "LimeSDR":
            if frequency >= 1.5e9:
                band = "HIGH"
            else:
                band = "LOW"
            if self.previousBand[self.channel] == band:
                return
            else:
                self.previousBand[self.channel] = band

            if frequency >= 1.5e9:
                self.sdr.setAntenna(SOAPY_SDR_TX, self.channel, 'BAND2')
            else:
                self.sdr.setAntenna(SOAPY_SDR_TX, self.channel, 'BAND1')
            if frequency >= 1.5e9:
                self.sdr.setAntenna(SOAPY_SDR_RX, self.channel, 'LNAH')
            else:
                self.sdr.setAntenna(SOAPY_SDR_RX, self.channel, 'LNAL')
        else:
            raise ValueError('Unsupported board : ' + self.boardName)

    #
    # TX RF frequency
    #

    @property
    def txRfFreq(self):
        return self.sdr.getFrequency(SOAPY_SDR_TX, self.channel, 'RF')

    @txRfFreq.setter
    def txRfFreq(self, freq):
        self.sdr.setFrequency(SOAPY_SDR_TX, self.channel, 'RF', freq)

    #
    # TX NCO frequency
    #

    @property
    def txNCOFreq(self):
        return self.sdr.getFrequency(SOAPY_SDR_TX, self.channel, 'BB')

    @txNCOFreq.setter
    def txNCOFreq(self, freq):
        self.sdr.setFrequency(SOAPY_SDR_TX, self.channel, 'BB', freq)

        #

    # RX RF frequency
    #

    @property
    def rxRfFreq(self):
        self.sdr.getFrequency(SOAPY_SDR_RX, self.channel, 'RF')

    @rxRfFreq.setter
    def rxRfFreq(self, freq):
        self.sdr.setFrequency(SOAPY_SDR_RX, self.channel, 'RF', freq)

    #
    # RX NCO frequency
    #

    @property
    def rxNCOFreq(self):
        self.sdr.getFrequency(SOAPY_SDR_RX, self.channel, 'BB')

    @rxNCOFreq.setter
    def rxNCOFreq(self, freq):
        self.sdr.setFrequency(SOAPY_SDR_RX, self.channel, 'BB', freq)

        #

    # Test signal
    #

    def testSignalDC(self, I, Q):
        if self.channel == 0:
            chan = 'A'
        else:
            chan = 'B'
        self.LMS7002.TxTSP[chan].INSEL = 'TEST'
        self.LMS7002.TxTSP[chan].TSGMODE = 'DC'
        self.LMS7002.TxTSP[chan].loadDCIQ(I, Q)

    #
    # TDD mode
    #

    @property
    def tddMode(self):
        return self._tdd

    @tddMode.setter
    def tddMode(self, tdd):
        """
        Put the chip in TDD mode.
        """
        self._tdd = tdd
        if tdd:
            self.LMS7002.SX['R'].EN_DIR = 0
            self.LMS7002.SX['T'].EN_DIR = 0
            self.LMS7002.SX['R'].EN_G = 0
            self.LMS7002.SX['T'].PD_LOCH_T2RBUF = 0  # Both RX and TX use the TX PLL
        else:
            self.LMS7002.SX['R'].EN_DIR = 1
            self.LMS7002.SX['T'].EN_DIR = 1
            self.LMS7002.SX['R'].EN_G = 1
            self.LMS7002.SX['T'].PD_LOCH_T2RBUF = 0  # RX and TX use different PLLs

    #
    # Sample rate
    #

    @property
    def rxSampleRate(self):
        return self.sdr.getSampleRate(SOAPY_SDR_RX, 0)

    @rxSampleRate.setter
    def rxSampleRate(self, val):
        self.sdr.setSampleRate(SOAPY_SDR_RX, 0, val)

    @property
    def txSampleRate(self):
        return self.sdr.getSampleRate(SOAPY_SDR_TX, 0)

    @txSampleRate.setter
    def txSampleRate(self, val):
        self.sdr.setSampleRate(SOAPY_SDR_TX, 0, val)

    @property
    def cgenFrequency(self):
        return self.sdr.getMasterClockRate()

    @cgenFrequency.setter
    def cgenFrequency(self, val):
        self.sdr.setMasterClockRate(val)

    #
    # Gain
    #

    @property
    def rxGain(self):
        return self.sdr.getGain(SOAPY_SDR_RX, 0)

    @rxGain.setter
    def rxGain(self, val):
        self.sdr.setGain(SOAPY_SDR_RX, 0, val)

    @property
    def txGain(self):
        return self.sdr.getGain(SOAPY_SDR_TX, 0)

    @txGain.setter
    def txGain(self, val):
        self.sdr.setGain(SOAPY_SDR_TX, 0, val)

    # Bandwidth
    @property
    def rxBandwidth(self):
        return self.sdr.getBandwidth(SOAPY_SDR_RX, 0)

    @rxBandwidth.setter
    def rxBandwidth(self, val):
        self.sdr.setBandwidth(SOAPY_SDR_RX, 0, val)

    @property
    def txBandwidth(self):
        return self.sdr.getBandwidth(SOAPY_SDR_TX, 0)

    @txBandwidth.setter
    def txBandwidth(self, val):
        self.sdr.setBandwidth(SOAPY_SDR_TX, 0, val)

    #########################
    # Low level functions
    #########################        

    def readRegister(self, register, chip="RFIC0"):
        val = self.sdr.readRegister(chip, register)
        if self.verbose > 10:
            self.log("rd " + hex(val) + " from " + hex(register))
        return val

    def writeRegister(self, register, value, chip="RFIC0"):
        if self.verbose > 10:
            self.log("wr " + hex(value) + " to " + hex(register))
        self.sdr.writeRegister(chip, register, value)

    def getLMS7002(self):
        return self.LMS7002

    def LMS7002_Write(self, regList, chip="RFIC0"):
        """
        Write the data to LMS7002 via SPI interface.
        regList is a list of registers to write in the format:
        [ (regAddr, regData), (regAddr, regData), ...]
        packetSize controls the number of register writes in a single USB transfer
        """
        for reg in regList:
            regAddr, regData = reg
            self.writeRegister(regAddr, regData, chip)

    def LMS7002_Read(self, regList, chip="RFIC0"):
        """
        Read the data from LMS7002 via SPI interface.
        regList is a list of registers to read in the format:
        [ regAddr, regAddr, ...]
        packetSize controls the number of register writes in a single USB transfer
        """
        regData = []
        for reg in regList:
            regData.append(self.readRegister(reg, chip))
        return regData

    #
    # LMS7002 MCU program
    #

    def MCUProgram(self, mcuProgram, Mode):
        ver, rev, mask = self.getLMS7002().chipInfo
        if mask == 1:
            # MCU has 16k RAM
            if len(mcuProgram) > 16384:
                raise ValueError(
                    "MCU program for mask 1 chips must be less than 16 kB. Given program size:" + str(len(mcuProgram)))
            if len(mcuProgram) == 8192:  # Check if program is 8k
                mcuProgram += [0] * 8192  # Extend it to 16k
            self._MCUProgram_Direct(mcuProgram, Mode)
        else:
            # MCU has 8k RAM
            if len(mcuProgram) > 8192:
                raise ValueError(
                    "MCU program for mask 0 chips must be less than 8 kB. Given program size:" + str(len(mcuProgram)))
            self._MCUProgram_Direct(mcuProgram, Mode)

    def _MCUProgram_Direct(self, mcuProgram, Mode):
        """
        Write the data to LMS7002 MCU via SPI interface.
        MCU is programmed directly by using bulk interface MCU commands.
        mcuProgram is 8192 or 16384 bytes long array holding the MCU program.
        mode selects the MCU programming mode.
        """
        if Mode not in [0, 1, 2, 3, 'EEPROM_AND_SRAM', 'SRAM', 'SRAM_FROM_EEPROM']:
            raise ValueError("Mode should be [1,2,3, 'EEPROM_AND_SRAM', 'SRAM', 'SRAM_FROM_EEPROM']")
        if Mode == 0:
            return
        elif Mode == 1 or Mode == 'EEPROM_AND_SRAM':
            mode = 1
        elif Mode == 2 or Mode == 'SRAM':
            mode = 2
        else:
            mode = 3

        if len(mcuProgram) != 8192 and len(mcuProgram) != 16384:
            raise ValueError("MCU program should be 8192 or 16384 bytes long")

        toSend = [(2, 0), (2, mode)]  # Write 0 to address 2, write mode to address 2 (mSPI_CTRL)
        self.LMS7002_Write(toSend)
        lms7002 = self.getLMS7002()

        pos = 0
        while pos < len(mcuProgram):
            startTime = timer()
            while lms7002.mSPI.EMPTY_WRITE_BUFF == 0:
                if timer() - startTime > 1:
                    raise IOError("MCU programming timeout")

            for j in range(0, 4):
                toSend = []
                for i in range(0, 8):
                    toSend.append((4, mcuProgram[pos]))
                    pos += 1
                self.LMS7002_Write(toSend)
            if mode == 3:
                break
        startTime = timer()
        while lms7002.mSPI.PROGRAMMED == 0:
            if timer() - startTime > 1:
                raise IOError("MCU programming timeout")
