# ***************************************************************
# * Name:      LMS7002_regDataStructs.py
# * Purpose:   Class for handling register file definitions
# * Author:    Lime Microsystems ()
# * Created:   2016-11-14
# * Copyright: Lime Microsystems (limemicro.com)
# * License:
# **************************************************************

import math
import warnings
from copy import copy
from copy import deepcopy

regDataStructsVer = "1.6a"


class RegBank(object):
    def __init__(self, name, specifier, nRegisterSets=1):
        self.name = name
        self.specifier = specifier
        self.nRegisterSets = nRegisterSets
        self.registers = []

        # Find don't care positions
        pos = 0
        while (specifier[len(specifier) - (pos + 1)]) == "X":
            pos = pos + 1

        if pos == 0:
            if "X" not in specifier:
                raise ValueError("Bank specifier " + specifier + " is a fixed address!")
            else:
                raise ValueError(
                    "Bank specifier can only have X for lowest bits. Specifier " + specifier + "violates this "
                                                                                               "constraint.")

        if "X" in specifier[0:-pos]:
            raise ValueError(
                "Bank specifier can only have X for lowest bits. Specifier " + specifier + " violates this constraint.")

        strLow = specifier[0:-pos] + "0" * int(pos)
        if "0x" in specifier:
            # Hexadecimal notation
            strHigh = specifier[0:-pos] + "F" * int(pos)
            self.addrL = int(strLow, 16)
            self.addrH = int(strHigh, 16)
        elif "0b" in specifier:
            # Binary notation
            strHigh = specifier[0:-pos] + "1" * int(pos)
            self.addrL = int(strLow, 2)
            self.addrH = int(strHigh, 2)
        else:
            raise ValueError("Invalid bank specifier : " + specifier)

    def getNRegisterSets(self):
        return self.nRegisterSets

    def __repr__(self):
        retVal = "REGBANK " + self.getName() + " " + self.getSpecifier() + " " + str(self.nRegisterSets) + "\n"
        return retVal

    def __str__(self):
        retVal = "Register bank : " + self.name + " " + self.specifier + " (" + hex(self.getAddrH()) + "," + hex(
            self.getAddrL()) + ") N=" + str(self.nRegisterSets) + "\n"
        regs = ""
        for reg in self.registers:
            if regs != "":
                regs = regs + ", " + reg.name
            else:
                regs = reg.name
        retVal = retVal + "Registers=[" + regs + "]"
        return retVal

    def getName(self):
        return self.name

    def getSpecifier(self):
        return self.specifier

    def getAddrL(self):
        # Returns the lowest address in bank
        return self.addrL

    def getAddrH(self):
        # Returns the highest address in bank
        return self.addrH

    def isInBank(self, addr):
        # Check if address is in this bank range
        if (addr >= self.addrL) and (addr <= self.addrH):
            return True
        return False

    def addRegister(self, register):
        # Check if register is in register bank address range
        if not self.isInBank(register.addr):
            raise ValueError(
                "Register with address " + hex(register.addr) + " cannot be added to bank " + self.name + " (" + hex(
                    self.getAddrH()) + "," + hex(self.getAddrL()) + ")")

        # Check if register collides with existing one
        for reg in self.registers:
            if reg.addr == register.addr:
                raise ValueError("Register " + reg.name + " is assigned to the address taken by " + register.name)
        self.registers.append(register)

    def getRegister(self, regName):
        # Get register by name
        for reg in self.registers:
            if regName == reg.name:
                return reg
        raise ValueError("Register " + regName + " does not exist in bank " + self.name)

    def hasRegister(self, regName):
        # Check if register exists in a register bank
        for reg in self.registers:
            if regName == reg.name:
                return True
        return False

    def getRegs(self):
        # Get all registers in a bank
        return self.registers

    def getSpecNBits(self):
        addrH = self.getAddrH()
        addrL = self.getAddrL()
        regAddrSpace = addrH - addrL + 1  # Size of register address space in register bank
        nBitsRegAddrSpace = int(math.log(regAddrSpace) / math.log(2))
        return int(15 - nBitsRegAddrSpace)

    def getSpecBits(self):
        nBits = self.getSpecNBits()
        bits = bin(self.getAddrL())  # bits contain 0b prefix
        bits = bits[2:]  # get rid of 0b
        # Make sure that bits has 15 digits
        while len(bits) < 15:
            bits = "0" + bits
        return bits[0:nBits]


