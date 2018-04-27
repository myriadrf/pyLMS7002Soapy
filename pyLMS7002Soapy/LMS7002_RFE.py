#***************************************************************
#* Name:      LMS7002_RFE.py
#* Purpose:   Class implementing LMS7002 RFE functions
#* Author:    Lime Microsystems ()
#* Created:   2016-11-14
#* Copyright: Lime Microsystems (limemicro.com)
#* License:
#**************************************************************

from LMS7002_base import *

class LMS7002_RFE(LMS7002_base):
    __slots__=[]    # Used to generate error on typos
    def __init__(self, chip, Channel):
        if Channel not in ['A', 'B']:
            raise ValueError("Parameter Channel must be 'A' or 'B'")
        self.chip = chip
        self.channel = Channel
        self.prefix = "RFE_"

    # EN_DIR
    @property 
    def EN_DIR(self):
        """
        Get the value of EN_DIR
        """
        prefix = self.prefix
        self.prefix = ""
        en_dir = self._readReg('TRX_EN_DIR', 'EN_DIR_RFE')
        self.prefix = prefix
        return en_dir

    @EN_DIR.setter
    def EN_DIR(self, value):
        """
        Set the value of EN_DIR
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        prefix = self.prefix
        self.prefix = ""
        self._writeReg('TRX_EN_DIR', 'EN_DIR_RFE', value)
        self.prefix = prefix

    #
    # RFE_CFG0 (0x010C)
    #

    # CDC_I_RFE<3:0>
    @property 
    def CDC_I_RFE(self):
        """
        Get the value of CDC_I_RFE<3:0>
        """
        return self._readReg('CFG0', 'CDC_I_RFE<3:0>')

    @CDC_I_RFE.setter
    def CDC_I_RFE(self, value):
        """
        Set the value of CDC_I_RFE<3:0>
        """
        if not(0 <= value <= 15):
            raise ValueError("Value must be [0,16]")
        self._writeReg('CFG0', 'CDC_I_RFE<3:0>', value)
        
    # CDC_Q_RFE<3:0>
    @property 
    def CDC_Q_RFE(self):
        """
        Get the value of CDC_Q_RFE<3:0>
        """
        return self._readReg('CFG0', 'CDC_Q_RFE<3:0>')

    @CDC_Q_RFE.setter
    def CDC_Q_RFE(self, value):
        """
        Set the value of CDC_Q_RFE<3:0>
        """
        if not(0 <= value <= 15):
            raise ValueError("Value must be [0,16]")
        self._writeReg('CFG0', 'CDC_Q_RFE<3:0>', value)

    # PD_LNA_RFE
    @property 
    def PD_LNA_RFE(self):
        """
        Get the value of PD_LNA_RFE
        """
        return self._readReg('CFG0', 'PD_LNA_RFE')

    @PD_LNA_RFE.setter
    def PD_LNA_RFE(self, value):
        """
        Set the value of PD_LNA_RFE
        """
        if value not in [0, 1, 'ON', 'OFF']:
            raise ValueError("Value must be [0,1,'ON', 'OFF']")
        if value==0 or value=='ON':
            val = 0
        else:
            val = 1
        self._writeReg('CFG0', 'PD_LNA_RFE', val)


    # PD_RLOOPB_1_RFE
    @property 
    def PD_RLOOPB_1_RFE(self):
        """
        Get the value of PD_RLOOPB_1_RFE
        """
        return self._readReg('CFG0', 'PD_RLOOPB_1_RFE')

    @PD_RLOOPB_1_RFE.setter
    def PD_RLOOPB_1_RFE(self, value):
        """
        Set the value of PD_RLOOPB_1_RFE
        """
        if value not in [0, 1, 'ON', 'OFF']:
            raise ValueError("Value must be [0,1,'ON', 'OFF']")
        if value==0 or value=='ON':
            val = 0
        else:
            val = 1
        self._writeReg('CFG0', 'PD_RLOOPB_1_RFE', val)

    # PD_RLOOPB_2_RFE
    @property 
    def PD_RLOOPB_2_RFE(self):
        """
        Get the value of PD_RLOOPB_2_RFE
        """
        return self._readReg('CFG0', 'PD_RLOOPB_2_RFE')

    @PD_RLOOPB_2_RFE.setter
    def PD_RLOOPB_2_RFE(self, value):
        """
        Set the value of PD_RLOOPB_2_RFE
        """
        if value not in [0, 1, 'ON', 'OFF']:
            raise ValueError("Value must be [0,1,'ON', 'OFF']")
        if value==0 or value=='ON':
            val = 0
        else:
            val = 1
        self._writeReg('CFG0', 'PD_RLOOPB_2_RFE', val)
        
    # PD_MXLOBUF_RFE
    @property 
    def PD_MXLOBUF_RFE(self):
        """
        Get the value of PD_MXLOBUF_RFE
        """
        return self._readReg('CFG0', 'PD_MXLOBUF_RFE')

    @PD_MXLOBUF_RFE.setter
    def PD_MXLOBUF_RFE(self, value):
        """
        Set the value of PD_MXLOBUF_RFE
        """
        if value not in [0, 1, 'ON', 'OFF']:
            raise ValueError("Value must be [0,1,'ON', 'OFF']")
        if value==0 or value=='ON':
            val = 0
        else:
            val = 1
        self._writeReg('CFG0', 'PD_MXLOBUF_RFE', val)

    # PD_QGEN_RFE
    @property 
    def PD_QGEN_RFE(self):
        """
        Get the value of PD_QGEN_RFE
        """
        return self._readReg('CFG0', 'PD_QGEN_RFE')

    @PD_QGEN_RFE.setter
    def PD_QGEN_RFE(self, value):
        """
        Set the value of PD_QGEN_RFE
        """
        if value not in [0, 1, 'ON', 'OFF']:
            raise ValueError("Value must be [0,1,'ON', 'OFF']")
        if value==0 or value=='ON':
            val = 0
        else:
            val = 1
        self._writeReg('CFG0', 'PD_QGEN_RFE', val)

    # PD_RSSI_RFE
    @property 
    def PD_RSSI_RFE(self):
        """
        Get the value of PD_RSSI_RFE
        """
        return self._readReg('CFG0', 'PD_RSSI_RFE')

    @PD_RSSI_RFE.setter
    def PD_RSSI_RFE(self, value):
        """
        Set the value of PD_RSSI_RFE
        """
        if value not in [0, 1, 'ON', 'OFF']:
            raise ValueError("Value must be [0,1,'ON', 'OFF']")
        if value==0 or value=='ON':
            val = 0
        else:
            val = 1
        self._writeReg('CFG0', 'PD_RSSI_RFE', val)

    # PD_TIA_RFE
    @property 
    def PD_TIA_RFE(self):
        """
        Get the value of PD_TIA_RFE
        """
        return self._readReg('CFG0', 'PD_TIA_RFE')

    @PD_TIA_RFE.setter
    def PD_TIA_RFE(self, value):
        """
        Set the value of PD_TIA_RFE
        """
        if value not in [0, 1, 'ON', 'OFF']:
            raise ValueError("Value must be [0,1,'ON', 'OFF']")
        if value==0 or value=='ON':
            val = 0
        else:
            val = 1
        self._writeReg('CFG0', 'PD_TIA_RFE', val)

    # EN_G_RFE
    @property 
    def EN_G_RFE(self):
        """
        Get the value of EN_G_RFE
        """
        return self._readReg('CFG0', 'EN_G_RFE')

    @EN_G_RFE.setter
    def EN_G_RFE(self, value):
        """
        Set the value of EN_G_RFE
        """
        if value not in [0, 1, 'ON', 'OFF']:
            raise ValueError("Value must be [0,1,'ON', 'OFF']")
        if value==0 or value=='OFF':
            val = 0
        else:
            val = 1
        self._writeReg('CFG0', 'EN_G_RFE', val)

    #
    # RFE_CFG1 (0x010D)
    #

    # SEL_PATH_RFE<1:0>
    @property 
    def SEL_PATH_RFE(self):
        """
        Get the value of SEL_PATH_RFE<1:0>
        """
        return self._readReg('CFG1', 'SEL_PATH_RFE<1:0>')

    @SEL_PATH_RFE.setter
    def SEL_PATH_RFE(self, value):
        """
        Set the value of SEL_PATH_RFE<1:0>
        """
        if value not in [0, 1, 2, 3, 'NONE', 'LNAH', 'LNAL', 'LNAW']:
            raise ValueError("Value must be [0, 1, 2, 3, 'NONE', 'LNAH', 'LNAL', 'LNAW']")
        if value==0 or value=='NONE':
            val = 0
        elif value==1 or value=='LNAH':
            val = 1
        elif value==2 or value=='LNAL':
            val = 2
        else:
            val = 3
        self._writeReg('CFG1', 'SEL_PATH_RFE<1:0>', val)

    # EN_DCOFF_RXFE_RFE
    @property 
    def EN_DCOFF_RXFE_RFE(self):
        """
        Get the value of EN_DCOFF_RXFE_RFE
        """
        return self._readReg('CFG1', 'EN_DCOFF_RXFE_RFE')

    @EN_DCOFF_RXFE_RFE.setter
    def EN_DCOFF_RXFE_RFE(self, value):
        """
        Set the value of EN_DCOFF_RXFE_RFE
        """
        if value not in [0, 1, 'ON', 'OFF']:
            raise ValueError("Value must be [0,1,'ON', 'OFF']")
        if value==0 or value=='OFF':
            val = 0
        else:
            val = 1
        self._writeReg('CFG1', 'EN_DCOFF_RXFE_RFE', val)

    # EN_INSHSW_LB1_RFE
    @property 
    def EN_INSHSW_LB1_RFE(self):
        """
        Get the value of EN_INSHSW_LB1_RFE
        """
        return self._readReg('CFG1', 'EN_INSHSW_LB1_RFE')

    @EN_INSHSW_LB1_RFE.setter
    def EN_INSHSW_LB1_RFE(self, value):
        """
        Set the value of EN_INSHSW_LB1_RFE
        """
        if value not in [0, 1, 'ON', 'OFF']:
            raise ValueError("Value must be [0,1,'ON', 'OFF']")
        if value==0 or value=='OFF':
            val = 0
        else:
            val = 1
        self._writeReg('CFG1', 'EN_INSHSW_LB1_RFE', val)

    # EN_INSHSW_LB2_RFE
    @property 
    def EN_INSHSW_LB2_RFE(self):
        """
        Get the value of EN_INSHSW_LB2_RFE
        """
        return self._readReg('CFG1', 'EN_INSHSW_LB2_RFE')

    @EN_INSHSW_LB2_RFE.setter
    def EN_INSHSW_LB2_RFE(self, value):
        """
        Set the value of EN_INSHSW_LB2_RFE
        """
        if value not in [0, 1, 'ON', 'OFF']:
            raise ValueError("Value must be [0,1,'ON', 'OFF']")
        if value==0 or value=='OFF':
            val = 0
        else:
            val = 1
        self._writeReg('CFG1', 'EN_INSHSW_LB2_RFE', val)

    # EN_INSHSW_L_RFE
    @property 
    def EN_INSHSW_L_RFE(self):
        """
        Get the value of EN_INSHSW_L_RFE
        """
        return self._readReg('CFG1', 'EN_INSHSW_L_RFE')

    @EN_INSHSW_L_RFE.setter
    def EN_INSHSW_L_RFE(self, value):
        """
        Set the value of EN_INSHSW_L_RFE
        """
        if value not in [0, 1, 'ON', 'OFF']:
            raise ValueError("Value must be [0,1,'ON', 'OFF']")
        if value==0 or value=='OFF':
            val = 0
        else:
            val = 1
        self._writeReg('CFG1', 'EN_INSHSW_L_RFE', val)

    # EN_INSHSW_W_RFE
    @property 
    def EN_INSHSW_W_RFE(self):
        """
        Get the value of EN_INSHSW_W_RFE
        """
        return self._readReg('CFG1', 'EN_INSHSW_W_RFE')

    @EN_INSHSW_W_RFE.setter
    def EN_INSHSW_W_RFE(self, value):
        """
        Set the value of EN_INSHSW_W_RFE
        """
        if value not in [0, 1, 'ON', 'OFF']:
            raise ValueError("Value must be [0,1,'ON', 'OFF']")
        if value==0 or value=='OFF':
            val = 0
        else:
            val = 1
        self._writeReg('CFG1', 'EN_INSHSW_W_RFE', val)

    # EN_NEXTRX_RFE
    @property 
    def EN_NEXTRX_RFE(self):
        """
        Get the value of EN_NEXTRX_RFE
        """
        return self._readReg('CFG1', 'EN_NEXTRX_RFE')

    @EN_NEXTRX_RFE.setter
    def EN_NEXTRX_RFE(self, value):
        """
        Set the value of EN_NEXTRX_RFE
        """
        if value not in [0, 1, 'SISO', 'MIMO']:
            raise ValueError("Value must be [0,1,'SISO', 'MIMO']")
        if value==0 or value=='SISO':
            val = 0
        else:
            val = 1
        self._writeReg('CFG1', 'EN_NEXTRX_RFE', val)
        

    #
    # RFE_DCOFF (0x010E)
    #
    
    # DCOFFI_RFE<6:0>
    @property 
    def DCOFFI_RFE(self):
        """
        Get the value of DCOFFI_RFE<6:0>
        """
        return self.signMagnitudeToInt(self._readReg('DCOFF', 'DCOFFI_RFE<6:0>'),7)

    @DCOFFI_RFE.setter
    def DCOFFI_RFE(self, value):
        """
        Set the value of DCOFFI_RFE<6:0>
        """
        if not(-63 <= value <= 63):
            raise ValueError("Value must be [-63..63]")
        self._writeReg('DCOFF', 'DCOFFI_RFE<6:0>', self.intToSignMagnitude(value,7))

    # DCOFFQ_RFE<6:0>
    @property 
    def DCOFFQ_RFE(self):
        """
        Get the value of DCOFFQ_RFE<6:0>
        """
        return self.signMagnitudeToInt(self._readReg('DCOFF', 'DCOFFQ_RFE<6:0>'),7)

    @DCOFFQ_RFE.setter
    def DCOFFQ_RFE(self, value):
        """
        Set the value of DCOFFQ_RFE<6:0>
        """
        if not(-63 <= value <= 63):
            raise ValueError("Value must be [-63..63]")
        self._writeReg('DCOFF', 'DCOFFQ_RFE<6:0>', self.intToSignMagnitude(value,7))

    #
    # RFE_ICT0 (0x010F)
    #

    # ICT_LOOPB_RFE<4:0>
    @property 
    def ICT_LOOPB_RFE(self):
        """
        Get the value of ICT_LOOPB_RFE<4:0>
        """
        return self._readReg('ICT0', 'ICT_LOOPB_RFE<4:0>')

    @ICT_LOOPB_RFE.setter
    def ICT_LOOPB_RFE(self, value):
        """
        Set the value of ICT_LOOPB_RFE<4:0>
        """
        if not(0 <= value <= 31):
            raise ValueError("Value must be [0..31]")
        self._writeReg('ICT0', 'ICT_LOOPB_RFE<4:0>', value)

    # ICT_TIAMAIN_RFE<4:0>
    @property 
    def ICT_TIAMAIN_RFE(self):
        """
        Get the value of ICT_TIAMAIN_RFE<4:0>
        """
        return self._readReg('ICT0', 'ICT_TIAMAIN_RFE<4:0>')

    @ICT_TIAMAIN_RFE.setter
    def ICT_TIAMAIN_RFE(self, value):
        """
        Set the value of ICT_TIAMAIN_RFE<4:0>
        """
        if not(0 <= value <= 31):
            raise ValueError("Value must be [0..31]")
        self._writeReg('ICT0', 'ICT_TIAMAIN_RFE<4:0>', value)

    # ICT_TIAOUT_RFE<4:0>
    @property 
    def ICT_TIAOUT_RFE(self):
        """
        Get the value of ICT_TIAOUT_RFE<4:0>
        """
        return self._readReg('ICT0', 'ICT_TIAOUT_RFE<4:0>')

    @ICT_TIAOUT_RFE.setter
    def ICT_TIAOUT_RFE(self, value):
        """
        Set the value of ICT_TIAOUT_RFE<4:0>
        """
        if not(0 <= value <= 31):
            raise ValueError("Value must be [0..31]")
        self._writeReg('ICT0', 'ICT_TIAOUT_RFE<4:0>', value)

    #
    # RFE_ICT1 (0x0110)
    #

    # ICT_LNACMO_RFE<4:0>
    @property 
    def ICT_LNACMO_RFE(self):
        """
        Get the value of ICT_LNACMO_RFE<4:0>
        """
        return self._readReg('ICT1', 'ICT_LNACMO_RFE<4:0>')

    @ICT_LNACMO_RFE.setter
    def ICT_LNACMO_RFE(self, value):
        """
        Set the value of ICT_LNACMO_RFE<4:0>
        """
        if not(0 <= value <= 31):
            raise ValueError("Value must be [0..31]")
        self._writeReg('ICT1', 'ICT_LNACMO_RFE<4:0>', value)

    # ICT_LNA_RFE<4:0>
    @property 
    def ICT_LNA_RFE(self):
        """
        Get the value of ICT_LNA_RFE<4:0>
        """
        return self._readReg('ICT1', 'ICT_LNA_RFE<4:0>')

    @ICT_LNA_RFE.setter
    def ICT_LNA_RFE(self, value):
        """
        Set the value of ICT_LNA_RFE<4:0>
        """
        if not(0 <= value <= 31):
            raise ValueError("Value must be [0..31]")
        self._writeReg('ICT1', 'ICT_LNA_RFE<4:0>', value)

    # ICT_LODC_RFE<4:0>
    @property 
    def ICT_LODC_RFE(self):
        """
        Get the value of ICT_LODC_RFE<4:0>
        """
        return self._readReg('ICT1', 'ICT_LODC_RFE<4:0>')

    @ICT_LODC_RFE.setter
    def ICT_LODC_RFE(self, value):
        """
        Set the value of ICT_LODC_RFE<4:0>
        """
        if not(0 <= value <= 31):
            raise ValueError("Value must be [0..31]")
        self._writeReg('ICT1', 'ICT_LODC_RFE<4:0>', value)

    #
    # RFE_CAP0 (0x0111)
    #

    # CAP_RXMXO_RFE<4:0>
    @property 
    def CAP_RXMXO_RFE(self):
        """
        Get the value of CAP_RXMXO_RFE<4:0>
        """
        return self._readReg('CAP0', 'CAP_RXMXO_RFE<4:0>')

    @CAP_RXMXO_RFE.setter
    def CAP_RXMXO_RFE(self, value):
        """
        Set the value of CAP_RXMXO_RFE<4:0>
        """
        if not(0 <= value <= 31):
            raise ValueError("Value must be [0..31]")
        self._writeReg('CAP0', 'CAP_RXMXO_RFE<4:0>', value)

    # CGSIN_LNA_RFE<4:0>
    @property 
    def CGSIN_LNA_RFE(self):
        """
        Get the value of CGSIN_LNA_RFE<4:0>
        """
        return self._readReg('CAP0', 'CGSIN_LNA_RFE<4:0>')

    @CGSIN_LNA_RFE.setter
    def CGSIN_LNA_RFE(self, value):
        """
        Set the value of CGSIN_LNA_RFE<4:0>
        """
        if not(0 <= value <= 31):
            raise ValueError("Value must be [0..31]")
        self._writeReg('CAP0', 'CGSIN_LNA_RFE<4:0>', value)

    #
    # RFE_CAP1 (0x0112)
    #

    # CCOMP_TIA_RFE<3:0>
    @property 
    def CCOMP_TIA_RFE(self):
        """
        Get the value of CCOMP_TIA_RFE<3:0>
        """
        return self._readReg('CAP1', 'CCOMP_TIA_RFE<3:0>')

    @CCOMP_TIA_RFE.setter
    def CCOMP_TIA_RFE(self, value):
        """
        Set the value of CCOMP_TIA_RFE<3:0>
        """
        if not(0 <= value <= 15):
            raise ValueError("Value must be [0..15]")
        self._writeReg('CAP1', 'CCOMP_TIA_RFE<3:0>', value)

    # CFB_TIA_RFE<11:0>
    @property 
    def CFB_TIA_RFE(self):
        """
        Get the value of CFB_TIA_RFE<11:0>
        """
        return self._readReg('CAP1', 'CFB_TIA_RFE<11:0>')

    @CFB_TIA_RFE.setter
    def CFB_TIA_RFE(self, value):
        """
        Set the value of CFB_TIA_RFE<11:0>
        """
        if not(0 <= value <= 4095):
            raise ValueError("Value must be [0..4095]")
        self._writeReg('CAP1', 'CFB_TIA_RFE<11:0>', value)

    #
    # RFE_GAIN (0x0113)
    #

    # G_LNA_RFE<3:0>
    @property 
    def G_LNA_RFE(self):
        """
        Get the value of G_LNA_RFE<3:0>
        """
        return self._readReg('GAIN', 'G_LNA_RFE<3:0>')

    @G_LNA_RFE.setter
    def G_LNA_RFE(self, value):
        """
        Set the value of G_LNA_RFE<3:0>
        """
        if not(1 <= value <= 15):
            raise ValueError("Value must be [1..15]")
        self._writeReg('GAIN', 'G_LNA_RFE<3:0>', value)

    # G_RXLOOPB_RFE<3:0>
    @property 
    def G_RXLOOPB_RFE(self):
        """
        Get the value of G_RXLOOPB_RFE<3:0>
        """
        return self._readReg('GAIN', 'G_RXLOOPB_RFE<3:0>')

    @G_RXLOOPB_RFE.setter
    def G_RXLOOPB_RFE(self, value):
        """
        Set the value of G_RXLOOPB_RFE<3:0>
        """
        if not(0 <= value <= 15):
            raise ValueError("Value must be [0..15]")
        self._writeReg('GAIN', 'G_RXLOOPB_RFE<3:0>', value)

    # G_TIA_RFE<1:0>
    @property 
    def G_TIA_RFE(self):
        """
        Get the value of G_TIA_RFE<1:0>
        """
        return self._readReg('GAIN', 'G_TIA_RFE<1:0>')

    @G_TIA_RFE.setter
    def G_TIA_RFE(self, value):
        """
        Set the value of G_TIA_RFE<1:0>
        """
        if not(1 <= value <= 3):
            raise ValueError("Value must be [1..3]")
        self._writeReg('GAIN', 'G_TIA_RFE<1:0>', value)

    #
    # RFE_TIA (0x0114)
    #

    # RCOMP_TIA_RFE<3:0>
    @property 
    def RCOMP_TIA_RFE(self):
        """
        Get the value of RCOMP_TIA_RFE<3:0>
        """
        return self._readReg('TIA', 'RCOMP_TIA_RFE<3:0>')

    @RCOMP_TIA_RFE.setter
    def RCOMP_TIA_RFE(self, value):
        """
        Set the value of RCOMP_TIA_RFE<3:0>
        """
        if not(0 <= value <= 15):
            raise ValueError("Value must be [0..15]")
        self._writeReg('TIA', 'RCOMP_TIA_RFE<3:0>', value)

    # RFB_TIA_RFE<4:0>
    @property 
    def RFB_TIA_RFE(self):
        """
        Get the value of RFB_TIA_RFE<4:0>
        """
        return self._readReg('TIA', 'RFB_TIA_RFE<4:0>')

    @RFB_TIA_RFE.setter
    def RFB_TIA_RFE(self, value):
        """
        Set the value of RFB_TIA_RFE<4:0>
        """
        if not(0 <= value <= 31):
            raise ValueError("Value must be [0..31]")
        self._writeReg('TIA', 'RFB_TIA_RFE<4:0>', value)

