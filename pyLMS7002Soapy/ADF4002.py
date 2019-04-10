# ***************************************************************
# * Name:      ADF4002.py
# * Purpose:   Class implementing ADF4002 functions
# * Author:    Lime Microsystems ()
# * Created:   2016-11-14
# * Copyright: Lime Microsystems (limemicro.com)
# * License:
# **************************************************************


class ADF4002(object):

    def __init__(self, programmingFn):
        """
        Initialize ADF4002.
        The initialization function turns off ADF4002
        """
        self.programmingFn = programmingFn

        self._fRef = 10
        self._fVCO = 30.72

        # Reference counter latch bits
        self._LDP = 0
        self._ABP = 0
        self._R = 125

        # N counter latch bits
        self._CPG = 0
        self._N = 384

        # Function latch bits
        self._PD2f = 0
        self._CS2f = 7
        self._CS1f = 7
        self._TCf = 0
        self._FLf = 0
        self._CPSf = 1
        self._PDPf = 1
        self._MOCf = 0
        self._PD1f = 0
        self._CRf = 1

        # Initialization latch bits
        self._PD2i = 0
        self._CS2i = 7
        self._CS1i = 7
        self._TCi = 0
        self._FLi = 0
        self._CPSi = 1
        self._PDPi = 1
        self._MOCi = 0
        self._PD1i = 0
        self._CRi = 1

        self.update()  # Upload values to ADF4002

    #
    # ADF4002 functions
    #

    def enable(self):
        # Enable counters, charge pump
        self.CRf = 0
        self.CRi = 0
        self.CPSf = 0
        self.CPSi = 0
        self.MOCi = 1
        self.MOCf = 1
        self.update()

    def disable(self):
        # Hold counters in reset, set charge pump output to three-state
        self.CRf = 1
        self.CRi = 1
        self.CPSf = 1
        self.CPSi = 1
        self.MOCi = 0
        self.MOCf = 0
        self.update()

    # fRef
    @property
    def fRef(self):
        """
        Get the value of fRef
        """
        return self._fRef

    @fRef.setter
    def fRef(self, value):
        """
        Set the value of fRef
        """
        if not (1 <= value <= 100):
            raise ValueError("Value is out of range (1,100). Frequency is in MHz.")
        self._fRef = value
        self.update()

    # fVCO
    @property
    def fVCO(self):
        """
        Get the value of fVCO
        """
        return self._fVCO

    @fVCO.setter
    def fVCO(self, value):
        """
        Set the value of fVCO
        """
        if not (1 <= value <= 100):
            raise ValueError("Value is out of range (1,100). Frequency is in MHz.")
        self._fVCO = value
        self.update()

    def update(self):
        self.calculateRN()
        data = self.getProgrammingValues()
        self.programmingFn(data)

    def getProgrammingValues(self):
        iniLatch = self.getInitializationLatchValue()
        fnLatch = self.getFunctionLatchValue()
        nCnt = self.getNCounterLatchValue()
        rCnt = self.getReferenceLatchValue()
        return [iniLatch, fnLatch, rCnt, nCnt]

    def calculateRN(self):
        x = self.fRef * 1e6
        y = self.fVCO * 1e6
        while (x > 0) and (y > 0):
            if x >= y:
                x = x % y
            else:
                y = y % x
        fComp = (x + y) / 1e6
        R = int((self.fRef / fComp) + 0.5)
        N = int((self.fVCO / fComp) + 0.5)
        self.R = R
        self.N = N

    #
    # Reference counter latch
    #

    # LDP
    @property
    def LDP(self):
        """
        Get the value of LDP
        """
        return self._LDP

    @LDP.setter
    def LDP(self, value):
        """
        Set the value of LDP
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._LDP = value

    # ABP
    @property
    def ABP(self):
        """
        Get the value of ABP
        """
        return self._ABP

    @ABP.setter
    def ABP(self, value):
        """
        Set the value of ABP
        """
        if value not in [0, 2, 3]:
            raise ValueError("Value must be [0, 2, 3]")
        self._ABP = value

    # R
    @property
    def R(self):
        """
        Get the value of R
        """
        return self._R

    @R.setter
    def R(self, value):
        """
        Set the value of R
        """
        if not (1 <= value <= 16383):
            raise ValueError("Value must be [1, 16383]")
        self._R = value

    #
    # N counter latch
    #

    # CPG
    @property
    def CPG(self):
        """
        Get the value of CPG
        """
        return self._CPG

    @CPG.setter
    def CPG(self, value):
        """
        Set the value of CPG
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._CPG = value

    # N
    @property
    def N(self):
        """
        Get the value of N
        """
        return self._N

    @N.setter
    def N(self, value):
        """
        Set the value of N
        """
        if not (1 <= value <= 8191):
            raise ValueError("Value must be [1, 8191]")
        self._N = value

    #
    # Function latch
    #

    # PD2f
    @property
    def PD2f(self):
        """
        Get the value of PD2f
        """
        return self._PD2f

    @PD2f.setter
    def PD2f(self, value):
        """
        Set the value of PD2f
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._PD2f = value

    # CS2f
    @property
    def CS2f(self):
        """
        Get the value of CS2f
        """
        return self._CS2f

    @CS2f.setter
    def CS2f(self, value):
        """
        Set the value of CS2f
        """
        if not (0 <= value <= 7):
            raise ValueError("Value must be [0,7]")
        self._CS2f = value

    # CS1f
    @property
    def CS1f(self):
        """
        Get the value of CS1f
        """
        return self._CS1f

    @CS1f.setter
    def CS1f(self, value):
        """
        Set the value of CS1f
        """
        if not (0 <= value <= 7):
            raise ValueError("Value must be [0,7]")
        self._CS1f = value

        # TCf

    @property
    def TCf(self):
        """
        Get the value of TCf
        """
        return self._TCf

    @TCf.setter
    def TCf(self, value):
        """
        Set the value of TCf
        """
        if not (0 <= value <= 15):
            raise ValueError("Value must be [0,15]")
        self._TCf = value

        # FLf

    @property
    def FLf(self):
        """
        Get the value of FLf
        """
        return self._FLf

    @FLf.setter
    def FLf(self, value):
        """
        Set the value of FLf
        """
        if not (0 <= value <= 3):
            raise ValueError("Value must be [0,3]")
        self._FLf = value

        # CPSf

    @property
    def CPSf(self):
        """
        Get the value of CPSf
        """
        return self._CPSf

    @CPSf.setter
    def CPSf(self, value):
        """
        Set the value of CPSf
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._CPSf = value

    # PDPf
    @property
    def PDPf(self):
        """
        Get the value of PDPf
        """
        return self._PDPf

    @PDPf.setter
    def PDPf(self, value):
        """
        Set the value of PDPf
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._PDPf = value

    # MOCf
    @property
    def MOCf(self):
        """
        Get the value of MOCf
        """
        return self._MOCf

    @MOCf.setter
    def MOCf(self, value):
        """
        Set the value of MOCf
        """
        if not (0 <= value <= 7):
            raise ValueError("Value must be [0,7]")
        self._MOCf = value

        # PD1f

    @property
    def PD1f(self):
        """
        Get the value of PD1f
        """
        return self._PD1f

    @PD1f.setter
    def PD1f(self, value):
        """
        Set the value of PD1f
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._PD1f = value

    # CRf
    @property
    def CRf(self):
        """
        Get the value of CRf
        """
        return self._CRf

    @CRf.setter
    def CRf(self, value):
        """
        Set the value of CRf
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._CRf = value

    #
    # Initialization latch
    #

    # PD2i
    @property
    def PD2i(self):
        """
        Get the value of PD2i
        """
        return self._PD2i

    @PD2i.setter
    def PD2i(self, value):
        """
        Set the value of PD2i
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._PD2i = value

    # CS2i
    @property
    def CS2i(self):
        """
        Get the value of CS2i
        """
        return self._CS2i

    @CS2i.setter
    def CS2i(self, value):
        """
        Set the value of CS2i
        """
        if not (0 <= value <= 7):
            raise ValueError("Value must be [0,7]")
        self._CS2i = value

    # CS1i
    @property
    def CS1i(self):
        """
        Get the value of CS1i
        """
        return self._CS1i

    @CS1i.setter
    def CS1i(self, value):
        """
        Set the value of CS1i
        """
        if not (0 <= value <= 7):
            raise ValueError("Value must be [0,7]")
        self._CS1i = value

        # TCi

    @property
    def TCi(self):
        """
        Get the value of TCi
        """
        return self._TCi

    @TCi.setter
    def TCi(self, value):
        """
        Set the value of TCi
        """
        if not (0 <= value <= 15):
            raise ValueError("Value must be [0,15]")
        self._TCi = value

        # FLi

    @property
    def FLi(self):
        """
        Get the value of FLi
        """
        return self._FLi

    @FLi.setter
    def FLi(self, value):
        """
        Set the value of FLi
        """
        if not (0 <= value <= 3):
            raise ValueError("Value must be [0,3]")
        self._FLi = value

        # CPSi

    @property
    def CPSi(self):
        """
        Get the value of CPSi
        """
        return self._CPSi

    @CPSi.setter
    def CPSi(self, value):
        """
        Set the value of CPSi
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._CPSi = value

    # PDPi
    @property
    def PDPi(self):
        """
        Get the value of PDPi
        """
        return self._PDPi

    @PDPi.setter
    def PDPi(self, value):
        """
        Set the value of PDPi
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._PDPi = value

    # MOCi
    @property
    def MOCi(self):
        """
        Get the value of MOCi
        """
        return self._MOCi

    @MOCi.setter
    def MOCi(self, value):
        """
        Set the value of MOCi
        """
        if not (0 <= value <= 7):
            raise ValueError("Value must be [0,7]")
        self._MOCi = value

        # PD1i

    @property
    def PD1i(self):
        """
        Get the value of PD1i
        """
        return self._PD1i

    @PD1i.setter
    def PD1i(self, value):
        """
        Set the value of PD1i
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._PD1i = value

    # CRi
    @property
    def CRi(self):
        """
        Get the value of CRi
        """
        return self._CRi

    @CRi.setter
    def CRi(self, value):
        """
        Set the value of CRi
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._CRi = value

    def getReferenceLatchValue(self):
        val = 0
        val += self._R << 2
        val += self._ABP << 16
        val += self._LDP << 20
        return val

    def getNCounterLatchValue(self):
        val = 1
        val += self._CPG << 21
        val += self._N << 8
        return val

    def getFunctionLatchValue(self):
        val = 2
        val += self._PD2f << 21
        val += self._CS2f << 18
        val += self._CS1f << 15
        val += self._TCf << 11
        val += self._FLf << 9
        val += self._CPSf << 8
        val += self._PDPf << 7
        val += self._MOCf << 4
        val += self._PD1f << 3
        val += self._CRf << 2
        return val

    def getInitializationLatchValue(self):
        val = 3
        val += self._PD2i << 21
        val += self._CS2i << 18
        val += self._CS1i << 15
        val += self._TCi << 11
        val += self._FLi << 9
        val += self._CPSi << 8
        val += self._PDPi << 7
        val += self._MOCi << 4
        val += self._PD1i << 3
        val += self._CRi << 2
        return val
