# ***************************************************************
# * Name:      LMS7002_XBUF.py
# * Purpose:   Class implementing LMS7002 XBUF functions
# * Author:    Lime Microsystems ()
# * Created:   2016-11-14
# * Copyright: Lime Microsystems (limemicro.com)
# * License:
# **************************************************************

from pyLMS7002Soapy.LMS7002_base import LMS7002_base


class LMS7002_XBUF(LMS7002_base):
    __slots__ = []  # Used to generate error on typos

    def __init__(self, chip):
        self.chip = chip
        self.channel = None
        self.prefix = "XBUF_"

    #
    # XBUF_CFG (0x0085)
    #

    # SLFB_XBUF_RX
    @property
    def SLFB_XBUF_RX(self):
        """
        Get the value of SLFB_XBUF_RX
        """
        return self._readReg('CFG', 'SLFB_XBUF_RX')

    @SLFB_XBUF_RX.setter
    def SLFB_XBUF_RX(self, value):
        """
        Set the value of SLFB_XBUF_RX
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG', 'SLFB_XBUF_RX', value)

    # SLFB_XBUF_TX
    @property
    def SLFB_XBUF_TX(self):
        """
        Get the value of SLFB_XBUF_TX
        """
        return self._readReg('CFG', 'SLFB_XBUF_TX')

    @SLFB_XBUF_TX.setter
    def SLFB_XBUF_TX(self, value):
        """
        Set the value of SLFB_XBUF_TX
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG', 'SLFB_XBUF_TX', value)

    # BYP_XBUF_RX
    @property
    def BYP_XBUF_RX(self):
        """
        Get the value of BYP_XBUF_RX
        """
        return self._readReg('CFG', 'BYP_XBUF_RX')

    @BYP_XBUF_RX.setter
    def BYP_XBUF_RX(self, value):
        """
        Set the value of BYP_XBUF_RX
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG', 'BYP_XBUF_RX', value)

    # BYP_XBUF_TX
    @property
    def BYP_XBUF_TX(self):
        """
        Get the value of BYP_XBUF_TX
        """
        return self._readReg('CFG', 'BYP_XBUF_TX')

    @BYP_XBUF_TX.setter
    def BYP_XBUF_TX(self, value):
        """
        Set the value of BYP_XBUF_TX
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG', 'BYP_XBUF_TX', value)

    # EN_OUT2_XBUF_TX
    @property
    def EN_OUT2_XBUF_TX(self):
        """
        Get the value of EN_OUT2_XBUF_TX
        """
        return self._readReg('CFG', 'EN_OUT2_XBUF_TX')

    @EN_OUT2_XBUF_TX.setter
    def EN_OUT2_XBUF_TX(self, value):
        """
        Set the value of EN_OUT2_XBUF_TX
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG', 'EN_OUT2_XBUF_TX', value)

    # EN_TBUFIN_XBUF_RX
    @property
    def EN_TBUFIN_XBUF_RX(self):
        """
        Get the value of EN_TBUFIN_XBUF_RX
        """
        return self._readReg('CFG', 'EN_TBUFIN_XBUF_RX')

    @EN_TBUFIN_XBUF_RX.setter
    def EN_TBUFIN_XBUF_RX(self, value):
        """
        Set the value of EN_TBUFIN_XBUF_RX
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG', 'EN_TBUFIN_XBUF_RX', value)

    # PD_XBUF_RX
    @property
    def PD_XBUF_RX(self):
        """
        Get the value of PD_XBUF_RX
        """
        return self._readReg('CFG', 'PD_XBUF_RX')

    @PD_XBUF_RX.setter
    def PD_XBUF_RX(self, value):
        """
        Set the value of PD_XBUF_RX
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG', 'PD_XBUF_RX', value)

    # PD_XBUF_TX
    @property
    def PD_XBUF_TX(self):
        """
        Get the value of PD_XBUF_TX
        """
        return self._readReg('CFG', 'PD_XBUF_TX')

    @PD_XBUF_TX.setter
    def PD_XBUF_TX(self, value):
        """
        Set the value of PD_XBUF_TX
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG', 'PD_XBUF_TX', value)

    # EN_G_XBUF
    @property
    def EN_G_XBUF(self):
        """
        Get the value of EN_G_XBUF
        """
        return self._readReg('CFG', 'EN_G_XBUF')

    @EN_G_XBUF.setter
    def EN_G_XBUF(self, value):
        """
        Set the value of EN_G_XBUF
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG', 'EN_G_XBUF', value)
