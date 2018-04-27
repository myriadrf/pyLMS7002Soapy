#***************************************************************
#* Name:      LMS7002_SX.py
#* Purpose:   Class implementing LMS7002 SXT/SXR functions
#* Author:    Lime Microsystems ()
#* Created:   2016-11-14
#* Copyright: Lime Microsystems (limemicro.com)
#* License:
#**************************************************************

from LMS7002_base import *
from time import sleep
from math import floor
class LMS7002_SX(LMS7002_base):
    __slots__ = []    # Used to generate error on typos
    def __init__(self, chip, Channel):
        if Channel not in ['R', 'T']:
            raise ValueError("Parameter Channel must be 'R' or 'T'")
        self.chip = chip
        self.channel = Channel
        self.prefix = "SXT_SXR_"

    # EN_DIR
    @property 
    def EN_DIR(self):
        """
        Get the value of EN_DIR
        """
        prefix = self.prefix
        self.prefix = ""
        en_dir = self._readReg('TRX_EN_DIR', 'EN_DIR')
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
        self._writeReg('TRX_EN_DIR', 'EN_DIR', value)
        self.prefix = prefix
        
    #
    # SXT_SXR_CFG0 (0x011C)
    #

    # RESET_N
    @property 
    def RESET_N(self):
        """
        Get the value of RESET_N
        """
        return self._readReg('CFG0', 'RESET_N')

    @RESET_N.setter
    def RESET_N(self, value):
        """
        Set the value of RESET_N
        """
        if value not in [0, 1, 'RESET', 'NORMAL']:
            raise ValueError("Value must be [0,1,'RESET', 'NORMAL']")
        if value==0 or value=='RESET':
            val = 0
        else:
            val = 1
        self._writeReg('CFG0', 'RESET_N', val)

    # SPDUP_VCO
    @property 
    def SPDUP_VCO(self):
        """
        Get the value of SPDUP_VCO
        """
        return self._readReg('CFG0', 'SPDUP_VCO')

    @SPDUP_VCO.setter
    def SPDUP_VCO(self, value):
        """
        Set the value of SPDUP_VCO
        """
        if value not in [0, 1, 'ON', 'OFF']:
            raise ValueError("Value must be [0,1,'ON', 'OFF']")
        if value==0 or value=='OFF':
            val = 0
        else:
            val = 1
        self._writeReg('CFG0', 'SPDUP_VCO', val)

    # BYPLDO_VCO
    @property 
    def BYPLDO_VCO(self):
        """
        Get the value of BYPLDO_VCO
        """
        return self._readReg('CFG0', 'BYPLDO_VCO')

    @BYPLDO_VCO.setter
    def BYPLDO_VCO(self, value):
        """
        Set the value of BYPLDO_VCO
        """
        if value not in [0, 1, 'BYP', 'ACT']:
            raise ValueError("Value must be [0,1,'BYP', 'ACT']")
        if value==0 or value=='ACT':
            val = 0
        else:
            val = 1
        self._writeReg('CFG0', 'BYPLDO_VCO', val)

    # EN_COARSEPLL
    @property 
    def EN_COARSEPLL(self):
        """
        Get the value of EN_COARSEPLL
        """
        return self._readReg('CFG0', 'EN_COARSEPLL')

    @EN_COARSEPLL.setter
    def EN_COARSEPLL(self, value):
        """
        Set the value of EN_COARSEPLL
        """
        if value not in [0, 1, 'ON', 'OFF']:
            raise ValueError("Value must be [0,1,'ON', 'OFF']")
        if value==0 or value=='OFF':
            val = 0
        else:
            val = 1
        self._writeReg('CFG0', 'EN_COARSEPLL', val)

    # CURLIM_VCO
    @property 
    def CURLIM_VCO(self):
        """
        Get the value of CURLIM_VCO
        """
        return self._readReg('CFG0', 'CURLIM_VCO')

    @CURLIM_VCO.setter
    def CURLIM_VCO(self, value):
        """
        Set the value of CURLIM_VCO
        """
        if value not in [0, 1, 'ON', 'OFF']:
            raise ValueError("Value must be [0,1,'ON', 'OFF']")
        if value==0 or value=='OFF':
            val = 0
        else:
            val = 1
        self._writeReg('CFG0', 'CURLIM_VCO', val)

    # EN_DIV2_DIVPROG
    @property 
    def EN_DIV2_DIVPROG(self):
        """
        Get the value of EN_DIV2_DIVPROG
        """
        return self._readReg('CFG0', 'EN_DIV2_DIVPROG')

    @EN_DIV2_DIVPROG.setter
    def EN_DIV2_DIVPROG(self, value):
        """
        Set the value of EN_DIV2_DIVPROG
        """
        if value not in [0, 1, 'ON', 'OFF']:
            raise ValueError("Value must be [0,1,'ON', 'OFF']")
        if value==0 or value=='OFF':
            val = 0
        else:
            val = 1
        self._writeReg('CFG0', 'EN_DIV2_DIVPROG', val)

    # EN_INTONLY_SDM
    @property 
    def EN_INTONLY_SDM(self):
        """
        Get the value of EN_INTONLY_SDM
        """
        return self._readReg('CFG0', 'EN_INTONLY_SDM')

    @EN_INTONLY_SDM.setter
    def EN_INTONLY_SDM(self, value):
        """
        Set the value of EN_INTONLY_SDM
        """
        if value not in [0, 1, 'FRACN', 'INTN']:
            raise ValueError("Value must be [0,1,'FRACN', 'INTN']")
        if value==0 or value=='FRACN':
            val = 0
        else:
            val = 1
        self._writeReg('CFG0', 'EN_INTONLY_SDM', val)

    # EN_SDM_CLK
    @property 
    def EN_SDM_CLK(self):
        """
        Get the value of EN_SDM_CLK
        """
        return self._readReg('CFG0', 'EN_SDM_CLK')

    @EN_SDM_CLK.setter
    def EN_SDM_CLK(self, value):
        """
        Set the value of EN_SDM_CLK
        """
        if value not in [0, 1, 'ON', 'OFF']:
            raise ValueError("Value must be [0,1,'ON', 'OFF']")
        if value==0 or value=='OFF':
            val = 0
        else:
            val = 1
        self._writeReg('CFG0', 'EN_SDM_CLK', val)

    # PD_FBDIV
    @property 
    def PD_FBDIV(self):
        """
        Get the value of PD_FBDIV
        """
        return self._readReg('CFG0', 'PD_FBDIV')

    @PD_FBDIV.setter
    def PD_FBDIV(self, value):
        """
        Set the value of PD_FBDIV
        """
        if value not in [0, 1, 'ON', 'OFF']:
            raise ValueError("Value must be [0,1,'ON', 'OFF']")
        if value==0 or value=='ON':
            val = 0
        else:
            val = 1
        self._writeReg('CFG0', 'PD_FBDIV', val)

    # PD_LOCH_T2RBUF
    @property 
    def PD_LOCH_T2RBUF(self):
        """
        Get the value of PD_LOCH_T2RBUF
        """
        return self._readReg('CFG0', 'PD_LOCH_T2RBUF')

    @PD_LOCH_T2RBUF.setter
    def PD_LOCH_T2RBUF(self, value):
        """
        Set the value of PD_LOCH_T2RBUF
        """
        if value not in [0, 1, 'ON', 'OFF']:
            raise ValueError("Value must be [0,1,'ON', 'OFF']")
        if value==0 or value=='ON':
            val = 0
        else:
            val = 1
        self._writeReg('CFG0', 'PD_LOCH_T2RBUF', val)

    # PD_CP
    @property 
    def PD_CP(self):
        """
        Get the value of PD_CP
        """
        return self._readReg('CFG0', 'PD_CP')

    @PD_CP.setter
    def PD_CP(self, value):
        """
        Set the value of PD_CP
        """
        if value not in [0, 1, 'ON', 'OFF']:
            raise ValueError("Value must be [0,1,'ON', 'OFF']")
        if value==0 or value=='ON':
            val = 0
        else:
            val = 1
        self._writeReg('CFG0', 'PD_CP', val)

    # PD_FDIV
    @property 
    def PD_FDIV(self):
        """
        Get the value of PD_FDIV
        """
        return self._readReg('CFG0', 'PD_FDIV')

    @PD_FDIV.setter
    def PD_FDIV(self, value):
        """
        Set the value of PD_FDIV
        """
        if value not in [0, 1, 'ON', 'OFF']:
            raise ValueError("Value must be [0,1,'ON', 'OFF']")
        if value==0 or value=='ON':
            val = 0
        else:
            val = 1
        self._writeReg('CFG0', 'PD_FDIV', val)

    # PD_SDM
    @property 
    def PD_SDM(self):
        """
        Get the value of PD_SDM
        """
        return self._readReg('CFG0', 'PD_SDM')

    @PD_SDM.setter
    def PD_SDM(self, value):
        """
        Set the value of PD_SDM
        """
        if value not in [0, 1, 'ON', 'OFF']:
            raise ValueError("Value must be [0,1,'ON', 'OFF']")
        if value==0 or value=='ON':
            val = 0
        else:
            val = 1
        self._writeReg('CFG0', 'PD_SDM', val)

    # PD_VCO_COMP
    @property 
    def PD_VCO_COMP(self):
        """
        Get the value of PD_VCO_COMP
        """
        return self._readReg('CFG0', 'PD_VCO_COMP')

    @PD_VCO_COMP.setter
    def PD_VCO_COMP(self, value):
        """
        Set the value of PD_VCO_COMP
        """
        if value not in [0, 1, 'ON', 'OFF']:
            raise ValueError("Value must be [0,1,'ON', 'OFF']")
        if value==0 or value=='ON':
            val = 0
        else:
            val = 1
        self._writeReg('CFG0', 'PD_VCO_COMP', val)

    # PD_VCO
    @property 
    def PD_VCO(self):
        """
        Get the value of PD_VCO
        """
        return self._readReg('CFG0', 'PD_VCO')

    @PD_VCO.setter
    def PD_VCO(self, value):
        """
        Set the value of PD_VCO
        """
        if value not in [0, 1, 'ON', 'OFF']:
            raise ValueError("Value must be [0,1,'ON', 'OFF']")
        if value==0 or value=='ON':
            val = 0
        else:
            val = 1
        self._writeReg('CFG0', 'PD_VCO', val)

    # EN_G
    @property 
    def EN_G(self):
        """
        Get the value of EN_G
        """
        return self._readReg('CFG0', 'EN_G')

    @EN_G.setter
    def EN_G(self, value):
        """
        Set the value of EN_G
        """
        if value not in [0, 1, 'ON', 'OFF']:
            raise ValueError("Value must be [0,1,'ON', 'OFF']")
        if value==0 or value=='OFF':
            val = 0
        else:
            val = 1
        self._writeReg('CFG0', 'EN_G', val)

    # FRAC_SDM
    @property 
    def FRAC_SDM(self):
        """
        Get the value of FRAC_SDM
        """
        lsb = self._readReg('FRACL', 'FRAC_SDM_L<15:0>')
        msb = self._readReg('FRACH', 'FRAC_SDM_H<3:0>')
        return (msb << 16) + lsb

    @FRAC_SDM.setter
    def FRAC_SDM(self, value):
        """
        Set the value of FRAC_SDM
        """
        if not(0<= value <=2**20-1):
            raise ValueError("Value must be [0,2*20-1]")
        lsb = value & 0xFFFF
        msb = (value >> 16) & 0xF
        self._writeReg('FRACL', 'FRAC_SDM_L<15:0>', lsb)
        self._writeReg('FRACH', 'FRAC_SDM_H<3:0>', msb)

    # INT_SDM<9:0>
    @property 
    def INT_SDM(self):
        """
        Get the value of INT_SDM<9:0>
        """
        return self._readReg('FRACH', 'INT_SDM<9:0>')

    @INT_SDM.setter
    def INT_SDM(self, value):
        """
        Set the value of INT_SDM<9:0>
        """
        if not(0<= value <=1023):
            raise ValueError("Value must be [0..1023]")
        self._writeReg('FRACH', 'INT_SDM<9:0>', value)

    #
    # SXT_SXR_CFG1 (0x011F)
    #

    # PW_DIV2_LOCH<2:0>
    @property 
    def PW_DIV2_LOCH(self):
        """
        Get the value of PW_DIV2_LOCH<2:0>
        """
        return self._readReg('CFG1', 'PW_DIV2_LOCH<2:0>')

    @PW_DIV2_LOCH.setter
    def PW_DIV2_LOCH(self, value):
        """
        Set the value of PW_DIV2_LOCH<2:0>
        """
        if not(0 <= value <= 7):
            raise ValueError("Value must be [0..7]")
        self._writeReg('CFG1', 'PW_DIV2_LOCH<2:0>', value)

    # PW_DIV4_LOCH<2:0>
    @property 
    def PW_DIV4_LOCH(self):
        """
        Get the value of PW_DIV4_LOCH<2:0>
        """
        return self._readReg('CFG1', 'PW_DIV4_LOCH<2:0>')

    @PW_DIV4_LOCH.setter
    def PW_DIV4_LOCH(self, value):
        """
        Set the value of PW_DIV4_LOCH<2:0>
        """
        if not(0 <= value <= 7):
            raise ValueError("Value must be [0..7]")
        self._writeReg('CFG1', 'PW_DIV4_LOCH<2:0>', value)

    # DIV_LOCH<2:0>
    @property 
    def DIV_LOCH(self):
        """
        Get the value of DIV_LOCH<2:0>
        """
        return self._readReg('CFG1', 'DIV_LOCH<2:0>')

    @DIV_LOCH.setter
    def DIV_LOCH(self, value):
        """
        Set the value of DIV_LOCH<2:0>
        """
        if not(0 <= value <= 7):
            raise ValueError("Value must be [0..7]")
        self._writeReg('CFG1', 'DIV_LOCH<2:0>', value)
    
    # TST_SX<2:0>
    @property 
    def TST_SX(self):
        """
        Get the value of TST_SX<2:0>
        """
        return self._readReg('CFG1', 'TST_SX<2:0>')

    @TST_SX.setter
    def TST_SX(self, value):
        """
        Set the value of TST_SX<2:0>
        """
        if not(0 <= value <= 7):
            raise ValueError("Value must be [0..7]")
        self._writeReg('CFG1', 'TST_SX<2:0>', value)

    # SEL_SDMCLK
    @property 
    def SEL_SDMCLK(self):
        """
        Get the value of SEL_SDMCLK
        """
        return self._readReg('CFG1', 'SEL_SDMCLK')

    @SEL_SDMCLK.setter
    def SEL_SDMCLK(self, value):
        """
        Set the value of SEL_SDMCLK
        """
        if value not in [0, 1, 'CLK_DIV', 'CLK_REF']:
            raise ValueError("Value must be [0,1,'CLK_DIV', 'CLK_REF']")
        if value==0 or value=='CLK_DIV':
            val = 0
        else:
            val = 1
        self._writeReg('CFG1', 'SEL_SDMCLK', val)

    # SX_DITHER_EN
    @property 
    def SX_DITHER_EN(self):
        """
        Get the value of SX_DITHER_EN
        """
        return self._readReg('CFG1', 'SX_DITHER_EN')

    @SX_DITHER_EN.setter
    def SX_DITHER_EN(self, value):
        """
        Set the value of SX_DITHER_EN
        """
        if value not in [0, 1, 'ON', 'OFF']:
            raise ValueError("Value must be [0,1,'ON', 'OFF']")
        if value==0 or value=='OFF':
            val = 0
        else:
            val = 1
        self._writeReg('CFG1', 'SX_DITHER_EN', val)

    # REV_SDMCLK
    @property 
    def REV_SDMCLK(self):
        """
        Get the value of REV_SDMCLK
        """
        return self._readReg('CFG1', 'REV_SDMCLK')

    @REV_SDMCLK.setter
    def REV_SDMCLK(self, value):
        """
        Set the value of REV_SDMCLK
        """
        if value not in [0, 1, 'ON', 'OFF']:
            raise ValueError("Value must be [0,1,'ON', 'OFF']")
        if value==0 or value=='OFF':
            val = 0
        else:
            val = 1
        self._writeReg('CFG1', 'REV_SDMCLK', val)

    #
    # SXT_SXR_VCO_BIAS (0x0120)
    #
    
    # VDIV_VCO<7:0>
    @property 
    def VDIV_VCO(self):
        """
        Get the value of VDIV_VCO<7:0>
        """
        return self._readReg('VCO_BIAS', 'VDIV_VCO<7:0>')

    @VDIV_VCO.setter
    def VDIV_VCO(self, value):
        """
        Set the value of VDIV_VCO<7:0>
        """
        if not(0<= value <=255):
            raise ValueError("Value must be [0..255]")
        self._writeReg('VCO_BIAS', 'VDIV_VCO<7:0>', value)

    # ICT_VCO<7:0>
    @property 
    def ICT_VCO(self):
        """
        Get the value of ICT_VCO<7:0>
        """
        return self._readReg('VCO_BIAS', 'ICT_VCO<7:0>')

    @ICT_VCO.setter
    def ICT_VCO(self, value):
        """
        Set the value of ICT_VCO<7:0>
        """
        if not(0<= value <=255):
            raise ValueError("Value must be [0..255]")
        self._writeReg('VCO_BIAS', 'ICT_VCO<7:0>', value)

    #
    # SXT_SXR_VCO_CFG (0x0121)
    #
    
    # RSEL_LDO_VCO<4:0>
    @property 
    def RSEL_LDO_VCO(self):
        """
        Get the value of RSEL_LDO_VCO<4:0>
        """
        return self._readReg('VCO_CFG', 'RSEL_LDO_VCO<4:0>')

    @RSEL_LDO_VCO.setter
    def RSEL_LDO_VCO(self, value):
        """
        Set the value of RSEL_LDO_VCO<4:0>
        """
        if not(0 <= value <= 31):
            raise ValueError("Value must be [0..31]")
        self._writeReg('VCO_CFG', 'RSEL_LDO_VCO<4:0>', value)

    # CSW_VCO<7:0>
    @property 
    def CSW_VCO(self):
        """
        Get the value of CSW_VCO<7:0>
        """
        return self._readReg('VCO_CFG', 'CSW_VCO<7:0>')

    @CSW_VCO.setter
    def CSW_VCO(self, value):
        """
        Set the value of CSW_VCO<7:0>
        """
        if not(0<= value <=255):
            raise ValueError("Value must be [0..255]")
        self._writeReg('VCO_CFG', 'CSW_VCO<7:0>', value)

    # SEL_VCO<1:0>
    @property 
    def SEL_VCO(self):
        """
        Get the value of SEL_VCO<1:0>
        """
        return self._readReg('VCO_CFG', 'SEL_VCO<1:0>')

    @SEL_VCO.setter
    def SEL_VCO(self, value):
        """
        Set the value of SEL_VCO<1:0>
        """
        if value not in [0,1,2, 'VCOL', 'VCOM', 'VCOH']:
            raise ValueError("Value must be [0,1,2, 'VCOL', 'VCOM', 'VCOH']")
        if value==0 or value=='VCOL':
            val = 0
        elif value==1 or value=='VCOM':
            val = 1
        else:
            val = 2
        self._writeReg('VCO_CFG', 'SEL_VCO<1:0>', val)

    # COARSE_START
    @property 
    def COARSE_START(self):
        """
        Get the value of COARSE_START
        """
        return self._readReg('VCO_CFG', 'COARSE_START')

    @COARSE_START.setter
    def COARSE_START(self, value):
        """
        Set the value of COARSE_START
        """
        if value not in [0, 1, 'ON', 'OFF']:
            raise ValueError("Value must be [0,1,'ON', 'OFF']")
        if value==0 or value=='OFF':
            val = 0
        else:
            val = 1
        self._writeReg('VCO_CFG', 'COARSE_START', val)

    #
    # SXT_SXR_PFDCP (0x0122)
    #

    # RZ_CTRL<1:0>
    @property 
    def RZ_CTRL(self):
        """
        Get the value of RZ_CTRL<1:0>
        """
        if self.chip.chipID == self.chip.chipIDMR3:        
            return self._readReg('PFDCP', 'RZ_CTRL<1:0>')
        else:
            raise ValueError("Bitfield RZ_CTRL<1:0> is not supported on chip version "+str(self.chip.chipID))


    @RZ_CTRL.setter
    def RZ_CTRL(self, value):
        """
        Set the value of RZ_CTRL<1:0>
        """
        if self.chip.chipID == self.chip.chipIDMR3:
            if value not in [0, 1, 2, 3]:
                raise ValueError("Value must be [0,1, 2, 3]")
            self._writeReg('PFDCP', 'RZ_CTRL<1:0>', val)
        else:
            raise ValueError("Bitfield RZ_CTRL<1:0> is not supported on chip version "+str(self.chip.chipID))

    # CMPLO_CTRL
    @property 
    def CMPLO_CTRL(self):
        """
        Get the value of CMPLO_CTRL
        """
        if self.chip.chipID == self.chip.chipIDMR3:        
            return self._readReg('PFDCP', 'CMPLO_CTRL')
        else:
            raise ValueError("Bitfield CMPLO_CTRL is not supported on chip version "+str(self.chip.chipID))


    @CMPLO_CTRL.setter
    def CMPLO_CTRL(self, value):
        """
        Set the value of CMPLO_CTRL
        """
        if self.chip.chipID == self.chip.chipIDMR3:
            if value not in [0, 1]:
                raise ValueError("Value must be [0,1]")
            self._writeReg('PFDCP', 'CMPLO_CTRL', val)
        else:
            raise ValueError("Bitfield CMPLO_CTRL is not supported on chip version "+str(self.chip.chipID))
    
    # REVPH_PFD
    @property 
    def REVPH_PFD(self):
        """
        Get the value of REVPH_PFD
        """
        return self._readReg('PFDCP', 'REVPH_PFD')

    @REVPH_PFD.setter
    def REVPH_PFD(self, value):
        """
        Set the value of REVPH_PFD
        """
        if value not in [0, 1, 'ON', 'OFF']:
            raise ValueError("Value must be [0,1,'ON', 'OFF']")
        if value==0 or value=='OFF':
            val = 0
        else:
            val = 1
        self._writeReg('PFDCP', 'REVPH_PFD', val)

    # IOFFSET_CP<5:0>
    @property 
    def IOFFSET_CP(self):
        """
        Get the value of IOFFSET_CP<5:0>
        """
        return self._readReg('PFDCP', 'IOFFSET_CP<5:0>')

    @IOFFSET_CP.setter
    def IOFFSET_CP(self, value):
        """
        Set the value of IOFFSET_CP<5:0>
        """
        if not(0 <= value <= 63):
            raise ValueError("Value must be [0..63]")
        self._writeReg('PFDCP', 'IOFFSET_CP<5:0>', value)

    # IPULSE_CP<5:0>
    @property 
    def IPULSE_CP(self):
        """
        Get the value of IPULSE_CP<5:0>
        """
        return self._readReg('PFDCP', 'IPULSE_CP<5:0>')

    @IPULSE_CP.setter
    def IPULSE_CP(self, value):
        """
        Set the value of IPULSE_CP<5:0>
        """
        if not(0 <= value <= 63):
            raise ValueError("Value must be [0..63]")
        self._writeReg('PFDCP', 'IPULSE_CP<5:0>', value)

    #
    # SXT_SXR_COMP_LPF (0x0123)
    #

    # COARSE_STEPDONE
    @property 
    def COARSE_STEPDONE(self):
        """
        Get the value of COARSE_STEPDONE
        """
        return self._readReg('COMP_LPF', 'COARSE_STEPDONE')

    # COARSEPLL_COMPO
    @property 
    def COARSEPLL_COMPO(self):
        """
        Get the value of COARSEPLL_COMPO
        """
        return self._readReg('COMP_LPF', 'COARSEPLL_COMPO')

    # VCO_CMPHO
    @property 
    def VCO_CMPHO(self):
        """
        Get the value of VCO_CMPHO
        """
        return self._readReg('COMP_LPF', 'VCO_CMPHO')

    # VCO_CMPLO
    @property 
    def VCO_CMPLO(self):
        """
        Get the value of VCO_CMPLO
        """
        return self._readReg('COMP_LPF', 'VCO_CMPLO')

    # CP2_PLL<3:0>
    @property 
    def CP2_PLL(self):
        """
        Get the value of CP2_PLL<3:0>
        """
        return self._readReg('COMP_LPF', 'CP2_PLL<3:0>')

    @CP2_PLL.setter
    def CP2_PLL(self, value):
        """
        Set the value of CP2_PLL<3:0>
        """
        if not(0 <= value <= 15):
            raise ValueError("Value must be [0..15]")
        self._writeReg('COMP_LPF', 'CP2_PLL<3:0>', value)

    # CP3_PLL<3:0>
    @property 
    def CP3_PLL(self):
        """
        Get the value of CP3_PLL<3:0>
        """
        return self._readReg('COMP_LPF', 'CP3_PLL<3:0>')

    @CP3_PLL.setter
    def CP3_PLL(self, value):
        """
        Set the value of CP3_PLL<3:0>
        """
        if not(0 <= value <= 15):
            raise ValueError("Value must be [0..15]")
        self._writeReg('COMP_LPF', 'CP3_PLL<3:0>', value)

    # CZ<3:0>
    @property 
    def CZ(self):
        """
        Get the value of CZ<3:0>
        """
        return self._readReg('COMP_LPF', 'CZ<3:0>')

    @CZ.setter
    def CZ(self, value):
        """
        Set the value of CZ<3:0>
        """
        if not(0 <= value <= 15):
            raise ValueError("Value must be [0..15]")
        self._writeReg('COMP_LPF', 'CZ<3:0>', value)

    #
    # SX PLL functions
    #

    def VCO_CTUNE(self, F_VCO, IntN_MODE=False, SPDUP_CTUNE=False):
        """
        VCO Coarse Tuning. In closed-loop mode, based on feedback from VTUNE monitoring circuit.
        F_VCO - desired VCO frequency
        """
        F_REF = self.chip.fRef   # get the chip reference frequency      
        
        
        # Reset PLL
        self.RESET_N=0
        
    	# Enable PLL Blocks
        self.SPDUP_VCO=0
        self.BYPLDO_VCO=1
        self.EN_COARSEPLL=0
        self.CURLIM_VCO=1                
        if (F_VCO>5.5e9):
            self.EN_DIV2_DIVPROG=1
        else:
            self.EN_DIV2_DIVPROG=0
        if (IntN_MODE):
            self.EN_INTONLY_SDM=1
            self.EN_SDM_CLK=0
        else:
            self.EN_INTONLY_SDM=0
            self.EN_SDM_CLK=1

        self.PD_FBDIV=0
        # bug!!!
        # should be set outside the method
        #self.PD_LOCH_T2RBUF=1
        self.PD_CP=0
        self.PD_FDIV=0
        self.PD_SDM=0
        self.PD_VCO_COMP=0
        self.PD_VCO=0
        self.EN_G=1
        
        # Calculate FB-DIV Configuration
        if (IntN_MODE):
            N_INT=round((F_VCO/2.0**self.EN_DIV2_DIVPROG)/F_REF)
            N_FRAC=0
            F_VCO=2.0**self.EN_DIV2_DIVPROG*N_INT*F_REF
        else:
            N_INT=floor((F_VCO/2.0**self.EN_DIV2_DIVPROG)/F_REF)
            N_FRAC=(2.0**20)*(((F_VCO/2.0**self.EN_DIV2_DIVPROG)/F_REF)-N_INT)
        
        # Set PLL to operate in IntN-Mode if targeted frequency is integer multiple of reference frequency and user did not set IntN_MODE argument to True
        if (N_FRAC==0 and IntN_MODE==False):
            self.EN_INTONLY_SDM=1
            self.EN_SDM_CLK=0

        # Activate PLL
        self.RESET_N=1
        
        # Write FB-DIV Configuration
        self.INT_SDM=(int(N_INT)-4)
        #print N_FRAC
        self.FRAC_SDM=int(N_FRAC)

        # Scale VCO Bias Current to maximum value
        self.ICT_VCO=255

        # Start VCO Coarse-Tuning Algo.
        # Find optimal VCO core for targeted frequency
        self.SEL_VCO=1
        self.CSW_VCO=7
      
        sleep(0.001)
      
        VTUNE_HIGH=1-self.VCO_CMPHO
        VTUNE_LOW=self.VCO_CMPLO
      
        if (VTUNE_LOW):
            self.SEL_VCO=0
        else:
            self.CSW_VCO=247
            sleep(0.001)
            VTUNE_HIGH=1-self.VCO_CMPHO
            VTUNE_LOW=self.VCO_CMPLO
            if (VTUNE_HIGH):
                self.SEL_VCO=2
            else:
                self.SEL_VCO=1

        # Find inital CSW_VCO for targeted frequency
        csw_low=0
        csw_high=255
        csw=int((csw_high+csw_low+1)/2.0)
        iter_num=0
        while(csw_low<csw_high and iter_num<=8):
           iter_num+=1
           self.CSW_VCO=csw
           sleep(0.001)
           
           VTUNE_HIGH=1-self.VCO_CMPHO
           VTUNE_LOW=self.VCO_CMPLO

           
           if (VTUNE_HIGH):
               #print 'VTUNE HIGH'
               csw_low=csw
               csw=int((csw_high+csw_low+1)/2.0)
           elif (VTUNE_LOW):
               csw_high=csw
               csw=int((csw_high+csw_low+1)/2.0)
           else:
                break
             
        self.chip.log("1st step of VCO Coarse Tuning Finished.", 1)
        self.chip.log('-'*60, 1)
        self.chip.log('SEL_VCO= %d' %(int(self.SEL_VCO)), 1)
        self.chip.log('CSW_VCO= %d' %(int(self.CSW_VCO)), 1)
        self.chip.log('-'*60, 1)
        self.chip.log('', 1)
        self.chip.log('', 1)

        if (not SPDUP_CTUNE):
            csw_init=csw
            # Find 1st CSW_VCO where VTUNE_LOW=1
            VTUNE_HIGH=1-self.VCO_CMPHO
            VTUNE_LOW=self.VCO_CMPLO
            while (VTUNE_LOW==0):
                  csw+=1
                  if (csw>=255):
                       break
                  self.CSW_VCO=csw
                  sleep(0.001)
                  VTUNE_HIGH=1-self.VCO_CMPHO
                  VTUNE_LOW=self.VCO_CMPLO
            csw_max=csw
        
            # Find 1st CSW_VCO where VTUNE_HIGH=1
            csw=csw_init
            self.CSW_VCO=csw
            sleep(0.001)
            VTUNE_HIGH=1-self.VCO_CMPHO
            VTUNE_LOW=self.VCO_CMPLO
            while (VTUNE_HIGH==0):
               csw=csw-1
               if (csw<=0):
                   break
      
               self.CSW_VCO=csw
               sleep(0.001)
               VTUNE_HIGH=1-self.VCO_CMPHO
               VTUNE_LOW=self.VCO_CMPLO

            csw_min=csw
        
            csw_opt=int((csw_min+csw_max)/2.0)
        else:
            csw_opt=csw
            csw_min=csw
            csw_max=csw

        self.CSW_VCO=csw_opt
        sleep(0.001)
        VTUNE_HIGH=1-self.VCO_CMPHO
        VTUNE_LOW=self.VCO_CMPLO
        
        self.chip.log('VCO Coarse Frequency Tuning Done.', 1)
        self.chip.log('-'*60, 1)
        self.chip.log('SEL_VCO= %d' %(self.SEL_VCO), 1)
        self.chip.log('CSW_VCO= %d' %(self.CSW_VCO), 1)
        self.chip.log('min(CSW_VCO)= %d' %(csw_min), 1)
        self.chip.log('max(CSW_VCO)= %d' %(csw_max), 1)
        self.chip.log('VTUNE_HIGH=%d, VTUNE_LOW=%d' %(VTUNE_HIGH, VTUNE_LOW), 1)
        self.chip.log('-'*60, 1)
        self.chip.log('', 1)
        self.chip.log('', 1)
        return True

    def setFREQ(self, F_LO, IntN_MODE=False, SPDUP_CTUNE=False, PD_TLOBUF_CTUNE=False):
        """
        Calculates FF-DIV Modulus. Calls VCO Corse Tuning Method. Configures PLL in LMS7002.
        """
        F_REF = self.chip.fRef   # get the chip reference frequency
        if not (0.24e9<=F_LO<=3.8e9):
             raise ValueError("Not Valid LO Frequency. 240 MHz< F_LO < 3.8 GHz")
        
        if (PD_TLOBUF_CTUNE):
            PD_TXMIXA=self.chip.TRF['A'].PD_TLOBUF_TRF
            PD_TXMIXB=self.chip.TRF['B'].PD_TLOBUF_TRF
            self.chip.TRF['A'].PD_TLOBUF_TRF=1
            self.chip.TRF['B'].PD_TLOBUF_TRF=1
        
        FF_MOD=0.0
        F_VCO=2*F_LO*(2**FF_MOD)

        while (not(3.8e9<F_VCO<=7.6e9)):
             FF_MOD+=1
             F_VCO=2*F_LO*(2**FF_MOD)
        
        self.chip.log('', 1)
        self.chip.log('FF-DIV Modulus', 1)
        self.chip.log('-'*60, 1)
        self.chip.log('FFDIV-MOD=%d ' %(2**FF_MOD), 1)
        self.chip.log('', 1)
        self.chip.log('', 1)
        self.DIV_LOCH=int(FF_MOD)
        self.VCO_CTUNE(F_VCO=F_VCO, IntN_MODE=IntN_MODE, SPDUP_CTUNE=SPDUP_CTUNE)
        
        if (PD_TLOBUF_CTUNE):
            self.chip.TRF['A'].PD_TLOBUF_TRF=PD_TXMIXA
            self.chip.TRF['B'].PD_TLOBUF_TRF=PD_TXMIXB
        return True

    def getVCOFrequency(self):
        """
        Returns the current SX VCO frequency
        """
        fRef = self.chip.fRef
        
        # Check if the SX is working in integer or fractional mode
        if self.EN_INTONLY_SDM==1:
            intNmode = True
        else:
            intNmode = False
        
        EN_DIV2_DIVPROG = self.EN_DIV2_DIVPROG
        INT_SDM = self.INT_SDM
        if intNmode:
            fVCO = (INT_SDM+4) * fRef * (2.0**EN_DIV2_DIVPROG)
        else:
            FRAC_SDM = self.FRAC_SDM
            fVCO = (2.0**EN_DIV2_DIVPROG) * fRef * ((1.0*FRAC_SDM)/(2.0**20) + (INT_SDM+4))
        return fVCO        

    def getFrequency(self):
        fVCO = self.getVCOFrequency()
        FF_MOD = self.DIV_LOCH
        return fVCO / (2.0 * 2**FF_MOD)
        