class Register(object):
    @staticmethod
    def intToHex(val, upperCase=True):
        hexVal = hex(val)[2:]
        while len(hexVal) < 4:
            hexVal = "0" + hexVal
        if upperCase:
            hexVal = hexVal.upper()
        hexVal = "0x" + hexVal
        return hexVal

    # Instance methods
    def __init__(self, regName, regAddr, chip=None):
        if " " in regName:
            raise ValueError("Invalid register name: " + regName + " (name contains space)")
        self.regAddr = regAddr
        self.name = regName
        if "0x" in regAddr:
            addr = int(regAddr, 16)
        elif "0b" in regAddr:
            addr = int(regAddr, 2)
        else:
            raise ValueError("Invalid register address " + str(regAddr))

        self.addr = addr
        self.comment = []
        self.bitFields = []
        self._chip = chip
        self.nSets = 1

    def makeBitFieldCopies(self, nCopies):
        self.nSets = nCopies
        bitFields = self.bitFields
        self.bitFields = []
        for i in range(0, nCopies):
            tmp = []
            for field in bitFields:
                tmp.append(deepcopy(field))
            self.bitFields.append(tmp)

    @property
    def chip(self):
        return self._chip

    @chip.setter
    def chip(self, val):
        self._chip = val

    @property
    def SPIwriteFn(self):
        return self.chip.SPIwriteFn

    @property
    def SPIreadFn(self):
        return self.chip.SPIreadFn

    @property
    def SPIImmediate(self):
        return self.getImmediateMode()

    def getImmediateMode(self):
        return self.chip.SPIImmediate

    def __repr__(self):
        return self.__str__()

    def __REPR__(self):
        register = self
        regName = self.name
        hexAddr = self.intToHex(self.addr)
        # Print register
        retVal = "REGISTER    " + regName + "    " + hexAddr + "\n"
        for bitField in register.getBitFields():
            retVal += bitField.__repr__
        retVal += "ENDREGISTER\n"
        return retVal

    def help(self):
        print(self.__REPR__())

    def __str__(self, maxFieldNameWidth=20):
        self.refresh()
        hexAddr = self.intToHex(self.addr)
        retVal = "Register : " + self.name + " " + hexAddr + "\n"
        flds = ""
        bitRepr = ""
        bitReprAll = ["0"] * 16

        # Determine max bitfield width
        for field in self.getBitFields():
            if maxFieldNameWidth < len(field.name):
                maxFieldNameWidth = len(field.name) + 1

        for field in self.getBitFields():
            bRep = field.evaluateBinRepr()
            bitRepr = bitRepr + field.name + " " * int(
                maxFieldNameWidth - len(field.name)) + bRep + "\t(" + self.intToHex(
                int("0b" + bRep.strip(), 2)) + " << " + str(field.getPosL()) + ")\t(" + str(
                int("0b" + bRep.strip(), 2)) + " << " + str(field.getPosL()) + ")\n"
            for i in range(0, 16):
                if bRep[i] != " ":
                    bitReprAll[i] = bRep[i]
            if flds != "":
                flds = flds + ", " + field.name
            else:
                flds = field.name
        # retVal = retVal+"Fields=["+flds+"]\n"
        retVal = retVal + bitRepr
        bRep = ""
        for i in range(0, 16):
            if bitReprAll[i] == "0":
                bRep = bRep + "0"
            else:
                bRep = bRep + "1"
        retVal = retVal + "Register value " + " " * int(
            maxFieldNameWidth - len("Register value ")) + bRep + "\t(" + self.intToHex(int("0b" + bRep, 2)) + ")\n"
        for comment in self.getComments():
            retVal = retVal + "#! " + comment.rstrip() + "\n"
        return retVal

    def getScriptRepr(self):
        self.refresh()
        retVal = self.name + " "
        for field in self.getBitFields():
            retVal += field.getName() + "=0b" + field.evaluateBinRepr().strip() + " "
        retVal.strip()
        return retVal

    def addBitField(self, bitField):
        # Check if bitfield collides with existing ones
        for field in self.getBitFields():
            if field.isInField(bitField.getPosH()) or field.isInField(bitField.getPosL()):
                raise ValueError(
                    "Bit field " + bitField.name + " position " + bitField.position + " collides with " + field.name + " position " + field.position)

        # All OK, add bitfield to register            
        self.bitFields.append(bitField)

    def getBitFieldByName(self, bitFieldName):
        for field in self.getBitFields():
            if bitFieldName == field.name:
                return field
        raise ValueError("Bit field " + bitFieldName + " does not exist in register " + self.name)

    def getBitFields(self):
        if self.nSets == 1:
            return self.bitFields
        else:
            activeSet = self.chip.MAC - 1
            return self.bitFields[activeSet]

    def getName(self):
        return self.name

    def addComment(self, commentLine):
        self.comment.append(commentLine)

    def getComments(self):
        return self.comment

    def getAddrBits(self):
        bits = bin(self.addr)
        bits = bits[2:]  # get rid of 0b
        # Make sure that bits has 15 digits
        while len(bits) < 15:
            bits = "0" + bits
        return bits

    def getAddress(self):
        return self.addr

    def getValue(self, noUpdate=False):
        # Evaluate bitfields
        if not noUpdate:
            self.refresh()
        val = 0
        for field in self.getBitFields():
            val = val | field.evaluate()
        return val

    def setValue(self, val, noUpdate=False):
        # Write value to bitfields
        for field in self.getBitFields():
            field.setValueFromReg(val)
        if not noUpdate:
            self.immediateWrite()

    def refresh(self):
        # Read the value from chip if immediate mode is enabled
        if self.getImmediateMode():
            if self.SPIreadFn is None:
                raise AttributeError("SPIreadFn must be set to use immediate mode")
            else:
                addr = self.getAddress()
                val = self.SPIreadFn([addr])[0]
                self.setValue(val, noUpdate=True)

    def immediateWrite(self):
        # Check if immediate mode is enabled
        if self.getImmediateMode():
            # Immediate mode is enabled, write the new value
            if self.SPIwriteFn is None:
                raise AttributeError("SPIwriteFn must be set to use immediate mode")
            else:
                addr = self.getAddress()
                val = self.getValue(noUpdate=True)
                self.SPIwriteFn([(addr, val)])

    def getValueBin(self):
        val = self.getValue()
        valB = bin(val)
        valB = valB[2:]
        while len(valB) < 16:
            valB = "0" + valB
        return valB

    def getReadValue(self):
        # Ignore write-only fields
        val = 0
        for field in self.getBitFields():
            if (field.mode == "R") or (field.mode == "RI") or (field.mode == "RW") or (field.mode == "RWI"):
                val = val | field.evaluate()
        return val

    def getReadValueBin(self):
        val = self.getReadValue()
        valB = bin(val)
        valB = valB[2:]
        while len(valB) < 16:
            valB = "0" + valB
        return valB

    def __len__(self):
        # Return the number of bitfields
        return len(self.getBitFields())

    def __getitem__(self, key):
        self.refresh()
        # Get the bitfield value
        bitField = self.getBitFieldByName(key)
        return bitField.getValue()

    def __setitem__(self, key, value):
        # Set the bitfield value
        self.refresh()
        if key == "":
            self.setValue(value)
        else:
            bitField = self.getBitFieldByName(key)
            if isinstance(value, int):
                val = int(value)
            elif "0b" in value:
                val = int(value, 2)
            elif "0x" in value:
                val = int(value, 16)
            else:
                raise ValueError("Unknown radix in value " + str(value))
            bitField.setValue(val)
            self.immediateWrite()


