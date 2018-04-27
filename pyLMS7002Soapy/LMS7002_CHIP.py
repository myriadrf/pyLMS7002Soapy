#***************************************************************
#* Name:      LMS7002_CHIP.py
#* Purpose:   Class implementing LMS7002 general functions
#* Author:    Lime Microsystems ()
#* Created:   2016-11-14
#* Copyright: Lime Microsystems (limemicro.com)
#* License:
#**************************************************************

from LMS7002_base import *

class LMS7002_CHIP(LMS7002_base):
    __slots__ = []    # Used to generate error on typos
    def __init__(self, chip):
        self.chip = chip
        self.channel = None
        self.prefix = ""
        
    def getChipInfo(self):
        """
        Get the chip info.
        Returns (VER, REV, MASK)
        """
        reg = self.chip['ChipVer']
        VER = reg['VER<4:0>']
        REV = reg['REV<4:0>']
        MASK = reg['MASK<5:0>']
        return (VER, REV, MASK)

            
    #
    # CHIPCFG (0x0020)
    #
    
    # LRST_TX_B
    @property 
    def LRST_TX_B(self):
        """
        Get the value of LRST_TX_B
        """
        return self._readReg('CHIPCFG', 'LRST_TX_B')

    @LRST_TX_B.setter
    def LRST_TX_B(self, value):
        """
        Set the value of LRST_TX_B
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CHIPCFG', 'LRST_TX_B', value)

    # MRST_TX_B
    @property 
    def MRST_TX_B(self):
        """
        Get the value of MRST_TX_B
        """
        return self._readReg('CHIPCFG', 'MRST_TX_B')

    @MRST_TX_B.setter
    def MRST_TX_B(self, value):
        """
        Set the value of MRST_TX_B
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CHIPCFG', 'MRST_TX_B', value)

    # LRST_TX_A
    @property 
    def LRST_TX_A(self):
        """
        Get the value of LRST_TX_A
        """
        return self._readReg('CHIPCFG', 'LRST_TX_A')

    @LRST_TX_A.setter
    def LRST_TX_A(self, value):
        """
        Set the value of LRST_TX_A
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CHIPCFG', 'LRST_TX_A', value)

    # MRST_TX_A
    @property 
    def MRST_TX_A(self):
        """
        Get the value of MRST_TX_A
        """
        return self._readReg('CHIPCFG', 'MRST_TX_A')

    @MRST_TX_A.setter
    def MRST_TX_A(self, value):
        """
        Set the value of MRST_TX_A
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CHIPCFG', 'MRST_TX_A', value)

    # LRST_RX_B
    @property 
    def LRST_RX_B(self):
        """
        Get the value of LRST_RX_B
        """
        return self._readReg('CHIPCFG', 'LRST_RX_B')

    @LRST_RX_B.setter
    def LRST_RX_B(self, value):
        """
        Set the value of LRST_RX_B
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CHIPCFG', 'LRST_RX_B', value)

    # MRST_RX_B
    @property 
    def MRST_RX_B(self):
        """
        Get the value of MRST_RX_B
        """
        return self._readReg('CHIPCFG', 'MRST_RX_B')

    @MRST_RX_B.setter
    def MRST_RX_B(self, value):
        """
        Set the value of MRST_RX_B
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CHIPCFG', 'MRST_RX_B', value)

    # LRST_RX_A
    @property 
    def LRST_RX_A(self):
        """
        Get the value of LRST_RX_A
        """
        return self._readReg('CHIPCFG', 'LRST_RX_A')

    @LRST_RX_A.setter
    def LRST_RX_A(self, value):
        """
        Set the value of LRST_RX_A
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CHIPCFG', 'LRST_RX_A', value)

    # MRST_RX_A
    @property 
    def MRST_RX_A(self):
        """
        Get the value of MRST_RX_A
        """
        return self._readReg('CHIPCFG', 'MRST_RX_A')

    @MRST_RX_A.setter
    def MRST_RX_A(self, value):
        """
        Set the value of MRST_RX_A
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CHIPCFG', 'MRST_RX_A', value)

    # SRST_RXFIFO
    @property 
    def SRST_RXFIFO(self):
        """
        Get the value of SRST_RXFIFO
        """
        return self._readReg('CHIPCFG', 'SRST_RXFIFO')

    @SRST_RXFIFO.setter
    def SRST_RXFIFO(self, value):
        """
        Set the value of SRST_RXFIFO
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CHIPCFG', 'SRST_RXFIFO', value)

    # SRST_TXFIFO
    @property 
    def SRST_TXFIFO(self):
        """
        Get the value of SRST_TXFIFO
        """
        return self._readReg('CHIPCFG', 'SRST_TXFIFO')

    @SRST_TXFIFO.setter
    def SRST_TXFIFO(self, value):
        """
        Set the value of SRST_TXFIFO
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CHIPCFG', 'SRST_TXFIFO', value)

    # RXEN_B
    @property 
    def RXEN_B(self):
        """
        Get the value of RXEN_B
        """
        return self._readReg('CHIPCFG', 'RXEN_B')

    @RXEN_B.setter
    def RXEN_B(self, value):
        """
        Set the value of RXEN_B
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CHIPCFG', 'RXEN_B', value)

    # RXEN_A
    @property 
    def RXEN_A(self):
        """
        Get the value of RXEN_A
        """
        return self._readReg('CHIPCFG', 'RXEN_A')

    @RXEN_A.setter
    def RXEN_A(self, value):
        """
        Set the value of RXEN_A
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CHIPCFG', 'RXEN_A', value)

    # TXEN_B
    @property 
    def TXEN_B(self):
        """
        Get the value of TXEN_B
        """
        return self._readReg('CHIPCFG', 'TXEN_B')

    @TXEN_B.setter
    def TXEN_B(self, value):
        """
        Set the value of TXEN_B
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CHIPCFG', 'TXEN_B', value)

    # TXEN_A
    @property 
    def TXEN_A(self):
        """
        Get the value of TXEN_A
        """
        return self._readReg('CHIPCFG', 'TXEN_A')

    @TXEN_A.setter
    def TXEN_A(self, value):
        """
        Set the value of TXEN_A
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CHIPCFG', 'TXEN_A', value)

    #
    # TSPCFG (0x002C)
    #

    # TXTSPCLKA_DIV<7:0>
    @property 
    def TXTSPCLKA_DIV(self):
        """
        Get the value of TXTSPCLKA_DIV<7:0>
        """
        return self._readReg('TSPCFG', 'TXTSPCLKA_DIV<7:0>')

    @TXTSPCLKA_DIV.setter
    def TXTSPCLKA_DIV(self, value):
        """
        Set the value of TXTSPCLKA_DIV<7:0>
        """
        if not(0<= value <=255):
            raise ValueError("Value must be [0..255]")
        self._writeReg('TSPCFG', 'TXTSPCLKA_DIV<7:0>', value)

    # RXTSPCLKA_DIV<7:0>
    @property 
    def RXTSPCLKA_DIV(self):
        """
        Get the value of RXTSPCLKA_DIV<7:0>
        """
        return self._readReg('TSPCFG', 'RXTSPCLKA_DIV<7:0>')

    @RXTSPCLKA_DIV.setter
    def RXTSPCLKA_DIV(self, value):
        """
        Set the value of RXTSPCLKA_DIV<7:0>
        """
        if not(0<= value <=255):
            raise ValueError("Value must be [0..255]")
        self._writeReg('TSPCFG', 'RXTSPCLKA_DIV<7:0>', value)


    #
    # EN_DIR (0x0081)
    #

    # TRX_GAIN_SRC
    @property 
    def TRX_GAIN_SRC(self):
        """
        Get the value of TRX_GAIN_SRC
        """
        if self.chip.chipID == self.chip.chipIDMR3:        
            return self._readReg('EN_DIR', 'TRX_GAIN_SRC')
        else:
            raise ValueError("Bitfield TRX_GAIN_SRC is not supported on chip version "+str(self.chip.chipID))

    @TRX_GAIN_SRC.setter
    def TRX_GAIN_SRC(self, value):
        """
        Set the value of TRX_GAIN_SRC
        """
        if self.chip.chipID == self.chip.chipIDMR3:
            if value not in [0, 1]:
                raise ValueError("Value must be [0,1]")
            self._writeReg('EN_DIR', 'TRX_GAIN_SRC', value)        
        else:
            raise ValueError("Bitfield TRX_GAIN_SRC is not supported on chip version "+str(self.chip.chipID))

    # EN_DIR_LDO
    @property 
    def EN_DIR_LDO(self):
        """
        Get the value of EN_DIR_LDO
        """
        return self._readReg('EN_DIR', 'EN_DIR_LDO')

    @EN_DIR_LDO.setter
    def EN_DIR_LDO(self, value):
        """
        Set the value of EN_DIR_LDO
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('EN_DIR', 'EN_DIR_LDO', value)

    # EN_DIR_CGEN
    @property 
    def EN_DIR_CGEN(self):
        """
        Get the value of EN_DIR_CGEN
        """
        return self._readReg('EN_DIR', 'EN_DIR_CGEN')

    @EN_DIR_CGEN.setter
    def EN_DIR_CGEN(self, value):
        """
        Set the value of EN_DIR_CGEN
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('EN_DIR', 'EN_DIR_CGEN', value)

    # EN_DIR_XBUF
    @property 
    def EN_DIR_XBUF(self):
        """
        Get the value of EN_DIR_XBUF
        """
        return self._readReg('EN_DIR', 'EN_DIR_XBUF')

    @EN_DIR_XBUF.setter
    def EN_DIR_XBUF(self, value):
        """
        Set the value of EN_DIR_XBUF
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('EN_DIR', 'EN_DIR_XBUF', value)

    # EN_DIR_AFE
    @property 
    def EN_DIR_AFE(self):
        """
        Get the value of EN_DIR_AFE
        """
        return self._readReg('EN_DIR', 'EN_DIR_AFE')

    @EN_DIR_AFE.setter
    def EN_DIR_AFE(self, value):
        """
        Set the value of EN_DIR_AFE
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('EN_DIR', 'EN_DIR_AFE', value)

    
    
