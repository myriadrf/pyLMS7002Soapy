# ***************************************************************
# * Name:      LMS7002_base.py
# * Purpose:   Class implementing LMS7002 base functions
# * Author:    Lime Microsystems ()
# * Created:   2016-11-14
# * Copyright: Lime Microsystems (limemicro.com)
# * License:
# **************************************************************


class LMS7002_base(object):
    __slots__ = ['channel', 'chip', 'prefix']

    #
    # Auxiliary functions
    #

    def _readReg(self, regName, fieldName):
        if self.channel is not None:
            prevMAC = self.chip.MAC  # save the value of MAC
            mac = self.chip.getMACfromName(self.channel)
            if mac != prevMAC:  # try to reduce the number of SPI accesses
                self.chip.MAC = mac
        regName = self.prefix + regName
        reg = self.chip[regName]
        val = reg[fieldName]
        if self.channel is not None:
            if mac != prevMAC:  # try to reduce the number of SPI accesses
                self.chip.MAC = prevMAC  # restore previous value of MAC
        return val

    def _writeReg(self, regName, fieldName, value):
        if self.channel is not None:
            prevMAC = self.chip.MAC  # save the value of MAC
            mac = self.chip.getMACfromName(self.channel)
            if mac != prevMAC:  # try to reduce the number of SPI accesses
                self.chip.MAC = mac
        regName = self.prefix + regName
        reg = self.chip[regName]
        reg[fieldName] = value
        if self.channel is not None:
            if mac != prevMAC:  # try to reduce the number of SPI accesses
                self.chip.MAC = prevMAC  # restore previous value of MAC

    @staticmethod
    def intToHex(val, upperCase=True):
        hexVal = hex(val)[2:]
        while len(hexVal) < 4:
            hexVal = "0" + hexVal
        if upperCase:
            hexVal = hexVal.upper()
        hexVal = "0x" + hexVal
        return hexVal

    @staticmethod
    def intTo2sComplement(val, nbits):
        """
        Convert integer to 2s complement representation
        """
        if val < 0:
            tmp = abs(val)
            tmp = ~tmp
            tmp += 1
            mask = (2 ** nbits) - 1
            return tmp & mask
        else:
            return val

    @staticmethod
    def twosComplementToInt(val, nbits):
        """
        Convert 2s complement representation to int
        """
        if val > 2 ** (nbits - 1):
            return -(2 ** nbits) + val
        else:
            return val

    @staticmethod
    def intToSignMagnitude(val, nbits):
        """
        Convert integer to sign-magnitude representation
        """
        if val < 0:
            sign = 1
        else:
            sign = 0
        ret = abs(val) & (2 ** (nbits - 1) - 1)
        ret += sign << (nbits - 1)
        return ret

    @staticmethod
    def signMagnitudeToInt(val, nbits):
        """
        Convert sign-magnitude representation to integer
        """
        ret = val & (2 ** (nbits - 1) - 1)
        if val & (1 << (nbits - 1)) != 0:
            sign = -1
        else:
            sign = 1
        return ret * sign
