#***************************************************************
#* Name:      LMS7002_DCCAL.py
#* Purpose:   Class implementing LMS7002 DCCAL functions
#* Author:    Lime Microsystems ()
#* Created:   2017-02-10
#* Copyright: Lime Microsystems (limemicro.com)
#* License:
#**************************************************************

from LMS7002_base import *

class LMS7002_DCCAL(LMS7002_base):
    __slots__ = []  # Used to generate error on typos
    def __init__(self, chip):
        self.chip = chip
        self.channel = None
        self.prefix = "DCCAL_"
        
    #
    # DCCAL_CFG (0x05C0)
    #

    # DCMODE
    @property 
    def DCMODE(self):
        """
        Get the value of DCMODE
        """
        if self.chip.chipID == self.chip.chipIDMR3:
            return self._readReg('CFG', 'DCMODE')
        else:
            raise ValueError("Bitfield DCMODE is not supported on chip version "+str(self.chip.chipID))


    @DCMODE.setter
    def DCMODE(self, value):
        """
        Set the value of DCMODE
        """
        if self.chip.chipID == self.chip.chipIDMR3:
            if value not in [0, 1, 'MANUAL', 'AUTO']:
                raise ValueError("Value must be [0,1,'MANUAL','AUTO']")
            if value==0 or value=='MANUAL':
                val = 0
            else:
                val = 1
            self._writeReg('CFG', 'DCMODE', val)
        else:
            raise ValueError("Bitfield DCMODE is not supported on chip version "+str(self.chip.chipID))

    # PD_DCDAC_RXB
    @property 
    def PD_DCDAC_RXB(self):
        """
        Get the value of PD_DCDAC_RXB
        """
        if self.chip.chipID == self.chip.chipIDMR3:
            return self._readReg('CFG', 'PD_DCDAC_RXB')
        else:
            raise ValueError("Bitfield PD_DCDAC_RXB is not supported on chip version "+str(self.chip.chipID))


    @PD_DCDAC_RXB.setter
    def PD_DCDAC_RXB(self, value):
        """
        Set the value of PD_DCDAC_RXB
        """
        if self.chip.chipID == self.chip.chipIDMR3:
            if value not in [0, 1]:
                raise ValueError("Value must be [0,1]")
            self._writeReg('CFG', 'PD_DCDAC_RXB', value)
        else:
            raise ValueError("Bitfield PD_DCDAC_RXB is not supported on chip version "+str(self.chip.chipID))

    # PD_DCDAC_RXA
    @property 
    def PD_DCDAC_RXA(self):
        """
        Get the value of PD_DCDAC_RXA
        """
        if self.chip.chipID == self.chip.chipIDMR3:
            return self._readReg('CFG', 'PD_DCDAC_RXA')
        else:
            raise ValueError("Bitfield PD_DCDAC_RXA is not supported on chip version "+str(self.chip.chipID))


    @PD_DCDAC_RXA.setter
    def PD_DCDAC_RXA(self, value):
        """
        Set the value of PD_DCDAC_RXA
        """
        if self.chip.chipID == self.chip.chipIDMR3:
            if value not in [0, 1]:
                raise ValueError("Value must be [0,1]")
            self._writeReg('CFG', 'PD_DCDAC_RXA', value)
        else:
            raise ValueError("Bitfield PD_DCDAC_RXA is not supported on chip version "+str(self.chip.chipID))

    # PD_DCDAC_TXB
    @property 
    def PD_DCDAC_TXB(self):
        """
        Get the value of PD_DCDAC_TXB
        """
        if self.chip.chipID == self.chip.chipIDMR3:
            return self._readReg('CFG', 'PD_DCDAC_TXB')
        else:
            raise ValueError("Bitfield PD_DCDAC_TXB is not supported on chip version "+str(self.chip.chipID))


    @PD_DCDAC_TXB.setter
    def PD_DCDAC_TXB(self, value):
        """
        Set the value of PD_DCDAC_TXB
        """
        if self.chip.chipID == self.chip.chipIDMR3:
            if value not in [0, 1]:
                raise ValueError("Value must be [0,1]")
            self._writeReg('CFG', 'PD_DCDAC_TXB', value)
        else:
            raise ValueError("Bitfield PD_DCDAC_TXB is not supported on chip version "+str(self.chip.chipID))

    # PD_DCDAC_TXA
    @property 
    def PD_DCDAC_TXA(self):
        """
        Get the value of PD_DCDAC_TXA
        """
        if self.chip.chipID == self.chip.chipIDMR3:
            return self._readReg('CFG', 'PD_DCDAC_TXA')
        else:
            raise ValueError("Bitfield PD_DCDAC_TXA is not supported on chip version "+str(self.chip.chipID))


    @PD_DCDAC_TXA.setter
    def PD_DCDAC_TXA(self, value):
        """
        Set the value of PD_DCDAC_TXA
        """
        if self.chip.chipID == self.chip.chipIDMR3:
            if value not in [0, 1]:
                raise ValueError("Value must be [0,1]")
            self._writeReg('CFG', 'PD_DCDAC_TXA', value)
        else:
            raise ValueError("Bitfield PD_DCDAC_TXA is not supported on chip version "+str(self.chip.chipID))

    # PD_DCCMP_RXB
    @property 
    def PD_DCCMP_RXB(self):
        """
        Get the value of PD_DCCMP_RXB
        """
        if self.chip.chipID == self.chip.chipIDMR3:
            return self._readReg('CFG', 'PD_DCCMP_RXB')
        else:
            raise ValueError("Bitfield PD_DCCMP_RXB is not supported on chip version "+str(self.chip.chipID))


    @PD_DCCMP_RXB.setter
    def PD_DCCMP_RXB(self, value):
        """
        Set the value of PD_DCCMP_RXB
        """
        if self.chip.chipID == self.chip.chipIDMR3:
            if value not in [0, 1]:
                raise ValueError("Value must be [0,1]")
            self._writeReg('CFG', 'PD_DCCMP_RXB', value)
        else:
            raise ValueError("Bitfield PD_DCCMP_RXB is not supported on chip version "+str(self.chip.chipID))

    # PD_DCCMP_RXA
    @property 
    def PD_DCCMP_RXA(self):
        """
        Get the value of PD_DCCMP_RXA
        """
        if self.chip.chipID == self.chip.chipIDMR3:
            return self._readReg('CFG', 'PD_DCCMP_RXA')
        else:
            raise ValueError("Bitfield PD_DCCMP_RXA is not supported on chip version "+str(self.chip.chipID))


    @PD_DCCMP_RXA.setter
    def PD_DCCMP_RXA(self, value):
        """
        Set the value of PD_DCCMP_RXA
        """
        if self.chip.chipID == self.chip.chipIDMR3:
            if value not in [0, 1]:
                raise ValueError("Value must be [0,1]")
            self._writeReg('CFG', 'PD_DCCMP_RXA', value)
        else:
            raise ValueError("Bitfield PD_DCCMP_RXA is not supported on chip version "+str(self.chip.chipID))

    # PD_DCCMP_TXB
    @property 
    def PD_DCCMP_TXB(self):
        """
        Get the value of PD_DCCMP_TXB
        """
        if self.chip.chipID == self.chip.chipIDMR3:
            return self._readReg('CFG', 'PD_DCCMP_TXB')
        else:
            raise ValueError("Bitfield PD_DCCMP_TXB is not supported on chip version "+str(self.chip.chipID))


    @PD_DCCMP_TXB.setter
    def PD_DCCMP_TXB(self, value):
        """
        Set the value of PD_DCCMP_TXB
        """
        if self.chip.chipID == self.chip.chipIDMR3:
            if value not in [0, 1]:
                raise ValueError("Value must be [0,1]")
            self._writeReg('CFG', 'PD_DCCMP_TXB', value)
        else:
            raise ValueError("Bitfield PD_DCCMP_TXB is not supported on chip version "+str(self.chip.chipID))

    # PD_DCCMP_TXA
    @property 
    def PD_DCCMP_TXA(self):
        """
        Get the value of PD_DCCMP_TXA
        """
        if self.chip.chipID == self.chip.chipIDMR3:
            return self._readReg('CFG', 'PD_DCCMP_TXA')
        else:
            raise ValueError("Bitfield PD_DCCMP_TXA is not supported on chip version "+str(self.chip.chipID))


    @PD_DCCMP_TXA.setter
    def PD_DCCMP_TXA(self, value):
        """
        Set the value of PD_DCCMP_TXA
        """
        if self.chip.chipID == self.chip.chipIDMR3:
            if value not in [0, 1]:
                raise ValueError("Value must be [0,1]")
            self._writeReg('CFG', 'PD_DCCMP_TXA', value)
        else:
            raise ValueError("Bitfield PD_DCCMP_TXA is not supported on chip version "+str(self.chip.chipID))


    #
    # DCCAL_STAT (0x05C1)
    #

    # DCCAL_CALSTATUS<7:0>
    @property 
    def DCCAL_CALSTATUS(self):
        """
        Get the value of DCCAL_CALSTATUS<7:0>
        """
        if self.chip.chipID == self.chip.chipIDMR3:
            return self._readReg('STAT', 'DCCAL_CALSTATUS<7:0>')
        else:
            raise ValueError("Bitfield DCCAL_CALSTATUS<7:0> is not supported on chip version "+str(self.chip.chipID))

    @DCCAL_CALSTATUS.setter
    def DCCAL_CALSTATUS(self, value):
        """
        Set the value of DCCAL_CALSTATUS<7:0>
        """
        if self.chip.chipID == self.chip.chipIDMR3:        
            if not(0<= value <=255):
                raise ValueError("Value must be [0..255]")
            self._writeReg('STAT', 'DCCAL_CALSTATUS<7:0>', value)
        else:
            raise ValueError("Bitfield DCCAL_CALSTATUS<7:0> is not supported on chip version "+str(self.chip.chipID))

    # DCCAL_CMPSTATUS<7:0>
    @property 
    def DCCAL_CMPSTATUS(self):
        """
        Get the value of DCCAL_CMPSTATUS<7:0>
        """
        if self.chip.chipID == self.chip.chipIDMR3:
            return self._readReg('STAT', 'DCCAL_CMPSTATUS<7:0>')
        else:
            raise ValueError("Bitfield DCCAL_CMPSTATUS<7:0> is not supported on chip version "+str(self.chip.chipID))

    @DCCAL_CMPSTATUS.setter
    def DCCAL_CMPSTATUS(self, value):
        """
        Set the value of DCCAL_CMPSTATUS<7:0>
        """
        if self.chip.chipID == self.chip.chipIDMR3:        
            if not(0<= value <=255):
                raise ValueError("Value must be [0..255]")
            self._writeReg('STAT', 'DCCAL_CMPSTATUS<7:0>', value)
        else:
            raise ValueError("Bitfield DCCAL_CMPSTATUS<7:0> is not supported on chip version "+str(self.chip.chipID))

    #
    # DCCAL_CFG2 (0x05C2)
    #

    # DCCAL_CMPCFG<7:0>
    @property 
    def DCCAL_CMPCFG(self):
        """
        Get the value of DCCAL_CMPCFG<7:0>
        """
        if self.chip.chipID == self.chip.chipIDMR3:
            return self._readReg('CFG2', 'DCCAL_CMPCFG<7:0>')
        else:
            raise ValueError("Bitfield DCCAL_CMPCFG<7:0> is not supported on chip version "+str(self.chip.chipID))

    @DCCAL_CMPCFG.setter
    def DCCAL_CMPCFG(self, value):
        """
        Set the value of DCCAL_CMPCFG<7:0>
        """
        if self.chip.chipID == self.chip.chipIDMR3:        
            if not(0<= value <=255):
                raise ValueError("Value must be [0..255]")
            self._writeReg('CFG2', 'DCCAL_CMPCFG<7:0>', value)
        else:
            raise ValueError("Bitfield DCCAL_CMPCFG<7:0> is not supported on chip version "+str(self.chip.chipID))

    # DCCAL_START<7:0>
    @property 
    def DCCAL_START(self):
        """
        Get the value of DCCAL_START<7:0>
        """
        if self.chip.chipID == self.chip.chipIDMR3:
            return self._readReg('CFG2', 'DCCAL_START<7:0>')
        else:
            raise ValueError("Bitfield DCCAL_START<7:0> is not supported on chip version "+str(self.chip.chipID))

    @DCCAL_START.setter
    def DCCAL_START(self, value):
        """
        Set the value of DCCAL_START<7:0>
        """
        if self.chip.chipID == self.chip.chipIDMR3:        
            if not(0<= value <=255):
                raise ValueError("Value must be [0..255]")
            self._writeReg('CFG2', 'DCCAL_START<7:0>', value)
        else:
            raise ValueError("Bitfield DCCAL_START<7:0> is not supported on chip version "+str(self.chip.chipID))

    def startRXBQ(self):
        """
        Starts RXBQ calibration.
        """
        self.DCCAL_START = 0
        self.DCCAL_START = 1<<7
        self.DCCAL_START = 0
        
    def startRXBI(self):
        """
        Starts RXBI calibration.
        """
        self.DCCAL_START = 0
        self.DCCAL_START = 1<<6
        self.DCCAL_START = 0

    def startRXAQ(self):
        """
        Starts RXAQ calibration.
        """
        self.DCCAL_START = 0
        self.DCCAL_START = 1<<5
        self.DCCAL_START = 0

    def startRXAI(self):
        """
        Starts RXAI calibration.
        """
        self.DCCAL_START = 0
        self.DCCAL_START = 1<<4
        self.DCCAL_START = 0
        
    def startTXBQ(self):
        """
        Starts TXBQ calibration.
        """
        self.DCCAL_START = 0
        self.DCCAL_START = 1<<3
        self.DCCAL_START = 0

    def startTXBI(self):
        """
        Starts TXBI calibration.
        """
        self.DCCAL_START = 0
        self.DCCAL_START = 1<<2
        self.DCCAL_START = 0

    def startTXAQ(self):
        """
        Starts TXAQ calibration.
        """
        self.DCCAL_START = 0
        self.DCCAL_START = 1<<1
        self.DCCAL_START = 0
        
    def startTXAI(self):
        """
        Starts TXAI calibration.
        """
        self.DCCAL_START = 0
        self.DCCAL_START = 1
        self.DCCAL_START = 0

    #
    # DCCAL_TXAI (0x05C3)
    #  

    @property 
    def DC_TXAI(self):
        """
        Get the value of DC_TXAI
        """
        if self.chip.chipID == self.chip.chipIDMR3:
            self._writeReg('TXAI', 'DCRD_TXAI', 0)
            self._writeReg('TXAI', 'DCRD_TXAI', 1)
            self._writeReg('TXAI', 'DCRD_TXAI', 0)            
            val = self._readReg('TXAI', 'DC_TXAI<10:0>')
            return self.signMagnitudeToInt(val, 11)
        else:
            raise ValueError("Bitfield DC_TXAI is not supported on chip version "+str(self.chip.chipID))

    @DC_TXAI.setter
    def DC_TXAI(self, value):
        """
        Set the value of DC_TXAI
        """
        if self.chip.chipID == self.chip.chipIDMR3:        
            if not(-1024<= value <=1024):
                raise ValueError("Value must be [-1024..1024]")
            val = self.intToSignMagnitude(value, 11)
            self._writeReg('TXAI', 'DC_TXAI<10:0>', val)
            self._writeReg('TXAI', 'DCWR_TXAI', 0)
            self._writeReg('TXAI', 'DCWR_TXAI', 1)
            self._writeReg('TXAI', 'DCWR_TXAI', 0)
        else:
            raise ValueError("Bitfield TXAI is not supported on chip version "+str(self.chip.chipID))

    #
    # DCCAL_TXAQ (0x05C4)
    #  

    @property 
    def DC_TXAQ(self):
        """
        Get the value of DC_TXAQ
        """
        if self.chip.chipID == self.chip.chipIDMR3:
            self._writeReg('TXAQ', 'DCRD_TXAQ', 0)
            self._writeReg('TXAQ', 'DCRD_TXAQ', 1)
            self._writeReg('TXAQ', 'DCRD_TXAQ', 0)            
            val = self._readReg('TXAQ', 'DC_TXAQ<10:0>')
            return self.signMagnitudeToInt(val, 11)
        else:
            raise ValueError("Bitfield DC_TXAQ is not supported on chip version "+str(self.chip.chipID))

    @DC_TXAQ.setter
    def DC_TXAQ(self, value):
        """
        Set the value of DC_TXAQ
        """
        if self.chip.chipID == self.chip.chipIDMR3:        
            if not(-1024<= value <=1024):
                raise ValueError("Value must be [-1024..1024]")
            val = self.intToSignMagnitude(value, 11)
            self._writeReg('TXAQ', 'DC_TXAQ<10:0>', val)
            self._writeReg('TXAQ', 'DCWR_TXAQ', 0)
            self._writeReg('TXAQ', 'DCWR_TXAQ', 1)
            self._writeReg('TXAQ', 'DCWR_TXAQ', 0)            
        else:
            raise ValueError("Bitfield TXAQ is not supported on chip version "+str(self.chip.chipID))
                                                                                        
    #
    # DCCAL_TXBI (0x05C5)
    #  

    @property 
    def DC_TXBI(self):
        """
        Get the value of DC_TXBI
        """
        if self.chip.chipID == self.chip.chipIDMR3:
            self._writeReg('TXBI', 'DCRD_TXBI', 0)
            self._writeReg('TXBI', 'DCRD_TXBI', 1)
            self._writeReg('TXBI', 'DCRD_TXBI', 0)            
            val = self._readReg('TXBI', 'DC_TXBI<10:0>')
            return self.signMagnitudeToInt(val, 11)
        else:
            raise ValueError("Bitfield DC_TXBI is not supported on chip version "+str(self.chip.chipID))

    @DC_TXBI.setter
    def DC_TXBI(self, value):
        """
        Set the value of DC_TXBI
        """
        if self.chip.chipID == self.chip.chipIDMR3:        
            if not(-1024<= value <=1024):
                raise ValueError("Value must be [-1024..1024]")
            val = self.intToSignMagnitude(value, 11)
            self._writeReg('TXBI', 'DC_TXBI<10:0>', val)
            self._writeReg('TXBI', 'DCWR_TXBI', 0)
            self._writeReg('TXBI', 'DCWR_TXBI', 1)
            self._writeReg('TXBI', 'DCWR_TXBI', 0)            
        else:
            raise ValueError("Bitfield TXBI is not supported on chip version "+str(self.chip.chipID))

    #
    # DCCAL_TXBQ (0x05C6)
    #  

    @property 
    def DC_TXBQ(self):
        """
        Get the value of DC_TXBQ
        """
        if self.chip.chipID == self.chip.chipIDMR3:
            self._writeReg('TXBQ', 'DCRD_TXBQ', 0)
            self._writeReg('TXBQ', 'DCRD_TXBQ', 1)
            self._writeReg('TXBQ', 'DCRD_TXBQ', 0)            
            val = self._readReg('TXBQ', 'DC_TXBQ<10:0>')
            return self.signMagnitudeToInt(val, 11)
        else:
            raise ValueError("Bitfield DC_TXBQ is not supported on chip version "+str(self.chip.chipID))

    @DC_TXBQ.setter
    def DC_TXBQ(self, value):
        """
        Set the value of DC_TXBQ
        """
        if self.chip.chipID == self.chip.chipIDMR3:        
            if not(-1024<= value <=1024):
                raise ValueError("Value must be [-1024..1024]")
            val = self.intToSignMagnitude(value, 11)
            self._writeReg('TXBQ', 'DC_TXBQ<10:0>', val)
            self._writeReg('TXBQ', 'DCWR_TXBQ', 0)
            self._writeReg('TXBQ', 'DCWR_TXBQ', 1)
            self._writeReg('TXBQ', 'DCWR_TXBQ', 0)            
        else:
            raise ValueError("Bitfield TXBQ is not supported on chip version "+str(self.chip.chipID))
            
    #
    # DCCAL_RXAI (0x05C7)
    #  

    @property 
    def DC_RXAI(self):
        """
        Get the value of DC_RXAI
        """
        if self.chip.chipID == self.chip.chipIDMR3:
            self._writeReg('RXAI', 'DCRD_RXAI', 0)
            self._writeReg('RXAI', 'DCRD_RXAI', 1)
            self._writeReg('RXAI', 'DCRD_RXAI', 0)            
            val = self._readReg('RXAI', 'DC_RXAI<6:0>')
            return self.signMagnitudeToInt(val, 7)
        else:
            raise ValueError("Bitfield DC_RXAI is not supported on chip version "+str(self.chip.chipID))

    @DC_RXAI.setter
    def DC_RXAI(self, value):
        """
        Set the value of DC_RXAI
        """
        if self.chip.chipID == self.chip.chipIDMR3:        
            if not(-63<= value <=63):
                raise ValueError("Value must be [-63..63]")
            val = self.intToSignMagnitude(value, 7)
            self._writeReg('RXAI', 'DC_RXAI<6:0>', val)
            self._writeReg('RXAI', 'DCWR_RXAI', 0)
            self._writeReg('RXAI', 'DCWR_RXAI', 1)
            self._writeReg('RXAI', 'DCWR_RXAI', 0)            
        else:
            raise ValueError("Bitfield RXAI is not supported on chip version "+str(self.chip.chipID))
            
    #
    # DCCAL_RXAQ (0x05C8)
    #  

    @property 
    def DC_RXAQ(self):
        """
        Get the value of DC_RXAQ
        """
        if self.chip.chipID == self.chip.chipIDMR3:
            self._writeReg('RXAQ', 'DCRD_RXAQ', 0)
            self._writeReg('RXAQ', 'DCRD_RXAQ', 1)
            self._writeReg('RXAQ', 'DCRD_RXAQ', 0)            
            val = self._readReg('RXAQ', 'DC_RXAQ<6:0>')
            return self.signMagnitudeToInt(val, 7)
        else:
            raise ValueError("Bitfield DC_RXAQ is not supported on chip version "+str(self.chip.chipID))

    @DC_RXAQ.setter
    def DC_RXAQ(self, value):
        """
        Set the value of DC_RXAQ
        """
        if self.chip.chipID == self.chip.chipIDMR3:        
            if not(-63<= value <=63):
                raise ValueError("Value must be [-63..63]")
            val = self.intToSignMagnitude(value, 7)
            self._writeReg('RXAQ', 'DC_RXAQ<6:0>', val)
            self._writeReg('RXAQ', 'DCWR_RXAQ', 0)
            self._writeReg('RXAQ', 'DCWR_RXAQ', 1)
            self._writeReg('RXAQ', 'DCWR_RXAQ', 0)            
        else:
            raise ValueError("Bitfield RXAQ is not supported on chip version "+str(self.chip.chipID))
            
    #
    # DCCAL_RXBI (0x05C9)
    #  

    @property 
    def DC_RXBI(self):
        """
        Get the value of DC_RXBI
        """
        if self.chip.chipID == self.chip.chipIDMR3:
            self._writeReg('RXBI', 'DCRD_RXBI', 0)
            self._writeReg('RXBI', 'DCRD_RXBI', 1)
            self._writeReg('RXBI', 'DCRD_RXBI', 0)            
            val = self._readReg('RXBI', 'DC_RXBI<6:0>')
            return self.signMagnitudeToInt(val, 7)
        else:
            raise ValueError("Bitfield DC_RXBI is not supported on chip version "+str(self.chip.chipID))

    @DC_RXBI.setter
    def DC_RXBI(self, value):
        """
        Set the value of DC_RXBI
        """
        if self.chip.chipID == self.chip.chipIDMR3:        
            if not(-63<= value <=63):
                raise ValueError("Value must be [-63..63]")
            val = self.intToSignMagnitude(value, 7)
            self._writeReg('RXBI', 'DC_RXBI<6:0>', val)
            self._writeReg('RXBI', 'DCWR_RXBI', 0)
            self._writeReg('RXBI', 'DCWR_RXBI', 1)
            self._writeReg('RXBI', 'DCWR_RXBI', 0)            
        else:
            raise ValueError("Bitfield RXBI is not supported on chip version "+str(self.chip.chipID))
            
    #
    # DCCAL_RXBQ (0x05CA)
    #  

    @property 
    def DC_RXBQ(self):
        """
        Get the value of DC_RXBQ
        """
        if self.chip.chipID == self.chip.chipIDMR3:
            self._writeReg('RXBQ', 'DCRD_RXBQ', 0)
            self._writeReg('RXBQ', 'DCRD_RXBQ', 1)
            self._writeReg('RXBQ', 'DCRD_RXBQ', 0)            
            val = self._readReg('RXBQ', 'DC_RXBQ<6:0>')
            return self.signMagnitudeToInt(val, 7)
        else:
            raise ValueError("Bitfield DC_RXBQ is not supported on chip version "+str(self.chip.chipID))

    @DC_RXBQ.setter
    def DC_RXBQ(self, value):
        """
        Set the value of DC_RXBQ
        """
        if self.chip.chipID == self.chip.chipIDMR3:        
            if not(-63<= value <=63):
                raise ValueError("Value must be [-63..63]")
            val = self.intToSignMagnitude(value, 7)
            self._writeReg('RXBQ', 'DC_RXBQ<6:0>', val)
            self._writeReg('RXBQ', 'DCWR_RXBQ', 0)
            self._writeReg('RXBQ', 'DCWR_RXBQ', 1)
            self._writeReg('RXBQ', 'DCWR_RXBQ', 0)            
        else:
            raise ValueError("Bitfield RXBQ is not supported on chip version "+str(self.chip.chipID))

    # DC_RXCDIV<7:0>
    @property 
    def DC_RXCDIV(self):
        """
        Get the value of DC_RXCDIV<7:0>
        """
        if self.chip.chipID == self.chip.chipIDMR3:
            return self._readReg('CLKDIV', 'DC_RXCDIV<7:0>')
        else:
            raise ValueError("Bitfield DC_RXCDIV<7:0> is not supported on chip version "+str(self.chip.chipID))


    @DC_RXCDIV.setter
    def DC_RXCDIV(self, value):
        """
        Set the value of DC_RXCDIV<7:0>
        """
        if self.chip.chipID == self.chip.chipIDMR3:        
            if not(0<= value <=255):
                raise ValueError("Value must be [0..255]")
            self._writeReg('CLKDIV', 'DC_RXCDIV<7:0>', value)
        else:
            raise ValueError("Bitfield DC_RXCDIV<7:0> is not supported on chip version "+str(self.chip.chipID))

    # DC_TXCDIV<7:0>
    @property 
    def DC_TXCDIV(self):
        """
        Get the value of DC_TXCDIV<7:0>
        """
        if self.chip.chipID == self.chip.chipIDMR3:
            return self._readReg('CLKDIV', 'DC_TXCDIV<7:0>')
        else:
            raise ValueError("Bitfield DC_TXCDIV<7:0> is not supported on chip version "+str(self.chip.chipID))


    @DC_TXCDIV.setter
    def DC_TXCDIV(self, value):
        """
        Set the value of DC_TXCDIV<7:0>
        """
        if self.chip.chipID == self.chip.chipIDMR3:        
            if not(0<= value <=255):
                raise ValueError("Value must be [0..255]")
            self._writeReg('CLKDIV', 'DC_TXCDIV<7:0>', value)
        else:
            raise ValueError("Bitfield DC_TXCDIV<7:0> is not supported on chip version "+str(self.chip.chipID))

    # HYSCMP_RXB<2:0>
    @property 
    def HYSCMP_RXB(self):
        """
        Get the value of HYSCMP_RXB<2:0>
        """
        if self.chip.chipID == self.chip.chipIDMR3:        
            return self._readReg('HYSTCFG', 'HYSCMP_RXB<2:0>')
        else:
            raise ValueError("Bitfield HYSCMP_RXB<2:0> is not supported on chip version "+str(self.chip.chipID))
            

    @HYSCMP_RXB.setter
    def HYSCMP_RXB(self, value):
        """
        Set the value of HYSCMP_RXB<2:0>
        """
        if self.chip.chipID == self.chip.chipIDMR3:
            if not(0 <= value <= 7):
                raise ValueError("Value must be [0..7]")
            self._writeReg('HYSTCFG', 'HYSCMP_RXB<2:0>', value)
        else:
            raise ValueError("Bitfield HYSCMP_RXB<2:0> is not supported on chip version "+str(self.chip.chipID))

    # HYSCMP_RXA<2:0>
    @property 
    def HYSCMP_RXA(self):
        """
        Get the value of HYSCMP_RXA<2:0>
        """
        if self.chip.chipID == self.chip.chipIDMR3:        
            return self._readReg('HYSTCFG', 'HYSCMP_RXA<2:0>')
        else:
            raise ValueError("Bitfield HYSCMP_RXA<2:0> is not supported on chip version "+str(self.chip.chipID))
            

    @HYSCMP_RXA.setter
    def HYSCMP_RXA(self, value):
        """
        Set the value of HYSCMP_RXA<2:0>
        """
        if self.chip.chipID == self.chip.chipIDMR3:
            if not(0 <= value <= 7):
                raise ValueError("Value must be [0..7]")
            self._writeReg('HYSTCFG', 'HYSCMP_RXA<2:0>', value)
        else:
            raise ValueError("Bitfield HYSCMP_RXA<2:0> is not supported on chip version "+str(self.chip.chipID))

    # HYSCMP_TXB<2:0>
    @property 
    def HYSCMP_TXB(self):
        """
        Get the value of HYSCMP_TXB<2:0>
        """
        if self.chip.chipID == self.chip.chipIDMR3:        
            return self._readReg('HYSTCFG', 'HYSCMP_TXB<2:0>')
        else:
            raise ValueError("Bitfield HYSCMP_TXB<2:0> is not supported on chip version "+str(self.chip.chipID))
            

    @HYSCMP_TXB.setter
    def HYSCMP_TXB(self, value):
        """
        Set the value of HYSCMP_TXB<2:0>
        """
        if self.chip.chipID == self.chip.chipIDMR3:
            if not(0 <= value <= 7):
                raise ValueError("Value must be [0..7]")
            self._writeReg('HYSTCFG', 'HYSCMP_TXB<2:0>', value)
        else:
            raise ValueError("Bitfield HYSCMP_TXB<2:0> is not supported on chip version "+str(self.chip.chipID))

    # HYSCMP_TXA<2:0>
    @property 
    def HYSCMP_TXA(self):
        """
        Get the value of HYSCMP_TXA<2:0>
        """
        if self.chip.chipID == self.chip.chipIDMR3:        
            return self._readReg('HYSTCFG', 'HYSCMP_TXA<2:0>')
        else:
            raise ValueError("Bitfield HYSCMP_TXA<2:0> is not supported on chip version "+str(self.chip.chipID))
            

    @HYSCMP_TXA.setter
    def HYSCMP_TXA(self, value):
        """
        Set the value of HYSCMP_TXA<2:0>
        """
        if self.chip.chipID == self.chip.chipIDMR3:
            if not(0 <= value <= 7):
                raise ValueError("Value must be [0..7]")
            self._writeReg('HYSTCFG', 'HYSCMP_TXA<2:0>', value)
        else:
            raise ValueError("Bitfield HYSCMP_TXA<2:0> is not supported on chip version "+str(self.chip.chipID))
                                                                        

