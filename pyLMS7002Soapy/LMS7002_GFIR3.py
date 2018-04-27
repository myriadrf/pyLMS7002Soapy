#***************************************************************
#* Name:      LMS7002_GFIR3.py
#* Purpose:   Class implementing LMS7002 GFIR3 functions
#* Author:    Lime Microsystems ()
#* Created:   2016-11-14
#* Copyright: Lime Microsystems (limemicro.com)
#* License:
#**************************************************************

from LMS7002_base import *
from LMS7002_GFIR import *

class LMS7002_GFIR3(LMS7002_base):
    __slots__ = ['CMB0a', 'CMB0b', 'CMB0c','CMB1a','CMB1b','CMB1c', 'CMB2a', 'CMB2b', 'CMB2c', 'CMB3a', 'CMB3b', 'CMB3c', 'CMB4a', 'CMB4b', 'CMB4c', 'rxtx']    # Used to generate error on typos
    def __init__(self, chip, RxTx, Channel):
        if RxTx not in ['RX', 'TX']:
            raise ValueError("Parameter RxTx must be 'RX' or 'TX'")
        if Channel not in ['A', 'B']:
            raise ValueError("Parameter Channel must be 'A' or 'B'")
        self.chip = chip
        self.rxtx = RxTx
        self.channel = Channel

        self.CMB0a = LMS7002_GFIR(chip, RxTx, Channel, 3, '0a')
        self.CMB1a = LMS7002_GFIR(chip, RxTx, Channel, 3, '1a')
        self.CMB2a = LMS7002_GFIR(chip, RxTx, Channel, 3, '2a')
        self.CMB3a = LMS7002_GFIR(chip, RxTx, Channel, 3, '3a')
        self.CMB4a = LMS7002_GFIR(chip, RxTx, Channel, 3, '4a')

        self.CMB0b = LMS7002_GFIR(chip, RxTx, Channel, 3, '0b')
        self.CMB1b = LMS7002_GFIR(chip, RxTx, Channel, 3, '1b')
        self.CMB2b = LMS7002_GFIR(chip, RxTx, Channel, 3, '2b')
        self.CMB3b = LMS7002_GFIR(chip, RxTx, Channel, 3, '3b')
        self.CMB4b = LMS7002_GFIR(chip, RxTx, Channel, 3, '4b')

        self.CMB0c = LMS7002_GFIR(chip, RxTx, Channel, 3, '0c')
        self.CMB1c = LMS7002_GFIR(chip, RxTx, Channel, 3, '1c')
        self.CMB2c = LMS7002_GFIR(chip, RxTx, Channel, 3, '2c')
        self.CMB3c = LMS7002_GFIR(chip, RxTx, Channel, 3, '3c')
        self.CMB4c = LMS7002_GFIR(chip, RxTx, Channel, 3, '4c')

    def zeroOut(self):
        """
        Initialize all FIR coefficients to 0
        """
        for i in range(0, 8):
            self.CMB0a[i] = 0
            self.CMB1a[i] = 0
            self.CMB2a[i] = 0
            self.CMB3a[i] = 0
            self.CMB4a[i] = 0

            self.CMB0b[i] = 0
            self.CMB1b[i] = 0
            self.CMB2b[i] = 0
            self.CMB3b[i] = 0
            self.CMB4b[i] = 0

            self.CMB0c[i] = 0
            self.CMB1c[i] = 0
            self.CMB2c[i] = 0
            self.CMB3c[i] = 0
            self.CMB4c[i] = 0
            
            
    #
    # Operator overloading for easy access FIR[index]=val
    #        

    def __getitem__(self, key):
        """
        Get the FIR coefficient bank
        """
        if key not in [(0,'a'), (0, 'b'), (0, 'c'), 
                       (1,'a'), (1, 'b'), (1, 'c'), 
                       (2,'a'), (2, 'b'), (2, 'c'), 
                       (3,'a'), (3, 'b'), (3, 'c'), 
                       (4,'a'), (4, 'b'), (4, 'c')]:
            raise ValueError("Index must be in [(0,'a'), (0, 'b'), (0, 'c'), (1,'a'), (1, 'b'), (1, 'c'), (2,'a'), (2, 'b'), (2, 'c'), (3,'a'), (3, 'b'), (3, 'c'), (4,'a'), (4, 'b'), (4, 'c')")
        if key==(0,'a'):
            return self.CMB0a
        elif key==(1,'a'):
            return self.CMB1a
        elif key==(2,'a'):
            return self.CMB2a
        elif key==(3,'a'):
            return self.CMB3a
        elif key==(4,'a'):
            return self.CMB4a
        elif key==(0,'b'):
            return self.CMB0b
        elif key==(1,'b'):
            return self.CMB1b
        elif key==(2,'b'):
            return self.CMB2b
        elif key==(3,'b'):
            return self.CMB3b
        elif key==(4,'b'):
            return self.CMB4b
        elif key==(0,'c'):
            return self.CMB0c
        elif key==(1,'c'):
            return self.CMB1c
        elif key==(2,'c'):
            return self.CMB2c
        elif key==(3,'c'):
            return self.CMB3c
        else:
            return self.CMB4c


    #
    # Operator overloading for readable representation of FIR coefficients
    #

    def __str__(self):
        return self.__repr__()
        
    def __repr__(self):
        ret = self.rxtx+"GFIR3 Channel "+self.channel+"\n"

        for coef in [self.CMB0a, self.CMB1a, self.CMB2a, self.CMB3a, self.CMB4a,
                    self.CMB0b, self.CMB1b, self.CMB2b, self.CMB3b, self.CMB4b,
                    self.CMB0c, self.CMB1c, self.CMB2c, self.CMB3c, self.CMB4c]:
            tmp = "CMB"+coef.suffix+" = ["
            for i in range(0,8):
                tmp += self.intToHex(coef[i])+', '
            tmp = tmp[:-2] + "]\n"
            ret += tmp

        
        return ret
        
