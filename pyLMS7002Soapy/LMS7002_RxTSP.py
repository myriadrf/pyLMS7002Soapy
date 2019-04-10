# ***************************************************************
# * Name:      LMS7002_RxTSP.py
# * Purpose:   Class implementing LMS7002 RxTSP functions
# * Author:    Lime Microsystems ()
# * Created:   2016-11-14
# * Copyright: Lime Microsystems (limemicro.com)
# * License:
# **************************************************************

from pyLMS7002Soapy.LMS7002_base import LMS7002_base


class LMS7002_RxTSP(LMS7002_base):
    __slots__ = []  # Used to generate error on typos

    def __init__(self, chip, Channel):
        if Channel not in ['A', 'B']:
            raise ValueError("Parameter Channel must be 'A' or 'B'")
        self.chip = chip
        self.channel = Channel
        self.prefix = "RXTSP_"

    #
    # RXTSP_CFG (0x0400) 
    #

    # CAPTURE
    @property
    def CAPTURE(self):
        """
        Get the value of CAPTURE
        """
        return self._readReg('CFG', 'CAPTURE')

    @CAPTURE.setter
    def CAPTURE(self, value):
        """
        Set the value of CAPTURE
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG', 'CAPTURE', value)

    # CAPSEL<1:0>
    @property
    def CAPSEL(self):
        """
        Get the value of CAPSEL<1:0>
        """
        return self._readReg('CFG', 'CAPSEL<1:0>')

    @CAPSEL.setter
    def CAPSEL(self, value):
        """
        Set the value of CAPSEL<1:0>
        """
        if value not in [0, 1, 'RSSI', 'ADC']:
            raise ValueError("Value must be [0,1, 'RSSI', 'ADC']")
        if value == 0 or value == 'RSSI':
            val = 0
        else:
            val = 1
        self._writeReg('CFG', 'CAPSEL<1:0>', val)

    # CAPSEL_ADC
    @property
    def CAPSEL_ADC(self):
        """
        Get the value of CAPSEL_ADC
        """
        if self.chip.chipID == self.chip.chipIDMR3:
            return self._readReg('CFG', 'CAPSEL_ADC')
        else:
            raise ValueError("Bitfield CAPSEL_ADC is not supported on chip version " + str(self.chip.chipID))

    @CAPSEL_ADC.setter
    def CAPSEL_ADC(self, value):
        """
        Set the value of CAPSEL_ADC
        """
        if self.chip.chipID == self.chip.chipIDMR3:
            if value not in [0, 1, 'IN', 'OUT']:
                raise ValueError("Value must be [0,1, 'IN', 'OUT']")
            if value == 0 or value == 'IN':
                val = 0
            else:
                val = 1
            self._writeReg('CFG', 'CAPSEL_ADC', val)
        else:
            raise ValueError("Bitfield CAPSEL_ADC is not supported on chip version " + str(self.chip.chipID))

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
        if value not in [0, 1, '-6dB', 'FULL']:
            raise ValueError("Value must be [0,1, '-6dB', 'FULL']")
        if value == 0 or value == '-6dB':
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
        if value not in [1, 2, 'CLK/8', 'CLK/4']:
            raise ValueError("Value must be [1,2, 'CLK/8', 'CLK/4']")
        if value == 1 or value == 'CLK/8':
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
        if value not in [0, 1]:
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
        if value not in [0, 1]:
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
        if value not in [0, 1]:
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
        if value not in [0, 1, 'NCO', 'DC']:
            raise ValueError("Value must be [0,1, 'NCO', 'DC']")
        if value == 0 or value == 'NCO':
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
        if value not in [0, 1, 'LML', 'TEST']:
            raise ValueError("Value must be [0,1, 'LML', 'TEST']")
        if value == 0 or value == 'LML':
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
        if value not in [0, 1, 'OFF', 'ON']:
            raise ValueError("Value must be [0,1, 'OFF', 'ON']")
        if value == 0 or value == 'OFF':
            val = 0
        else:
            val = 1
        self._writeReg('CFG', 'EN', val)

    #
    # RXTSP_GCORRQ (0x0401) GCORRQ<10:0>
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
        if not (0 <= value <= 2047):
            raise ValueError("Value must be [0..2047]")
        self._writeReg('GCORRQ', 'GCORRQ<10:0>', value)

    #
    # RXTSP_GCORRI (0x0402) GCORRI<10:0>
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
        if not (0 <= value <= 2047):
            raise ValueError("Value must be [0..2047]")
        self._writeReg('GCORRI', 'GCORRI<10:0>', value)

    #
    # RXTSP_INTPH (0x0403)
    #

    # HBD_OVR<2:0>
    @property
    def HBD_OVR(self):
        """
        Get the value of HBD_OVR
        """
        return self._readReg('INTPH', 'HBD_OVR<2:0>')

    @HBD_OVR.setter
    def HBD_OVR(self, value):
        """
        Set the value of HBD_OVR
        """
        if value not in [0, 1, 2, 3, 4, 7, '2', '4', '8', '16', '32', 'BYP']:
            raise ValueError("Value must be [0,1,2,3,4,7, '2', '4', '8', '16', '32', 'BYP']")
        if value == 0 or value == '2':
            val = 0
        elif value == 1 or value == '4':
            val = 1
        elif value == 2 or value == '8':
            val = 2
        elif value == 3 or value == '16':
            val = 3
        elif value == 4 or value == '32':
            val = 4
        else:
            val = 7
        self._writeReg('INTPH', 'HBD_OVR<2:0>', val)

    # IQCORR<11:0>
    @property
    def IQCORR(self):
        """
        Get the value of IQCORR<11:0>
        """
        return self.twosComplementToInt(self._readReg('INTPH', 'IQCORR<11:0>'), 12)

    @IQCORR.setter
    def IQCORR(self, value):
        """
        Set the value of IQCORR<11:0>
        """
        if not (-2048 <= value <= 2047):
            raise ValueError("Value must be [-2048..2047]")
        self._writeReg('INTPH', 'IQCORR<11:0>', self.intTo2sComplement(value, 12))

    #
    # RXTSP_DCCORR_AVG (0x0404)
    #

    # HBD_DLY
    @property
    def HBD_DLY(self):
        """
        Get the value of HBD_DLY<2:0>
        """
        if self.chip.chipID == self.chip.chipIDMR3:
            return self._readReg('DCCORRAVG', 'HBD_DLY<2:0>')
        else:
            raise ValueError("Bitfield HBD_DLY<2:0> is not supported on chip version " + str(self.chip.chipID))

    @HBD_DLY.setter
    def HBD_DLY(self, value):
        """
        Set the value of HBD_DLY<2:0>
        """
        if self.chip.chipID == self.chip.chipIDMR3:
            if not (0 <= value <= 7):
                raise ValueError("Value must be [0..7]")
            self._writeReg('DCCORRAVG', 'HBD_DLY<2:0>', value)
        else:
            raise ValueError("Bitfield HBD_DLY<2:0> is not supported on chip version " + str(self.chip.chipID))

    # DCCORR_AVG<2:0>
    @property
    def DCCORR_AVG(self):
        """
        Get the value of DCCORR_AVG<2:0>
        """
        return self._readReg('DCCORRAVG', 'DCCORR_AVG<2:0>')

    @DCCORR_AVG.setter
    def DCCORR_AVG(self, value):
        """
        Set the value of DCCORR_AVG<2:0>
        """
        if not (0 <= value <= 7):
            raise ValueError("Value must be [0..7]")
        self._writeReg('DCCORRAVG', 'DCCORR_AVG<2:0>', value)

    #
    # RXTSP_GFIR1 (0x0405)
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
        if not (0 <= value <= 7):
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
        if not (0 <= value <= 255):
            raise ValueError("Value must be [0..255]")
        self._writeReg('GFIR1', 'GFIR1_N<7:0>', value)

    #
    # RXTSP_GFIR2 (0x0406)
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
        if not (0 <= value <= 7):
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
        if not (0 <= value <= 255):
            raise ValueError("Value must be [0..255]")
        self._writeReg('GFIR2', 'GFIR2_N<7:0>', value)

    #
    # RXTSP_GFIR3 (0x0407)
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
        if not (0 <= value <= 7):
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
        if not (0 <= value <= 255):
            raise ValueError("Value must be [0..255]")
        self._writeReg('GFIR3', 'GFIR3_N<7:0>', value)

    #
    # AGC_K
    #

    @property
    def AGC_K(self):
        """
        Get the value of AGC<17:0>
        """
        valH = self._readReg('AGC1', 'AGC_K<17:16>')
        valL = self._readReg('AGC0', 'AGC_K<15:0>')
        return (valH << 16) + valL

    @AGC_K.setter
    def AGC_K(self, value):
        """
        Set the value of AGC_K
        """
        if not (0 <= value <= 2 ** 18 - 1):
            raise ValueError("Value must be [0..2^18-1]")
        valL = value & 0xFFFF
        valH = (value >> 16) & 0x3
        self._writeReg('AGC1', 'AGC_K<17:16>', valH)
        self._writeReg('AGC0', 'AGC_K<15:0>', valL)

    # AGC_DESIRED<11:0>
    @property
    def AGC_DESIRED(self):
        """
        Get the value of AGC_DESIRED<11:0>
        """
        return self._readReg('AGC1', 'AGC_DESIRED<11:0>')

    @AGC_DESIRED.setter
    def AGC_DESIRED(self, value):
        """
        Set the value of AGC_DESIRED<11:0>
        """
        if not (0 <= value <= 2 ** 12 - 1):
            raise ValueError("Value must be [0..2^12-1]")
        self._writeReg('AGC1', 'AGC_DESIRED<11:0>', value)

    #
    # RXTSP_AGC2 (0x040A)
    #

    # RSSI_MODE<1:0>
    @property
    def RSSI_MODE(self):
        """
        Get the value of RSSI_MODE<1:0>
        """
        return self._readReg('AGC2', 'RSSI_MODE<1:0>')

    @RSSI_MODE.setter
    def RSSI_MODE(self, value):
        """
        Set the value of RSSI_MODE<1:0>
        """
        if value not in [0, 1, 2, 'RSSI', 'I', 'Q']:
            raise ValueError("Value must be [0,1,2,'RSSI', 'I', 'Q']")
        if value == 0 or value == 'RSSI':
            val = 0
        elif value == 1 or value == 'I':
            val = 1
        elif value == 2 or value == 'Q':
            val = 2
        else:
            raise ValueError("Value of 3 is not allowed")
        self._writeReg('AGC2', 'RSSI_MODE<1:0>', val)

    # AGC_MODE<1:0>
    @property
    def AGC_MODE(self):
        """
        Get the value of AGC_MODE<1:0>
        """
        return self._readReg('AGC2', 'AGC_MODE<1:0>')

    @AGC_MODE.setter
    def AGC_MODE(self, value):
        """
        Set the value of AGC_MODE<1:0>
        """
        if value not in [0, 1, 2, 3, 'AGC', 'RSSI', 'BYP']:
            raise ValueError("Value must be [0,1,2,3,'AGC', 'RSSI', 'BYP']")
        if value == 0 or value == 'AGC':
            val = 0
        elif value == 1 or value == 'RSSI':
            val = 1
        else:
            val = 2
        self._writeReg('AGC2', 'AGC_MODE<1:0>', val)

    # AGC_AVG<2:0>
    @property
    def AGC_AVG(self):
        """
        Get the value of AGC_AVG<2:0>
        """
        return self._readReg('AGC2', 'AGC_AVG<2:0>')

    @AGC_AVG.setter
    def AGC_AVG(self, value):
        """
        Set the value of AGC_AVG<2:0>
        """
        if not (0 <= value <= 7):
            raise ValueError("Value must be [0..7]")
        self._writeReg('AGC2', 'AGC_AVG<2:0>', value)

    #
    # RXTSP_DC (0x040B) DC_REG<15:0>
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
        if not (0 <= value <= 65535):
            raise ValueError("Value must be [0..65535]")
        self._writeReg('DC', 'DC_REG<15:0>', value)

        #

    # RXTSP_CMIXBYP (0x040C)
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
        if value not in [0, 1, 2, 3, '0dB', '6dB', '-6dB']:
            raise ValueError("Value must be [0,1,2,3,'0dB', '6dB', '-6dB']")
        if value == 0 or value == '0dB':
            val = 0
        elif value == 1 or value == '6dB':
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
        if value not in [0, 1, 'UP', 'DOWN']:
            raise ValueError("Value must be [0,1,'UP', 'DOWN']")
        if value == 0 or value == 'UP':
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
            raise ValueError("Bitfield CMIX_GAIN2 is not supported on chip version " + str(self.chip.chipID))

    @CMIX_GAIN2.setter
    def CMIX_GAIN2(self, value):
        """
        Set the value of CMIX_GAIN2
        """
        if self.chip.chipID == self.chip.chipIDMR3:
            if value not in [0, 1]:
                raise ValueError("Value must be [0,1]")
            self._writeReg('CMIXBYP', 'CMIX_GAIN2', value)
        else:
            raise ValueError("Bitfield CMIX_GAIN2 is not supported on chip version " + str(self.chip.chipID))

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
        if value not in [0, 1, 'USE', 'BYP']:
            raise ValueError("Value must be [0,1,'USE', 'BYP']")
        if value == 0 or value == 'USE':
            val = 0
        else:
            val = 1
        self._writeReg('CMIXBYP', 'CMIX_BYP', val)

    # AGC_BYP
    @property
    def AGC_BYP(self):
        """
        Get the value of AGC_BYP
        """
        return self._readReg('CMIXBYP', 'AGC_BYP')

    @AGC_BYP.setter
    def AGC_BYP(self, value):
        """
        Set the value of AGC_BYP
        """
        if value not in [0, 1, 'USE', 'BYP']:
            raise ValueError("Value must be [0,1,'USE', 'BYP']")
        if value == 0 or value == 'USE':
            val = 0
        else:
            val = 1
        self._writeReg('CMIXBYP', 'AGC_BYP', val)

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
        if value not in [0, 1, 'USE', 'BYP']:
            raise ValueError("Value must be [0,1,'USE', 'BYP']")
        if value == 0 or value == 'USE':
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
        if value not in [0, 1, 'USE', 'BYP']:
            raise ValueError("Value must be [0,1,'USE', 'BYP']")
        if value == 0 or value == 'USE':
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
        if value not in [0, 1, 'USE', 'BYP']:
            raise ValueError("Value must be [0,1,'USE', 'BYP']")
        if value == 0 or value == 'USE':
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
        if value not in [0, 1, 'USE', 'BYP']:
            raise ValueError("Value must be [0,1,'USE', 'BYP']")
        if value == 0 or value == 'USE':
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
        if value not in [0, 1, 'USE', 'BYP']:
            raise ValueError("Value must be [0,1,'USE', 'BYP']")
        if value == 0 or value == 'USE':
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
        if value not in [0, 1, 'USE', 'BYP']:
            raise ValueError("Value must be [0,1,'USE', 'BYP']")
        if value == 0 or value == 'USE':
            val = 0
        else:
            val = 1
        self._writeReg('CMIXBYP', 'PH_BYP', val)

    #
    # RXTSP_CAPDL (0x040E) CAPDL<15:0>
    #
    @property
    def CAPDL(self):
        """
        Get the value of CAPDL<15:0>
        """
        return self._readReg('CAPDL', 'CAPDL<15:0>')

    @CAPDL.setter
    def CAPDL(self, value):
        """
        Set the value of CAPDL<15:0>
        """
        if not (0 <= value <= 65535):
            raise ValueError("Value must be [0..65535]")
        self._writeReg('CAPDL', 'CAPDL<15:0>', value)

        #

    # RXTSP_CAPDH (0x040F) CAPDH<15:0>
    #
    @property
    def CAPDH(self):
        """
        Get the value of CAPDH<15:0>
        """
        return self._readReg('CAPDH', 'CAPDH<15:0>')

    @CAPDH.setter
    def CAPDH(self, value):
        """
        Set the value of CAPDH<15:0>
        """
        if not (0 <= value <= 65535):
            raise ValueError("Value must be [0..65535]")
        self._writeReg('CAPDH', 'CAPDH<15:0>', value)

        #

    # Convenience functions
    #

    @property
    def CAPD(self):
        self.CAPTURE = 0
        self.CAPTURE = 1
        self.CAPTURE = 0
        CAPDH = self.CAPDH
        CAPDL = self.CAPDL
        return (CAPDH << 2) + CAPDL

    @property
    def RSSI(self):
        oldVal = self.CAPSEL
        self.CAPSEL = 'RSSI'
        ret = self.CAPD
        self.CAPSEL = oldVal
        return ret

    @property
    def ADCIQ(self):
        # Returns (I,Q)
        if self.chip.chipID == self.chip.chipIDMR3:
            if self.CAPSEL_ADC == 0:
                nBits = 10
            else:
                nBits = 16
        else:
            nBits = 10
        oldVal = self.CAPSEL
        self.CAPSEL = 'ADC'
        self.CAPTURE = 0
        self.CAPTURE = 1
        self.CAPTURE = 0
        CAPDH = self.twosComplementToInt(self.CAPDH, nBits)
        CAPDL = self.twosComplementToInt(self.CAPDL, nBits)
        self.CAPSEL = oldVal
        return CAPDL, CAPDH
