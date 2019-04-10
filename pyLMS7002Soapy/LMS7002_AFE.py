# ***************************************************************
# * Name:      LMS7002_AFE.py
# * Purpose:   Class implementing LMS7002 AFE functions
# * Author:    Lime Microsystems ()
# * Created:   2016-11-14
# * Copyright: Lime Microsystems (limemicro.com)
# * License:
# **************************************************************

from pyLMS7002Soapy.LMS7002_base import LMS7002_base


class LMS7002_AFE(LMS7002_base):
    __slots__ = []  # Used to generate error on typos

    def __init__(self, chip):
        self.chip = chip
        self.channel = None
        self.prefix = "AFE_"

    #
    # AFE_CFG (0x0082)
    #

    # ISEL_DAC_AFE<2:0>
    @property
    def ISEL_DAC_AFE(self):
        """
        Get the value of ISEL_DAC_AFE<2:0>
        """
        return self._readReg('CFG', 'ISEL_DAC_AFE<2:0>')

    @ISEL_DAC_AFE.setter
    def ISEL_DAC_AFE(self, value):
        """
        Set the value of ISEL_DAC_AFE<2:0>
        """
        if not (0 <= value <= 7):
            raise ValueError("Value must be [0..7]")
        self._writeReg('CFG', 'ISEL_DAC_AFE<2:0>', value)

    # MODE_INTERLEAVE_AFE
    @property
    def MODE_INTERLEAVE_AFE(self):
        """
        Get the value of MODE_INTERLEAVE_AFE
        """
        return self._readReg('CFG', 'MODE_INTERLEAVE_AFE')

    @MODE_INTERLEAVE_AFE.setter
    def MODE_INTERLEAVE_AFE(self, value):
        """
        Set the value of MODE_INTERLEAVE_AFE
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG', 'MODE_INTERLEAVE_AFE', value)

    # MUX_AFE_1<1:0>
    @property
    def MUX_AFE_1(self):
        """
        Get the value of MUX_AFE_1<1:0>
        """
        return self._readReg('CFG', 'MUX_AFE_1<1:0>')

    @MUX_AFE_1.setter
    def MUX_AFE_1(self, value):
        """
        Set the value of MUX_AFE_1<1:0>
        """
        if not (0 <= value <= 3):
            raise ValueError("Value must be [0..3]")
        self._writeReg('CFG', 'MUX_AFE_1<1:0>', value)

    # MUX_AFE_2<1:0>
    @property
    def MUX_AFE_2(self):
        """
        Get the value of MUX_AFE_2<1:0>
        """
        return self._readReg('CFG', 'MUX_AFE_2<1:0>')

    @MUX_AFE_2.setter
    def MUX_AFE_2(self, value):
        """
        Set the value of MUX_AFE_2<1:0>
        """
        if not (0 <= value <= 3):
            raise ValueError("Value must be [0..3]")
        self._writeReg('CFG', 'MUX_AFE_2<1:0>', value)

    # PD_AFE
    @property
    def PD_AFE(self):
        """
        Get the value of PD_AFE
        """
        return self._readReg('CFG', 'PD_AFE')

    @PD_AFE.setter
    def PD_AFE(self, value):
        """
        Set the value of PD_AFE
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG', 'PD_AFE', value)

    # PD_RX_AFE1
    @property
    def PD_RX_AFE1(self):
        """
        Get the value of PD_RX_AFE1
        """
        return self._readReg('CFG', 'PD_RX_AFE1')

    @PD_RX_AFE1.setter
    def PD_RX_AFE1(self, value):
        """
        Set the value of PD_RX_AFE1
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG', 'PD_RX_AFE1', value)

    # PD_RX_AFE2
    @property
    def PD_RX_AFE2(self):
        """
        Get the value of PD_RX_AFE2
        """
        return self._readReg('CFG', 'PD_RX_AFE2')

    @PD_RX_AFE2.setter
    def PD_RX_AFE2(self, value):
        """
        Set the value of PD_RX_AFE2
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG', 'PD_RX_AFE2', value)

    # PD_TX_AFE1
    @property
    def PD_TX_AFE1(self):
        """
        Get the value of PD_TX_AFE1
        """
        return self._readReg('CFG', 'PD_TX_AFE1')

    @PD_TX_AFE1.setter
    def PD_TX_AFE1(self, value):
        """
        Set the value of PD_TX_AFE1
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG', 'PD_TX_AFE1', value)

    # PD_TX_AFE2
    @property
    def PD_TX_AFE2(self):
        """
        Get the value of PD_TX_AFE2
        """
        return self._readReg('CFG', 'PD_TX_AFE2')

    @PD_TX_AFE2.setter
    def PD_TX_AFE2(self, value):
        """
        Set the value of PD_TX_AFE2
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG', 'PD_TX_AFE2', value)

    # EN_G_AFE
    @property
    def EN_G_AFE(self):
        """
        Get the value of EN_G_AFE
        """
        return self._readReg('CFG', 'EN_G_AFE')

    @EN_G_AFE.setter
    def EN_G_AFE(self, value):
        """
        Set the value of EN_G_AFE
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG', 'EN_G_AFE', value)
