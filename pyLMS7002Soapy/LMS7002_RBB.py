# ***************************************************************
# * Name:      LMS7002_RBB.py
# * Purpose:   Class implementing LMS7002 RBB functions
# * Author:    Lime Microsystems ()
# * Created:   2016-11-14
# * Copyright: Lime Microsystems (limemicro.com)
# * License:
# **************************************************************

from pyLMS7002Soapy.LMS7002_base import LMS7002_base


class LMS7002_RBB(LMS7002_base):
    __slots__ = []  # Used to generate error on typos

    def __init__(self, chip, Channel):
        if Channel not in ['A', 'B']:
            raise ValueError("Parameter Channel must be 'A' or 'B'")
        self.chip = chip
        self.channel = Channel
        self.prefix = "RBB_"

    # EN_DIR
    @property
    def EN_DIR(self):
        """
        Get the value of EN_DIR
        """
        prefix = self.prefix
        self.prefix = ""
        en_dir = self._readReg('TRX_EN_DIR', 'EN_DIR_RBB')
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
        self._writeReg('TRX_EN_DIR', 'EN_DIR_RBB', value)
        self.prefix = prefix

    #
    # RBB_PD (0x0115)
    #

    # EN_LB_LPFH_RBB
    @property
    def EN_LB_LPFH_RBB(self):
        """
        Get the value of EN_LB_LPFH_RBB
        """
        return self._readReg('PD', 'EN_LB_LPFH_RBB')

    @EN_LB_LPFH_RBB.setter
    def EN_LB_LPFH_RBB(self, value):
        """
        Set the value of EN_LB_LPFH_RBB
        """
        if value not in [0, 1, 'ON', 'OFF']:
            raise ValueError("Value must be [0,1,'ON', 'OFF']")
        if value == 0 or value == 'OFF':
            val = 0
        else:
            val = 1
        self._writeReg('PD', 'EN_LB_LPFH_RBB', val)

    # EN_LB_LPFL_RBB
    @property
    def EN_LB_LPFL_RBB(self):
        """
        Get the value of EN_LB_LPFL_RBB
        """
        return self._readReg('PD', 'EN_LB_LPFL_RBB')

    @EN_LB_LPFL_RBB.setter
    def EN_LB_LPFL_RBB(self, value):
        """
        Set the value of EN_LB_LPFL_RBB
        """
        if value not in [0, 1, 'ON', 'OFF']:
            raise ValueError("Value must be [0,1,'ON', 'OFF']")
        if value == 0 or value == 'OFF':
            val = 0
        else:
            val = 1
        self._writeReg('PD', 'EN_LB_LPFL_RBB', val)

    # PD_LPFH_RBB
    @property
    def PD_LPFH_RBB(self):
        """
        Get the value of PD_LPFH_RBB
        """
        return self._readReg('PD', 'PD_LPFH_RBB')

    @PD_LPFH_RBB.setter
    def PD_LPFH_RBB(self, value):
        """
        Set the value of PD_LPFH_RBB
        """
        if value not in [0, 1, 'ON', 'OFF']:
            raise ValueError("Value must be [0,1,'ON', 'OFF']")
        if value == 0 or value == 'ON':
            val = 0
        else:
            val = 1
        self._writeReg('PD', 'PD_LPFH_RBB', val)

    # PD_LPFL_RBB
    @property
    def PD_LPFL_RBB(self):
        """
        Get the value of PD_LPFL_RBB
        """
        return self._readReg('PD', 'PD_LPFL_RBB')

    @PD_LPFL_RBB.setter
    def PD_LPFL_RBB(self, value):
        """
        Set the value of PD_LPFL_RBB
        """
        if value not in [0, 1, 'ON', 'OFF']:
            raise ValueError("Value must be [0,1,'ON', 'OFF']")
        if value == 0 or value == 'ON':
            val = 0
        else:
            val = 1
        self._writeReg('PD', 'PD_LPFL_RBB', val)

    # PD_PGA_RBB
    @property
    def PD_PGA_RBB(self):
        """
        Get the value of PD_PGA_RBB
        """
        return self._readReg('PD', 'PD_PGA_RBB')

    @PD_PGA_RBB.setter
    def PD_PGA_RBB(self, value):
        """
        Set the value of PD_PGA_RBB
        """
        if value not in [0, 1, 'ON', 'OFF']:
            raise ValueError("Value must be [0,1,'ON', 'OFF']")
        if value == 0 or value == 'ON':
            val = 0
        else:
            val = 1
        self._writeReg('PD', 'PD_PGA_RBB', val)

    # EN_G_RBB
    @property
    def EN_G_RBB(self):
        """
        Get the value of EN_G_RBB
        """
        return self._readReg('PD', 'EN_G_RBB')

    @EN_G_RBB.setter
    def EN_G_RBB(self, value):
        """
        Set the value of EN_G_RBB
        """
        if value not in [0, 1, 'ON', 'OFF']:
            raise ValueError("Value must be [0,1,'ON', 'OFF']")
        if value == 0 or value == 'OFF':
            val = 0
        else:
            val = 1
        self._writeReg('PD', 'EN_G_RBB', val)

    #
    # RBB_LFP0 (0x0116)
    #

    # R_CTL_LPF_RBB<4:0>
    @property
    def R_CTL_LPF_RBB(self):
        """
        Get the value of R_CTL_LPF_RBB<4:0>
        """
        return self._readReg('LPF0', 'R_CTL_LPF_RBB<4:0>')

    @R_CTL_LPF_RBB.setter
    def R_CTL_LPF_RBB(self, value):
        """
        Set the value of R_CTL_LPF_RBB<4:0>
        """
        if not (0 <= value <= 31):
            raise ValueError("Value must be [0..31]")
        self._writeReg('LPF0', 'R_CTL_LPF_RBB<4:0>', value)

    # RCC_CTL_LPFH_RBB<2:0>
    @property
    def RCC_CTL_LPFH_RBB(self):
        """
        Get the value of RCC_CTL_LPFH_RBB<2:0>
        """
        return self._readReg('LPF0', 'RCC_CTL_LPFH_RBB<2:0>')

    @RCC_CTL_LPFH_RBB.setter
    def RCC_CTL_LPFH_RBB(self, value):
        """
        Set the value of RCC_CTL_LPFH_RBB<2:0>
        """
        if not (0 <= value <= 7):
            raise ValueError("Value must be [0..7]")
        self._writeReg('LPF0', 'RCC_CTL_LPFH_RBB<2:0>', value)

    # C_CTL_LPFH_RBB<7:0>
    @property
    def C_CTL_LPFH_RBB(self):
        """
        Get the value of C_CTL_LPFH_RBB<7:0>
        """
        return self._readReg('LPF0', 'C_CTL_LPFH_RBB<7:0>')

    @C_CTL_LPFH_RBB.setter
    def C_CTL_LPFH_RBB(self, value):
        """
        Set the value of C_CTL_LPFH_RBB<7:0>
        """
        if not (0 <= value <= 255):
            raise ValueError("Value must be [0..255]")
        self._writeReg('LPF0', 'C_CTL_LPFH_RBB<7:0>', value)

    #
    # RBB_LPF1 (0x0117)
    #

    # RCC_CTL_LPFL_RBB<2:0>
    @property
    def RCC_CTL_LPFL_RBB(self):
        """
        Get the value of RCC_CTL_LPFL_RBB<2:0>
        """
        return self._readReg('LPF1', 'RCC_CTL_LPFL_RBB<2:0>')

    @RCC_CTL_LPFL_RBB.setter
    def RCC_CTL_LPFL_RBB(self, value):
        """
        Set the value of RCC_CTL_LPFL_RBB<2:0>
        """
        if not (0 <= value <= 7):
            raise ValueError("Value must be [0..7]")
        self._writeReg('LPF1', 'RCC_CTL_LPFL_RBB<2:0>', value)

    # C_CTL_LPFL_RBB<10:0>
    @property
    def C_CTL_LPFL_RBB(self):
        """
        Get the value of C_CTL_LPFL_RBB<10:0>
        """
        return self._readReg('LPF1', 'C_CTL_LPFL_RBB<10:0>')

    @C_CTL_LPFL_RBB.setter
    def C_CTL_LPFL_RBB(self, value):
        """
        Set the value of C_CTL_LPFL_RBB<10:0>
        """
        if not (0 <= value <= 2047):
            raise ValueError("Value must be [0..2047]")
        self._writeReg('LPF1', 'C_CTL_LPFL_RBB<10:0>', value)

    #
    # RBB_LPFICT (0x0118)
    #

    # INPUT_CTL_PGA_RBB<2:0>
    @property
    def INPUT_CTL_PGA_RBB(self):
        """
        Get the value of INPUT_CTL_PGA_RBB<2:0>
        """
        return self._readReg('LPFICT', 'INPUT_CTL_PGA_RBB<2:0>')

    @INPUT_CTL_PGA_RBB.setter
    def INPUT_CTL_PGA_RBB(self, value):
        """
        Set the value of INPUT_CTL_PGA_RBB<2:0>
        """
        if value not in [0, 1, 2, 3, 4, 'LPFL', 'LPHF', 'LPFBYP', 'LOOPBTX', 'LOOPBPK']:
            raise ValueError("Value must be [0,1,2,3,4, 'LPFL', 'LPHF', 'LPFBYP', 'LOOPBTX', 'LOOPBPK']")
        if value == 0 or value == 'LPFL':
            val = 0
        elif value == 1 or value == 'LPFH':
            val = 1
        elif value == 2 or value == 'LPFBYP':
            val = 2
        elif value == 3 or value == 'LOOPBTX':
            val = 3
        else:
            val = 4
        self._writeReg('LPFICT', 'INPUT_CTL_PGA_RBB<2:0>', val)

    # ICT_LPF_IN_RBB<4:0>
    @property
    def ICT_LPF_IN_RBB(self):
        """
        Get the value of ICT_LPF_IN_RBB<4:0>
        """
        return self._readReg('LPFICT', 'ICT_LPF_IN_RBB<4:0>')

    @ICT_LPF_IN_RBB.setter
    def ICT_LPF_IN_RBB(self, value):
        """
        Set the value of ICT_LPF_IN_RBB<4:0>
        """
        if not (0 <= value <= 31):
            raise ValueError("Value must be [0..31]")
        self._writeReg('LPFICT', 'ICT_LPF_IN_RBB<4:0>', value)

    # ICT_LPF_OUT_RBB<4:0>
    @property
    def ICT_LPF_OUT_RBB(self):
        """
        Get the value of ICT_LPF_OUT_RBB<4:0>
        """
        return self._readReg('LPFICT', 'ICT_LPF_OUT_RBB<4:0>')

    @ICT_LPF_OUT_RBB.setter
    def ICT_LPF_OUT_RBB(self, value):
        """
        Set the value of ICT_LPF_OUT_RBB<4:0>
        """
        if not (0 <= value <= 31):
            raise ValueError("Value must be [0..31]")
        self._writeReg('LPFICT', 'ICT_LPF_OUT_RBB<4:0>', value)

    #
    # RBB_PGA0 (0x0119)
    #

    # OSW_PGA_RBB
    @property
    def OSW_PGA_RBB(self):
        """
        Get the value of OSW_PGA_RBB
        """
        return self._readReg('PGA0', 'OSW_PGA_RBB')

    @OSW_PGA_RBB.setter
    def OSW_PGA_RBB(self, value):
        """
        Set the value of OSW_PGA_RBB
        """
        if value not in [0, 1, 'ADC', 'PADS']:
            raise ValueError("Value must be [0,1, 'ADC', 'PADS']")
        if value == 0 or value == 'ADC':
            val = 0
        else:
            val = 1
        self._writeReg('PGA0', 'OSW_PGA_RBB', val)

    # ICT_PGA_OUT_RBB<4:0>
    @property
    def ICT_PGA_OUT_RBB(self):
        """
        Get the value of ICT_PGA_OUT_RBB<4:0>
        """
        return self._readReg('PGA0', 'ICT_PGA_OUT_RBB<4:0>')

    @ICT_PGA_OUT_RBB.setter
    def ICT_PGA_OUT_RBB(self, value):
        """
        Set the value of ICT_PGA_OUT_RBB<4:0>
        """
        if not (0 <= value <= 31):
            raise ValueError("Value must be [0..31]")
        self._writeReg('PGA0', 'ICT_PGA_OUT_RBB<4:0>', value)

    # ICT_PGA_IN_RBB<4:0>
    @property
    def ICT_PGA_IN_RBB(self):
        """
        Get the value of ICT_PGA_IN_RBB<4:0>
        """
        return self._readReg('PGA0', 'ICT_PGA_IN_RBB<4:0>')

    @ICT_PGA_IN_RBB.setter
    def ICT_PGA_IN_RBB(self, value):
        """
        Set the value of ICT_PGA_IN_RBB<4:0>
        """
        if not (0 <= value <= 31):
            raise ValueError("Value must be [0..31]")
        self._writeReg('PGA0', 'ICT_PGA_IN_RBB<4:0>', value)

    # G_PGA_RBB<4:0>
    @property
    def G_PGA_RBB(self):
        """
        Get the value of G_PGA_RBB<4:0>
        """
        return self._readReg('PGA0', 'G_PGA_RBB<4:0>')

    @G_PGA_RBB.setter
    def G_PGA_RBB(self, value):
        """
        Set the value of G_PGA_RBB<4:0>
        """
        if not (0 <= value <= 31):
            raise ValueError("Value must be [0..31]")
        self._writeReg('PGA0', 'G_PGA_RBB<4:0>', value)

    #
    # RBB_PGA1 (0x011A)
    #

    # RCC_CTL_PGA_RBB<4:0>
    @property
    def RCC_CTL_PGA_RBB(self):
        """
        Get the value of RCC_CTL_PGA_RBB<4:0>
        """
        return self._readReg('PGA1', 'RCC_CTL_PGA_RBB<4:0>')

    @RCC_CTL_PGA_RBB.setter
    def RCC_CTL_PGA_RBB(self, value):
        """
        Set the value of RCC_CTL_PGA_RBB<4:0>
        """
        if not (0 <= value <= 31):
            raise ValueError("Value must be [0..31]")
        self._writeReg('PGA1', 'RCC_CTL_PGA_RBB<4:0>', value)

    # C_CTL_PGA_RBB<7:0>
    @property
    def C_CTL_PGA_RBB(self):
        """
        Get the value of C_CTL_PGA_RBB<7:0>
        """
        return self._readReg('PGA1', 'C_CTL_PGA_RBB<7:0>')

    @C_CTL_PGA_RBB.setter
    def C_CTL_PGA_RBB(self, value):
        """
        Set the value of C_CTL_PGA_RBB<7:0>
        """
        if not (0 <= value <= 255):
            raise ValueError("Value must be [0..255]")
        self._writeReg('PGA1', 'C_CTL_PGA_RBB<7:0>', value)