class BitField(object):
    def __init__(self, name, position, defValue, mode):
        self.name = name
        self.position = position
        self.defValue = defValue
        self.mode = mode.upper()
        self.comment = []
        self.stickyBit = False
        self.readBack = ""

        if mode == "RB":
            self.readBack = defValue
            self.defValue = "0" * int(self.getLenFromName())

        if mode == "STICKYBIT":
            if self.defValue != '0':
                raise ValueError("Bitfield " + name + " declared as sticky bit, but default value is not '0'")
            if self.getLenFromName() > 1:
                raise ValueError("Bitfield " + name + " declared as sticky bit, but bitfield length > 1")
            self.stickyBit = True
            self.mode = "RW"

        # Do some checks
        self.checkPosition()
        if self.getLen() != self.getLenFromName():
            raise ValueError("Bitfield " + self.name + " length is " + str(
                self.getLenFromName()) + " bits, while position " + self.position + " specifies a length of " + str(
                self.getLen()) + " bits")
        if self.getLen() != len(self.defValue):
            raise ValueError("Invalid default value. Expected " + str(self.getLen()) + " bits, got " + str(
                len(self.defValue)) + " (" + self.defValue + ")")

        if self.mode not in ["R", "RI", "RB", "W", "WI", "RW", "RWI", "RWE"]:
            raise ValueError("Invalid mode " + mode + " specified for bitfield " + self.name)

    def __repr__(self):
        bitField = self
        # Print bitField definition
        retVal = "    BITFIELD   " + bitField.getName() + "\n"
        retVal += "        POSITION=" + bitField.getPosition() + "\n"
        if self.mode == "RB":
            retVal += "        VALUE=" + bitField.getReadBackValue() + "\n"
        else:
            retVal += "        VALUE=" + bitField.getDefaultValue() + "\n"
        if not self.isSticky():
            retVal += "        MODE=" + bitField.getMode() + "\n"
        else:
            retVal += "        MODE=STICKYBIT\n"
        comments = bitField.getComments()
        for comment in comments:
            retVal += "        #! " + comment + "\n"
        retVal += "    ENDBITFIELD\n"
        return retVal

    def __str__(self):
        if not self.isSticky():
            retVal = "Bitfield : " + self.name + " POSITION=" + self.position + " VALUE=" + self.defValue + " MODE=" + self.mode + "\n"
        else:
            retVal = "Bitfield : " + self.name + " POSITION=" + self.position + " VALUE=" + self.defValue + " MODE=STICKYBIT\n"
        bitRepr = self.getBitRepr()
        retVal = retVal + "Bitfield position : " + bitRepr + "\n"
        for comment in self.getComments():
            retVal = retVal + "#! " + comment.rstrip() + "\n"
        return retVal

    def getReadBackValue(self):
        return self.readBack

    def isSticky(self):
        return self.stickyBit

    def getBitRepr(self):
        return ("-" * int(15 - self.getPosH())) + ("#" * int(self.getPosH() - self.getPosL() + 1)) + (
                    "-" * int(self.getPosL()))

    def getName(self):
        return self.name

    def getOnlyName(self):
        if "<" in self.name:
            # Vector
            return (self.name.split("<"))[0]
        else:
            return self.name

    def getPosition(self):
        return self.position

    def getDefaultValue(self):
        return self.defValue

    def getMode(self):
        return self.mode

    def getComments(self):
        return self.comment

    def checkPosition(self):
        if "<" in self.position:
            # Vector
            if ">" not in self.position:
                raise ValueError("Invalid bit field position " + self.position)
            tmp = self.position.split(":")
            low = int(tmp[1].split(">")[0])
            high = int(tmp[0].split("<")[1])
            if low < 0:
                raise ValueError("Invalid bit field position " + self.position)
            if high > 15:
                raise ValueError("Invalid bit field position " + self.position)
        else:
            # Single bit
            pos = int(self.position)
            if pos < 0:
                raise ValueError("Invalid bit field position " + self.position)
            if pos > 15:
                raise ValueError("Invalid bit field position " + self.position)
        return True

    def getPosH(self):
        if "<" in self.position:
            # Vector
            if ">" not in self.position:
                raise ValueError("Invalid bit field position " + self.position)
            tmp = self.position.split(":")
            high = int(tmp[0].split("<")[1])
            return high
        else:
            # Single bit
            pos = int(self.position)
            return pos

    def getPosHFromName(self):
        if "<" in self.name:
            # Vector
            if ">" not in self.name:
                raise ValueError("Invalid bit field position " + self.name)
            tmp = self.name.split(":")
            high = int(tmp[0].split("<")[1])
            return high
        else:
            # Single bit
            pos = -1
            return pos

    def getPosL(self):
        if "<" in self.position:
            # Vector
            if ">" not in self.position:
                raise ValueError("Invalid bit field position " + self.position)
            tmp = self.position.split(":")
            low = int(tmp[1].split(">")[0])
            return low
        else:
            # Single bit
            pos = int(self.position)
            return pos

    def getPosLFromName(self):
        if "<" in self.name:
            # Vector
            if ">" not in self.name:
                raise ValueError("Invalid bit field position " + self.name)
            tmp = self.name.split(":")
            low = int(tmp[1].split(">")[0])
            return low
        else:
            # Single bit
            pos = -1
            return pos

    def getLen(self):
        # Returns the length of bitfield
        if "<" in self.position:
            # Vector
            if ">" not in self.position:
                raise ValueError("Invalid bit field position " + self.position)
            tmp = self.position.split(":")
            low = int(tmp[1].split(">")[0])
            high = int(tmp[0].split("<")[1])
            return high - low + 1
        else:
            # Single bit
            return 1

    def getLenFromName(self):
        # Returns the length of bitfield from name
        if "<" in self.name:
            # Vector
            if ">" not in self.name:
                raise ValueError("Invalid bit field name " + self.name)
            tmp = self.name.split(":")
            low = int(tmp[1].split(">")[0])
            high = int(tmp[0].split("<")[1])
            return high - low + 1
        else:
            # Single bit
            return 1

    def isInField(self, bitPos):
        if "<" in self.position:
            # Vector
            if ">" not in self.position:
                raise ValueError("Invalid bit field position " + self.position)
            tmp = self.position.split(":")
            low = int(tmp[1].split(">")[0])
            high = int(tmp[0].split("<")[1])
            if (bitPos >= low) and (bitPos <= high):
                return True
            else:
                return False
        else:
            # Single bit
            pos = int(self.position)
            if bitPos == pos:
                return True
            else:
                return False

    def setValue(self, valueInt):
        binValue = bin(valueInt)[2:]
        while len(binValue) < self.getLen():
            binValue = "0" + binValue
        self.defValue = binValue

    def setValueBin(self, valueBin):
        if len(valueBin) != self.getLen():
            raise ValueError("Wrong number of bits given. Bitfield width is " + str(self.getLen()) +
                             ", while " + str(len(valueBin)) + " bits given.")
        self.defValue = valueBin

    def setValueFromReg(self, regValue):
        # Set bitfield value from register value
        val = regValue >> self.getPosL()
        mask = int("0b" + "1" * self.getLen(), 2)
        val = val & mask
        self.setValue(val)

    def getValueBin(self):
        # Return binary representation of bitfield
        return self.getDefaultValue()

    def getValue(self):
        # Return integer value of bitfield
        return int("0b" + self.getDefaultValue(), 2)

    def evaluate(self, bitFieldVal=None):
        # Evaluate bitfield value. Shift to correct position.
        if bitFieldVal is None:
            val = self.defValue
        else:
            val = bitFieldVal
        if len(val) != self.getLen():
            raise ValueError("Wrong number of bits given. Bitfield width is " + str(self.getLen()) +
                             ", while " + str(len(val)) + " bits given.")
        valInt = int("0b" + val, 2)
        valInt = int(valInt * (2 ** self.getPosL()))
        return valInt

    def evaluateBin(self, bitFieldVal=None):
        if bitFieldVal is None:
            val = self.defValue
        else:
            val = bitFieldVal
        valInt = self.evaluate(val)
        valB = bin(valInt)
        valB = valB[2:]  # get rid of 0b
        while len(valB) < 16:
            valB = "0" + valB
        return valB

    def evaluateBinRepr(self):
        binVal = self.evaluateBin()
        retVal = (" " * int(15 - self.getPosH())) + (binVal[16 - (self.getPosH() + 1):16 - self.getPosL()]) + (
                    " " * int(self.getPosL()))
        return retVal

    def addComment(self, commentLine):
        self.comment.append(commentLine)


