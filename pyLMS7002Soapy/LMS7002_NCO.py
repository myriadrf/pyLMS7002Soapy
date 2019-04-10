# ***************************************************************
# * Name:      LMS7002_NCO.py
# * Purpose:   Class implementing LMS7002 NCO functions
# * Author:    Lime Microsystems ()
# * Created:   2016-11-14
# * Copyright: Lime Microsystems (limemicro.com)
# * License:
# **************************************************************

from pyLMS7002Soapy.LMS7002_base import LMS7002_base


class LMS7002_NCO(LMS7002_base):
    __slots__ = ['rxtx', 'fcwDict', 'phoDict']  # Used to generate error on typos

    def __init__(self, chip, RxTx, Channel):
        if RxTx not in ['RX', 'TX']:
            raise ValueError("Parameter RxTx must be 'RX' or 'TX'")
        if Channel not in ['A', 'B']:
            raise ValueError("Parameter Channel must be 'A' or 'B'")
        self.chip = chip
        self.rxtx = RxTx
        self.channel = Channel
        self.prefix = self.rxtx + "NCO_"
        # FCW lookup dictionary
        self.fcwDict = {0: ('1', '2'),
                        1: ('3', '4'),
                        2: ('5', '6'),
                        3: ('7', '8'),
                        4: ('9', 'A'),
                        5: ('B', 'C'),
                        6: ('D', 'E'),
                        7: ('F', '10'),
                        8: ('11', '12'),
                        9: ('13', '14'),
                        10: ('15', '16'),
                        11: ('17', '18'),
                        12: ('19', '1A'),
                        13: ('1B', '1C'),
                        14: ('1D', '1E'),
                        15: ('1F', '20')}
        # PHO lookup dictionary
        self.phoDict = {0: '3',
                        1: '4',
                        2: '5',
                        3: '6',
                        4: '7',
                        5: '8',
                        6: '9',
                        7: 'A',
                        8: 'B',
                        9: 'C',
                        10: 'D',
                        11: 'E',
                        12: 'F',
                        13: '10',
                        14: '11',
                        15: '12'}

    #
    # NCO mode
    #

    @property
    def MODE(self):
        """
        Get the mode of NCO
        """
        return self._readReg('CFG', 'MODE')

    @MODE.setter
    def MODE(self, value):
        """
        Set the mode of NCO
        """
        if value not in range(0, 2):
            raise ValueError("Mode must be [0,1]")
        self._writeReg('CFG', 'MODE', value)

    #
    # NCO phase for mode=0
    #

    @property
    def PHO(self):
        """
        Get the NCO phase for mode=0
        """
        return self._readReg('0', 'DATA<15:0>')

    @PHO.setter
    def PHO(self, value):
        """
        Set the NCO phase for mode=0
        """
        if not (0 <= value <= 65535):
            raise ValueError("PHO must be [0,65535]")
        self._writeReg('0', 'DATA<15:0>', value)

    #
    # NCO dithering
    #

    @property
    def DTHBIT(self):
        """
        Get the number of dithered NCO bits 
        """
        return self._readReg('CFG', 'DTHBIT<3:0>')

    @DTHBIT.setter
    def DTHBIT(self, value):
        """
        Set the number of dithered NCO bits
        """
        if not (0 <= value <= 15):
            raise ValueError("Number of bits for dithering must be in [0,15]")
        self._writeReg('CFG', 'DTHBIT<3:0>', value)

    #
    # NCO select
    #    

    @property
    def SEL(self):
        """
        Get the current value of SEL<3:0>
        """
        return self._readReg('CFG', 'SEL<3:0>')

    @SEL.setter
    def SEL(self, value):
        """
        Set the value of SEL<3:0>
        """
        if not (0 <= value <= 15):
            raise ValueError("SEL<3:0> value must be in [0,15]")
        self._writeReg('CFG', 'SEL<3:0>', value)

    #
    # Operator overloading for easy access NCO[index]=val
    #        

    def __getitem__(self, key):
        """
        Get the PHO of FCW, depending on selected mode
        """
        if key not in range(0, 16):
            raise ValueError("Index must be in [0,15]")
        if self.MODE == 0:
            # FCW
            hiWord, loWord = self.fcwDict[key]
            hiVal = self._readReg(hiWord, 'DATA<15:0>')
            loVal = self._readReg(loWord, 'DATA<15:0>')
            val = (hiVal << 16) + loVal
        else:
            # PHO
            regName = self.phoDict[key]
            val = self._readReg(regName, 'DATA<15:0>')
        return val

    def __setitem__(self, key, val):
        """
        Set the PHO of FCW, depending on selected mode
        """
        if key not in range(0, 16):
            raise ValueError("Index must be in [0,15]")
        if self.MODE == 0:
            # FCW
            hiWord, loWord = self.fcwDict[key]
            hiVal = (val >> 16) & 0xFFFF
            loVal = val & 0xFFFF
            self._writeReg(hiWord, 'DATA<15:0>', hiVal)
            self._writeReg(loWord, 'DATA<15:0>', loVal)
        else:
            # PHO
            regName = self.phoDict[key]
            self._writeReg(regName, 'DATA<15:0>', val)

    #
    # Operator overloading for readable representation of NCO configuration
    #

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        prevMAC = self.chip.MAC  # save the value of MAC
        self.chip.MAC = self.chip.getMACfromName(self.channel)  # set MAC to reduce the number SPI accesses
        mode = self.MODE
        sel = self.SEL
        ret = "NCO " + self.rxtx + " " + self.channel + "\n"
        ret += "MODE\t= " + str(mode) + "\n"
        ret += "DTHBIT\t= " + str(self.DTHBIT) + "\n"
        ret += "SEL\t= " + str(sel) + "\n"
        if mode == 0:
            # FCW
            ret += "PHO\t= " + self.intToHex(self.PHO) + "\n"
            for i in range(0, 16):
                if i == sel:
                    ret += "FCW[" + str(i) + "]\t= " + self.intToHex(self[i]) + " <- Selected\n"
                else:
                    ret += "FCW[" + str(i) + "]\t= " + self.intToHex(self[i]) + "\n"
        else:
            # PHO
            for i in range(0, 16):
                if i == sel:
                    ret += "PHO[" + str(i) + "]\t= " + self.intToHex(self[i]) + " <- Selected\n"
                else:
                    ret += "PHO[" + str(i) + "]\t= " + self.intToHex(self[i]) + "\n"
        self.chip.MAC = prevMAC  # restore previous value of MAC
        return ret[:-1]

        #

    # Convenience functions
    #

    def getFrequency(self, testSignal=False):
        """
        Returns a value of NCO clock frequency
        """
        chip = self.chip
        if self.rxtx == 'RX':
            # RX NCO, clock is reffered to ADC clock
            adcClock = chip.CGEN.getADCFrequency()
            channel = self.channel
            TSGFCW = chip.RxTSP[channel].TSGFCW
            if TSGFCW == 1:
                fDiv = 8
            else:
                fDiv = 4
            if not testSignal:
                fDiv = 1
            ncoClock = adcClock / fDiv
        else:
            # TX NCO, clock is reffered to DAC clock
            dacClock = chip.CGEN.getDACFrequency()
            channel = self.channel
            TSGFCW = chip.TxTSP[channel].TSGFCW
            if TSGFCW == 1:
                fDiv = 8
            else:
                fDiv = 4
            if not testSignal:
                fDiv = 1
            ncoClock = dacClock / fDiv
        return ncoClock

    def calcNCOValue(self, freq):
        ncoClk = self.getFrequency()
        ncoVal = int((2.0 ** 32) * (freq / ncoClk))
        return ncoVal

    def setNCOFrequency(self, ncoNum, freq):
        val = self.calcNCOValue(freq)
        hiWord, loWord = self.fcwDict[ncoNum]
        hiVal = (val >> 16) & 0xFFFF
        loVal = val & 0xFFFF
        self._writeReg(hiWord, 'DATA<15:0>', hiVal)
        self._writeReg(loWord, 'DATA<15:0>', loVal)
