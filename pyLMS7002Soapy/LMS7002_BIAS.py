#***************************************************************
#* Name:      LMS7002_BIAS.py
#* Purpose:   Class implementing LMS7002 BIAS functions
#* Author:    Lime Microsystems ()
#* Created:   2016-11-14
#* Copyright: Lime Microsystems (limemicro.com)
#* License:
#**************************************************************

from LMS7002_base import *

class LMS7002_BIAS(LMS7002_base):
    __slots__ = ['allowLDO']    # Used to generate error on typos
    def __init__(self, chip):
        self.chip = chip
        self.channel = None
        self.prefix = "BIAS_"
        self.allowLDO = False   # Do not allow changing of LDO voltage
            
    #
    # BIAS_CFG (0x0084)
    #

    # MUX_BIAS_OUT<1:0>
    @property 
    def MUX_BIAS_OUT(self):
        """
        Get the value of MUX_BIAS_OUT<1:0>
        """
        return self._readReg('CFG', 'MUX_BIAS_OUT<1:0>')

    @MUX_BIAS_OUT.setter
    def MUX_BIAS_OUT(self, value):
        """
        Set the value of MUX_BIAS_OUT<1:0>
        """
        if not(0 <= value <= 3):
            raise ValueError("Value must be [0..3]")
        self._writeReg('CFG', 'MUX_BIAS_OUT<1:0>', value)

    # RP_CALIB_BIAS<4:0>
    @property 
    def RP_CALIB_BIAS(self):
        """
        Get the value of RP_CALIB_BIAS<4:0>
        """
        return self._readReg('CFG', 'RP_CALIB_BIAS<4:0>')

    @RP_CALIB_BIAS.setter
    def RP_CALIB_BIAS(self, value):
        """
        Set the value of RP_CALIB_BIAS<4:0>
        """
        if not(0 <= value <= 31):
            raise ValueError("Value must be [0..31]")
        self._writeReg('CFG', 'RP_CALIB_BIAS<4:0>', value)

    # PD_FRP_BIAS
    @property 
    def PD_FRP_BIAS(self):
        """
        Get the value of PD_FRP_BIAS
        """
        return self._readReg('CFG', 'PD_FRP_BIAS')

    @PD_FRP_BIAS.setter
    def PD_FRP_BIAS(self, value):
        """
        Set the value of PD_FRP_BIAS
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG', 'PD_FRP_BIAS', value)

    # PD_F_BIAS
    @property 
    def PD_F_BIAS(self):
        """
        Get the value of PD_F_BIAS
        """
        return self._readReg('CFG', 'PD_F_BIAS')

    @PD_F_BIAS.setter
    def PD_F_BIAS(self, value):
        """
        Set the value of PD_F_BIAS
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG', 'PD_F_BIAS', value)

    # PD_PTRP_BIAS
    @property 
    def PD_PTRP_BIAS(self):
        """
        Get the value of PD_PTRP_BIAS
        """
        return self._readReg('CFG', 'PD_PTRP_BIAS')

    @PD_PTRP_BIAS.setter
    def PD_PTRP_BIAS(self, value):
        """
        Set the value of PD_PTRP_BIAS
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG', 'PD_PTRP_BIAS', value)

    # PD_PT_BIAS
    @property 
    def PD_PT_BIAS(self):
        """
        Get the value of PD_PT_BIAS
        """
        return self._readReg('CFG', 'PD_PT_BIAS')

    @PD_PT_BIAS.setter
    def PD_PT_BIAS(self, value):
        """
        Set the value of PD_PT_BIAS
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG', 'PD_PT_BIAS', value)

    # PD_BIAS_MASTER
    @property 
    def PD_BIAS_MASTER(self):
        """
        Get the value of PD_BIAS_MASTER
        """
        return self._readReg('CFG', 'PD_BIAS_MASTER')

    @PD_BIAS_MASTER.setter
    def PD_BIAS_MASTER(self, value):
        """
        Set the value of PD_BIAS_MASTER
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG', 'PD_BIAS_MASTER', value)

    #
    # BIAS_CFG0 (0x0092)
    #
    
    # EN_LDO_DIG
    @property 
    def EN_LDO_DIG(self):
        """
        Get the value of EN_LDO_DIG
        """
        return self._readReg('CFG0', 'EN_LDO_DIG')

    @EN_LDO_DIG.setter
    def EN_LDO_DIG(self, value):
        """
        Set the value of EN_LDO_DIG
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG0', 'EN_LDO_DIG', value)

    # EN_LDO_DIGGN
    @property 
    def EN_LDO_DIGGN(self):
        """
        Get the value of EN_LDO_DIGGN
        """
        return self._readReg('CFG0', 'EN_LDO_DIGGN')

    @EN_LDO_DIGGN.setter
    def EN_LDO_DIGGN(self, value):
        """
        Set the value of EN_LDO_DIGGN
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG0', 'EN_LDO_DIGGN', value)

    # EN_LDO_DIGSXR
    @property 
    def EN_LDO_DIGSXR(self):
        """
        Get the value of EN_LDO_DIGSXR
        """
        return self._readReg('CFG0', 'EN_LDO_DIGSXR')

    @EN_LDO_DIGSXR.setter
    def EN_LDO_DIGSXR(self, value):
        """
        Set the value of EN_LDO_DIGSXR
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG0', 'EN_LDO_DIGSXR', value)

    # EN_LDO_DIGSXT
    @property 
    def EN_LDO_DIGSXT(self):
        """
        Get the value of EN_LDO_DIGSXT
        """
        return self._readReg('CFG0', 'EN_LDO_DIGSXT')

    @EN_LDO_DIGSXT.setter
    def EN_LDO_DIGSXT(self, value):
        """
        Set the value of EN_LDO_DIGSXT
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG0', 'EN_LDO_DIGSXT', value)

    # EN_LDO_DIVGN
    @property 
    def EN_LDO_DIVGN(self):
        """
        Get the value of EN_LDO_DIVGN
        """
        return self._readReg('CFG0', 'EN_LDO_DIVGN')

    @EN_LDO_DIVGN.setter
    def EN_LDO_DIVGN(self, value):
        """
        Set the value of EN_LDO_DIVGN
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG0', 'EN_LDO_DIVGN', value)

    # EN_LDO_DIVSXR
    @property 
    def EN_LDO_DIVSXR(self):
        """
        Get the value of EN_LDO_DIVSXR
        """
        return self._readReg('CFG0', 'EN_LDO_DIVSXR')

    @EN_LDO_DIVSXR.setter
    def EN_LDO_DIVSXR(self, value):
        """
        Set the value of EN_LDO_DIVSXR
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG0', 'EN_LDO_DIVSXR', value)

    # EN_LDO_DIVSXT
    @property 
    def EN_LDO_DIVSXT(self):
        """
        Get the value of EN_LDO_DIVSXT
        """
        return self._readReg('CFG0', 'EN_LDO_DIVSXT')

    @EN_LDO_DIVSXT.setter
    def EN_LDO_DIVSXT(self, value):
        """
        Set the value of EN_LDO_DIVSXT
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG0', 'EN_LDO_DIVSXT', value)

    # EN_LDO_LNA12
    @property 
    def EN_LDO_LNA12(self):
        """
        Get the value of EN_LDO_LNA12
        """
        return self._readReg('CFG0', 'EN_LDO_LNA12')

    @EN_LDO_LNA12.setter
    def EN_LDO_LNA12(self, value):
        """
        Set the value of EN_LDO_LNA12
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG0', 'EN_LDO_LNA12', value)

    # EN_LDO_LNA14
    @property 
    def EN_LDO_LNA14(self):
        """
        Get the value of EN_LDO_LNA14
        """
        return self._readReg('CFG0', 'EN_LDO_LNA14')

    @EN_LDO_LNA14.setter
    def EN_LDO_LNA14(self, value):
        """
        Set the value of EN_LDO_LNA14
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG0', 'EN_LDO_LNA14', value)

    # EN_LDO_MXRFE
    @property 
    def EN_LDO_MXRFE(self):
        """
        Get the value of EN_LDO_MXRFE
        """
        return self._readReg('CFG0', 'EN_LDO_MXRFE')

    @EN_LDO_MXRFE.setter
    def EN_LDO_MXRFE(self, value):
        """
        Set the value of EN_LDO_MXRFE
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG0', 'EN_LDO_MXRFE', value)

    # EN_LDO_RBB
    @property 
    def EN_LDO_RBB(self):
        """
        Get the value of EN_LDO_RBB
        """
        return self._readReg('CFG0', 'EN_LDO_RBB')

    @EN_LDO_RBB.setter
    def EN_LDO_RBB(self, value):
        """
        Set the value of EN_LDO_RBB
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG0', 'EN_LDO_RBB', value)

    # EN_LDO_RXBUF
    @property 
    def EN_LDO_RXBUF(self):
        """
        Get the value of EN_LDO_RXBUF
        """
        return self._readReg('CFG0', 'EN_LDO_RXBUF')

    @EN_LDO_RXBUF.setter
    def EN_LDO_RXBUF(self, value):
        """
        Set the value of EN_LDO_RXBUF
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG0', 'EN_LDO_RXBUF', value)

    # EN_LDO_TBB
    @property 
    def EN_LDO_TBB(self):
        """
        Get the value of EN_LDO_TBB
        """
        return self._readReg('CFG0', 'EN_LDO_TBB')

    @EN_LDO_TBB.setter
    def EN_LDO_TBB(self, value):
        """
        Set the value of EN_LDO_TBB
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG0', 'EN_LDO_TBB', value)

    # EN_LDO_TIA12
    @property 
    def EN_LDO_TIA12(self):
        """
        Get the value of EN_LDO_TIA12
        """
        return self._readReg('CFG0', 'EN_LDO_TIA12')

    @EN_LDO_TIA12.setter
    def EN_LDO_TIA12(self, value):
        """
        Set the value of EN_LDO_TIA12
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG0', 'EN_LDO_TIA12', value)

    # EN_LDO_TIA14
    @property 
    def EN_LDO_TIA14(self):
        """
        Get the value of EN_LDO_TIA14
        """
        return self._readReg('CFG0', 'EN_LDO_TIA14')

    @EN_LDO_TIA14.setter
    def EN_LDO_TIA14(self, value):
        """
        Set the value of EN_LDO_TIA14
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG0', 'EN_LDO_TIA14', value)

    # EN_G_LDO
    @property 
    def EN_G_LDO(self):
        """
        Get the value of EN_G_LDO
        """
        return self._readReg('CFG0', 'EN_G_LDO')

    @EN_G_LDO.setter
    def EN_G_LDO(self, value):
        """
        Set the value of EN_G_LDO
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG0', 'EN_G_LDO', value)

    #
    # BIAS_CFG1 (0x0093)
    #
    
    # EN_LOADIMP_LDO_TLOB
    @property 
    def EN_LOADIMP_LDO_TLOB(self):
        """
        Get the value of EN_LOADIMP_LDO_TLOB
        """
        return self._readReg('CFG1', 'EN_LOADIMP_LDO_TLOB')

    @EN_LOADIMP_LDO_TLOB.setter
    def EN_LOADIMP_LDO_TLOB(self, value):
        """
        Set the value of EN_LOADIMP_LDO_TLOB
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG1', 'EN_LOADIMP_LDO_TLOB', value)

    # EN_LOADIMP_LDO_TPAD
    @property 
    def EN_LOADIMP_LDO_TPAD(self):
        """
        Get the value of EN_LOADIMP_LDO_TPAD
        """
        return self._readReg('CFG1', 'EN_LOADIMP_LDO_TPAD')

    @EN_LOADIMP_LDO_TPAD.setter
    def EN_LOADIMP_LDO_TPAD(self, value):
        """
        Set the value of EN_LOADIMP_LDO_TPAD
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG1', 'EN_LOADIMP_LDO_TPAD', value)

    # EN_LOADIMP_LDO_TXBUF
    @property 
    def EN_LOADIMP_LDO_TXBUF(self):
        """
        Get the value of EN_LOADIMP_LDO_TXBUF
        """
        return self._readReg('CFG1', 'EN_LOADIMP_LDO_TXBUF')

    @EN_LOADIMP_LDO_TXBUF.setter
    def EN_LOADIMP_LDO_TXBUF(self, value):
        """
        Set the value of EN_LOADIMP_LDO_TXBUF
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG1', 'EN_LOADIMP_LDO_TXBUF', value)

    # EN_LOADIMP_LDO_VCOGN
    @property 
    def EN_LOADIMP_LDO_VCOGN(self):
        """
        Get the value of EN_LOADIMP_LDO_VCOGN
        """
        return self._readReg('CFG1', 'EN_LOADIMP_LDO_VCOGN')

    @EN_LOADIMP_LDO_VCOGN.setter
    def EN_LOADIMP_LDO_VCOGN(self, value):
        """
        Set the value of EN_LOADIMP_LDO_VCOGN
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG1', 'EN_LOADIMP_LDO_VCOGN', value)

    # EN_LOADIMP_LDO_VCOSXR
    @property 
    def EN_LOADIMP_LDO_VCOSXR(self):
        """
        Get the value of EN_LOADIMP_LDO_VCOSXR
        """
        return self._readReg('CFG1', 'EN_LOADIMP_LDO_VCOSXR')

    @EN_LOADIMP_LDO_VCOSXR.setter
    def EN_LOADIMP_LDO_VCOSXR(self, value):
        """
        Set the value of EN_LOADIMP_LDO_VCOSXR
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG1', 'EN_LOADIMP_LDO_VCOSXR', value)

    # EN_LOADIMP_LDO_VCOSXT
    @property 
    def EN_LOADIMP_LDO_VCOSXT(self):
        """
        Get the value of EN_LOADIMP_LDO_VCOSXT
        """
        return self._readReg('CFG1', 'EN_LOADIMP_LDO_VCOSXT')

    @EN_LOADIMP_LDO_VCOSXT.setter
    def EN_LOADIMP_LDO_VCOSXT(self, value):
        """
        Set the value of EN_LOADIMP_LDO_VCOSXT
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG1', 'EN_LOADIMP_LDO_VCOSXT', value)

    # EN_LDO_AFE
    @property 
    def EN_LDO_AFE(self):
        """
        Get the value of EN_LDO_AFE
        """
        return self._readReg('CFG1', 'EN_LDO_AFE')

    @EN_LDO_AFE.setter
    def EN_LDO_AFE(self, value):
        """
        Set the value of EN_LDO_AFE
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG1', 'EN_LDO_AFE', value)

    # EN_LDO_CPGN
    @property 
    def EN_LDO_CPGN(self):
        """
        Get the value of EN_LDO_CPGN
        """
        return self._readReg('CFG1', 'EN_LDO_CPGN')

    @EN_LDO_CPGN.setter
    def EN_LDO_CPGN(self, value):
        """
        Set the value of EN_LDO_CPGN
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG1', 'EN_LDO_CPGN', value)

    # EN_LDO_CPSXR
    @property 
    def EN_LDO_CPSXR(self):
        """
        Get the value of EN_LDO_CPSXR
        """
        return self._readReg('CFG1', 'EN_LDO_CPSXR')

    @EN_LDO_CPSXR.setter
    def EN_LDO_CPSXR(self, value):
        """
        Set the value of EN_LDO_CPSXR
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG1', 'EN_LDO_CPSXR', value)

    # EN_LDO_TLOB
    @property 
    def EN_LDO_TLOB(self):
        """
        Get the value of EN_LDO_TLOB
        """
        return self._readReg('CFG1', 'EN_LDO_TLOB')

    @EN_LDO_TLOB.setter
    def EN_LDO_TLOB(self, value):
        """
        Set the value of EN_LDO_TLOB
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG1', 'EN_LDO_TLOB', value)

    # EN_LDO_TPAD
    @property 
    def EN_LDO_TPAD(self):
        """
        Get the value of EN_LDO_TPAD
        """
        return self._readReg('CFG1', 'EN_LDO_TPAD')

    @EN_LDO_TPAD.setter
    def EN_LDO_TPAD(self, value):
        """
        Set the value of EN_LDO_TPAD
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG1', 'EN_LDO_TPAD', value)

    # EN_LDO_TXBUF
    @property 
    def EN_LDO_TXBUF(self):
        """
        Get the value of EN_LDO_TXBUF
        """
        return self._readReg('CFG1', 'EN_LDO_TXBUF')

    @EN_LDO_TXBUF.setter
    def EN_LDO_TXBUF(self, value):
        """
        Set the value of EN_LDO_TXBUF
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG1', 'EN_LDO_TXBUF', value)

    # EN_LDO_VCOGN
    @property 
    def EN_LDO_VCOGN(self):
        """
        Get the value of EN_LDO_VCOGN
        """
        return self._readReg('CFG1', 'EN_LDO_VCOGN')

    @EN_LDO_VCOGN.setter
    def EN_LDO_VCOGN(self, value):
        """
        Set the value of EN_LDO_VCOGN
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG1', 'EN_LDO_VCOGN', value)

    # EN_LDO_VCOSXR
    @property 
    def EN_LDO_VCOSXR(self):
        """
        Get the value of EN_LDO_VCOSXR
        """
        return self._readReg('CFG1', 'EN_LDO_VCOSXR')

    @EN_LDO_VCOSXR.setter
    def EN_LDO_VCOSXR(self, value):
        """
        Set the value of EN_LDO_VCOSXR
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG1', 'EN_LDO_VCOSXR', value)

    # EN_LDO_VCOSXT
    @property 
    def EN_LDO_VCOSXT(self):
        """
        Get the value of EN_LDO_VCOSXT
        """
        return self._readReg('CFG1', 'EN_LDO_VCOSXT')

    @EN_LDO_VCOSXT.setter
    def EN_LDO_VCOSXT(self, value):
        """
        Set the value of EN_LDO_VCOSXT
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG1', 'EN_LDO_VCOSXT', value)

    # EN_LDO_CPSXT
    @property 
    def EN_LDO_CPSXT(self):
        """
        Get the value of EN_LDO_CPSXT
        """
        return self._readReg('CFG1', 'EN_LDO_CPSXT')

    @EN_LDO_CPSXT.setter
    def EN_LDO_CPSXT(self, value):
        """
        Set the value of EN_LDO_CPSXT
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG1', 'EN_LDO_CPSXT', value)

    #
    # BIAS_CFG2 (0x0094)
    #    

    # EN_LOADIMP_LDO_CPSXT
    @property 
    def EN_LOADIMP_LDO_CPSXT(self):
        """
        Get the value of EN_LOADIMP_LDO_CPSXT
        """
        return self._readReg('CFG2', 'EN_LOADIMP_LDO_CPSXT')

    @EN_LOADIMP_LDO_CPSXT.setter
    def EN_LOADIMP_LDO_CPSXT(self, value):
        """
        Set the value of EN_LOADIMP_LDO_CPSXT
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG2', 'EN_LOADIMP_LDO_CPSXT', value)

    # EN_LOADIMP_LDO_DIG
    @property 
    def EN_LOADIMP_LDO_DIG(self):
        """
        Get the value of EN_LOADIMP_LDO_DIG
        """
        return self._readReg('CFG2', 'EN_LOADIMP_LDO_DIG')

    @EN_LOADIMP_LDO_DIG.setter
    def EN_LOADIMP_LDO_DIG(self, value):
        """
        Set the value of EN_LOADIMP_LDO_DIG
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG2', 'EN_LOADIMP_LDO_DIG', value)

    # EN_LOADIMP_LDO_DIGGN
    @property 
    def EN_LOADIMP_LDO_DIGGN(self):
        """
        Get the value of EN_LOADIMP_LDO_DIGGN
        """
        return self._readReg('CFG2', 'EN_LOADIMP_LDO_DIGGN')

    @EN_LOADIMP_LDO_DIGGN.setter
    def EN_LOADIMP_LDO_DIGGN(self, value):
        """
        Set the value of EN_LOADIMP_LDO_DIGGN
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG2', 'EN_LOADIMP_LDO_DIGGN', value)

    # EN_LOADIMP_LDO_DIGSXR
    @property 
    def EN_LOADIMP_LDO_DIGSXR(self):
        """
        Get the value of EN_LOADIMP_LDO_DIGSXR
        """
        return self._readReg('CFG2', 'EN_LOADIMP_LDO_DIGSXR')

    @EN_LOADIMP_LDO_DIGSXR.setter
    def EN_LOADIMP_LDO_DIGSXR(self, value):
        """
        Set the value of EN_LOADIMP_LDO_DIGSXR
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG2', 'EN_LOADIMP_LDO_DIGSXR', value)

    # EN_LOADIMP_LDO_DIGSXT
    @property 
    def EN_LOADIMP_LDO_DIGSXT(self):
        """
        Get the value of EN_LOADIMP_LDO_DIGSXT
        """
        return self._readReg('CFG2', 'EN_LOADIMP_LDO_DIGSXT')

    @EN_LOADIMP_LDO_DIGSXT.setter
    def EN_LOADIMP_LDO_DIGSXT(self, value):
        """
        Set the value of EN_LOADIMP_LDO_DIGSXT
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG2', 'EN_LOADIMP_LDO_DIGSXT', value)

    # EN_LOADIMP_LDO_DIVGN
    @property 
    def EN_LOADIMP_LDO_DIVGN(self):
        """
        Get the value of EN_LOADIMP_LDO_DIVGN
        """
        return self._readReg('CFG2', 'EN_LOADIMP_LDO_DIVGN')

    @EN_LOADIMP_LDO_DIVGN.setter
    def EN_LOADIMP_LDO_DIVGN(self, value):
        """
        Set the value of EN_LOADIMP_LDO_DIVGN
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG2', 'EN_LOADIMP_LDO_DIVGN', value)

    # EN_LOADIMP_LDO_DIVSXR
    @property 
    def EN_LOADIMP_LDO_DIVSXR(self):
        """
        Get the value of EN_LOADIMP_LDO_DIVSXR
        """
        return self._readReg('CFG2', 'EN_LOADIMP_LDO_DIVSXR')

    @EN_LOADIMP_LDO_DIVSXR.setter
    def EN_LOADIMP_LDO_DIVSXR(self, value):
        """
        Set the value of EN_LOADIMP_LDO_DIVSXR
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG2', 'EN_LOADIMP_LDO_DIVSXR', value)

    # EN_LOADIMP_LDO_DIVSXT
    @property 
    def EN_LOADIMP_LDO_DIVSXT(self):
        """
        Get the value of EN_LOADIMP_LDO_DIVSXT
        """
        return self._readReg('CFG2', 'EN_LOADIMP_LDO_DIVSXT')

    @EN_LOADIMP_LDO_DIVSXT.setter
    def EN_LOADIMP_LDO_DIVSXT(self, value):
        """
        Set the value of EN_LOADIMP_LDO_DIVSXT
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG2', 'EN_LOADIMP_LDO_DIVSXT', value)

    # EN_LOADIMP_LDO_LNA12
    @property 
    def EN_LOADIMP_LDO_LNA12(self):
        """
        Get the value of EN_LOADIMP_LDO_LNA12
        """
        return self._readReg('CFG2', 'EN_LOADIMP_LDO_LNA12')

    @EN_LOADIMP_LDO_LNA12.setter
    def EN_LOADIMP_LDO_LNA12(self, value):
        """
        Set the value of EN_LOADIMP_LDO_LNA12
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG2', 'EN_LOADIMP_LDO_LNA12', value)

    # EN_LOADIMP_LDO_LNA14
    @property 
    def EN_LOADIMP_LDO_LNA14(self):
        """
        Get the value of EN_LOADIMP_LDO_LNA14
        """
        return self._readReg('CFG2', 'EN_LOADIMP_LDO_LNA14')

    @EN_LOADIMP_LDO_LNA14.setter
    def EN_LOADIMP_LDO_LNA14(self, value):
        """
        Set the value of EN_LOADIMP_LDO_LNA14
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG2', 'EN_LOADIMP_LDO_LNA14', value)

    # EN_LOADIMP_LDO_MXRFE
    @property 
    def EN_LOADIMP_LDO_MXRFE(self):
        """
        Get the value of EN_LOADIMP_LDO_MXRFE
        """
        return self._readReg('CFG2', 'EN_LOADIMP_LDO_MXRFE')

    @EN_LOADIMP_LDO_MXRFE.setter
    def EN_LOADIMP_LDO_MXRFE(self, value):
        """
        Set the value of EN_LOADIMP_LDO_MXRFE
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG2', 'EN_LOADIMP_LDO_MXRFE', value)

    # EN_LOADIMP_LDO_RBB
    @property 
    def EN_LOADIMP_LDO_RBB(self):
        """
        Get the value of EN_LOADIMP_LDO_RBB
        """
        return self._readReg('CFG2', 'EN_LOADIMP_LDO_RBB')

    @EN_LOADIMP_LDO_RBB.setter
    def EN_LOADIMP_LDO_RBB(self, value):
        """
        Set the value of EN_LOADIMP_LDO_RBB
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG2', 'EN_LOADIMP_LDO_RBB', value)

    # EN_LOADIMP_LDO_RXBUF
    @property 
    def EN_LOADIMP_LDO_RXBUF(self):
        """
        Get the value of EN_LOADIMP_LDO_RXBUF
        """
        return self._readReg('CFG2', 'EN_LOADIMP_LDO_RXBUF')

    @EN_LOADIMP_LDO_RXBUF.setter
    def EN_LOADIMP_LDO_RXBUF(self, value):
        """
        Set the value of EN_LOADIMP_LDO_RXBUF
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG2', 'EN_LOADIMP_LDO_RXBUF', value)

    # EN_LOADIMP_LDO_TBB
    @property 
    def EN_LOADIMP_LDO_TBB(self):
        """
        Get the value of EN_LOADIMP_LDO_TBB
        """
        return self._readReg('CFG2', 'EN_LOADIMP_LDO_TBB')

    @EN_LOADIMP_LDO_TBB.setter
    def EN_LOADIMP_LDO_TBB(self, value):
        """
        Set the value of EN_LOADIMP_LDO_TBB
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG2', 'EN_LOADIMP_LDO_TBB', value)

    # EN_LOADIMP_LDO_TIA12
    @property 
    def EN_LOADIMP_LDO_TIA12(self):
        """
        Get the value of EN_LOADIMP_LDO_TIA12
        """
        return self._readReg('CFG2', 'EN_LOADIMP_LDO_TIA12')

    @EN_LOADIMP_LDO_TIA12.setter
    def EN_LOADIMP_LDO_TIA12(self, value):
        """
        Set the value of EN_LOADIMP_LDO_TIA12
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG2', 'EN_LOADIMP_LDO_TIA12', value)

    # EN_LOADIMP_LDO_TIA14
    @property 
    def EN_LOADIMP_LDO_TIA14(self):
        """
        Get the value of EN_LOADIMP_LDO_TIA14
        """
        return self._readReg('CFG2', 'EN_LOADIMP_LDO_TIA14')

    @EN_LOADIMP_LDO_TIA14.setter
    def EN_LOADIMP_LDO_TIA14(self, value):
        """
        Set the value of EN_LOADIMP_LDO_TIA14
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG2', 'EN_LOADIMP_LDO_TIA14', value)

    #
    # BIAS_CFG3 (0x0095)
    #    
    
    # BYP_LDO_TBB
    @property 
    def BYP_LDO_TBB(self):
        """
        Get the value of BYP_LDO_TBB
        """
        return self._readReg('CFG3', 'BYP_LDO_TBB')

    @BYP_LDO_TBB.setter
    def BYP_LDO_TBB(self, value):
        """
        Set the value of BYP_LDO_TBB
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG3', 'BYP_LDO_TBB', value)

    # BYP_LDO_TIA12
    @property 
    def BYP_LDO_TIA12(self):
        """
        Get the value of BYP_LDO_TIA12
        """
        return self._readReg('CFG3', 'BYP_LDO_TIA12')

    @BYP_LDO_TIA12.setter
    def BYP_LDO_TIA12(self, value):
        """
        Set the value of BYP_LDO_TIA12
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG3', 'BYP_LDO_TIA12', value)

    # BYP_LDO_TIA14
    @property 
    def BYP_LDO_TIA14(self):
        """
        Get the value of BYP_LDO_TIA14
        """
        return self._readReg('CFG3', 'BYP_LDO_TIA14')

    @BYP_LDO_TIA14.setter
    def BYP_LDO_TIA14(self, value):
        """
        Set the value of BYP_LDO_TIA14
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG3', 'BYP_LDO_TIA14', value)

    # BYP_LDO_TLOB
    @property 
    def BYP_LDO_TLOB(self):
        """
        Get the value of BYP_LDO_TLOB
        """
        return self._readReg('CFG3', 'BYP_LDO_TLOB')

    @BYP_LDO_TLOB.setter
    def BYP_LDO_TLOB(self, value):
        """
        Set the value of BYP_LDO_TLOB
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG3', 'BYP_LDO_TLOB', value)

    # BYP_LDO_TPAD
    @property 
    def BYP_LDO_TPAD(self):
        """
        Get the value of BYP_LDO_TPAD
        """
        return self._readReg('CFG3', 'BYP_LDO_TPAD')

    @BYP_LDO_TPAD.setter
    def BYP_LDO_TPAD(self, value):
        """
        Set the value of BYP_LDO_TPAD
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG3', 'BYP_LDO_TPAD', value)

    # BYP_LDO_TXBUF
    @property 
    def BYP_LDO_TXBUF(self):
        """
        Get the value of BYP_LDO_TXBUF
        """
        return self._readReg('CFG3', 'BYP_LDO_TXBUF')

    @BYP_LDO_TXBUF.setter
    def BYP_LDO_TXBUF(self, value):
        """
        Set the value of BYP_LDO_TXBUF
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG3', 'BYP_LDO_TXBUF', value)

    # BYP_LDO_VCOGN
    @property 
    def BYP_LDO_VCOGN(self):
        """
        Get the value of BYP_LDO_VCOGN
        """
        return self._readReg('CFG3', 'BYP_LDO_VCOGN')

    @BYP_LDO_VCOGN.setter
    def BYP_LDO_VCOGN(self, value):
        """
        Set the value of BYP_LDO_VCOGN
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG3', 'BYP_LDO_VCOGN', value)

    # BYP_LDO_VCOSXR
    @property 
    def BYP_LDO_VCOSXR(self):
        """
        Get the value of BYP_LDO_VCOSXR
        """
        return self._readReg('CFG3', 'BYP_LDO_VCOSXR')

    @BYP_LDO_VCOSXR.setter
    def BYP_LDO_VCOSXR(self, value):
        """
        Set the value of BYP_LDO_VCOSXR
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG3', 'BYP_LDO_VCOSXR', value)

    # BYP_LDO_VCOSXT
    @property 
    def BYP_LDO_VCOSXT(self):
        """
        Get the value of BYP_LDO_VCOSXT
        """
        return self._readReg('CFG3', 'BYP_LDO_VCOSXT')

    @BYP_LDO_VCOSXT.setter
    def BYP_LDO_VCOSXT(self, value):
        """
        Set the value of BYP_LDO_VCOSXT
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG3', 'BYP_LDO_VCOSXT', value)

    # EN_LOADIMP_LDO_AFE
    @property 
    def EN_LOADIMP_LDO_AFE(self):
        """
        Get the value of EN_LOADIMP_LDO_AFE
        """
        return self._readReg('CFG3', 'EN_LOADIMP_LDO_AFE')

    @EN_LOADIMP_LDO_AFE.setter
    def EN_LOADIMP_LDO_AFE(self, value):
        """
        Set the value of EN_LOADIMP_LDO_AFE
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG3', 'EN_LOADIMP_LDO_AFE', value)

    # EN_LOADIMP_LDO_CPGN
    @property 
    def EN_LOADIMP_LDO_CPGN(self):
        """
        Get the value of EN_LOADIMP_LDO_CPGN
        """
        return self._readReg('CFG3', 'EN_LOADIMP_LDO_CPGN')

    @EN_LOADIMP_LDO_CPGN.setter
    def EN_LOADIMP_LDO_CPGN(self, value):
        """
        Set the value of EN_LOADIMP_LDO_CPGN
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG3', 'EN_LOADIMP_LDO_CPGN', value)

    # EN_LOADIMP_LDO_CPSXR
    @property 
    def EN_LOADIMP_LDO_CPSXR(self):
        """
        Get the value of EN_LOADIMP_LDO_CPSXR
        """
        return self._readReg('CFG3', 'EN_LOADIMP_LDO_CPSXR')

    @EN_LOADIMP_LDO_CPSXR.setter
    def EN_LOADIMP_LDO_CPSXR(self, value):
        """
        Set the value of EN_LOADIMP_LDO_CPSXR
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG3', 'EN_LOADIMP_LDO_CPSXR', value)

    #
    # BIAS_CFG4 (0x0096)
    #    

    # BYP_LDO_AFE
    @property 
    def BYP_LDO_AFE(self):
        """
        Get the value of BYP_LDO_AFE
        """
        return self._readReg('CFG4', 'BYP_LDO_AFE')

    @BYP_LDO_AFE.setter
    def BYP_LDO_AFE(self, value):
        """
        Set the value of BYP_LDO_AFE
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG4', 'BYP_LDO_AFE', value)

    # BYP_LDO_CPGN
    @property 
    def BYP_LDO_CPGN(self):
        """
        Get the value of BYP_LDO_CPGN
        """
        return self._readReg('CFG4', 'BYP_LDO_CPGN')

    @BYP_LDO_CPGN.setter
    def BYP_LDO_CPGN(self, value):
        """
        Set the value of BYP_LDO_CPGN
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG4', 'BYP_LDO_CPGN', value)

    # BYP_LDO_CPSXR
    @property 
    def BYP_LDO_CPSXR(self):
        """
        Get the value of BYP_LDO_CPSXR
        """
        return self._readReg('CFG4', 'BYP_LDO_CPSXR')

    @BYP_LDO_CPSXR.setter
    def BYP_LDO_CPSXR(self, value):
        """
        Set the value of BYP_LDO_CPSXR
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG4', 'BYP_LDO_CPSXR', value)

    # BYP_LDO_CPSXT
    @property 
    def BYP_LDO_CPSXT(self):
        """
        Get the value of BYP_LDO_CPSXT
        """
        return self._readReg('CFG4', 'BYP_LDO_CPSXT')

    @BYP_LDO_CPSXT.setter
    def BYP_LDO_CPSXT(self, value):
        """
        Set the value of BYP_LDO_CPSXT
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG4', 'BYP_LDO_CPSXT', value)

    # BYP_LDO_DIG
    @property 
    def BYP_LDO_DIG(self):
        """
        Get the value of BYP_LDO_DIG
        """
        return self._readReg('CFG4', 'BYP_LDO_DIG')

    @BYP_LDO_DIG.setter
    def BYP_LDO_DIG(self, value):
        """
        Set the value of BYP_LDO_DIG
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG4', 'BYP_LDO_DIG', value)

    # BYP_LDO_DIGGN
    @property 
    def BYP_LDO_DIGGN(self):
        """
        Get the value of BYP_LDO_DIGGN
        """
        return self._readReg('CFG4', 'BYP_LDO_DIGGN')

    @BYP_LDO_DIGGN.setter
    def BYP_LDO_DIGGN(self, value):
        """
        Set the value of BYP_LDO_DIGGN
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG4', 'BYP_LDO_DIGGN', value)

    # BYP_LDO_DIGSXR
    @property 
    def BYP_LDO_DIGSXR(self):
        """
        Get the value of BYP_LDO_DIGSXR
        """
        return self._readReg('CFG4', 'BYP_LDO_DIGSXR')

    @BYP_LDO_DIGSXR.setter
    def BYP_LDO_DIGSXR(self, value):
        """
        Set the value of BYP_LDO_DIGSXR
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG4', 'BYP_LDO_DIGSXR', value)

    # BYP_LDO_DIGSXT
    @property 
    def BYP_LDO_DIGSXT(self):
        """
        Get the value of BYP_LDO_DIGSXT
        """
        return self._readReg('CFG4', 'BYP_LDO_DIGSXT')

    @BYP_LDO_DIGSXT.setter
    def BYP_LDO_DIGSXT(self, value):
        """
        Set the value of BYP_LDO_DIGSXT
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG4', 'BYP_LDO_DIGSXT', value)

    # BYP_LDO_DIVGN
    @property 
    def BYP_LDO_DIVGN(self):
        """
        Get the value of BYP_LDO_DIVGN
        """
        return self._readReg('CFG4', 'BYP_LDO_DIVGN')

    @BYP_LDO_DIVGN.setter
    def BYP_LDO_DIVGN(self, value):
        """
        Set the value of BYP_LDO_DIVGN
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG4', 'BYP_LDO_DIVGN', value)

    # BYP_LDO_DIVSXR
    @property 
    def BYP_LDO_DIVSXR(self):
        """
        Get the value of BYP_LDO_DIVSXR
        """
        return self._readReg('CFG4', 'BYP_LDO_DIVSXR')

    @BYP_LDO_DIVSXR.setter
    def BYP_LDO_DIVSXR(self, value):
        """
        Set the value of BYP_LDO_DIVSXR
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG4', 'BYP_LDO_DIVSXR', value)

    # BYP_LDO_DIVSXT
    @property 
    def BYP_LDO_DIVSXT(self):
        """
        Get the value of BYP_LDO_DIVSXT
        """
        return self._readReg('CFG4', 'BYP_LDO_DIVSXT')

    @BYP_LDO_DIVSXT.setter
    def BYP_LDO_DIVSXT(self, value):
        """
        Set the value of BYP_LDO_DIVSXT
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG4', 'BYP_LDO_DIVSXT', value)

    # BYP_LDO_LNA12
    @property 
    def BYP_LDO_LNA12(self):
        """
        Get the value of BYP_LDO_LNA12
        """
        return self._readReg('CFG4', 'BYP_LDO_LNA12')

    @BYP_LDO_LNA12.setter
    def BYP_LDO_LNA12(self, value):
        """
        Set the value of BYP_LDO_LNA12
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG4', 'BYP_LDO_LNA12', value)

    # BYP_LDO_LNA14
    @property 
    def BYP_LDO_LNA14(self):
        """
        Get the value of BYP_LDO_LNA14
        """
        return self._readReg('CFG4', 'BYP_LDO_LNA14')

    @BYP_LDO_LNA14.setter
    def BYP_LDO_LNA14(self, value):
        """
        Set the value of BYP_LDO_LNA14
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG4', 'BYP_LDO_LNA14', value)

    # BYP_LDO_MXRFE
    @property 
    def BYP_LDO_MXRFE(self):
        """
        Get the value of BYP_LDO_MXRFE
        """
        return self._readReg('CFG4', 'BYP_LDO_MXRFE')

    @BYP_LDO_MXRFE.setter
    def BYP_LDO_MXRFE(self, value):
        """
        Set the value of BYP_LDO_MXRFE
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG4', 'BYP_LDO_MXRFE', value)

    # BYP_LDO_RBB
    @property 
    def BYP_LDO_RBB(self):
        """
        Get the value of BYP_LDO_RBB
        """
        return self._readReg('CFG4', 'BYP_LDO_RBB')

    @BYP_LDO_RBB.setter
    def BYP_LDO_RBB(self, value):
        """
        Set the value of BYP_LDO_RBB
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG4', 'BYP_LDO_RBB', value)

    # BYP_LDO_RXBUF
    @property 
    def BYP_LDO_RXBUF(self):
        """
        Get the value of BYP_LDO_RXBUF
        """
        return self._readReg('CFG4', 'BYP_LDO_RXBUF')

    @BYP_LDO_RXBUF.setter
    def BYP_LDO_RXBUF(self, value):
        """
        Set the value of BYP_LDO_RXBUF
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG4', 'BYP_LDO_RXBUF', value)

    #
    # BIAS_CFG5 (0x0097)
    #
    
    # SPDUP_LDO_DIVSXR
    @property 
    def SPDUP_LDO_DIVSXR(self):
        """
        Get the value of SPDUP_LDO_DIVSXR
        """
        return self._readReg('CFG5', 'SPDUP_LDO_DIVSXR')

    @SPDUP_LDO_DIVSXR.setter
    def SPDUP_LDO_DIVSXR(self, value):
        """
        Set the value of SPDUP_LDO_DIVSXR
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG5', 'SPDUP_LDO_DIVSXR', value)

    # SPDUP_LDO_DIVSXT
    @property 
    def SPDUP_LDO_DIVSXT(self):
        """
        Get the value of SPDUP_LDO_DIVSXT
        """
        return self._readReg('CFG5', 'SPDUP_LDO_DIVSXT')

    @SPDUP_LDO_DIVSXT.setter
    def SPDUP_LDO_DIVSXT(self, value):
        """
        Set the value of SPDUP_LDO_DIVSXT
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG5', 'SPDUP_LDO_DIVSXT', value)

    # SPDUP_LDO_LNA12
    @property 
    def SPDUP_LDO_LNA12(self):
        """
        Get the value of SPDUP_LDO_LNA12
        """
        return self._readReg('CFG5', 'SPDUP_LDO_LNA12')

    @SPDUP_LDO_LNA12.setter
    def SPDUP_LDO_LNA12(self, value):
        """
        Set the value of SPDUP_LDO_LNA12
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG5', 'SPDUP_LDO_LNA12', value)

    # SPDUP_LDO_LNA14
    @property 
    def SPDUP_LDO_LNA14(self):
        """
        Get the value of SPDUP_LDO_LNA14
        """
        return self._readReg('CFG5', 'SPDUP_LDO_LNA14')

    @SPDUP_LDO_LNA14.setter
    def SPDUP_LDO_LNA14(self, value):
        """
        Set the value of SPDUP_LDO_LNA14
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG5', 'SPDUP_LDO_LNA14', value)

    # SPDUP_LDO_MXRFE
    @property 
    def SPDUP_LDO_MXRFE(self):
        """
        Get the value of SPDUP_LDO_MXRFE
        """
        return self._readReg('CFG5', 'SPDUP_LDO_MXRFE')

    @SPDUP_LDO_MXRFE.setter
    def SPDUP_LDO_MXRFE(self, value):
        """
        Set the value of SPDUP_LDO_MXRFE
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG5', 'SPDUP_LDO_MXRFE', value)

    # SPDUP_LDO_RBB
    @property 
    def SPDUP_LDO_RBB(self):
        """
        Get the value of SPDUP_LDO_RBB
        """
        return self._readReg('CFG5', 'SPDUP_LDO_RBB')

    @SPDUP_LDO_RBB.setter
    def SPDUP_LDO_RBB(self, value):
        """
        Set the value of SPDUP_LDO_RBB
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG5', 'SPDUP_LDO_RBB', value)

    # SPDUP_LDO_RXBUF
    @property 
    def SPDUP_LDO_RXBUF(self):
        """
        Get the value of SPDUP_LDO_RXBUF
        """
        return self._readReg('CFG5', 'SPDUP_LDO_RXBUF')

    @SPDUP_LDO_RXBUF.setter
    def SPDUP_LDO_RXBUF(self, value):
        """
        Set the value of SPDUP_LDO_RXBUF
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG5', 'SPDUP_LDO_RXBUF', value)

    # SPDUP_LDO_TBB
    @property 
    def SPDUP_LDO_TBB(self):
        """
        Get the value of SPDUP_LDO_TBB
        """
        return self._readReg('CFG5', 'SPDUP_LDO_TBB')

    @SPDUP_LDO_TBB.setter
    def SPDUP_LDO_TBB(self, value):
        """
        Set the value of SPDUP_LDO_TBB
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG5', 'SPDUP_LDO_TBB', value)

    # SPDUP_LDO_TIA12
    @property 
    def SPDUP_LDO_TIA12(self):
        """
        Get the value of SPDUP_LDO_TIA12
        """
        return self._readReg('CFG5', 'SPDUP_LDO_TIA12')

    @SPDUP_LDO_TIA12.setter
    def SPDUP_LDO_TIA12(self, value):
        """
        Set the value of SPDUP_LDO_TIA12
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG5', 'SPDUP_LDO_TIA12', value)

    # SPDUP_LDO_TIA14
    @property 
    def SPDUP_LDO_TIA14(self):
        """
        Get the value of SPDUP_LDO_TIA14
        """
        return self._readReg('CFG5', 'SPDUP_LDO_TIA14')

    @SPDUP_LDO_TIA14.setter
    def SPDUP_LDO_TIA14(self, value):
        """
        Set the value of SPDUP_LDO_TIA14
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG5', 'SPDUP_LDO_TIA14', value)

    # SPDUP_LDO_TLOB
    @property 
    def SPDUP_LDO_TLOB(self):
        """
        Get the value of SPDUP_LDO_TLOB
        """
        return self._readReg('CFG5', 'SPDUP_LDO_TLOB')

    @SPDUP_LDO_TLOB.setter
    def SPDUP_LDO_TLOB(self, value):
        """
        Set the value of SPDUP_LDO_TLOB
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG5', 'SPDUP_LDO_TLOB', value)

    # SPDUP_LDO_TPAD
    @property 
    def SPDUP_LDO_TPAD(self):
        """
        Get the value of SPDUP_LDO_TPAD
        """
        return self._readReg('CFG5', 'SPDUP_LDO_TPAD')

    @SPDUP_LDO_TPAD.setter
    def SPDUP_LDO_TPAD(self, value):
        """
        Set the value of SPDUP_LDO_TPAD
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG5', 'SPDUP_LDO_TPAD', value)

    # SPDUP_LDO_TXBUF
    @property 
    def SPDUP_LDO_TXBUF(self):
        """
        Get the value of SPDUP_LDO_TXBUF
        """
        return self._readReg('CFG5', 'SPDUP_LDO_TXBUF')

    @SPDUP_LDO_TXBUF.setter
    def SPDUP_LDO_TXBUF(self, value):
        """
        Set the value of SPDUP_LDO_TXBUF
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG5', 'SPDUP_LDO_TXBUF', value)

    # SPDUP_LDO_VCOGN
    @property 
    def SPDUP_LDO_VCOGN(self):
        """
        Get the value of SPDUP_LDO_VCOGN
        """
        return self._readReg('CFG5', 'SPDUP_LDO_VCOGN')

    @SPDUP_LDO_VCOGN.setter
    def SPDUP_LDO_VCOGN(self, value):
        """
        Set the value of SPDUP_LDO_VCOGN
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG5', 'SPDUP_LDO_VCOGN', value)

    # SPDUP_LDO_VCOSXR
    @property 
    def SPDUP_LDO_VCOSXR(self):
        """
        Get the value of SPDUP_LDO_VCOSXR
        """
        return self._readReg('CFG5', 'SPDUP_LDO_VCOSXR')

    @SPDUP_LDO_VCOSXR.setter
    def SPDUP_LDO_VCOSXR(self, value):
        """
        Set the value of SPDUP_LDO_VCOSXR
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG5', 'SPDUP_LDO_VCOSXR', value)

    # SPDUP_LDO_VCOSXT
    @property 
    def SPDUP_LDO_VCOSXT(self):
        """
        Get the value of SPDUP_LDO_VCOSXT
        """
        return self._readReg('CFG5', 'SPDUP_LDO_VCOSXT')

    @SPDUP_LDO_VCOSXT.setter
    def SPDUP_LDO_VCOSXT(self, value):
        """
        Set the value of SPDUP_LDO_VCOSXT
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG5', 'SPDUP_LDO_VCOSXT', value)

    #
    # BIAS_CFG6 (0x0098)
    #

    # SPDUP_LDO_AFE
    @property 
    def SPDUP_LDO_AFE(self):
        """
        Get the value of SPDUP_LDO_AFE
        """
        return self._readReg('CFG6', 'SPDUP_LDO_AFE')

    @SPDUP_LDO_AFE.setter
    def SPDUP_LDO_AFE(self, value):
        """
        Set the value of SPDUP_LDO_AFE
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG6', 'SPDUP_LDO_AFE', value)

    # SPDUP_LDO_CPGN
    @property 
    def SPDUP_LDO_CPGN(self):
        """
        Get the value of SPDUP_LDO_CPGN
        """
        return self._readReg('CFG6', 'SPDUP_LDO_CPGN')

    @SPDUP_LDO_CPGN.setter
    def SPDUP_LDO_CPGN(self, value):
        """
        Set the value of SPDUP_LDO_CPGN
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG6', 'SPDUP_LDO_CPGN', value)

    # SPDUP_LDO_CPSXR
    @property 
    def SPDUP_LDO_CPSXR(self):
        """
        Get the value of SPDUP_LDO_CPSXR
        """
        return self._readReg('CFG6', 'SPDUP_LDO_CPSXR')

    @SPDUP_LDO_CPSXR.setter
    def SPDUP_LDO_CPSXR(self, value):
        """
        Set the value of SPDUP_LDO_CPSXR
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG6', 'SPDUP_LDO_CPSXR', value)

    # SPDUP_LDO_CPSXT
    @property 
    def SPDUP_LDO_CPSXT(self):
        """
        Get the value of SPDUP_LDO_CPSXT
        """
        return self._readReg('CFG6', 'SPDUP_LDO_CPSXT')

    @SPDUP_LDO_CPSXT.setter
    def SPDUP_LDO_CPSXT(self, value):
        """
        Set the value of SPDUP_LDO_CPSXT
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG6', 'SPDUP_LDO_CPSXT', value)

    # SPDUP_LDO_DIG
    @property 
    def SPDUP_LDO_DIG(self):
        """
        Get the value of SPDUP_LDO_DIG
        """
        return self._readReg('CFG6', 'SPDUP_LDO_DIG')

    @SPDUP_LDO_DIG.setter
    def SPDUP_LDO_DIG(self, value):
        """
        Set the value of SPDUP_LDO_DIG
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG6', 'SPDUP_LDO_DIG', value)

    # SPDUP_LDO_DIGGN
    @property 
    def SPDUP_LDO_DIGGN(self):
        """
        Get the value of SPDUP_LDO_DIGGN
        """
        return self._readReg('CFG6', 'SPDUP_LDO_DIGGN')

    @SPDUP_LDO_DIGGN.setter
    def SPDUP_LDO_DIGGN(self, value):
        """
        Set the value of SPDUP_LDO_DIGGN
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG6', 'SPDUP_LDO_DIGGN', value)

    # SPDUP_LDO_DIGSXR
    @property 
    def SPDUP_LDO_DIGSXR(self):
        """
        Get the value of SPDUP_LDO_DIGSXR
        """
        return self._readReg('CFG6', 'SPDUP_LDO_DIGSXR')

    @SPDUP_LDO_DIGSXR.setter
    def SPDUP_LDO_DIGSXR(self, value):
        """
        Set the value of SPDUP_LDO_DIGSXR
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG6', 'SPDUP_LDO_DIGSXR', value)

    # SPDUP_LDO_DIGSXT
    @property 
    def SPDUP_LDO_DIGSXT(self):
        """
        Get the value of SPDUP_LDO_DIGSXT
        """
        return self._readReg('CFG6', 'SPDUP_LDO_DIGSXT')

    @SPDUP_LDO_DIGSXT.setter
    def SPDUP_LDO_DIGSXT(self, value):
        """
        Set the value of SPDUP_LDO_DIGSXT
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG6', 'SPDUP_LDO_DIGSXT', value)

    # SPDUP_LDO_DIVGN
    @property 
    def SPDUP_LDO_DIVGN(self):
        """
        Get the value of SPDUP_LDO_DIVGN
        """
        return self._readReg('CFG6', 'SPDUP_LDO_DIVGN')

    @SPDUP_LDO_DIVGN.setter
    def SPDUP_LDO_DIVGN(self, value):
        """
        Set the value of SPDUP_LDO_DIVGN
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG6', 'SPDUP_LDO_DIVGN', value)

    #
    # BIAS_CFG7 (0x0099)
    #

    # RDIV_VCOSXR<7:0>
    @property 
    def RDIV_VCOSXR(self):
        """
        Get the value of RDIV_VCOSXR<7:0>
        """
        return self._readReg('CFG7', 'RDIV_VCOSXR<7:0>')

    @RDIV_VCOSXR.setter
    def RDIV_VCOSXR(self, value):
        """
        Set the value of RDIV_VCOSXR<7:0>
        """
        if self.allowLDO:
            if not(0<= value <=255):
                raise ValueError("Value must be [0..255]")
            self._writeReg('CFG7', 'RDIV_VCOSXR<7:0>', value)
        else:
            self.chip.log("Changing LDO voltage is not permitted. To change the LDO voltage, set BIAS.allowLDO=True")
            
    # RDIV_VCOSXT<7:0>
    @property 
    def RDIV_VCOSXT(self):
        """
        Get the value of RDIV_VCOSXT<7:0>
        """
        return self._readReg('CFG7', 'RDIV_VCOSXT<7:0>')

    @RDIV_VCOSXT.setter
    def RDIV_VCOSXT(self, value):
        """
        Set the value of RDIV_VCOSXT<7:0>
        """
        if self.allowLDO:
            if not(0<= value <=255):
                raise ValueError("Value must be [0..255]")
            self._writeReg('CFG7', 'RDIV_VCOSXT<7:0>', value)
        else:
            self.chip.log("Changing LDO voltage is not permitted. To change the LDO voltage, set BIAS.allowLDO=True")

    #
    # BIAS_CFG8 (0x009A)
    #

    # RDIV_TXBUF<7:0>
    @property 
    def RDIV_TXBUF(self):
        """
        Get the value of RDIV_TXBUF<7:0>
        """
        return self._readReg('CFG8', 'RDIV_TXBUF<7:0>')

    @RDIV_TXBUF.setter
    def RDIV_TXBUF(self, value):
        """
        Set the value of RDIV_TXBUF<7:0>
        """
        if self.allowLDO:
            if not(0<= value <=255):
                raise ValueError("Value must be [0..255]")
            self._writeReg('CFG8', 'RDIV_TXBUF<7:0>', value)
        else:
            self.chip.log("Changing LDO voltage is not permitted. To change the LDO voltage, set BIAS.allowLDO=True")
            
    # RDIV_VCOGN<7:0>
    @property 
    def RDIV_VCOGN(self):
        """
        Get the value of RDIV_VCOGN<7:0>
        """
        return self._readReg('CFG8', 'RDIV_VCOGN<7:0>')

    @RDIV_VCOGN.setter
    def RDIV_VCOGN(self, value):
        """
        Set the value of RDIV_VCOGN<7:0>
        """
        if self.allowLDO:
            if not(0<= value <=255):
                raise ValueError("Value must be [0..255]")
            self._writeReg('CFG8', 'RDIV_VCOGN<7:0>', value)
        else:
            self.chip.log("Changing LDO voltage is not permitted. To change the LDO voltage, set BIAS.allowLDO=True")

    #
    # BIAS_CFG9 (0x009B)
    #
    
    # RDIV_TLOB<7:0>
    @property 
    def RDIV_TLOB(self):
        """
        Get the value of RDIV_TLOB<7:0>
        """
        return self._readReg('CFG9', 'RDIV_TLOB<7:0>')

    @RDIV_TLOB.setter
    def RDIV_TLOB(self, value):
        """
        Set the value of RDIV_TLOB<7:0>
        """
        if self.allowLDO:
            if not(0<= value <=255):
                raise ValueError("Value must be [0..255]")
            self._writeReg('CFG9', 'RDIV_TLOB<7:0>', value)
        else:
            self.chip.log("Changing LDO voltage is not permitted. To change the LDO voltage, set BIAS.allowLDO=True")
            
    # RDIV_TPAD<7:0>
    @property 
    def RDIV_TPAD(self):
        """
        Get the value of RDIV_TPAD<7:0>
        """
        return self._readReg('CFG9', 'RDIV_TPAD<7:0>')

    @RDIV_TPAD.setter
    def RDIV_TPAD(self, value):
        """
        Set the value of RDIV_TPAD<7:0>
        """
        if self.allowLDO:
            if not(0<= value <=255):
                raise ValueError("Value must be [0..255]")
            self._writeReg('CFG9', 'RDIV_TPAD<7:0>', value)
        else:
            self.chip.log("Changing LDO voltage is not permitted. To change the LDO voltage, set BIAS.allowLDO=True")

    #
    # BIAS_CFG10 (0x009C)
    #

    # RDIV_TIA12<7:0>
    @property 
    def RDIV_TIA12(self):
        """
        Get the value of RDIV_TIA12<7:0>
        """
        return self._readReg('CFG10', 'RDIV_TIA12<7:0>')

    @RDIV_TIA12.setter
    def RDIV_TIA12(self, value):
        """
        Set the value of RDIV_TIA12<7:0>
        """
        if self.allowLDO:
            if not(0<= value <=255):
                raise ValueError("Value must be [0..255]")
            self._writeReg('CFG10', 'RDIV_TIA12<7:0>', value)
        else:
            self.chip.log("Changing LDO voltage is not permitted. To change the LDO voltage, set BIAS.allowLDO=True")
            
    # RDIV_TIA14<7:0>
    @property 
    def RDIV_TIA14(self):
        """
        Get the value of RDIV_TIA14<7:0>
        """
        return self._readReg('CFG10', 'RDIV_TIA14<7:0>')

    @RDIV_TIA14.setter
    def RDIV_TIA14(self, value):
        """
        Set the value of RDIV_TIA14<7:0>
        """
        if self.allowLDO:
            if not(0<= value <=255):
                raise ValueError("Value must be [0..255]")
            self._writeReg('CFG10', 'RDIV_TIA14<7:0>', value)
        else:
            self.chip.log("Changing LDO voltage is not permitted. To change the LDO voltage, set BIAS.allowLDO=True")

    #
    # BIAS_CFG11 (0x009D)
    #

    # RDIV_RXBUF<7:0>
    @property 
    def RDIV_RXBUF(self):
        """
        Get the value of RDIV_RXBUF<7:0>
        """
        return self._readReg('CFG11', 'RDIV_RXBUF<7:0>')

    @RDIV_RXBUF.setter
    def RDIV_RXBUF(self, value):
        """
        Set the value of RDIV_RXBUF<7:0>
        """
        if self.allowLDO:
            if not(0<= value <=255):
                raise ValueError("Value must be [0..255]")
            self._writeReg('CFG11', 'RDIV_RXBUF<7:0>', value)
        else:
            self.chip.log("Changing LDO voltage is not permitted. To change the LDO voltage, set BIAS.allowLDO=True")
            
    # RDIV_TBB<7:0>
    @property 
    def RDIV_TBB(self):
        """
        Get the value of RDIV_TBB<7:0>
        """
        return self._readReg('CFG11', 'RDIV_TBB<7:0>')

    @RDIV_TBB.setter
    def RDIV_TBB(self, value):
        """
        Set the value of RDIV_TBB<7:0>
        """
        if self.allowLDO:
            if not(0<= value <=255):
                raise ValueError("Value must be [0..255]")
            self._writeReg('CFG11', 'RDIV_TBB<7:0>', value)
        else:
            self.chip.log("Changing LDO voltage is not permitted. To change the LDO voltage, set BIAS.allowLDO=True")

    #
    # BIAS_CFG12 (0x009E)
    #

    # RDIV_MXRFE<7:0>
    @property 
    def RDIV_MXRFE(self):
        """
        Get the value of RDIV_MXRFE<7:0>
        """
        return self._readReg('CFG12', 'RDIV_MXRFE<7:0>')

    @RDIV_MXRFE.setter
    def RDIV_MXRFE(self, value):
        """
        Set the value of RDIV_MXRFE<7:0>
        """
        if self.allowLDO:
            if not(0<= value <=255):
                raise ValueError("Value must be [0..255]")
            self._writeReg('CFG12', 'RDIV_MXRFE<7:0>', value)
        else:
            self.chip.log("Changing LDO voltage is not permitted. To change the LDO voltage, set BIAS.allowLDO=True")
            
    # RDIV_RBB<7:0>
    @property 
    def RDIV_RBB(self):
        """
        Get the value of RDIV_RBB<7:0>
        """
        return self._readReg('CFG12', 'RDIV_RBB<7:0>')

    @RDIV_RBB.setter
    def RDIV_RBB(self, value):
        """
        Set the value of RDIV_RBB<7:0>
        """
        if self.allowLDO:
            if not(0<= value <=255):
                raise ValueError("Value must be [0..255]")
            self._writeReg('CFG12', 'RDIV_RBB<7:0>', value)
        else:
            self.chip.log("Changing LDO voltage is not permitted. To change the LDO voltage, set BIAS.allowLDO=True")

    #
    # BIAS_CFG13 (0x009F)
    #

    # RDIV_LNA12<7:0>
    @property 
    def RDIV_LNA12(self):
        """
        Get the value of RDIV_LNA12<7:0>
        """
        return self._readReg('CFG13', 'RDIV_LNA12<7:0>')

    @RDIV_LNA12.setter
    def RDIV_LNA12(self, value):
        """
        Set the value of RDIV_LNA12<7:0>
        """
        if self.allowLDO:
            if not(0<= value <=255):
                raise ValueError("Value must be [0..255]")
            self._writeReg('CFG13', 'RDIV_LNA12<7:0>', value)
        else:
            self.chip.log("Changing LDO voltage is not permitted. To change the LDO voltage, set BIAS.allowLDO=True")
            
    # RDIV_LNA14<7:0>
    @property 
    def RDIV_LNA14(self):
        """
        Get the value of RDIV_LNA14<7:0>
        """
        return self._readReg('CFG13', 'RDIV_LNA14<7:0>')

    @RDIV_LNA14.setter
    def RDIV_LNA14(self, value):
        """
        Set the value of RDIV_LNA14<7:0>
        """
        if self.allowLDO:
            if not(0<= value <=255):
                raise ValueError("Value must be [0..255]")
            self._writeReg('CFG13', 'RDIV_LNA14<7:0>', value)
        else:
            self.chip.log("Changing LDO voltage is not permitted. To change the LDO voltage, set BIAS.allowLDO=True")

    #
    # BIAS_CFG14 (0x00A0)
    #

    # RDIV_DIVSXR<7:0>
    @property 
    def RDIV_DIVSXR(self):
        """
        Get the value of RDIV_DIVSXR<7:0>
        """
        return self._readReg('CFG14', 'RDIV_DIVSXR<7:0>')

    @RDIV_DIVSXR.setter
    def RDIV_DIVSXR(self, value):
        """
        Set the value of RDIV_DIVSXR<7:0>
        """
        if self.allowLDO:
            if not(0<= value <=255):
                raise ValueError("Value must be [0..255]")
            self._writeReg('CFG14', 'RDIV_DIVSXR<7:0>', value)
        else:
            self.chip.log("Changing LDO voltage is not permitted. To change the LDO voltage, set BIAS.allowLDO=True")
            
    # RDIV_DIVSXT<7:0>
    @property 
    def RDIV_DIVSXT(self):
        """
        Get the value of RDIV_DIVSXT<7:0>
        """
        return self._readReg('CFG14', 'RDIV_DIVSXT<7:0>')

    @RDIV_DIVSXT.setter
    def RDIV_DIVSXT(self, value):
        """
        Set the value of RDIV_DIVSXT<7:0>
        """
        if self.allowLDO:
            if not(0<= value <=255):
                raise ValueError("Value must be [0..255]")
            self._writeReg('CFG14', 'RDIV_DIVSXT<7:0>', value)
        else:
            self.chip.log("Changing LDO voltage is not permitted. To change the LDO voltage, set BIAS.allowLDO=True")

    #
    # BIAS_CFG15 (0x00A1)
    #

    # RDIV_DIGSXT<7:0>
    @property 
    def RDIV_DIGSXT(self):
        """
        Get the value of RDIV_DIGSXT<7:0>
        """
        return self._readReg('CFG15', 'RDIV_DIGSXT<7:0>')

    @RDIV_DIGSXT.setter
    def RDIV_DIGSXT(self, value):
        """
        Set the value of RDIV_DIGSXT<7:0>
        """
        if self.allowLDO:
            if not(0<= value <=255):
                raise ValueError("Value must be [0..255]")
            self._writeReg('CFG15', 'RDIV_DIGSXT<7:0>', value)
        else:
            self.chip.log("Changing LDO voltage is not permitted. To change the LDO voltage, set BIAS.allowLDO=True")
            
    # RDIV_DIVGN<7:0>
    @property 
    def RDIV_DIVGN(self):
        """
        Get the value of RDIV_DIVGN<7:0>
        """
        return self._readReg('CFG15', 'RDIV_DIVGN<7:0>')

    @RDIV_DIVGN.setter
    def RDIV_DIVGN(self, value):
        """
        Set the value of RDIV_DIVGN<7:0>
        """
        if self.allowLDO:
            if not(0<= value <=255):
                raise ValueError("Value must be [0..255]")
            self._writeReg('CFG15', 'RDIV_DIVGN<7:0>', value)
        else:
            self.chip.log("Changing LDO voltage is not permitted. To change the LDO voltage, set BIAS.allowLDO=True")

    #
    # BIAS_CFG16 (0x00A2)
    #

    # RDIV_DIGGN<7:0>
    @property 
    def RDIV_DIGGN(self):
        """
        Get the value of RDIV_DIGGN<7:0>
        """
        return self._readReg('CFG16', 'RDIV_DIGGN<7:0>')

    @RDIV_DIGGN.setter
    def RDIV_DIGGN(self, value):
        """
        Set the value of RDIV_DIGGN<7:0>
        """
        if self.allowLDO:
            if not(0<= value <=255):
                raise ValueError("Value must be [0..255]")
            self._writeReg('CFG16', 'RDIV_DIGGN<7:0>', value)
        else:
            self.chip.log("Changing LDO voltage is not permitted. To change the LDO voltage, set BIAS.allowLDO=True")
            
    # RDIV_DIGSXR<7:0>
    @property 
    def RDIV_DIGSXR(self):
        """
        Get the value of RDIV_DIGSXR<7:0>
        """
        return self._readReg('CFG16', 'RDIV_DIGSXR<7:0>')

    @RDIV_DIGSXR.setter
    def RDIV_DIGSXR(self, value):
        """
        Set the value of RDIV_DIGSXR<7:0>
        """
        if self.allowLDO:
            if not(0<= value <=255):
                raise ValueError("Value must be [0..255]")
            self._writeReg('CFG16', 'RDIV_DIGSXR<7:0>', value)
        else:
            self.chip.log("Changing LDO voltage is not permitted. To change the LDO voltage, set BIAS.allowLDO=True")

    #
    # BIAS_CFG17 (0x00A3)
    #

    # RDIV_CPSXT<7:0>
    @property 
    def RDIV_CPSXT(self):
        """
        Get the value of RDIV_CPSXT<7:0>
        """
        return self._readReg('CFG17', 'RDIV_CPSXT<7:0>')

    @RDIV_CPSXT.setter
    def RDIV_CPSXT(self, value):
        """
        Set the value of RDIV_CPSXT<7:0>
        """
        if self.allowLDO:
            if not(0<= value <=255):
                raise ValueError("Value must be [0..255]")
            self._writeReg('CFG17', 'RDIV_CPSXT<7:0>', value)
        else:
            self.chip.log("Changing LDO voltage is not permitted. To change the LDO voltage, set BIAS.allowLDO=True")
            
    # RDIV_DIG<7:0>
    @property 
    def RDIV_DIG(self):
        """
        Get the value of RDIV_DIG<7:0>
        """
        return self._readReg('CFG17', 'RDIV_DIG<7:0>')

    @RDIV_DIG.setter
    def RDIV_DIG(self, value):
        """
        Set the value of RDIV_DIG<7:0>
        """
        if self.allowLDO:
            if not(0<= value <=255):
                raise ValueError("Value must be [0..255]")
            self._writeReg('CFG17', 'RDIV_DIG<7:0>', value)
        else:
            self.chip.log("Changing LDO voltage is not permitted. To change the LDO voltage, set BIAS.allowLDO=True")
            
    #
    # BIAS_CFG18 (0x00A4)
    #
    
    # RDIV_CPGN<7:0>
    @property 
    def RDIV_CPGN(self):
        """
        Get the value of RDIV_CPGN<7:0>
        """
        return self._readReg('CFG18', 'RDIV_CPGN<7:0>')

    @RDIV_CPGN.setter
    def RDIV_CPGN(self, value):
        """
        Set the value of RDIV_CPGN<7:0>
        """
        if self.allowLDO:
            if not(0<= value <=255):
                raise ValueError("Value must be [0..255]")
            self._writeReg('CFG18', 'RDIV_CPGN<7:0>', value)
        else:
            self.chip.log("Changing LDO voltage is not permitted. To change the LDO voltage, set BIAS.allowLDO=True")
            
    # RDIV_CPSXR<7:0>
    @property 
    def RDIV_CPSXR(self):
        """
        Get the value of RDIV_CPSXR<7:0>
        """
        return self._readReg('CFG18', 'RDIV_CPSXR<7:0>')

    @RDIV_CPSXR.setter
    def RDIV_CPSXR(self, value):
        """
        Set the value of RDIV_CPSXR<7:0>
        """
        if self.allowLDO:
            if not(0<= value <=255):
                raise ValueError("Value must be [0..255]")
            self._writeReg('CFG18', 'RDIV_CPSXR<7:0>', value)
        else:
            self.chip.log("Changing LDO voltage is not permitted. To change the LDO voltage, set BIAS.allowLDO=True")
                                                                                                                                                    
    #
    # BIAS_CFG19 (0x00A5)
    #

    # RDIV_SPIBUF<7:0>
    @property 
    def RDIV_SPIBUF(self):
        """
        Get the value of RDIV_SPIBUF<7:0>
        """
        return self._readReg('CFG19', 'RDIV_SPIBUF<7:0>')

    @RDIV_SPIBUF.setter
    def RDIV_SPIBUF(self, value):
        """
        Set the value of RDIV_SPIBUF<7:0>
        """
        if self.allowLDO:
            if not(0<= value <=255):
                raise ValueError("Value must be [0..255]")
            self._writeReg('CFG19', 'RDIV_SPIBUF<7:0>', value)
        else:
            self.chip.log("Changing LDO voltage is not permitted. To change the LDO voltage, set BIAS.allowLDO=True")
            
    # RDIV_AFE<7:0>
    @property 
    def RDIV_AFE(self):
        """
        Get the value of RDIV_AFE<7:0>
        """
        return self._readReg('CFG19', 'RDIV_AFE<7:0>')

    @RDIV_AFE.setter
    def RDIV_AFE(self, value):
        """
        Set the value of RDIV_AFE<7:0>
        """
        if self.allowLDO:
            if not(0<= value <=255):
                raise ValueError("Value must be [0..255]")
            self._writeReg('CFG19', 'RDIV_AFE<7:0>', value)
        else:
            self.chip.log("Changing LDO voltage is not permitted. To change the LDO voltage, set BIAS.allowLDO=True")

    #
    # BIAS_CFG20 (0x00A6)
    #

    # ISINK_SPIBUFF<2:0>
    @property 
    def ISINK_SPIBUFF(self):
        """
        Get the value of ISINK_SPIBUFF<2:0>
        """
        if self.chip.chipID == self.chip.chipIDMR3:        
            return self._readReg('CFG20', 'ISINK_SPIBUFF<2:0>')
        else:
            raise ValueError("Bitfield ISINK_SPIBUFF<2:0> is not supported on chip version "+str(self.chip.chipID))
            

    @ISINK_SPIBUFF.setter
    def ISINK_SPIBUFF(self, value):
        """
        Set the value of ISINK_SPIBUFF<2:0>
        """
        if self.chip.chipID == self.chip.chipIDMR3:                
            if value not in range(0,8):
                raise ValueError("Value must be [0,1]")
            self._writeReg('CFG20', 'ISINK_SPIBUFF<2:0>', value)
        else:
            raise ValueError("Bitfield ISINK_SPIBUFF<2:0> is not supported on chip version "+str(self.chip.chipID))
    
    # SPDUP_LDO_SPIBUF
    @property 
    def SPDUP_LDO_SPIBUF(self):
        """
        Get the value of SPDUP_LDO_SPIBUF
        """
        return self._readReg('CFG20', 'SPDUP_LDO_SPIBUF')

    @SPDUP_LDO_SPIBUF.setter
    def SPDUP_LDO_SPIBUF(self, value):
        """
        Set the value of SPDUP_LDO_SPIBUF
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG20', 'SPDUP_LDO_SPIBUF', value)

    # SPDUP_LDO_DIGIp2
    @property 
    def SPDUP_LDO_DIGIp2(self):
        """
        Get the value of SPDUP_LDO_DIGIp2
        """
        return self._readReg('CFG20', 'SPDUP_LDO_DIGIp2')

    @SPDUP_LDO_DIGIp2.setter
    def SPDUP_LDO_DIGIp2(self, value):
        """
        Set the value of SPDUP_LDO_DIGIp2
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG20', 'SPDUP_LDO_DIGIp2', value)

    # SPDUP_LDO_DIGIp1
    @property 
    def SPDUP_LDO_DIGIp1(self):
        """
        Get the value of SPDUP_LDO_DIGIp1
        """
        return self._readReg('CFG20', 'SPDUP_LDO_DIGIp1')

    @SPDUP_LDO_DIGIp1.setter
    def SPDUP_LDO_DIGIp1(self, value):
        """
        Set the value of SPDUP_LDO_DIGIp1
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG20', 'SPDUP_LDO_DIGIp1', value)

    # BYP_LDO_SPIBUF
    @property 
    def BYP_LDO_SPIBUF(self):
        """
        Get the value of BYP_LDO_SPIBUF
        """
        return self._readReg('CFG20', 'BYP_LDO_SPIBUF')

    @BYP_LDO_SPIBUF.setter
    def BYP_LDO_SPIBUF(self, value):
        """
        Set the value of BYP_LDO_SPIBUF
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG20', 'BYP_LDO_SPIBUF', value)

    # BYP_LDO_DIGIp2
    @property 
    def BYP_LDO_DIGIp2(self):
        """
        Get the value of BYP_LDO_DIGIp2
        """
        return self._readReg('CFG20', 'BYP_LDO_DIGIp2')

    @BYP_LDO_DIGIp2.setter
    def BYP_LDO_DIGIp2(self, value):
        """
        Set the value of BYP_LDO_DIGIp2
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG20', 'BYP_LDO_DIGIp2', value)

    # BYP_LDO_DIGIp1
    @property 
    def BYP_LDO_DIGIp1(self):
        """
        Get the value of BYP_LDO_DIGIp1
        """
        return self._readReg('CFG20', 'BYP_LDO_DIGIp1')

    @BYP_LDO_DIGIp1.setter
    def BYP_LDO_DIGIp1(self, value):
        """
        Set the value of BYP_LDO_DIGIp1
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG20', 'BYP_LDO_DIGIp1', value)

    # EN_LOADIMP_LDO_SPIBUF
    @property 
    def EN_LOADIMP_LDO_SPIBUF(self):
        """
        Get the value of EN_LOADIMP_LDO_SPIBUF
        """
        return self._readReg('CFG20', 'EN_LOADIMP_LDO_SPIBUF')

    @EN_LOADIMP_LDO_SPIBUF.setter
    def EN_LOADIMP_LDO_SPIBUF(self, value):
        """
        Set the value of EN_LOADIMP_LDO_SPIBUF
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG20', 'EN_LOADIMP_LDO_SPIBUF', value)

    # EN_LOADIMP_LDO_DIGIp2
    @property 
    def EN_LOADIMP_LDO_DIGIp2(self):
        """
        Get the value of EN_LOADIMP_LDO_DIGIp2
        """
        return self._readReg('CFG20', 'EN_LOADIMP_LDO_DIGIp2')

    @EN_LOADIMP_LDO_DIGIp2.setter
    def EN_LOADIMP_LDO_DIGIp2(self, value):
        """
        Set the value of EN_LOADIMP_LDO_DIGIp2
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG20', 'EN_LOADIMP_LDO_DIGIp2', value)

    # EN_LOADIMP_LDO_DIGIp1
    @property 
    def EN_LOADIMP_LDO_DIGIp1(self):
        """
        Get the value of EN_LOADIMP_LDO_DIGIp1
        """
        return self._readReg('CFG20', 'EN_LOADIMP_LDO_DIGIp1')

    @EN_LOADIMP_LDO_DIGIp1.setter
    def EN_LOADIMP_LDO_DIGIp1(self, value):
        """
        Set the value of EN_LOADIMP_LDO_DIGIp1
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG20', 'EN_LOADIMP_LDO_DIGIp1', value)

    # PD_LDO_SPIBUF
    @property 
    def PD_LDO_SPIBUF(self):
        """
        Get the value of PD_LDO_SPIBUF
        """
        return self._readReg('CFG20', 'PD_LDO_SPIBUF')

    @PD_LDO_SPIBUF.setter
    def PD_LDO_SPIBUF(self, value):
        """
        Set the value of PD_LDO_SPIBUF
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG20', 'PD_LDO_SPIBUF', value)

    # PD_LDO_DIGIp2
    @property 
    def PD_LDO_DIGIp2(self):
        """
        Get the value of PD_LDO_DIGIp2
        """
        return self._readReg('CFG20', 'PD_LDO_DIGIp2')

    @PD_LDO_DIGIp2.setter
    def PD_LDO_DIGIp2(self, value):
        """
        Set the value of PD_LDO_DIGIp2
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG20', 'PD_LDO_DIGIp2', value)

    # PD_LDO_DIGIp1
    @property 
    def PD_LDO_DIGIp1(self):
        """
        Get the value of PD_LDO_DIGIp1
        """
        return self._readReg('CFG20', 'PD_LDO_DIGIp1')

    @PD_LDO_DIGIp1.setter
    def PD_LDO_DIGIp1(self, value):
        """
        Set the value of PD_LDO_DIGIp1
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG20', 'PD_LDO_DIGIp1', value)

    # EN_G_LDOP
    @property 
    def EN_G_LDOP(self):
        """
        Get the value of EN_G_LDOP
        """
        return self._readReg('CFG20', 'EN_G_LDOP')

    @EN_G_LDOP.setter
    def EN_G_LDOP(self, value):
        """
        Set the value of EN_G_LDOP
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG20', 'EN_G_LDOP', value)

    #
    # BIAS_CFG21 (0x00A7)
    #
    
    # RDIV_DIGIp2<7:0>
    @property 
    def RDIV_DIGIp2(self):
        """
        Get the value of RDIV_DIGIp2<7:0>
        """
        return self._readReg('CFG21', 'RDIV_DIGIp2<7:0>')

    @RDIV_DIGIp2.setter
    def RDIV_DIGIp2(self, value):
        """
        Set the value of RDIV_DIGIp2<7:0>
        """
        if self.allowLDO:
            if not(0<= value <=255):
                raise ValueError("Value must be [0..255]")
            self._writeReg('CFG21', 'RDIV_DIGIp2<7:0>', value)
        else:
            self.chip.log("Changing LDO voltage is not permitted. To change the LDO voltage, set BIAS.allowLDO=True")
            
    # RDIV_DIGIp1<7:0>
    @property 
    def RDIV_DIGIp1(self):
        """
        Get the value of RDIV_DIGIp1<7:0>
        """
        return self._readReg('CFG21', 'RDIV_DIGIp1<7:0>')

    @RDIV_DIGIp1.setter
    def RDIV_DIGIp1(self, value):
        """
        Set the value of RDIV_DIGIp1<7:0>
        """
        if self.allowLDO:
            if not(0<= value <=255):
                raise ValueError("Value must be [0..255]")
            self._writeReg('CFG21', 'RDIV_DIGIp1<7:0>', value)
        else:
            self.chip.log("Changing LDO voltage is not permitted. To change the LDO voltage, set BIAS.allowLDO=True")
                                                                
    
            
        
