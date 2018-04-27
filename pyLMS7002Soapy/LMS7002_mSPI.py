#***************************************************************
#* Name:      LMS7002_mSPI.py
#* Purpose:   Class implementing LMS7002 mSPI functions
#* Author:    Lime Microsystems ()
#* Created:   2016-11-14
#* Copyright: Lime Microsystems (limemicro.com)
#* License:
#**************************************************************

from LMS7002_base import *
import time

class LMS7002_mSPI(LMS7002_base):
    __slots__=[]    # Used to generate error on typos
    def __init__(self, chip):
        self.chip = chip
        self.channel = None
        self.prefix = "mSPI_"

    def getOpCode(self, opCode):
        if opCode == "SFR":
            return 0x7E
        elif opCode == "IRAM_READ":
            return 0x78
        elif opCode == "RESET_PC":
            return 0x70
        elif opCode == "RUN_INSTR":
            return 0x74
        else:
            raise ValueError("Unknown MCU opcode :"+str(opCode))

    #
    # Auxiliary functions
    #

    def _readHex(self, hexFileName, isString=False):
        """
        Read Intel hex file.
        Returns a 16384 or 8192 bytes long list containing the MCU program.
        """
        if not isString:
            inFile = open(hexFileName, 'r')
        else:
            inFile = hexFileName.split('\n')
        ret = [0]*16384
        maxAddr = 0
        for line in inFile:
            line = line.strip()
            if line=='':
                continue
            if line[0]!=':':
                raise ValueError("Line does not start with :. Is this an Intel hex file?")
            lineData = []
            for i in range(1,len(line),2):
                lineData.append(int("0x"+line[i:i+2],16))
            nBytes = lineData[0]
            offset = (lineData[1]<<8) + lineData[2]
            recType = lineData[3]
            data = lineData[4:4+nBytes]
            ckSum = 0
            for i in range(0, len(lineData)-1):
                ckSum += lineData[i]
            ckSum = ~ckSum + 1
            ckSum = ckSum%256
            if ckSum != lineData[len(lineData)-1]:
                raise ValueError("Checksum error in line : "+line)
            for i in range(0, len(data)):
                if offset+i>maxAddr:
                    maxAddr = offset+i
                ret[offset+i] = data[i]
        if not isString:
            inFile.close()
        if maxAddr<8192:
            ret = ret[:8192]    # Discard last 8192 bytes, since they are not used
        return ret

    def loadHex(self, hexFileName, mode='SRAM', isString=False):
        immMode = self.chip.SPIImmediate
        self.chip.SPIImmediate = True
        mcuProgram = self._readHex(hexFileName, isString)
        self.chip._MCUProgram(mcuProgram, mode)
        self.chip.SPIImmediate = immMode
        
    def reset(self):
        """
        Put the MCU in reset, and hold it in reset state
        """
        immMode = self.chip.SPIImmediate
        self.chip.SPIImmediate = True
        self.MODE = 'RESET'
        self.DEBUG = 0
        self.EXT_INT = 0
        self.RXD = 0
        self.P0 = 0
        self.chip.SPIImmediate = immMode

    def resetPC(self):
        immMode = self.chip.SPIImmediate
        self.chip.SPIImmediate = True
        ret = self._command([self.getOpCode("RESET_PC")], 1)
        self.chip.SPIImmediate = immMode
        return ret

    def runInstr(self):
        immMode = self.chip.SPIImmediate
        self.chip.SPIImmediate = True
        data = self._command([self.getOpCode("RUN_INSTR"), 0, 0], 3)
        self.chip.SPIImmediate = immMode
        return data[1]*256+data[2]

    def call(self, data):
        immMode = self.chip.SPIImmediate
        self.chip.SPIImmediate = True
        self.P0 = 0
        if data!=0:
            self.SPISW_CTRL = 1
        else:
            self.SPISW_CTRL = 0
        self.P0 = data
        self.chip.SPIImmediate = immMode
        
    def waitForMCU(self, timeout=1):
        immMode = self.chip.SPIImmediate
        self.chip.SPIImmediate = True
        t0 = time.time()
        while time.time()-t0<timeout:
            val = self.P1
            if val!= 0xFF:
                break
        if time.time()-t0>timeout:
            raise ValueError("Timeout expired in waitForMCU")
        self.chip.SPIImmediate = immMode
        return val
        
    def startDebugMode(self):
        immMode = self.chip.SPIImmediate
        self.chip.SPIImmediate = True
        self.DEBUG = 1
        self.chip.SPIImmediate = immMode
            
    def exitDebugMode(self):
        immMode = self.chip.SPIImmediate
        self.chip.SPIImmediate = True
        self.DEBUG = 0        
        self.chip.SPIImmediate = immMode
        
    def _waitUntilWritten(self, timeout=1):
        """
        Waits until WRITE_REQ=1 or timeout expires.
        If timeout expires an exception is raised.
        """
        immMode = self.chip.SPIImmediate
        self.chip.SPIImmediate = True
        t0 = time.time()
        while (self.WRITE_REQ==1) and (time.time()-t0<timeout):
            pass
        self.chip.SPIImmediate = immMode
        if time.time()-t0>timeout:
            raise ValueError("Timeout expired in waitUntilWritten")

    def _readOneByte(self, timeout=1):
        """
        Waits until READ_REQ=0 or timeout expires.
        If timeout expires an exception is raised.
        """
        immMode = self.chip.SPIImmediate
        self.chip.SPIImmediate = True
        t0 = time.time()
        while (self.READ_REQ==0) and (time.time()-t0<timeout):
            pass
        data = self.DFM
        self.chip.SPIImmediate = immMode
        if time.time()-t0>timeout:
            raise ValueError("Timeout expired in readOneByte")
        return data

    def _command(self, writeData, bytesToReceive):
        """
        Writes the data given in writeData list.
        Returns bytesToReceive received bytes
        """
        immMode = self.chip.SPIImmediate
        self.chip.SPIImmediate = True
        for data in writeData:
            self.DTM = data
            self._waitUntilWritten()
        recData = []
        for i in range(0, bytesToReceive):
            recData.append(self._readOneByte())
        self.chip.SPIImmediate = immMode
        return recData

    def _wait(self, n):
        immMode = self.chip.SPIImmediate
        self.chip.SPIImmediate = True
        for i in range(0, n//64):
            tmp = self.chip['mSPI_STAT']
        self.chip.SPIImmediate = immMode

    def changeMCUFrequency(self, value):
        self._command( [self.getOpCode("SFR"), 0x8E, value], 3)
        
    def readIRAM(self):
        data = [0]*256
        opCode = self.getOpCode("IRAM_READ")
        for i in range(0,256):
            res = self._command( [opCode, i, 0], 3)
            data[i] = res[2]
            self._wait(64)
        return data

    #
    # mSPI_P0 (0x0000)
    #

    @property 
    def P0(self):
        """
        Get the value of P0<7:0>
        """
        return self._readReg('P0', 'P0<7:0>')

    @P0.setter
    def P0(self, value):
        """
        Set the value of P0<7:0>
        """
        if not(0<= value <=1023):
            raise ValueError("Value must be [0..255]")
        self._writeReg('P0', 'P0<7:0>', value)

    #
    # mSPI_P1 (0x0001)
    #

    @property 
    def P1(self):
        """
        Get the value of P1<7:0>
        """
        return self._readReg('P1', 'P1<7:0>')

    @P1.setter
    def P1(self, value):
        """
        Set the value of P1<7:0>
        """
        if not(0<= value <=255):
            raise ValueError("Value must be [0..255]")
        self._writeReg('P1', 'P1<7:0>', value)

    #
    # mSPI_CFG (0x0002)
    #
    
    # RXD
    @property 
    def RXD(self):
        """
        Get the value of RXD
        """
        return self._readReg('CFG', 'RXD')

    @RXD.setter
    def RXD(self, value):
        """
        Set the value of RXD
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG', 'RXD', value)

    # DEBUG
    @property 
    def DEBUG(self):
        """
        Get the value of DEBUG
        """
        return self._readReg('CFG', 'DEBUG')

    @DEBUG.setter
    def DEBUG(self, value):
        """
        Set the value of DEBUG
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('CFG', 'DEBUG', value)

    # EXT_INT<5:2>
    @property 
    def EXT_INT(self):
        """
        Get the value of EXT_INT<5:2>
        """
        return self._readReg('CFG', 'EXT_INT<5:2>')

    @EXT_INT.setter
    def EXT_INT(self, value):
        """
        Set the value of EXT_INT<5:2>
        """
        if not(0 <= value <= 15):
            raise ValueError("Value must be [0..15]")
        self._writeReg('CFG', 'EXT_INT<5:2>', value)

    # MODE<1:0>
    @property 
    def MODE(self):
        """
        Get the value of MODE<1:0>
        """
        return self._readReg('CFG', 'MODE<1:0>')

    @MODE.setter
    def MODE(self, Mode):
        """
        Set the value of MODE<1:0>
        """
        if Mode not in [0, 1,2,3, 'RESET', 'EEPROM_AND_SRAM', 'SRAM', 'SRAM_FROM_EEPROM']:
            raise ValueError("Mode should be [0, 1,2,3, 'RESET', 'EEPROM_AND_SRAM', 'SRAM', 'SRAM_FROM_EEPROM']")
        if Mode==0 or Mode=='RESET':
            return
        elif Mode==1 or Mode=='EEPROM_AND_SRAM':
            mode = 1
        elif Mode==2 or Mode=='SRAM':
            mode = 2
        else:
            mode = 3
        self._writeReg('CFG', 'MODE<1:0>', mode)

    #
    # mSPI_STAT (0x0003)
    #

    # TXD
    @property 
    def TXD(self):
        """
        Get the value of TXD
        """
        return self._readReg('STAT', 'TXD')

    @TXD.setter
    def TXD(self, value):
        """
        Set the value of TXD
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('STAT', 'TXD', value)

    # PROGRAMMED
    @property 
    def PROGRAMMED(self):
        """
        Get the value of PROGRAMMED
        """
        return self._readReg('STAT', 'PROGRAMMED')

    # READ_REQ
    @property 
    def READ_REQ(self):
        """
        Get the value of READ_REQ
        """
        return self._readReg('STAT', 'READ_REQ')

    @READ_REQ.setter
    def READ_REQ(self, value):
        """
        Set the value of READ_REQ
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('STAT', 'READ_REQ', value)

    # WRITE_REQ
    @property 
    def WRITE_REQ(self):
        """
        Get the value of WRITE_REQ
        """
        return self._readReg('STAT', 'WRITE_REQ')

    @WRITE_REQ.setter
    def WRITE_REQ(self, value):
        """
        Set the value of WRITE_REQ
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('STAT', 'WRITE_REQ', value)

    # FULL_WRITE_BUFF
    @property 
    def FULL_WRITE_BUFF(self):
        """
        Get the value of FULL_WRITE_BUFF
        """
        return self._readReg('STAT', 'FULL_WRITE_BUFF')

    @FULL_WRITE_BUFF.setter
    def FULL_WRITE_BUFF(self, value):
        """
        Set the value of FULL_WRITE_BUFF
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('STAT', 'FULL_WRITE_BUFF', value)

    # EMPTY_WRITE_BUFF
    @property 
    def EMPTY_WRITE_BUFF(self):
        """
        Get the value of EMPTY_WRITE_BUFF
        """
        return self._readReg('STAT', 'EMPTY_WRITE_BUFF')

    @EMPTY_WRITE_BUFF.setter
    def EMPTY_WRITE_BUFF(self, value):
        """
        Set the value of EMPTY_WRITE_BUFF
        """
        if value not in [0, 1]:
            raise ValueError("Value must be [0,1]")
        self._writeReg('STAT', 'EMPTY_WRITE_BUFF', value)

    #
    # mSPI_DTM (0x0004)
    #
    @property 
    def DTM(self):
        """
        Get the value of DTM<7:0>
        """
        return self._readReg('DTM', 'DTM<7:0>')

    @DTM.setter
    def DTM(self, value):
        """
        Set the value of DTM<7:0>
        """
        if not(0<= value <=255):
            raise ValueError("Value must be [0..255]")
        self._writeReg('DTM', 'DTM<7:0>', value)

    #
    # mSPI_DFM (0x0005)
    #
    @property 
    def DFM(self):
        """
        Get the value of DFM<7:0>
        """
        return self._readReg('DFM', 'DFM<7:0>')

    @DFM.setter
    def DFM(self, value):
        """
        Set the value of DFM<7:0>
        """
        if not(0<= value <=255):
            raise ValueError("Value must be [0..255]")
        self._writeReg('DFM', 'DFM<7:0>', value)

    #
    # mSPI_SPISW (0x0006)
    #

    # SPISW_CTRL
    @property 
    def SPISW_CTRL(self):
        """
        Get the value of SPISW_CTRL
        """
        return self._readReg('SPISW', 'SPISW_CTRL')

    @SPISW_CTRL.setter
    def SPISW_CTRL(self, value):
        """
        Set the value of SPISW_CTRL
        """
        if value not in [0, 1, 'BB', 'MCU']:
            raise ValueError("Value must be [0,1]")
        if value == 0 or value == 'BB':
            val = 0
        else:
            val = 1
        self._writeReg('SPISW', 'SPISW_CTRL', val)

    def getProductionTestHex(self):
        return """:06000000020041020108AC
        :03000B00020412DA
        :03001300020120C7
        :03001B000204AB31
        :030023000207A829
        :03002B000207D9F0
        :01003300329A
        :03003B0002079821
        :03009A0002003E23
        :03003E0002082194
        :20009D00752F7F7582FF75830374A1F074FFE0F530C394A17002C27878FE75BF0374A2F259
        :2000BD0074FFE2F531C394A27002C27979FD75BF0374A3F374FFE3F532C394A37002C27A26
        :2000DD00750FA4740FF8E6F533C394A47002C27B790E77A5E50EF534C394A57002C27C003D
        :2000FD0075EC3575880575A8850022C0E0C0D074A6F535C394A67004C27DC2A80000D0D059
        :20011D00D0E032C0E0C0D074A7F536C394A77004C27EC2AA0000D0D0D0E032752F77758CAE
        :20013D001F758A52758DFE758BA375891075885075A88A752B07752C070022752F7775ECA0
        :20015D0011758CFC758AFC758DFC758BFE75896675885075A88A752B07752C070022752F10
        :20017D007775A8A075CAA375CBFE75CCA375CDFE75C80C752D070022752F7775EC11758C48
        :20019D00FE758A0A75890175881075A882759800C29FD29E75CA9F75CBFF75CC9F75CDFF74
        :2001BD0075C804D2CC752B07752D007599AA0022752F7775EC11758921758CFE758A0A75F7
        :2001DD008BF0758DF075878075885075A882759800C29FD29ED29C752C00752B07752D00F7
        :2001FD000022752F7775EC1175ED35758CFC758AFE758DFC758BFC7589EE75885075A88AC8
        :20021D00752B07752C07752D000022752FFF752B647520007521017522027523037524040A
        :20023D00752505752606752707E52B79A0F794647002C2787401C2D3C2D478202879A1F789
        :20025D0094217002C279742179242979A2F794457002C27A74457924989979A3F79401708C
        :20027D0002C27B7401D2D3C2D47821792526F5F027F5F079A4F794077002C27C74077821B1
        :20029D0079259697F5F0C2D3D2D47822792625222526F5F079A5F794097002C27D7409794D
        :2002BD0026952297F5F0D2D3D2D478237927262407F5F079A6F7740B7927940397F5F0794B
        :2002DD00A7F77401C2D3C2D478237921D3383735253401F5F079A8F7742C782304F5F00894
        :2002FD0088F0E8F5F079A9F794247002C27EE521792107E779AAF794027002C27F00227591
        :20031D002FFFC2D3C2D4752B0578087508077F0374055F79B0F794017002C27874085679B8
        :20033D00B1F794007002C2797409522B532B0FE52B79B2F794017002C27A74014F752B0C4B
        :20035D00452B79B3F7940F7002C27B7403464401422BE52B79B4F7940F7002C27C740F68BA
        :20037D00652B66640579B5F7940A7002C27D632B05E52B79B6F7940A7002C27E740FF4C439
        :20039D002333333333130379B7F794787002C27F0022752FFFD3C3D200C200400679C07770
        :2003BD00AAC278B3500679C177AAC279B20000B20010000679C277AAC27A8200B000400613
        :2003DD0079C377AAC27B7200400679C477AAC27CC3400679C577AAC27DA000500679C677BF
        :2003FD00AAC27ED200A200B3920010000679C777AAC27F0022C0E0C007C000C0D075D00067
        :20041D007828B60210E52B2440F8A62B758C1E758AA30080527828B6030AE52B2450F8A602
        :20043D002B0080437828B6051CE52B2470F8A62BE52B94007006C2CCC299C2CA758CFE75CA
        :20045D008A0A0080227828B60610E52B2480F8A62B758CFE758A0A00800D7828B60708E581
        :20047D002B2490F8A62B00782CE6C454F0FF782BE62F782FF6782BE67006C28CC2A9800594
        :20049D00782B16D28CD0D0D000D007D0E032C0E0C007C000C0D075D0007828B6020E758D9B
        :2004BD00FE758BA3E52C2448F8A62C007828B60308E52C2458F8A62C007828B60708E52C09
        :2004DD002498F8A62C00782CE6C454F0FF782BE62F782FF6782CE67006C28EC2AB800578D9
        :2004FD002C16D28ED0D0D000D007D0E032752FFF78000874FE48F8740F58F818740F98F841
        :20051D00D8027802D3740138C328780668B40006788876AAC27879000974FE49F9740F59F3
        :20053D00F919740F99F9D9027902D3740139C329790669B40006788976AAC2797A000A74BE
        :20055D00FE4AFA740F5AFA1A740F9AFADA027A02D374013AC32A7A066AB40006788A76AAA7
        :20057D00C27A7B000B74FE4BFB740F5BFB1B740F9BFBDB027B02D374013BC32B7B066BB46C
        :20059D000006788B76AAC27B7C000C74FE4CFC740F5CFC1C740F9CFCDC027C02D374013CA4
        :2005BD00C32C7C066CB40006788C76AAC27C7D000D74FE4DFD740F5DFD1D740F9DFDDD02E9
        :2005DD007D02D374013DC32D7D066DB40006788D76AAC27D7E000E74FE4EFE740F5EFE1EB5
        :2005FD00740F9EFEDE027E02D374013EC32E7E066EB40006788E76AAC27E7F000F74FE4F87
        :20061D00FF740F5FFF1F740F9FFFDF027F02D374013FC32F7F066FB40006788F76AAC27FAC
        :20063D0022752FFF74FF75F0FFA4B4010F78B8F6C278E5F0B4FE05C27978B9F674AA75F0C8
        :20065D00BBA4B42E0F78BAF6C27AE5F0B47C05C27B78BBF674CC75F099A4B4EC0F78BCF69E
        :20067D00C27CE5F0B47905C27D78BDF6740075F0FFA4B4000F78BEF6C27EE5F0B4000578FD
        :20069D00BFF6C27F22752FFF74FF75F00184B4FF0F78C8F6C278E5F0B40005C27978C9F6F3
        :2006BD0074AA75F00B84B40F0F78CAF6C27AE5F0B40505C27B78CBF674CC75F00984B416C0
        :2006DD000F78CCF6C27CE5F0B40605C27D78CDF674FF75F00084B4000F78CEF6C27EE5F0F8
        :2006FD00B4000578CFF6C27F22752FFFC340057537A8C278D350037537A8D2002000037567
        :20071D0037003000057538A9C27910000375380074AA700375380074006003753800752B9D
        :20073D0000B52B037539AA746FB46F05753AABC27A747F7903B90103753A007820752007B1
        :20075D00B60705753BACC27B752B01D52B05753CADC27CF180753EAF7801D805753FB0C290
        :20077D007DE194740290078673E18BE18E00753C00753DAEC27E2200C27F22C000C0D075EE
        :20079D00D00078297601D0D0D00032C0E0C007C000C0D075D000309816782C7600782CE634
        :2007BD00C454F0FF782BE62F782FF6C28EC2ACC298C299D0D0D000D007D0E032C0E0C001C3
        :2007DD00C000C0D075D000C2CFC2CEE52D2460F8A62D00782D792FE6F7782DE67006C2CA2E
        :2007FD00C2AD8003782D16D0D0D000D001D0E03278F0760078F0B6FA00500800000078F056
        :20081D000680F1227581D075800F75900075A2FF7591FF75A10778FF74000075880075A915
        :20083D000475A880782976007829B601FB7829760078287601782886907828B60F0050E80F
        :20085D007828B6010A782E760212009D0209267828B6020A782E7632120138020926782850
        :20087D00B6030A782E76321201580209267828B6040A782E763212017B0209267828B605E2
        :20089D000A782E76321201950209267828B6060A782E76321201CD0209267828B6070A7866
        :2008BD002E76321201FF0209267828B60809782E760212022880527828B60909782E7602E9
        :2008DD0012031C80447828B60A09782E76021203AF80367828B60B09782E760212070680DE
        :2008FD00287828B60C09782E760212050A801A7828B60D09782E760212063E800C7828B6AD
        :20091D000E07782E76021206A2782A7601782A792EC3E796401D12080D75800E12080D7508
        :20093D00800F12080D75800D12080D75800F782A0680DA12080D782FE6700A782806782841
        :14095D0086900208567828743026F5907828760F020856227A
        :06007000E478FFF6D8FD64
        :20004E007900E94400601B7A00900975780075A000E493F2A308B8000205A0D9F4DAF275DB
        :02006E00A0FFF1
        :200076007800E84400600A790075A000E4F309D8FC7800E84400600C7900900000E4F0A38A
        :04009600D8FCD9FABF
        :0D004100758120120971E582600302003E06
        :040971007582002269
        :00000001FF
        """    
    
