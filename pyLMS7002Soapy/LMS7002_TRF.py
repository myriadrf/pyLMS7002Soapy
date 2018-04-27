#***************************************************************
#* Name:      LMS7002_TRF.py
#* Purpose:   Class implementing LMS7002 TRF functions
#* Author:    Lime Microsystems ()
#* Created:   2016-11-14
#* Copyright: Lime Microsystems (limemicro.com)
#* License:
#**************************************************************

from LMS7002_base import *

class LMS7002_TRF(LMS7002_base):
    __slots__ = []    # Used to generate error on typos
    def __init__(self, chip, Channel):
        if Channel not in ['A', 'B']:
            raise ValueError("Parameter Channel must be 'A' or 'B'")
        self.chip = chip
        self.channel = Channel
        self.prefix = "TRF_"

    # EN_DIR
    @property 
    def EN_DIR(self):
        """
        Get the value of EN_DIR
        """
        prefix = self.prefix
        self.prefix = ""
        en_dir = self._readReg('TRX_EN_DIR', 'EN_DIR_TRF')
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
        self._writeReg('TRX_EN_DIR', 'EN_DIR_TRF', value)
        self.prefix = prefix
        
    #
    # TRF_CFG (0x0100)
    #

    # EN_LOWBWLOMX_TMX_TRF
    @property 
    def EN_LOWBWLOMX_TMX_TRF(self):
        """
        Get the value of EN_LOWBWLOMX_TMX_TRF
        """
        return self._readReg('CFG', 'EN_LOWBWLOMX_TMX_TRF')

    @EN_LOWBWLOMX_TMX_TRF.setter
    def EN_LOWBWLOMX_TMX_TRF(self, value):
        """
        Set the value of EN_LOWBWLOMX_TMX_TRF
        """
        if value not in [0, 1, 'ON', 'OFF']:
            raise ValueError("Value must be [0,1,'ON', 'OFF']")
        if value==0 or value=='OFF':
            val = 0
        else:
            val = 1
        self._writeReg('CFG', 'EN_LOWBWLOMX_TMX_TRF', val)

    # EN_NEXTTX_TRF
    @property 
    def EN_NEXTTX_TRF(self):
        """
        Get the value of EN_NEXTTX_TRF
        """
        return self._readReg('CFG', 'EN_NEXTTX_TRF')

    @EN_NEXTTX_TRF.setter
    def EN_NEXTTX_TRF(self, value):
        """
        Set the value of EN_NEXTTX_TRF
        """
        if value not in [0, 1, 'ON', 'OFF']:
            raise ValueError("Value must be [0,1,'ON', 'OFF']")
        if value==0 or value=='OFF':
            val = 0
        else:
            val = 1
        self._writeReg('CFG', 'EN_NEXTTX_TRF', val)

    # EN_AMPHF_PDET_TRF<1:0>
    @property 
    def EN_AMPHF_PDET_TRF(self):
        """
        Get the value of EN_AMPHF_PDET_TRF<1:0>
        """
        return self._readReg('CFG', 'EN_AMPHF_PDET_TRF<1:0>')

    @EN_AMPHF_PDET_TRF.setter
    def EN_AMPHF_PDET_TRF(self, value):
        """
        Set the value of EN_AMPHF_PDET_TRF<1:0>
        """
        if not(0 <= value <= 3):
            raise ValueError("Value must be [0..3]")
        self._writeReg('CFG', 'EN_AMPHF_PDET_TRF<1:0>', value)

    # LOADR_PDET_TRF<1:0>
    @property 
    def LOADR_PDET_TRF(self):
        """
        Get the value of LOADR_PDET_TRF<1:0>
        """
        return self._readReg('CFG', 'LOADR_PDET_TRF<1:0>')

    @LOADR_PDET_TRF.setter
    def LOADR_PDET_TRF(self, value):
        """
        Set the value of LOADR_PDET_TRF<1:0>
        """
        if not(0 <= value <= 3):
            raise ValueError("Value must be [0..3]")
        self._writeReg('CFG', 'LOADR_PDET_TRF<1:0>', value)

    # PD_PDET_TRF
    @property 
    def PD_PDET_TRF(self):
        """
        Get the value of PD_PDET_TRF
        """
        return self._readReg('CFG', 'PD_PDET_TRF')

    @PD_PDET_TRF.setter
    def PD_PDET_TRF(self, value):
        """
        Set the value of PD_PDET_TRF
        """
        if value not in [0, 1, 'ON', 'OFF']:
            raise ValueError("Value must be [0,1,'ON', 'OFF']")
        if value==0 or value=='ON':
            val = 0
        else:
            val = 1
        self._writeReg('CFG', 'PD_PDET_TRF', val)

    # PD_TLOBUF_TRF
    @property 
    def PD_TLOBUF_TRF(self):
        """
        Get the value of PD_TLOBUF_TRF
        """
        return self._readReg('CFG', 'PD_TLOBUF_TRF')

    @PD_TLOBUF_TRF.setter
    def PD_TLOBUF_TRF(self, value):
        """
        Set the value of PD_TLOBUF_TRF
        """
        if value not in [0, 1, 'ON', 'OFF']:
            raise ValueError("Value must be [0,1,'ON', 'OFF']")
        if value==0 or value=='ON':
            val = 0
        else:
            val = 1
        self._writeReg('CFG', 'PD_TLOBUF_TRF', val)

    # PD_TXPAD_TRF
    @property 
    def PD_TXPAD_TRF(self):
        """
        Get the value of PD_TXPAD_TRF
        """
        return self._readReg('CFG', 'PD_TXPAD_TRF')

    @PD_TXPAD_TRF.setter
    def PD_TXPAD_TRF(self, value):
        """
        Set the value of PD_TXPAD_TRF
        """
        if value not in [0, 1, 'ON', 'OFF']:
            raise ValueError("Value must be [0,1,'ON', 'OFF']")
        if value==0 or value=='ON':
            val = 0
        else:
            val = 1
        self._writeReg('CFG', 'PD_TXPAD_TRF', val)

    # EN_G_TRF
    @property 
    def EN_G_TRF(self):
        """
        Get the value of EN_G_TRF
        """
        return self._readReg('CFG', 'EN_G_TRF')

    @EN_G_TRF.setter
    def EN_G_TRF(self, value):
        """
        Set the value of EN_G_TRF
        """
        if value not in [0, 1, 'ON', 'OFF']:
            raise ValueError("Value must be [0,1,'ON', 'OFF']")
        if value==0 or value=='OFF':
            val = 0
        else:
            val = 1
        self._writeReg('CFG', 'EN_G_TRF', val)

    #
    # TRF_TXPAD (0x0101)
    #

    # F_TXPAD_TRF<2:0>
    @property 
    def F_TXPAD_TRF(self):
        """
        Get the value of F_TXPAD_TRF<2:0>
        """
        return self._readReg('TXPAD', 'F_TXPAD_TRF<2:0>')

    @F_TXPAD_TRF.setter
    def F_TXPAD_TRF(self, value):
        """
        Set the value of F_TXPAD_TRF<2:0>
        """
        if not(0 <= value <= 7):
            raise ValueError("Value must be [0..7]")
        self._writeReg('TXPAD', 'F_TXPAD_TRF<2:0>', value)

    # L_LOOPB_TXPAD_TRF<1:0>
    @property 
    def L_LOOPB_TXPAD_TRF(self):
        """
        Get the value of L_LOOPB_TXPAD_TRF<1:0>
        """
        return self._readReg('TXPAD', 'L_LOOPB_TXPAD_TRF<1:0>')

    @L_LOOPB_TXPAD_TRF.setter
    def L_LOOPB_TXPAD_TRF(self, value):
        """
        Set the value of L_LOOPB_TXPAD_TRF<1:0>
        """
        if not(0 <= value <= 3):
            raise ValueError("Value must be [0..3]")
        self._writeReg('TXPAD', 'L_LOOPB_TXPAD_TRF<1:0>', value)

    # LOSS_LIN_TXPAD_TRF<4:0>
    @property 
    def LOSS_LIN_TXPAD_TRF(self):
        """
        Get the value of LOSS_LIN_TXPAD_TRF<4:0>
        """
        return self._readReg('TXPAD', 'LOSS_LIN_TXPAD_TRF<4:0>')

    @LOSS_LIN_TXPAD_TRF.setter
    def LOSS_LIN_TXPAD_TRF(self, value):
        """
        Set the value of LOSS_LIN_TXPAD_TRF<4:0>
        """
        if not(0 <= value <= 31):
            raise ValueError("Value must be [0..31]")
        self._writeReg('TXPAD', 'LOSS_LIN_TXPAD_TRF<4:0>', value)

    # LOSS_MAIN_TXPAD_TRF<4:0>
    @property 
    def LOSS_MAIN_TXPAD_TRF(self):
        """
        Get the value of LOSS_MAIN_TXPAD_TRF<4:0>
        """
        return self._readReg('TXPAD', 'LOSS_MAIN_TXPAD_TRF<4:0>')

    @LOSS_MAIN_TXPAD_TRF.setter
    def LOSS_MAIN_TXPAD_TRF(self, value):
        """
        Set the value of LOSS_MAIN_TXPAD_TRF<4:0>
        """
        if not(0 <= value <= 31):
            raise ValueError("Value must be [0..31]")
        self._writeReg('TXPAD', 'LOSS_MAIN_TXPAD_TRF<4:0>', value)

    # EN_LOOPB_TXPAD_TRF
    @property 
    def EN_LOOPB_TXPAD_TRF(self):
        """
        Get the value of EN_LOOPB_TXPAD_TRF
        """
        return self._readReg('TXPAD', 'EN_LOOPB_TXPAD_TRF')

    @EN_LOOPB_TXPAD_TRF.setter
    def EN_LOOPB_TXPAD_TRF(self, value):
        """
        Set the value of EN_LOOPB_TXPAD_TRF
        """
        if value not in [0, 1, 'ON', 'OFF']:
            raise ValueError("Value must be [0,1,'ON', 'OFF']")
        if value==0 or value=='OFF':
            val = 0
        else:
            val = 1
        self._writeReg('TXPAD', 'EN_LOOPB_TXPAD_TRF', val)

    #
    # TRF_TXPADBIAS (0x0102)
    #

    # GCAS_GNDREF_TXPAD_TRF
    @property 
    def GCAS_GNDREF_TXPAD_TRF(self):
        """
        Get the value of GCAS_GNDREF_TXPAD_TRF
        """
        return self._readReg('TXPADBIAS', 'GCAS_GNDREF_TXPAD_TRF')

    @GCAS_GNDREF_TXPAD_TRF.setter
    def GCAS_GNDREF_TXPAD_TRF(self, value):
        """
        Set the value of GCAS_GNDREF_TXPAD_TRF
        """
        if value not in [0, 1, 'VDD', 'GND']:
            raise ValueError("Value must be [0,1,'VDD', 'GND']")
        if value==0 or value=='VDD':
            val = 0
        else:
            val = 1
        self._writeReg('TXPADBIAS', 'GCAS_GNDREF_TXPAD_TRF', val)

    # ICT_LIN_TXPAD_TRF<4:0>
    @property 
    def ICT_LIN_TXPAD_TRF(self):
        """
        Get the value of ICT_LIN_TXPAD_TRF<4:0>
        """
        return self._readReg('TXPADBIAS', 'ICT_LIN_TXPAD_TRF<4:0>')

    @ICT_LIN_TXPAD_TRF.setter
    def ICT_LIN_TXPAD_TRF(self, value):
        """
        Set the value of ICT_LIN_TXPAD_TRF<4:0>
        """
        if not(0 <= value <= 31):
            raise ValueError("Value must be [0..31]")
        self._writeReg('TXPADBIAS', 'ICT_LIN_TXPAD_TRF<4:0>', value)

    # ICT_MAIN_TXPAD_TRF<4:0>
    @property 
    def ICT_MAIN_TXPAD_TRF(self):
        """
        Get the value of ICT_MAIN_TXPAD_TRF<4:0>
        """
        return self._readReg('TXPADBIAS', 'ICT_MAIN_TXPAD_TRF<4:0>')

    @ICT_MAIN_TXPAD_TRF.setter
    def ICT_MAIN_TXPAD_TRF(self, value):
        """
        Set the value of ICT_MAIN_TXPAD_TRF<4:0>
        """
        if not(0 <= value <= 31):
            raise ValueError("Value must be [0..31]")
        self._writeReg('TXPADBIAS', 'ICT_MAIN_TXPAD_TRF<4:0>', value)

    # VGCAS_TXPAD_TRF<4:0>
    @property 
    def VGCAS_TXPAD_TRF(self):
        """
        Get the value of VGCAS_TXPAD_TRF<4:0>
        """
        return self._readReg('TXPADBIAS', 'VGCAS_TXPAD_TRF<4:0>')

    @VGCAS_TXPAD_TRF.setter
    def VGCAS_TXPAD_TRF(self, value):
        """
        Set the value of VGCAS_TXPAD_TRF<4:0>
        """
        if not(0 <= value <= 31):
            raise ValueError("Value must be [0..31]")
        self._writeReg('TXPADBIAS', 'VGCAS_TXPAD_TRF<4:0>', value)

    #
    # TRF_LOBAND (0x0103)
    #    

    # SEL_BAND1_TRF
    @property 
    def SEL_BAND1_TRF(self):
        """
        Get the value of SEL_BAND1_TRF
        """
        return self._readReg('LOBAND', 'SEL_BAND1_TRF')

    @SEL_BAND1_TRF.setter
    def SEL_BAND1_TRF(self, value):
        """
        Set the value of SEL_BAND1_TRF
        """
        if value not in [0, 1, 'ON', 'OFF']:
            raise ValueError("Value must be [0,1,'ON', 'OFF']")
        if value==0 or value=='OFF':
            val = 0
        else:
            val = 1
        self._writeReg('LOBAND', 'SEL_BAND1_TRF', val)

    # SEL_BAND2_TRF
    @property 
    def SEL_BAND2_TRF(self):
        """
        Get the value of SEL_BAND2_TRF
        """
        return self._readReg('LOBAND', 'SEL_BAND2_TRF')

    @SEL_BAND2_TRF.setter
    def SEL_BAND2_TRF(self, value):
        """
        Set the value of SEL_BAND2_TRF
        """
        if value not in [0, 1, 'ON', 'OFF']:
            raise ValueError("Value must be [0,1,'ON', 'OFF']")
        if value==0 or value=='OFF':
            val = 0
        else:
            val = 1
        self._writeReg('LOBAND', 'SEL_BAND2_TRF', val)

    # LOBIASN_TXM_TRF<4:0>
    @property 
    def LOBIASN_TXM_TRF(self):
        """
        Get the value of LOBIASN_TXM_TRF<4:0>
        """
        return self._readReg('LOBAND', 'LOBIASN_TXM_TRF<4:0>')

    @LOBIASN_TXM_TRF.setter
    def LOBIASN_TXM_TRF(self, value):
        """
        Set the value of LOBIASN_TXM_TRF<4:0>
        """
        if not(0 <= value <= 31):
            raise ValueError("Value must be [0..31]")
        self._writeReg('LOBAND', 'LOBIASN_TXM_TRF<4:0>', value)

    # LOBIASP_TXX_TRF<4:0>
    @property 
    def LOBIASP_TXX_TRF(self):
        """
        Get the value of LOBIASP_TXX_TRF<4:0>
        """
        return self._readReg('LOBAND', 'LOBIASP_TXX_TRF<4:0>')

    @LOBIASP_TXX_TRF.setter
    def LOBIASP_TXX_TRF(self, value):
        """
        Set the value of LOBIASP_TXX_TRF<4:0>
        """
        if not(0 <= value <= 31):
            raise ValueError("Value must be [0..31]")
        self._writeReg('LOBAND', 'LOBIASP_TXX_TRF<4:0>', value)

    #
    # TRF_CDC (0x0104)
    #    

    # CDC_I_TRF<3:0>
    @property 
    def CDC_I_TRF(self):
        """
        Get the value of CDC_I_TRF<3:0>
        """
        return self._readReg('CDC', 'CDC_I_TRF<3:0>')

    @CDC_I_TRF.setter
    def CDC_I_TRF(self, value):
        """
        Set the value of CDC_I_TRF<3:0>
        """
        if not(0 <= value <= 15):
            raise ValueError("Value must be [0..15]")
        self._writeReg('CDC', 'CDC_I_TRF<3:0>', value)

    # CDC_Q_TRF<3:0>
    @property 
    def CDC_Q_TRF(self):
        """
        Get the value of CDC_Q_TRF<3:0>
        """
        return self._readReg('CDC', 'CDC_Q_TRF<3:0>')

    @CDC_Q_TRF.setter
    def CDC_Q_TRF(self, value):
        """
        Set the value of CDC_Q_TRF<3:0>
        """
        if not(0 <= value <= 15):
            raise ValueError("Value must be [0..15]")
        self._writeReg('CDC', 'CDC_Q_TRF<3:0>', value)
                

