#***************************************************************
#* Name:      LMS7002_LimeLight.py
#* Purpose:   Class implementing LMS7002 LimeLight functions
#* Author:    Lime Microsystems ()
#* Created:   2016-11-14
#* Copyright: Lime Microsystems (limemicro.com)
#* License:
#**************************************************************

from LMS7002_base import *

class LMS7002_LimeLight(LMS7002_base):
    __slots__=[]    # Used to generate error on typos
    def __init__(self, chip):
        self.chip = chip
        self.channel = None
        self.prefix = "LimeLight_"

    #
    # LimeLight_IOCFG (0x0023)
    #
    
    # DIQDIRCTR2
    @property 
    def DIQDIRCTR2(self):
        """
        Get the value of DIQDIRCTR2
        """
        return self._readReg('IOCFG', 'DIQDIRCTR2')

    @DIQDIRCTR2.setter
    def DIQDIRCTR2(self, value):
        """
        Set the value of DIQDIRCTR2
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('IOCFG', 'DIQDIRCTR2', value)

    # DIQDIR2
    @property 
    def DIQDIR2(self):
        """
        Get the value of DIQDIR2
        """
        return self._readReg('IOCFG', 'DIQDIR2')

    @DIQDIR2.setter
    def DIQDIR2(self, value):
        """
        Set the value of DIQDIR2
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('IOCFG', 'DIQDIR2', value)

    # DIQDIRCTR1
    @property 
    def DIQDIRCTR1(self):
        """
        Get the value of DIQDIRCTR1
        """
        return self._readReg('IOCFG', 'DIQDIRCTR1')

    @DIQDIRCTR1.setter
    def DIQDIRCTR1(self, value):
        """
        Set the value of DIQDIRCTR1
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('IOCFG', 'DIQDIRCTR1', value)

    # DIQDIR1
    @property 
    def DIQDIR1(self):
        """
        Get the value of DIQDIR1
        """
        return self._readReg('IOCFG', 'DIQDIR1')

    @DIQDIR1.setter
    def DIQDIR1(self, value):
        """
        Set the value of DIQDIR1
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('IOCFG', 'DIQDIR1', value)

    # ENABLEDIRCTR2
    @property 
    def ENABLEDIRCTR2(self):
        """
        Get the value of ENABLEDIRCTR2
        """
        return self._readReg('IOCFG', 'ENABLEDIRCTR2')

    @ENABLEDIRCTR2.setter
    def ENABLEDIRCTR2(self, value):
        """
        Set the value of ENABLEDIRCTR2
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('IOCFG', 'ENABLEDIRCTR2', value)

    # ENABLEDIR2
    @property 
    def ENABLEDIR2(self):
        """
        Get the value of ENABLEDIR2
        """
        return self._readReg('IOCFG', 'ENABLEDIR2')

    @ENABLEDIR2.setter
    def ENABLEDIR2(self, value):
        """
        Set the value of ENABLEDIR2
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('IOCFG', 'ENABLEDIR2', value)

    # ENABLEDIRCTR1
    @property 
    def ENABLEDIRCTR1(self):
        """
        Get the value of ENABLEDIRCTR1
        """
        return self._readReg('IOCFG', 'ENABLEDIRCTR1')

    @ENABLEDIRCTR1.setter
    def ENABLEDIRCTR1(self, value):
        """
        Set the value of ENABLEDIRCTR1
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('IOCFG', 'ENABLEDIRCTR1', value)

    # ENABLEDIR1
    @property 
    def ENABLEDIR1(self):
        """
        Get the value of ENABLEDIR1
        """
        return self._readReg('IOCFG', 'ENABLEDIR1')

    @ENABLEDIR1.setter
    def ENABLEDIR1(self, value):
        """
        Set the value of ENABLEDIR1
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('IOCFG', 'ENABLEDIR1', value)

    # MOD_EN
    @property 
    def MOD_EN(self):
        """
        Get the value of MOD_EN
        """
        return self._readReg('IOCFG', 'MOD_EN')

    @MOD_EN.setter
    def MOD_EN(self, value):
        """
        Set the value of MOD_EN
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('IOCFG', 'MOD_EN', value)

    # LML2_FIDM
    @property 
    def LML2_FIDM(self):
        """
        Get the value of LML2_FIDM
        """
        return self._readReg('IOCFG', 'LML2_FIDM')

    @LML2_FIDM.setter
    def LML2_FIDM(self, value):
        """
        Set the value of LML2_FIDM
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('IOCFG', 'LML2_FIDM', value)

    # LML2_TXNRXIQ
    @property 
    def LML2_TXNRXIQ(self):
        """
        Get the value of LML2_TXNRXIQ
        """
        return self._readReg('IOCFG', 'LML2_TXNRXIQ')

    @LML2_TXNRXIQ.setter
    def LML2_TXNRXIQ(self, value):
        """
        Set the value of LML2_TXNRXIQ
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('IOCFG', 'LML2_TXNRXIQ', value)

    # LML2_MODE
    @property 
    def LML2_MODE(self):
        """
        Get the value of LML2_MODE
        """
        return self._readReg('IOCFG', 'LML2_MODE')

    @LML2_MODE.setter
    def LML2_MODE(self, value):
        """
        Set the value of LML2_MODE
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('IOCFG', 'LML2_MODE', value)

    # LML1_FIDM
    @property 
    def LML1_FIDM(self):
        """
        Get the value of LML1_FIDM
        """
        return self._readReg('IOCFG', 'LML1_FIDM')

    @LML1_FIDM.setter
    def LML1_FIDM(self, value):
        """
        Set the value of LML1_FIDM
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('IOCFG', 'LML1_FIDM', value)

    # LML1_TXNRXIQ
    @property 
    def LML1_TXNRXIQ(self):
        """
        Get the value of LML1_TXNRXIQ
        """
        return self._readReg('IOCFG', 'LML1_TXNRXIQ')

    @LML1_TXNRXIQ.setter
    def LML1_TXNRXIQ(self, value):
        """
        Set the value of LML1_TXNRXIQ
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('IOCFG', 'LML1_TXNRXIQ', value)

    # LML1_MODE
    @property 
    def LML1_MODE(self):
        """
        Get the value of LML1_MODE
        """
        return self._readReg('IOCFG', 'LML1_MODE')

    @LML1_MODE.setter
    def LML1_MODE(self, value):
        """
        Set the value of LML1_MODE
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('IOCFG', 'LML1_MODE', value)

    #
    # LimeLight_POS1 (0x0024)
    #
    
    # LML1_S3S<1:0>
    @property 
    def LML1_S3S(self):
        """
        Get the value of LML1_S3S<1:0>
        """
        return self._readReg('POS1', 'LML1_S3S<1:0>')

    @LML1_S3S.setter
    def LML1_S3S(self, value):
        """
        Set the value of LML1_S3S<1:0>
        """
        if not(0 <= value <= 3):
            raise ValueError("Value must be [0..3]")
        self._writeReg('POS1', 'LML1_S3S<1:0>', value)

    # LML1_S2S<1:0>
    @property 
    def LML1_S2S(self):
        """
        Get the value of LML1_S2S<1:0>
        """
        return self._readReg('POS1', 'LML1_S2S<1:0>')

    @LML1_S2S.setter
    def LML1_S2S(self, value):
        """
        Set the value of LML1_S2S<1:0>
        """
        if not(0 <= value <= 3):
            raise ValueError("Value must be [0..3]")
        self._writeReg('POS1', 'LML1_S2S<1:0>', value)

    # LML1_S1S<1:0>
    @property 
    def LML1_S1S(self):
        """
        Get the value of LML1_S1S<1:0>
        """
        return self._readReg('POS1', 'LML1_S1S<1:0>')

    @LML1_S1S.setter
    def LML1_S1S(self, value):
        """
        Set the value of LML1_S1S<1:0>
        """
        if not(0 <= value <= 3):
            raise ValueError("Value must be [0..3]")
        self._writeReg('POS1', 'LML1_S1S<1:0>', value)

    # LML1_S0S<1:0>
    @property 
    def LML1_S0S(self):
        """
        Get the value of LML1_S0S<1:0>
        """
        return self._readReg('POS1', 'LML1_S0S<1:0>')

    @LML1_S0S.setter
    def LML1_S0S(self, value):
        """
        Set the value of LML1_S0S<1:0>
        """
        if not(0 <= value <= 3):
            raise ValueError("Value must be [0..3]")
        self._writeReg('POS1', 'LML1_S0S<1:0>', value)

    # LML1_BQP<1:0>
    @property 
    def LML1_BQP(self):
        """
        Get the value of LML1_BQP<1:0>
        """
        return self._readReg('POS1', 'LML1_BQP<1:0>')

    @LML1_BQP.setter
    def LML1_BQP(self, value):
        """
        Set the value of LML1_BQP<1:0>
        """
        if not(0 <= value <= 3):
            raise ValueError("Value must be [0..3]")
        self._writeReg('POS1', 'LML1_BQP<1:0>', value)

    # LML1_BIP<1:0>
    @property 
    def LML1_BIP(self):
        """
        Get the value of LML1_BIP<1:0>
        """
        return self._readReg('POS1', 'LML1_BIP<1:0>')

    @LML1_BIP.setter
    def LML1_BIP(self, value):
        """
        Set the value of LML1_BIP<1:0>
        """
        if not(0 <= value <= 3):
            raise ValueError("Value must be [0..3]")
        self._writeReg('POS1', 'LML1_BIP<1:0>', value)

    # LML1_AQP<1:0>
    @property 
    def LML1_AQP(self):
        """
        Get the value of LML1_AQP<1:0>
        """
        return self._readReg('POS1', 'LML1_AQP<1:0>')

    @LML1_AQP.setter
    def LML1_AQP(self, value):
        """
        Set the value of LML1_AQP<1:0>
        """
        if not(0 <= value <= 3):
            raise ValueError("Value must be [0..3]")
        self._writeReg('POS1', 'LML1_AQP<1:0>', value)

    # LML1_AIP<1:0>
    @property 
    def LML1_AIP(self):
        """
        Get the value of LML1_AIP<1:0>
        """
        return self._readReg('POS1', 'LML1_AIP<1:0>')

    @LML1_AIP.setter
    def LML1_AIP(self, value):
        """
        Set the value of LML1_AIP<1:0>
        """
        if not(0 <= value <= 3):
            raise ValueError("Value must be [0..3]")
        self._writeReg('POS1', 'LML1_AIP<1:0>', value)

    #
    # LimeLight_BBRF1 (0x0025)
    #

    # LML1_BB2RF_PST<4:0>
    @property 
    def LML1_BB2RF_PST(self):
        """
        Get the value of LML1_BB2RF_PST<4:0>
        """
        return self._readReg('BBRF1', 'LML1_BB2RF_PST<4:0>')

    @LML1_BB2RF_PST.setter
    def LML1_BB2RF_PST(self, value):
        """
        Set the value of LML1_BB2RF_PST<4:0>
        """
        if not(0 <= value <= 31):
            raise ValueError("Value must be [0..31]")
        self._writeReg('BBRF1', 'LML1_BB2RF_PST<4:0>', value)

    # LML1_BB2RF_PRE<4:0>
    @property 
    def LML1_BB2RF_PRE(self):
        """
        Get the value of LML1_BB2RF_PRE<4:0>
        """
        return self._readReg('BBRF1', 'LML1_BB2RF_PRE<4:0>')

    @LML1_BB2RF_PRE.setter
    def LML1_BB2RF_PRE(self, value):
        """
        Set the value of LML1_BB2RF_PRE<4:0>
        """
        if not(0 <= value <= 31):
            raise ValueError("Value must be [0..31]")
        self._writeReg('BBRF1', 'LML1_BB2RF_PRE<4:0>', value)

    #
    # LimeLight_RFBB1 (0x0026)
    #

    # LML1_RF2BB_PST<4:0>
    @property 
    def LML1_RF2BB_PST(self):
        """
        Get the value of LML1_RF2BB_PST<4:0>
        """
        return self._readReg('RFBB1', 'LML1_RF2BB_PST<4:0>')

    @LML1_RF2BB_PST.setter
    def LML1_RF2BB_PST(self, value):
        """
        Set the value of LML1_RF2BB_PST<4:0>
        """
        if not(0 <= value <= 31):
            raise ValueError("Value must be [0..31]")
        self._writeReg('RFBB1', 'LML1_RF2BB_PST<4:0>', value)

    # LML1_RF2BB_PRE<4:0>
    @property 
    def LML1_RF2BB_PRE(self):
        """
        Get the value of LML1_RF2BB_PRE<4:0>
        """
        return self._readReg('RFBB1', 'LML1_RF2BB_PRE<4:0>')

    @LML1_RF2BB_PRE.setter
    def LML1_RF2BB_PRE(self, value):
        """
        Set the value of LML1_RF2BB_PRE<4:0>
        """
        if not(0 <= value <= 31):
            raise ValueError("Value must be [0..31]")
        self._writeReg('RFBB1', 'LML1_RF2BB_PRE<4:0>', value)

    #
    # LimeLight_POS2 (0x0027)
    #
    
    # LML2_S3S<1:0>
    @property 
    def LML2_S3S(self):
        """
        Get the value of LML2_S3S<1:0>
        """
        return self._readReg('POS2', 'LML2_S3S<1:0>')

    @LML2_S3S.setter
    def LML2_S3S(self, value):
        """
        Set the value of LML2_S3S<1:0>
        """
        if not(0 <= value <= 3):
            raise ValueError("Value must be [0..3]")
        self._writeReg('POS2', 'LML2_S3S<1:0>', value)

    # LML2_S2S<1:0>
    @property 
    def LML2_S2S(self):
        """
        Get the value of LML2_S2S<1:0>
        """
        return self._readReg('POS2', 'LML2_S2S<1:0>')

    @LML2_S2S.setter
    def LML2_S2S(self, value):
        """
        Set the value of LML2_S2S<1:0>
        """
        if not(0 <= value <= 3):
            raise ValueError("Value must be [0..3]")
        self._writeReg('POS2', 'LML2_S2S<1:0>', value)

    # LML2_S1S<1:0>
    @property 
    def LML2_S1S(self):
        """
        Get the value of LML2_S1S<1:0>
        """
        return self._readReg('POS2', 'LML2_S1S<1:0>')

    @LML2_S1S.setter
    def LML2_S1S(self, value):
        """
        Set the value of LML2_S1S<1:0>
        """
        if not(0 <= value <= 3):
            raise ValueError("Value must be [0..3]")
        self._writeReg('POS2', 'LML2_S1S<1:0>', value)

    # LML2_S0S<1:0>
    @property 
    def LML2_S0S(self):
        """
        Get the value of LML2_S0S<1:0>
        """
        return self._readReg('POS2', 'LML2_S0S<1:0>')

    @LML2_S0S.setter
    def LML2_S0S(self, value):
        """
        Set the value of LML2_S0S<1:0>
        """
        if not(0 <= value <= 3):
            raise ValueError("Value must be [0..3]")
        self._writeReg('POS2', 'LML2_S0S<1:0>', value)

    # LML2_BQP<1:0>
    @property 
    def LML2_BQP(self):
        """
        Get the value of LML2_BQP<1:0>
        """
        return self._readReg('POS2', 'LML2_BQP<1:0>')

    @LML2_BQP.setter
    def LML2_BQP(self, value):
        """
        Set the value of LML2_BQP<1:0>
        """
        if not(0 <= value <= 3):
            raise ValueError("Value must be [0..3]")
        self._writeReg('POS2', 'LML2_BQP<1:0>', value)

    # LML2_BIP<1:0>
    @property 
    def LML2_BIP(self):
        """
        Get the value of LML2_BIP<1:0>
        """
        return self._readReg('POS2', 'LML2_BIP<1:0>')

    @LML2_BIP.setter
    def LML2_BIP(self, value):
        """
        Set the value of LML2_BIP<1:0>
        """
        if not(0 <= value <= 3):
            raise ValueError("Value must be [0..3]")
        self._writeReg('POS2', 'LML2_BIP<1:0>', value)

    # LML2_AQP<1:0>
    @property 
    def LML2_AQP(self):
        """
        Get the value of LML2_AQP<1:0>
        """
        return self._readReg('POS2', 'LML2_AQP<1:0>')

    @LML2_AQP.setter
    def LML2_AQP(self, value):
        """
        Set the value of LML2_AQP<1:0>
        """
        if not(0 <= value <= 3):
            raise ValueError("Value must be [0..3]")
        self._writeReg('POS2', 'LML2_AQP<1:0>', value)

    # LML2_AIP<1:0>
    @property 
    def LML2_AIP(self):
        """
        Get the value of LML2_AIP<1:0>
        """
        return self._readReg('POS2', 'LML2_AIP<1:0>')

    @LML2_AIP.setter
    def LML2_AIP(self, value):
        """
        Set the value of LML2_AIP<1:0>
        """
        if not(0 <= value <= 3):
            raise ValueError("Value must be [0..3]")
        self._writeReg('POS2', 'LML2_AIP<1:0>', value)

    #
    # LimeLight_BBRF2 (0x0028)
    #
    
    # LML2_BB2RF_PST<4:0>
    @property 
    def LML2_BB2RF_PST(self):
        """
        Get the value of LML2_BB2RF_PST<4:0>
        """
        return self._readReg('BBRF2', 'LML2_BB2RF_PST<4:0>')

    @LML2_BB2RF_PST.setter
    def LML2_BB2RF_PST(self, value):
        """
        Set the value of LML2_BB2RF_PST<4:0>
        """
        if not(0 <= value <= 31):
            raise ValueError("Value must be [0..31]")
        self._writeReg('BBRF2', 'LML2_BB2RF_PST<4:0>', value)

    # LML2_RF2BB_PRE<4:0>
    @property 
    def LML2_RF2BB_PRE(self):
        """
        Get the value of LML2_RF2BB_PRE<4:0>
        """
        return self._readReg('BBRF2', 'LML2_RF2BB_PRE<4:0>')

    @LML2_RF2BB_PRE.setter
    def LML2_RF2BB_PRE(self, value):
        """
        Set the value of LML2_RF2BB_PRE<4:0>
        """
        if not(0 <= value <= 31):
            raise ValueError("Value must be [0..31]")
        self._writeReg('BBRF2', 'LML2_RF2BB_PRE<4:0>', value)

    #
    # LimeLight_RFBB2 (0x0029)
    #
    
    # LML2_RF2BB_PST<4:0>
    @property 
    def LML2_RF2BB_PST(self):
        """
        Get the value of LML2_RF2BB_PST<4:0>
        """
        return self._readReg('RFBB2', 'LML2_RF2BB_PST<4:0>')

    @LML2_RF2BB_PST.setter
    def LML2_RF2BB_PST(self, value):
        """
        Set the value of LML2_RF2BB_PST<4:0>
        """
        if not(0 <= value <= 31):
            raise ValueError("Value must be [0..31]")
        self._writeReg('RFBB2', 'LML2_RF2BB_PST<4:0>', value)

    # LML2_RF2BB_PRE<4:0>
    @property 
    def LML2_RF2BB_PRE(self):
        """
        Get the value of LML2_RF2BB_PRE<4:0>
        """
        return self._readReg('RFBB2', 'LML2_RF2BB_PRE<4:0>')

    @LML2_RF2BB_PRE.setter
    def LML2_RF2BB_PRE(self, value):
        """
        Set the value of LML2_RF2BB_PRE<4:0>
        """
        if not(0 <= value <= 31):
            raise ValueError("Value must be [0..31]")
        self._writeReg('RFBB2', 'LML2_RF2BB_PRE<4:0>', value)

    #
    # LimeLight_CLKSRC (0x002A)
    #

    # FCLK2_DLY<1:0>
    @property 
    def FCLK2_DLY(self):
        """
        Get the value of FCLK2_DLY<1:0>
        """
        if self.chip.chipID == self.chip.chipIDMR3:
            return self._readReg('CLKSRC', 'FCLK2_DLY<1:0>')
        else:
            raise ValueError("Bitfield FCLK2_DLY is not supported on chip version "+str(self.chip.chipID))


    @FCLK2_DLY.setter
    def FCLK2_DLY(self, value):
        """
        Set the value of FCLK2_DLY<1:0>
        """
        if self.chip.chipID == self.chip.chipIDMR3:
            if not(0 <= value <= 3):
                raise ValueError("Value must be [0..3]")
            self._writeReg('CLKSRC', 'FCLK2_DLY<1:0>', value)
        else:
            raise ValueError("Bitfield FCLK2_DLY is not supported on chip version "+str(self.chip.chipID))

    # FCLK1_DLY<1:0>
    @property 
    def FCLK1_DLY(self):
        """
        Get the value of FCLK1_DLY<1:0>
        """
        if self.chip.chipID == self.chip.chipIDMR3:
            return self._readReg('CLKSRC', 'FCLK1_DLY<1:0>')
        else:
            raise ValueError("Bitfield FCLK1_DLY is not supported on chip version "+str(self.chip.chipID))


    @FCLK1_DLY.setter
    def FCLK1_DLY(self, value):
        """
        Set the value of FCLK1_DLY<1:0>
        """
        if self.chip.chipID == self.chip.chipIDMR3:
            if not(0 <= value <= 3):
                raise ValueError("Value must be [0..3]")
            self._writeReg('CLKSRC', 'FCLK1_DLY<1:0>', value)
        else:
            raise ValueError("Bitfield FCLK1_DLY is not supported on chip version "+str(self.chip.chipID))
    
    # RX_MUX<1:0>
    @property 
    def RX_MUX(self):
        """
        Get the value of RX_MUX<1:0>
        """
        return self._readReg('CLKSRC', 'RX_MUX<1:0>')

    @RX_MUX.setter
    def RX_MUX(self, value):
        """
        Set the value of RX_MUX<1:0>
        """
        if not(0 <= value <= 3):
            raise ValueError("Value must be [0..3]")
        self._writeReg('CLKSRC', 'RX_MUX<1:0>', value)

    # TX_MUX<1:0>
    @property 
    def TX_MUX(self):
        """
        Get the value of TX_MUX<1:0>
        """
        return self._readReg('CLKSRC', 'TX_MUX<1:0>')

    @TX_MUX.setter
    def TX_MUX(self, value):
        """
        Set the value of TX_MUX<1:0>
        """
        if not(0 <= value <= 3):
            raise ValueError("Value must be [0..3]")
        self._writeReg('CLKSRC', 'TX_MUX<1:0>', value)

    # TXRDCLK_MUX<1:0>
    @property 
    def TXRDCLK_MUX(self):
        """
        Get the value of TXRDCLK_MUX<1:0>
        """
        return self._readReg('CLKSRC', 'TXRDCLK_MUX<1:0>')

    @TXRDCLK_MUX.setter
    def TXRDCLK_MUX(self, value):
        """
        Set the value of TXRDCLK_MUX<1:0>
        """
        if not(0 <= value <= 3):
            raise ValueError("Value must be [0..3]")
        self._writeReg('CLKSRC', 'TXRDCLK_MUX<1:0>', value)

    # TXWRCLK_MUX<1:0>
    @property 
    def TXWRCLK_MUX(self):
        """
        Get the value of TXWRCLK_MUX<1:0>
        """
        return self._readReg('CLKSRC', 'TXWRCLK_MUX<1:0>')

    @TXWRCLK_MUX.setter
    def TXWRCLK_MUX(self, value):
        """
        Set the value of TXWRCLK_MUX<1:0>
        """
        if not(0 <= value <= 3):
            raise ValueError("Value must be [0..3]")
        self._writeReg('CLKSRC', 'TXWRCLK_MUX<1:0>', value)

    # RXRDCLK_MUX<1:0>
    @property 
    def RXRDCLK_MUX(self):
        """
        Get the value of RXRDCLK_MUX<1:0>
        """
        return self._readReg('CLKSRC', 'RXRDCLK_MUX<1:0>')

    @RXRDCLK_MUX.setter
    def RXRDCLK_MUX(self, value):
        """
        Set the value of RXRDCLK_MUX<1:0>
        """
        if not(0 <= value <= 3):
            raise ValueError("Value must be [0..3]")
        self._writeReg('CLKSRC', 'RXRDCLK_MUX<1:0>', value)

    # RXWRCLK_MUX<1:0>
    @property 
    def RXWRCLK_MUX(self):
        """
        Get the value of RXWRCLK_MUX<1:0>
        """
        return self._readReg('CLKSRC', 'RXWRCLK_MUX<1:0>')

    @RXWRCLK_MUX.setter
    def RXWRCLK_MUX(self, value):
        """
        Set the value of RXWRCLK_MUX<1:0>
        """
        if not(0 <= value <= 3):
            raise ValueError("Value must be [0..3]")
        self._writeReg('CLKSRC', 'RXWRCLK_MUX<1:0>', value)

    #
    # LimeLight_CLKCFG (0x002B)
    #

    # FCLK2_INV
    @property 
    def FCLK2_INV(self):
        """
        Get the value of FCLK2_INV
        """
        return self._readReg('CLKCFG', 'FCLK2_INV')

    @FCLK2_INV.setter
    def FCLK2_INV(self, value):
        """
        Set the value of FCLK2_INV
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CLKCFG', 'FCLK2_INV', value)

    # FCLK1_INV
    @property 
    def FCLK1_INV(self):
        """
        Get the value of FCLK1_INV
        """
        return self._readReg('CLKCFG', 'FCLK1_INV')

    @FCLK1_INV.setter
    def FCLK1_INV(self, value):
        """
        Set the value of FCLK1_INV
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CLKCFG', 'FCLK1_INV', value)

    # MCLK2_DLY<1:0>
    @property 
    def MCLK2_DLY(self):
        """
        Get the value of MCLK2_DLY<1:0>
        """
        if self.chip.chipID == self.chip.chipIDMR3:
            return self._readReg('CLKCFG', 'MCLK2_DLY<1:0>')
        else:
            raise ValueError("Bitfield MCLK2_DLY is not supported on chip version "+str(self.chip.chipID))


    @MCLK2_DLY.setter
    def MCLK2_DLY(self, value):
        """
        Set the value of MCLK2_DLY<1:0>
        """
        if self.chip.chipID == self.chip.chipIDMR3:
            if not(0 <= value <= 3):
                raise ValueError("Value must be [0..3]")
            self._writeReg('CLKCFG', 'MCLK2_DLY<1:0>', value)
        else:
            raise ValueError("Bitfield MCLK2_DLY is not supported on chip version "+str(self.chip.chipID))

    # MCLK1_DLY<1:0>
    @property 
    def MCLK1_DLY(self):
        """
        Get the value of MCLK1_DLY<1:0>
        """
        if self.chip.chipID == self.chip.chipIDMR3:
            return self._readReg('CLKCFG', 'MCLK1_DLY<1:0>')
        else:
            raise ValueError("Bitfield MCLK1_DLY is not supported on chip version "+str(self.chip.chipID))


    @MCLK1_DLY.setter
    def MCLK1_DLY(self, value):
        """
        Set the value of MCLK1_DLY<1:0>
        """
        if self.chip.chipID == self.chip.chipIDMR3:
            if not(0 <= value <= 3):
                raise ValueError("Value must be [0..3]")
            self._writeReg('CLKCFG', 'MCLK1_DLY<1:0>', value)
        else:
            raise ValueError("Bitfield MCLK1_DLY is not supported on chip version "+str(self.chip.chipID))

    # MCLK2_INV
    @property 
    def MCLK2_INV(self):
        """
        Get the value of MCLK2_INV
        """
        if self.chip.chipID == self.chip.chipIDMR3:
            return self._readReg('CLKCFG', 'MCLK2_INV')
        else:
            raise ValueError("Bitfield MCLK2_INV is not supported on chip version "+str(self.chip.chipID))

    @MCLK2_INV.setter
    def MCLK2_INV(self, value):
        """
        Set the value of MCLK2_INV
        """
        if self.chip.chipID == self.chip.chipIDMR3:
            if value not in [0, 1]:
                raise ValueError("Value must be [0,1]")
            self._writeReg('CLKCFG', 'MCLK2_INV', value)
        else:
            raise ValueError("Bitfield MCLK2_INV is not supported on chip version "+str(self.chip.chipID))

    # MCLK1_INV
    @property 
    def MCLK1_INV(self):
        """
        Get the value of MCLK1_INV
        """
        if self.chip.chipID == self.chip.chipIDMR3:
            return self._readReg('CLKCFG', 'MCLK1_INV')
        else:
            raise ValueError("Bitfield MCLK1_INV is not supported on chip version "+str(self.chip.chipID))

    @MCLK1_INV.setter
    def MCLK1_INV(self, value):
        """
        Set the value of MCLK1_INV
        """
        if self.chip.chipID == self.chip.chipIDMR3:
            if value not in [0, 1]:
                raise ValueError("Value must be [0,1]")
            self._writeReg('CLKCFG', 'MCLK1_INV', value)
        else:
            raise ValueError("Bitfield MCLK1_INV is not supported on chip version "+str(self.chip.chipID))

    # MCLK2SRC<1:0>
    @property 
    def MCLK2SRC(self):
        """
        Get the value of MCLK2SRC<1:0>
        """
        return self._readReg('CLKCFG', 'MCLK2SRC<1:0>')

    @MCLK2SRC.setter
    def MCLK2SRC(self, value):
        """
        Set the value of MCLK2SRC<1:0>
        """
        if not(0 <= value <= 3):
            raise ValueError("Value must be [0..3]")
        self._writeReg('CLKCFG', 'MCLK2SRC<1:0>', value)

    # MCLK1SRC<1:0>
    @property 
    def MCLK1SRC(self):
        """
        Get the value of MCLK1SRC<1:0>
        """
        return self._readReg('CLKCFG', 'MCLK1SRC<1:0>')

    @MCLK1SRC.setter
    def MCLK1SRC(self, value):
        """
        Set the value of MCLK1SRC<1:0>
        """
        if not(0 <= value <= 3):
            raise ValueError("Value must be [0..3]")
        self._writeReg('CLKCFG', 'MCLK1SRC<1:0>', value)

    # TXDIVEN
    @property 
    def TXDIVEN(self):
        """
        Get the value of TXDIVEN
        """
        return self._readReg('CLKCFG', 'TXDIVEN')

    @TXDIVEN.setter
    def TXDIVEN(self, value):
        """
        Set the value of TXDIVEN
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CLKCFG', 'TXDIVEN', value)

    # RXDIVEN
    @property 
    def RXDIVEN(self):
        """
        Get the value of RXDIVEN
        """
        return self._readReg('CLKCFG', 'RXDIVEN')

    @RXDIVEN.setter
    def RXDIVEN(self, value):
        """
        Set the value of RXDIVEN
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CLKCFG', 'RXDIVEN', value)
    

