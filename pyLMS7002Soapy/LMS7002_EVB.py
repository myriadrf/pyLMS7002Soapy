#***************************************************************
#* Name:      LMS7002_EVB.py
#* Purpose:   Class implementing LMS7002_EVB functions
#* Author:    Lime Microsystems ()
#* Created:   2016-11-14
#* Copyright: Lime Microsystems (limemicro.com)
#* License:
#**************************************************************

import serial
import serial.tools.list_ports
from copy import copy
from LMS7002 import *
from ADF4002 import *
from Si5351 import *

class LMS7002_EVB(object):

    def __init__(self, portName='/dev/ttyACM0', fRef = 30.72e6, verbose=0):
        """
        Initialize communication with LMS7002_EVB
        """
        self.ser=serial.Serial(port=portName)
        self.verbose = verbose
        self.fRef = fRef # reference frequency
        if not self.ser.isOpen():
            self.ser = None
            raise IOError("Could not open port "+portName+"\nPlease ensure that the port exists and that the permissions are set correctly.\nOn Linux systems permissions can be set by sudo chmod a+rw /dev/portName")
        FW_VER, DEV_TYPE, LMS_PROTOCOL_VER, HW_VER, EXP_BOARD = self.getInfo()
        if DEV_TYPE!=7:
            ret = "FW_VER           : "+str(FW_VER)+"\n"
            ret += "DEV_TYPE         : "+str(DEV_TYPE)+"\n"
            ret += "LMS_PROTOCOL_VER : " + str(LMS_PROTOCOL_VER)+"\n"
            ret += "HW_VER           : " + str(HW_VER)+"\n"
            ret += "EXP_BOARD        : " + str(EXP_BOARD)+"\n"
            raise ValueError("The board is not LMS7002_EVB.\nBoard info:\n"+ret)
        if verbose>0:
            self.printInfo()
        
        #
        # Initialize on-board chips
        #
        
        self.LMS7002 = LMS7002(SPIwriteFn=self.LMS7002_Write, SPIreadFn=self.LMS7002_Read, verbose=verbose, MCUProgram=self.MCUProgram, fRef = self.fRef)
        self.LMS7002.MIMO = 'MIMO'
        self.ADF4002 = ADF4002(self.ADF4002Program)
        self.Si5351 = Si5351(self.Si5351Progam)
        
        
    def __del__(self):
        """
        Close communication with LMS7002_EVB
        """
        if self.ser:
            self.ser.close()
    
    @staticmethod
    def findLMS7002():
        res = []
        for port in serial.tools.list_ports.comports():
            if port.vid==1003 and port.pid==8267:
                try:
                    portName = port.device
                    ser=serial.Serial(port=portName)
                    bytes = [0]*64
                    s = ""
                    for i in range(0,len(bytes)):
                        s += chr(bytes[i])                
                    ser.write(s)
                    tmp = ser.read(size=64)
                    bytes = [0]*int(len(tmp))
                    for i in range(0, len(tmp)):
                        bytes[i] = ord(tmp[i])                
                    if len(bytes)<64:
                        ser.close()
                        continue
                    rxData = bytes[8:]
                    if rxData[1]==7:
                        res.append(portName)
                    ser.close()
                except:
                    pass
        return res            
            
    def log(self, logMsg):
        print logMsg

    def getCommandNumber(self, cmdName):
        if cmdName == "CMD_GET_INFO":
            return 0x00
        elif cmdName == "CMD_LMS_RST":
            return 0x20
        elif cmdName == "LMS_RST_DEACTIVATE":
            return 0x00
        elif cmdName == "LMS_RST_ACTIVATE":
            return 0x01
        elif cmdName == "LMS_RST_PULSE":
            return 0x02
        elif cmdName == "CMD_LMS7002_WR":
            return 0x21
        elif cmdName == "CMD_LMS7002_RD":
            return 0x22
        elif cmdName == "CMD_PROG_MCU":
            return 0x2C
        elif cmdName == "CMD_ADF4002_WR":
            return 0x31
        elif cmdName == "CMD_SI5351_WR":
            return 0x13
        else:
            raise ValueError("Unknown command "+cmdName)

    def getLMS7002(self):
        return self.LMS7002
            
    #
    # Low level communication
    #
    
    @staticmethod
    def bytes2string(bytes):
        """
        Convert the byte array to string.
        Used for serial communication.
        """
        s = ""
        for i in range(0,len(bytes)):
            s += chr(bytes[i])
        return s

    @staticmethod
    def string2bytes(string):
        """
        Convert the string to byte array.
        Used for serial communication.
        """
        bytes = [0]*int(len(string))
        for i in range(0, len(string)):
            bytes[i] = ord(string[i])
        return bytes

    def sendCommand(self, command, nDataBlocks=0, periphID=0, data=[]):
        """
        Send the command to LMS7002_EVB.
        Function returns (status, data)
        """
        tmp = [0]*64
        tmp[0] = command
        tmp[1] = 0
        tmp[2] = nDataBlocks
        tmp[3] = periphID
        nData = len(data)
        if nData>56:
            raise ValueError("Length of data must be less than 56, "+str(nData)+" bytes given")
        for i in range(0, nData):
            tmp[8+i] = data[i]
        if self.verbose>2:
            self.log("sendCommand:Write    : "+str(tmp))
        self.ser.write(self.bytes2string(tmp))
        tmp = self.string2bytes(self.ser.read(size=64))
        if len(tmp)<64:
            raise IOError("Lenght of received data "+len(tmp)+"<64 bytes")
        if self.verbose>2:
            self.log("sendCommand:Response : "+str(tmp))
        rxStatus = tmp[1]
        rxData = tmp[8:]
        return (rxStatus, rxData)

    #
    # Utility functions
    #

    def getInfo(self):
        """
        Get the information about LMS7002_EVB.
        Function returns 
        (FW_VER, DEV_TYPE, LMS_PROTOCOL_VER, HW_VER, EXP_BOARD)
        """
        command = self.getCommandNumber("CMD_GET_INFO")
        status, rxData = self.sendCommand(command)
        if status != 1:
            raise IOError("Command returned with status "+str(status))
        FW_VER = rxData[0]
        DEV_TYPE = rxData[1]
        LMS_PROTOCOL_VER = rxData[2]
        HW_VER = rxData[3]
        EXP_BOARD = rxData[4]
        return (FW_VER, DEV_TYPE, LMS_PROTOCOL_VER, HW_VER, EXP_BOARD)
   
    def printInfo(self):
        """
        Print info about LMS7002_EVB
        """
        FW_VER, DEV_TYPE, LMS_PROTOCOL_VER, HW_VER, EXP_BOARD = self.getInfo()
        self.log("FW_VER           : "+str(FW_VER))
        self.log("DEV_TYPE         : "+str(DEV_TYPE))
        self.log("LMS_PROTOCOL_VER : " + str(LMS_PROTOCOL_VER))
        self.log("HW_VER           : " + str(HW_VER))
        self.log("EXP_BOARD        : " + str(EXP_BOARD))
        
    def LMS7002_Reset(self, rstType="pulse"):
        """
        Reset LMS7002.
        rstType specifies the type of reset:
            pulse - activate and deactivate reset
            activate - activate reset
            deactivate - deactivate reset
        """
        command = self.getCommandNumber("CMD_LMS_RST")
        if rstType=="pulse":
            data = [self.getCommandNumber("LMS_RST_PULSE")]
        elif rstType=="activate":
            data = [self.getCommandNumber("LMS_RST_ACTIVATE")]        
        elif rstType=="deactivate":
            data = [self.getCommandNumber("LMS_RST_DEACTIVATE")]        
        else:
            raise ValueError("Invalid reset type "+str(rstType))
        rxStatus, rxData = self.sendCommand(command, data=data)
        if rxStatus != 1:
            raise IOError("Command returned with status "+str(status))
        self.LMS7002.loadResetValues()
		
