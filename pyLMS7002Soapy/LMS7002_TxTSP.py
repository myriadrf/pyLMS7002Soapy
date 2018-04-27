#***************************************************************
#* Name:      LMS7002_TxTSP.py
#* Purpose:   Class implementing LMS7002 TxTSP functions
#* Author:    Lime Microsystems ()
#* Created:   2016-11-14
#* Copyright: Lime Microsystems (limemicro.com)
#* License:
#**************************************************************

from LMS7002_base import *

class LMS7002_TxTSP(LMS7002_base):
    __slots__ = []    # Used to generate error on typos
    def __init__(self, chip, Channel):
        if Channel not in ['A', 'B']:
            raise ValueError("Parameter Channel must be 'A' or 'B'")
        self.chip = chip
        self.channel = Channel
        self.prefix = "TXTSP_"

    #
    # TXTSP_CFG (0x0200) 
    #

    # TSGFC
    @property 
    def TSGFC(self):
        """
        Get the value of TSGFC
        """
        return self._readReg('CFG', 'TSGFC')

    @TSGFC.setter
    def TSGFC(self, value):
        """
        Set the value of TSGFC
        """
        if value not in [0,1, '-6dB', 'FULL']:
            raise ValueError("Value must be [0,1, '-6dB', 'FULL']")
        if value==0 or value=='-6dB':
            val = 0
        else:
            val = 1    
        self._writeReg('CFG', 'TSGFC', val)

    # TSGFCW
    @property 
    def TSGFCW(self):
        """
        Get the value of TSGFCW
        """
        return self._readReg('CFG', 'TSGFCW<1:0>')

    @TSGFCW.setter
    def TSGFCW(self, value):
        """
        Set the value of TSGFCW
        """
        if value not in [1,2, 'CLK/8', 'CLK/4']:
            raise ValueError("Value must be [1,2, 'CLK/8', 'CLK/4']")
        if value==1 or value=='CLK/8':
            val = 1
        else:
            val = 2    
        self._writeReg('CFG', 'TSGFCW<1:0>', val)

    # TSGDCLDQ
    @property 
    def TSGDCLDQ(self):
        """
        Get the value of TSGDCLDQ
        """
        return self._readReg('CFG', 'TSGDCLDQ')

    @TSGDCLDQ.setter
    def TSGDCLDQ(self, value):
        """
        Set the value of TSGDCLDQ
        """
        if value not in [0,1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG', 'TSGDCLDQ', value)

    # TSGDCLDI
    @property 
    def TSGDCLDI(self):
        """
        Get the value of TSGDCLDI
        """
        return self._readReg('CFG', 'TSGDCLDI')

    @TSGDCLDI.setter
    def TSGDCLDI(self, value):
        """
        Set the value of TSGDCLDI
        """
        if value not in [0,1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG', 'TSGDCLDI', value)

    # TSGSWAPIQ
    @property 
    def TSGSWAPIQ(self):
        """
        Get the value of TSGSWAPIQ
        """
        return self._readReg('CFG', 'TSGSWAPIQ')

    @TSGSWAPIQ.setter
    def TSGSWAPIQ(self, value):
        """
        Set the value of TSGSWAPIQ
        """
        if value not in [0,1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG', 'TSGSWAPIQ', value)

    # TSGMODE
    @property 
    def TSGMODE(self):
        """
        Get the value of TSGMODE
        """
        return self._readReg('CFG', 'TSGMODE')

    @TSGMODE.setter
    def TSGMODE(self, value):
        """
        Set the value of TSGMODE
        """
        if value not in [0,1, 'NCO', 'DC']:
            raise ValueError("Value must be [0,1, 'NCO', 'DC']")
        if value==0 or value=='NCO':
            val = 0
        else:
            val = 1    
        self._writeReg('CFG', 'TSGMODE', val)

    # INSEL
    @property 
    def INSEL(self):
        """
        Get the value of INSEL
        """
        return self._readReg('CFG', 'INSEL')

    @INSEL.setter
    def INSEL(self, value):
        """
        Set the value of INSEL
        """
        if value not in [0,1, 'LML', 'TEST']:
            raise ValueError("Value must be [0,1, 'LML', 'TEST']")
        if value==0 or value=='LML':
            val = 0
        else:
            val = 1    
        self._writeReg('CFG', 'INSEL', val)

    # EN
    @property 
    def EN(self):
        """
        Get the value of EN
        """
        return self._readReg('CFG', 'EN')

    @EN.setter
    def EN(self, value):
        """
        Set the value of EN
        """
        if value not in [0,1, 'OFF', 'ON']:
            raise ValueError("Value must be [0,1, 'OFF', 'ON']")
        if value==0 or value=='OFF':
            val = 0
        else:
            val = 1    
        self._writeReg('CFG', 'EN', val)

    #
    # TXTSP_GCORRQ (0x0201) GCORRQ<10:0>
    #
    @property 
    def GCORRQ(self):
        """
        Get the value of GCORRQ
        """
        return self._readReg('GCORRQ', 'GCORRQ<10:0>')

    @GCORRQ.setter
    def GCORRQ(self, value):
        """
        Set the value of GCORRQ
        """
        if not(0 <= value <= 2047):
            raise ValueError("Value must be [0..2047]")
        self._writeReg('GCORRQ', 'GCORRQ<10:0>', value)

    #
    # TXTSP_GCORRI (0x0202) GCORRI<10:0>
    #
    @property 
    def GCORRI(self):
        """
        Get the value of GCORRI
        """
        return self._readReg('GCORRI', 'GCORRI<10:0>')

    @GCORRI.setter
    def GCORRI(self, value):
        """
        Set the value of GCORRI
        """
        if not(0 <= value <= 2047):
            raise ValueError("Value must be [0..2047]")
        self._writeReg('GCORRI', 'GCORRI<10:0>', value)
        #msavic 160606
#        print("Setting GCORRI = " + str(value))
    
    #
    # TXTSP_INTPH (0x0203)
    #
    
    # HBI_OVR<2:0>
    @property 
    def HBI_OVR(self):
        """
        Get the value of HBI_OVR
        """
        return self._readReg('INTPH', 'HBI_OVR<2:0>')

    @HBI_OVR.setter
    def HBI_OVR(self, value):
        """
        Set the value of HBI_OVR
        """
        if value not in [0,1,2,3,4,7, '2', '4', '8', '16', '32', 'BYP']:
            raise ValueError("Value must be [0,1,2,3,4,7, '2', '4', '8', '16', '32', 'BYP']")
        if value==0 or value=='2':
            val = 0
        elif value==1 or value=='4':
            val = 1
        elif value==2 or value=='8':
            val = 2
        elif value==3 or value=='16':
            val = 3
        elif value==4 or value=='32':
            val = 4
        else:
            val = 7
        self._writeReg('INTPH', 'HBI_OVR<2:0>', val)

    # IQCORR<11:0>
    @property 
    def IQCORR(self):
        """
        Get the value of IQCORR<11:0>
        """
        return self.twosComplementToInt(self._readReg('INTPH', 'IQCORR<11:0>'),12)

    @IQCORR.setter
    def IQCORR(self, value):
        """
        Set the value of IQCORR<11:0>
        """
        if not(-2048 <= value <= 2047):
            raise ValueError("Value must be [-2048..2047]")
        self._writeReg('INTPH', 'IQCORR<11:0>', self.intTo2sComplement(value,12))

    #
    # TXTSP_DCCORR (0x0204)
    #

    # DCCORRI<7:0>
    @property 
    def DCCORRI(self):
        """
        Get the value of DCCORRI<7:0>
        """
        return self.twosComplementToInt(self._readReg('DCCORR', 'DCCORRI<7:0>'),8)

    @DCCORRI.setter
    def DCCORRI(self, value):
        """
        Set the value of DCCORRI<7:0>
        """
        if not(-128 <= value <= 127):
            raise ValueError("Value must be [-128..127]")
        self._writeReg('DCCORR', 'DCCORRI<7:0>', self.intTo2sComplement(value,8))

    # DCCORRQ<7:0>
    @property 
    def DCCORRQ(self):
        """
        Get the value of DCCORRQ<7:0>
        """
        return self.twosComplementToInt(self._readReg('DCCORR', 'DCCORRQ<7:0>'),8)

    @DCCORRQ.setter
    def DCCORRQ(self, value):
        """
        Set the value of DCCORRQ<7:0>
        """
        if not(-128 <= value <= 127):
            raise ValueError("Value must be [-128..127]")
        self._writeReg('DCCORR', 'DCCORRQ<7:0>', self.intTo2sComplement(value,8))

    #
    # TXTSP_GFIR1 (0x0205)
    #
    
    # GFIR1_L<2:0>
    @property 
    def GFIR1_L(self):
        """
        Get the value of GFIR1_L<2:0>
        """
        return self._readReg('GFIR1', 'GFIR1_L<2:0>')

    @GFIR1_L.setter
    def GFIR1_L(self, value):
        """
        Set the value of GFIR1_L<2:0>
        """
        if not(0 <= value <= 7):
            raise ValueError("Value must be [0..7]")
        self._writeReg('GFIR1', 'GFIR1_L<2:0>', value)

    # GFIR1_N<7:0>
    @property 
    def GFIR1_N(self):
        """
        Get the value of GFIR1_N<7:0>
        """
        return self._readReg('GFIR1', 'GFIR1_N<7:0>')

    @GFIR1_N.setter
    def GFIR1_N(self, value):
        """
        Set the value of GFIR1_N<7:0>
        """
        if not(0 <= value <= 255):
            raise ValueError("Value must be [0..255]")
        self._writeReg('GFIR1', 'GFIR1_N<7:0>', value)

    #
    # TXTSP_GFIR2 (0x0206)
    #
    
    # GFIR2_L<2:0>
    @property 
    def GFIR2_L(self):
        """
        Get the value of GFIR2_L<2:0>
        """
        return self._readReg('GFIR2', 'GFIR2_L<2:0>')

    @GFIR2_L.setter
    def GFIR2_L(self, value):
        """
        Set the value of GFIR2_L<2:0>
        """
        if not(0 <= value <= 7):
            raise ValueError("Value must be [0..7]")
        self._writeReg('GFIR2', 'GFIR2_L<2:0>', value)

    # GFIR2_N<7:0>
    @property 
    def GFIR2_N(self):
        """
        Get the value of GFIR2_N<7:0>
        """
        return self._readReg('GFIR2', 'GFIR2_N<7:0>')

    @GFIR2_N.setter
    def GFIR2_N(self, value):
        """
        Set the value of GFIR2_N<7:0>
        """
        if not(0 <= value <= 255):
            raise ValueError("Value must be [0..255]")
        self._writeReg('GFIR2', 'GFIR2_N<7:0>', value)

    #
    # TXTSP_GFIR3 (0x0207)
    #
    
    # GFIR3_L<2:0>
    @property 
    def GFIR3_L(self):
        """
        Get the value of GFIR3_L<2:0>
        """
        return self._readReg('GFIR3', 'GFIR3_L<2:0>')

    @GFIR3_L.setter
    def GFIR3_L(self, value):
        """
        Set the value of GFIR3_L<2:0>
        """
        if not(0 <= value <= 7):
            raise ValueError("Value must be [0..7]")
        self._writeReg('GFIR3', 'GFIR3_L<2:0>', value)

    # GFIR3_N<7:0>
    @property 
    def GFIR3_N(self):
        """
        Get the value of GFIR3_N<7:0>
        """
        return self._readReg('GFIR3', 'GFIR3_N<7:0>')

    @GFIR3_N.setter
    def GFIR3_N(self, value):
        """
        Set the value of GFIR3_N<7:0>
        """
        if not(0 <= value <= 255):
            raise ValueError("Value must be [0..255]")
        self._writeReg('GFIR3', 'GFIR3_N<7:0>', value)

    #
    # TXTSP_CMIXBYP (0x0208)
    #

    # CMIX_GAIN<1:0>
    @property 
    def CMIX_GAIN(self):
        """
        Get the value of CMIX_GAIN<1:0>
        """
        return self._readReg('CMIXBYP', 'CMIX_GAIN<1:0>')

    @CMIX_GAIN.setter
    def CMIX_GAIN(self, value):
        """
        Set the value of CMIX_GAIN<1:0>
        """
        if value not in [0,1,2,3,'0dB', '6dB', '-6dB']:
            raise ValueError("Value must be [0,1,2,3,'0dB', '6dB', '-6dB']")
        if value==0 or value=='0dB':
            val = 0
        elif value==1 or value=='6dB':
            val = 1
        else:
            val = 2
        self._writeReg('CMIXBYP', 'CMIX_GAIN<1:0>', val)

    # CMIX_SC
    @property 
    def CMIX_SC(self):
        """
        Get the value of CMIX_SC
        """
        return self._readReg('CMIXBYP', 'CMIX_SC')

    @CMIX_SC.setter
    def CMIX_SC(self, value):
        """
        Set the value of CMIX_SC
        """
        if value not in [0,1,'UP', 'DOWN']:
            raise ValueError("Value must be [0,1,'UP', 'DOWN']")
        if value==0 or value=='UP':
            val = 0
        else:
            val = 1
        self._writeReg('CMIXBYP', 'CMIX_SC', val)

    # CMIX_GAIN2
    @property 
    def CMIX_GAIN2(self):
        """
        Get the value of CMIX_GAIN2
        """
        if self.chip.chipID == self.chip.chipIDMR3:
            return self._readReg('CMIXBYP', 'CMIX_GAIN2')
        else:
            raise ValueError("Bitfield CMIX_GAIN2 is not supported on chip version "+str(self.chip.chipID))

    @CMIX_GAIN2.setter
    def CMIX_GAIN2(self, value):
        """
        Set the value of CMIX_GAIN2
        """
        if self.chip.chipID == self.chip.chipIDMR3:
            if value not in [0,1]:
                raise ValueError("Value must be [0,1]")
            self._writeReg('CMIXBYP', 'CMIX_GAIN2', val)
        else:
            raise ValueError("Bitfield CMIX_GAIN2 is not supported on chip version "+str(self.chip.chipID))

    # CMIX_BYP
    @property 
    def CMIX_BYP(self):
        """
        Get the value of CMIX_BYP
        """
        return self._readReg('CMIXBYP', 'CMIX_BYP')

    @CMIX_BYP.setter
    def CMIX_BYP(self, value):
        """
        Set the value of CMIX_BYP
        """
        if value not in [0,1,'USE', 'BYP']:
            raise ValueError("Value must be [0,1,'USE', 'BYP']")
        if value==0 or value=='USE':
            val = 0
        else:
            val = 1
        self._writeReg('CMIXBYP', 'CMIX_BYP', val)

    # ISINC_BYP
    @property 
    def ISINC_BYP(self):
        """
        Get the value of ISINC_BYP
        """
        return self._readReg('CMIXBYP', 'ISINC_BYP')

    @ISINC_BYP.setter
    def ISINC_BYP(self, value):
        """
        Set the value of ISINC_BYP
        """
        if value not in [0,1,'USE', 'BYP']:
            raise ValueError("Value must be [0,1,'USE', 'BYP']")
        if value==0 or value=='USE':
            val = 0
        else:
            val = 1
        self._writeReg('CMIXBYP', 'ISINC_BYP', val)

    # GFIR3_BYP
    @property 
    def GFIR3_BYP(self):
        """
        Get the value of GFIR3_BYP
        """
        return self._readReg('CMIXBYP', 'GFIR3_BYP')

    @GFIR3_BYP.setter
    def GFIR3_BYP(self, value):
        """
        Set the value of GFIR3_BYP
        """
        if value not in [0,1,'USE', 'BYP']:
            raise ValueError("Value must be [0,1,'USE', 'BYP']")
        if value==0 or value=='USE':
            val = 0
        else:
            val = 1
        self._writeReg('CMIXBYP', 'GFIR3_BYP', val)

    # GFIR2_BYP
    @property 
    def GFIR2_BYP(self):
        """
        Get the value of GFIR2_BYP
        """
        return self._readReg('CMIXBYP', 'GFIR2_BYP')

    @GFIR2_BYP.setter
    def GFIR2_BYP(self, value):
        """
        Set the value of GFIR2_BYP
        """
        if value not in [0,1,'USE', 'BYP']:
            raise ValueError("Value must be [0,1,'USE', 'BYP']")
        if value==0 or value=='USE':
            val = 0
        else:
            val = 1
        self._writeReg('CMIXBYP', 'GFIR2_BYP', val)

    # GFIR1_BYP
    @property 
    def GFIR1_BYP(self):
        """
        Get the value of GFIR1_BYP
        """
        return self._readReg('CMIXBYP', 'GFIR1_BYP')

    @GFIR1_BYP.setter
    def GFIR1_BYP(self, value):
        """
        Set the value of GFIR1_BYP
        """
        if value not in [0,1,'USE', 'BYP']:
            raise ValueError("Value must be [0,1,'USE', 'BYP']")
        if value==0 or value=='USE':
            val = 0
        else:
            val = 1
        self._writeReg('CMIXBYP', 'GFIR1_BYP', val)

    # DC_BYP
    @property 
    def DC_BYP(self):
        """
        Get the value of DC_BYP
        """
        return self._readReg('CMIXBYP', 'DC_BYP')

    @DC_BYP.setter
    def DC_BYP(self, value):
        """
        Set the value of DC_BYP
        """
        if value not in [0,1,'USE', 'BYP']:
            raise ValueError("Value must be [0,1,'USE', 'BYP']")
        if value==0 or value=='USE':
            val = 0
        else:
            val = 1
        self._writeReg('CMIXBYP', 'DC_BYP', val)

    # GC_BYP
    @property 
    def GC_BYP(self):
        """
        Get the value of GC_BYP
        """
        return self._readReg('CMIXBYP', 'GC_BYP')

    @GC_BYP.setter
    def GC_BYP(self, value):
        """
        Set the value of GC_BYP
        """
        if value not in [0,1,'USE', 'BYP']:
            raise ValueError("Value must be [0,1,'USE', 'BYP']")
        if value==0 or value=='USE':
            val = 0
        else:
            val = 1
        self._writeReg('CMIXBYP', 'GC_BYP', val)

    # PH_BYP
    @property 
    def PH_BYP(self):
        """
        Get the value of PH_BYP
        """
        return self._readReg('CMIXBYP', 'PH_BYP')

    @PH_BYP.setter
    def PH_BYP(self, value):
        """
        Set the value of PH_BYP
        """
        if value not in [0,1,'USE', 'BYP']:
            raise ValueError("Value must be [0,1,'USE', 'BYP']")
        if value==0 or value=='USE':
            val = 0
        else:
            val = 1
        self._writeReg('CMIXBYP', 'PH_BYP', val)

    #
    # TXTSP_DC (0x020C) DC_REG<15:0>
    #
    @property 
    def DC_REG(self):
        """
        Get the value of DC_REG<15:0>
        """
        return self._readReg('DC', 'DC_REG<15:0>')

    @DC_REG.setter
    def DC_REG(self, value):
        """
        Set the value of DC_REG<15:0>
        """
        if not(0 <= value <= 65535):
            raise ValueError("Value must be [0..65535]")
        self._writeReg('DC', 'DC_REG<15:0>', value)        

    def loadDCIQ(self, I, Q):
        self.DC_REG = I
        self.TSGDCLDI = 0
        self.TSGDCLDI = 1
        self.TSGDCLDI = 0
        self.DC_REG = Q
        self.TSGDCLDQ = 0
        self.TSGDCLDQ = 1
        self.TSGDCLDQ = 0
    
