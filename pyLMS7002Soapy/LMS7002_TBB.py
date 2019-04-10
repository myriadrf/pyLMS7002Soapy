# ***************************************************************
# * Name:      LMS7002_TBB.py
# * Purpose:   Class implementing LMS7002 TBB functions
# * Author:    Lime Microsystems ()
# * Created:   2016-11-14
# * Copyright: Lime Microsystems (limemicro.com)
# * License:
# **************************************************************

from pyLMS7002Soapy.LMS7002_base import LMS7002_base


class LMS7002_TBB(LMS7002_base):
    __slots__ = []  # Used to generate error on typos

    def __init__(self, chip, Channel):
        if Channel not in ['A', 'B']:
            raise ValueError("Parameter Channel must be 'A' or 'B'")
        self.chip = chip
        self.channel = Channel
        self.prefix = "TBB_"

    # EN_DIR
    @property
    def EN_DIR(self):
        """
        Get the value of EN_DIR
        """
        prefix = self.prefix
        self.prefix = ""
        en_dir = self._readReg('TRX_EN_DIR', 'EN_DIR_TBB')
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
        self._writeReg('TRX_EN_DIR', 'EN_DIR_TBB', value)
        self.prefix = prefix

    #
    # TBB_CFG (0x0105)
    #

    # STATPULSE_TBB
    @property
    def STATPULSE_TBB(self):
        """
        Get the value of STATPULSE_TBB
        """
        return self._readReg('CFG', 'STATPULSE_TBB')

    @STATPULSE_TBB.setter
    def STATPULSE_TBB(self, value):
        """
        Set the value of STATPULSE_TBB
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG', 'STATPULSE_TBB', value)

    # LOOPB_TBB<2:0>
    @property
    def LOOPB_TBB(self):
        """
        Get the value of LOOPB_TBB<2:0>
        """
        return self._readReg('CFG', 'LOOPB_TBB<2:0>')

    @LOOPB_TBB.setter
    def LOOPB_TBB(self, value):
        """
        Set the value of LOOPB_TBB<2:0>
        """
        if not (0 <= value <= 7):
            raise ValueError("Value must be [0..7]")
        self._writeReg('CFG', 'LOOPB_TBB<2:0>', value)

    # PD_LPFH_TBB
    @property
    def PD_LPFH_TBB(self):
        """
        Get the value of PD_LPFH_TBB
        """
        return self._readReg('CFG', 'PD_LPFH_TBB')

    @PD_LPFH_TBB.setter
    def PD_LPFH_TBB(self, value):
        """
        Set the value of PD_LPFH_TBB
        """
        if value not in [0, 1, 'ON', 'OFF']:
            raise ValueError("Value must be [0,1,'ON', 'OFF']")
        if value == 0 or value == 'ON':
            val = 0
        else:
            val = 1
        self._writeReg('CFG', 'PD_LPFH_TBB', val)

    # PD_LPFIAMP_TBB
    @property
    def PD_LPFIAMP_TBB(self):
        """
        Get the value of PD_LPFIAMP_TBB
        """
        return self._readReg('CFG', 'PD_LPFIAMP_TBB')

    @PD_LPFIAMP_TBB.setter
    def PD_LPFIAMP_TBB(self, value):
        """
        Set the value of PD_LPFIAMP_TBB
        """
        if value not in [0, 1, 'ON', 'OFF']:
            raise ValueError("Value must be [0,1,'ON', 'OFF']")
        if value == 0 or value == 'ON':
            val = 0
        else:
            val = 1
        self._writeReg('CFG', 'PD_LPFIAMP_TBB', val)

    # PD_LPFLAD_TBB
    @property
    def PD_LPFLAD_TBB(self):
        """
        Get the value of PD_LPFLAD_TBB
        """
        return self._readReg('CFG', 'PD_LPFLAD_TBB')

    @PD_LPFLAD_TBB.setter
    def PD_LPFLAD_TBB(self, value):
        """
        Set the value of PD_LPFLAD_TBB
        """
        if value not in [0, 1, 'ON', 'OFF']:
            raise ValueError("Value must be [0,1,'ON', 'OFF']")
        if value == 0 or value == 'ON':
            val = 0
        else:
            val = 1
        self._writeReg('CFG', 'PD_LPFLAD_TBB', val)

    # PD_LPFS5_TBB
    @property
    def PD_LPFS5_TBB(self):
        """
        Get the value of PD_LPFS5_TBB
        """
        return self._readReg('CFG', 'PD_LPFS5_TBB')

    @PD_LPFS5_TBB.setter
    def PD_LPFS5_TBB(self, value):
        """
        Set the value of PD_LPFS5_TBB
        """
        if value not in [0, 1, 'ON', 'OFF']:
            raise ValueError("Value must be [0,1,'ON', 'OFF']")
        if value == 0 or value == 'ON':
            val = 0
        else:
            val = 1
        self._writeReg('CFG', 'PD_LPFS5_TBB', val)

    # EN_G_TBB
    @property
    def EN_G_TBB(self):
        """
        Get the value of EN_G_TBB
        """
        return self._readReg('CFG', 'EN_G_TBB')

    @EN_G_TBB.setter
    def EN_G_TBB(self, value):
        """
        Set the value of EN_G_TBB
        """
        if value not in [0, 1, 'ON', 'OFF']:
            raise ValueError("Value must be [0,1,'ON', 'OFF']")
        if value == 0 or value == 'OFF':
            val = 0
        else:
            val = 1
        self._writeReg('CFG', 'EN_G_TBB', val)

    #
    # TBB_ICT0 (0x0106)
    #

    # ICT_LPFS5_F_TBB<4:0>
    @property
    def ICT_LPFS5_F_TBB(self):
        """
        Get the value of ICT_LPFS5_F_TBB<4:0>
        """
        return self._readReg('ICT0', 'ICT_LPFS5_F_TBB<4:0>')

    @ICT_LPFS5_F_TBB.setter
    def ICT_LPFS5_F_TBB(self, value):
        """
        Set the value of ICT_LPFS5_F_TBB<4:0>
        """
        if not (0 <= value <= 31):
            raise ValueError("Value must be [0..31]")
        self._writeReg('ICT0', 'ICT_LPFS5_F_TBB<4:0>', value)

    # ICT_LPFS5_PT_TBB<4:0>
    @property
    def ICT_LPFS5_PT_TBB(self):
        """
        Get the value of ICT_LPFS5_PT_TBB<4:0>
        """
        return self._readReg('ICT0', 'ICT_LPFS5_PT_TBB<4:0>')

    @ICT_LPFS5_PT_TBB.setter
    def ICT_LPFS5_PT_TBB(self, value):
        """
        Set the value of ICT_LPFS5_PT_TBB<4:0>
        """
        if not (0 <= value <= 31):
            raise ValueError("Value must be [0..31]")
        self._writeReg('ICT0', 'ICT_LPFS5_PT_TBB<4:0>', value)

    # ICT_LPF_H_PT_TBB<4:0>
    @property
    def ICT_LPF_H_PT_TBB(self):
        """
        Get the value of ICT_LPF_H_PT_TBB<4:0>
        """
        return self._readReg('ICT0', 'ICT_LPF_H_PT_TBB<4:0>')

    @ICT_LPF_H_PT_TBB.setter
    def ICT_LPF_H_PT_TBB(self, value):
        """
        Set the value of ICT_LPF_H_PT_TBB<4:0>
        """
        if not (0 <= value <= 31):
            raise ValueError("Value must be [0..31]")
        self._writeReg('ICT0', 'ICT_LPF_H_PT_TBB<4:0>', value)

    #
    # TBB_ICT1 (0x0107)
    #

    # ICT_LPFH_F_TBB<4:0>
    @property
    def ICT_LPFH_F_TBB(self):
        """
        Get the value of ICT_LPFH_F_TBB<4:0>
        """
        return self._readReg('ICT1', 'ICT_LPFH_F_TBB<4:0>')

    @ICT_LPFH_F_TBB.setter
    def ICT_LPFH_F_TBB(self, value):
        """
        Set the value of ICT_LPFH_F_TBB<4:0>
        """
        if not (0 <= value <= 31):
            raise ValueError("Value must be [0..31]")
        self._writeReg('ICT1', 'ICT_LPFH_F_TBB<4:0>', value)

    # ICT_LPFLAD_F_TBB<4:0>
    @property
    def ICT_LPFLAD_F_TBB(self):
        """
        Get the value of ICT_LPFLAD_F_TBB<4:0>
        """
        return self._readReg('ICT1', 'ICT_LPFLAD_F_TBB<4:0>')

    @ICT_LPFLAD_F_TBB.setter
    def ICT_LPFLAD_F_TBB(self, value):
        """
        Set the value of ICT_LPFLAD_F_TBB<4:0>
        """
        if not (0 <= value <= 31):
            raise ValueError("Value must be [0..31]")
        self._writeReg('ICT1', 'ICT_LPFLAD_F_TBB<4:0>', value)

    # ICT_LPFLAD_PT_TBB<4:0>
    @property
    def ICT_LPFLAD_PT_TBB(self):
        """
        Get the value of ICT_LPFLAD_PT_TBB<4:0>
        """
        return self._readReg('ICT1', 'ICT_LPFLAD_PT_TBB<4:0>')

    @ICT_LPFLAD_PT_TBB.setter
    def ICT_LPFLAD_PT_TBB(self, value):
        """
        Set the value of ICT_LPFLAD_PT_TBB<4:0>
        """
        if not (0 <= value <= 31):
            raise ValueError("Value must be [0..31]")
        self._writeReg('ICT1', 'ICT_LPFLAD_PT_TBB<4:0>', value)

    #
    # TBB_IAMP (0x0108)
    #

    # CG_IAMP_TBB<5:0>
    @property
    def CG_IAMP_TBB(self):
        """
        Get the value of CG_IAMP_TBB<5:0>
        """
        return self._readReg('IAMP', 'CG_IAMP_TBB<5:0>')

    @CG_IAMP_TBB.setter
    def CG_IAMP_TBB(self, value):
        """
        Set the value of CG_IAMP_TBB<5:0>
        """
        if not (0 <= value <= 63):
            raise ValueError("Value must be [0..63]")
        self._writeReg('IAMP', 'CG_IAMP_TBB<5:0>', value)

    # ICT_IAMP_FRP_TBB<4:0>
    @property
    def ICT_IAMP_FRP_TBB(self):
        """
        Get the value of ICT_IAMP_FRP_TBB<4:0>
        """
        return self._readReg('IAMP', 'ICT_IAMP_FRP_TBB<4:0>')

    @ICT_IAMP_FRP_TBB.setter
    def ICT_IAMP_FRP_TBB(self, value):
        """
        Set the value of ICT_IAMP_FRP_TBB<4:0>
        """
        if not (0 <= value <= 31):
            raise ValueError("Value must be [0..31]")
        self._writeReg('IAMP', 'ICT_IAMP_FRP_TBB<4:0>', value)

    # ICT_IAMP_GG_FRP_TBB<4:0>
    @property
    def ICT_IAMP_GG_FRP_TBB(self):
        """
        Get the value of ICT_IAMP_GG_FRP_TBB<4:0>
        """
        return self._readReg('IAMP', 'ICT_IAMP_GG_FRP_TBB<4:0>')

    @ICT_IAMP_GG_FRP_TBB.setter
    def ICT_IAMP_GG_FRP_TBB(self, value):
        """
        Set the value of ICT_IAMP_GG_FRP_TBB<4:0>
        """
        if not (0 <= value <= 31):
            raise ValueError("Value must be [0..31]")
        self._writeReg('IAMP', 'ICT_IAMP_GG_FRP_TBB<4:0>', value)

    #
    # TBB_LPF0 (0x0109)
    #

    # RCAL_LPFH_TBB<7:0>
    @property
    def RCAL_LPFH_TBB(self):
        """
        Get the value of RCAL_LPFH_TBB<7:0>
        """
        return self._readReg('LPF0', 'RCAL_LPFH_TBB<7:0>')

    @RCAL_LPFH_TBB.setter
    def RCAL_LPFH_TBB(self, value):
        """
        Set the value of RCAL_LPFH_TBB<7:0>
        """
        if not (0 <= value <= 255):
            raise ValueError("Value must be [0..255]")
        self._writeReg('LPF0', 'RCAL_LPFH_TBB<7:0>', value)

    # RCAL_LPFLAD_TBB<7:0>
    @property
    def RCAL_LPFLAD_TBB(self):
        """
        Get the value of RCAL_LPFLAD_TBB<7:0>
        """
        return self._readReg('LPF0', 'RCAL_LPFLAD_TBB<7:0>')

    @RCAL_LPFLAD_TBB.setter
    def RCAL_LPFLAD_TBB(self, value):
        """
        Set the value of RCAL_LPFLAD_TBB<7:0>
        """
        if not (0 <= value <= 255):
            raise ValueError("Value must be [0..255]")
        self._writeReg('LPF0', 'RCAL_LPFLAD_TBB<7:0>', value)

    #
    # TBB_LPF1 (0x010A)
    #

    # TSTIN_TBB<1:0>
    @property
    def TSTIN_TBB(self):
        """
        Get the value of TSTIN_TBB<1:0>
        """
        return self._readReg('LPF1', 'TSTIN_TBB<1:0>')

    @TSTIN_TBB.setter
    def TSTIN_TBB(self, value):
        """
        Set the value of TSTIN_TBB<1:0>
        """
        if not (0 <= value <= 3):
            raise ValueError("Value must be [0..3]")
        self._writeReg('LPF1', 'TSTIN_TBB<1:0>', value)

    # BYPLADDER_TBB
    @property
    def BYPLADDER_TBB(self):
        """
        Get the value of BYPLADDER_TBB
        """
        return self._readReg('LPF1', 'BYPLADDER_TBB')

    @BYPLADDER_TBB.setter
    def BYPLADDER_TBB(self, value):
        """
        Set the value of BYPLADDER_TBB
        """
        if value not in [0, 1, 'OFF', 'BYP']:
            raise ValueError("Value must be [0,1,'BYP', 'OFF']")
        if value == 0 or value == 'OFF':
            val = 0
        else:
            val = 1
        self._writeReg('LPF1', 'BYPLADDER_TBB', val)

    # CCAL_LPFLAD_TBB<4:0>
    @property
    def CCAL_LPFLAD_TBB(self):
        """
        Get the value of CCAL_LPFLAD_TBB<4:0>
        """
        return self._readReg('LPF1', 'CCAL_LPFLAD_TBB<4:0>')

    @CCAL_LPFLAD_TBB.setter
    def CCAL_LPFLAD_TBB(self, value):
        """
        Set the value of CCAL_LPFLAD_TBB<4:0>
        """
        if not (0 <= value <= 31):
            raise ValueError("Value must be [0..31]")
        self._writeReg('LPF1', 'CCAL_LPFLAD_TBB<4:0>', value)

    # RCAL_LPFS5_TBB<7:0>
    @property
    def RCAL_LPFS5_TBB(self):
        """
        Get the value of RCAL_LPFS5_TBB<7:0>
        """
        return self._readReg('LPF0', 'RCAL_LPFS5_TBB<7:0>')

    @RCAL_LPFS5_TBB.setter
    def RCAL_LPFS5_TBB(self, value):
        """
        Set the value of RCAL_LPFS5_TBB<7:0>
        """
        if not (0 <= value <= 255):
            raise ValueError("Value must be [0..255]")
        self._writeReg('LPF0', 'RCAL_LPFS5_TBB<7:0>', value)

    #
    # TBB_LPF_BYP (0x010B)
    #

    # R5_LPF_BYP_TBB
    @property
    def R5_LPF_BYP_TBB(self):
        """
        Get the value of R5_LPF_BYP_TBB
        """
        if self.chip.chipID == self.chip.chipIDMR3:
            return self._readReg('LPF_BYP', 'R5_LPF_BYP_TBB')
        else:
            raise ValueError("Bitfield R5_LPF_BYP_TBB is not supported on chip version " + str(self.chip.chipID))

    @R5_LPF_BYP_TBB.setter
    def R5_LPF_BYP_TBB(self, value):
        """
        Set the value of R5_LPF_BYP_TBB
        """
        if self.chip.chipID == self.chip.chipIDMR3:
            if value not in [0, 1, 'USE', 'BYP']:
                raise ValueError("Value must be [0,1,'USE', 'OFF']")
            if value == 0 or value == 'OFF':
                val = 0
            else:
                val = 1
            self._writeReg('LPF_BYP', 'R5_LPF_BYP_TBB', val)
        else:
            raise ValueError("Bitfield R5_LPF_BYP_TBB is not supported on chip version " + str(self.chip.chipID))
