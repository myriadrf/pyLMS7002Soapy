# ***************************************************************
# * Name:      LMS7002_GFIR2.py
# * Purpose:   Class implementing LMS7002 GFIR2 functions
# * Author:    Lime Microsystems ()
# * Created:   2016-11-14
# * Copyright: Lime Microsystems (limemicro.com)
# * License:
# **************************************************************

from pyLMS7002Soapy.LMS7002_base import LMS7002_base
from pyLMS7002Soapy.LMS7002_GFIR import LMS7002_GFIR


class LMS7002_GFIR2(LMS7002_base):
    __slots__ = ['CMB0', 'CMB1', 'CMB2', 'CMB3', 'CMB4', 'rxtx']  # Used to generate error on typos

    def __init__(self, chip, RxTx, Channel):
        if RxTx not in ['RX', 'TX']:
            raise ValueError("Parameter RxTx must be 'RX' or 'TX'")
        if Channel not in ['A', 'B']:
            raise ValueError("Parameter Channel must be 'A' or 'B'")
        self.chip = chip
        self.rxtx = RxTx
        self.channel = Channel

        self.CMB0 = LMS7002_GFIR(chip, RxTx, Channel, 2, '0')
        self.CMB1 = LMS7002_GFIR(chip, RxTx, Channel, 2, '1')
        self.CMB2 = LMS7002_GFIR(chip, RxTx, Channel, 2, '2')
        self.CMB3 = LMS7002_GFIR(chip, RxTx, Channel, 2, '3')
        self.CMB4 = LMS7002_GFIR(chip, RxTx, Channel, 2, '4')

    def zeroOut(self):
        """
        Initialize all FIR coefficients to 0
        """
        for i in range(0, 8):
            self.CMB0[i] = 0
            self.CMB1[i] = 0
            self.CMB2[i] = 0
            self.CMB3[i] = 0
            self.CMB4[i] = 0
            #

    # Operator overloading for easy access FIR[index]=val
    #

    def __getitem__(self, key):
        """
        Get the FIR coefficient bank
        """
        if key not in range(0, 5):
            raise ValueError("Index must be in [0..4]")
        if key == 0:
            return self.CMB0
        elif key == 1:
            return self.CMB1
        elif key == 2:
            return self.CMB2
        elif key == 3:
            return self.CMB3
        else:
            return self.CMB4

    #
    # Operator overloading for readable representation of FIR coefficients
    #

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        ret = self.rxtx + "GFIR2 Channel " + self.channel + "\n"

        coef = self.CMB0
        tmp = "CMB0 = ["
        for i in range(0, 8):
            tmp += self.intToHex(coef[i]) + ', '
        tmp = tmp[:-2] + "]\n"
        ret += tmp

        coef = self.CMB1
        tmp = "CMB1 = ["
        for i in range(0, 8):
            tmp += self.intToHex(coef[i]) + ', '
        tmp = tmp[:-2] + "]\n"
        ret += tmp

        coef = self.CMB2
        tmp = "CMB2 = ["
        for i in range(0, 8):
            tmp += self.intToHex(coef[i]) + ', '
        tmp = tmp[:-2] + "]\n"
        ret += tmp

        coef = self.CMB3
        tmp = "CMB3 = ["
        for i in range(0, 8):
            tmp += self.intToHex(coef[i]) + ', '
        tmp = tmp[:-2] + "]\n"
        ret += tmp

        coef = self.CMB4
        tmp = "CMB4 = ["
        for i in range(0, 8):
            tmp += self.intToHex(coef[i]) + ', '
        tmp = tmp[:-2] + "]\n"
        ret += tmp

        return ret