#msavic 160606
    def LMS7002_ResetClean(self, rstType="pulse"):
        """
        Reset LMS7002.
        rstType specifies the type of reset:
            pulse - activate and deactivate reset
            activate - activate reset
            deactivate - deactivate reset
        """
        command = self.getCommandNumber("CMD_LMS_RST")
        if rstType=="pulse":
            data = [self.getCommandNumber("LMS_RST_PULSE")]
        elif rstType=="activate":
            data = [self.getCommandNumber("LMS_RST_ACTIVATE")]        
        elif rstType=="deactivate":
            data = [self.getCommandNumber("LMS_RST_DEACTIVATE")]        
        else:
            raise ValueError("Invalid reset type "+str(rstType))
        rxStatus, rxData = self.sendCommand(command, data=data)
        if rxStatus != 1:
            raise IOError("Command returned with status "+str(status))
#        self.LMS7002.loadResetValues()		

    def LMS7002_Write(self, regList, packetSize=14):
        """
        Write the data to LMS7002 via SPI interface.
        regList is a list of registers to write in the format:
        [ (regAddr, regData), (regAddr, regData), ...]
        packetSize controls the number of register writes in a single USB transfer
        """
        command = self.getCommandNumber("CMD_LMS7002_WR")
        nDataBlocks = len(regList)

        toSend = copy(regList)
       
        while len(toSend)>0:
            nPackets = 0
            data = []
            while nPackets<packetSize and len(toSend)>0:
                regAddr, regData = toSend[0]
                toSend.pop(0)
                regAddrH = regAddr >> 8
                regAddrL = regAddr % 256
                regDataH = regData >> 8
                regDataL = regData % 256
                data += [regAddrH, regAddrL, regDataH, regDataL]
                nPackets += 1
            rxStatus, rxData = self.sendCommand(command, nDataBlocks = nPackets, data=data)
            if rxStatus != 1:
                raise IOError("Command returned with status "+str(rxStatus))

        
    def LMS7002_Read(self, regList, packetSize=14):
        """
        Read the data from LMS7002 via SPI interface.
        regList is a list of registers to read in the format:
        [ regAddr, regAddr, ...]
        packetSize controls the number of register writes in a single USB transfer
        """
        command = self.getCommandNumber("CMD_LMS7002_RD")
        nDataBlocks = len(regList)

        toRead = copy(regList)
        regData = []
       
        while len(toRead)>0:
            nPackets = 0
            data = []
            while nPackets<packetSize and len(toRead)>0:
                regAddr = toRead[0]
                toRead.pop(0)
                regAddrH = regAddr >> 8
                regAddrL = regAddr % 256
                data += [regAddrH, regAddrL]
                nPackets += 1
            rxStatus, rxData = self.sendCommand(command, nDataBlocks = nPackets, data=data)
            if rxStatus != 1:
                raise IOError("Command returned with status "+str(rxStatus))
            for i in range(0, nPackets):
                regDataH = rxData[i*4+2]
                regDataL = rxData[i*4+3]
                regData.append( (regDataH << 8) + regDataL)
        return regData

    #
    # LMS7002 MCU program
    #
    
    def MCUProgram(self, mcuProgram, Mode):
        """
        Write the data to LMS7002 MCU via SPI interface.
        mcuProgram is 8192 bytes long array holding the MCU program.
        mode selects the MCU programming mode.
        """
        if Mode not in [0, 1,2,3, 'EEPROM_AND_SRAM', 'SRAM', 'SRAM_FROM_EEPROM']:
            raise ValueError("Mode should be [1,2,3, 'EEPROM_AND_SRAM', 'SRAM', 'SRAM_FROM_EEPROM']")
        if Mode==0:
            return
        elif Mode==1 or Mode=='EEPROM_AND_SRAM':
            mode = 1
        elif Mode==2 or Mode=='SRAM':
            mode = 2
        else:
            mode = 3

        if len(mcuProgram)!=8192:
            raise ValueError("MCU program should be 8192 bytes long")
        
        command = self.getCommandNumber("CMD_PROG_MCU")

        pos = 0
        while pos<8192:
            data = [0]*34
            data[0] = mode
            data[1] = pos//32
            for i in range(0,32):
                data[2+i] = mcuProgram[pos+i]
            rxStatus, rxData = self.sendCommand(command, nDataBlocks=34, data=data)
            if rxStatus != 1:
                raise IOError("Command returned with status "+str(rxStatus))
            pos += 32
            if mode==3:
                break

    #
    # ADF4002 program
    #                

    def ADF4002Program(self, regValues):
        """
        Program ADF4002 with given regValues.
        regValues = [reg1, reg2, reg3, reg4]
        where reg1-4 are integers containing the values of ADF4002 registers (24 bit).
        """
        if len(regValues)!=4:
            raise ValueError("Expected four 24-bit values, got "+str(len(regValues)))
        data = []
        for reg in regValues:
            bits23_16 = (reg >> 16) & 0xFF
            bits15_8 = (reg >> 8) & 0xFF
            bits7_0 = reg & 0xFF
            data += [bits23_16, bits15_8, bits7_0]
        command = self.getCommandNumber("CMD_ADF4002_WR")
        rxStatus, rxData = self.sendCommand(command, nDataBlocks=4, data=data)
        if rxStatus != 1:
            raise IOError("Command returned with status "+str(rxStatus))


    #
    # Si5351
    #        
    def Si5351Progam(self, regList, packetSize=20):
        """
        Program Si5351
        """
        command = self.getCommandNumber("CMD_SI5351_WR")
        nDataBlocks = len(regList)

        toSend = copy(regList)
       
        while len(toSend)>0:
            nPackets = 0
            data = []
            while nPackets<packetSize and len(toSend)>0:
                regAddr, regData = toSend[0]
                toSend.pop(0)
                data += [regAddr, regData]
                nPackets += 1
            rxStatus, rxData = self.sendCommand(command, nDataBlocks = nPackets, data=data)
            if rxStatus != 1:
                raise IOError("Command returned with status "+str(rxStatus))

        
