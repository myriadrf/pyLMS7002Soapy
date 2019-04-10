# ***************************************************************
# * Name:      LMS7002_IO.py
# * Purpose:   Class implementing LMS7002 IO functions
# * Author:    Lime Microsystems ()
# * Created:   2016-11-14
# * Copyright: Lime Microsystems (limemicro.com)
# * License:
# **************************************************************

from pyLMS7002Soapy.LMS7002_base import LMS7002_base


class LMS7002_IO(LMS7002_base):
    __slots__ = []  # Used to generate error on typos

    def __init__(self, chip):
        self.chip = chip
        self.channel = None
        self.prefix = ""

    #
    # IOCFG0 (0x0021)
    #

    # TX_CLK_PE
    @property
    def TX_CLK_PE(self):
        """
        Get the value of TX_CLK_PE
        """
        return self._readReg('IOCFG0', 'TX_CLK_PE')

    @TX_CLK_PE.setter
    def TX_CLK_PE(self, value):
        """
        Set the value of TX_CLK_PE
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('IOCFG0', 'TX_CLK_PE', value)

    # RX_CLK_PE
    @property
    def RX_CLK_PE(self):
        """
        Get the value of RX_CLK_PE
        """
        return self._readReg('IOCFG0', 'RX_CLK_PE')

    @RX_CLK_PE.setter
    def RX_CLK_PE(self, value):
        """
        Set the value of RX_CLK_PE
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('IOCFG0', 'RX_CLK_PE', value)

    # SDA_PE
    @property
    def SDA_PE(self):
        """
        Get the value of SDA_PE
        """
        return self._readReg('IOCFG0', 'SDA_PE')

    @SDA_PE.setter
    def SDA_PE(self, value):
        """
        Set the value of SDA_PE
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('IOCFG0', 'SDA_PE', value)

    # SDA_DS
    @property
    def SDA_DS(self):
        """
        Get the value of SDA_DS
        """
        return self._readReg('IOCFG0', 'SDA_DS')

    @SDA_DS.setter
    def SDA_DS(self, value):
        """
        Set the value of SDA_DS
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('IOCFG0', 'SDA_DS', value)

    # SCL_PE
    @property
    def SCL_PE(self):
        """
        Get the value of SCL_PE
        """
        return self._readReg('IOCFG0', 'SCL_PE')

    @SCL_PE.setter
    def SCL_PE(self, value):
        """
        Set the value of SCL_PE
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('IOCFG0', 'SCL_PE', value)

    # SCL_DS
    @property
    def SCL_DS(self):
        """
        Get the value of SCL_DS
        """
        return self._readReg('IOCFG0', 'SCL_DS')

    @SCL_DS.setter
    def SCL_DS(self, value):
        """
        Set the value of SCL_DS
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('IOCFG0', 'SCL_DS', value)

    # SDIO_DS
    @property
    def SDIO_DS(self):
        """
        Get the value of SDIO_DS
        """
        return self._readReg('IOCFG0', 'SDIO_DS')

    @SDIO_DS.setter
    def SDIO_DS(self, value):
        """
        Set the value of SDIO_DS
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('IOCFG0', 'SDIO_DS', value)

    # SDIO_PE
    @property
    def SDIO_PE(self):
        """
        Get the value of SDIO_PE
        """
        return self._readReg('IOCFG0', 'SDIO_PE')

    @SDIO_PE.setter
    def SDIO_PE(self, value):
        """
        Set the value of SDIO_PE
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('IOCFG0', 'SDIO_PE', value)

    # SDO_PE
    @property
    def SDO_PE(self):
        """
        Get the value of SDO_PE
        """
        return self._readReg('IOCFG0', 'SDO_PE')

    @SDO_PE.setter
    def SDO_PE(self, value):
        """
        Set the value of SDO_PE
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('IOCFG0', 'SDO_PE', value)

    # SCLK_PE
    @property
    def SCLK_PE(self):
        """
        Get the value of SCLK_PE
        """
        return self._readReg('IOCFG0', 'SCLK_PE')

    @SCLK_PE.setter
    def SCLK_PE(self, value):
        """
        Set the value of SCLK_PE
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('IOCFG0', 'SCLK_PE', value)

    # SEN_PE
    @property
    def SEN_PE(self):
        """
        Get the value of SEN_PE
        """
        return self._readReg('IOCFG0', 'SEN_PE')

    @SEN_PE.setter
    def SEN_PE(self, value):
        """
        Set the value of SEN_PE
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('IOCFG0', 'SEN_PE', value)

    # SPIMODE
    @property
    def SPIMODE(self):
        """
        Get the value of SPIMODE
        """
        return self._readReg('IOCFG0', 'SPIMODE')

    @SPIMODE.setter
    def SPIMODE(self, value):
        """
        Set the value of SPIMODE
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('IOCFG0', 'SPIMODE', value)

    #
    # IOCFG1 (0x0022)
    #

    # LML2_TRXIQPULSE
    @property
    def LML2_TRXIQPULSE(self):
        """
        Get the value of LML2_TRXIQPULSE
        """
        if self.chip.chipID == self.chip.chipIDMR3:
            return self._readReg('IOCFG1', 'LML2_TRXIQPULSE')
        else:
            raise ValueError("Bitfield LML2_TRXIQPULSE is not supported on chip version " + str(self.chip.chipID))

    @LML2_TRXIQPULSE.setter
    def LML2_TRXIQPULSE(self, value):
        """
        Set the value of LML2_TRXIQPULSE
        """
        if self.chip.chipID == self.chip.chipIDMR3:
            if value not in [0, 1]:
                raise ValueError("Value must be [0,1]")
            self._writeReg('IOCFG1', 'LML2_TRXIQPULSE', value)
        else:
            raise ValueError("Bitfield LML2_TRXIQPULSE is not supported on chip version " + str(self.chip.chipID))

    # LML2_SISODDR
    @property
    def LML2_SISODDR(self):
        """
        Get the value of LML2_SISODDR
        """
        if self.chip.chipID == self.chip.chipIDMR3:
            return self._readReg('IOCFG1', 'LML2_SISODDR')
        else:
            raise ValueError("Bitfield LML2_SISODDR is not supported on chip version " + str(self.chip.chipID))

    @LML2_SISODDR.setter
    def LML2_SISODDR(self, value):
        """
        Set the value of LML2_SISODDR
        """
        if self.chip.chipID == self.chip.chipIDMR3:
            if value not in [0, 1]:
                raise ValueError("Value must be [0,1]")
            self._writeReg('IOCFG1', 'LML2_SISODDR', value)
        else:
            raise ValueError("Bitfield LML2_SISODDR is not supported on chip version " + str(self.chip.chipID))

    # LML1_TRXIQPULSE
    @property
    def LML1_TRXIQPULSE(self):
        """
        Get the value of LML1_TRXIQPULSE
        """
        if self.chip.chipID == self.chip.chipIDMR3:
            return self._readReg('IOCFG1', 'LML1_TRXIQPULSE')
        else:
            raise ValueError("Bitfield LML1_TRXIQPULSE is not supported on chip version " + str(self.chip.chipID))

    @LML1_TRXIQPULSE.setter
    def LML1_TRXIQPULSE(self, value):
        """
        Set the value of LML1_TRXIQPULSE
        """
        if self.chip.chipID == self.chip.chipIDMR3:
            if value not in [0, 1]:
                raise ValueError("Value must be [0,1]")
            self._writeReg('IOCFG1', 'LML1_TRXIQPULSE', value)
        else:
            raise ValueError("Bitfield LML1_TRXIQPULSE is not supported on chip version " + str(self.chip.chipID))

    # LML1_SISODDR
    @property
    def LML1_SISODDR(self):
        """
        Get the value of LML1_SISODDR
        """
        if self.chip.chipID == self.chip.chipIDMR3:
            return self._readReg('IOCFG1', 'LML1_SISODDR')
        else:
            raise ValueError("Bitfield LML1_SISODDR is not supported on chip version " + str(self.chip.chipID))

    @LML1_SISODDR.setter
    def LML1_SISODDR(self, value):
        """
        Set the value of LML1_SISODDR
        """
        if self.chip.chipID == self.chip.chipIDMR3:
            if value not in [0, 1]:
                raise ValueError("Value must be [0,1]")
            self._writeReg('IOCFG1', 'LML1_SISODDR', value)
        else:
            raise ValueError("Bitfield LML1_SISODDR is not supported on chip version " + str(self.chip.chipID))

    # DIQ2_DS
    @property
    def DIQ2_DS(self):
        """
        Get the value of DIQ2_DS
        """
        return self._readReg('IOCFG1', 'DIQ2_DS')

    @DIQ2_DS.setter
    def DIQ2_DS(self, value):
        """
        Set the value of DIQ2_DS
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('IOCFG1', 'DIQ2_DS', value)

    # DIQ2_PE
    @property
    def DIQ2_PE(self):
        """
        Get the value of DIQ2_PE
        """
        return self._readReg('IOCFG1', 'DIQ2_PE')

    @DIQ2_PE.setter
    def DIQ2_PE(self, value):
        """
        Set the value of DIQ2_PE
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('IOCFG1', 'DIQ2_PE', value)

    # IQ_SEL_EN_2_PE
    @property
    def IQ_SEL_EN_2_PE(self):
        """
        Get the value of IQ_SEL_EN_2_PE
        """
        return self._readReg('IOCFG1', 'IQ_SEL_EN_2_PE')

    @IQ_SEL_EN_2_PE.setter
    def IQ_SEL_EN_2_PE(self, value):
        """
        Set the value of IQ_SEL_EN_2_PE
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('IOCFG1', 'IQ_SEL_EN_2_PE', value)

    # TXNRX2_PE
    @property
    def TXNRX2_PE(self):
        """
        Get the value of TXNRX2_PE
        """
        return self._readReg('IOCFG1', 'TXNRX2_PE')

    @TXNRX2_PE.setter
    def TXNRX2_PE(self, value):
        """
        Set the value of TXNRX2_PE
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('IOCFG1', 'TXNRX2_PE', value)

    # FCLK2_PE
    @property
    def FCLK2_PE(self):
        """
        Get the value of FCLK2_PE
        """
        return self._readReg('IOCFG1', 'FCLK2_PE')

    @FCLK2_PE.setter
    def FCLK2_PE(self, value):
        """
        Set the value of FCLK2_PE
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('IOCFG1', 'FCLK2_PE', value)

    # MCLK2_PE
    @property
    def MCLK2_PE(self):
        """
        Get the value of MCLK2_PE
        """
        return self._readReg('IOCFG1', 'MCLK2_PE')

    @MCLK2_PE.setter
    def MCLK2_PE(self, value):
        """
        Set the value of MCLK2_PE
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('IOCFG1', 'MCLK2_PE', value)

    # DIQ1_DS
    @property
    def DIQ1_DS(self):
        """
        Get the value of DIQ1_DS
        """
        return self._readReg('IOCFG1', 'DIQ1_DS')

    @DIQ1_DS.setter
    def DIQ1_DS(self, value):
        """
        Set the value of DIQ1_DS
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('IOCFG1', 'DIQ1_DS', value)

    # DIQ1_PE
    @property
    def DIQ1_PE(self):
        """
        Get the value of DIQ1_PE
        """
        return self._readReg('IOCFG1', 'DIQ1_PE')

    @DIQ1_PE.setter
    def DIQ1_PE(self, value):
        """
        Set the value of DIQ1_PE
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('IOCFG1', 'DIQ1_PE', value)

    # IQ_SEL_EN_1_PE
    @property
    def IQ_SEL_EN_1_PE(self):
        """
        Get the value of IQ_SEL_EN_1_PE
        """
        return self._readReg('IOCFG1', 'IQ_SEL_EN_1_PE')

    @IQ_SEL_EN_1_PE.setter
    def IQ_SEL_EN_1_PE(self, value):
        """
        Set the value of IQ_SEL_EN_1_PE
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('IOCFG1', 'IQ_SEL_EN_1_PE', value)

    # TXNRX1_PE
    @property
    def TXNRX1_PE(self):
        """
        Get the value of TXNRX1_PE
        """
        return self._readReg('IOCFG1', 'TXNRX1_PE')

    @TXNRX1_PE.setter
    def TXNRX1_PE(self, value):
        """
        Set the value of TXNRX1_PE
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('IOCFG1', 'TXNRX1_PE', value)

    # FCLK1_PE
    @property
    def FCLK1_PE(self):
        """
        Get the value of FCLK1_PE
        """
        return self._readReg('IOCFG1', 'FCLK1_PE')

    @FCLK1_PE.setter
    def FCLK1_PE(self, value):
        """
        Set the value of FCLK1_PE
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('IOCFG1', 'FCLK1_PE', value)

    # MCLK1_PE
    @property
    def MCLK1_PE(self):
        """
        Get the value of MCLK1_PE
        """
        return self._readReg('IOCFG1', 'MCLK1_PE')

    @MCLK1_PE.setter
    def MCLK1_PE(self, value):
        """
        Set the value of MCLK1_PE
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('IOCFG1', 'MCLK1_PE', value)