class regDescParser(object):
    def __init__(self, regDefList, chip=None):
        """
        Read register definitions from a given file        
        """

        # Init locals
        self.regBanks = []  # Register banks specified in description
        self.registers = []  # registers
        self.comments = []  # comments

        self.regDefList = regDefList
        self.nLine = 0
        self.chip = chip

        # Read and parse the input file
        getLine = self.getLine
        try:
            while self.nLine < len(regDefList):
                line = getLine()
                if line == "":
                    continue

                line = line.strip()
                line = (line.split("##")[0]).rstrip()  # Throw away comments

                if line == "":
                    continue
                keyword = line.split()[0]
                if "#!" in keyword:
                    # Documentation comment
                    comment = line.split("#!")[1]
                    self.comments.append(comment)
                    continue
                if "REGISTER" in keyword:
                    # Register definition. Bitfields are parsed within register parser
                    reg = self.parseRegister(line)
                    reg.chip = self.chip
                    self.registers.append(reg)
                    continue
                if "REGBANK" in keyword:
                    # Register bank definition
                    bank = self.parseRegBank(line)
                    self.regBanks.append(bank)
                    continue
                # If we get here, we have encountered an unknown construct.
                # Signal error and exit
                raise ValueError("Unknown construct : " + line)
                return
        except error:
            retVal = "(" + str(self.nLine) + ") ERROR: " + str(error)
            raise ValueError(retVal)

        # Put registers to banks
        for reg in self.registers:
            regAssigned = False
            for bank in self.regBanks:
                if bank.isInBank(reg.addr):
                    bank.addRegister(reg)
                    if bank.nRegisterSets > 1:
                        reg.makeBitFieldCopies(bank.nRegisterSets)
                    regAssigned = True
                    break
            if not regAssigned:
                retVal = "ERROR : Register " + reg.name + " does not belong to any register bank"
                raise ValueError(retVal)

        RegisterDefinition.performChecks(self.regBanks)
        return

    def getLine(self):
        line = self.regDefList[self.nLine]
        self.nLine = self.nLine + 1  # Keep track of lines
        return line

    @staticmethod
    def parseRegBank(firstLine):
        # Register bank parsing
        args = firstLine.split()
        # We expect that first argument is REGBANK
        if args[0].strip() != "REGBANK":
            raise ValueError("Missing REGBANK keyword")
        name = args[1].strip()
        if len(name) == 0:
            raise ValueError("Missing register bank name")
        specifier = args[2].strip()
        if len(args) == 4:
            nRegisterSets = int(args[3].strip())
        else:
            nRegisterSets = 1
        return RegBank(name, specifier, nRegisterSets)

    def parseRegister(self, firstLine):
        # Register parsing
        args = firstLine.split()
        # We expect that first argument is REGISTER
        if args[0].strip() != "REGISTER":
            raise ValueError("Missing REGISTER keyword")
        name = args[1].strip()
        if len(name) == 0:
            raise ValueError("Missing register name")
        addr = args[2].strip()
        reg = Register(name, addr)  # Create register
        line = " "
        endRegister = False
        while line:
            line = self.getLine()
            if line == "":
                continue
            line = line.strip()
            line = (line.split("##")[0]).strip()  # Throw away comments
            if line == "":
                line = " "
                continue
            keyword = (line.split()[0]).strip()
            if "#!" in keyword:
                # Documentation comment
                comment = line.split("#!")[1]
                reg.addComment(comment)
                continue
            if "BITFIELD" in keyword:
                # Bitfiels definition
                bf = self.parseBitField(line)
                reg.addBitField(bf)
                continue
            if "ENDREGISTER" in keyword:
                # Finished parsing register
                endRegister = True
                break
            # Parser has encountered an unknown keyword
            raise ValueError("Unknown construct in register definition : " + line)

        if endRegister:
            return reg
        else:
            raise ValueError("Unexpected end of file while parsing register " + name)

    def parseBitField(self, firstLine):
        # Bitfield parsing
        args = firstLine.split()
        # We expect that first argument is BITFIELD
        if args[0].strip() != "BITFIELD":
            raise ValueError("Missing BITFIELD keyword")
        name = args[1].strip()
        if len(name) == 0:
            raise ValueError("Missing bitfield name")
        position = None
        defaultValue = None
        mode = None
        comments = []
        line = " "
        endBitField = False
        while line:
            line = self.getLine()
            if line == "":
                continue
            line = line.strip()
            line = (line.split("##")[0]).strip()  # Throw away comments
            if line == "":
                line = " "
                continue
            keyword = (line.split()[0]).strip()
            if "#!" in keyword:
                # Documentation comment
                comment = line.split("#!")[1]
                comments.append(comment)
                continue
            if "POSITION" in keyword:
                # Get position
                args = line.split("=")
                position = (args[1]).strip()
                continue
            if "DEFAULT" in keyword:
                # Get default value
                args = line.split("=")
                defaultValue = (args[1]).strip()
                continue
            if "MODE" in keyword:
                # Get mode
                args = line.split("=")
                mode = (args[1]).strip()
                continue
            if "ENDBITFIELD" in keyword:
                # Finished parsing bitfield
                endBitField = True
                break
            # Parser has encountered an unknown keyword
            raise ValueError("Unknown construct in bitfield definition : " + line)

        if endBitField:
            if not position:
                raise ValueError("Bit position is missing.")
                return None
            if not defaultValue:
                raise ValueError("Default value is missing.")
                return None
            if not mode:
                raise ValueError("Mode is missing.")
                return None
            bf = BitField(name, position, defaultValue, mode)
            # Add comments to bitfield
            for comment in comments:
                bf.addComment(comment)
            return bf
        else:
            raise ValueError("Unexpected end of file while parsing bitfield " + name)

    def findReg(self, regName):
        for reg in self.registers:
            if reg.name == regName:
                return reg
        raise ValueError("Register " + regName + " does not exist in register bank!")

    def getRegisterDefinition(self):
        regDef = RegisterDefinition("# Register definition")

        for regBank in self.regBanks:
            regDef.addRegBank(regBank)
        for comment in self.comments:
            regDef.addComment(comment)
        regDef.makeDictionaries()
        return regDef


