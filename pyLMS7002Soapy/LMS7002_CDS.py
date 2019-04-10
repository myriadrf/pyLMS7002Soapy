# ***************************************************************
# * Name:      LMS7002_CDS.py
# * Purpose:   Class implementing LMS7002 CDS functions
# * Author:    Lime Microsystems ()
# * Created:   2016-11-14
# * Copyright: Lime Microsystems (limemicro.com)
# * License:
# **************************************************************

from pyLMS7002Soapy.LMS7002_base import LMS7002_base


class LMS7002_CDS(LMS7002_base):
    __slots__ = []  # Used to generate error on typos

    def __init__(self, chip):
        self.chip = chip
        self.channel = None
        self.prefix = "CDS_"

    #
    # CDS_CFG0 (0x00AD)
    #

    # CDS_MCLK2<1:0>
    @property
    def CDS_MCLK2(self):
        """
        Get the value of CDS_MCLK2<1:0>
        """
        return self._readReg('CFG0', 'CDS_MCLK2<1:0>')

    @CDS_MCLK2.setter
    def CDS_MCLK2(self, value):
        """
        Set the value of CDS_MCLK2<1:0>
        """
        if not (0 <= value <= 3):
            raise ValueError("Value must be [0..3]")
        self._writeReg('CFG0', 'CDS_MCLK2<1:0>', value)

    # CDS_MCLK1<1:0>
    @property
    def CDS_MCLK1(self):
        """
        Get the value of CDS_MCLK1<1:0>
        """
        return self._readReg('CFG0', 'CDS_MCLK1<1:0>')

    @CDS_MCLK1.setter
    def CDS_MCLK1(self, value):
        """
        Set the value of CDS_MCLK1<1:0>
        """
        if not (0 <= value <= 3):
            raise ValueError("Value must be [0..3]")
        self._writeReg('CFG0', 'CDS_MCLK1<1:0>', value)

    # CDSN_TXBTSP
    @property
    def CDSN_TXBTSP(self):
        """
        Get the value of CDSN_TXBTSP
        """
        return self._readReg('CFG0', 'CDSN_TXBTSP')

    @CDSN_TXBTSP.setter
    def CDSN_TXBTSP(self, value):
        """
        Set the value of CDSN_TXBTSP
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG0', 'CDSN_TXBTSP', value)

    # CDSN_TXATSP
    @property
    def CDSN_TXATSP(self):
        """
        Get the value of CDSN_TXATSP
        """
        return self._readReg('CFG0', 'CDSN_TXATSP')

    @CDSN_TXATSP.setter
    def CDSN_TXATSP(self, value):
        """
        Set the value of CDSN_TXATSP
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG0', 'CDSN_TXATSP', value)

    # CDSN_RXBTSP
    @property
    def CDSN_RXBTSP(self):
        """
        Get the value of CDSN_RXBTSP
        """
        return self._readReg('CFG0', 'CDSN_RXBTSP')

    @CDSN_RXBTSP.setter
    def CDSN_RXBTSP(self, value):
        """
        Set the value of CDSN_RXBTSP
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG0', 'CDSN_RXBTSP', value)

    # CDSN_RXATSP
    @property
    def CDSN_RXATSP(self):
        """
        Get the value of CDSN_RXATSP
        """
        return self._readReg('CFG0', 'CDSN_RXATSP')

    @CDSN_RXATSP.setter
    def CDSN_RXATSP(self, value):
        """
        Set the value of CDSN_RXATSP
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG0', 'CDSN_RXATSP', value)

    # CDSN_TXBLML
    @property
    def CDSN_TXBLML(self):
        """
        Get the value of CDSN_TXBLML
        """
        return self._readReg('CFG0', 'CDSN_TXBLML')

    @CDSN_TXBLML.setter
    def CDSN_TXBLML(self, value):
        """
        Set the value of CDSN_TXBLML
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG0', 'CDSN_TXBLML', value)

    # CDSN_TXALML
    @property
    def CDSN_TXALML(self):
        """
        Get the value of CDSN_TXALML
        """
        return self._readReg('CFG0', 'CDSN_TXALML')

    @CDSN_TXALML.setter
    def CDSN_TXALML(self, value):
        """
        Set the value of CDSN_TXALML
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG0', 'CDSN_TXALML', value)

    # CDSN_RXBLML
    @property
    def CDSN_RXBLML(self):
        """
        Get the value of CDSN_RXBLML
        """
        return self._readReg('CFG0', 'CDSN_RXBLML')

    @CDSN_RXBLML.setter
    def CDSN_RXBLML(self, value):
        """
        Set the value of CDSN_RXBLML
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG0', 'CDSN_RXBLML', value)

    # CDSN_RXALML
    @property
    def CDSN_RXALML(self):
        """
        Get the value of CDSN_RXALML
        """
        return self._readReg('CFG0', 'CDSN_RXALML')

    @CDSN_RXALML.setter
    def CDSN_RXALML(self, value):
        """
        Set the value of CDSN_RXALML
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG0', 'CDSN_RXALML', value)

    # CDSN_MCLK2
    @property
    def CDSN_MCLK2(self):
        """
        Get the value of CDSN_MCLK2
        """
        return self._readReg('CFG0', 'CDSN_MCLK2')

    @CDSN_MCLK2.setter
    def CDSN_MCLK2(self, value):
        """
        Set the value of CDSN_MCLK2
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG0', 'CDSN_MCLK2', value)

    # CDSN_MCLK1
    @property
    def CDSN_MCLK1(self):
        """
        Get the value of CDSN_MCLK1
        """
        return self._readReg('CFG0', 'CDSN_MCLK1')

    @CDSN_MCLK1.setter
    def CDSN_MCLK1(self, value):
        """
        Set the value of CDSN_MCLK1
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG0', 'CDSN_MCLK1', value)

    # CDS_TXBTSP<1:0>
    @property
    def CDS_TXBTSP(self):
        """
        Get the value of CDS_TXBTSP<1:0>
        """
        return self._readReg('CFG1', 'CDS_TXBTSP<1:0>')

    @CDS_TXBTSP.setter
    def CDS_TXBTSP(self, value):
        """
        Set the value of CDS_TXBTSP<1:0>
        """
        if not (0 <= value <= 3):
            raise ValueError("Value must be [0..3]")
        self._writeReg('CFG1', 'CDS_TXBTSP<1:0>', value)

    # CDS_TXATSP<1:0>
    @property
    def CDS_TXATSP(self):
        """
        Get the value of CDS_TXATSP<1:0>
        """
        return self._readReg('CFG1', 'CDS_TXATSP<1:0>')

    @CDS_TXATSP.setter
    def CDS_TXATSP(self, value):
        """
        Set the value of CDS_TXATSP<1:0>
        """
        if not (0 <= value <= 3):
            raise ValueError("Value must be [0..3]")
        self._writeReg('CFG1', 'CDS_TXATSP<1:0>', value)

    # CDS_RXBTSP<1:0>
    @property
    def CDS_RXBTSP(self):
        """
        Get the value of CDS_RXBTSP<1:0>
        """
        return self._readReg('CFG1', 'CDS_RXBTSP<1:0>')

    @CDS_RXBTSP.setter
    def CDS_RXBTSP(self, value):
        """
        Set the value of CDS_RXBTSP<1:0>
        """
        if not (0 <= value <= 3):
            raise ValueError("Value must be [0..3]")
        self._writeReg('CFG1', 'CDS_RXBTSP<1:0>', value)

    # CDS_RXATSP<1:0>
    @property
    def CDS_RXATSP(self):
        """
        Get the value of CDS_RXATSP<1:0>
        """
        return self._readReg('CFG1', 'CDS_RXATSP<1:0>')

    @CDS_RXATSP.setter
    def CDS_RXATSP(self, value):
        """
        Set the value of CDS_RXATSP<1:0>
        """
        if not (0 <= value <= 3):
            raise ValueError("Value must be [0..3]")
        self._writeReg('CFG1', 'CDS_RXATSP<1:0>', value)

    # CDS_TXBLML<1:0>
    @property
    def CDS_TXBLML(self):
        """
        Get the value of CDS_TXBLML<1:0>
        """
        return self._readReg('CFG1', 'CDS_TXBLML<1:0>')

    @CDS_TXBLML.setter
    def CDS_TXBLML(self, value):
        """
        Set the value of CDS_TXBLML<1:0>
        """
        if not (0 <= value <= 3):
            raise ValueError("Value must be [0..3]")
        self._writeReg('CFG1', 'CDS_TXBLML<1:0>', value)

    # CDS_TXALML<1:0>
    @property
    def CDS_TXALML(self):
        """
        Get the value of CDS_TXALML<1:0>
        """
        return self._readReg('CFG1', 'CDS_TXALML<1:0>')

    @CDS_TXALML.setter
    def CDS_TXALML(self, value):
        """
        Set the value of CDS_TXALML<1:0>
        """
        if not (0 <= value <= 3):
            raise ValueError("Value must be [0..3]")
        self._writeReg('CFG1', 'CDS_TXALML<1:0>', value)

    # CDS_RXBLML<1:0>
    @property
    def CDS_RXBLML(self):
        """
        Get the value of CDS_RXBLML<1:0>
        """
        return self._readReg('CFG1', 'CDS_RXBLML<1:0>')

    @CDS_RXBLML.setter
    def CDS_RXBLML(self, value):
        """
        Set the value of CDS_RXBLML<1:0>
        """
        if not (0 <= value <= 3):
            raise ValueError("Value must be [0..3]")
        self._writeReg('CFG1', 'CDS_RXBLML<1:0>', value)

    # CDS_RXALML<1:0>
    @property
    def CDS_RXALML(self):
        """
        Get the value of CDS_RXALML<1:0>
        """
        return self._readReg('CFG1', 'CDS_RXALML<1:0>')

    @CDS_RXALML.setter
    def CDS_RXALML(self, value):
        """
        Set the value of CDS_RXALML<1:0>
        """
        if not (0 <= value <= 3):
            raise ValueError("Value must be [0..3]")
        self._writeReg('CFG1', 'CDS_RXALML<1:0>', value)
