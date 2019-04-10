# ***************************************************************
# * Name:      LMS7002_CGEN.py
# * Purpose:   Class implementing LMS7002 CGEN functions
# * Author:    Lime Microsystems ()
# * Created:   2016-11-14
# * Copyright: Lime Microsystems (limemicro.com)
# * License:
# **************************************************************

from pyLMS7002Soapy.LMS7002_base import LMS7002_base
from math import floor
from time import sleep


class LMS7002_CGEN(LMS7002_base):
    __slots__ = []  # Used to generate error on typos

    def __init__(self, chip):
        self.chip = chip
        self.channel = None
        self.prefix = "CGEN_"

    #
    # CGEN_CFG (0x0086)
    #

    # RESET_N_CGEN
    @property
    def RESET_N_CGEN(self):
        """
        Get the value of RESET_N_CGEN
        """
        return self._readReg('CFG', 'RESET_N_CGEN')

    @RESET_N_CGEN.setter
    def RESET_N_CGEN(self, value):
        """
        Set the value of RESET_N_CGEN
        """
        if value not in [0, 1, 'RESET', 'NORMAL']:
            raise ValueError("Value must be [0,1,'RESET', 'NORMAL']")
        if value == 0 or value == 'RESET':
            val = 0
        else:
            val = 1
        self._writeReg('CFG', 'RESET_N_CGEN', val)

    # SPDUP_VCO_CGEN
    @property
    def SPDUP_VCO_CGEN(self):
        """
        Get the value of SPDUP_VCO_CGEN
        """
        return self._readReg('CFG', 'SPDUP_VCO_CGEN')

    @SPDUP_VCO_CGEN.setter
    def SPDUP_VCO_CGEN(self, value):
        """
        Set the value of SPDUP_VCO_CGEN
        """
        if value not in [0, 1, 'ON', 'OFF']:
            raise ValueError("Value must be [0,1,'ON', 'OFF']")
        if value == 0 or value == 'OFF':
            val = 0
        else:
            val = 1
        self._writeReg('CFG', 'SPDUP_VCO_CGEN', val)

    # EN_ADCCLKH_CLKGN
    @property
    def EN_ADCCLKH_CLKGN(self):
        """
        Get the value of EN_ADCCLKH_CLKGN
        """
        return self._readReg('CFG', 'EN_ADCCLKH_CLKGN')

    @EN_ADCCLKH_CLKGN.setter
    def EN_ADCCLKH_CLKGN(self, value):
        """
        Set the value of EN_ADCCLKH_CLKGN
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG', 'EN_ADCCLKH_CLKGN', value)

    # EN_COARSE_CKLGEN
    @property
    def EN_COARSE_CKLGEN(self):
        """
        Get the value of EN_COARSE_CKLGEN
        """
        return self._readReg('CFG', 'EN_COARSE_CKLGEN')

    @EN_COARSE_CKLGEN.setter
    def EN_COARSE_CKLGEN(self, value):
        """
        Set the value of EN_COARSE_CKLGEN
        """
        if value not in [0, 1, 'ON', 'OFF']:
            raise ValueError("Value must be [0,1,'ON', 'OFF']")
        if value == 0 or value == 'OFF':
            val = 0
        else:
            val = 1
        self._writeReg('CFG', 'EN_COARSE_CKLGEN', val)

    # EN_INTONLY_SDM_CGEN
    @property
    def EN_INTONLY_SDM_CGEN(self):
        """
        Get the value of EN_INTONLY_SDM_CGEN
        """
        return self._readReg('CFG', 'EN_INTONLY_SDM_CGEN')

    @EN_INTONLY_SDM_CGEN.setter
    def EN_INTONLY_SDM_CGEN(self, value):
        """
        Set the value of EN_INTONLY_SDM_CGEN
        """
        if value not in [0, 1, 'FRACN', 'INTN']:
            raise ValueError("Value must be [0,1,'FRACN', 'INTN']")
        if value == 0 or value == 'FRACN':
            val = 0
        else:
            val = 1
        self._writeReg('CFG', 'EN_INTONLY_SDM_CGEN', val)

    # EN_SDM_CLK_CGEN
    @property
    def EN_SDM_CLK_CGEN(self):
        """
        Get the value of EN_SDM_CLK_CGEN
        """
        return self._readReg('CFG', 'EN_SDM_CLK_CGEN')

    @EN_SDM_CLK_CGEN.setter
    def EN_SDM_CLK_CGEN(self, value):
        """
        Set the value of EN_SDM_CLK_CGEN
        """
        if value not in [0, 1, 'ON', 'OFF']:
            raise ValueError("Value must be [0,1,'ON', 'OFF']")
        if value == 0 or value == 'OFF':
            val = 0
        else:
            val = 1
        self._writeReg('CFG', 'EN_SDM_CLK_CGEN', val)

    # PD_CP_CGEN
    @property
    def PD_CP_CGEN(self):
        """
        Get the value of PD_CP_CGEN
        """
        return self._readReg('CFG', 'PD_CP_CGEN')

    @PD_CP_CGEN.setter
    def PD_CP_CGEN(self, value):
        """
        Set the value of PD_CP_CGEN
        """
        if value not in [0, 1, 'ON', 'OFF']:
            raise ValueError("Value must be [0,1,'ON', 'OFF']")
        if value == 0 or value == 'ON':
            val = 0
        else:
            val = 1
        self._writeReg('CFG', 'PD_CP_CGEN', val)

    # PD_FDIV_FB_CGEN
    @property
    def PD_FDIV_FB_CGEN(self):
        """
        Get the value of PD_FDIV_FB_CGEN
        """
        return self._readReg('CFG', 'PD_FDIV_FB_CGEN')

    @PD_FDIV_FB_CGEN.setter
    def PD_FDIV_FB_CGEN(self, value):
        """
        Set the value of PD_FDIV_FB_CGEN
        """
        if value not in [0, 1, 'ON', 'OFF']:
            raise ValueError("Value must be [0,1,'ON', 'OFF']")
        if value == 0 or value == 'ON':
            val = 0
        else:
            val = 1
        self._writeReg('CFG', 'PD_FDIV_FB_CGEN', val)

    # PD_FDIV_O_CGEN
    @property
    def PD_FDIV_O_CGEN(self):
        """
        Get the value of PD_FDIV_O_CGEN
        """
        return self._readReg('CFG', 'PD_FDIV_O_CGEN')

    @PD_FDIV_O_CGEN.setter
    def PD_FDIV_O_CGEN(self, value):
        """
        Set the value of PD_FDIV_O_CGEN
        """
        if value not in [0, 1, 'ON', 'OFF']:
            raise ValueError("Value must be [0,1,'ON', 'OFF']")
        if value == 0 or value == 'ON':
            val = 0
        else:
            val = 1
        self._writeReg('CFG', 'PD_FDIV_O_CGEN', val)

    # PD_SDM_CGEN
    @property
    def PD_SDM_CGEN(self):
        """
        Get the value of PD_SDM_CGEN
        """
        return self._readReg('CFG', 'PD_SDM_CGEN')

    @PD_SDM_CGEN.setter
    def PD_SDM_CGEN(self, value):
        """
        Set the value of PD_SDM_CGEN
        """
        if value not in [0, 1, 'ON', 'OFF']:
            raise ValueError("Value must be [0,1,'ON', 'OFF']")
        if value == 0 or value == 'ON':
            val = 0
        else:
            val = 1
        self._writeReg('CFG', 'PD_SDM_CGEN', val)

    # PD_VCO_CGEN
    @property
    def PD_VCO_CGEN(self):
        """
        Get the value of PD_VCO_CGEN
        """
        return self._readReg('CFG', 'PD_VCO_CGEN')

    @PD_VCO_CGEN.setter
    def PD_VCO_CGEN(self, value):
        """
        Set the value of PD_VCO_CGEN
        """
        if value not in [0, 1, 'ON', 'OFF']:
            raise ValueError("Value must be [0,1,'ON', 'OFF']")
        if value == 0 or value == 'ON':
            val = 0
        else:
            val = 1
        self._writeReg('CFG', 'PD_VCO_CGEN', val)

    # PD_VCO_COMP_CGEN
    @property
    def PD_VCO_COMP_CGEN(self):
        """
        Get the value of PD_VCO_COMP_CGEN
        """
        return self._readReg('CFG', 'PD_VCO_COMP_CGEN')

    @PD_VCO_COMP_CGEN.setter
    def PD_VCO_COMP_CGEN(self, value):
        """
        Set the value of PD_VCO_COMP_CGEN
        """
        if value not in [0, 1, 'ON', 'OFF']:
            raise ValueError("Value must be [0,1,'ON', 'OFF']")
        if value == 0 or value == 'ON':
            val = 0
        else:
            val = 1
        self._writeReg('CFG', 'PD_VCO_COMP_CGEN', val)

    # EN_G_CGEN
    @property
    def EN_G_CGEN(self):
        """
        Get the value of EN_G_CGEN
        """
        return self._readReg('CFG', 'EN_G_CGEN')

    @EN_G_CGEN.setter
    def EN_G_CGEN(self, value):
        """
        Set the value of EN_G_CGEN
        """
        if value not in [0, 1, 'ON', 'OFF']:
            raise ValueError("Value must be [0,1,'ON', 'OFF']")
        if value == 0 or value == 'OFF':
            val = 0
        else:
            val = 1
        self._writeReg('CFG', 'EN_G_CGEN', val)

    # FRAC_SDM_CGEN
    @property
    def FRAC_SDM_CGEN(self):
        """
        Get the value of FRAC_SDM_CGEN
        """
        lsb = self._readReg('FRACL', 'FRAC_SDM_CGENL<15:0>')
        msb = self._readReg('FRACH', 'FRAC_SDM_CGENH<3:0>')
        return (msb << 16) + lsb

    @FRAC_SDM_CGEN.setter
    def FRAC_SDM_CGEN(self, value):
        """
        Set the value of FRAC_SDM_CGEN
        """
        if not (0 <= value <= 2 ** 21 - 1):
            raise ValueError("Value must be [0,2*21-1]")
        lsb = value & 0xFFFF
        msb = (value >> 16) & 0xF
        self._writeReg('FRACL', 'FRAC_SDM_CGENL<15:0>', lsb)
        self._writeReg('FRACH', 'FRAC_SDM_CGENH<3:0>', msb)

    # INT_SDM_CGEN<9:0>
    @property
    def INT_SDM_CGEN(self):
        """
        Get the value of INT_SDM_CGEN<9:0>
        """
        return self._readReg('FRACH', 'INT_SDM_CGEN<9:0>')

    @INT_SDM_CGEN.setter
    def INT_SDM_CGEN(self, value):
        """
        Set the value of INT_SDM_CGEN<9:0>
        """
        if not (0 <= value <= 1023):
            raise ValueError("Value must be [0..1023]")
        self._writeReg('FRACH', 'INT_SDM_CGEN<9:0>', value)

    #
    # CGEN_SXCFG0 (0x0089)
    #

    # REV_SDMCLK_CGEN
    @property
    def REV_SDMCLK_CGEN(self):
        """
        Get the value of REV_SDMCLK_CGEN
        """
        return self._readReg('SXCFG0', 'REV_SDMCLK_CGEN')

    @REV_SDMCLK_CGEN.setter
    def REV_SDMCLK_CGEN(self, value):
        """
        Set the value of REV_SDMCLK_CGEN
        """
        if value not in [0, 1, 'ON', 'OFF']:
            raise ValueError("Value must be [0,1,'ON', 'OFF']")
        if value == 0 or value == 'OFF':
            val = 0
        else:
            val = 1
        self._writeReg('SXCFG0', 'REV_SDMCLK_CGEN', val)

    # SEL_SDMCLK_CGEN
    @property
    def SEL_SDMCLK_CGEN(self):
        """
        Get the value of SEL_SDMCLK_CGEN
        """
        return self._readReg('SXCFG0', 'SEL_SDMCLK_CGEN')

    @SEL_SDMCLK_CGEN.setter
    def SEL_SDMCLK_CGEN(self, value):
        """
        Set the value of SEL_SDMCLK_CGEN
        """
        if value not in [0, 1, 'CLK_DIV', 'CLK_REF']:
            raise ValueError("Value must be [0,1,'CLK_DIV', 'CLK_REF']")
        if value == 0 or value == 'CLK_DIV':
            val = 0
        else:
            val = 1
        self._writeReg('SXCFG0', 'SEL_SDMCLK_CGEN', val)

    # SX_DITHER_EN_CGEN
    @property
    def SX_DITHER_EN_CGEN(self):
        """
        Get the value of SX_DITHER_EN_CGEN
        """
        return self._readReg('SXCFG0', 'SX_DITHER_EN_CGEN')

    @SX_DITHER_EN_CGEN.setter
    def SX_DITHER_EN_CGEN(self, value):
        """
        Set the value of SX_DITHER_EN_CGEN
        """
        if value not in [0, 1, 'ON', 'OFF']:
            raise ValueError("Value must be [0,1,'ON', 'OFF']")
        if value == 0 or value == 'OFF':
            val = 0
        else:
            val = 1
        self._writeReg('SXCFG0', 'SX_DITHER_EN_CGEN', val)

    # CLKH_OV_CLKL_CGEN<1:0>
    @property
    def CLKH_OV_CLKL_CGEN(self):
        """
        Get the value of CLKH_OV_CLKL_CGEN<1:0>
        """
        return self._readReg('SXCFG0', 'CLKH_OV_CLKL_CGEN<1:0>')

    @CLKH_OV_CLKL_CGEN.setter
    def CLKH_OV_CLKL_CGEN(self, value):
        """
        Set the value of CLKH_OV_CLKL_CGEN<1:0>
        """
        if not (0 <= value <= 3):
            raise ValueError("Value must be [0..3]")
        self._writeReg('SXCFG0', 'CLKH_OV_CLKL_CGEN<1:0>', value)

    # DIV_OUTCH_CGEN<7:0>
    @property
    def DIV_OUTCH_CGEN(self):
        """
        Get the value of DIV_OUTCH_CGEN<7:0>
        """
        return self._readReg('SXCFG0', 'DIV_OUTCH_CGEN<7:0>')

    @DIV_OUTCH_CGEN.setter
    def DIV_OUTCH_CGEN(self, value):
        """
        Set the value of DIV_OUTCH_CGEN<7:0>
        """
        if not (0 <= value <= 1023):
            raise ValueError("Value must be [0..255]")
        self._writeReg('SXCFG0', 'DIV_OUTCH_CGEN<7:0>', value)

    # TST_CGEN<2:0>
    @property
    def TST_CGEN(self):
        """
        Get the value of TST_CGEN<2:0>
        """
        return self._readReg('SXCFG0', 'TST_CGEN<2:0>')

    @TST_CGEN.setter
    def TST_CGEN(self, value):
        """
        Set the value of TST_CGEN<2:0>
        """
        if not (0 <= value <= 7):
            raise ValueError("Value must be [0..3]")
        self._writeReg('SXCFG0', 'TST_CGEN<2:0>', value)

    #
    # CGEN_SXCFG1 (0x008A)
    #

    # REV_CLKDAC_CGEN
    @property
    def REV_CLKDAC_CGEN(self):
        """
        Get the value of REV_CLKDAC_CGEN
        """
        return self._readReg('SXCFG1', 'REV_CLKDAC_CGEN')

    @REV_CLKDAC_CGEN.setter
    def REV_CLKDAC_CGEN(self, value):
        """
        Set the value of REV_CLKDAC_CGEN
        """
        if value not in [0, 1, 'ON', 'OFF']:
            raise ValueError("Value must be [0,1,'ON', 'OFF']")
        if value == 0 or value == 'OFF':
            val = 0
        else:
            val = 1
        self._writeReg('SXCFG1', 'REV_CLKDAC_CGEN', val)

    # REV_CLKADC_CGEN
    @property
    def REV_CLKADC_CGEN(self):
        """
        Get the value of REV_CLKADC_CGEN
        """
        return self._readReg('SXCFG1', 'REV_CLKADC_CGEN')

    @REV_CLKADC_CGEN.setter
    def REV_CLKADC_CGEN(self, value):
        """
        Set the value of REV_CLKADC_CGEN
        """
        if value not in [0, 1, 'ON', 'OFF']:
            raise ValueError("Value must be [0,1,'ON', 'OFF']")
        if value == 0 or value == 'OFF':
            val = 0
        else:
            val = 1
        self._writeReg('SXCFG1', 'REV_CLKADC_CGEN', val)

    # REVPH_PFD_CGEN
    @property
    def REVPH_PFD_CGEN(self):
        """
        Get the value of REVPH_PFD_CGEN
        """
        return self._readReg('SXCFG1', 'REVPH_PFD_CGEN')

    @REVPH_PFD_CGEN.setter
    def REVPH_PFD_CGEN(self, value):
        """
        Set the value of REVPH_PFD_CGEN
        """
        if value not in [0, 1, 'ON', 'OFF']:
            raise ValueError("Value must be [0,1,'ON', 'OFF']")
        if value == 0 or value == 'OFF':
            val = 0
        else:
            val = 1
        self._writeReg('SXCFG1', 'REVPH_PFD_CGEN', val)

    # IOFFSET_CP_CGEN<5:0>
    @property
    def IOFFSET_CP_CGEN(self):
        """
        Get the value of IOFFSET_CP_CGEN<5:0>
        """
        return self._readReg('SXCFG1', 'IOFFSET_CP_CGEN<5:0>')

    @IOFFSET_CP_CGEN.setter
    def IOFFSET_CP_CGEN(self, value):
        """
        Set the value of IOFFSET_CP_CGEN<5:0>
        """
        if not (0 <= value <= 63):
            raise ValueError("Value must be [0..63]")
        self._writeReg('SXCFG1', 'IOFFSET_CP_CGEN<5:0>', value)

    # IPULSE_CP_CGEN<5:0>
    @property
    def IPULSE_CP_CGEN(self):
        """
        Get the value of IPULSE_CP_CGEN<5:0>
        """
        return self._readReg('SXCFG1', 'IPULSE_CP_CGEN<5:0>')

    @IPULSE_CP_CGEN.setter
    def IPULSE_CP_CGEN(self, value):
        """
        Set the value of IPULSE_CP_CGEN<5:0>
        """
        if not (0 <= value <= 63):
            raise ValueError("Value must be [0..63]")
        self._writeReg('SXCFG1', 'IPULSE_CP_CGEN<5:0>', value)

    #
    # CGEN_SXCFG2 (0x008B)
    #

    # CMPLO_CTRL_CGEN
    @property
    def CMPLO_CTRL_CGEN(self):
        """
        Get the value of CMPLO_CTRL_CGEN
        """
        if self.chip.chipID == self.chip.chipIDMR3:
            return self._readReg('SXCFG2', 'CMPLO_CTRL_CGEN')
        else:
            raise ValueError("Bitfield CMPLO_CTRL_CGEN is not supported on chip version " + str(self.chip.chipID))

    @CMPLO_CTRL_CGEN.setter
    def CMPLO_CTRL_CGEN(self, value):
        """
        Set the value of CMPLO_CTRL_CGEN
        """
        if self.chip.chipID == self.chip.chipIDMR3:
            if value not in [0, 1]:
                raise ValueError("Value must be [0,1]")
            if value == 0 or value == 'OFF':
                val = 0
            else:
                val = 1
            self._writeReg('SXCFG2', 'CMPLO_CTRL_CGEN', val)
        else:
            raise ValueError("Bitfield CMPLO_CTRL_CGEN is not supported on chip version " + str(self.chip.chipID))

    # ICT_VCO_CGEN<4:0>
    @property
    def ICT_VCO_CGEN(self):
        """
        Get the value of ICT_VCO_CGEN<4:0>
        """
        return self._readReg('SXCFG2', 'ICT_VCO_CGEN<4:0>')

    @ICT_VCO_CGEN.setter
    def ICT_VCO_CGEN(self, value):
        """
        Set the value of ICT_VCO_CGEN<4:0>
        """
        if not (0 <= value <= 31):
            raise ValueError("Value must be [0..31]")
        self._writeReg('SXCFG2', 'ICT_VCO_CGEN<4:0>', value)

    # CSW_VCO_CGEN<7:0>
    @property
    def CSW_VCO_CGEN(self):
        """
        Get the value of CSW_VCO_CGEN<7:0>
        """
        return self._readReg('SXCFG2', 'CSW_VCO_CGEN<7:0>')

    @CSW_VCO_CGEN.setter
    def CSW_VCO_CGEN(self, value):
        """
        Set the value of CSW_VCO_CGEN<7:0>
        """
        if not (0 <= value <= 255):
            raise ValueError("Value must be [0..255]")
        self._writeReg('SXCFG2', 'CSW_VCO_CGEN<7:0>', value)

    # COARSE_START_CGEN
    @property
    def COARSE_START_CGEN(self):
        """
        Get the value of COARSE_START_CGEN
        """
        return self._readReg('SXCFG2', 'COARSE_START_CGEN')

    @COARSE_START_CGEN.setter
    def COARSE_START_CGEN(self, value):
        """
        Set the value of COARSE_START_CGEN
        """
        if value not in [0, 1, 'ON', 'OFF']:
            raise ValueError("Value must be [0,1,'ON', 'OFF']")
        if value == 0 or value == 'OFF':
            val = 0
        else:
            val = 1
        self._writeReg('SXCFG2', 'COARSE_START_CGEN', val)

    #
    # CGEN_SXCFG3 (0x008C)
    #

    # COARSE_STEPDONE_CGEN
    @property
    def COARSE_STEPDONE_CGEN(self):
        """
        Get the value of COARSE_STEPDONE_CGEN
        """
        return self._readReg('SXCFG3', 'COARSE_STEPDONE_CGEN')

    # COARSEPLL_COMPO_CGEN
    @property
    def COARSEPLL_COMPO_CGEN(self):
        """
        Get the value of COARSEPLL_COMPO_CGEN
        """
        return self._readReg('SXCFG3', 'COARSEPLL_COMPO_CGEN')

    # VCO_CMPHO_CGEN
    @property
    def VCO_CMPHO_CGEN(self):
        """
        Get the value of VCO_CMPHO_CGEN
        """
        return self._readReg('SXCFG3', 'VCO_CMPHO_CGEN')

    # VCO_CMPLO_CGEN
    @property
    def VCO_CMPLO_CGEN(self):
        """
        Get the value of VCO_CMPLO_CGEN
        """
        return self._readReg('SXCFG3', 'VCO_CMPLO_CGEN')

    # CP2_CGEN<3:0>
    @property
    def CP2_CGEN(self):
        """
        Get the value of CP2_CGEN<3:0>
        """
        return self._readReg('SXCFG3', 'CP2_CGEN<3:0>')

    @CP2_CGEN.setter
    def CP2_CGEN(self, value):
        """
        Set the value of CP2_CGEN<3:0>
        """
        if not (0 <= value <= 15):
            raise ValueError("Value must be [0..15]")
        self._writeReg('SXCFG3', 'CP2_CGEN<3:0>', value)

    # CP3_CGEN<3:0>
    @property
    def CP3_CGEN(self):
        """
        Get the value of CP3_CGEN<3:0>
        """
        return self._readReg('SXCFG3', 'CP3_CGEN<3:0>')

    @CP3_CGEN.setter
    def CP3_CGEN(self, value):
        """
        Set the value of CP3_CGEN<3:0>
        """
        if not (0 <= value <= 15):
            raise ValueError("Value must be [0..15]")
        self._writeReg('SXCFG3', 'CP3_CGEN<3:0>', value)

    # CZ_CGEN<3:0>
    @property
    def CZ_CGEN(self):
        """
        Get the value of CZ_CGEN<3:0>
        """
        return self._readReg('SXCFG3', 'CZ_CGEN<3:0>')

    @CZ_CGEN.setter
    def CZ_CGEN(self, value):
        """
        Set the value of CZ_CGEN<3:0>
        """
        if not (0 <= value <= 15):
            raise ValueError("Value must be [0..15]")
        self._writeReg('SXCFG3', 'CZ_CGEN<3:0>', value)

    #
    # CGEN PLL functions
    #

    def VCO_CTUNE(self, F_VCO, IntN_MODE=False):
        """
        VCO Coarse Tuning. In closed-loop mode, based on feedback from VTUNE monitoring circuit.
        F_VCO - desired VCO frequency
	    In CLKGEN VCO covers frequency range from 2.0 to 2.7 GHz, according to data given LMS7002M EVB GUI
        """
        F_REF = self.chip.fRef  # get the chip reference frequency
        # Reset PLL
        self.RESET_N_CGEN = 0

        # Enable PLL Blocks
        self.SPDUP_VCO_CGEN = 0
        self.EN_COARSE_CKLGEN = 0

        if IntN_MODE:
            self.EN_INTONLY_SDM_CGEN = 1
            self.EN_SDM_CLK_CGEN = 0
        else:
            self.EN_INTONLY_SDM_CGEN = 0
            self.EN_SDM_CLK_CGEN = 1

        self.PD_FDIV_FB_CGEN = 0
        self.PD_CP_CGEN = 0
        self.PD_FDIV_O_CGEN = 0
        self.PD_SDM_CGEN = 0
        self.PD_VCO_COMP_CGEN = 0
        self.PD_VCO_CGEN = 0
        self.EN_G_CGEN = 1

        # Calculate FB-DIV Configuration
        if IntN_MODE:
            N_INT = round(F_VCO / F_REF)
            N_FRAC = 0
        else:
            N_INT = floor(F_VCO / F_REF)
            N_FRAC = (2.0 ** 20) * ((F_VCO / F_REF) - N_INT)

        # Set PLL to operate in IntN-Mode if targeted frequency is integer multiple of reference frequency and user did not set IntN_MODE argument to True
        if N_FRAC == 0 and IntN_MODE == False:
            self.EN_INTONLY_SDM_CGEN = 1
            self.EN_SDM_CLK_CGEN = 0

        # Activate PLL
        self.RESET_N_CGEN = 1

        # Write FB-DIV Configuration
        self.INT_SDM_CGEN = (int(N_INT) - 1)
        # print N_FRAC
        self.FRAC_SDM_CGEN = int(N_FRAC)

        # Scale VCO Bias Current to maximum value
        self.ICT_VCO_CGEN = 16

        # Start VCO Coarse-Tuning Algo.
        # In CLKGEN there is only ONE VCO Core

        # Find inital CSW_VCO for targeted frequency
        csw_low = 0
        csw_high = 255
        csw = int((csw_high + csw_low + 1) / 2.0)
        iter_num = 0
        while csw_low < csw_high and iter_num <= 8:
            iter_num += 1
            self.CSW_VCO_CGEN = csw
            sleep(0.01)

            VTUNE_HIGH = 1 - self.VCO_CMPHO_CGEN
            VTUNE_LOW = self.VCO_CMPLO_CGEN

            if VTUNE_HIGH:
                # print 'VTUNE HIGH'
                csw_low = csw
                csw = int((csw_high + csw_low + 1) / 2.0)
            elif VTUNE_LOW:
                csw_high = csw
                csw = int((csw_high + csw_low + 1) / 2.0)
            else:
                break

        self.chip.log("1st step of VCO Coarse Tuning Finished.", 1)
        self.chip.log('-' * 60, 1)
        self.chip.log('CSW_VCO= %d' % (int(self.CSW_VCO_CGEN)), 1)
        self.chip.log('-' * 60, 1)
        self.chip.log('', 1)
        self.chip.log('', 1)

        csw_init = csw
        # Find 1st CSW_VCO where VTUNE_LOW=1
        VTUNE_LOW = self.VCO_CMPLO_CGEN
        while VTUNE_LOW == 0:
            csw += 1
            if csw >= 255:
                break
            self.CSW_VCO_CGEN = csw
            sleep(0.01)
            VTUNE_LOW = self.VCO_CMPLO_CGEN
        csw_max = csw

        # Find 1st CSW_VCO where VTUNE_HIGH=1
        csw = csw_init
        self.CSW_VCO_CGEN = csw
        sleep(0.01)
        VTUNE_HIGH = 1 - self.VCO_CMPHO_CGEN

        while VTUNE_HIGH == 0:
            csw = csw - 1
            if csw <= 0:
                break

            self.CSW_VCO_CGEN = csw
            sleep(0.01)
            VTUNE_HIGH = 1 - self.VCO_CMPHO_CGEN

        csw_min = csw

        csw_opt = int((csw_min + csw_max) / 2.0)
        self.CSW_VCO_CGEN = csw_opt
        sleep(0.01)
        VTUNE_HIGH = 1 - self.VCO_CMPHO_CGEN
        VTUNE_LOW = self.VCO_CMPLO_CGEN

        self.chip.log('CLKGEN VCO Coarse Frequency Tuning Done.', 1)
        self.chip.log('-' * 60, 1)
        self.chip.log('CSW_VCO= %d' % self.CSW_VCO_CGEN, 1)
        self.chip.log('min(CSW_VCO)= %d' % csw_min, 1)
        self.chip.log('max(CSW_VCO)= %d' % csw_max, 1)
        self.chip.log('VTUNE_HIGH=%d, VTUNE_LOW=%d' % (VTUNE_HIGH, VTUNE_LOW), 1)
        self.chip.log('-' * 60, 1)
        self.chip.log('', 1)
        self.chip.log('', 1)

        return True

    def setCLK(self, F_CLKH, IntN_MODE=False):
        """
        Calculates CLKGEN Output Divider Modulus. Calls VCO Corse Tuning Method. Configures CLKGEN in LMS7002.
	    F_CLKH covers continuous frequency range from 5 to 320 MHz. This is taken as a valid range for F_CLKH input argument.
        """
        if not (5.0e6 <= F_CLKH <= 3.2e8):
            raise ValueError("Not Valid CLKGEN Frequency. 5 MHz< F_CLKH < 320.0 MHz")

        OUT_MOD = 0.0
        F_VCO = F_CLKH * 2 * (OUT_MOD + 1)

        while not (2.0e9 < F_VCO <= 2.7e9):
            OUT_MOD += 1
            F_VCO = F_CLKH * 2 * (OUT_MOD + 1)

        self.chip.log('', 1)
        self.chip.log('CLKGEN OUT-DIV Modulus', 1)
        self.chip.log('-' * 60, 1)
        self.chip.log('CLKGEN OUTDIV-MOD=%d ' % OUT_MOD, 1)
        self.chip.log('', 1)
        self.chip.log('', 1)
        self.DIV_OUTCH_CGEN = int(OUT_MOD)
        self.VCO_CTUNE(F_VCO=F_VCO, IntN_MODE=IntN_MODE)
        return True

    def getVCOFrequency(self):
        """
        Returns the current CGEN output frequency
        """
        fRef = self.chip.fRef

        # Check if the CGEN is working in integer or fractional mode
        if self.EN_INTONLY_SDM_CGEN == 1:
            intNmode = True
        else:
            intNmode = False

        INT_SDM_CGEN = self.INT_SDM_CGEN
        if intNmode:
            fVCO = (INT_SDM_CGEN + 1) * fRef
        else:
            FRAC_SDM_CGEN = self.FRAC_SDM_CGEN
            fVCO = fRef * ((1.0 * FRAC_SDM_CGEN) / (2.0 ** 20) + (INT_SDM_CGEN + 1))
        return fVCO

    def getFrequency(self):
        """
        Returns the CGEN output frequency
        """
        fVCO = self.getVCOFrequency()
        return fVCO / (2.0 * (self.DIV_OUTCH_CGEN + 1.0))

    def getDACFrequency(self):
        """
        Returns the DAC clock frequency
        """
        if self.EN_ADCCLKH_CLKGN == 0:
            # DAC clock is divided
            return self.getFrequency() / (2 ** self.CLKH_OV_CLKL_CGEN)
        else:
            # DAC clock is not divided
            return self.getFrequency()

    def getADCFrequency(self):
        """
        Returns the ADC clock frequency
        """
        if self.EN_ADCCLKH_CLKGN == 1:
            # ADC clock is divided
            return self.getFrequency() / (2.0 ** self.CLKH_OV_CLKL_CGEN) / 4.0
        else:
            # ADC clock is not divided
            return self.getFrequency() / 4.0