class RegisterDefinition(object):
    # Container class for the chip register definition
    def __init__(self, name):
        self.regNameDict = {}
        self.regAddrDict = {}
        self.name = name
        self.regBanks = []  # Register banks
        self.comments = []  # comments

    def makeDictionaries(self):
        for regBank in self.regBanks:
            for reg in regBank.getRegs():
                regName = reg.getName()
                regAddr = reg.getAddress()
                self.regNameDict.update({regName: reg})
                self.regAddrDict.update({regAddr: reg})

    def getComments(self):
        return self.comments

    def getName(self):
        return self.name

    def addRegBank(self, regBank):
        self.regBanks.append(regBank)

    def getRegBanks(self):
        return self.regBanks

    def getRegBankByName(self, name):
        for regBank in self.regBanks:
            if regBank.getName() == name:
                return regBank
        raise ValueError("Register bank " + name + " not found")

    def addComment(self, comment):
        self.comments.append(comment)

    def getRegisterByName(self, regName):
        # if self.regNameDict.has_key(regName):
        if regName in self.regNameDict:
                return self.regNameDict[regName]
        else:
            raise ValueError("Register " + regName + " not found")

    def getRegisterByAddress(self, regAddr):
        # if self.regAddrDict.has_key(regAddr):
        if regAddr in self.regAddrDict:
            return self.regAddrDict[regAddr]
        else:
            # msavic 160606
            #            raise ValueError("Register on address "+str(regAddr)+" not found")
            warnings.warn("Register on address " + str(regAddr) + " not found")
            return -1

    def getRegistersByName(self, regList="ALL"):
        if regList == "ALL":
            regs = copy(list(self.regNameDict.values()))
        else:
            regs = []
            for regName in regList:
                regs.append(self.getRegisterByName(regName))
        return regs

    def getRegisterAddresesByName(self, regList="ALL"):
        if regList == "ALL":
            regAddrs = copy(list(self.regAddrDict.keys()))
        else:
            regAddrs = []
            for regName in regList:
                regAddrs.append(self.getRegisterByName(regName).getAddress())
        return regAddrs

    def __repr__(self):
        # Dump the whole register bank
        retVal = self.name + "\n"
        for comment in self.getComments():
            retVal += comment + "\n"

        for regBank in self.regBanks:
            retVal += regBank.__repr__

        for regBank in self.regBanks:
            for reg in regBank.getRegs():
                retVal += reg.__repr__ + "\n"
        return retVal

    def check(self):
        self.performChecks(self.getRegBanks())

    @staticmethod
    def performChecks(regBanks):
        # Perform various checks on a set of register banks

        # Check if register bank names are unique
        allRegBanks = {}
        for bank in regBanks:
            # if allRegBanks.has_key(bank.name):
            if bank.name in allRegBanks:
                retVal = "ERROR: Bank name " + bank.name + " is not unique."
                raise ValueError(retVal)
            allRegBanks.update({bank.name: None})

        # Check if register and field names are unique
        allRegs = {}
        for bank in regBanks:
            for reg in bank.getRegs():
                # if allRegs.has_key(reg.name):
                if reg.name in allRegs:
                    retVal = "ERROR: Register name " + reg.name + " is not unique."
                    raise ValueError(retVal)
                allRegs.update({reg.name: None})

        # Check if register banks are overlapping
        for bank1 in regBanks:
            for bank2 in regBanks:
                if bank1 == bank2:
                    continue
                lowAddr = bank1.getAddrL()
                highAddr = bank1.getAddrH()
                if bank2.isInBank(lowAddr) or bank2.isInBank(highAddr):
                    raise ValueError("ERROR: Banks " + bank1.getName() + " and " + bank2.getName() + " are overlapping")
