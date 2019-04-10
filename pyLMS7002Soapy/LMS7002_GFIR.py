# ***************************************************************
# * Name:      LMS7002_GFIR.py
# * Purpose:   Class implementing LMS7002 GFIR functions
# * Author:    Lime Microsystems ()
# * Created:   2016-11-14
# * Copyright: Lime Microsystems (limemicro.com)
# * License:
# **************************************************************

from pyLMS7002Soapy.LMS7002_base import LMS7002_base


class LMS7002_GFIR(LMS7002_base):
    __slots__ = ['rxtx', 'nFIR', 'suffix']  # Used to generate error on typos

    def __init__(self, chip, RxTx, Channel, nFIR, suffix):
        if RxTx not in ['RX', 'TX']:
            raise ValueError("Parameter RxTx must be 'RX' or 'TX'")
        if Channel not in ['A', 'B']:
            raise ValueError("Parameter Channel must be 'A' or 'B'")
        self.chip = chip
        self.rxtx = RxTx
        self.channel = Channel
        self.nFIR = nFIR
        self.prefix = self.rxtx + str(nFIR) + "CMB" + suffix + "_"
        self.suffix = suffix

    #
    # Operator overloading for easy access FIR[index]=val
    #

    def __getitem__(self, key):
        """
        Get the FIR coefficient
        """
        if key not in range(0, 8):
            raise ValueError("Index must be in [0..7]. Given " + str(key))
        return self._readReg(str(key), 'COEFF<15:0>')

    def __setitem__(self, key, val):
        """
        Set the FIR coefficient
        """
        if not (0 <= val <= 65535):
            raise ValueError("Value must be in [0..65535]")
        if key not in range(0, 8):
            raise ValueError("Index must be in [0..7]")
        self._writeReg(str(key), 'COEFF<15:0>', val)

    #
    # Operator overloading for readable representation of FIR coefficients
    #

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        prevMAC = self.chip.MAC  # save the value of MAC
        self.chip.MAC = self.chip.getMACfromName(self.channel)  # set MAC to reduce the number SPI accesses
        ret = "GFIR" + str(self.nFIR) + "[" + self.suffix + "] " + self.rxtx + " " + self.channel + "\n"
        tmp = "Coeff = ["
        for i in range(0, 8):
            tmp += self.intToHex(self[i]) + ", "
        ret += tmp[:-2] + "]\n"
        self.chip.MAC = prevMAC  # restore previous value of MAC
        return ret[:-1]
