LMS7002_REGDESC_MR3="""

REGBANK uC 0x000X 1
REGBANK LimeLight 0b00000000001XXXXX 1
REGBANK TopControl 0b000000001XXXXXXX 1
REGBANK TRX 0b000000010XXXXXXX 2
REGBANK TXTSP 0b00000010000XXXXX 2
REGBANK TXNCO 0b0000001001XXXXXX 2
REGBANK TXGFIR1 0b0000001010XXXXXX 2
REGBANK TXGFIR2 0b0000001011XXXXXX 2
REGBANK TXGFIR3a 0b0000001100XXXXXX 2
REGBANK TXGFIR3b 0b0000001101XXXXXX 2
REGBANK TXGFIR3c 0b0000001110XXXXXX 2
REGBANK RXTSP 0b00000100000XXXXX 2
REGBANK RXNCO 0b0000010001XXXXXX 2
REGBANK RXGFIR1 0b0000010010XXXXXX 2
REGBANK RXGFIR2 0b0000010011XXXXXX 2
REGBANK RXGFIR3a 0b0000010100XXXXXX 2
REGBANK RXGFIR3b 0b0000010101XXXXXX 2
REGBANK RXGFIR3c 0b0000010110XXXXXX 2
REGBANK DCCalibration 0b00000101110XXXXX 1
REGBANK RPT_Config 0b00000110000XXXXX 1
REGBANK RSSI_DCCAL 0b00000110010XXXXX 2
REGISTER    mSPI_P0    0x0000
    BITFIELD   P0<7:0>
        POSITION=<7:0>
        DEFAULT=00000000
        MODE=RW
        #! The data at MCU port P0 input can be changed by writing data into this register
    ENDBITFIELD
ENDREGISTER

REGISTER    mSPI_P1    0x0001
    BITFIELD   P1<7:0>
        POSITION=<7:0>
        DEFAULT=00000000
        MODE=RW
        #! The content of MCU P1 port output can be obtained by reading this register
    ENDBITFIELD
ENDREGISTER

REGISTER    mSPI_CFG    0x0002
    BITFIELD   RXD
        POSITION=7
        DEFAULT=0
        MODE=RW
        #! The MCU USART receive input pin
    ENDBITFIELD
    BITFIELD   DEBUG
        POSITION=6
        DEFAULT=0
        MODE=RW
        #! Enables hardware MCU debugging mode
        #!     0 - normal mode
        #!     1 - debug mode
    ENDBITFIELD
    BITFIELD   EXT_INT<5:2>
        POSITION=<5:2>
        DEFAULT=0000
        MODE=RW
        #! External interrupts
    ENDBITFIELD
    BITFIELD   MODE<1:0>
        POSITION=<1:0>
        DEFAULT=00
        MODE=RW
        #! controls MCU program memory initialization modes:
        #!     0 - the MCU is in reset
        #!     1 - Programming both EEPROM and SRAM through mSPI
        #!     2 - Programming only SRAM only through mSPI
        #!     3 - Programming SRAM by reading the EEPROM
    ENDBITFIELD
ENDREGISTER

REGISTER    mSPI_STAT    0x0003
    BITFIELD   TXD
        POSITION=7
        DEFAULT=0
        MODE=RW
        #! The USART transmit output pin
    ENDBITFIELD
    BITFIELD   PROGRAMMED
        POSITION=6
        DEFAULT=0
        MODE=R
        #! Status output signal; when is set, it indicates that programming
        #! signals (mSPI_REG3) process is finished, and MCU executes instructions (read only)
    ENDBITFIELD
    BITFIELD   READ_REQ
        POSITION=3
        DEFAULT=0
        MODE=RW
        #! Status signal; new 8-bit data (the register mSPI_REG5 content) is  ready to be read through mSPI
    ENDBITFIELD
    BITFIELD   WRITE_REQ
        POSITION=2
        DEFAULT=0
        MODE=RW
        #! Status signal; a new data byte is waiting in the mSPI_REG4 register to be transferred into MCU
    ENDBITFIELD
    BITFIELD   FULL_WRITE_BUFF
        POSITION=1
        DEFAULT=0
        MODE=RW
        #! indicates that INPUT 32-byte FIFO buffer is full, the MCU is  not ready to receive data, and base band processor has to wait
    ENDBITFIELD
    BITFIELD   EMPTY_WRITE_BUFF
        POSITION=0
        DEFAULT=0
        MODE=RW
        #! Tells that INPUT 32-byte FIFO is empty
    ENDBITFIELD
ENDREGISTER

REGISTER    mSPI_DTM    0x0004
    BITFIELD   DTM<7:0>
        POSITION=<7:0>
        DEFAULT=00000000
        MODE=RW
        #! output (byte) is fed to Data_to_MCU<7:0> input bus
    ENDBITFIELD
ENDREGISTER

REGISTER    mSPI_DFM    0x0005
    BITFIELD   DFM<7:0>
        POSITION=<7:0>
        DEFAULT=00000000
        MODE=RW
        #! data (byte) received from bus Data_from_MCU<7:0>
    ENDBITFIELD
ENDREGISTER

REGISTER    mSPI_SPISW    0x0006
    BITFIELD   SPISW_CTRL
        POSITION=0
        DEFAULT=0
        MODE=RW
        #! Controls the SPI switch
        #!     0 - Transceiver is controlled by Base Band (default)
        #!     1 - Transceiver is controlled by MCU
    ENDBITFIELD
ENDREGISTER

REGISTER    CHIPCFG    0x0020
    BITFIELD   LRST_TX_B
        POSITION=15
        DEFAULT=1
        MODE=RW
        #! Resets all the logic registers to the default state for Tx MIMO channel
        #! B.
        #!     0 - Reset active
        #!     1 - Reset inactive (default)
    ENDBITFIELD
    BITFIELD   MRST_TX_B
        POSITION=14
        DEFAULT=1
        MODE=RW
        #! Resets all the configuration memory to the default state for Tx MIMO
        #! channel B.
        #!     0 - Reset active
        #!     1 - Reset inactive (default)
    ENDBITFIELD
    BITFIELD   LRST_TX_A
        POSITION=13
        DEFAULT=1
        MODE=RW
        #! Resets all the logic registers to the default state for Tx MIMO channel
        #! A.
        #!     0 - Reset active
        #!     1 - Reset inactive (default)
    ENDBITFIELD
    BITFIELD   MRST_TX_A
        POSITION=12
        DEFAULT=1
        MODE=RW
        #! Resets all the configuration memory to the default state for Tx MIMO
        #! channel A.
        #!     0 - Reset active
        #!     1 - Reset inactive (default)
    ENDBITFIELD
    BITFIELD   LRST_RX_B
        POSITION=11
        DEFAULT=1
        MODE=RW
        #! Resets all the logic registers to the default state for Rx MIMO channel
        #! B.
        #!     0 - Reset active
        #!     1 - Reset inactive (default)
    ENDBITFIELD
    BITFIELD   MRST_RX_B
        POSITION=10
        DEFAULT=1
        MODE=RW
        #! Resets all the configuration memory to the default state for Rx MIMO
        #! channel B.
        #!     0 - Reset active
        #!     1 - Reset inactive (default)
    ENDBITFIELD
    BITFIELD   LRST_RX_A
        POSITION=9
        DEFAULT=1
        MODE=RW
        #! Resets all the logic registers to the default state for Rx MIMO channel
        #! A.
        #!     0 - Reset active
        #!     1 - Reset inactive (default)
    ENDBITFIELD
    BITFIELD   MRST_RX_A
        POSITION=8
        DEFAULT=1
        MODE=RW
        #! Resets all the configuration memory to the default state for Rx MIMO
        #! channel A.
        #!     0 - Reset active
        #!     1 - Reset inactive (default)
    ENDBITFIELD
    BITFIELD   SRST_RXFIFO
        POSITION=7
        DEFAULT=1
        MODE=RW
        #! RX FIFO soft reset (LimeLightTM Interface).
        #!     0 - Reset active
        #!     1 - Reset inactive (default)
    ENDBITFIELD
    BITFIELD   SRST_TXFIFO
        POSITION=6
        DEFAULT=1
        MODE=RW
        #! TX FIFO soft reset (LimeLightTM Interface).
        #!     0 - Reset active
        #!     1 - Reset inactive (default)
    ENDBITFIELD
    BITFIELD   RXEN_B
        POSITION=5
        DEFAULT=1
        MODE=RW
        #! Power control for Rx MIMO channel B.
        #!     0 - Rx MIMO channel B powered down
        #!     1 - Rx MIMO channel B enabled (default)
    ENDBITFIELD
    BITFIELD   RXEN_A
        POSITION=4
        DEFAULT=1
        MODE=RW
        #! Power control for Rx MIMO channel A.
        #!     0 - Rx MIMO channel A powered down
        #!     1 - Rx MIMO channel A enabled (default)
    ENDBITFIELD
    BITFIELD   TXEN_B
        POSITION=3
        DEFAULT=1
        MODE=RW
        #! Power control for Tx MIMO channel B.
        #!     0 - Tx MIMO channel B powered down
        #!     1 - Tx MIMO channel B enabled (default)
    ENDBITFIELD
    BITFIELD   TXEN_A
        POSITION=2
        DEFAULT=1
        MODE=RW
        #! Power control for Tx MIMO channel A.
        #!     0 - Tx MIMO channel A powered down
        #!     1 - Tx MIMO channel A enabled (default)
    ENDBITFIELD
    BITFIELD   MAC<1:0>
        POSITION=<1:0>
        DEFAULT=11
        MODE=RW
        #! MIMO access control.
        #!     11 - Channels A and B accessible. SPI write operation only (default)
        #!     01 - Channel A accessible only. Valid for SPI read/write
        #!     10 - Channel B accessible only. Valid for SPI read/write
    ENDBITFIELD
ENDREGISTER

REGISTER    IOCFG0    0x0021
    BITFIELD   TX_CLK_PE
        POSITION=11
        DEFAULT=1
        MODE=RW
        #! Pull up control of TX_CLK pad.
        #!     0 - Pull up disengaged
        #!     1 - Pull up engaged (default)
    ENDBITFIELD
    BITFIELD   RX_CLK_PE
        POSITION=10
        DEFAULT=1
        MODE=RW
        #! Pull up control of RX_CLK pad.
        #!     0 - Pull up disengaged
        #!     1 - Pull up engaged (default)
    ENDBITFIELD
    BITFIELD   SDA_PE
        POSITION=9
        DEFAULT=1
        MODE=RW
        #! Pull up control of SDA pad.
        #!     0 - Pull up disengaged
        #!     1 - Pull up engaged (default)
    ENDBITFIELD
    BITFIELD   SDA_DS
        POSITION=8
        DEFAULT=0
        MODE=RW
        #! Driver strength of SDA pad.
        #!     0 - Driver strength is 4mA (default)
        #!     1 - Driver strength is 8mA
    ENDBITFIELD
    BITFIELD   SCL_PE
        POSITION=7
        DEFAULT=1
        MODE=RW
        #! Pull up control of SCL pad.
        #!     0 - Pull up disengaged
        #!     1 - Pull up engaged (default)
    ENDBITFIELD
    BITFIELD   SCL_DS
        POSITION=6
        DEFAULT=0
        MODE=RW
        #! Driver strength of SCL pad.
        #!     0 - Driver strength is 4mA (default)
        #!     1 - Driver strength is 8mA
    ENDBITFIELD
    BITFIELD   SDIO_DS
        POSITION=5
        DEFAULT=0
        MODE=RW
        #! Driver strength of SDIO pad.
        #!     0 - Driver strength is 4mA (default)
        #!     1 - Driver strength is 8mA
    ENDBITFIELD
    BITFIELD   SDIO_PE
        POSITION=4
        DEFAULT=1
        MODE=RW
        #! Pull up control of SDIO pad.
        #!     0 - Pull up disengaged
        #!     1 - Pull up engaged (default)
    ENDBITFIELD
    BITFIELD   SDO_PE
        POSITION=3
        DEFAULT=1
        MODE=RW
        #! Pull up control of SDO pad.
        #!     0 - Pull up disengaged
        #!     1 - Pull up engaged (default)
    ENDBITFIELD
    BITFIELD   SCLK_PE
        POSITION=2
        DEFAULT=1
        MODE=RW
        #! Pull up control of SCLK pad.
        #!     0 - Pull up disengaged
        #!     1 - Pull up engaged (default)
    ENDBITFIELD
    BITFIELD   SEN_PE
        POSITION=1
        DEFAULT=1
        MODE=RW
        #! Pull up control of SEN pad.
        #!     0 - Pull up disengaged
        #!     1 - Pull up engaged (default)
    ENDBITFIELD
    BITFIELD   SPIMODE
        POSITION=0
        DEFAULT=1
        MODE=RW
        #! SPI communication mode.
        #!     0 - 3 wire mode
        #!     1 - 4 wire mode (default)
    ENDBITFIELD
ENDREGISTER

REGISTER    IOCFG1    0x0022
    BITFIELD   LML2_TRXIQPULSE
        POSITION=15
        DEFAULT=0
        MODE=RW
        #! TRXIQPULSE mode selection for LML Port 2.
        #!     0 - TRXIQPULSE mode off (default)
        #!     1 - TRXIQPULSE mode on
    ENDBITFIELD
    BITFIELD   LML2_SISODDR
        POSITION=14
        DEFAULT=0
        MODE=RW
        #! SISODDR mode selection for LML Port 2.
        #!     0 - SISODDR mode off (default)
        #!     1 - SISODDR mode on
    ENDBITFIELD
    BITFIELD   LML1_TRXIQPULSE
        POSITION=13
        DEFAULT=0
        MODE=RW
        #! TRXIQPULSE mode selection for LML Port 1.
        #!     0 - TRXIQPULSE mode off (default)
        #!     1 - TRXIQPULSE mode on
    ENDBITFIELD
    BITFIELD   LML1_SISODDR
        POSITION=12
        DEFAULT=0
        MODE=RW
        #! SISODDR mode selection for LML Port 1.
        #!     0 - SISODDR mode off (default)
        #!     1 - SISODDR mode on
    ENDBITFIELD
    BITFIELD   DIQ2_DS
        POSITION=11
        DEFAULT=0
        MODE=RW
        #! Driver strength of DIQ2 pad.
        #!     0 - Driver strength is 4mA (default)
        #!     1 - Driver strength is 8mA
    ENDBITFIELD
    BITFIELD   DIQ2_PE
        POSITION=10
        DEFAULT=1
        MODE=RW
        #! Pull up control of DIQ2 pad.
        #!     0 - Pull up disengaged
        #!     1 - Pull up engaged (default)
    ENDBITFIELD
    BITFIELD   IQ_SEL_EN_2_PE
        POSITION=9
        DEFAULT=1
        MODE=RW
        #! Pull up control of IQ_SEL_EN_2 pad.
        #!     0 - Pull up disengaged
        #!     1 - Pull up engaged (default)
    ENDBITFIELD
    BITFIELD   TXNRX2_PE
        POSITION=8
        DEFAULT=1
        MODE=RW
        #! Pull up control of TXNRX2 pad.
        #!     0 - Pull up disengaged
        #!     1 - Pull up engaged (default)
    ENDBITFIELD
    BITFIELD   FCLK2_PE
        POSITION=7
        DEFAULT=1
        MODE=RW
        #! Pull up control of FCLK2 pad.
        #!     0 - Pull up disengaged
        #!     1 - Pull up engaged (default)
    ENDBITFIELD
    BITFIELD   MCLK2_PE
        POSITION=6
        DEFAULT=1
        MODE=RW
        #! Pull up control of MCLK2 pad.
        #!     0 - Pull up disengaged
        #!     1 - Pull up engaged (default)
    ENDBITFIELD
    BITFIELD   DIQ1_DS
        POSITION=5
        DEFAULT=0
        MODE=RW
        #! Driver strength of DIQ1 pad.
        #!     0 - Driver strength is 4mA (default)
        #!     1 - Driver strength is 8mA
    ENDBITFIELD
    BITFIELD   DIQ1_PE
        POSITION=4
        DEFAULT=1
        MODE=RW
        #! Pull up control of DIQ1 pad.
        #!     0 - Pull up disengaged
        #!     1 - Pull up engaged (default)
    ENDBITFIELD
    BITFIELD   IQ_SEL_EN_1_PE
        POSITION=3
        DEFAULT=1
        MODE=RW
        #! Pull up control of IQ_SEL_EN_1 pad.
        #!     0 - Pull up disengaged
        #!     1 - Pull up engaged (default)
    ENDBITFIELD
    BITFIELD   TXNRX1_PE
        POSITION=2
        DEFAULT=1
        MODE=RW
        #! Pull up control of TXNRX1 pad.
        #!     0 - Pull up disengaged
        #!     1 - Pull up engaged (default)
    ENDBITFIELD
    BITFIELD   FCLK1_PE
        POSITION=1
        DEFAULT=1
        MODE=RW
        #! Pull up control of FCLK1 pad.
        #!     0 - Pull up disengaged
        #!     1 - Pull up engaged (default)
    ENDBITFIELD
    BITFIELD   MCLK1_PE
        POSITION=0
        DEFAULT=1
        MODE=RW
        #! Pull up control of MCLK1 pad.
        #!     0 - Pull up disengaged
        #!     1 - Pull up engaged (default)
    ENDBITFIELD
ENDREGISTER

REGISTER    LimeLight_IOCFG    0x0023
    BITFIELD   DIQDIRCTR2
        POSITION=15
        DEFAULT=0
        MODE=RW
        #! DIQ2 direction control mode.
        #!     0 - Automatic (default)
        #!     1 - Manual, controllable from DIQDIR2
    ENDBITFIELD
    BITFIELD   DIQDIR2
        POSITION=14
        DEFAULT=1
        MODE=RW
        #! DIQ2 direction.
        #!     0 - Output
        #!     1 - Input (default)
    ENDBITFIELD
    BITFIELD   DIQDIRCTR1
        POSITION=13
        DEFAULT=0
        MODE=RW
        #! DIQ1 direction control mode.
        #!     0 - Automatic (default)
        #!     1 - Manual, controllable from DIQDIR1
    ENDBITFIELD
    BITFIELD   DIQDIR1
        POSITION=12
        DEFAULT=1
        MODE=RW
        #! DIQ1 direction.
        #!     0 - Output
        #!     1 - Input (default)
    ENDBITFIELD
    BITFIELD   ENABLEDIRCTR2
        POSITION=11
        DEFAULT=0
        MODE=RW
        #! ENABLE2 direction control mode.
        #!     0 - Automatic (default)
        #!     1 - Manual, controllable from ENABLEDIR2
    ENDBITFIELD
    BITFIELD   ENABLEDIR2
        POSITION=10
        DEFAULT=1
        MODE=RW
        #! ENABLE2 direction.
        #!     0 - Output
        #!     1 - Input (default)
    ENDBITFIELD
    BITFIELD   ENABLEDIRCTR1
        POSITION=9
        DEFAULT=0
        MODE=RW
        #! ENABLE1 direction control mode.
        #!     0 - Automatic (default)
        #!     1 - Manual, controllable from ENABLEDIR1
    ENDBITFIELD
    BITFIELD   ENABLEDIR1
        POSITION=8
        DEFAULT=1
        MODE=RW
        #! ENABLE1 direction.
        #!     0 - Output
        #!     1 - Input (default)
    ENDBITFIELD
    BITFIELD   MOD_EN
        POSITION=6
        DEFAULT=1
        MODE=RW
        #! LimeLightTM interface enable.
        #!     0 - Interface disabled
        #!     1 - Interface enabled (default)
    ENDBITFIELD
    BITFIELD   LML2_FIDM
        POSITION=5
        DEFAULT=0
        MODE=RW
        #! Frame start ID selection for Port 2, when LML_MODE2 = 0.
        #!     0 - Frame start, when 0 (default)
        #!     1 - Frame start, when 1
    ENDBITFIELD
    BITFIELD   LML2_TXNRXIQ
        POSITION=4
        DEFAULT=1
        MODE=RW
        #! TXIQ/RXIQ mode selection for Port 2, when LML_MODE2 = 0.
        #!     0 - RXIQ mode
        #!     1 - TXIQ mode (default)
    ENDBITFIELD
    BITFIELD   LML2_MODE
        POSITION=3
        DEFAULT=1
        MODE=RW
        #! Mode of LimeLightTM Port 2.
        #!     0 - TRXIQ mode
        #!     1 - JESD207 mode (default)
    ENDBITFIELD
    BITFIELD   LML1_FIDM
        POSITION=2
        DEFAULT=0
        MODE=RW
        #! Frame start ID selection for Port 1, when LML_MODE1 = 0.
        #!     0 - Frame start, when 0 (default)
        #!     1 - Frame start, when 1
    ENDBITFIELD
    BITFIELD   LML1_TXNRXIQ
        POSITION=1
        DEFAULT=0
        MODE=RW
        #! TXIQ/RXIQ mode selection for Port 1, when LML_MODE1 = 0.
        #!     0 - RXIQ mode (default)
        #!     1 - TXIQ mode
    ENDBITFIELD
    BITFIELD   LML1_MODE
        POSITION=0
        DEFAULT=1
        MODE=RW
        #! Mode of LimeLightTM Port 1.
        #!     0 - TRXIQ mode
        #!     1 - JESD207 mode (default)
    ENDBITFIELD
ENDREGISTER

REGISTER    LimeLight_POS1    0x0024
    BITFIELD   LML1_S3S<1:0>
        POSITION=<15:14>
        DEFAULT=11
        MODE=RW
        #! Sample source in position 3, when direction of Port 1 is RF2BB.
        #!     11 - Sample in frame position 0 is BQ (default)
        #!     10 - Sample in frame position 0 is BI
        #!     01 - Sample in frame position 0 is AQ
        #!     00 - Sample in frame position 0 is AI
    ENDBITFIELD
    BITFIELD   LML1_S2S<1:0>
        POSITION=<13:12>
        DEFAULT=10
        MODE=RW
        #! Sample source in position 2, when direction of Port 1 is RF2BB.
        #!     11 - Sample in frame position 0 is BQ
        #!     10 - Sample in frame position 0 is BI (default)
        #!     01 - Sample in frame position 0 is AQ
        #!     00 - Sample in frame position 0 is AI
    ENDBITFIELD
    BITFIELD   LML1_S1S<1:0>
        POSITION=<11:10>
        DEFAULT=01
        MODE=RW
        #! Sample source in position 1, when direction of Port 1 is RF2BB.
        #!     11 - Sample in frame position 0 is BQ
        #!     10 - Sample in frame position 0 is BI
        #!     01 - Sample in frame position 0 is AQ (default)
        #!     00 - Sample in frame position 0 is AI
    ENDBITFIELD
    BITFIELD   LML1_S0S<1:0>
        POSITION=<9:8>
        DEFAULT=00
        MODE=RW
        #! Sample source in position 0, when direction of Port 1 is RF2BB.
        #!     11 - Sample in frame position 0 is BQ
        #!     10 - Sample in frame position 0 is BI
        #!     01 - Sample in frame position 0 is AQ
        #!     00 - Sample in frame position 0 is AI (default)
    ENDBITFIELD
    BITFIELD   LML1_BQP<1:0>
        POSITION=<7:6>
        DEFAULT=11
        MODE=RW
        #! BQ sample position in frame, when direction of Port 1 is BB2RF.
        #!     11 - BQ sample position is 3 (default)
        #!     10 - BQ sample position is 2
        #!     01 - BQ sample position is 1
        #!     00 - BQ sample position is 0
    ENDBITFIELD
    BITFIELD   LML1_BIP<1:0>
        POSITION=<5:4>
        DEFAULT=10
        MODE=RW
        #! BI sample position in frame, when direction of Port 1 is BB2RF.
        #!     11 - BI sample position is 3
        #!     10 - BI sample position is 2 (default)
        #!     01 - BI sample position is 1
        #!     00 - BI sample position is 0
    ENDBITFIELD
    BITFIELD   LML1_AQP<1:0>
        POSITION=<3:2>
        DEFAULT=01
        MODE=RW
        #! AQ sample position in frame, when direction of Port 1 is BB2RF.
        #!     11 - AQ sample position is 3
        #!     10 - AQ sample position is 2
        #!     01 - AQ sample position is 1 (default)
        #!     00 - AQ sample position is 0
    ENDBITFIELD
    BITFIELD   LML1_AIP<1:0>
        POSITION=<1:0>
        DEFAULT=00
        MODE=RW
        #! AI sample position in frame, when direction of Port 1 is BB2RF.
        #!     11 - AI sample position is 3
        #!     10 - AI sample position is 2
        #!     01 - AI sample position is 1
        #!     00 - AI sample position is 0 (default)
    ENDBITFIELD
ENDREGISTER

REGISTER    LimeLight_BBRF1    0x0025
    BITFIELD   LML1_BB2RF_PST<4:0>
        POSITION=<12:8>
        DEFAULT=00001
        MODE=RW
        #! Number of clock cycles to wait after burst stop is detected
        #! in JESD207 mode on Port 1 and direction of Port 1 is BB2RF. Unsigned integer.
        #! Possible values are 0 - 31, default is 1.
    ENDBITFIELD
    BITFIELD   LML1_BB2RF_PRE<4:0>
        POSITION=<4:0>
        DEFAULT=00001
        MODE=RW
        #! Number of clock cycles to wait after burst start is detected
        #! in JESD207 mode on Port 1 and direction of Port 1 is BB2RF. Unsigned integer.
        #! Possible values are 0 - 31, default is 1.
    ENDBITFIELD
ENDREGISTER

REGISTER    LimeLight_RFBB1    0x0026
    BITFIELD   LML1_RF2BB_PST<4:0>
        POSITION=<12:8>
        DEFAULT=00001
        MODE=RW
        #! Number of clock cycles to wait after burst stop is detected
        #! in JESD207 mode on Port 1 and direction of Port 1 is RF2BB. Unsigned integer.
        #! Possible values are 0 - 31, default is 1.
    ENDBITFIELD
    BITFIELD   LML1_RF2BB_PRE<4:0>
        POSITION=<4:0>
        DEFAULT=00001
        MODE=RW
        #! Number of clock cycles to after burst start is detected in
        #! JESD207 mode on Port 1 and direction of Port 1 is RF2BB. Unsigned integer.
        #! Possible values are 0 - 31, default is 1.
    ENDBITFIELD
ENDREGISTER

REGISTER    LimeLight_POS2    0x0027
    BITFIELD   LML2_S3S<1:0>
        POSITION=<15:14>
        DEFAULT=11
        MODE=RW
        #! Sample source in position 3, when direction of Port 2 is RF2BB.
        #!     11 - Sample in frame position 0 is BQ (default)
        #!     10 - Sample in frame position 0 is BI
        #!     01 - Sample in frame position 0 is AQ
        #!     00 - Sample in frame position 0 is AI
    ENDBITFIELD
    BITFIELD   LML2_S2S<1:0>
        POSITION=<13:12>
        DEFAULT=10
        MODE=RW
        #! Sample source in position 2, when direction of Port 2 is RF2BB.
        #!     11 - Sample in frame position 0 is BQ
        #!     10 - Sample in frame position 0 is BI (default)
        #!     01 - Sample in frame position 0 is AQ
        #!     00 - Sample in frame position 0 is AI
    ENDBITFIELD
    BITFIELD   LML2_S1S<1:0>
        POSITION=<11:10>
        DEFAULT=01
        MODE=RW
        #! Sample source in position 1, when direction of Port 2 is RF2BB.
        #!     11 - Sample in frame position 0 is BQ
        #!     10 - Sample in frame position 0 is BI
        #!     01 - Sample in frame position 0 is AQ (default)
        #!     00 - Sample in frame position 0 is AI
    ENDBITFIELD
    BITFIELD   LML2_S0S<1:0>
        POSITION=<9:8>
        DEFAULT=00
        MODE=RW
        #! Sample source in position 0, when direction of Port 2 is RF2BB.
        #!     11 - Sample in frame position 0 is BQ
        #!     10 - Sample in frame position 0 is BI
        #!     01 - Sample in frame position 0 is AQ
        #!     00 - Sample in frame position 0 is AI (default)
    ENDBITFIELD
    BITFIELD   LML2_BQP<1:0>
        POSITION=<7:6>
        DEFAULT=11
        MODE=RW
        #! BQ sample position in frame, when direction of Port 2 is BB2RF.
        #!     11 - BQ sample position is 3 (default)
        #!     10 - BQ sample position is 2
        #!     01 - BQ sample position is 1
        #!     00 - BQ sample position is 0
    ENDBITFIELD
    BITFIELD   LML2_BIP<1:0>
        POSITION=<5:4>
        DEFAULT=10
        MODE=RW
        #! BI sample position in frame, when direction of Port 2 is BB2RF.
        #!     11 - BI sample position is 3
        #!     10 - BI sample position is 2 (default)
        #!     01 - BI sample position is 1
        #!     00 - BI sample position is 0
    ENDBITFIELD
    BITFIELD   LML2_AQP<1:0>
        POSITION=<3:2>
        DEFAULT=01
        MODE=RW
        #! AQ sample position in frame, when direction of Port 2 is BB2RF.
        #!     11 - AQ sample position is 3
        #!     10 - AQ sample position is 2
        #!     01 - AQ sample position is 1 (default)
        #!     00 - AQ sample position is 0
    ENDBITFIELD
    BITFIELD   LML2_AIP<1:0>
        POSITION=<1:0>
        DEFAULT=00
        MODE=RW
        #! AI sample position in frame, when direction of Port 2 is BB2RF.
        #!     11 - AI sample position is 3
        #!     10 - AI sample position is 2
        #!     01 - AI sample position is 1
        #!     00 - AI sample position is 0 (default)
    ENDBITFIELD
ENDREGISTER

REGISTER    LimeLight_BBRF2    0x0028
    BITFIELD   LML2_BB2RF_PST<4:0>
        POSITION=<12:8>
        DEFAULT=00001
        MODE=RW
        #! Number of clock cycles to wait after burst stop is detected
        #! in JESD207 mode on Port 2 and direction of Port 2 is BB2RF. Unsigned integer.
        #! Possible values are 0 - 31, default is 1.
    ENDBITFIELD
    BITFIELD   LML2_RF2BB_PRE<4:0>
        POSITION=<4:0>
        DEFAULT=00001
        MODE=RW
        #! Number of clock cycles to wait after burst start is detected
        #! in JESD207 mode on Port 2 and direction of Port 2 is RF2BB. Unsigned integer.
        #! Possible values are 0 - 31, default is 1.
    ENDBITFIELD
ENDREGISTER

REGISTER    LimeLight_RFBB2    0x0029
    BITFIELD   LML2_RF2BB_PST<4:0>
        POSITION=<12:8>
        DEFAULT=00001
        MODE=RW
        #! Number of clock cycles to wait after burst stop is detected
        #! in JESD207 mode on Port 2 and direction of Port 2 is RF2BB. Unsigned integer.
        #! Possible values are 0 - 31, default is 1.
    ENDBITFIELD
    BITFIELD   LML2_RF2BB_PRE<4:0>
        POSITION=<4:0>
        DEFAULT=00001
        MODE=RW
        #! Number of clock cycles to wait after burst start is detected
        #! in JESD207 mode on Port 2 and direction of Port 2 is RF2BB. Unsigned integer.
        #! Possible values are 0 - 31, default is 1.
    ENDBITFIELD
ENDREGISTER

REGISTER    LimeLight_CLKSRC    0x002A
    BITFIELD   FCLK2_DLY<1:0>
        POSITION=<15:14>
        DEFAULT=00
        MODE=RW
        #! FCLK2 clock internal delay.
        #!     11 - 3x delay
        #!     10 - 2x delay
        #!     01 - 1x delay
        #!     00 - No delay (default)
    ENDBITFIELD
    BITFIELD   FCLK1_DLY<1:0>
        POSITION=<13:12>
        DEFAULT=00
        MODE=RW
        #! FCLK2 clock internal delay.
        #!     11 - 3x delay
        #!     10 - 2x delay
        #!     01 - 1x delay
        #!     00 - No delay (default)
    ENDBITFIELD
    BITFIELD   RX_MUX<1:0>
        POSITION=<11:10>
        DEFAULT=00
        MODE=RW
        #! RxFIFO data source selection.
        #!     00 - RxTSPCLK (default)
        #!     01 - TxFIFO
        #!     10, 11 - LFSR
    ENDBITFIELD
    BITFIELD   TX_MUX<1:0>
        POSITION=<9:8>
        DEFAULT=00
        MODE=RW
        #! Port selection for data transmit to TSP.
        #!     10, 11 - Data source is RxTSP
        #!     01 - Data source is Port 2
        #!     00 - Data source is Port 1 (default)
    ENDBITFIELD
    BITFIELD   TXRDCLK_MUX<1:0>
        POSITION=<7:6>
        DEFAULT=10
        MODE=RW
        #! TX FIFO read clock selection.
        #!     10, 11 - Clock source is TxTSPCLK (default)
        #!     01 - Clock source is FCLK2
        #!     00 - Clock source is FCLK1
    ENDBITFIELD
    BITFIELD   TXWRCLK_MUX<1:0>
        POSITION=<5:4>
        DEFAULT=00
        MODE=RW
        #! TX FIFO write clock selection.
        #!     10, 11 - Clock source is RxTSPCLK (use for TSP loop back)
        #!     01 - Clock source is FCLK2
        #!     00 - Clock source is FCLK1 (default)
    ENDBITFIELD
    BITFIELD   RXRDCLK_MUX<1:0>
        POSITION=<3:2>
        DEFAULT=01
        MODE=RW
        #! RX FIFO read clock selection.
        #!     11 - Clock source is FCLK2
        #!     10 - Clock source is FCLK1
        #!     01 - Clock source is MCLK2 (default)
        #!     00 - Clock source is MCLK1
    ENDBITFIELD
    BITFIELD   RXWRCLK_MUX<1:0>
        POSITION=<1:0>
        DEFAULT=10
        MODE=RW
        #! RX FIFO write clock selection.
        #!     10, 11 - Clock source is RxTSPCLK (default)
        #!     01 - Clock source is FCLK2
        #!     00 - Clock source is FCLK1
    ENDBITFIELD
ENDREGISTER

REGISTER    LimeLight_CLKCFG    0x002B
    BITFIELD   FCLK2_INV
        POSITION=15
        DEFAULT=0
        MODE=RW
        #! FCLK2 clock inversion.
        #!     1 - Inverted
        #!     0 - Not inverted (default)
    ENDBITFIELD
    BITFIELD   FCLK1_INV
        POSITION=14
        DEFAULT=0
        MODE=RW
        #! FCLK1 clock inversion.
        #!     1 - Inverted
        #!     0 - Not inverted (default)
    ENDBITFIELD
    BITFIELD   MCLK2_DLY<1:0>
        POSITION=<13:12>
        DEFAULT=00
        MODE=RW
        #! MCLK2 clock internal delay.
        #!     11 - 3x delay
        #!     10 - 2x delay
        #!     01 - 1x delay
        #!     00 - No delay (default)
    ENDBITFIELD
    BITFIELD   MCLK1_DLY<1:0>
        POSITION=<11:10>
        DEFAULT=00
        MODE=RW
        #! MCLK2 clock internal delay.
        #!     11 - 3x delay
        #!     10 - 2x delay
        #!     01 - 1x delay
        #!     00 - No delay (default)
    ENDBITFIELD
    BITFIELD   MCLK2_INV
        POSITION=9
        DEFAULT=0
        MODE=RW
        #! MCLK2 clock inversion.
        #!     1 - Inverted
        #!     0 - Not inverted (default)
    ENDBITFIELD
    BITFIELD   MCLK1_INV
        POSITION=8
        DEFAULT=0
        MODE=RW
        #! MCLK1 clock inversion.
        #!     1 - Inverted
        #!     0 - Not inverted (default)
    ENDBITFIELD
    BITFIELD   MCLK2SRC<1:0>
        POSITION=<5:4>
        DEFAULT=01
        MODE=RW
        #! MCLK2 clock source.
        #!     11 - RxTSPCLKA
        #!     10 - TxTSPCLKA
        #!     01 - RxTSPCLKA after divider (default)
        #!     00 - TxTSPCLKA after divider
    ENDBITFIELD
    BITFIELD   MCLK1SRC<1:0>
        POSITION=<3:2>
        DEFAULT=00
        MODE=RW
        #! MCLK1 clock source.
        #!     11 - RxTSPCLKA
        #!     10 - TxTSPCLKA
        #!     01 - RxTSPCLKA after divider
        #!     00 - TxTSPCLKA after divider (default)
    ENDBITFIELD
    BITFIELD   TXDIVEN
        POSITION=1
        DEFAULT=0
        MODE=RW
        #! TX clock divider enable.
        #!     1 - Divider enabled
        #!     0 - Divider disabled (default)
    ENDBITFIELD
    BITFIELD   RXDIVEN
        POSITION=0
        DEFAULT=0
        MODE=RW
        #! RX clock divider enable.
        #!     1 - Divider enabled
        #!     0 - Divider disabled (default)
    ENDBITFIELD
ENDREGISTER

REGISTER    TSPCFG    0x002C
    BITFIELD   TXTSPCLKA_DIV<7:0>
        POSITION=<15:8>
        DEFAULT=11111111
        MODE=RW
        #! TxTSP clock divider, used to produce MCLK(1/2) clocks.
        #! Clock division ratio is 2(TXTSPCLKA_DIV + 1). Unsigned integer.
        #! Possible values are 0 - 255, default is 255.
    ENDBITFIELD
    BITFIELD   RXTSPCLKA_DIV<7:0>
        POSITION=<7:0>
        DEFAULT=11111111
        MODE=RW
        #! RxTSP clock divider, used to produce MCLK(1/2) clocks.
        #! Clock division ratio is 2(TXTSPCLKA_DIV + 1). Unsigned integer.
        #! Possible values are 0 - 255, default is 255.
    ENDBITFIELD
ENDREGISTER

REGISTER    MIMOCFG    0x002E
    BITFIELD   MIMO_SISO
        POSITION=15
        DEFAULT=0
        MODE=RW
        #! MIMO channel B enable control.
        #!     1 - Disables MIMO channel B, when SISO_ID (from pad) is 1.
        #!     0 - Enables MIMO channel B, when SISO_ID (from pad) is 0.
    ENDBITFIELD
ENDREGISTER

REGISTER    ChipVer    0x002F
    BITFIELD   VER<4:0>
        POSITION=<15:11>
        DEFAULT=00111
        MODE=R
        #! Chip version. Read only.
        #! 00111 - Chip version is 7
    ENDBITFIELD
    BITFIELD   REV<4:0>
        POSITION=<10:6>
        DEFAULT=00001
        MODE=R
        #! Chip revision. Read only.
        #! 00001 - Chip revision is 1
    ENDBITFIELD
    BITFIELD   MASK<5:0>
        POSITION=<5:0>
        DEFAULT=000001
        MODE=R
        #! Chip mask. Read only.
        #! 000001 - Chip mask is 1
    ENDBITFIELD
ENDREGISTER

REGISTER    EN_DIR    0x0081
    BITFIELD   TRX_GAIN_SRC
        POSITION=15
        DEFAULT=0
        MODE=RW
        #! Alternative TRX gain source select. See section 2.12 for more
        #! information.
        #!     0 - Gain control from separate registers (default)
        #!     1 - Gain control from combined registers
    ENDBITFIELD
    BITFIELD   EN_DIR_LDO
        POSITION=3
        DEFAULT=0
        MODE=RW
        #! Enables direct control of PDs and ENs for LDO module.
        #!     0 - direct control disabled (default)
        #!     1 - direct control enabled
    ENDBITFIELD
    BITFIELD   EN_DIR_CGEN
        POSITION=2
        DEFAULT=0
        MODE=RW
        #! Enables direct control of PDs and ENs for CGEN module.
        #!     0 - direct control disabled (default)
        #!     1 - direct control enabled
    ENDBITFIELD
    BITFIELD   EN_DIR_XBUF
        POSITION=1
        DEFAULT=0
        MODE=RW
        #! Enables direct control of PDs and ENs for XBUF module.
        #!     0 - direct control disabled (default)
        #!     1 - direct control enabled
    ENDBITFIELD
    BITFIELD   EN_DIR_AFE
        POSITION=0
        DEFAULT=0
        MODE=RW
        #! Enables direct control of PDs and ENs for AFE module.
        #!     0 - direct control disabled (default)
        #!     1 - direct control enabled
    ENDBITFIELD
ENDREGISTER

REGISTER    AFE_CFG    0x0082
    BITFIELD   ISEL_DAC_AFE<2:0>
        POSITION=<15:13>
        DEFAULT=100
        MODE=RW
        #! Controls the peak current of the DAC output current. Default: 4
        #! Iout_peak = 325uA+ISEL_DAC_AFE*75uA
        #! Nominal = 625uA
    ENDBITFIELD
    BITFIELD   MODE_INTERLEAVE_AFE
        POSITION=12
        DEFAULT=0
        MODE=RW
        #! Time interleaves the two ADCs into one ADC
        #!     0 - Two ADCs (default)
        #!     1 - Interleaved
    ENDBITFIELD
    BITFIELD   MUX_AFE_1<1:0>
        POSITION=<11:10>
        DEFAULT=00
        MODE=RW
        #! Controls the MUX at the input of the ADC channel 1
        #!     0 - MUX off, only PGA output is connected to ADC input (default)
        #!     1 - pdet_1 is connected to ADC channel 1. PGA should be powered down
        #!     2 - BIAS_TOP test outputs will be connected to ADC channel 1 input (Please see MUX_BIAS_OUT<1:0>)
        #!     3 - RSSI 1 output will be connected to ADC 1 input
    ENDBITFIELD
    BITFIELD   MUX_AFE_2<1:0>
        POSITION=<9:8>
        DEFAULT=00
        MODE=RW
        #! Controls the MUX at the input of the ADC channel 2
        #!     0 - MUX off, only PGA output is connected to ADC input (default)
        #!     1 - pdet_2 is connected to ADC channel 2. PGA should be powered down
        #!     2 - RSSI 1 output will be connected to ADC 2 input
        #!     3 - RSSI 2 output will be connected to ADC 2 input
    ENDBITFIELD
    BITFIELD   PD_AFE
        POSITION=5
        DEFAULT=0
        MODE=RW
        #! Power down control for the AFE current mirror in BIAS_TOP
        #!     0 - Active (default)
        #!     1 - powered down
    ENDBITFIELD
    BITFIELD   PD_RX_AFE1
        POSITION=4
        DEFAULT=0
        MODE=RW
        #! Power down control for the ADC of channel 1
        #!     0 - Active (default)
        #!     1 - powered down
    ENDBITFIELD
    BITFIELD   PD_RX_AFE2
        POSITION=3
        DEFAULT=1
        MODE=RW
        #! Power down control for the ADC of channel 2
        #!     0 - Active
        #!     1 - powered down (default)
    ENDBITFIELD
    BITFIELD   PD_TX_AFE1
        POSITION=2
        DEFAULT=0
        MODE=RW
        #! Power down control for the DAC of channel 1
        #!     0 - Active (default)
        #!     1 - powered down
    ENDBITFIELD
    BITFIELD   PD_TX_AFE2
        POSITION=1
        DEFAULT=1
        MODE=RW
        #! Power down control for the DAC of channel 2
        #!     0 - Active
        #!     1 - powered down (default)
    ENDBITFIELD
    BITFIELD   EN_G_AFE
        POSITION=0
        DEFAULT=1
        MODE=RW
        #! Enable control for all the AFE power downs
        #!     0 - All AFE modules powered down
        #!     1 - All AFE modules controlled by individual power down registers
    ENDBITFIELD
ENDREGISTER

REGISTER    BIAS_CFG    0x0084
    BITFIELD   MUX_BIAS_OUT<1:0>
        POSITION=<12:11>
        DEFAULT=00
        MODE=RW
        #! Test mode of the BIAS_TOP
        #!     0 - NO test mode (default)
        #!     1 - vr_ext_bak and vr_cal_ref=600mV is passed to the ADC input MUX.
        #! Vr_ext_bak is the voltage read on the off-chip 10Kohm reference resistor. Ip60f is connected to r_ext=10kOhm and RP_CALIB_BIAS is changed until vr_ext becomes 600mV.
        #!     2 - Vptat_600mV and vr_cal_ref=600mV is passed to the ADC input MUX. The ratio between the two will be proportional to absolute temp.
        #!     3 - No test mode
    ENDBITFIELD
    BITFIELD   RP_CALIB_BIAS<4:0>
        POSITION=<10:6>
        DEFAULT=10000
        MODE=RW
        #! Calibration code for rppolywo. This code is set by the calibration algorithm: BIAS_RPPOLY_calibration Default: 16
    ENDBITFIELD
    BITFIELD   PD_FRP_BIAS
        POSITION=4
        DEFAULT=0
        MODE=RW
        #! Power down signal for Fix/RP block
        #!     0 - Enabled (default)
        #!     1 - Powered down
    ENDBITFIELD
    BITFIELD   PD_F_BIAS
        POSITION=3
        DEFAULT=0
        MODE=RW
        #! Power down signal for Fix
        #!     0 - Enabled (default)
        #!     1 - Powered down
    ENDBITFIELD
    BITFIELD   PD_PTRP_BIAS
        POSITION=2
        DEFAULT=0
        MODE=RW
        #! Power down signal for PTAT/RP block
        #!     0 - Enabled (default)
        #!     1- Powered down
    ENDBITFIELD
    BITFIELD   PD_PT_BIAS
        POSITION=1
        DEFAULT=0
        MODE=RW
        #! Power down signal for PTAT block
        #!     0 - Enabled (default)
        #!     1 - Powered down
    ENDBITFIELD
    BITFIELD   PD_BIAS_MASTER
        POSITION=0
        DEFAULT=0
        MODE=RW
        #! Enable signal for central bias block
        #!     0 - Sub blocks may be selectively powered down (default)
        #!     1 - Poweres down all BIAS blocks
    ENDBITFIELD
ENDREGISTER

REGISTER    XBUF_CFG    0x0085
    BITFIELD   SLFB_XBUF_RX
        POSITION=8
        DEFAULT=0
        MODE=RW
        #! Self biasing digital control.
        #!     0 - disable the DC voltage level from the chip, the input signal, IN, needs to be DC coupled to the chip (default)
        #!     1 - enable biasing the input's DC voltage level from the chip, the input signal, IN, needs to be AC coupled to the chip
    ENDBITFIELD
    BITFIELD   SLFB_XBUF_TX
        POSITION=7
        DEFAULT=0
        MODE=RW
        #! Self biasing digital control.
        #!     0 - disable the DC voltage level from the chip, the input signal, IN, needs to be DC coupled to the chip. (default)
        #!     1 - enable biasing the input's DC voltage level from the chip, the input signal, IN, needs to be AC coupled to the chip.
    ENDBITFIELD
    BITFIELD   BYP_XBUF_RX
        POSITION=6
        DEFAULT=0
        MODE=RW
        #! Shorts the Input 3.3V buffer in XBUF
        #! The final 2nd 1.2V buffers are still active. The input in Bypass mode should be a
        #! 1.2V full scale CMOS signal.
        #!     0 - Bypass not active (default)
        #!     1 - Bypass active
    ENDBITFIELD
    BITFIELD   BYP_XBUF_TX
        POSITION=5
        DEFAULT=0
        MODE=RW
        #! Shorts the Input 3.3V buffer in XBUF
        #! The final 2nd 1.2V buffers are still active. The input in Bypass mode should be a
        #! 1.2V full scale CMOS signal.
        #!     0 - Bypass not active (default)
        #!     1 - Bypass active
    ENDBITFIELD
    BITFIELD   EN_OUT2_XBUF_TX
        POSITION=4
        DEFAULT=0
        MODE=RW
        #! Enables the 2nd output of TX XBUF. This 2nd buffer goes to
        #! XBUF_RX. This should be active when only 1 XBUF is to be used.
        #!     0 - TX XBUF 2nd output is disabled (default)
        #!     1 - TX XBUF 2nd output is active
    ENDBITFIELD
    BITFIELD   EN_TBUFIN_XBUF_RX
        POSITION=3
        DEFAULT=0
        MODE=RW
        #! Disables the input from the external XOSC and buffers the
        #! 2nd input signal (from TX XBUF 2nd output) to the RX. This should be active when
        #! only 1 XBUF is to be used.
        #!     0 - RX XBUF input is coming from external XOSC (default)
        #!     1 - RX XBUF input is coming from TX
    ENDBITFIELD
    BITFIELD   PD_XBUF_RX
        POSITION=2
        DEFAULT=0
        MODE=RW
        #! Power down signal
        #!     0 - block active (default)
        #!     1 - block powered down
    ENDBITFIELD
    BITFIELD   PD_XBUF_TX
        POSITION=1
        DEFAULT=0
        MODE=RW
        #! Power down signal
        #!     0 - block active (default)
        #!     1 - block powered down
    ENDBITFIELD
    BITFIELD   EN_G_XBUF
        POSITION=0
        DEFAULT=1
        MODE=RW
        #! Enable control for all the XBUF power downs
        #!     0 - All XBUF modules powered down
        #!     1 - All XBUF modules controlled by individual power down registers (default)
    ENDBITFIELD
ENDREGISTER

REGISTER    CGEN_CFG    0x0086
    BITFIELD   SPDUP_VCO_CGEN
        POSITION=15
        DEFAULT=0
        MODE=RW
        #! Bypasses the noise filter resistor for fast settling time. It
        #! should be connected to a 1us pulse.
        #!     0 - speed up disabled (noise filter resistor active) (default)
        #!     1 - speed up enabled (noise filter resistor shorted)
    ENDBITFIELD
    BITFIELD   RESET_N_CGEN
        POSITION=14
        DEFAULT=1
        MODE=RW
        #! Resets SX. A pulse should be used in the start-up to reset.
        #!     0 - Reset
        #!     1 - Normal operation (default)
    ENDBITFIELD
    BITFIELD   EN_ADCCLKH_CLKGN
        POSITION=11
        DEFAULT=1
        MODE=RW
        #! Selects if F_CLKH or F_CLKL is connected to FCLK_ADC
        #! (F_CLKH and F_CLKL are the two internally generated clocks. A MUX will connect
        #! one of them to FCLK_ADC and the other to FCLK_DAC.).
        #!     0 - FCLK_ADC from F_CLKH / FCLK_DAC from F_CLKL
        #!     1 - FCLK_ADC from F_CLKL / FCLK_DAC from F_CLKH (default)
    ENDBITFIELD
    BITFIELD   EN_COARSE_CKLGEN
        POSITION=10
        DEFAULT=0
        MODE=RW
        #! Enable signal for coarse tuning block.
        #!     0 - Coarse tuning disabled (default)
        #!     1 - Coarse tuning enabled
    ENDBITFIELD
    BITFIELD   EN_INTONLY_SDM_CGEN
        POSITION=9
        DEFAULT=0
        MODE=RW
        #! Enables INTEGER-N mode of the SX.
        #!     0 - Frac-N mode (default)
        #!     1 - INT-N mode
    ENDBITFIELD
    BITFIELD   EN_SDM_CLK_CGEN
        POSITION=8
        DEFAULT=1
        MODE=RW
        #! Enables/Disables SDM clock. In INT-N mode or for noise testing, SDM clock can be disabled.
        #!     0 - SDM clock disabled
        #!     1 - SDM clock enabled (default)
    ENDBITFIELD
    BITFIELD   PD_CP_CGEN
        POSITION=6
        DEFAULT=0
        MODE=RW
        #! Power down for Charge Pump.
        #!     0 - block active (default)
        #!     1 - block powered down
    ENDBITFIELD
    BITFIELD   PD_FDIV_FB_CGEN
        POSITION=5
        DEFAULT=0
        MODE=RW
        #! Power down for feedback frequency divider.
        #!     0 - block active (default)
        #!     1 - block powered down
    ENDBITFIELD
    BITFIELD   PD_FDIV_O_CGEN
        POSITION=4
        DEFAULT=0
        MODE=RW
        #! Power down for forward frequency divider of the CGEN block.
        #!     0 - block active (default)
        #!     1 - block powered down
    ENDBITFIELD
    BITFIELD   PD_SDM_CGEN
        POSITION=3
        DEFAULT=0
        MODE=RW
        #! Power down for SDM.
        #!     0 - block active (default)
        #!     1 - block powered down
    ENDBITFIELD
    BITFIELD   PD_VCO_CGEN
        POSITION=2
        DEFAULT=1
        MODE=RW
        #! Power down for VCO.
        #!     0 - block active
        #!     1 - block powered down (default)
    ENDBITFIELD
    BITFIELD   PD_VCO_COMP_CGEN
        POSITION=1
        DEFAULT=0
        MODE=RW
        #! Power down for VCO comparator.
        #!     0 - block active (default)
        #!     1 - block powered down
    ENDBITFIELD
    BITFIELD   EN_G_CGEN
        POSITION=0
        DEFAULT=1
        MODE=RW
        #! Enable control for all the CGEN power downs.
        #!     0 - All CGEN modules powered down
        #!     1 - All CGEN modules controlled by individual power down registers (default)
    ENDBITFIELD
ENDREGISTER

REGISTER    CGEN_FRACL    0x0087
    BITFIELD   FRAC_SDM_CGENL<15:0>
        POSITION=<15:0>
        DEFAULT=0000010000000000
        MODE=RW
        #! Fractional control of the division ratio LSB. Default: 1024
        #! =2^20*[ Fvco/Fref - int(Fvco/Fref)]
    ENDBITFIELD
ENDREGISTER

REGISTER    CGEN_FRACH    0x0088
    BITFIELD   INT_SDM_CGEN<9:0>
        POSITION=<13:4>
        DEFAULT=0001111000
        MODE=RW
        #! Controls Integer section of the division ratio Default: 120
        #! INT_SDM_SX=int(Fvco/Fref)-1
    ENDBITFIELD
    BITFIELD   FRAC_SDM_CGENH<3:0>
        POSITION=<3:0>
        DEFAULT=0000
        MODE=RW
        #! Fractional control of the division ratio MSB.
    ENDBITFIELD
ENDREGISTER

REGISTER    CGEN_SXCFG0    0x0089
    BITFIELD   REV_SDMCLK_CGEN
        POSITION=15
        DEFAULT=0
        MODE=RW
        #! Reverses the SDM clock
        #!     0 - default (default)
        #!     1 - reversed (after INV)
    ENDBITFIELD
    BITFIELD   SEL_SDMCLK_CGEN
        POSITION=14
        DEFAULT=0
        MODE=RW
        #! Selects between the feedback divider output and Fref for SDM
        #!     0 - CLK CLK_DIV (default)
        #!     1 - CLK CLK_REF
    ENDBITFIELD
    BITFIELD   SX_DITHER_EN_CGEN
        POSITION=13
        DEFAULT=0
        MODE=RW
        #! Enabled dithering in SDM
        #!     0 - Disabled (default)
        #!     1 - Enabled
    ENDBITFIELD
    BITFIELD   CLKH_OV_CLKL_CGEN<1:0>
        POSITION=<12:11>
        DEFAULT=00
        MODE=RW
        #! FCLKL here is ADC clock. FCLKH is the clock to the DAC and if no division is added to the ADC as well. Default: 0
        #! FCLKL=FCLKH/2^(CLKH_OV_CLKL)
    ENDBITFIELD
    BITFIELD   DIV_OUTCH_CGEN<7:0>
        POSITION=<10:3>
        DEFAULT=00000100
        MODE=RW
        #! Controls the output divider chain of the CGEN.
        #! F_CLKH=Fvco_CGEN/(2*(DIV_OUTCH_CGEN+1)) Shadow register.
        #! Default: 4
    ENDBITFIELD
    BITFIELD   TST_CGEN<2:0>
        POSITION=<2:0>
        DEFAULT=000
        MODE=RW
        #! Controls the test mode of the SX
        #!     0 - TST disabled; RSSI analog outputs enabled if RSSI blocks active and
        #!      when all PLL test signals are off (default)
        #!     1 - tstdo[0]=ADC clock; tstdo[1]=DAC clock; tstao = High impedance;
        #!     2 - tstdo[0]=SDM clock; tstdo[1]= feedback divider output; tstao = VCO
        #!       tune through a 60kOhm resistor;
        #!     3 - tstdo[0]=Reference clock; tstdo[1]= feedback divider output; tstao =
        #!       VCO tune through a 10kOhm resistor;
        #!     4 - tstdo[0]= High impedance; tstdo[1]= High impedance; tstao = High
        #!       impedance;
        #!     5 - tstdo[0]=Charge pump Down signal; tstdo[1]=Charge pump Up signal;
        #!       tstao = High impedance;
        #!     6 - tstdo[0]= High impedance; tstdo[1]= High impedance; tstao = VCO
        #!       tune through a 60kOhm resistor;
        #!     7 - tstdo[0]= High impedance; tstdo[1]= High impedance; tstao = VCO
        #!       tune through a 10kOhm resistor;
        #! if TST_SX[2]=1 --> VCO_TSTBUF active generating VCO_TST_DIV20
        #! and VCO_TST_DIV40
    ENDBITFIELD
ENDREGISTER

REGISTER    CGEN_SXCFG1    0x008A
    BITFIELD   REV_CLKDAC_CGEN
        POSITION=14
        DEFAULT=0
        MODE=RW
        #! Inverts the clock F_CLKL.
        #!     0 - Normal (default)
        #!     1 - Inverted
    ENDBITFIELD
    BITFIELD   REV_CLKADC_CGEN
        POSITION=13
        DEFAULT=0
        MODE=RW
        #! Inverts the clock F_CLKL.
        #!     0 - Normal (default)
        #!     1 - Inverted
    ENDBITFIELD
    BITFIELD   REVPH_PFD_CGEN
        POSITION=12
        DEFAULT=0
        MODE=RW
        #! Reverse the pulses of PFD. It can be used to reverse the
        #! polarity of the PLL loop (positive feedback to negative feedback). Default: 0
    ENDBITFIELD
    BITFIELD   IOFFSET_CP_CGEN<5:0>
        POSITION=<11:6>
        DEFAULT=010100
        MODE=RW
        #! Scales the offset current of the charge pump, 0-->63.
        #! This current is used in Fran-N mode to create an offset in the CP response and
        #! avoid the non-linear section. Default: 20
        #! ioffset=0.243uA * IOFFSET_CP_SX
        #! ioffset/ipulse=4/(INT_SDM_SX+4) [First estimation]
    ENDBITFIELD
    BITFIELD   IPULSE_CP_CGEN<5:0>
        POSITION=<5:0>
        DEFAULT=010100
        MODE=RW
        #! Scales the pulse current of the charge pump, 0-->63. Default: 20
        #! ipulse=2.312uA * IPULSE_CP_SX
    ENDBITFIELD
ENDREGISTER

REGISTER    CGEN_SXCFG2    0x008B
    BITFIELD   CMPLO_CTRL_CGEN
        POSITION=14
        DEFAULT=0
        MODE=RW
        #! Controls the CGEN PLL VCO comparator low treshold
        #! value:
        #!     0 - Low treshold is set to 0.18V (Default)
        #!     1 - Low treshold is set to 0.1V
    ENDBITFIELD
    BITFIELD   ICT_VCO_CGEN<4:0>
        POSITION=<13:9>
        DEFAULT=01100
        MODE=RW
        #! Scales the VCO bias current from 0 to 2.5xInom. Default: 12
    ENDBITFIELD
    BITFIELD   CSW_VCO_CGEN<7:0>
        POSITION=<8:1>
        DEFAULT=10000000
        MODE=RW
        #! Coarse control of VCO frequency, 0 for lowest frequency
        #! and 255 for highest. This control is set by SX_SWC_calibration. Shadow register.
        #! Default: 128
    ENDBITFIELD
    BITFIELD   COARSE_START_CGEN
        POSITION=0
        DEFAULT=0
        MODE=RW
        #! Control signal for coarse tuning algorithm (SX_SWC_calibration). Default: 0
    ENDBITFIELD
ENDREGISTER

REGISTER    CGEN_SXCFG3    0x008C
    BITFIELD   COARSE_STEPDONE_CGEN
        POSITION=15
        DEFAULT=0
        MODE=R
        #! Read only
    ENDBITFIELD
    BITFIELD   COARSEPLL_COMPO_CGEN
        POSITION=14
        DEFAULT=0
        MODE=R
        #! Read only
    ENDBITFIELD
    BITFIELD   VCO_CMPHO_CGEN
        POSITION=13
        DEFAULT=0
        MODE=R
        #! Read only
    ENDBITFIELD
    BITFIELD   VCO_CMPLO_CGEN
        POSITION=12
        DEFAULT=0
        MODE=R
        #! Read only
    ENDBITFIELD
    BITFIELD   CP2_CGEN<3:0>
        POSITION=<11:8>
        DEFAULT=0110
        MODE=RW
        #! Controls the value of CP2 (cap from CP output to GND) in the PLL         filter. Default: 6
        #! cp2=CP2_PLL_SX*6*63.2fF
    ENDBITFIELD
    BITFIELD   CP3_CGEN<3:0>
        POSITION=<7:4>
        DEFAULT=0111
        MODE=RW
        #! Controls the value of CP3 (cap from VCO Vtune input to GND) in the PLL filter. Default: 7
        #! cp3=CP3_PLL_SX*248fF
    ENDBITFIELD
    BITFIELD   CZ_CGEN<3:0>
        POSITION=<3:0>
        DEFAULT=1011
        MODE=RW
        #! Controls the value of CZ (Zero capacitor) in the PLL filter. Default:  11
        #! cz=CZ_PLL_SX*8*365fF
    ENDBITFIELD
ENDREGISTER

REGISTER    BIAS_CFG0    0x0092
    BITFIELD   EN_LDO_DIG
        POSITION=15
        DEFAULT=0
        MODE=RW
        #! Enables the LDO
        #!     0 - Powered down (default)
        #!     1 - Enabled
    ENDBITFIELD
    BITFIELD   EN_LDO_DIGGN
        POSITION=14
        DEFAULT=0
        MODE=RW
        #! Enables the LDO
        #!     0 - Powered down (default)
        #!     1 - Enabled
    ENDBITFIELD
    BITFIELD   EN_LDO_DIGSXR
        POSITION=13
        DEFAULT=0
        MODE=RW
        #! Enables the LDO
        #!     0 - Powered down (default)
        #!     1 - Enabled
    ENDBITFIELD
    BITFIELD   EN_LDO_DIGSXT
        POSITION=12
        DEFAULT=0
        MODE=RW
        #! Enables the LDO
        #!     0 - Powered down (default)
        #!     1 - Enabled
    ENDBITFIELD
    BITFIELD   EN_LDO_DIVGN
        POSITION=11
        DEFAULT=0
        MODE=RW
        #! Enables the LDO
        #!     0 - Powered down (default)
        #!     1 - Enabled
    ENDBITFIELD
    BITFIELD   EN_LDO_DIVSXR
        POSITION=10
        DEFAULT=0
        MODE=RW
        #! Enables the LDO
        #!     0 - Powered down (default)
        #!     1 - Enabled
    ENDBITFIELD
    BITFIELD   EN_LDO_DIVSXT
        POSITION=9
        DEFAULT=0
        MODE=RW
        #! Enables the LDO
        #!     0 - Powered down (default)
        #!     1 - Enabled
    ENDBITFIELD
    BITFIELD   EN_LDO_LNA12
        POSITION=8
        DEFAULT=0
        MODE=RW
        #! Enables the LDO
        #!     0 - Powered down (default)
        #!     1 - Enabled
    ENDBITFIELD
    BITFIELD   EN_LDO_LNA14
        POSITION=7
        DEFAULT=0
        MODE=RW
        #! Enables the LDO
        #!     0 - Powered down (default)
        #!     1 - Enabled
    ENDBITFIELD
    BITFIELD   EN_LDO_MXRFE
        POSITION=6
        DEFAULT=0
        MODE=RW
        #! Enables the LDO
        #!     0 - Powered down (default)
        #!     1 - Enabled
    ENDBITFIELD
    BITFIELD   EN_LDO_RBB
        POSITION=5
        DEFAULT=0
        MODE=RW
        #! Enables the LDO
        #!     0 - Powered down (default)
        #!     1 - Enabled
    ENDBITFIELD
    BITFIELD   EN_LDO_RXBUF
        POSITION=4
        DEFAULT=0
        MODE=RW
        #! Enables the LDO
        #!     0 - Powered down (default)
        #!     1 - Enabled
    ENDBITFIELD
    BITFIELD   EN_LDO_TBB
        POSITION=3
        DEFAULT=0
        MODE=RW
        #! Enables the LDO
        #!     0 - Powered down (default)
        #!     1 - Enabled
    ENDBITFIELD
    BITFIELD   EN_LDO_TIA12
        POSITION=2
        DEFAULT=0
        MODE=RW
        #! Enables the LDO
        #!     0 - Powered down (default)
        #!     1 - Enabled
    ENDBITFIELD
    BITFIELD   EN_LDO_TIA14
        POSITION=1
        DEFAULT=0
        MODE=RW
        #! Enables the LDO
        #!     0 - Powered down (default)
        #!     1 - Enabled
    ENDBITFIELD
    BITFIELD   EN_G_LDO
        POSITION=0
        DEFAULT=1
        MODE=RW
        #! Enable control for all the LDO power downs
        #!     0 - All LDO modules powered down
        #!     1 - All LDO modules controlled by individual power down registers (default)
    ENDBITFIELD
ENDREGISTER

REGISTER    BIAS_CFG1    0x0093
    BITFIELD   EN_LOADIMP_LDO_TLOB
        POSITION=15
        DEFAULT=0
        MODE=RW
        #! Enables the load dependent bias to optimize the load regulation
        #!     0 - Constant bias (default)
        #!     1 - Load dependent bias
    ENDBITFIELD
    BITFIELD   EN_LOADIMP_LDO_TPAD
        POSITION=14
        DEFAULT=0
        MODE=RW
        #! Enables the load dependent bias to optimize the load regulation
        #!     0 - Constant bias (default)
        #!     1 - Load dependent bias
    ENDBITFIELD
    BITFIELD   EN_LOADIMP_LDO_TXBUF
        POSITION=13
        DEFAULT=0
        MODE=RW
        #! Enables the load dependent bias to optimize the load regulation
        #!     0 - Constant bias (default)
        #!     1 - Load dependent bias
    ENDBITFIELD
    BITFIELD   EN_LOADIMP_LDO_VCOGN
        POSITION=12
        DEFAULT=0
        MODE=RW
        #! Enables the load dependent bias to optimize the load regulation
        #!     0 - Constant bias (default)
        #!     1 - Load dependent bias
    ENDBITFIELD
    BITFIELD   EN_LOADIMP_LDO_VCOSXR
        POSITION=11
        DEFAULT=0
        MODE=RW
        #! Enables the load dependent bias to optimize the load regulation
        #!     0 - Constant bias (default)
        #!     1 - Load dependent bias
    ENDBITFIELD
    BITFIELD   EN_LOADIMP_LDO_VCOSXT
        POSITION=10
        DEFAULT=0
        MODE=RW
        #! Enables the load dependent bias to optimize the load regulation
        #!     0 - Constant bias (default)
        #!     1 - Load dependent bias
    ENDBITFIELD
    BITFIELD   EN_LDO_AFE
        POSITION=9
        DEFAULT=0
        MODE=RW
        #! Enables the LDO
        #!     0 - Powered down (default)
        #!     1 - Enabled
    ENDBITFIELD
    BITFIELD   EN_LDO_CPGN
        POSITION=8
        DEFAULT=0
        MODE=RW
        #! Enables the LDO
        #!     0 - Powered down (default)
        #!     1 - Enabled
    ENDBITFIELD
    BITFIELD   EN_LDO_CPSXR
        POSITION=7
        DEFAULT=0
        MODE=RW
        #! Enables the LDO
        #!     0 - Powered down (default)
        #!     1 - Enabled
    ENDBITFIELD
    BITFIELD   EN_LDO_TLOB
        POSITION=6
        DEFAULT=0
        MODE=RW
        #! Enables the LDO
        #!     0 - Powered down (default)
        #!     1 - Enabled
    ENDBITFIELD
    BITFIELD   EN_LDO_TPAD
        POSITION=5
        DEFAULT=0
        MODE=RW
        #! Enables the LDO
        #!     0 - Powered down (default)
        #!     1 - Enabled
    ENDBITFIELD
    BITFIELD   EN_LDO_TXBUF
        POSITION=4
        DEFAULT=0
        MODE=RW
        #! Enables the LDO
        #!     0 - Powered down (default)
        #!     1 - Enabled
    ENDBITFIELD
    BITFIELD   EN_LDO_VCOGN
        POSITION=3
        DEFAULT=0
        MODE=RW
        #! Enables the LDO
        #!     0 - Powered down (default)
        #!     1 - Enabled
    ENDBITFIELD
    BITFIELD   EN_LDO_VCOSXR
        POSITION=2
        DEFAULT=0
        MODE=RW
        #! Enables the LDO
        #!     0 - Powered down (default)
        #!     1 - Enabled
    ENDBITFIELD
    BITFIELD   EN_LDO_VCOSXT
        POSITION=1
        DEFAULT=0
        MODE=RW
        #! Enables the LDO
        #!     0 - Powered down (default)
        #!     1 - Enabled
    ENDBITFIELD
    BITFIELD   EN_LDO_CPSXT
        POSITION=0
        DEFAULT=0
        MODE=RW
        #! Enables the LDO
        #!     0 - Powered down (default)
        #!     1 - Enabled
    ENDBITFIELD
ENDREGISTER

REGISTER    BIAS_CFG2    0x0094
    BITFIELD   EN_LOADIMP_LDO_CPSXT
        POSITION=15
        DEFAULT=0
        MODE=RW
        #! Enables the load dependent bias to optimize the load regulation
        #!     0 - Constant bias (default)
        #!     1 - Load dependent bias
    ENDBITFIELD
    BITFIELD   EN_LOADIMP_LDO_DIG
        POSITION=14
        DEFAULT=0
        MODE=RW
        #! Enables the load dependent bias to optimize the load regulation
        #!     0 - Constant bias (default)
        #!     1 - Load dependent bias
    ENDBITFIELD
    BITFIELD   EN_LOADIMP_LDO_DIGGN
        POSITION=13
        DEFAULT=0
        MODE=RW
        #! Enables the load dependent bias to optimize the load regulation
        #!     0 - Constant bias (default)
        #!     1 - Load dependent bias
    ENDBITFIELD
    BITFIELD   EN_LOADIMP_LDO_DIGSXR
        POSITION=12
        DEFAULT=0
        MODE=RW
        #! Enables the load dependent bias to optimize the load regulation
        #!     0 - Constant bias (default)
        #!     1 - Load dependent bias
    ENDBITFIELD
    BITFIELD   EN_LOADIMP_LDO_DIGSXT
        POSITION=11
        DEFAULT=0
        MODE=RW
        #! Enables the load dependent bias to optimize the load regulation
        #!     0 - Constant bias (default)
        #!     1 - Load dependent bias
    ENDBITFIELD
    BITFIELD   EN_LOADIMP_LDO_DIVGN
        POSITION=10
        DEFAULT=0
        MODE=RW
        #! Enables the load dependent bias to optimize the load regulation
        #!     0 - Constant bias (default)
        #!     1 - Load dependent bias
    ENDBITFIELD
    BITFIELD   EN_LOADIMP_LDO_DIVSXR
        POSITION=9
        DEFAULT=0
        MODE=RW
        #! Enables the load dependent bias to optimize the load regulation
        #!     0 - Constant bias (default)
        #!     1 - Load dependent bias
    ENDBITFIELD
    BITFIELD   EN_LOADIMP_LDO_DIVSXT
        POSITION=8
        DEFAULT=0
        MODE=RW
        #! Enables the load dependent bias to optimize the load regulation
        #!     0 - Constant bias (default)
        #!     1 - Load dependent bias
    ENDBITFIELD
    BITFIELD   EN_LOADIMP_LDO_LNA12
        POSITION=7
        DEFAULT=0
        MODE=RW
        #! Enables the load dependent bias to optimize the load regulation
        #!     0 - Constant bias (default)
        #!     1 - Load dependent bias
    ENDBITFIELD
    BITFIELD   EN_LOADIMP_LDO_LNA14
        POSITION=6
        DEFAULT=0
        MODE=RW
        #! Enables the load dependent bias to optimize the load regulation
        #!     0 - Constant bias (default)
        #!     1 - Load dependent bias
    ENDBITFIELD
    BITFIELD   EN_LOADIMP_LDO_MXRFE
        POSITION=5
        DEFAULT=0
        MODE=RW
        #! Enables the load dependent bias to optimize the load regulation
        #!     0 - Constant bias (default)
        #!     1 - Load dependent bias
    ENDBITFIELD
    BITFIELD   EN_LOADIMP_LDO_RBB
        POSITION=4
        DEFAULT=0
        MODE=RW
        #! Enables the load dependent bias to optimize the load regulation
        #!     0 - Constant bias (default)
        #!     1 - Load dependent bias
    ENDBITFIELD
    BITFIELD   EN_LOADIMP_LDO_RXBUF
        POSITION=3
        DEFAULT=0
        MODE=RW
        #! Enables the load dependent bias to optimize the load regulation
        #!     0 - Constant bias (default)
        #!     1 - Load dependent bias
    ENDBITFIELD
    BITFIELD   EN_LOADIMP_LDO_TBB
        POSITION=2
        DEFAULT=0
        MODE=RW
        #! Enables the load dependent bias to optimize the load regulation
        #!     0 - Constant bias (default)
        #!     1 - Load dependent bias
    ENDBITFIELD
    BITFIELD   EN_LOADIMP_LDO_TIA12
        POSITION=1
        DEFAULT=0
        MODE=RW
        #! Enables the load dependent bias to optimize the load regulation
        #!     0 - Constant bias (default)
        #!     1 - Load dependent bias
    ENDBITFIELD
    BITFIELD   EN_LOADIMP_LDO_TIA14
        POSITION=0
        DEFAULT=0
        MODE=RW
        #! Enables the load dependent bias to optimize the load regulation
        #!     0 - Constant bias (default)
        #!     1 - Load dependent bias
    ENDBITFIELD
ENDREGISTER

REGISTER    BIAS_CFG3    0x0095
    BITFIELD   BYP_LDO_TBB
        POSITION=15
        DEFAULT=0
        MODE=RW
        #! Bypass signal for the LDO
        #!     0 - Does not bypass. Normal LDO operation (default)
        #!     1 - Bypasses LDO. Connects Vinput to Voutput
    ENDBITFIELD
    BITFIELD   BYP_LDO_TIA12
        POSITION=14
        DEFAULT=0
        MODE=RW
        #! Bypass signal for the LDO
        #!     0 - Does not bypass. Normal LDO operation (default)
        #!     1 - Bypasses LDO. Connects Vinput to Voutput
    ENDBITFIELD
    BITFIELD   BYP_LDO_TIA14
        POSITION=13
        DEFAULT=0
        MODE=RW
        #! Bypass signal for the LDO
        #!     0 - Does not bypass. Normal LDO operation (default)
        #!     1 - Bypasses LDO. Connects Vinput to Voutput
    ENDBITFIELD
    BITFIELD   BYP_LDO_TLOB
        POSITION=12
        DEFAULT=0
        MODE=RW
        #! Bypass signal for the LDO
        #!     0 - Does not bypass. Normal LDO operation (default)
        #!     1 - Bypasses LDO. Connects Vinput to Voutput
    ENDBITFIELD
    BITFIELD   BYP_LDO_TPAD
        POSITION=11
        DEFAULT=0
        MODE=RW
        #! Bypass signal for the LDO
        #!     0 - Does not bypass. Normal LDO operation (default)
        #!     1 - Bypasses LDO. Connects Vinput to Voutput
    ENDBITFIELD
    BITFIELD   BYP_LDO_TXBUF
        POSITION=10
        DEFAULT=0
        MODE=RW
        #! Bypass signal for the LDO
        #!     0 - Does not bypass. Normal LDO operation (default)
        #!     1 - Bypasses LDO. Connects Vinput to Voutput
    ENDBITFIELD
    BITFIELD   BYP_LDO_VCOGN
        POSITION=9
        DEFAULT=0
        MODE=RW
        #! Bypass signal for the LDO
        #!     0 - Does not bypass. Normal LDO operation (default)
        #!     1 - Bypasses LDO. Connects Vinput to Voutput
    ENDBITFIELD
    BITFIELD   BYP_LDO_VCOSXR
        POSITION=8
        DEFAULT=0
        MODE=RW
        #! Bypass signal for the LDO
        #!     0 - Does not bypass. Normal LDO operation (default)
        #!     1 - Bypasses LDO. Connects Vinput to Voutput
    ENDBITFIELD
    BITFIELD   BYP_LDO_VCOSXT
        POSITION=7
        DEFAULT=0
        MODE=RW
        #! Bypass signal for the LDO
        #!     0 - Does not bypass. Normal LDO operation (default)
        #!     1 - Bypasses LDO. Connects Vinput to Voutput
    ENDBITFIELD
    BITFIELD   EN_LOADIMP_LDO_AFE
        POSITION=2
        DEFAULT=0
        MODE=RW
        #! Enables the load dependent bias to optimize the load regulation
        #!     0 - Constant bias (default)
        #!     1 - Load dependent bias
    ENDBITFIELD
    BITFIELD   EN_LOADIMP_LDO_CPGN
        POSITION=1
        DEFAULT=0
        MODE=RW
        #! Enables the load dependent bias to optimize the load regulation
        #!     0 - Constant bias (default)
        #!     1 - Load dependent bias
    ENDBITFIELD
    BITFIELD   EN_LOADIMP_LDO_CPSXR
        POSITION=0
        DEFAULT=0
        MODE=RW
        #! Enables the load dependent bias to optimize the load regulation
        #!     0 - Constant bias (default)
        #!     1 - Load dependent bias
    ENDBITFIELD
ENDREGISTER

REGISTER    BIAS_CFG4    0x0096
    BITFIELD   BYP_LDO_AFE
        POSITION=15
        DEFAULT=0
        MODE=RW
        #! Bypass signal for the LDO
        #!     0 - Does not bypass. Normal LDO operation (default)
        #!     1 - Bypasses LDO. Connects Vinput to Voutput
    ENDBITFIELD
    BITFIELD   BYP_LDO_CPGN
        POSITION=14
        DEFAULT=0
        MODE=RW
        #! Bypass signal for the LDO
        #!     0 - Does not bypass. Normal LDO operation (default)
        #!     1 - Bypasses LDO. Connects Vinput to Voutput
    ENDBITFIELD
    BITFIELD   BYP_LDO_CPSXR
        POSITION=13
        DEFAULT=0
        MODE=RW
        #! Bypass signal for the LDO
        #!     0 - Does not bypass. Normal LDO operation (default)
        #!     1 - Bypasses LDO. Connects Vinput to Voutput
    ENDBITFIELD
    BITFIELD   BYP_LDO_CPSXT
        POSITION=12
        DEFAULT=0
        MODE=RW
        #! Bypass signal for the LDO
        #!     0 - Does not bypass. Normal LDO operation (default)
        #!     1 - Bypasses LDO. Connects Vinput to Voutput
    ENDBITFIELD
    BITFIELD   BYP_LDO_DIG
        POSITION=11
        DEFAULT=0
        MODE=RW
        #! Bypass signal for the LDO
        #!     0 - Does not bypass. Normal LDO operation (default)
        #!     1 - Bypasses LDO. Connects Vinput to Voutput
    ENDBITFIELD
    BITFIELD   BYP_LDO_DIGGN
        POSITION=10
        DEFAULT=0
        MODE=RW
        #! Bypass signal for the LDO
        #!     0 - Does not bypass. Normal LDO operation (default)
        #!     1 - Bypasses LDO. Connects Vinput to Voutput
    ENDBITFIELD
    BITFIELD   BYP_LDO_DIGSXR
        POSITION=9
        DEFAULT=0
        MODE=RW
        #! Bypass signal for the LDO
        #!     0 - Does not bypass. Normal LDO operation (default)
        #!     1 - Bypasses LDO. Connects Vinput to Voutput
    ENDBITFIELD
    BITFIELD   BYP_LDO_DIGSXT
        POSITION=8
        DEFAULT=0
        MODE=RW
        #! Bypass signal for the LDO
        #!     0 - Does not bypass. Normal LDO operation (default)
        #!     1 - Bypasses LDO. Connects Vinput to Voutput
    ENDBITFIELD
    BITFIELD   BYP_LDO_DIVGN
        POSITION=7
        DEFAULT=0
        MODE=RW
        #! Bypass signal for the LDO
        #!     0 - Does not bypass. Normal LDO operation (default)
        #!     1 - Bypasses LDO. Connects Vinput to Voutput
    ENDBITFIELD
    BITFIELD   BYP_LDO_DIVSXR
        POSITION=6
        DEFAULT=0
        MODE=RW
        #! Bypass signal for the LDO
        #!     0 - Does not bypass. Normal LDO operation (default)
        #!     1 - Bypasses LDO. Connects Vinput to Voutput
    ENDBITFIELD
    BITFIELD   BYP_LDO_DIVSXT
        POSITION=5
        DEFAULT=0
        MODE=RW
        #! Bypass signal for the LDO
        #!     0 - Does not bypass. Normal LDO operation (default)
        #!     1 - Bypasses LDO. Connects Vinput to Voutput
    ENDBITFIELD
    BITFIELD   BYP_LDO_LNA12
        POSITION=4
        DEFAULT=0
        MODE=RW
        #! Bypass signal for the LDO
        #!     0 - Does not bypass. Normal LDO operation (default)
        #!     1 - Bypasses LDO. Connects Vinput to Voutput
    ENDBITFIELD
    BITFIELD   BYP_LDO_LNA14
        POSITION=3
        DEFAULT=0
        MODE=RW
        #! Bypass signal for the LDO
        #!     0 - Does not bypass. Normal LDO operation (default)
        #!     1 - Bypasses LDO. Connects Vinput to Voutput
    ENDBITFIELD
    BITFIELD   BYP_LDO_MXRFE
        POSITION=2
        DEFAULT=0
        MODE=RW
        #! Bypass signal for the LDO
        #!     0 - Does not bypass. Normal LDO operation (default)
        #!     1 - Bypasses LDO. Connects Vinput to Voutput
    ENDBITFIELD
    BITFIELD   BYP_LDO_RBB
        POSITION=1
        DEFAULT=0
        MODE=RW
        #! Bypass signal for the LDO
        #!     0 - Does not bypass. Normal LDO operation (default)
        #!     1 - Bypasses LDO. Connects Vinput to Voutput
    ENDBITFIELD
    BITFIELD   BYP_LDO_RXBUF
        POSITION=0
        DEFAULT=0
        MODE=RW
        #! Bypass signal for the LDO
        #!     0 - Does not bypass. Normal LDO operation (default)
        #!     1 - Bypasses LDO. Connects Vinput to Voutput
    ENDBITFIELD
ENDREGISTER

REGISTER    BIAS_CFG5    0x0097
    BITFIELD   SPDUP_LDO_DIVSXR
        POSITION=15
        DEFAULT=0
        MODE=RW
        #! Short the noise filter resistor to speed up the settling time
        #!     0 - noise filter resistor in place (default)
        #!     1 - Noise filter resistor bypassed
        #! should be connected to a 1~5uS at the power up
    ENDBITFIELD
    BITFIELD   SPDUP_LDO_DIVSXT
        POSITION=14
        DEFAULT=0
        MODE=RW
        #! Short the noise filter resistor to speed up the settling time
        #!     0 - noise filter resistor in place (default)
        #!     1 - Noise filter resistor bypassed
        #! should be connected to a 1~5uS at the power up
    ENDBITFIELD
    BITFIELD   SPDUP_LDO_LNA12
        POSITION=13
        DEFAULT=0
        MODE=RW
        #! Short the noise filter resistor to speed up the settling time
        #!     0 - noise filter resistor in place (default)
        #!     1 - Noise filter resistor bypassed
        #! should be connected to a 1~5uS at the power up
    ENDBITFIELD
    BITFIELD   SPDUP_LDO_LNA14
        POSITION=12
        DEFAULT=0
        MODE=RW
        #! Short the noise filter resistor to speed up the settling time
        #!     0 - noise filter resistor in place (default)
        #!     1 - Noise filter resistor bypassed
        #! should be connected to a 1~5uS at the power up
    ENDBITFIELD
    BITFIELD   SPDUP_LDO_MXRFE
        POSITION=11
        DEFAULT=0
        MODE=RW
        #! Short the noise filter resistor to speed up the settling time
        #!     0 - noise filter resistor in place (default)
        #!     1 - Noise filter resistor bypassed
        #! should be connected to a 1~5uS at the power up
    ENDBITFIELD
    BITFIELD   SPDUP_LDO_RBB
        POSITION=10
        DEFAULT=0
        MODE=RW
        #! Short the noise filter resistor to speed up the settling time
        #!     0 - noise filter resistor in place (default)
        #!     1 - Noise filter resistor bypassed
        #! should be connected to a 1~5uS at the power up
    ENDBITFIELD
    BITFIELD   SPDUP_LDO_RXBUF
        POSITION=9
        DEFAULT=0
        MODE=RW
        #! Short the noise filter resistor to speed up the settling time
        #!     0 - noise filter resistor in place (default)
        #!     1 - Noise filter resistor bypassed
        #! should be connected to a 1~5uS at the power up
    ENDBITFIELD
    BITFIELD   SPDUP_LDO_TBB
        POSITION=8
        DEFAULT=0
        MODE=RW
        #! Short the noise filter resistor to speed up the settling time
        #!     0 - noise filter resistor in place (default)
        #!     1 - Noise filter resistor bypassed
        #! should be connected to a 1~5uS at the power up
    ENDBITFIELD
    BITFIELD   SPDUP_LDO_TIA12
        POSITION=7
        DEFAULT=0
        MODE=RW
        #! Short the noise filter resistor to speed up the settling time
        #!     0 - noise filter resistor in place (default)
        #!     1 - Noise filter resistor bypassed
        #! should be connected to a 1~5uS at the power up
    ENDBITFIELD
    BITFIELD   SPDUP_LDO_TIA14
        POSITION=6
        DEFAULT=0
        MODE=RW
        #! Short the noise filter resistor to speed up the settling time
        #!     0 - noise filter resistor in place (default)
        #!     1 - Noise filter resistor bypassed
        #! should be connected to a 1~5uS at the power up
    ENDBITFIELD
    BITFIELD   SPDUP_LDO_TLOB
        POSITION=5
        DEFAULT=0
        MODE=RW
        #! Short the noise filter resistor to speed up the settling time
        #!     0 - noise filter resistor in place (default)
        #!     1 - Noise filter resistor bypassed
        #! should be connected to a 1~5uS at the power up
    ENDBITFIELD
    BITFIELD   SPDUP_LDO_TPAD
        POSITION=4
        DEFAULT=0
        MODE=RW
        #! Short the noise filter resistor to speed up the settling time
        #!     0 - noise filter resistor in place (default)
        #!     1 - Noise filter resistor bypassed
        #! should be connected to a 1~5uS at the power up
    ENDBITFIELD
    BITFIELD   SPDUP_LDO_TXBUF
        POSITION=3
        DEFAULT=0
        MODE=RW
        #! Short the noise filter resistor to speed up the settling time
        #!     0 - noise filter resistor in place (default)
        #!     1 - Noise filter resistor bypassed
        #! should be connected to a 1~5uS at the power up
    ENDBITFIELD
    BITFIELD   SPDUP_LDO_VCOGN
        POSITION=2
        DEFAULT=0
        MODE=RW
        #! Short the noise filter resistor to speed up the settling time
        #!     0 - noise filter resistor in place (default)
        #!     1 - Noise filter resistor bypassed
        #! should be connected to a 1~5uS at the power up
    ENDBITFIELD
    BITFIELD   SPDUP_LDO_VCOSXR
        POSITION=1
        DEFAULT=0
        MODE=RW
        #! Short the noise filter resistor to speed up the settling time
        #!     0 - noise filter resistor in place (default)
        #!     1 - Noise filter resistor bypassed
        #! should be connected to a 1~5uS at the power up
    ENDBITFIELD
    BITFIELD   SPDUP_LDO_VCOSXT
        POSITION=0
        DEFAULT=0
        MODE=RW
        #! Short the noise filter resistor to speed up the settling time
        #!     0 - noise filter resistor in place (default)
        #!     1 - Noise filter resistor bypassed
        #! should be connected to a 1~5uS at the power up
    ENDBITFIELD
ENDREGISTER

REGISTER    BIAS_CFG6    0x0098
    BITFIELD   SPDUP_LDO_AFE
        POSITION=8
        DEFAULT=0
        MODE=RW
        #! Short the noise filter resistor to speed up the settling time
        #!     0 - noise filter resistor in place (default)
        #!     1 - Noise filter resistor bypassed
        #! should be connected to a 1~5uS at the power up
    ENDBITFIELD
    BITFIELD   SPDUP_LDO_CPGN
        POSITION=7
        DEFAULT=0
        MODE=RW
        #! Short the noise filter resistor to speed up the settling time
        #!     0 - noise filter resistor in place (default)
        #!     1 - Noise filter resistor bypassed
        #! should be connected to a 1~5uS at the power up
    ENDBITFIELD
    BITFIELD   SPDUP_LDO_CPSXR
        POSITION=6
        DEFAULT=0
        MODE=RW
        #! Short the noise filter resistor to speed up the settling time
        #!     0 - noise filter resistor in place (default)
        #!     1 - Noise filter resistor bypassed
        #! should be connected to a 1~5uS at the power up
    ENDBITFIELD
    BITFIELD   SPDUP_LDO_CPSXT
        POSITION=5
        DEFAULT=0
        MODE=RW
        #! Short the noise filter resistor to speed up the settling time
        #!     0 - noise filter resistor in place (default)
        #!     1 - Noise filter resistor bypassed
        #! should be connected to a 1~5uS at the power up
    ENDBITFIELD
    BITFIELD   SPDUP_LDO_DIG
        POSITION=4
        DEFAULT=0
        MODE=RW
        #! Short the noise filter resistor to speed up the settling time
        #!     0 - noise filter resistor in place (default)
        #!     1 - Noise filter resistor bypassed
        #! should be connected to a 1~5uS at the power up
    ENDBITFIELD
    BITFIELD   SPDUP_LDO_DIGGN
        POSITION=3
        DEFAULT=0
        MODE=RW
        #! Short the noise filter resistor to speed up the settling time
        #!     0 - noise filter resistor in place (default)
        #!     1 - Noise filter resistor bypassed
        #! should be connected to a 1~5uS at the power up
    ENDBITFIELD
    BITFIELD   SPDUP_LDO_DIGSXR
        POSITION=2
        DEFAULT=0
        MODE=RW
        #! Short the noise filter resistor to speed up the settling time
        #!     0 - noise filter resistor in place (default)
        #!     1 - Noise filter resistor bypassed
        #! should be connected to a 1~5uS at the power up
    ENDBITFIELD
    BITFIELD   SPDUP_LDO_DIGSXT
        POSITION=1
        DEFAULT=0
        MODE=RW
        #! Short the noise filter resistor to speed up the settling time
        #!     0 - noise filter resistor in place (default)
        #!     1 - Noise filter resistor bypassed
        #! should be connected to a 1~5uS at the power up
    ENDBITFIELD
    BITFIELD   SPDUP_LDO_DIVGN
        POSITION=0
        DEFAULT=0
        MODE=RW
        #! Short the noise filter resistor to speed up the settling time
        #!     0 - noise filter resistor in place (default)
        #!     1 - Noise filter resistor bypassed
        #! should be connected to a 1~5uS at the power up
    ENDBITFIELD
ENDREGISTER

REGISTER    BIAS_CFG7    0x0099
    BITFIELD   RDIV_VCOSXR<7:0>
        POSITION=<15:8>
        DEFAULT=01100101
        MODE=RW
        #! Controls the output voltage of the LDO by setting the resistive
        #! voltage divider ratio. Default: 101
        #! Vout=860mV+3.92mV *RDIV
    ENDBITFIELD
    BITFIELD   RDIV_VCOSXT<7:0>
        POSITION=<7:0>
        DEFAULT=01100101
        MODE=RW
        #! Controls the output voltage of the LDO by setting the resistive
        #! voltage divider ratio. Default: 101
        #! Vout=860mV+3.92mV *RDIV
    ENDBITFIELD
ENDREGISTER

REGISTER    BIAS_CFG8    0x009A
    BITFIELD   RDIV_TXBUF<7:0>
        POSITION=<15:8>
        DEFAULT=01100101
        MODE=RW
        #! Controls the output voltage of the LDO by setting the resistive
        #! voltage divider ratio. Default: 101
        #! Vout=860mV+3.92mV *RDIV
    ENDBITFIELD
    BITFIELD   RDIV_VCOGN<7:0>
        POSITION=<7:0>
        DEFAULT=10001100
        MODE=RW
        #! Controls the output voltage of the LDO by setting the resistive
        #! voltage divider ratio. Default: 140
        #! Vout=860mV+3.92mV *RDIV
    ENDBITFIELD
ENDREGISTER

REGISTER    BIAS_CFG9    0x009B
    BITFIELD   RDIV_TLOB<7:0>
        POSITION=<15:8>
        DEFAULT=01100101
        MODE=RW
        #! Controls the output voltage of the LDO by setting the resistive
        #! voltage divider ratio. Default: 101
        #! Vout=860mV+3.92mV *RDIV
    ENDBITFIELD
    BITFIELD   RDIV_TPAD<7:0>
        POSITION=<7:0>
        DEFAULT=01100101
        MODE=RW
        #! Controls the output voltage of the LDO by setting the resistive
        #! voltage divider ratio. Default: 101
        #! Vout=860mV+3.92mV *RDIV
    ENDBITFIELD
ENDREGISTER

REGISTER    BIAS_CFG10    0x009C
    BITFIELD   RDIV_TIA12<7:0>
        POSITION=<15:8>
        DEFAULT=01100101
        MODE=RW
        #! Controls the output voltage of the LDO by setting the resistive
        #! voltage divider ratio. Default: 101
        #! Vout=860mV+3.92mV *RDIV
    ENDBITFIELD
    BITFIELD   RDIV_TIA14<7:0>
        POSITION=<7:0>
        DEFAULT=10001100
        MODE=RW
        #! Controls the output voltage of the LDO by setting the resistive
        #! voltage divider ratio. Default: 140
        #! Vout=860mV+3.92mV *RDIV
    ENDBITFIELD
ENDREGISTER

REGISTER    BIAS_CFG11    0x009D
    BITFIELD   RDIV_RXBUF<7:0>
        POSITION=<15:8>
        DEFAULT=01100101
        MODE=RW
        #! Controls the output voltage of the LDO by setting the resistive
        #! voltage divider ratio. Default: 101
        #! Vout=860mV+3.92mV *RDIV
    ENDBITFIELD
    BITFIELD   RDIV_TBB<7:0>
        POSITION=<7:0>
        DEFAULT=01100101
        MODE=RW
        #! Controls the output voltage of the LDO by setting the resistive
        #! voltage divider ratio. Default: 101
        #! Vout=860mV+3.92mV *RDIV
    ENDBITFIELD
ENDREGISTER

REGISTER    BIAS_CFG12    0x009E
    BITFIELD   RDIV_MXRFE<7:0>
        POSITION=<15:8>
        DEFAULT=01100101
        MODE=RW
        #! Controls the output voltage of the LDO by setting the resistive
        #! voltage divider ratio. Default: 101
        #! Vout=860mV+3.92mV *RDIV
    ENDBITFIELD
    BITFIELD   RDIV_RBB<7:0>
        POSITION=<7:0>
        DEFAULT=10001100
        MODE=RW
        #! Controls the output voltage of the LDO by setting the resistive
        #! voltage divider ratio. Default: 140
        #! Vout=860mV+3.92mV *RDIV
    ENDBITFIELD
ENDREGISTER

REGISTER    BIAS_CFG13    0x009F
    BITFIELD   RDIV_LNA12<7:0>
        POSITION=<15:8>
        DEFAULT=01100101
        MODE=RW
        #! Controls the output voltage of the LDO by setting the resistive
        #! voltage divider ratio. Default: 101
        #! Vout=860mV+3.92mV *RDIV
    ENDBITFIELD
    BITFIELD   RDIV_LNA14<7:0>
        POSITION=<7:0>
        DEFAULT=10001100
        MODE=RW
        #! Controls the output voltage of the LDO by setting the resistive
        #! voltage divider ratio. Default: 140
        #! Vout=860mV+3.92mV *RDIV
    ENDBITFIELD
ENDREGISTER

REGISTER    BIAS_CFG14    0x00A0
    BITFIELD   RDIV_DIVSXR<7:0>
        POSITION=<15:8>
        DEFAULT=01100101
        MODE=RW
        #! Controls the output voltage of the LDO by setting the resistive
        #! voltage divider ratio. Default: 101
        #! Vout=860mV+3.92mV *RDIV
    ENDBITFIELD
    BITFIELD   RDIV_DIVSXT<7:0>
        POSITION=<7:0>
        DEFAULT=01100101
        MODE=RW
        #! Controls the output voltage of the LDO by setting the resistive
        #! voltage divider ratio. Default: 101
        #! Vout=860mV+3.92mV *RDIV
    ENDBITFIELD
ENDREGISTER

REGISTER    BIAS_CFG15    0x00A1
    BITFIELD   RDIV_DIGSXT<7:0>
        POSITION=<15:8>
        DEFAULT=01100101
        MODE=RW
        #! Controls the output voltage of the LDO by setting the resistive
        #! voltage divider ratio. Default: 101
        #! Vout=860mV+3.92mV *RDIV
    ENDBITFIELD
    BITFIELD   RDIV_DIVGN<7:0>
        POSITION=<7:0>
        DEFAULT=01100101
        MODE=RW
        #! Controls the output voltage of the LDO by setting the resistive
        #! voltage divider ratio. Default: 101
        #! Vout=860mV+3.92mV *RDIV
    ENDBITFIELD
ENDREGISTER

REGISTER    BIAS_CFG16    0x00A2
    BITFIELD   RDIV_DIGGN<7:0>
        POSITION=<15:8>
        DEFAULT=01100101
        MODE=RW
        #! Controls the output voltage of the LDO by setting the resistive
        #! voltage divider ratio. Default: 101
        #! Vout=860mV+3.92mV *RDIV
    ENDBITFIELD
    BITFIELD   RDIV_DIGSXR<7:0>
        POSITION=<7:0>
        DEFAULT=01100101
        MODE=RW
        #! Controls the output voltage of the LDO by setting the resistive
        #! voltage divider ratio. Default: 101
        #! Vout=860mV+3.92mV *RDIV
    ENDBITFIELD
ENDREGISTER

REGISTER    BIAS_CFG17    0x00A3
    BITFIELD   RDIV_CPSXT<7:0>
        POSITION=<15:8>
        DEFAULT=01100101
        MODE=RW
        #! Controls the output voltage of the LDO by setting the resistive
        #! voltage divider ratio. Default: 101
        #! Vout=860mV+3.92mV *RDIV
    ENDBITFIELD
    BITFIELD   RDIV_DIG<7:0>
        POSITION=<7:0>
        DEFAULT=01100101
        MODE=RW
        #! Controls the output voltage of the LDO by setting the resistive
        #! voltage divider ratio. Default: 101
        #! Vout=860mV+3.92mV *RDIV
    ENDBITFIELD
ENDREGISTER

REGISTER    BIAS_CFG18    0x00A4
    BITFIELD   RDIV_CPGN<7:0>
        POSITION=<15:8>
        DEFAULT=01100101
        MODE=RW
        #! Controls the output voltage of the LDO by setting the resistive
        #! voltage divider ratio. Default: 101
        #! Vout=860mV+3.92mV *RDIV
    ENDBITFIELD
    BITFIELD   RDIV_CPSXR<7:0>
        POSITION=<7:0>
        DEFAULT=01100101
        MODE=RW
        #! Controls the output voltage of the LDO by setting the resistive
        #! voltage divider ratio. Default: 101
        #! Vout=860mV+3.92mV *RDIV
    ENDBITFIELD
ENDREGISTER

REGISTER    BIAS_CFG19    0x00A5
    BITFIELD   RDIV_SPIBUF<7:0>
        POSITION=<15:8>
        DEFAULT=01100101
        MODE=RW
        #! Controls the output voltage of the LDO by setting the resistive
        #! voltage divider ratio. Default: 101
        #! Vout=860mV+3.92mV *RDIV
    ENDBITFIELD
    BITFIELD   RDIV_AFE<7:0>
        POSITION=<7:0>
        DEFAULT=01100101
        MODE=RW
        #! Controls the output voltage of the LDO by setting the resistive
        #! voltage divider ratio. Default: 101
        #! Vout=860mV+3.92mV *RDIV
    ENDBITFIELD
ENDREGISTER

REGISTER    BIAS_CFG20    0x00A6
    BITFIELD   ISINK_SPIBUFF<2:0>
        POSITION=<15:13>
        DEFAULT=000
        MODE=RW
        #! Controls the SPIBUF LDO output resistive load.
        #!     0 - Off (default)
        #!     1 - 10kOhm
        #!     2 - 2.5kOhm
        #!     3 - 2kOhm
        #!     4 - 625Ohm
        #!     5 - 588Ohm
        #!     6 - 500Ohm
        #!     7 - 476Ohm
    ENDBITFIELD
    BITFIELD   SPDUP_LDO_SPIBUF
        POSITION=12
        DEFAULT=0
        MODE=RW
        #! Short the noise filter resistor to speed up the settling time
        #!     0 - Noise filter resistor in place (default)
        #!     1 - Noise filter resistor bypassed
        #! should be connected to a 1~5uS at the power up
    ENDBITFIELD
    BITFIELD   SPDUP_LDO_DIGIp2
        POSITION=11
        DEFAULT=0
        MODE=RW
        #! Short the noise filter resistor to speed up the settling time
        #!     0 - Noise filter resistor in place (default)
        #!     1 - Noise filter resistor bypassed
        #! should be connected to a 1~5uS at the power up
    ENDBITFIELD
    BITFIELD   SPDUP_LDO_DIGIp1
        POSITION=10
        DEFAULT=0
        MODE=RW
        #! Short the noise filter resistor to speed up the settling time
        #!     0 - Noise filter resistor in place (default)
        #!     1 - Noise filter resistor bypassed
        #! should be connected to a 1~5uS at the power up
    ENDBITFIELD
    BITFIELD   BYP_LDO_SPIBUF
        POSITION=9
        DEFAULT=0
        MODE=RW
        #! Bypass signal for the LDO
        #!     0 - Does not bypass. Normal LDO operation (default)
        #!     1 - Bypasses LDO. Connects Vinput to Voutput
    ENDBITFIELD
    BITFIELD   BYP_LDO_DIGIp2
        POSITION=8
        DEFAULT=0
        MODE=RW
        #! Bypass signal for the LDO
        #!     0 - Does not bypass. Normal LDO operation (default)
        #!     1 - Bypasses LDO. Connects Vinput to Voutput
    ENDBITFIELD
    BITFIELD   BYP_LDO_DIGIp1
        POSITION=7
        DEFAULT=0
        MODE=RW
        #! Bypass signal for the LDO
        #!     0 - Does not bypass. Normal LDO operation (default)
        #!     1 - Bypasses LDO. Connects Vinput to Voutput
    ENDBITFIELD
    BITFIELD   EN_LOADIMP_LDO_SPIBUF
        POSITION=6
        DEFAULT=0
        MODE=RW
        #! Enables the load dependent bias to optimize the load regulation
        #!     0 - Constant bias (default)
        #!     1 - Load depdent bias
    ENDBITFIELD
    BITFIELD   EN_LOADIMP_LDO_DIGIp2
        POSITION=5
        DEFAULT=0
        MODE=RW
        #! Enables the load dependent bias to optimize the load regulation
        #!     0 - Constant bias (default)
        #!     1 - Load depdent bias
    ENDBITFIELD
    BITFIELD   EN_LOADIMP_LDO_DIGIp1
        POSITION=4
        DEFAULT=0
        MODE=RW
        #! Enables the load dependent bias to optimize the load regulation
        #!     0 - Constant bias (default)
        #!     1 - Load depdent bias
    ENDBITFIELD
    BITFIELD   PD_LDO_SPIBUF
        POSITION=3
        DEFAULT=0
        MODE=RW
        #! Enables the LDO
        #!     0 - Block active (default)
        #!     1 - Power down
    ENDBITFIELD
    BITFIELD   PD_LDO_DIGIp2
        POSITION=2
        DEFAULT=0
        MODE=RW
        #! Enables the LDO
        #!     0 - Block active (default)
        #!     1 - Power down
    ENDBITFIELD
    BITFIELD   PD_LDO_DIGIp1
        POSITION=1
        DEFAULT=0
        MODE=RW
        #! Enables the LDO
        #!     0 - Block active (default)
        #!     1 - Power down
    ENDBITFIELD
    BITFIELD   EN_G_LDOP
        POSITION=0
        DEFAULT=1
        MODE=RW
        #! Enable control for all the LDO power downs
        #!     0 - All LDO modules powered down
        #!     1 - All LDO modules controlled by individual power down registers
    ENDBITFIELD
ENDREGISTER

REGISTER    BIAS_CFG21    0x00A7
    BITFIELD   RDIV_DIGIp2<7:0>
        POSITION=<15:8>
        DEFAULT=01100101
        MODE=RW
        #! Controls the output voltage of the LDO by setting the resistive
        #! voltage divider ratio. Default: 101
        #! Vout=860mV+3.92mV *RDIV
    ENDBITFIELD
    BITFIELD   RDIV_DIGIp1<7:0>
        POSITION=<7:0>
        DEFAULT=01100101
        MODE=RW
        #! Controls the output voltage of the LDO by setting the resistive
        #! voltage divider ratio. Default: 101
        #! Vout=860mV+3.92mV *RDIV
    ENDBITFIELD
ENDREGISTER

REGISTER    BIST0    0x00A8
    BITFIELD   BSIGT<6:0>
        POSITION=<15:9>
        DEFAULT=0000000
        MODE=RW
        #! BIST signature, Transmitter, LSB. Default: 0 (Register is used in production test only).
    ENDBITFIELD
    BITFIELD   BSTATE
        POSITION=8
        DEFAULT=0
        MODE=RW
        #! BIST state indicator (read only). (Register is used in production test only) .
        #!     0 - BIST is not running (default)
        #!     1 - BIST in progress
    ENDBITFIELD
    BITFIELD   EN_SDM_TSTO_SXT
        POSITION=6
        DEFAULT=0
        MODE=RW
        #! Enables the SDM_TSTO<12:0> outputs which will buffer the SDM outputs (inputs to the frequency divider) for testing purposes.
        #!     0 - all outputs are grounded (default)
        #!     1 - SDM_TSTO active
    ENDBITFIELD
    BITFIELD   EN_SDM_TSTO_SXR
        POSITION=5
        DEFAULT=0
        MODE=RW
        #! Enables the SDM_TSTO<12:0> outputs which will buffer the SDM outputs (inputs to the frequency divider) for testing purposes.
        #!     0 - all outputs are grounded (default)
        #!     1 - SDM_TSTO active
    ENDBITFIELD
    BITFIELD   EN_SDM_TSTO_CGEN
        POSITION=4
        DEFAULT=0
        MODE=RW
        #! Enables the SDM_TSTO<12:0> outputs which will buffer the SDM outputs (inputs to the frequency divider) for testing purposes.
        #!     0 - all outputs are grounded (default)
        #!     1 - SDM_TSTO active
    ENDBITFIELD
    BITFIELD   BENC
        POSITION=3
        DEFAULT=0
        MODE=RW
        #! Enables CGEN BIST. (Register is used in production test only) .
        #!     0 - disabled (default)
        #!     1 - enabled
    ENDBITFIELD
    BITFIELD   BENR
        POSITION=2
        DEFAULT=0
        MODE=RW
        #! Enables receiver BIST. (Register is used in production test only) .
        #!     0 - disabled (default)
        #!     1 - enabled
    ENDBITFIELD
    BITFIELD   BENT
        POSITION=1
        DEFAULT=0
        MODE=RW
        #! Enables transmitter BIST. (Register is used in production test only) .
        #!     0 - disabled (default)
        #!     1 - enabled
    ENDBITFIELD
    BITFIELD   BSTART
        POSITION=0
        DEFAULT=0
        MODE=RW
        #! Starts delta sigma built in self test. Keep it at 1 one at least three clock cycles. (Register is used in production test only) .
        #!     0 - (default)
        #!     0-to-1 - positive edge activates BIST
    ENDBITFIELD
ENDREGISTER

REGISTER    BIST1    0x00A9
    BITFIELD   BSIGT<22:7>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=R
        #! BIST signature, Transmitter, MSB (read only). (Register is used in production test only) .
    ENDBITFIELD
ENDREGISTER

REGISTER    BIST2    0x00AA
    BITFIELD   BSIGR<22:7>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=R
        #! BIST signature, Receiver, MSB (read only). (Register is used in production test only) .
    ENDBITFIELD
ENDREGISTER

REGISTER    BIST3    0x00AB
    BITFIELD   BSIGC<8:0>
        POSITION=<15:7>
        DEFAULT=000000000
        MODE=R
        #! BIST signature, CGEN , LSB (read only). (Register is used in production test only) .
    ENDBITFIELD
    BITFIELD   BSIGR<22:16>
        POSITION=<6:0>
        DEFAULT=0000000
        MODE=R
        #! BIST signature, Receiver, MSB (read only). (Register is used in production test only) .
    ENDBITFIELD
ENDREGISTER

REGISTER    BIST4    0x00AC
    BITFIELD   BSIGC<22:7>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=R
        #! BIST signature, Receiver, MSB (read only). (Register is used in production test only) .
    ENDBITFIELD
ENDREGISTER

REGISTER    CDS_CFG0    0x00AD
    BITFIELD   CDS_MCLK2<1:0>
        POSITION=<15:14>
        DEFAULT=00
        MODE=RW
        #! MCLK2 clock delay.
        #!     00 - delay by 400ps (default)
        #!     01 - delay by 500ps
        #!     10 - delay by 600ps
        #!     11 - delay by 700ps
    ENDBITFIELD
    BITFIELD   CDS_MCLK1<1:0>
        POSITION=<13:12>
        DEFAULT=00
        MODE=RW
        #! MCLK1 clock delay.
        #!     00 - delay by 400ps (default)
        #!     01 - delay by 500ps
        #!     10 - delay by 600ps
        #!     11 - delay by 700ps
    ENDBITFIELD
    BITFIELD   CDSN_TXBTSP
        POSITION=9
        DEFAULT=1
        MODE=RW
        #! TX TSPB clock inversion control.
        #!     0 - Clock is inverted
        #!     1 - Clock is not inverted (default)
    ENDBITFIELD
    BITFIELD   CDSN_TXATSP
        POSITION=8
        DEFAULT=1
        MODE=RW
        #! TX TSPA clock inversion control.
        #!     0 - Clock is inverted
        #!     1 - Clock is not inverted (default)
    ENDBITFIELD
    BITFIELD   CDSN_RXBTSP
        POSITION=7
        DEFAULT=1
        MODE=RW
        #! RX TSPB clock inversion control.
        #!     0 - Clock is inverted
        #!     1 - Clock is not inverted (default)
    ENDBITFIELD
    BITFIELD   CDSN_RXATSP
        POSITION=6
        DEFAULT=1
        MODE=RW
        #! RX TSPA clock inversion control.
        #!     0 - Clock is inverted
        #!     1 - Clock is not inverted (default)
    ENDBITFIELD
    BITFIELD   CDSN_TXBLML
        POSITION=5
        DEFAULT=1
        MODE=RW
        #! TX LMLB clock inversion control.
        #!     0 - Clock is inverted
        #!     1 - Clock is not inverted (default)
    ENDBITFIELD
    BITFIELD   CDSN_TXALML
        POSITION=4
        DEFAULT=1
        MODE=RW
        #! TX LMLA clock inversion control.
        #!     0 - Clock is inverted
        #!     1 - Clock is not inverted (default)
    ENDBITFIELD
    BITFIELD   CDSN_RXBLML
        POSITION=3
        DEFAULT=1
        MODE=RW
        #! RX LMLB clock inversion control.
        #!     0 - Clock is inverted
        #!     1 - Clock is not inverted (default)
    ENDBITFIELD
    BITFIELD   CDSN_RXALML
        POSITION=2
        DEFAULT=1
        MODE=RW
        #! RX LMLA clock inversion control.
        #!     0 - Clock is inverted
        #!     1 - Clock is not inverted (default)
    ENDBITFIELD
    BITFIELD   CDSN_MCLK2
        POSITION=1
        DEFAULT=1
        MODE=RW
        #! MCLK2 clock inversion control.
        #!     0 - Clock is inverted
        #!     1 - Clock is not inverted (default)
    ENDBITFIELD
    BITFIELD   CDSN_MCLK1
        POSITION=0
        DEFAULT=1
        MODE=RW
        #! MCLK1 clock inversion control.
        #!     0 - Clock is inverted
        #!     1 - Clock is not inverted (default)
    ENDBITFIELD
ENDREGISTER

REGISTER    CDS_CFG1    0x00AE
    BITFIELD   CDS_TXBTSP<1:0>
        POSITION=<15:14>
        DEFAULT=00
        MODE=RW
        #! TX TSP B clock delay.
        #!     00 - delay by 400ps (default)
        #!     01 - delay by 500ps
        #!     10 - delay by 600ps
        #!     11 - delay by 700ps
    ENDBITFIELD
    BITFIELD   CDS_TXATSP<1:0>
        POSITION=<13:12>
        DEFAULT=00
        MODE=RW
        #! TX TSP A clock delay.
        #!     00 - delay by 400ps (default)
        #!     01 - delay by 500ps
        #!     10 - delay by 600ps
        #!     11 - delay by 700ps
    ENDBITFIELD
    BITFIELD   CDS_RXBTSP<1:0>
        POSITION=<11:10>
        DEFAULT=00
        MODE=RW
        #! RX TSP B clock delay.
        #!     00 - delay by 200ps (default)
        #!     01 - delay by 500ps
        #!     10 - delay by 800ps
        #!     11 - delay by 1100ps
    ENDBITFIELD
    BITFIELD   CDS_RXATSP<1:0>
        POSITION=<9:8>
        DEFAULT=00
        MODE=RW
        #! RX TSP A clock delay.
        #!     00 - delay by 200ps (default)
        #!     01 - delay by 500ps
        #!     10 - delay by 800ps
        #!     11 - delay by 1100ps
    ENDBITFIELD
    BITFIELD   CDS_TXBLML<1:0>
        POSITION=<7:6>
        DEFAULT=00
        MODE=RW
        #! TX LML B clock delay.
        #!     00 - delay by 400ps (default)
        #!     01 - delay by 500ps
        #!     10 - delay by 600ps
        #!     11 - delay by 700ps
    ENDBITFIELD
    BITFIELD   CDS_TXALML<1:0>
        POSITION=<5:4>
        DEFAULT=00
        MODE=RW
        #! TX LML A clock delay.
        #!     00 - delay by 400ps (default)
        #!     01 - delay by 500ps
        #!     10 - delay by 600ps
        #!     11 - delay by 700ps
    ENDBITFIELD
    BITFIELD   CDS_RXBLML<1:0>
        POSITION=<3:2>
        DEFAULT=00
        MODE=RW
        #! RX LML B clock delay.
        #!     00 - delay by 200ps (default)
        #!     01 - delay by 500ps
        #!     10 - delay by 800ps
        #!     11 - delay by 1100ps
    ENDBITFIELD
    BITFIELD   CDS_RXALML<1:0>
        POSITION=<1:0>
        DEFAULT=00
        MODE=RW
        #! RX LML A clock delay.
        #!     00 - delay by 200ps (default)
        #!     01 - delay by 500ps
        #!     10 - delay by 800ps
        #!     11 - delay by 1100ps
    ENDBITFIELD
ENDREGISTER

REGISTER    TRF_CFG    0x0100
    BITFIELD   EN_LOWBWLOMX_TMX_TRF
        POSITION=15
        DEFAULT=0
        MODE=RW
        #! Controls the high pass pole frequency of the
        #! RC biasing the gate of the mixer switches.
        #!     0 - High band - bias resistor 3K (default)
        #!     1 - Low band - bias resistor 30K
    ENDBITFIELD
    BITFIELD   EN_NEXTTX_TRF
        POSITION=14
        DEFAULT=0
        MODE=RW
        #! Enables the daisy change LO buffer going from TRF_1 to TRF2
        #!     0 - Buffer disabled (SISO) (default)
        #!     1 - Buffer enabled (MIMO)
    ENDBITFIELD
    BITFIELD   EN_AMPHF_PDET_TRF<1:0>
        POSITION=<13:12>
        DEFAULT=11
        MODE=RW
        #! Enables the TXPAD power detector preamplifier
        #!     3 - Preamp gain 25dB (default)
        #!     2 - Do not use
        #!     1 - Preamp gain 7dB
        #!     0 - Preamp gain -10dB
    ENDBITFIELD
    BITFIELD   LOADR_PDET_TRF<1:0>
        POSITION=<11:10>
        DEFAULT=01
        MODE=RW
        #! Controls the resistive load of the Power detector
        #!     0 - R_DIFF 5K||2.5K||1.25K
        #!     1 - R_DIFF 5K||1.25K (default)
        #!     2 - R_DIFF 5K||2.5K
        #!     3 - R_DIGG 5K
    ENDBITFIELD
    BITFIELD   PD_PDET_TRF
        POSITION=3
        DEFAULT=1
        MODE=RW
        #! Power down signal for Power Detector
        #!     0 - Enabled
        #!     1 - Powered down (default)
    ENDBITFIELD
    BITFIELD   PD_TLOBUF_TRF
        POSITION=2
        DEFAULT=0
        MODE=RW
        #! Power down signal for TX LO buffer
        #!     0 - Enabled (default)
        #!     1 - Powered down
    ENDBITFIELD
    BITFIELD   PD_TXPAD_TRF
        POSITION=1
        DEFAULT=0
        MODE=RW
        #! Power down signal for TXPAD
        #!     0 - Enabled (default)
        #!     1 - Powered down
    ENDBITFIELD
    BITFIELD   EN_G_TRF
        POSITION=0
        DEFAULT=1
        MODE=RW
        #! Enable control for all the TRF_1 power downs
        #!     0 - All TRF_1 modules powered down
        #!     1 - All TRF_1 modules controlled by individual power down registers (default)
    ENDBITFIELD
ENDREGISTER

REGISTER    TRF_TXPAD    0x0101
    BITFIELD   F_TXPAD_TRF<2:0>
        POSITION=<15:13>
        DEFAULT=011
        MODE=RW
        #! Controls the switched capacitor at the TXPAD output. Is used for fine tuning of the TXPAD output. Default: 3
    ENDBITFIELD
    BITFIELD   L_LOOPB_TXPAD_TRF<1:0>
        POSITION=<12:11>
        DEFAULT=11
        MODE=RW
        #! Controls the loss of the of the loopback path at the TX side
        #!     0 - Loss=0dB
        #!     1 - Loss=-1.4dB
        #!     2 - Loss=-3.3dB
        #!     3 - Loss=-4.3dB (default)
    ENDBITFIELD
    BITFIELD   LOSS_LIN_TXPAD_TRF<4:0>
        POSITION=<10:6>
        DEFAULT=00000
        MODE=RW
        #! Controls the gain of the linearizing part of the TXPAD Default: 0
        #!     0<=Loss<=10 - Pout=Pout_max-Loss
        #!     11<=Loss<31 - Pout=Pout_max-10-2*(Loss-10)
        #! Ideally LOSS_LIN = LOSS_MAIN
    ENDBITFIELD
    BITFIELD   LOSS_MAIN_TXPAD_TRF<4:0>
        POSITION=<5:1>
        DEFAULT=00000
        MODE=RW
        #! Controls the gain & output power of the TXPAD. Default: 0
        #!     0<=Loss<=10 - Pout=Pout_max-Loss
        #!     11<=Loss<31 - Pout=Pout_max-10-2*(Loss-10)
    ENDBITFIELD
    BITFIELD   EN_LOOPB_TXPAD_TRF
        POSITION=0
        DEFAULT=0
        MODE=RW
        #! Enables the TXPAD loopback path
        #!     0 - Loopback disabled (default)
        #!     1 - Loopback enabled
    ENDBITFIELD
ENDREGISTER

REGISTER    TRF_TXPADBIAS    0x0102
    BITFIELD   GCAS_GNDREF_TXPAD_TRF
        POSITION=15
        DEFAULT=0
        MODE=RW
        #! Controls if the TXPAD cascode transistor gate bias is referred to VDD or GND.
        #!     0 - VDD referred (default)
        #!     1 - GNDS referred
    ENDBITFIELD
    BITFIELD   ICT_LIN_TXPAD_TRF<4:0>
        POSITION=<14:10>
        DEFAULT=01100
        MODE=RW
        #! Control the bias current of the linearization section of the TXPAD. Default: 12
        #! I_bias=I_bias_nominal * ICT/12
    ENDBITFIELD
    BITFIELD   ICT_MAIN_TXPAD_TRF<4:0>
        POSITION=<9:5>
        DEFAULT=01100
        MODE=RW
        #! Control the bias current of the main gm section of the TXPAD. Default: 12
        #! I_bias=I_bias_nominal * ICT/12
    ENDBITFIELD
    BITFIELD   VGCAS_TXPAD_TRF<4:0>
        POSITION=<4:0>
        DEFAULT=00000
        MODE=RW
        #! Controls the bias voltage at the gate of TXPAD cascade. Default: 0
        #! vgcas=(VGCAS_TXOAD/12)*100u*10K, when GCAS_GNDREF=1
        #! vgcas=VDD18-(VGCAS_TXOAD/12)*100u*7.5K, when GCAS_GNDREF=0
    ENDBITFIELD
ENDREGISTER

REGISTER    TRF_LOBAND    0x0103
    BITFIELD   SEL_BAND1_TRF
        POSITION=11
        DEFAULT=1
        MODE=RW
        #! Enable signal for TXFE, band 1
        #!     0 - Disabled
        #!     1 - Enabled (default)
    ENDBITFIELD
    BITFIELD   SEL_BAND2_TRF
        POSITION=10
        DEFAULT=0
        MODE=RW
        #! Enable signal for TXFE, band 2
        #!     0 - Disabled (default)
        #!     1 - Enabled
    ENDBITFIELD
    BITFIELD   LOBIASN_TXM_TRF<4:0>
        POSITION=<9:5>
        DEFAULT=10000
        MODE=RW
        #! Controls the bias at the gate of the mixer NMOS switch. Default: 16
        #! Vgate_bias=Vth_nmos+25K*LOBIASN/12*20u
    ENDBITFIELD
    BITFIELD   LOBIASP_TXX_TRF<4:0>
        POSITION=<4:0>
        DEFAULT=10000
        MODE=RW
        #! Controls the bias at the gate of the mixer PMOS switch. Default: 18
        #! Vgate_bias=Vth_pmos-25K*LOBIASP/12*20u
    ENDBITFIELD
ENDREGISTER

REGISTER    TRF_CDC    0x0104
    BITFIELD   CDC_I_TRF<3:0>
        POSITION=<7:4>
        DEFAULT=1000
        MODE=RW
        #! Trims the duty cycle in I channel. Default = 8;
    ENDBITFIELD
    BITFIELD   CDC_Q_TRF<3:0>
        POSITION=<3:0>
        DEFAULT=1000
        MODE=RW
        #! Trims the duty cycle in Q channel. Default = 8;
    ENDBITFIELD
ENDREGISTER

REGISTER    TBB_CFG    0x0105
    BITFIELD   STATPULSE_TBB
        POSITION=15
        DEFAULT=0
        MODE=RW
        #! This is a narrow start-up pulse of more than 1us width. Default: 0
    ENDBITFIELD
    BITFIELD   LOOPB_TBB<2:0>
        POSITION=<14:12>
        DEFAULT=000
        MODE=RW
        #! This controls which signal is connected to the loopback output pins loopb as follows:
        #! Bits [1:0]:
        #!     0 - output is disconnected (high impedance) loop back is disabled. (default)
        #!     1 - DAC current output is routed to the loopb pins.
        #!     2 - low band ladder output is routed to the output.
        #!     3 - main TBB output is routed to the loopb outputs.
        #! Bit [2] (swaps the I Q channels):
        #!     0 TBB output I goes to loopb_2 path and Q goes to loopb_1 path. (default)
        #!     1 - TBB output I goes to loopb_1 path and Q goes to loopb_2 path.
        #! Note: when both the lowpass ladder and real pole are powered down, the output of
        #! the active highband biquad is routed to the loopb outputs on setting 3.
    ENDBITFIELD
    BITFIELD   PD_LPFH_TBB
        POSITION=4
        DEFAULT=0
        MODE=RW
        #! This selectively powers down the LPFH_TBB biquad. Please note, the LPFH_TBB is powered down if any of the following is true:
        #! PD_LPFLAB_TBB=0 & PD_LPFS5_TBB=0, or, PD_TBB = 1, or PD_LPFH_TBB = 1.
        #!     0 - Active (default)
        #!     1 - powered down
    ENDBITFIELD
    BITFIELD   PD_LPFIAMP_TBB
        POSITION=3
        DEFAULT=0
        MODE=RW
        #! This selectively powers down the LPFIAMP_TBB front-end current amp of the transmitter base band.
        #! Please note, the LPFIAMP_TBB is powered down if any of the following is true:
        #! PD_TBB = 1, or PD_LPFIAMP_TBB = 1
        #!     0 - Active (default)
        #!     1 - powered down
    ENDBITFIELD
    BITFIELD   PD_LPFLAD_TBB
        POSITION=2
        DEFAULT=1
        MODE=RW
        #! This selectively powers down the LPFLAD_TBB low pass  ladder filter of the transmitter base band.
        #! Please note, the ladder is powered down if any of the following is true:
        #! PD_TBB = 1, or PD_LPFLAD_TBB = 1
        #!     0 - Active
        #!     1 - powered down (default)
    ENDBITFIELD
    BITFIELD   PD_LPFS5_TBB
        POSITION=1
        DEFAULT=1
        MODE=RW
        #! This selectively powers down the LPFS5_TBB low pass real-pole filter of the transmitter base band.
        #! Please note, the real-pole stage is powered down if any of the following is true:
        #! PD_TBB = 1, or PD_LPFS5_TBB = 1
        #!     0 - Active
        #!     1 - powered down (default)
    ENDBITFIELD
    BITFIELD   EN_G_TBB
        POSITION=0
        DEFAULT=1
        MODE=RW
        #! Enable control for all the TBB_TOP power downs
        #!     0 - All TBB_TOP modules powered down
        #!     1 - All TBB_TOP modules may be selectively turned off (default)
    ENDBITFIELD
ENDREGISTER

REGISTER    TBB_ICT0    0x0106
    BITFIELD   ICT_LPFS5_F_TBB<4:0>
        POSITION=<14:10>
        DEFAULT=01100
        MODE=RW
        #! This controls the operational amplifier's output stage bias current of the low band real pole filter of the transmitter's base band. Default: 12
    ENDBITFIELD
    BITFIELD   ICT_LPFS5_PT_TBB<4:0>
        POSITION=<9:5>
        DEFAULT=01100
        MODE=RW
        #! This controls the operational amplifier's input stage bias current of the low band real pole filter of the transmitter's base band. Default: 12
    ENDBITFIELD
    BITFIELD   ICT_LPF_H_PT_TBB<4:0>
        POSITION=<4:0>
        DEFAULT=01100
        MODE=RW
        #! This controls the operational amplifiers input stage bias reference current of the high band low pass filter of the transmitter's base band (LPFH_TBB). Default: 12
    ENDBITFIELD
ENDREGISTER

REGISTER    TBB_ICT1    0x0107
    BITFIELD   ICT_LPFH_F_TBB<4:0>
        POSITION=<14:10>
        DEFAULT=01100
        MODE=RW
        #! This controls the operational amplifiers output stage bias reference current of the high band low pass filter of the transmitter's base band (LPFH_TBB). Default: 12
    ENDBITFIELD
    BITFIELD   ICT_LPFLAD_F_TBB<4:0>
        POSITION=<9:5>
        DEFAULT=01100
        MODE=RW
        #! This controls the operational amplifiers' output stages bias reference current of the low band ladder filter of the transmitter's base band. Default: 12
    ENDBITFIELD
    BITFIELD   ICT_LPFLAD_PT_TBB<4:0>
        POSITION=<4:0>
        DEFAULT=01100
        MODE=RW
        #! This controls the operational amplifiers' input stages bias reference current of the low band ladder filter of the transmitter's base band. Default: 12
    ENDBITFIELD
ENDREGISTER

REGISTER    TBB_IAMP    0x0108
    BITFIELD   CG_IAMP_TBB<5:0>
        POSITION=<15:10>
        DEFAULT=100101
        MODE=RW
        #! This controls the front-end gain of the TBB. For a given
        #! gain value, this control value varies with the set TX mode. After resistance
        #! calibration, the following table gives the nominal values for each frequency setting.
        #! However, this table is to be updated and corrected after calibration. Default: 37
        #! Low Band:
        #!     5 - when 2.4MHz
        #!     7 - when 2.74MHz
        #!     12 - when 5.5MHz
        #!     18 - when 8.2MHz
        #!     24 - when 11MHz
        #! High Band:
        #!     18 - when 18.5MHz
        #!     37 - when 38MHz
        #!     54 - when 54MHz
    ENDBITFIELD
    BITFIELD   ICT_IAMP_FRP_TBB<4:0>
        POSITION=<9:5>
        DEFAULT=01100
        MODE=RW
        #! This controls the reference bias current of the IAMP main bias current sources. Default: 12
    ENDBITFIELD
    BITFIELD   ICT_IAMP_GG_FRP_TBB<4:0>
        POSITION=<4:0>
        DEFAULT=01100
        MODE=RW
        #! This controls the reference bias current of the IAMP's cascode transistors gate voltages that set the IAMP's input voltage level.
        #! The IAMP's input is connected to the DAC output. Default: 12
    ENDBITFIELD
ENDREGISTER

REGISTER    TBB_LPF0    0x0109
    BITFIELD   RCAL_LPFH_TBB<7:0>
        POSITION=<15:8>
        DEFAULT=01100001
        MODE=RW
        #! This controls the value of the equivalent resistance of the resistor banks of the biquad filter stage (of the high band section) of the
        #! transmitter base band(TBB). Default: 97
        #! Following is a nominal values table that are corrected for any process variation after calibration:
        #! RCAL_LPFH_TBB=(p1*(freq^4)+ p2*(freq^3)+ p3*(freq^2) +p4*freq+p5)
        #! p1= 1.10383261611112E-06
        #! p2= -0.000210800032517545
        #! p3= 0.0190494874803309
        #! p4= 1.43317445923528
        #! p5= -47.6950779298333
    ENDBITFIELD
    BITFIELD   RCAL_LPFLAD_TBB<7:0>
        POSITION=<7:0>
        DEFAULT=11000001
        MODE=RW
        #! This controls the value of the equivalent resistance of the resistor banks of the low pass filter ladder (of the low band section) of the
        #! transmitter base band (TBB). Default: 193
        #! Following is a nominal values table that are corrected for any process variations
        #! after calibration.
        #! RCAL_LPFLAD_TBB=(p1*(freq^4)+ p2*(freq^3)+ p3*(freq^2) +p4*freq+p5)
        #! p1= 1.29858903647958E-16
        #! p2= -0.000110746929967704
        #! p3= 0.00277593485991029
        #! p4= 21.0384293169607
        #! p5= -48.4092606238297
    ENDBITFIELD
ENDREGISTER

REGISTER    TBB_LPF1    0x010A
    BITFIELD   TSTIN_TBB<1:0>
        POSITION=<15:14>
        DEFAULT=00
        MODE=RW
        #! This control selects where the input test signal
        #! (vinp/n_aux_bbq/i) is routed to as well as disabling the route.
        #!     0 - Disabled. Test signal is not routed any where. (default)
        #!     1 - Test signal is routed to the input of the Highband Filter.
        #!     2 - Test signal is routed to the input of the LowBand Filter.
        #!     3 - Test signal is routed to the input of the current amplifier.
    ENDBITFIELD
    BITFIELD   BYPLADDER_TBB
        POSITION=13
        DEFAULT=0
        MODE=RW
        #! This signal by passes the LPF ladder of TBB and directly
        #! connects the output of current amplifier to the null port of the real pole stage of TBB
        #! low pass filter.
        #!     1 - bypass is active
        #!     0 - bypass is inactive (default)
    ENDBITFIELD
    BITFIELD   CCAL_LPFLAD_TBB<4:0>
        POSITION=<12:8>
        DEFAULT=10000
        MODE=RW
        #! A common control signal for all the capacitor
        #! banks of TBB filters (including the ladder, real pole, and the high band biquad). It is
        #! the calibrated value of the banks control that sets the value of the banks' equivalent
        #! capacitor to their respective nominal values. Default: 16
    ENDBITFIELD
    BITFIELD   RCAL_LPFS5_TBB<7:0>
        POSITION=<7:0>
        DEFAULT=01001100
        MODE=RW
        #! This controls the value of the equivalent resistance
        #! of the resistor banks of the real pole filter stage (of the low band section) of the
        #! transmitter base band (TBB). Following is a nominal values table that are corrected
        #! for any process variation after calibration. Default: 76.
        #! RCAL_LPFS5_TBB=(p1*(freq^4)+ p2*(freq^3)+ p3*(freq^2) +p4*freq+p5)
        #! p1= 1.93821841029921E-15
        #! p2= -0.0429694461214244
        #! p3= 0.253501254059498
        #! p4= 88.9545445989649
        #! p5= -48.0847491316861
    ENDBITFIELD
ENDREGISTER

REGISTER    TBB_LPF_BYP    0x010B
    BITFIELD   RESRV_TBB<1:0>
        POSITION=<2:1>
        DEFAULT=00
        MODE=RW
        #! Reserved
    ENDBITFIELD
    BITFIELD   R5_LPF_BYP_TBB
        POSITION=0
        DEFAULT=0
        MODE=RW
        #! 0 - Normal LPFS5_TBB low pass real-pole filter operation. (default)
        #! 1 - LPFS5_TBB low pass real-pole filter acts as a buffer.
    ENDBITFIELD
ENDREGISTER

REGISTER    RFE_CFG0    0x010C
    BITFIELD   CDC_I_RFE<3:0>
        POSITION=<15:12>
        DEFAULT=0100
        MODE=RW
        #! Trims the duty cycle in I channel. Default = 8;
    ENDBITFIELD
    BITFIELD   CDC_Q_RFE<3:0>
        POSITION=<11:8>
        DEFAULT=0100
        MODE=RW
        #! Trims the duty cycle in Q channel. Default = 8;
    ENDBITFIELD
    BITFIELD   PD_LNA_RFE
        POSITION=7
        DEFAULT=1
        MODE=RW
        #! Power control signal for LNA_RFE
        #!     0 - block active
        #!     1 - block powered down (default)
    ENDBITFIELD
    BITFIELD   PD_RLOOPB_1_RFE
        POSITION=6
        DEFAULT=1
        MODE=RW
        #! Power control signal for RXFE loopback 1
        #!     0 - block active
        #!     1 - block powered down (default)
    ENDBITFIELD
    BITFIELD   PD_RLOOPB_2_RFE
        POSITION=5
        DEFAULT=1
        MODE=RW
        #! Power control signal for RXFE loopback 2
        #!     0 - block active
        #!     1 - block powered down (default)
    ENDBITFIELD
    BITFIELD   PD_MXLOBUF_RFE
        POSITION=4
        DEFAULT=1
        MODE=RW
        #! Power control signal for RXFE mixer lo buffer
        #!     0 - block active
        #!     1 - block powered down (default)
    ENDBITFIELD
    BITFIELD   PD_QGEN_RFE
        POSITION=3
        DEFAULT=1
        MODE=RW
        #! Power control signal for RXFE quadrature LO generator
        #!     0 - block active
        #!     1 - block powered down (default)
    ENDBITFIELD
    BITFIELD   PD_RSSI_RFE
        POSITION=2
        DEFAULT=1
        MODE=RW
        #! Power control signal for RXFE RSSI
        #!     0 - block active
        #!     1 - block powered down (default)
    ENDBITFIELD
    BITFIELD   PD_TIA_RFE
        POSITION=1
        DEFAULT=0
        MODE=RW
        #! Power control signal for RXFE TIA
        #!     0 - block active (default)
        #!     1 - block powered down
    ENDBITFIELD
    BITFIELD   EN_G_RFE
        POSITION=0
        DEFAULT=1
        MODE=RW
        #! Enable control for all the RFE_1 power downs
        #!     0 - All RFE modules powered down
        #!     1 - All RFE modules controlled by individual power down registers
    ENDBITFIELD
ENDREGISTER

REGISTER    RFE_CFG1    0x010D
    BITFIELD   SEL_PATH_RFE<1:0>
        POSITION=<8:7>
        DEFAULT=01
        MODE=RW
        #! Selects the active path of the RXFE
        #!     0 - No path active
        #!     1 - LNAH path active (default)
        #!     2 - LNAL path active
        #!     3 - LNAW path active
    ENDBITFIELD
    BITFIELD   EN_DCOFF_RXFE_RFE
        POSITION=6
        DEFAULT=0
        MODE=RW
        #! Enables the DCOFFSET block for the RXFE
        #!     0 - disabled (default)
        #!     1 - enabled
    ENDBITFIELD
    BITFIELD   EN_INSHSW_LB1_RFE
        POSITION=4
        DEFAULT=1
        MODE=RW
        #! Enables the input shorting switch at the input of the
        #! loopback 1 (in parallel with LNAL mixer). Switch ON resistance < 3ohm
        #!     0 - switch OFF
        #!     1 - switch ON (default)
        #! Should be '1' when RXFE loopback1 is NOT active
    ENDBITFIELD
    BITFIELD   EN_INSHSW_LB2_RFE
        POSITION=3
        DEFAULT=1
        MODE=RW
        #! Enables the input shorting switch at the input of the
        #! loopback 2 (in parallel with LNAW mixer)
        #! Switch ON resistance < 3ohm
        #!     0 - switch OFF
        #!     1 - switch ON (default)
        #! Should be '1' when RXFE Loopback2 is NOT active
    ENDBITFIELD
    BITFIELD   EN_INSHSW_L_RFE
        POSITION=2
        DEFAULT=1
        MODE=RW
        #! Enables the input shorting switch at the input of the
        #! LNAL
        #! Switch ON resistance < 3ohm
        #!     0 - switch OFF
        #!     1 - switch ON (default)
        #! Should be '1' when LNAL is NOT active
    ENDBITFIELD
    BITFIELD   EN_INSHSW_W_RFE
        POSITION=1
        DEFAULT=1
        MODE=RW
        #! Enables the input shorting switch at the input of the
        #! LNAW. Switch ON resistance < 3ohm
        #!     0 - switch OFF
        #!     1 - switch ON (default)
        #! Should be '1' when LNAW is NOT active
    ENDBITFIELD
    BITFIELD   EN_NEXTRX_RFE
        POSITION=0
        DEFAULT=0
        MODE=RW
        #! Enables the daisy chain LO buffer going from RXFE1 to
        #! RXFE2.
        #!     0 - SISO (default)
        #!     1 - MIMO
    ENDBITFIELD
ENDREGISTER

REGISTER    RFE_DCOFF    0x010E
    BITFIELD   DCOFFI_RFE<6:0>
        POSITION=<13:7>
        DEFAULT=1000000
        MODE=RW
        #! Controls DC offset at the output of the TIA by injecting
        #! current t o the input of the TIA. (For I side). Default: 64
        #!     DCOFFSETx_RFE<6> - sign.
        #!     DCOFFSETx_RFE<5:0> - magnitude. When DCOFFSETx_RFE<5:0>=0,
        #!                          no current injection - no added noise.
    ENDBITFIELD
    BITFIELD   DCOFFQ_RFE<6:0>
        POSITION=<6:0>
        DEFAULT=1000000
        MODE=RW
        #! Controls DC offset at the output of the TIA by injecting
        #! current t o the input of the TIA. (For Q side). Default: 64
        #!     DCOFFSETx_RFE<6> - sign.
        #!     DCOFFSETx_RFE<5:0> - magnitude. When DCOFFSETx_RFE<5:0>=0,
        #!                         no current injection - no added noise.
    ENDBITFIELD
ENDREGISTER

REGISTER    RFE_ICT0    0x010F
    BITFIELD   ICT_LOOPB_RFE<4:0>
        POSITION=<14:10>
        DEFAULT=01100
        MODE=RW
        #! Controls the reference current of the RXFE loopback
        #! amplifier. Default: 12
        #! I supply = I supply nominal *(ICT/12).
    ENDBITFIELD
    BITFIELD   ICT_TIAMAIN_RFE<4:0>
        POSITION=<9:5>
        DEFAULT=01100
        MODE=RW
        #! Controls the reference current of the RXFE TIA first
        #! stage. Default: 12
        #! I supply = I supply nominal *(ICT/12).
    ENDBITFIELD
    BITFIELD   ICT_TIAOUT_RFE<4:0>
        POSITION=<4:0>
        DEFAULT=01100
        MODE=RW
        #! Controls the reference current of the RXFE TIA 2nd
        #! stage. Default: 12
        #! I supply = I supply nominal *(ICT/12).
    ENDBITFIELD
ENDREGISTER

REGISTER    RFE_ICT1    0x0110
    BITFIELD   ICT_LNACMO_RFE<4:0>
        POSITION=<14:10>
        DEFAULT=00010
        MODE=RW
        #! Controls the current generating LNA output
        #! common mode voltage. Default: 2
    ENDBITFIELD
    BITFIELD   ICT_LNA_RFE<4:0>
        POSITION=<9:5>
        DEFAULT=01100
        MODE=RW
        #! Controls the current of the LNA core. Default: 12
        #! Block current = Nominal current * (ICT / 12)
    ENDBITFIELD
    BITFIELD   ICT_LODC_RFE<4:0>
        POSITION=<4:0>
        DEFAULT=10100
        MODE=RW
        #! Controls the DC of the mixer LO signal at the gate of
        #! the mixer switches. Default: 20
        #! Vgate=Vth+3.5Kohm*20uA*(ICT/12)
        #! If Vgate is too high, the voltage saturates and further increasing this ICT
        #! will not increase Vgate. Possible over voltage on mixer gates.
    ENDBITFIELD
ENDREGISTER

REGISTER    RFE_CAP0    0x0111
    BITFIELD   CAP_RXMXO_RFE<4:0>
        POSITION=<9:5>
        DEFAULT=00100
        MODE=RW
        #! Control the decoupling cap at the output of the RX
        #! Mixer. Default: 4
        #! SE cap = (CAP_RXMXO_RFE +1) * 80fF
    ENDBITFIELD
    BITFIELD   CGSIN_LNA_RFE<4:0>
        POSITION=<4:0>
        DEFAULT=00011
        MODE=RW
        #! Controls the cap parallel with the LNA input NMOS
        #! CGS to control the Q of the matching circuit and provides trade off between gain/NF
        #! and IIP. The higher the frequency, the lower CGSIN_LNA_RFE should be. Also, the
        #! higher CGSIN, the lower the Q, The lower the gain, the higher the NF, and the
        #! higher the IIP3
        #!     0 - for 3500MHz
        #!     1 - for 2600MHz
        #!     3 - for 1900MHz (default)
        #!     6 - for 800MHz
    ENDBITFIELD
ENDREGISTER

REGISTER    RFE_CAP1    0x0112
    BITFIELD   CCOMP_TIA_RFE<3:0>
        POSITION=<15:12>
        DEFAULT=1100
        MODE=RW
        #! Compensation capacitor for TIA. This is a function of
        #! CFB_TIA_RFE. Default: 12.
        #! When G_TIA_RFE==1,
        #! CCOMP_TIA_RFE=int(CFB_TIA_RFE/100) +1, where max value is 15
        #! When G_TIA_RFE==3 || G_TIA_RFE==2,
        #! CCOMP_TIA_RFE=int(CFB_TIA_RFE/100), where max value is 15
    ENDBITFIELD
    BITFIELD   CFB_TIA_RFE<11:0>
        POSITION=<11:0>
        DEFAULT=000011100110
        MODE=RW
        #! Feedback capacitor for TIA. Controls the 3dB BW of the
        #! TIA. Should be set with calibration through digital base band. Default: 230
        #! When G_TIA_RFE==1,
        #! CFB_TIA_RFE=int(5400/freq -15), where value range [0:4095]
        #! When G_TIA_RFE==3 || G_TIA_RFE==2,
        #! CFB_TIA_RFE=int(1680/freq -10), where value range [0:4095]
    ENDBITFIELD
ENDREGISTER

REGISTER    RFE_GAIN    0x0113
    BITFIELD   G_LNA_RFE<3:0>
        POSITION=<9:6>
        DEFAULT=1111
        MODE=RW
        #! Controls the gain of the LNA
        #!     15 - Gmax (default)
        #!     14 - Gmax-1
        #!     13 - Gmax-2
        #!     12 - Gmax-3
        #!     11 - Gmax-4
        #!     10 - Gmax-5
        #!     9 - Gmax-6
        #!     8 - Gmax-9
        #!     7 - Gmax-12
        #!     6 - Gmax-15
        #!     5 - Gmax-18
        #!     4 - Gmax-21
        #!     3 - Gmax-24
        #!     2 - Gmax-27
        #!     1 - Gmax-30
    ENDBITFIELD
    BITFIELD   G_RXLOOPB_RFE<3:0>
        POSITION=<5:2>
        DEFAULT=0000
        MODE=RW
        #! Controls RXFE loopback gain
        #!     15 - Gmax
        #!     14 - Gmax-0.5
        #!     13 - Gmax-1
        #!     12 - Gmax-1.6
        #!     11 - Gmax-2.4
        #!     10 - Gmax-3
        #!     9 - Gmax-4
        #!     8 - Gmax-5
        #!     7 - Gmax-6.2
        #!     6 - Gmax-7.5
        #!     5 - Gmax-9
        #!     4 - Gmax-11
        #!     3 - Gmax-14
        #!     2 - Gmax-17
        #!     1 - Gmax-24
        #!     0 - Gmax-40 (default)
        #! Should be '0' when actual LNAs are working
    ENDBITFIELD
    BITFIELD   G_TIA_RFE<1:0>
        POSITION=<1:0>
        DEFAULT=11
        MODE=RW
        #! Controls the Gain of the TIA.
        #!     3 - Gmax (default)
        #!     2 - Gmax-3
        #!     1 - Gmax-12
        #!     0 - Not allowed
    ENDBITFIELD
ENDREGISTER

REGISTER    RFE_TIA    0x0114
    BITFIELD   RCOMP_TIA_RFE<3:0>
        POSITION=<8:5>
        DEFAULT=0100
        MODE=RW
        #! Controls the compensation resistors of the TIA
        #! operational amplifier. Default: 4.
        #! RCOMP_TIA_RFE=int(15-CFB_TIA_RFE*2/100), where min value is 0
    ENDBITFIELD
    BITFIELD   RFB_TIA_RFE<4:0>
        POSITION=<4:0>
        DEFAULT=01101
        MODE=RW
        #! RCOMP_TIA_RFE=int(15- CFB_TIA_RFE*2/100), where min value is 0
        #! RFB_TIA_RFE_(1, 2)[4:0]: Sets the feedback resistor to the nominal value.
        #! This is set using the rppolywo calibration code from the bias block
        #! (BIAS_RPPOLY_calibration). Default: 13
    ENDBITFIELD
ENDREGISTER

REGISTER    RBB_PD    0x0115
    BITFIELD   EN_LB_LPFH_RBB
        POSITION=15
        DEFAULT=0
        MODE=RW
        #! This is the loopback enable signal that is enabled when
        #! high band LPFH_RBB is selected for the loopback path that connects the loopb_lpfi
        #! inputs to the virtual ground of the LPFH_RBB block.
        #!     1 - enabled
        #!     0 - disabled (default)
        #! Note: Only one of EN_LB_LPFH_RBB/EN_LB_LPFL_RBB can be
        #! enabled concurrently.
    ENDBITFIELD
    BITFIELD   EN_LB_LPFL_RBB
        POSITION=14
        DEFAULT=0
        MODE=RW
        #! This is the loopback enable signal that is enabled when
        #! the high-band low pass filter LPFL_RBB is selected for the loopback path that
        #! connects the loopb_lpf inputs to the virtual ground of the LPFL_RBB block.
        #!     1 - enabled
        #!     0 - disabled (default)
        #! Note: Only one of EN_LB_LPFH_RBB/EN_LB_LPFL_RBB can be
        #! enabled concurrently.
    ENDBITFIELD
    BITFIELD   PD_LPFH_RBB
        POSITION=3
        DEFAULT=1
        MODE=RW
        #! Power down of the LPFH block.
        #!     0 - active
        #!     1 - powered down (default)
    ENDBITFIELD
    BITFIELD   PD_LPFL_RBB
        POSITION=2
        DEFAULT=0
        MODE=RW
        #! Power down of the LPFL block.
        #!     0 - active (default)
        #!     1 - powered down
    ENDBITFIELD
    BITFIELD   PD_PGA_RBB
        POSITION=1
        DEFAULT=0
        MODE=RW
        #! Power down of the PGA block.
        #!     0 - active (default)
        #!     1 - powered down
    ENDBITFIELD
    BITFIELD   EN_G_RBB
        POSITION=0
        DEFAULT=1
        MODE=RW
        #! Enable control for all the RBB_1 power downs
        #!     0 - All RBB modules powered down
        #!     1 - All RBB modules controlled by individual power down registers (default)
    ENDBITFIELD
ENDREGISTER

REGISTER    RBB_LPF0    0x0116
    BITFIELD   R_CTL_LPF_RBB<4:0>
        POSITION=<15:11>
        DEFAULT=10000
        MODE=RW
        #! Controls the absolute value of the resistance of the
        #! RC time constant of the RBB_LPF blocks (both Low and High).
        #! This value is corrected during the calibration process. Default: 16
    ENDBITFIELD
    BITFIELD   RCC_CTL_LPFH_RBB<2:0>
        POSITION=<10:8>
        DEFAULT=001
        MODE=RW
        #! Controls the stability passive compensation of
        #! the LPFH_RBB operational amplifier. Default: 1
        #!     1 - when rxMode is 37MHz,
        #!     4 - when rxMode 66MHz,
        #!     7 - when rxMode 108MHz
    ENDBITFIELD
    BITFIELD   C_CTL_LPFH_RBB<7:0>
        POSITION=<7:0>
        DEFAULT=10000000
        MODE=RW
        #! Controls the capacitance value of the RC time
        #! constant of RBB_LPFH and it varies with the respective rxMode from 20MHz to
        #! 108MHz.
        #! Its value is equal to (120*50M/rxMode)*ccor-cfrH; where: rxMode is the receiver
        #! mode of operation 20MHz up to 108MHz, ccor is determined by calibration and cfrH
        #! is valued at 50.
        #! This control signal can be determined by lookup tables generated during the
        #! calibration phase. Default: 128
    ENDBITFIELD
ENDREGISTER

REGISTER    RBB_LPF1    0x0117
    BITFIELD   RCC_CTL_LPFL_RBB<2:0>
        POSITION=<13:11>
        DEFAULT=101
        MODE=RW
        #! Controls the stability passive compensation of
        #! the LPFL_RBB operational amplifier.
        #!     0 - when rxMode is 1.4MHz,
        #!     1 - when 3MHz
        #!     2 - when 5MHz
        #!     3 - when 10MHz
        #!     4 - when 15MHz
        #!     5 - when 20MHz (default)
    ENDBITFIELD
    BITFIELD   C_CTL_LPFL_RBB<10:0>
        POSITION=<10:0>
        DEFAULT=00000001100
        MODE=RW
        #! Controls the capacitance value of the RC time constant of RBB_LPFL and it varies with the respective rxMode from 1.4MHz to 20MHz.
        #! Its value is equal to (120*18M/rxMode)*ccor-cfrL ; where: rxMode is the receiver mode of operation from 1.4MHz up to 20MHz, ccor is determined by calibration and ctrL is valued at 103.
        #! This control signal can be determined by lookup tables generated during the calibration phase. Default: 12
    ENDBITFIELD
ENDREGISTER

REGISTER    RBB_LPFICT    0x0118
    BITFIELD   INPUT_CTL_PGA_RBB<2:0>
        POSITION=<15:13>
        DEFAULT=000
        MODE=RW
        #! There are a total of four different differential
        #! inputs to the PGA. Only one of them is active at a time.
        #!     0 - when LPFL input is selected (rxMode <=20MHz); The output of the LPFL_RBB block is selected as input. (default)
        #!     1 - when LPFH input is selected (rxMode > 20MHz); The output of the LPFH_RBB is selected as input.
        #!     2 - when bypassing the LPF blocks; The input signal to either RBB_LPFH  or RBB_LPFL is bypassed and connected directly to the PGA bypass input.
        #!     3 - when connecting loopb_tx (the loop back from TBB) to the input of the  PGA.
        #!     4 - when loopb_pkd (Loop back path from the peak detector) is selected.
    ENDBITFIELD
    BITFIELD   ICT_LPF_IN_RBB<4:0>
        POSITION=<9:5>
        DEFAULT=01100
        MODE=RW
        #! Controls the reference bias current of the input stage
        #! of the operational amplifier used in RBB_LPF blocks (Low or High). Must increase
        #! up to 24 when a strong close blocker is detected to maintain the linearity
        #! performance. Default: 12
    ENDBITFIELD
    BITFIELD   ICT_LPF_OUT_RBB<4:0>
        POSITION=<4:0>
        DEFAULT=01100
        MODE=RW
        #! Controls the reference bias current of the output
        #! stage of the operational amplifier used in RBB_LPF blocks (low or High). Must
        #! increase up to 24 when a strong close blocker is detected to maintain the linearity
        #! performance. Default: 12
    ENDBITFIELD
ENDREGISTER

REGISTER    RBB_PGA0    0x0119
    BITFIELD   OSW_PGA_RBB
        POSITION=15
        DEFAULT=0
        MODE=RW
        #! There are two instances of the PGA circuit in the design.
        #! The output of the RBB_LPF blocks are connected the input of these PGA blocks
        #! (common). The output of one of them is connected to two pads pgaoutn and
        #! pgaoutp and the output of the other PGA is connected directly to the ADC input.
        #!     0 - the PGA connected to the ADC is selected; (default)
        #!     1 - the PGA connected to the output pads is selected instead.
    ENDBITFIELD
    BITFIELD   ICT_PGA_OUT_RBB<4:0>
        POSITION=<14:10>
        DEFAULT=00110
        MODE=RW
        #! Controls the output stage reference bias current of the operational amplifier used in the PGA circuit. Must increase up to 12 when a strong close blocker is detected or when operating at the high band frequencies to maintain the linearity performance. Default: 6
    ENDBITFIELD
    BITFIELD   ICT_PGA_IN_RBB<4:0>
        POSITION=<9:5>
        DEFAULT=00110
        MODE=RW
        #! Controls the input stage reference bias current of the operational amplifier used in the PGA circuit. Must increase up to 12 when a strong close blocker is detected or when operating at the high band frequencies to maintain the linearity performance. Default: 6
    ENDBITFIELD
    BITFIELD   G_PGA_RBB<4:0>
        POSITION=<4:0>
        DEFAULT=01011
        MODE=RW
        #! This is the gain of the PGA. The gain is adaptively set to maintain signal swing of 0.6Vpkd at the output of the PGA. The value of the gain is: Gain(dB) = -12+G_PGA_RBB. Default: 11
    ENDBITFIELD
ENDREGISTER

REGISTER    RBB_PGA1    0x011A
    BITFIELD   RCC_CTL_PGA_RBB<4:0>
        POSITION=<13:9>
        DEFAULT=10111
        MODE=RW
        #! Controls the stability passive compensation of the PGA_RBB operational amplifier. Its value is equal to: (430f*(0.65**(G_PGA_RBB/10))-110.35f)/20.4516f + 16 when ICT_PGA is 12. An offline/off chip lookup table can be generated and stored. Default: 23
    ENDBITFIELD
    BITFIELD   C_CTL_PGA_RBB<7:0>
        POSITION=<7:0>
        DEFAULT=00001101
        MODE=RW
        #! Control the value of the feedback capacitor of the PGA that is used to help against the parasitic cap at the virtual node for stability.
        #!     3 - when 0<=G_PGA_RBB<8
        #!     2 - when 8<=G_PGA_RBB<13 (default)
        #!     1 - when 13<=G_PGA_RBB<21
        #!     0 - when 21<=G_PGA_RBB
    ENDBITFIELD
ENDREGISTER

REGISTER    SXT_SXR_CFG0    0x011C
    BITFIELD   RESET_N
        POSITION=15
        DEFAULT=1
        MODE=RW
        #! Resets SX. A pulse should be used in the start-up to reset
        #!     0 - Reset
        #!     1 - Normal operation (default)
    ENDBITFIELD
    BITFIELD   SPDUP_VCO
        POSITION=14
        DEFAULT=0
        MODE=RW
        #! Bypasses the noise filter resistor for fast settling time. It should be connected to a 1uS pulse
        #!     0 - speed up disabled (noise filter resistor active) (default)
        #!     1 - speed up enabled (noise filter resistor shorted)
    ENDBITFIELD
    BITFIELD   BYPLDO_VCO
        POSITION=13
        DEFAULT=1
        MODE=RW
        #! Controls the bypass signal for the SX LDO
        #!     0 - LDO active
        #!     1 - LDO bypassed (input/output of the SX LDO shorted) (default)
    ENDBITFIELD
    BITFIELD   EN_COARSEPLL
        POSITION=12
        DEFAULT=0
        MODE=RW
        #! Enable signal for coarse tuning block
        #!     0 - Coarse tuning disabled (default)
        #!     1 - Coarse tuning enabled
    ENDBITFIELD
    BITFIELD   CURLIM_VCO
        POSITION=11
        DEFAULT=1
        MODE=RW
        #! Enables the output current limitation in the VCO regulator
        #!     0 - Current limit disabled
        #!     1 - Current limit enabled (default)
    ENDBITFIELD
    BITFIELD   EN_DIV2_DIVPROG
        POSITION=10
        DEFAULT=1
        MODE=RW
        #! Enables additional DIV2 prescaler at the input of the Programmable divider. The core of programmable divider in the SX feedback divider works up to 5.5GHz. For FVCO>5.5GHz, the prescaler is needed to lower the input frequency to DIVPROG_SX. Shadow register.
        #!     0 - DIVPROG input =Fvco [Fvco=Fref*((INT_SDM_SX+4)+FRAC_SDM)
        #!     1 - DIVPROG input =Fvco/2 [Fvco=2*Fref*((INT_SDM_SX+4)+FRAC_SDM) (default)
    ENDBITFIELD
    BITFIELD   EN_INTONLY_SDM
        POSITION=9
        DEFAULT=0
        MODE=RW
        #! Enables INTEGER-N mode of the SX
        #!     0 - Frac-N mode (default)
        #!     1 - INT-N mode
    ENDBITFIELD
    BITFIELD   EN_SDM_CLK
        POSITION=8
        DEFAULT=1
        MODE=RW
        #! Enables/Disables SDM clock. In INT-N mode or for noise testing, SDM clock can be disabled
        #!     0 - SDM clock disabled
        #!     1 - SDM clock enabled (default)
    ENDBITFIELD
    BITFIELD   PD_FBDIV
        POSITION=7
        DEFAULT=0
        MODE=RW
        #! Power down the feedback divider block.
        #!     0 - block active (default)
        #!     1 - block powered down
    ENDBITFIELD
    BITFIELD   PD_LOCH_T2RBUF
        POSITION=6
        DEFAULT=1
        MODE=RW
        #! Power down for LO buffer from SXT to SXR. To be active only in the TDD mode. In TX part only.
        #!     0 - block active
        #!     1 - block powered down (default)
    ENDBITFIELD
    BITFIELD   PD_CP
        POSITION=5
        DEFAULT=0
        MODE=RW
        #! Power down for Charge Pump
        #!     0 - block active (default)
        #!     1 - block powered down
    ENDBITFIELD
    BITFIELD   PD_FDIV
        POSITION=4
        DEFAULT=0
        MODE=RW
        #! Power down for forward frequency divider and divider chain of the LO chain.
        #!     0 - blocks active (default)
        #!     1 - blocks powered down
    ENDBITFIELD
    BITFIELD   PD_SDM
        POSITION=3
        DEFAULT=0
        MODE=RW
        #! Power down for SDM
        #!     0 - block active (default)
        #!     1 - block powered down
    ENDBITFIELD
    BITFIELD   PD_VCO_COMP
        POSITION=2
        DEFAULT=0
        MODE=RW
        #! Power down for VCO comparator
        #!     0 - block active (default)
        #!     1 - block powered down
    ENDBITFIELD
    BITFIELD   PD_VCO
        POSITION=1
        DEFAULT=1
        MODE=RW
        #! Power down for VCO
        #!     0 - block active
        #!     1 - block powered down (default)
    ENDBITFIELD
    BITFIELD   EN_G
        POSITION=0
        DEFAULT=1
        MODE=RW
        #! Enable control for all the SX power downs
        #!     0 - All SXT modules powered down
        #!     1 - All SXT modules controlled by individual power down registers (default)
    ENDBITFIELD
ENDREGISTER

REGISTER    SXT_SXR_FRACL    0x011D
    BITFIELD   FRAC_SDM_L<15:0>
        POSITION=<15:0>
        DEFAULT=0000010000000000
        MODE=RW
        #! Fractional control of the division ratio LSB. Default: 1024
        #! =2^20*[Fvco/(Fref * 2^ EN_DIV2_DIVPROG_(SXR, SXT)) -
        #! int(Fvco/(Fref * 2^ EN_DIV2_DIVPROG_(SXR, SXT)))]
    ENDBITFIELD
ENDREGISTER

REGISTER    SXT_SXR_FRACH    0x011E
    BITFIELD   INT_SDM<9:0>
        POSITION=<13:4>
        DEFAULT=0001111000
        MODE=RW
        #! Controls Integer section of the division ratio
        #! INT_SDM= int(Fvco/2^(EN_DIV2_DIVPROG_SX)/Fref)-4
        #! Default: 120
    ENDBITFIELD
    BITFIELD   FRAC_SDM_H<3:0>
        POSITION=<3:0>
        DEFAULT=0000
        MODE=RW
        #! Fractional control of the division ratio MSB.
    ENDBITFIELD
ENDREGISTER

REGISTER    SXT_SXR_CFG1    0x011F
    BITFIELD   PW_DIV2_LOCH<2:0>
        POSITION=<14:12>
        DEFAULT=011
        MODE=RW
        #! Trims the duty cycle of DIV2 LOCH. Only works when forward divider is dividing by at least 2 (excluding quadrature block division). If
        #! in bypass mode, this does not work. Default: 3
    ENDBITFIELD
    BITFIELD   PW_DIV4_LOCH<2:0>
        POSITION=<11:9>
        DEFAULT=011
        MODE=RW
        #! Trims the duty cycle of DIV4 LOCH. Only works when forward divider is dividing by at least 4 (excluding quadrature block division). If
        #! in bypass mode, this does not work. Default: 3
    ENDBITFIELD
    BITFIELD   DIV_LOCH<2:0>
        POSITION=<8:6>
        DEFAULT=001
        MODE=RW
        #! Controls the division ratio in the LOCH_DIV. There is additional DIV/2 in the quadrature generator
        #!    Flo = Fvco / divRatio_LOCH / 2
        #!    divRatio_LOCH = 2^(DIV_LOCH_SX)
        #! Note: Value 111 not allowed.
        #!    Shadow register. Default: 1
    ENDBITFIELD
    BITFIELD   TST_SX<2:0>
        POSITION=<5:3>
        DEFAULT=000
        MODE=RW
        #! Controls the test mode of PLLs. TST signal lines are shared between all PLLs (CGEN, RX and TX). Only one TST signal of any PLL should be active at a given time.
        #!     0 - TST disabled; RSSI analog outputs enabled if RSSI blocks active and
        #!         when all PLL test signals are off (default)
        #!     1 - tstdo[0]=VCO/20 clock*; tstdo[1]=VCO/40 clock*; tstao = High
        #!         impedance;
        #!     2 - tstdo[0]=SDM clock; tstdo[1]= feedback divider output; tstao = VCO
        #!         tune through a 60kOhm resistor;
        #!     3 - tstdo[0]=Reference clock; tstdo[1]= feedback divider output; tstao =
        #!         VCO tune through a 10kOhm resistor;
        #!     4 - tstdo[0]= High impedance; tstdo[1]= High impedance; tstao = High
        #!         impedance;
        #!     5 - tstdo[0]=Charge pump Down signal; tstdo[1]=Charge pump Up signal;
        #!         tstao = High impedance;
        #!     6 - tstdo[0]= High impedance; tstdo[1]= High impedance; tstao = VCO
        #!         tune through a 60kOhm resistor;
        #!     7 - tstdo[0]= High impedance; tstdo[1]= High impedance; tstao = VCO
        #!         tune through a 10kOhm resistor;
        #! if TST_SX[2]=1 --> VCO_TSTBUF active generating VCO_TST_DIV20
        #! and VCO_TST_DIV40
        #! * When EN_DIV2_DIVPROG_(SXR, SXT) is active, the division ratio must
        #! be multiplied by 2 (40/80);
    ENDBITFIELD
    BITFIELD   SEL_SDMCLK
        POSITION=2
        DEFAULT=0
        MODE=RW
        #! Selects between the feedback divider output and Fref for SDM
        #!     0 - CLK CLK_DIV (default)
        #!     1 - CLK CLK_REF
    ENDBITFIELD
    BITFIELD   SX_DITHER_EN
        POSITION=1
        DEFAULT=0
        MODE=RW
        #! Enabled dithering in SDM
        #!     0 - Disabled (default)
        #!     1 - Enabled
    ENDBITFIELD
    BITFIELD   REV_SDMCLK
        POSITION=0
        DEFAULT=0
        MODE=RW
        #! Reverses the SDM clock
        #!     0 - direct (default)
        #!     1 - reversed (after INV)
    ENDBITFIELD
ENDREGISTER

REGISTER    SXT_SXR_VCO_BIAS    0x0120
    BITFIELD   VDIV_VCO<7:0>
        POSITION=<15:8>
        DEFAULT=10111001
        MODE=RW
        #! Controls VCO LDO output voltage. Default: 185
        #! Vout(VCO_LDO)=VDD18_VCO* [ (29.1/(29.1 + 233/(VDIV_VCO_SX+2)))]
        #! 185 --> Vout(VCO_LDO)=1.55V (VDD18_VCO=1.72)
    ENDBITFIELD
    BITFIELD   ICT_VCO<7:0>
        POSITION=<7:0>
        DEFAULT=10000000
        MODE=RW
        #! Scales the VCO bias current from 0 to 2.5xInom
        #! Default: 128
    ENDBITFIELD
ENDREGISTER

REGISTER    SXT_SXR_VCO_CFG    0x0121
    BITFIELD   RSEL_LDO_VCO<4:0>
        POSITION=<15:11>
        DEFAULT=10000
        MODE=RW
        #! Set the reference voltage that supplies bias
        #! voltage of switch-cap array and varactor. Default: 16
        #! Vref=60uA * 180kOhm / RSEL_LDO_VCO
    ENDBITFIELD
    BITFIELD   CSW_VCO<7:0>
        POSITION=<10:3>
        DEFAULT=10000000
        MODE=RW
        #! Coarse control of VCO frequency, 0 for lowest frequency and 255 for highest. This control is set by SX_SWC_calibration. Shadow register. Default: 128
    ENDBITFIELD
    BITFIELD   SEL_VCO<1:0>
        POSITION=<2:1>
        DEFAULT=10
        MODE=RW
        #! Selects the active VCO. It is set by SX_SWC_calibration. Shadow register.
        #!     0 - VCOL
        #!     1 - VCOM
        #!     2 - VCOH (default)
        #!     3 - Not Valid
    ENDBITFIELD
    BITFIELD   COARSE_START
        POSITION=0
        DEFAULT=0
        MODE=RW
        #! Control signal for coarse tuning algorithm (SX_SWC_calibration). Default: 0
    ENDBITFIELD
ENDREGISTER

REGISTER    SXT_SXR_PFDCP    0x0122
    BITFIELD   RZ_CTRL<1:0>
        POSITION=<15:14>
        DEFAULT=00
        MODE=RW
        #! Controls the PLL LPF zero resistor values:
        #!     0 - Rzero = 20kOhm (default)
        #!     1 - Rzero = 8kOhm
        #!     2 - Rzero = 4kOhm
        #!     3 - LPF resistors are in bypass mode (<100 Ohm)
    ENDBITFIELD
    BITFIELD   CMPLO_CTRL
        POSITION=13
        DEFAULT=0
        MODE=RW
        #! 0 - Low treshold is set to 0.18V (default)
        #! 1 - Low treshold is set to 0.1V
    ENDBITFIELD
    BITFIELD   REVPH_PFD
        POSITION=12
        DEFAULT=0
        MODE=RW
        #! Reverse the pulses of PFD. It can be used to reverse the polarity of the PLL loop (positive feedback to negative feedback). Default: 0
    ENDBITFIELD
    BITFIELD   IOFFSET_CP<5:0>
        POSITION=<11:6>
        DEFAULT=010100
        MODE=RW
        #! Scales the offset current of the charge pump, 0-->63. This current is used in Frac-N mode to create an offset in the CP response and avoid the non-linear section. Default: 20
        #! ioffset=0.243uA * IOFFSET_CP_SX
        #! ioffset/ipulse=4/(INT_SDM_SX+4) [First estimation]
    ENDBITFIELD
    BITFIELD   IPULSE_CP<5:0>
        POSITION=<5:0>
        DEFAULT=010100
        MODE=RW
        #! Scales the pulse current of the charge pump, 0-->63. Default: 20
        #! ipulse=2.312uA * IPULSE_CP_SX
    ENDBITFIELD
ENDREGISTER

REGISTER    SXT_SXR_COMP_LPF    0x0123
    BITFIELD   COARSE_STEPDONE
        POSITION=15
        DEFAULT=0
        MODE=R
        #! Read only.
    ENDBITFIELD
    BITFIELD   COARSEPLL_COMPO
        POSITION=14
        DEFAULT=0
        MODE=R
        #! Read only.
    ENDBITFIELD
    BITFIELD   VCO_CMPHO
        POSITION=13
        DEFAULT=0
        MODE=R
        #! Compares Vtune value to a predefined value of 920mV. Read only register.
        #!     0 - Vtune voltage level is higher than CMPHO threshold voltage of 920mV
        #!     1 - Vtune voltage level is lower than CMPHO threshold voltage of 920mV
    ENDBITFIELD
    BITFIELD   VCO_CMPLO
        POSITION=12
        DEFAULT=0
        MODE=R
        #! Compares Vtune value to a predefined value of 180mV. Read only register.
        #!     0 - Vtune voltage level is higher than CMPLO threshold voltage of 180mV
        #!     1 - Vtune voltage level is lower than CMPLO threshold voltage of 180mV
    ENDBITFIELD
    BITFIELD   CP2_PLL<3:0>
        POSITION=<11:8>
        DEFAULT=0110
        MODE=RW
        #! Controls the value of CP2 (cap from CP output to GND) in the PLL filter. Default: 6
        #! cp2=CP2_PLL_SX*6*387fF
    ENDBITFIELD
    BITFIELD   CP3_PLL<3:0>
        POSITION=<7:4>
        DEFAULT=0111
        MODE=RW
        #! Controls the value of CP3 (cap from VCO Vtune input to GND) in the PLL filter. Default: 7
        #! cp3=CP3_PLL_SX*6*980fF
    ENDBITFIELD
    BITFIELD   CZ<3:0>
        POSITION=<3:0>
        DEFAULT=1011
        MODE=RW
        #! Controls the value of CZ (Zero capacitor) in the PLL filter. Default: 11
        #! cz=CZ_PLL_SX*8*5.88pF
    ENDBITFIELD
ENDREGISTER

REGISTER    TRX_EN_DIR    0x0124
    BITFIELD   EN_DIR
        POSITION=4
        DEFAULT=0
        MODE=RW
        #! Enables direct control of PDs and ENs for SXR/SXT module.
        #!     0 - direct control disabled (default)
        #!     1 - direct control enabled
    ENDBITFIELD
    BITFIELD   EN_DIR_RBB
        POSITION=3
        DEFAULT=0
        MODE=RW
        #! Enables direct control of PDs and ENs for RBB(1, 2) module.
        #!     0 - direct control disabled (default)
        #!     1 - direct control enabled
    ENDBITFIELD
    BITFIELD   EN_DIR_RFE
        POSITION=2
        DEFAULT=0
        MODE=RW
        #! Enables direct control of PDs and ENs for RFE(1, 2) module.
        #!     0 - direct control disabled (default)
        #!     1 - direct control enabled
    ENDBITFIELD
    BITFIELD   EN_DIR_TBB
        POSITION=1
        DEFAULT=0
        MODE=RW
        #! Enables direct control of PDs and ENs for TBB(1, 2) module.
        #!     0 - direct control disabled (default)
        #!     1 - direct control enabled
    ENDBITFIELD
    BITFIELD   EN_DIR_TRF
        POSITION=0
        DEFAULT=0
        MODE=RW
        #! Enables direct control of PDs and ENs for TRF(1, 2) module.
        #!     0 - direct control disabled (default)
        #!     1 - direct control enabled
    ENDBITFIELD
ENDREGISTER

REGISTER    TRX_GAIN_CFG1    0x0125
    BITFIELD   CG_IAMP_TBB<5:0>
        POSITION=<15:10>
        DEFAULT=100101
        MODE=RW
        #! This controls the front-end gain of the TBB. For a given
        #! gain value, this control value varies with the set TX mode. After resistance
        #! calibration, the following table gives the nominal values for each frequency setting.
        #! However, this table is to be updated and corrected after calibration. Default: 37
        #! Low Band:
        #!     5 - when 2.4MHz
        #!     7 - when 2.74MHz
        #!     12 - when 5.5MHz
        #!     18 - when 8.2MHz
        #!     24 - when 11MHz
        #! High Band:
        #!     18 - when 18.5MHz
        #!     37 - when 38MHz
        #!     54 - when 54MHz
    ENDBITFIELD
    BITFIELD   LOSS_LIN_TXPAD_TRF<4:0>
        POSITION=<9:5>
        DEFAULT=00000
        MODE=RW
        #! Controls the gain of the linearizing part of the TXPAD Default: 0
        #!     0<=Loss<=10 - Pout=Pout_max-Loss
        #!     11<=Loss<31 - Pout=Pout_max-10-2*(Loss-10)
        #! Ideally LOSS_LIN = LOSS_MAIN
    ENDBITFIELD
    BITFIELD   LOSS_MAIN_TXPAD_TRF<4:0>
        POSITION=<4:0>
        DEFAULT=00000
        MODE=RW
        #! Controls the gain & output power of the TXPAD. Default: 0
        #!     0<=Loss<=10 - Pout=Pout_max-Loss
        #!     11<=Loss<31 - Pout=Pout_max-10-2*(Loss-10)
    ENDBITFIELD
ENDREGISTER

REGISTER    TRX_GAIN_CFG2    0x0126
    BITFIELD   C_CTL_PGA_RBB<1:0>
        POSITION=<12:11>
        DEFAULT=10
        MODE=RW
        #! Control the value of the feedback capacitor of the PGA that is used to help against the parasitic cap at the virtual node for stability.
        #!     3 - when 0<=G_PGA_RBB<8
        #!     2 - when 8<=G_PGA_RBB<13 (default)
        #!     1 - when 13<=G_PGA_RBB<21
        #!     0 - when 21<=G_PGA_RBB
    ENDBITFIELD
    BITFIELD   G_PGA_RBB<4:0>
        POSITION=<10:6>
        DEFAULT=01011
        MODE=RW
        #! This is the gain of the PGA. The gain is adaptively set to maintain signal swing of 0.6Vpkd at the output of the PGA. The value of the gain is: Gain(dB) = -12+G_PGA_RBB. Default: 11
    ENDBITFIELD
    BITFIELD   G_LNA_RFE<3:0>
        POSITION=<5:2>
        DEFAULT=1111
        MODE=RW
        #! Controls the gain of the LNA
        #!     15 - Gmax (default)
        #!     14 - Gmax-1
        #!     13 - Gmax-2
        #!     12 - Gmax-3
        #!     11 - Gmax-4
        #!     10 - Gmax-5
        #!     9 - Gmax-6
        #!     8 - Gmax-9
        #!     7 - Gmax-12
        #!     6 - Gmax-15
        #!     5 - Gmax-18
        #!     4 - Gmax-21
        #!     3 - Gmax-24
        #!     2 - Gmax-27
        #!     1 - Gmax-30
    ENDBITFIELD
    BITFIELD   G_TIA_RFE<1:0>
        POSITION=<1:0>
        DEFAULT=11
        MODE=RW
        #! Controls the Gain of the TIA.
        #!     3 - Gmax (default)
        #!     2 - Gmax-3
        #!     1 - Gmax-12
        #!     0 - Not allowed
    ENDBITFIELD
ENDREGISTER

REGISTER    TXTSP_CFG    0x0200
    BITFIELD   TSGFC
        POSITION=9
        DEFAULT=0
        MODE=RW
        #! TSG full scale control.
        #!     0 - -6dB (default)
        #!     1 - Full scale
    ENDBITFIELD
    BITFIELD   TSGFCW<1:0>
        POSITION=<8:7>
        DEFAULT=01
        MODE=RW
        #! Set frequency of TSG's NCO.
        #!     DC  TSG NCO frequency
        #!     ========================
        #!     00  do not use
        #!     01  TSP clk/8 (default)
        #!     10  TSP clk/4
        #!     11  do not use
    ENDBITFIELD
    BITFIELD   TSGDCLDQ
        POSITION=6
        DEFAULT=0
        MODE=RW
        #! Load TSG DC Q register with value from DC_REG<15:0>.
        #!     0 - No action (default)
        #!     0-to-1 - positive edge loads TSG's DC register Q.
    ENDBITFIELD
    BITFIELD   TSGDCLDI
        POSITION=5
        DEFAULT=0
        MODE=RW
        #! Load TSG DC I register with value from DC_REG<15:0>.
        #!     0 - No action (default)
        #!     0-to-1 - positive edge loads TSG's DC register I.
    ENDBITFIELD
    BITFIELD   TSGSWAPIQ
        POSITION=4
        DEFAULT=0
        MODE=RW
        #! Swap signals at test signal generator's output.
        #!     0 - Do not swap (default)
        #!     1 - Swap I an Q signal sources comming from TSG
    ENDBITFIELD
    BITFIELD   TSGMODE
        POSITION=3
        DEFAULT=0
        MODE=RW
        #! Test signal generator mode.
        #!     0 - NCO (default)
        #!     1 - DC source
    ENDBITFIELD
    BITFIELD   INSEL
        POSITION=2
        DEFAULT=0
        MODE=RW
        #! Input source of TxTSP:
        #!     0 - LML output (default)
        #!     1 - Test signal generator
    ENDBITFIELD
    BITFIELD   BSTART
        POSITION=1
        DEFAULT=0
        MODE=RW
        #! Starts TxTSP built in self test. Keep it at 1 one at least three clock cycles.
        #! (Register is used in production test only) .
        #!     0 - (default)
        #!     0-to-1 - positive edge activates BIST
    ENDBITFIELD
    BITFIELD   EN
        POSITION=0
        DEFAULT=1
        MODE=RW
        #! TxTSP modules enable.
        #!     0 - Disabled
        #!     1 - Enabled (default)
    ENDBITFIELD
ENDREGISTER

REGISTER    TXTSP_GCORRQ    0x0201
    BITFIELD   GCORRQ<10:0>
        POSITION=<10:0>
        DEFAULT=11111111111
        MODE=RW
        #! Gain corrector value, channel Q. Unsigned integer.
        #! Possible values are 0 - 2047, default is 2047
    ENDBITFIELD
ENDREGISTER

REGISTER    TXTSP_GCORRI    0x0202
    BITFIELD   GCORRI<10:0>
        POSITION=<10:0>
        DEFAULT=11111111111
        MODE=RW
        #! Gain corrector value, channel I. Unsigned integer.
        #! Possible values are 0 - 2047, default is 2047
    ENDBITFIELD
ENDREGISTER

REGISTER    TXTSP_INTPH    0x0203
    BITFIELD   HBI_OVR<2:0>
        POSITION=<14:12>
        DEFAULT=000
        MODE=RW
        #! HBI interpolation ratio. Interpolation ratio is 2HBI_OVR+1.
        #!     000 - Interpolation ratio is 2 (default)
        #!     001 - Interpolation ratio is 4
        #!     010 - Interpolation ratio is 8
        #!     011 - Interpolation ratio is 16
        #!     100 - Interpolation ratio is 32
        #!     111 - Bypass
    ENDBITFIELD
    BITFIELD   IQCORR<11:0>
        POSITION=<11:0>
        DEFAULT=000000000000
        MODE=RW
        #! Phase corrector value (tan(Alpha/2)). Integer, 2's complement.
        #! Possible values are -2048 to 2047, default is 0.
    ENDBITFIELD
ENDREGISTER

REGISTER    TXTSP_DCCORR    0x0204
    BITFIELD   DCCORRI<7:0>
        POSITION=<15:8>
        DEFAULT=00000000
        MODE=RW
        #! DC corrector value, channel I. Integer, 2's complement.
        #! Possible values are -128 to 127, default is 0
    ENDBITFIELD
    BITFIELD   DCCORRQ<7:0>
        POSITION=<7:0>
        DEFAULT=00000000
        MODE=RW
        #! DC corrector value, channel Q. Integer, 2's complement.
        #! Possible values are -128 to 127, default is 0
    ENDBITFIELD
ENDREGISTER

REGISTER    TXTSP_GFIR1    0x0205
    BITFIELD   GFIR1_L<2:0>
        POSITION=<10:8>
        DEFAULT=000
        MODE=RW
        #! Parameter l of GFIR1 (l = roundUp(CoeffN/5)-1). Unsigned integer.
        #! Possible values are 0 to 7, default is 0
    ENDBITFIELD
    BITFIELD   GFIR1_N<7:0>
        POSITION=<7:0>
        DEFAULT=00000000
        MODE=RW
        #! Clock division ratio of GFIR1 is GFIR1_N + 1. Unsigned integer.
        #! Possible values are 0 to 255, default is 0
    ENDBITFIELD
ENDREGISTER

REGISTER    TXTSP_GFIR2    0x0206
    BITFIELD   GFIR2_L<2:0>
        POSITION=<10:8>
        DEFAULT=000
        MODE=RW
        #! Parameter l of GFIR2 (l = roundUp(CoeffN/5)-1). Unsigned integer.
        #! Possible values are 0 to 7, default is 0
    ENDBITFIELD
    BITFIELD   GFIR2_N<7:0>
        POSITION=<7:0>
        DEFAULT=00000000
        MODE=RW
        #! Clock division ratio of GFIR2 is GFIR1_N + 1. Unsigned integer.
        #! Possible values are 0 to 255, default is 0
    ENDBITFIELD
ENDREGISTER

REGISTER    TXTSP_GFIR3    0x0207
    BITFIELD   GFIR3_L<2:0>
        POSITION=<10:8>
        DEFAULT=000
        MODE=RW
        #! Parameter l of GFIR3 (l = roundUp(CoeffN/5)-1). Unsigned integer.
        #! Possible values are 0 to 7, default is 0
    ENDBITFIELD
    BITFIELD   GFIR3_N<7:0>
        POSITION=<7:0>
        DEFAULT=00000000
        MODE=RW
        #! Clock division ratio of GFIR3 is GFIR1_N + 1. Unsigned integer.
        #! Possible values are 0 to 255, default is 0
    ENDBITFIELD
ENDREGISTER

REGISTER    TXTSP_CMIXBYP    0x0208
    BITFIELD   CMIX_GAIN<1:0>
        POSITION=<15:14>
        DEFAULT=00
        MODE=RW
        #! Gain of CMIX output.
        #!     00 - CMIX output gain is 0dB (default)
        #!     01 - CMIX output gain is +6dB
        #!     10, 11 - CMIX output gain is -6dB
    ENDBITFIELD
    BITFIELD   CMIX_SC
        POSITION=13
        DEFAULT=0
        MODE=RW
        #! Spectrum control of CMIX.
        #!     1 - Downconvert
        #!     0 - Upconvert (default)
    ENDBITFIELD
    BITFIELD   CMIX_GAIN2
        POSITION=12
        DEFAULT=0
        MODE=RW
        #! Gain of CMIX output, most significant part.
        #! CMIX_GAIN[2]    CMIX_GAIN[1:0]    CMIX output gain
        #! ============================================
        #! 1               00               +3dB
        #! 1               01, 10, 11       -3dB
    ENDBITFIELD
    BITFIELD   CMIX_BYP
        POSITION=8
        DEFAULT=0
        MODE=RW
        #! CMIX bypass.
        #!     1 - Bypass
        #!     0 - Use (default)
    ENDBITFIELD
    BITFIELD   ISINC_BYP
        POSITION=7
        DEFAULT=0
        MODE=RW
        #! ISINC bypass.
        #!     1 - Bypass
        #!     0 - Use (default)
    ENDBITFIELD
    BITFIELD   GFIR3_BYP
        POSITION=6
        DEFAULT=0
        MODE=RW
        #! GFIR3 bypass.
        #!     1 - Bypass
        #!     0 - Use (default)
    ENDBITFIELD
    BITFIELD   GFIR2_BYP
        POSITION=5
        DEFAULT=0
        MODE=RW
        #! GFIR2 bypass.
        #!     1 - Bypass
        #!     0 - Use (default)
    ENDBITFIELD
    BITFIELD   GFIR1_BYP
        POSITION=4
        DEFAULT=0
        MODE=RW
        #! GFIR1 bypass.
        #!     1 - Bypass
        #!     0 - Use (default)
    ENDBITFIELD
    BITFIELD   DC_BYP
        POSITION=3
        DEFAULT=0
        MODE=RW
        #! DC corrector bypass.
        #!     1 - Bypass
        #!     0 - Use (default)
    ENDBITFIELD
    BITFIELD   GC_BYP
        POSITION=1
        DEFAULT=0
        MODE=RW
        #! Gain corrector bypass.
        #!     1 - Bypass
        #!     0 - Use (default)
    ENDBITFIELD
    BITFIELD   PH_BYP
        POSITION=0
        DEFAULT=0
        MODE=RW
        #! Phase corrector bypass.
        #!     1 - Bypass
        #!     0 - Use (default)
    ENDBITFIELD
ENDREGISTER

REGISTER    TXTSP_BSIGI    0x0209
    BITFIELD   BSIGI<14:0>
        POSITION=<15:1>
        DEFAULT=000000000000000
        MODE=R
        #! TxTSP BIST signature, channel I, LSB. (Register is used in production test only) .
    ENDBITFIELD
    BITFIELD   BSTATE
        POSITION=0
        DEFAULT=0
        MODE=R
        #! TxTSP BIST state indicator. (Register is used in production test only) .
        #!     0 - BIST is not running
        #!     1 - BIST in progress
    ENDBITFIELD
ENDREGISTER

REGISTER    TXTSP_BSIGIQ    0x020A
    BITFIELD   BSIGQ<7:0>
        POSITION=<15:8>
        DEFAULT=00000000
        MODE=R
        #! TxTSP BIST signature, channel Q, LSB. (Register is used in production test only) .
    ENDBITFIELD
    BITFIELD   BSIGI<22:15>
        POSITION=<7:0>
        DEFAULT=00000000
        MODE=R
        #! TxTSP BIST signature, channel I, MSB. (Register is used in production test only) .
    ENDBITFIELD
ENDREGISTER

REGISTER    TXTSP_BSIGQ    0x020B
    BITFIELD   BSIGQ<22:8>
        POSITION=<14:0>
        DEFAULT=000000000000000
        MODE=R
        #! TxTSP BIST signature, channel Q, MSB. (Register is used in production test only) .
    ENDBITFIELD
ENDREGISTER

REGISTER    TXTSP_DC    0x020C
    BITFIELD   DC_REG<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! DC data source for test purposes.
        #! Possible values: 2^16-1 - 0 (default)
    ENDBITFIELD
ENDREGISTER

REGISTER    TXNCO_CFG    0x0240
    BITFIELD   DTHBIT<3:0>
        POSITION=<8:5>
        DEFAULT=0001
        MODE=RW
        #! NCO bits to dither.
        #!     0000 - Dithering disabled
        #!     0001 - 1 bit dithering (default)
        #!     ...
        #!     1111 - 15 bit dithering
    ENDBITFIELD
    BITFIELD   SEL<3:0>
        POSITION=<4:1>
        DEFAULT=0001
        MODE=RW
        #! Selects PHO or FCW to feed to NCO, according to MODE. Shadow register.
        #!     0000 - PHO0 or FCW0 selected (default)
        #!     0001 - PHO1 or FCW1 selected
        #!     ...
        #!     1111 - PHO15 or FCW15 selected
    ENDBITFIELD
    BITFIELD   MODE
        POSITION=0
        DEFAULT=0
        MODE=RW
        #! Memory table mode. Shadow register.
        #!     1 - PHO table (data at addresses 0x4 to 0x13 are PHO)
        #!     0 - FCW table (data at addresses 0x2 to 0x20 are FCW) (default)
    ENDBITFIELD
ENDREGISTER

REGISTER    TXNCO_0    0x0241
    BITFIELD   DATA<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! PHO<15:0> NCO Phase offset register, when MODE = 0.
    ENDBITFIELD
ENDREGISTER

REGISTER    TXNCO_1    0x0242
    BITFIELD   DATA<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! FCW0<31:16>: NCO frequency control word register 0. MSB part.
    ENDBITFIELD
ENDREGISTER

REGISTER    TXNCO_2    0x0243
    BITFIELD   DATA<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! FCW0<15:0>: NCO frequency control word register 0. LSB part.
    ENDBITFIELD
ENDREGISTER

REGISTER    TXNCO_3    0x0244
    BITFIELD   DATA<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! FCW1<31:16>: NCO frequency control word register 1, when MODE = 0. MSB part.
        #! PHO0<15:0>: NCO Phase offset register 0, when MODE = 1.
    ENDBITFIELD
ENDREGISTER

REGISTER    TXNCO_4    0x0245
    BITFIELD   DATA<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! FCW1<15:0>: NCO frequency control word register 1, when MODE = 0. LSB part.
        #! PHO1<15:0>: NCO Phase offset register 1, when MODE = 1.
    ENDBITFIELD
ENDREGISTER

REGISTER    TXNCO_5    0x0246
    BITFIELD   DATA<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! FCW2<31:16>: NCO frequency control word register 1, when MODE = 0. MSB part.
        #! PHO2<15:0>: NCO Phase offset register 0, when MODE = 1.
    ENDBITFIELD
ENDREGISTER

REGISTER    TXNCO_6    0x0247
    BITFIELD   DATA<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! FCW2<15:0>: NCO frequency control word register 1, when MODE = 0. LSB part.
        #! PHO3<15:0>: NCO Phase offset register 1, when MODE = 1.
    ENDBITFIELD
ENDREGISTER

REGISTER    TXNCO_7    0x0248
    BITFIELD   DATA<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! FCW3<31:16>: NCO frequency control word register 1, when MODE = 0. MSB part.
        #! PHO4<15:0>: NCO Phase offset register 0, when MODE = 1.
    ENDBITFIELD
ENDREGISTER

REGISTER    TXNCO_8    0x0249
    BITFIELD   DATA<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! FCW3<15:0>: NCO frequency control word register 1, when MODE = 0. LSB part.
        #! PHO5<15:0>: NCO Phase offset register 1, when MODE = 1.
    ENDBITFIELD
ENDREGISTER

REGISTER    TXNCO_9    0x024A
    BITFIELD   DATA<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! FCW4<31:16>: NCO frequency control word register 1, when MODE = 0. MSB part.
        #! PHO6<15:0>: NCO Phase offset register 0, when MODE = 1.
    ENDBITFIELD
ENDREGISTER

REGISTER    TXNCO_A    0x024B
    BITFIELD   DATA<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! FCW4<15:0>: NCO frequency control word register 1, when MODE = 0. LSB part.
        #! PHO7<15:0>: NCO Phase offset register 1, when MODE = 1.
    ENDBITFIELD
ENDREGISTER

REGISTER    TXNCO_B    0x024C
    BITFIELD   DATA<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! FCW5<31:16>: NCO frequency control word register 1, when MODE = 0. MSB part.
        #! PHO8<15:0>: NCO Phase offset register 0, when MODE = 1.
    ENDBITFIELD
ENDREGISTER

REGISTER    TXNCO_C    0x024D
    BITFIELD   DATA<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! FCW5<15:0>: NCO frequency control word register 1, when MODE = 0. LSB part.
        #! PHO9<15:0>: NCO Phase offset register 1, when MODE = 1.
    ENDBITFIELD
ENDREGISTER

REGISTER    TXNCO_D    0x024E
    BITFIELD   DATA<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! FCW6<31:16>: NCO frequency control word register 1, when MODE = 0. MSB part.
        #! PHO10<15:0>: NCO Phase offset register 0, when MODE = 1.
    ENDBITFIELD
ENDREGISTER

REGISTER    TXNCO_E    0x024F
    BITFIELD   DATA<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! FCW6<15:0>: NCO frequency control word register 1, when MODE = 0. LSB part.
        #! PHO11<15:0>: NCO Phase offset register 1, when MODE = 1.
    ENDBITFIELD
ENDREGISTER

REGISTER    TXNCO_F    0x0250
    BITFIELD   DATA<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! FCW7<31:16>: NCO frequency control word register 1, when MODE = 0. MSB part.
        #! PHO12<15:0>: NCO Phase offset register 0, when MODE = 1.
    ENDBITFIELD
ENDREGISTER

REGISTER    TXNCO_10    0x0251
    BITFIELD   DATA<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! FCW7<15:0>: NCO frequency control word register 1, when MODE = 0. LSB part.
        #! PHO13<15:0>: NCO Phase offset register 1, when MODE = 1.
    ENDBITFIELD
ENDREGISTER

REGISTER    TXNCO_11    0x0252
    BITFIELD   DATA<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! FCW8<31:16>: NCO frequency control word register 1, when MODE = 0. MSB part.
        #! PHO14<15:0>: NCO Phase offset register 0, when MODE = 1.
    ENDBITFIELD
ENDREGISTER

REGISTER    TXNCO_12    0x0253
    BITFIELD   DATA<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! FCW8<15:0>: NCO frequency control word register 1, when MODE = 0. LSB part.
        #! PHO15<15:0>: NCO Phase offset register 1, when MODE = 1.
    ENDBITFIELD
ENDREGISTER

REGISTER    TXNCO_13    0x0254
    BITFIELD   DATA<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! FCW9<31:16>: NCO frequency control word register 1, when MODE = 0. MSB part.
    ENDBITFIELD
ENDREGISTER

REGISTER    TXNCO_14    0x0255
    BITFIELD   DATA<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! FCW9<15:0>: NCO frequency control word register 1, when MODE = 0. LSB part.
    ENDBITFIELD
ENDREGISTER

REGISTER    TXNCO_15    0x0256
    BITFIELD   DATA<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! FCW10<31:16>: NCO frequency control word register 1, when MODE = 0. MSB part.
    ENDBITFIELD
ENDREGISTER

REGISTER    TXNCO_16    0x0257
    BITFIELD   DATA<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! FCW10<15:0>: NCO frequency control word register 1, when MODE = 0. LSB part.
    ENDBITFIELD
ENDREGISTER

REGISTER    TXNCO_17    0x0258
    BITFIELD   DATA<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! FCW11<31:16>: NCO frequency control word register 1, when MODE = 0. MSB part.
    ENDBITFIELD
ENDREGISTER

REGISTER    TXNCO_18    0x0259
    BITFIELD   DATA<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! FCW11<15:0>: NCO frequency control word register 1, when MODE = 0. LSB part.
    ENDBITFIELD
ENDREGISTER

REGISTER    TXNCO_19    0x025A
    BITFIELD   DATA<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! FCW12<31:16>: NCO frequency control word register 1, when MODE = 0. MSB part.
    ENDBITFIELD
ENDREGISTER

REGISTER    TXNCO_1A    0x025B
    BITFIELD   DATA<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! FCW12<15:0>: NCO frequency control word register 1, when MODE = 0. LSB part.
    ENDBITFIELD
ENDREGISTER

REGISTER    TXNCO_1B    0x025C
    BITFIELD   DATA<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! FCW13<31:16>: NCO frequency control word register 1, when MODE = 0. MSB part.
    ENDBITFIELD
ENDREGISTER

REGISTER    TXNCO_1C    0x025D
    BITFIELD   DATA<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! FCW13<15:0>: NCO frequency control word register 1, when MODE = 0. LSB part.
    ENDBITFIELD
ENDREGISTER

REGISTER    TXNCO_1D    0x025E
    BITFIELD   DATA<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! FCW14<31:16>: NCO frequency control word register 1, when MODE = 0. MSB part.
    ENDBITFIELD
ENDREGISTER

REGISTER    TXNCO_1E    0x025F
    BITFIELD   DATA<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! FCW14<15:0>: NCO frequency control word register 1, when MODE = 0. LSB part.
    ENDBITFIELD
ENDREGISTER

REGISTER    TXNCO_1F    0x0260
    BITFIELD   DATA<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! FCW15<31:16>: NCO frequency control word register 1, when MODE = 0. MSB part.
    ENDBITFIELD
ENDREGISTER

REGISTER    TXNCO_20    0x0261
    BITFIELD   DATA<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! FCW15<15:0>: NCO frequency control word register 1, when MODE = 0. LSB part.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX1CMB0_0    0x0280
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 0 for TXGFIR1.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX1CMB0_1    0x0281
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 0 for TXGFIR1.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX1CMB0_2    0x0282
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 0 for TXGFIR1.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX1CMB0_3    0x0283
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 0 for TXGFIR1.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX1CMB0_4    0x0284
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 0 for TXGFIR1.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX1CMB0_5    0x0285
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 0 for TXGFIR1.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX1CMB0_6    0x0286
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 0 for TXGFIR1.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX1CMB0_7    0x0287
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 0 for TXGFIR1.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX1CMB1_0    0x0288
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 1 for TXGFIR1.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX1CMB1_1    0x0289
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 1 for TXGFIR1.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX1CMB1_2    0x028A
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 1 for TXGFIR1.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX1CMB1_3    0x028B
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 1 for TXGFIR1.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX1CMB1_4    0x028C
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 1 for TXGFIR1.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX1CMB1_5    0x028D
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 1 for TXGFIR1.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX1CMB1_6    0x028E
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 1 for TXGFIR1.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX1CMB1_7    0x028F
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 1 for TXGFIR1.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX1CMB2_0    0x0290
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 2 for TXGFIR1.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX1CMB2_1    0x0291
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 2 for TXGFIR1.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX1CMB2_2    0x0292
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 2 for TXGFIR1.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX1CMB2_3    0x0293
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 2 for TXGFIR1.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX1CMB2_4    0x0294
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 2 for TXGFIR1.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX1CMB2_5    0x0295
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 2 for TXGFIR1.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX1CMB2_6    0x0296
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 2 for TXGFIR1.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX1CMB2_7    0x0297
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 2 for TXGFIR1.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX1CMB3_0    0x0298
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 3 for TXGFIR1.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX1CMB3_1    0x0299
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 3 for TXGFIR1.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX1CMB3_2    0x029A
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 3 for TXGFIR1.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX1CMB3_3    0x029B
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 3 for TXGFIR1.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX1CMB3_4    0x029C
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 3 for TXGFIR1.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX1CMB3_5    0x029D
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 3 for TXGFIR1.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX1CMB3_6    0x029E
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 3 for TXGFIR1.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX1CMB3_7    0x029F
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 3 for TXGFIR1.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX1CMB4_0    0x02A0
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 4 for TXGFIR1.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX1CMB4_1    0x02A1
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 4 for TXGFIR1.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX1CMB4_2    0x02A2
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 4 for TXGFIR1.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX1CMB4_3    0x02A3
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 4 for TXGFIR1.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX1CMB4_4    0x02A4
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 4 for TXGFIR1.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX1CMB4_5    0x02A5
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 4 for TXGFIR1.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX1CMB4_6    0x02A6
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 4 for TXGFIR1.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX1CMB4_7    0x02A7
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 4 for TXGFIR1.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX2CMB0_0    0x02C0
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 0 for TXGFIR2.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX2CMB0_1    0x02C1
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 0 for TXGFIR2.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX2CMB0_2    0x02C2
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 0 for TXGFIR2.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX2CMB0_3    0x02C3
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 0 for TXGFIR2.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX2CMB0_4    0x02C4
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 0 for TXGFIR2.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX2CMB0_5    0x02C5
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 0 for TXGFIR2.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX2CMB0_6    0x02C6
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 0 for TXGFIR2.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX2CMB0_7    0x02C7
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 0 for TXGFIR2.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX2CMB1_0    0x02C8
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 1 for TXGFIR2.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX2CMB1_1    0x02C9
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 1 for TXGFIR2.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX2CMB1_2    0x02CA
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 1 for TXGFIR2.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX2CMB1_3    0x02CB
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 1 for TXGFIR2.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX2CMB1_4    0x02CC
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 1 for TXGFIR2.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX2CMB1_5    0x02CD
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 1 for TXGFIR2.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX2CMB1_6    0x02CE
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 1 for TXGFIR2.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX2CMB1_7    0x02CF
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 1 for TXGFIR2.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX2CMB2_0    0x02D0
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 2 for TXGFIR2.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX2CMB2_1    0x02D1
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 2 for TXGFIR2.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX2CMB2_2    0x02D2
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 2 for TXGFIR2.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX2CMB2_3    0x02D3
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 2 for TXGFIR2.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX2CMB2_4    0x02D4
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 2 for TXGFIR2.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX2CMB2_5    0x02D5
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 2 for TXGFIR2.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX2CMB2_6    0x02D6
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 2 for TXGFIR2.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX2CMB2_7    0x02D7
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 2 for TXGFIR2.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX2CMB3_0    0x02D8
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 3 for TXGFIR2.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX2CMB3_1    0x02D9
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 3 for TXGFIR2.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX2CMB3_2    0x02DA
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 3 for TXGFIR2.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX2CMB3_3    0x02DB
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 3 for TXGFIR2.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX2CMB3_4    0x02DC
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 3 for TXGFIR2.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX2CMB3_5    0x02DD
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 3 for TXGFIR2.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX2CMB3_6    0x02DE
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 3 for TXGFIR2.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX2CMB3_7    0x02DF
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 3 for TXGFIR2.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX2CMB4_0    0x02E0
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 4 for TXGFIR2.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX2CMB4_1    0x02E1
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 4 for TXGFIR2.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX2CMB4_2    0x02E2
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 4 for TXGFIR2.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX2CMB4_3    0x02E3
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 4 for TXGFIR2.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX2CMB4_4    0x02E4
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 4 for TXGFIR2.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX2CMB4_5    0x02E5
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 4 for TXGFIR2.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX2CMB4_6    0x02E6
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 4 for TXGFIR2.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX2CMB4_7    0x02E7
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 4 for TXGFIR2.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX3CMB0a_0    0x0300
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 0 for TXGFIR3a.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX3CMB0a_1    0x0301
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 0 for TXGFIR3a.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX3CMB0a_2    0x0302
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 0 for TXGFIR3a.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX3CMB0a_3    0x0303
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 0 for TXGFIR3a.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX3CMB0a_4    0x0304
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 0 for TXGFIR3a.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX3CMB0a_5    0x0305
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 0 for TXGFIR3a.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX3CMB0a_6    0x0306
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 0 for TXGFIR3a.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX3CMB0a_7    0x0307
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 0 for TXGFIR3a.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX3CMB1a_0    0x0308
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 1 for TXGFIR3a.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX3CMB1a_1    0x0309
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 1 for TXGFIR3a.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX3CMB1a_2    0x030A
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 1 for TXGFIR3a.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX3CMB1a_3    0x030B
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 1 for TXGFIR3a.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX3CMB1a_4    0x030C
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 1 for TXGFIR3a.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX3CMB1a_5    0x030D
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 1 for TXGFIR3a.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX3CMB1a_6    0x030E
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 1 for TXGFIR3a.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX3CMB1a_7    0x030F
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 1 for TXGFIR3a.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX3CMB2a_0    0x0310
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 2 for TXGFIR3a.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX3CMB2a_1    0x0311
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 2 for TXGFIR3a.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX3CMB2a_2    0x0312
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 2 for TXGFIR3a.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX3CMB2a_3    0x0313
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 2 for TXGFIR3a.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX3CMB2a_4    0x0314
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 2 for TXGFIR3a.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX3CMB2a_5    0x0315
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 2 for TXGFIR3a.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX3CMB2a_6    0x0316
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 2 for TXGFIR3a.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX3CMB2a_7    0x0317
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 2 for TXGFIR3a.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX3CMB3a_0    0x0318
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 3 for TXGFIR3a.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX3CMB3a_1    0x0319
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 3 for TXGFIR3a.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX3CMB3a_2    0x031A
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 3 for TXGFIR3a.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX3CMB3a_3    0x031B
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 3 for TXGFIR3a.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX3CMB3a_4    0x031C
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 3 for TXGFIR3a.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX3CMB3a_5    0x031D
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 3 for TXGFIR3a.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX3CMB3a_6    0x031E
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 3 for TXGFIR3a.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX3CMB3a_7    0x031F
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 3 for TXGFIR3a.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX3CMB4a_0    0x0320
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 4 for TXGFIR3a.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX3CMB4a_1    0x0321
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 4 for TXGFIR3a.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX3CMB4a_2    0x0322
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 4 for TXGFIR3a.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX3CMB4a_3    0x0323
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 4 for TXGFIR3a.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX3CMB4a_4    0x0324
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 4 for TXGFIR3a.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX3CMB4a_5    0x0325
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 4 for TXGFIR3a.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX3CMB4a_6    0x0326
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 4 for TXGFIR3a.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX3CMB4a_7    0x0327
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 4 for TXGFIR3a.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX3CMB0b_0    0x0340
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 0 for TXGFIR3b.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX3CMB0b_1    0x0341
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 0 for TXGFIR3b.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX3CMB0b_2    0x0342
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 0 for TXGFIR3b.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX3CMB0b_3    0x0343
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 0 for TXGFIR3b.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX3CMB0b_4    0x0344
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 0 for TXGFIR3b.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX3CMB0b_5    0x0345
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 0 for TXGFIR3b.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX3CMB0b_6    0x0346
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 0 for TXGFIR3b.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX3CMB0b_7    0x0347
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 0 for TXGFIR3b.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX3CMB1b_0    0x0348
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 1 for TXGFIR3b.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX3CMB1b_1    0x0349
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 1 for TXGFIR3b.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX3CMB1b_2    0x034A
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 1 for TXGFIR3b.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX3CMB1b_3    0x034B
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 1 for TXGFIR3b.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX3CMB1b_4    0x034C
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 1 for TXGFIR3b.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX3CMB1b_5    0x034D
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 1 for TXGFIR3b.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX3CMB1b_6    0x034E
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 1 for TXGFIR3b.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX3CMB1b_7    0x034F
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 1 for TXGFIR3b.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX3CMB2b_0    0x0350
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 2 for TXGFIR3b.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX3CMB2b_1    0x0351
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 2 for TXGFIR3b.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX3CMB2b_2    0x0352
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 2 for TXGFIR3b.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX3CMB2b_3    0x0353
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 2 for TXGFIR3b.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX3CMB2b_4    0x0354
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 2 for TXGFIR3b.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX3CMB2b_5    0x0355
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 2 for TXGFIR3b.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX3CMB2b_6    0x0356
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 2 for TXGFIR3b.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX3CMB2b_7    0x0357
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 2 for TXGFIR3b.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX3CMB3b_0    0x0358
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 3 for TXGFIR3b.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX3CMB3b_1    0x0359
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 3 for TXGFIR3b.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX3CMB3b_2    0x035A
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 3 for TXGFIR3b.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX3CMB3b_3    0x035B
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 3 for TXGFIR3b.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX3CMB3b_4    0x035C
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 3 for TXGFIR3b.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX3CMB3b_5    0x035D
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 3 for TXGFIR3b.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX3CMB3b_6    0x035E
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 3 for TXGFIR3b.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX3CMB3b_7    0x035F
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 3 for TXGFIR3b.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX3CMB4b_0    0x0360
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 4 for TXGFIR3b.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX3CMB4b_1    0x0361
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 4 for TXGFIR3b.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX3CMB4b_2    0x0362
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 4 for TXGFIR3b.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX3CMB4b_3    0x0363
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 4 for TXGFIR3b.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX3CMB4b_4    0x0364
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 4 for TXGFIR3b.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX3CMB4b_5    0x0365
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 4 for TXGFIR3b.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX3CMB4b_6    0x0366
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 4 for TXGFIR3b.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX3CMB4b_7    0x0367
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 4 for TXGFIR3b.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX3CMB0c_0    0x0380
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 0 for TXGFIR3c.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX3CMB0c_1    0x0381
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 0 for TXGFIR3c.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX3CMB0c_2    0x0382
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 0 for TXGFIR3c.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX3CMB0c_3    0x0383
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 0 for TXGFIR3c.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX3CMB0c_4    0x0384
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 0 for TXGFIR3c.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX3CMB0c_5    0x0385
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 0 for TXGFIR3c.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX3CMB0c_6    0x0386
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 0 for TXGFIR3c.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX3CMB0c_7    0x0387
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 0 for TXGFIR3c.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX3CMB1c_0    0x0388
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 1 for TXGFIR3c.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX3CMB1c_1    0x0389
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 1 for TXGFIR3c.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX3CMB1c_2    0x038A
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 1 for TXGFIR3c.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX3CMB1c_3    0x038B
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 1 for TXGFIR3c.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX3CMB1c_4    0x038C
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 1 for TXGFIR3c.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX3CMB1c_5    0x038D
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 1 for TXGFIR3c.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX3CMB1c_6    0x038E
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 1 for TXGFIR3c.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX3CMB1c_7    0x038F
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 1 for TXGFIR3c.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX3CMB2c_0    0x0390
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 2 for TXGFIR3c.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX3CMB2c_1    0x0391
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 2 for TXGFIR3c.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX3CMB2c_2    0x0392
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 2 for TXGFIR3c.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX3CMB2c_3    0x0393
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 2 for TXGFIR3c.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX3CMB2c_4    0x0394
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 2 for TXGFIR3c.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX3CMB2c_5    0x0395
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 2 for TXGFIR3c.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX3CMB2c_6    0x0396
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 2 for TXGFIR3c.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX3CMB2c_7    0x0397
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 2 for TXGFIR3c.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX3CMB3c_0    0x0398
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 3 for TXGFIR3c.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX3CMB3c_1    0x0399
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 3 for TXGFIR3c.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX3CMB3c_2    0x039A
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 3 for TXGFIR3c.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX3CMB3c_3    0x039B
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 3 for TXGFIR3c.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX3CMB3c_4    0x039C
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 3 for TXGFIR3c.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX3CMB3c_5    0x039D
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 3 for TXGFIR3c.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX3CMB3c_6    0x039E
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 3 for TXGFIR3c.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX3CMB3c_7    0x039F
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 3 for TXGFIR3c.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX3CMB4c_0    0x03A0
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 4 for TXGFIR3c.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX3CMB4c_1    0x03A1
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 4 for TXGFIR3c.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX3CMB4c_2    0x03A2
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 4 for TXGFIR3c.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX3CMB4c_3    0x03A3
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 4 for TXGFIR3c.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX3CMB4c_4    0x03A4
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 4 for TXGFIR3c.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX3CMB4c_5    0x03A5
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 4 for TXGFIR3c.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX3CMB4c_6    0x03A6
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 4 for TXGFIR3c.
    ENDBITFIELD
ENDREGISTER

REGISTER    TX3CMB4c_7    0x03A7
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 4 for TXGFIR3c.
    ENDBITFIELD
ENDREGISTER

REGISTER    RXTSP_CFG    0x0400
    BITFIELD   CAPTURE
        POSITION=15
        DEFAULT=0
        MODE=RW
        #! Captures value, selected by CAPSEL<1:0>.
        #!     0 - (default)
        #!     0-to-1 - positive edge captures value, selected by CAPSEL<1:0>
    ENDBITFIELD
    BITFIELD   CAPSEL<1:0>
        POSITION=<14:13>
        DEFAULT=00
        MODE=RW
        #! Selects what parameters to capture to memory (addresses 0x0400E and 0x0400F)
        #!     00 - RSSI (default)
        #!     01 - ADCI and ADCQ
        #!     10 - BSIGI and BSTATE
        #!     11 - BSIGQ and BSTATE
    ENDBITFIELD
    BITFIELD   CAPSEL_ADC
        POSITION=12
        DEFAULT=0
        MODE=RW
        #! Selects ADC value source to be captured, when CAPSEL[1:0] = 01.
        #!     0 - RxTSP input (default)
        #!     1 - RxTSP output
    ENDBITFIELD
    BITFIELD   TSGFC
        POSITION=9
        DEFAULT=0
        MODE=RW
        #! TSG full scale control.
        #!     0 - -6dB (default)
        #!     1 - Full scale
    ENDBITFIELD
    BITFIELD   TSGFCW<1:0>
        POSITION=<8:7>
        DEFAULT=01
        MODE=RW
        #! Set frequency of TSG's NCO.
        #!     DC  TSG NCO frequency
        #!     ========================
        #!     00  do not use
        #!     01  TSP clk/8 (default)
        #!     10  TSP clk/4
        #!     11  do not use
    ENDBITFIELD
    BITFIELD   TSGDCLDQ
        POSITION=6
        DEFAULT=0
        MODE=RW
        #! Load TSG DC Q register with value from DC_REG<15:0>.
        #!     0 - No action (default)
        #!     0-to-1 - positive edge loads TSG's DC register Q.
    ENDBITFIELD
    BITFIELD   TSGDCLDI
        POSITION=5
        DEFAULT=0
        MODE=RW
        #! Load TSG DC I register with value from DC_REG<15:0>.
        #!     0 - No action (default)
        #!     0-to-1 - positive edge loads TSG's DC register I.
    ENDBITFIELD
    BITFIELD   TSGSWAPIQ
        POSITION=4
        DEFAULT=0
        MODE=RW
        #! Swap signals at test signal generator's output.
        #!     0 - Do not swap (default)
        #!     1 - Swap I an Q signal sources comming from TSG
    ENDBITFIELD
    BITFIELD   TSGMODE
        POSITION=3
        DEFAULT=0
        MODE=RW
        #! Test signal generator mode.
        #!     0 - NCO (default)
        #!     1 - DC source
    ENDBITFIELD
    BITFIELD   INSEL
        POSITION=2
        DEFAULT=0
        MODE=RW
        #! Input source of RXTSP:
        #!     0 - LML output (default)
        #!     1 - Test signal generator
    ENDBITFIELD
    BITFIELD   BSTART
        POSITION=1
        DEFAULT=0
        MODE=RW
        #! Starts RXTSP built in self test. Keep it at 1 one at least three clock cycles.
        #! (Register is used in production test only) .
        #!     0 - (default)
        #!     0-to-1 - positive edge activates BIST
    ENDBITFIELD
    BITFIELD   EN
        POSITION=0
        DEFAULT=1
        MODE=RW
        #! RXTSP modules enable.
        #!     0 - Disabled
        #!     1 - Enabled (default)
    ENDBITFIELD
ENDREGISTER

REGISTER    RXTSP_GCORRQ    0x0401
    BITFIELD   GCORRQ<10:0>
        POSITION=<10:0>
        DEFAULT=11111111111
        MODE=RW
        #! Gain corrector value, channel Q. Unsigned integer.
        #! Possible values are 0 - 2047, default is 2047
    ENDBITFIELD
ENDREGISTER

REGISTER    RXTSP_GCORRI    0x0402
    BITFIELD   GCORRI<10:0>
        POSITION=<10:0>
        DEFAULT=11111111111
        MODE=RW
        #! Gain corrector value, channel I. Unsigned integer.
        #! Possible values are 0 - 2047, default is 2047
    ENDBITFIELD
ENDREGISTER

REGISTER    RXTSP_INTPH    0x0403
    BITFIELD   HBD_OVR<2:0>
        POSITION=<14:12>
        DEFAULT=000
        MODE=RW
        #! HBD decimation ratio. Decimation ratio is 2^(HBD_OVR+1).
        #!     000 - Decimation ratio is 2 (default)
        #!     001 - Decimation ratio is 4
        #!     010 - Decimation ratio is 8
        #!     011 - Decimation ratio is 16
        #!     100 - Decimation ratio is 32
        #!     111 - Bypass
    ENDBITFIELD
    BITFIELD   IQCORR<11:0>
        POSITION=<11:0>
        DEFAULT=000000000000
        MODE=RW
        #! Phase corrector value (tan(Alpha/2)). Integer, 2's complement.
        #! Possible values are -2048 to 2047, default is 0.
    ENDBITFIELD
ENDREGISTER

REGISTER    RXTSP_DCCORRAVG    0x0404
    BITFIELD   HBD_DLY<2:0>
        POSITION=<15:13>
        DEFAULT=000
        MODE=RW
        #! HBD delay line control.
        #!     000 - No delay (default)
        #!     001 - Delay is 1 clock cycle
        #!     010 - Delay is 2 clock cycles
        #!     011 - Delay is 3 clock cycles
        #!     100 to 111- Delay is 4 clock cycles
    ENDBITFIELD
    BITFIELD   DCCORR_AVG<2:0>
        POSITION=<2:0>
        DEFAULT=000
        MODE=RW
        #! Number of samples to average for Automatic DC corrector.
        #! Number of samples to average is 2^(DCCORR_AVG + 12).
    ENDBITFIELD
ENDREGISTER

REGISTER    RXTSP_GFIR1    0x0405
    BITFIELD   GFIR1_L<2:0>
        POSITION=<10:8>
        DEFAULT=000
        MODE=RW
        #! Parameter l of GFIR1 (l = roundUp(CoeffN/5)-1). Unsigned integer.
        #! Possible values are 0 to 7, default is 0
    ENDBITFIELD
    BITFIELD   GFIR1_N<7:0>
        POSITION=<7:0>
        DEFAULT=00000000
        MODE=RW
        #! Clock division ratio of GFIR1 is GFIR1_N + 1. Unsigned integer.
        #! Possible values are 0 to 255, default is 0
    ENDBITFIELD
ENDREGISTER

REGISTER    RXTSP_GFIR2    0x0406
    BITFIELD   GFIR2_L<2:0>
        POSITION=<10:8>
        DEFAULT=000
        MODE=RW
        #! Parameter l of GFIR2 (l = roundUp(CoeffN/5)-1). Unsigned integer.
        #! Possible values are 0 to 7, default is 0
    ENDBITFIELD
    BITFIELD   GFIR2_N<7:0>
        POSITION=<7:0>
        DEFAULT=00000000
        MODE=RW
        #! Clock division ratio of GFIR2 is GFIR1_N + 1. Unsigned integer.
        #! Possible values are 0 to 255, default is 0
    ENDBITFIELD
ENDREGISTER

REGISTER    RXTSP_GFIR3    0x0407
    BITFIELD   GFIR3_L<2:0>
        POSITION=<10:8>
        DEFAULT=000
        MODE=RW
        #! Parameter l of GFIR3 (l = roundUp(CoeffN/5)-1). Unsigned integer.
        #! Possible values are 0 to 7, default is 0
    ENDBITFIELD
    BITFIELD   GFIR3_N<7:0>
        POSITION=<7:0>
        DEFAULT=00000000
        MODE=RW
        #! Clock division ratio of GFIR3 is GFIR1_N + 1. Unsigned integer.
        #! Possible values are 0 to 255, default is 0
    ENDBITFIELD
ENDREGISTER

REGISTER    RXTSP_AGC0    0x0408
    BITFIELD   AGC_K<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! AGC loop gain, LSB.
    ENDBITFIELD
ENDREGISTER

REGISTER    RXTSP_AGC1    0x0409
    BITFIELD   AGC_ADESIRED<11:0>
        POSITION=<15:4>
        DEFAULT=000000000000
        MODE=RW
        #! Desired output signal level.
    ENDBITFIELD
    BITFIELD   AGC_K<17:16>
        POSITION=<1:0>
        DEFAULT=00
        MODE=RW
        #! AGC loop gain, MSB.
    ENDBITFIELD
ENDREGISTER

REGISTER    RXTSP_AGC2    0x040A
    BITFIELD   RSSI_MODE<1:0>
        POSITION=<15:14>
        DEFAULT=00
        MODE=RW
        #! RSSI Mode.
        #!     00 - Normal RSSI
        #!     01 - I amplitude
        #!     10 - Q amplitude
        #!     11 - Do not use
    ENDBITFIELD
    BITFIELD   AGC_MODE<1:0>
        POSITION=<13:12>
        DEFAULT=00
        MODE=RW
        #! AGC Mode.
        #!     0 - AGC mode
        #!     1 - RSSI mode
        #!     2, 3 - Bypass
    ENDBITFIELD
    BITFIELD   AGC_AVG<2:0>
        POSITION=<2:0>
        DEFAULT=000
        MODE=RW
        #! AGC averaging window size is 2^(AGC_AVG + 7)
    ENDBITFIELD
ENDREGISTER

REGISTER    RXTSP_DC    0x040B
    BITFIELD   DC_REG<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! DC data source for test purposes.
        #! Possible values: 2^16-1 - 0 (default)
    ENDBITFIELD
ENDREGISTER

REGISTER    RXTSP_CMIXBYP    0x040C
    BITFIELD   CMIX_GAIN<1:0>
        POSITION=<15:14>
        DEFAULT=00
        MODE=RW
        #! Gain of CMIX output.
        #!     00 - CMIX output gain is 0dB (default)
        #!     01 - CMIX output gain is +6dB
        #!     10, 11 - CMIX output gain is -6dB
    ENDBITFIELD
    BITFIELD   CMIX_SC
        POSITION=13
        DEFAULT=0
        MODE=RW
        #! Spectrum control of CMIX.
        #!     1 - Downconvert
        #!     0 - Upconvert (default)
    ENDBITFIELD
    BITFIELD   CMIX_GAIN2
        POSITION=12
        DEFAULT=0
        MODE=RW
        #! Gain of CMIX output, most significant part.
        #! CMIX_GAIN[2]    CMIX_GAIN[1:0]    CMIX output gain
        #! ============================================
        #! 1               00               +3dB
        #! 1               01, 10, 11       -3dB
    ENDBITFIELD
    BITFIELD   CMIX_BYP
        POSITION=7
        DEFAULT=0
        MODE=RW
        #! CMIX bypass.
        #!     1 - Bypass
        #!     0 - Use (default)
    ENDBITFIELD
    BITFIELD   AGC_BYP
        POSITION=6
        DEFAULT=0
        MODE=RW
        #! AGC bypass.
        #!     1 - Bypass
        #!     0 - Use (default)
    ENDBITFIELD
    BITFIELD   GFIR3_BYP
        POSITION=5
        DEFAULT=0
        MODE=RW
        #! GFIR3 bypass.
        #!     1 - Bypass
        #!     0 - Use (default)
    ENDBITFIELD
    BITFIELD   GFIR2_BYP
        POSITION=4
        DEFAULT=0
        MODE=RW
        #! GFIR2 bypass.
        #!     1 - Bypass
        #!     0 - Use (default)
    ENDBITFIELD
    BITFIELD   GFIR1_BYP
        POSITION=3
        DEFAULT=0
        MODE=RW
        #! GFIR1 bypass.
        #!     1 - Bypass
        #!     0 - Use (default)
    ENDBITFIELD
    BITFIELD   DC_BYP
        POSITION=2
        DEFAULT=0
        MODE=RW
        #! DC corrector bypass.
        #!     1 - Bypass
        #!     0 - Use (default)
    ENDBITFIELD
    BITFIELD   GC_BYP
        POSITION=1
        DEFAULT=0
        MODE=RW
        #! Gain corrector bypass.
        #!     1 - Bypass
        #!     0 - Use (default)
    ENDBITFIELD
    BITFIELD   PH_BYP
        POSITION=0
        DEFAULT=0
        MODE=RW
        #! Phase corrector bypass.
        #!     1 - Bypass
        #!     0 - Use (default)
    ENDBITFIELD
ENDREGISTER

REGISTER    RXTSP_CAPDL    0x040E
    BITFIELD   CAPDL<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=R
        #! Data capture register. Stores data, selected by CAPSEL<1:0>, on rising
        #! edge of CAPTURE. Register layout is as follows:
        #! 0x040E, 0x040F
        #! =======================================================
        #! 0   00      0s, RSSI[1:0]      RSSI[17:2]
        #! 0   01      0s, ADCI_i[9:0]    0s, ADCQ_i[9:0]
        #! 1   XX      ADCI_o[15:0]       ADCQ_o[15:0]
        #! 0   10      BISTI[14:0],BSTATE 0s, BISTI[22:15]
        #! 0   11      BISTQ[14:0],BSTATE 0s, BISTQ[22:15]
    ENDBITFIELD
ENDREGISTER

REGISTER    RXTSP_CAPDH    0x040F
    BITFIELD   CAPDH<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=R
        #! Data capture register. Stores data, selected by CAPSEL<1:0>, on rising
        #! edge of CAPTURE. Register layout is as follows:
        #! 0x040E, 0x040F
        #! =======================================================
        #! 0   00      0s, RSSI[1:0]      RSSI[17:2]
        #! 0   01      0s, ADCI_i[9:0]    0s, ADCQ_i[9:0]
        #! 1   XX      ADCI_o[15:0]       ADCQ_o[15:0]
        #! 0   10      BISTI[14:0],BSTATE 0s, BISTI[22:15]
        #! 0   11      BISTQ[14:0],BSTATE 0s, BISTQ[22:15]
    ENDBITFIELD
ENDREGISTER

REGISTER    RXNCO_CFG    0x0440
    BITFIELD   DTHBIT<3:0>
        POSITION=<8:5>
        DEFAULT=0001
        MODE=RW
        #! NCO bits to dither.
        #!     0000 - Dithering disabled
        #!     0001 - 1 bit dithering (default)
        #!     ...
        #!     1111 - 15 bit dithering
    ENDBITFIELD
    BITFIELD   SEL<3:0>
        POSITION=<4:1>
        DEFAULT=0001
        MODE=RW
        #! Selects PHO or FCW to feed to NCO, according to MODE. Shadow register.
        #!     0000 - PHO0 or FCW0 selected (default)
        #!     0001 - PHO1 or FCW1 selected
        #!     ...
        #!     1111 - PHO15 or FCW15 selected
    ENDBITFIELD
    BITFIELD   MODE
        POSITION=0
        DEFAULT=0
        MODE=RW
        #! Memory table mode. Shadow register.
        #!     1 - PHO table (data at addresses 0x4 to 0x13 are PHO)
        #!     0 - FCW table (data at addresses 0x2 to 0x20 are FCW) (default)
    ENDBITFIELD
ENDREGISTER

REGISTER    RXNCO_0    0x0441
    BITFIELD   DATA<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! PHO<15:0> NCO Phase offset register, when MODE = 0.
    ENDBITFIELD
ENDREGISTER

REGISTER    RXNCO_1    0x0442
    BITFIELD   DATA<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! FCW0<31:16>: NCO frequency control word register 0. MSB part.
    ENDBITFIELD
ENDREGISTER

REGISTER    RXNCO_2    0x0443
    BITFIELD   DATA<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! FCW0<15:0>: NCO frequency control word register 0. LSB part.
    ENDBITFIELD
ENDREGISTER

REGISTER    RXNCO_3    0x0444
    BITFIELD   DATA<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! FCW1<31:16>: NCO frequency control word register 1, when MODE = 0. MSB part.
        #! PHO0<15:0>: NCO Phase offset register 0, when MODE = 1.
    ENDBITFIELD
ENDREGISTER

REGISTER    RXNCO_4    0x0445
    BITFIELD   DATA<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! FCW1<15:0>: NCO frequency control word register 1, when MODE = 0. LSB part.
        #! PHO1<15:0>: NCO Phase offset register 1, when MODE = 1.
    ENDBITFIELD
ENDREGISTER

REGISTER    RXNCO_5    0x0446
    BITFIELD   DATA<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! FCW2<31:16>: NCO frequency control word register 1, when MODE = 0. MSB part.
        #! PHO2<15:0>: NCO Phase offset register 0, when MODE = 1.
    ENDBITFIELD
ENDREGISTER

REGISTER    RXNCO_6    0x0447
    BITFIELD   DATA<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! FCW2<15:0>: NCO frequency control word register 1, when MODE = 0. LSB part.
        #! PHO3<15:0>: NCO Phase offset register 1, when MODE = 1.
    ENDBITFIELD
ENDREGISTER

REGISTER    RXNCO_7    0x0448
    BITFIELD   DATA<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! FCW3<31:16>: NCO frequency control word register 1, when MODE = 0. MSB part.
        #! PHO4<15:0>: NCO Phase offset register 0, when MODE = 1.
    ENDBITFIELD
ENDREGISTER

REGISTER    RXNCO_8    0x0449
    BITFIELD   DATA<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! FCW3<15:0>: NCO frequency control word register 1, when MODE = 0. LSB part.
        #! PHO5<15:0>: NCO Phase offset register 1, when MODE = 1.
    ENDBITFIELD
ENDREGISTER

REGISTER    RXNCO_9    0x044A
    BITFIELD   DATA<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! FCW4<31:16>: NCO frequency control word register 1, when MODE = 0. MSB part.
        #! PHO6<15:0>: NCO Phase offset register 0, when MODE = 1.
    ENDBITFIELD
ENDREGISTER

REGISTER    RXNCO_A    0x044B
    BITFIELD   DATA<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! FCW4<15:0>: NCO frequency control word register 1, when MODE = 0. LSB part.
        #! PHO7<15:0>: NCO Phase offset register 1, when MODE = 1.
    ENDBITFIELD
ENDREGISTER

REGISTER    RXNCO_B    0x044C
    BITFIELD   DATA<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! FCW5<31:16>: NCO frequency control word register 1, when MODE = 0. MSB part.
        #! PHO8<15:0>: NCO Phase offset register 0, when MODE = 1.
    ENDBITFIELD
ENDREGISTER

REGISTER    RXNCO_C    0x044D
    BITFIELD   DATA<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! FCW5<15:0>: NCO frequency control word register 1, when MODE = 0. LSB part.
        #! PHO9<15:0>: NCO Phase offset register 1, when MODE = 1.
    ENDBITFIELD
ENDREGISTER

REGISTER    RXNCO_D    0x044E
    BITFIELD   DATA<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! FCW6<31:16>: NCO frequency control word register 1, when MODE = 0. MSB part.
        #! PHO10<15:0>: NCO Phase offset register 0, when MODE = 1.
    ENDBITFIELD
ENDREGISTER

REGISTER    RXNCO_E    0x044F
    BITFIELD   DATA<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! FCW6<15:0>: NCO frequency control word register 1, when MODE = 0. LSB part.
        #! PHO11<15:0>: NCO Phase offset register 1, when MODE = 1.
    ENDBITFIELD
ENDREGISTER

REGISTER    RXNCO_F    0x0450
    BITFIELD   DATA<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! FCW7<31:16>: NCO frequency control word register 1, when MODE = 0. MSB part.
        #! PHO12<15:0>: NCO Phase offset register 0, when MODE = 1.
    ENDBITFIELD
ENDREGISTER

REGISTER    RXNCO_10    0x0451
    BITFIELD   DATA<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! FCW7<15:0>: NCO frequency control word register 1, when MODE = 0. LSB part.
        #! PHO13<15:0>: NCO Phase offset register 1, when MODE = 1.
    ENDBITFIELD
ENDREGISTER

REGISTER    RXNCO_11    0x0452
    BITFIELD   DATA<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! FCW8<31:16>: NCO frequency control word register 1, when MODE = 0. MSB part.
        #! PHO14<15:0>: NCO Phase offset register 0, when MODE = 1.
    ENDBITFIELD
ENDREGISTER

REGISTER    RXNCO_12    0x0453
    BITFIELD   DATA<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! FCW8<15:0>: NCO frequency control word register 1, when MODE = 0. LSB part.
        #! PHO15<15:0>: NCO Phase offset register 1, when MODE = 1.
    ENDBITFIELD
ENDREGISTER

REGISTER    RXNCO_13    0x0454
    BITFIELD   DATA<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! FCW9<31:16>: NCO frequency control word register 1, when MODE = 0. MSB part.
    ENDBITFIELD
ENDREGISTER

REGISTER    RXNCO_14    0x0455
    BITFIELD   DATA<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! FCW9<15:0>: NCO frequency control word register 1, when MODE = 0. LSB part.
    ENDBITFIELD
ENDREGISTER

REGISTER    RXNCO_15    0x0456
    BITFIELD   DATA<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! FCW10<31:16>: NCO frequency control word register 1, when MODE = 0. MSB part.
    ENDBITFIELD
ENDREGISTER

REGISTER    RXNCO_16    0x0457
    BITFIELD   DATA<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! FCW10<15:0>: NCO frequency control word register 1, when MODE = 0. LSB part.
    ENDBITFIELD
ENDREGISTER

REGISTER    RXNCO_17    0x0458
    BITFIELD   DATA<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! FCW11<31:16>: NCO frequency control word register 1, when MODE = 0. MSB part.
    ENDBITFIELD
ENDREGISTER

REGISTER    RXNCO_18    0x0459
    BITFIELD   DATA<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! FCW11<15:0>: NCO frequency control word register 1, when MODE = 0. LSB part.
    ENDBITFIELD
ENDREGISTER

REGISTER    RXNCO_19    0x045A
    BITFIELD   DATA<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! FCW12<31:16>: NCO frequency control word register 1, when MODE = 0. MSB part.
    ENDBITFIELD
ENDREGISTER

REGISTER    RXNCO_1A    0x045B
    BITFIELD   DATA<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! FCW12<15:0>: NCO frequency control word register 1, when MODE = 0. LSB part.
    ENDBITFIELD
ENDREGISTER

REGISTER    RXNCO_1B    0x045C
    BITFIELD   DATA<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! FCW13<31:16>: NCO frequency control word register 1, when MODE = 0. MSB part.
    ENDBITFIELD
ENDREGISTER

REGISTER    RXNCO_1C    0x045D
    BITFIELD   DATA<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! FCW13<15:0>: NCO frequency control word register 1, when MODE = 0. LSB part.
    ENDBITFIELD
ENDREGISTER

REGISTER    RXNCO_1D    0x045E
    BITFIELD   DATA<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! FCW14<31:16>: NCO frequency control word register 1, when MODE = 0. MSB part.
    ENDBITFIELD
ENDREGISTER

REGISTER    RXNCO_1E    0x045F
    BITFIELD   DATA<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! FCW14<15:0>: NCO frequency control word register 1, when MODE = 0. LSB part.
    ENDBITFIELD
ENDREGISTER

REGISTER    RXNCO_1F    0x0460
    BITFIELD   DATA<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! FCW15<31:16>: NCO frequency control word register 1, when MODE = 0. MSB part.
    ENDBITFIELD
ENDREGISTER

REGISTER    RXNCO_20    0x0461
    BITFIELD   DATA<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! FCW15<15:0>: NCO frequency control word register 1, when MODE = 0. LSB part.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX1CMB0_0    0x0480
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 0 for RXGFIR1.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX1CMB0_1    0x0481
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 0 for RXGFIR1.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX1CMB0_2    0x0482
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 0 for RXGFIR1.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX1CMB0_3    0x0483
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 0 for RXGFIR1.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX1CMB0_4    0x0484
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 0 for RXGFIR1.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX1CMB0_5    0x0485
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 0 for RXGFIR1.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX1CMB0_6    0x0486
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 0 for RXGFIR1.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX1CMB0_7    0x0487
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 0 for RXGFIR1.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX1CMB1_0    0x0488
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 1 for RXGFIR1.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX1CMB1_1    0x0489
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 1 for RXGFIR1.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX1CMB1_2    0x048A
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 1 for RXGFIR1.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX1CMB1_3    0x048B
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 1 for RXGFIR1.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX1CMB1_4    0x048C
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 1 for RXGFIR1.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX1CMB1_5    0x048D
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 1 for RXGFIR1.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX1CMB1_6    0x048E
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 1 for RXGFIR1.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX1CMB1_7    0x048F
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 1 for RXGFIR1.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX1CMB2_0    0x0490
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 2 for RXGFIR1.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX1CMB2_1    0x0491
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 2 for RXGFIR1.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX1CMB2_2    0x0492
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 2 for RXGFIR1.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX1CMB2_3    0x0493
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 2 for RXGFIR1.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX1CMB2_4    0x0494
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 2 for RXGFIR1.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX1CMB2_5    0x0495
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 2 for RXGFIR1.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX1CMB2_6    0x0496
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 2 for RXGFIR1.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX1CMB2_7    0x0497
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 2 for RXGFIR1.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX1CMB3_0    0x0498
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 3 for RXGFIR1.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX1CMB3_1    0x0499
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 3 for RXGFIR1.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX1CMB3_2    0x049A
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 3 for RXGFIR1.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX1CMB3_3    0x049B
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 3 for RXGFIR1.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX1CMB3_4    0x049C
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 3 for RXGFIR1.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX1CMB3_5    0x049D
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 3 for RXGFIR1.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX1CMB3_6    0x049E
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 3 for RXGFIR1.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX1CMB3_7    0x049F
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 3 for RXGFIR1.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX1CMB4_0    0x04A0
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 4 for RXGFIR1.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX1CMB4_1    0x04A1
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 4 for RXGFIR1.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX1CMB4_2    0x04A2
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 4 for RXGFIR1.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX1CMB4_3    0x04A3
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 4 for RXGFIR1.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX1CMB4_4    0x04A4
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 4 for RXGFIR1.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX1CMB4_5    0x04A5
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 4 for RXGFIR1.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX1CMB4_6    0x04A6
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 4 for RXGFIR1.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX1CMB4_7    0x04A7
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 4 for RXGFIR1.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX2CMB0_0    0x04C0
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 0 for RXGFIR2.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX2CMB0_1    0x04C1
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 0 for RXGFIR2.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX2CMB0_2    0x04C2
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 0 for RXGFIR2.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX2CMB0_3    0x04C3
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 0 for RXGFIR2.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX2CMB0_4    0x04C4
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 0 for RXGFIR2.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX2CMB0_5    0x04C5
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 0 for RXGFIR2.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX2CMB0_6    0x04C6
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 0 for RXGFIR2.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX2CMB0_7    0x04C7
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 0 for RXGFIR2.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX2CMB1_0    0x04C8
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 1 for RXGFIR2.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX2CMB1_1    0x04C9
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 1 for RXGFIR2.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX2CMB1_2    0x04CA
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 1 for RXGFIR2.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX2CMB1_3    0x04CB
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 1 for RXGFIR2.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX2CMB1_4    0x04CC
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 1 for RXGFIR2.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX2CMB1_5    0x04CD
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 1 for RXGFIR2.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX2CMB1_6    0x04CE
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 1 for RXGFIR2.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX2CMB1_7    0x04CF
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 1 for RXGFIR2.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX2CMB2_0    0x04D0
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 2 for RXGFIR2.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX2CMB2_1    0x04D1
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 2 for RXGFIR2.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX2CMB2_2    0x04D2
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 2 for RXGFIR2.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX2CMB2_3    0x04D3
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 2 for RXGFIR2.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX2CMB2_4    0x04D4
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 2 for RXGFIR2.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX2CMB2_5    0x04D5
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 2 for RXGFIR2.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX2CMB2_6    0x04D6
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 2 for RXGFIR2.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX2CMB2_7    0x04D7
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 2 for RXGFIR2.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX2CMB3_0    0x04D8
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 3 for RXGFIR2.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX2CMB3_1    0x04D9
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 3 for RXGFIR2.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX2CMB3_2    0x04DA
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 3 for RXGFIR2.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX2CMB3_3    0x04DB
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 3 for RXGFIR2.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX2CMB3_4    0x04DC
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 3 for RXGFIR2.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX2CMB3_5    0x04DD
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 3 for RXGFIR2.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX2CMB3_6    0x04DE
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 3 for RXGFIR2.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX2CMB3_7    0x04DF
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 3 for RXGFIR2.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX2CMB4_0    0x04E0
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 4 for RXGFIR2.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX2CMB4_1    0x04E1
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 4 for RXGFIR2.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX2CMB4_2    0x04E2
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 4 for RXGFIR2.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX2CMB4_3    0x04E3
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 4 for RXGFIR2.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX2CMB4_4    0x04E4
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 4 for RXGFIR2.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX2CMB4_5    0x04E5
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 4 for RXGFIR2.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX2CMB4_6    0x04E6
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 4 for RXGFIR2.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX2CMB4_7    0x04E7
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 4 for RXGFIR2.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX3CMB0a_0    0x0500
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 0 for RXGFIR3a.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX3CMB0a_1    0x0501
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 0 for RXGFIR3a.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX3CMB0a_2    0x0502
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 0 for RXGFIR3a.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX3CMB0a_3    0x0503
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 0 for RXGFIR3a.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX3CMB0a_4    0x0504
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 0 for RXGFIR3a.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX3CMB0a_5    0x0505
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 0 for RXGFIR3a.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX3CMB0a_6    0x0506
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 0 for RXGFIR3a.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX3CMB0a_7    0x0507
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 0 for RXGFIR3a.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX3CMB1a_0    0x0508
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 1 for RXGFIR3a.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX3CMB1a_1    0x0509
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 1 for RXGFIR3a.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX3CMB1a_2    0x050A
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 1 for RXGFIR3a.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX3CMB1a_3    0x050B
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 1 for RXGFIR3a.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX3CMB1a_4    0x050C
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 1 for RXGFIR3a.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX3CMB1a_5    0x050D
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 1 for RXGFIR3a.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX3CMB1a_6    0x050E
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 1 for RXGFIR3a.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX3CMB1a_7    0x050F
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 1 for RXGFIR3a.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX3CMB2a_0    0x0510
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 2 for RXGFIR3a.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX3CMB2a_1    0x0511
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 2 for RXGFIR3a.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX3CMB2a_2    0x0512
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 2 for RXGFIR3a.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX3CMB2a_3    0x0513
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 2 for RXGFIR3a.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX3CMB2a_4    0x0514
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 2 for RXGFIR3a.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX3CMB2a_5    0x0515
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 2 for RXGFIR3a.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX3CMB2a_6    0x0516
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 2 for RXGFIR3a.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX3CMB2a_7    0x0517
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 2 for RXGFIR3a.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX3CMB3a_0    0x0518
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 3 for RXGFIR3a.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX3CMB3a_1    0x0519
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 3 for RXGFIR3a.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX3CMB3a_2    0x051A
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 3 for RXGFIR3a.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX3CMB3a_3    0x051B
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 3 for RXGFIR3a.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX3CMB3a_4    0x051C
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 3 for RXGFIR3a.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX3CMB3a_5    0x051D
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 3 for RXGFIR3a.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX3CMB3a_6    0x051E
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 3 for RXGFIR3a.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX3CMB3a_7    0x051F
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 3 for RXGFIR3a.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX3CMB4a_0    0x0520
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 4 for RXGFIR3a.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX3CMB4a_1    0x0521
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 4 for RXGFIR3a.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX3CMB4a_2    0x0522
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 4 for RXGFIR3a.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX3CMB4a_3    0x0523
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 4 for RXGFIR3a.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX3CMB4a_4    0x0524
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 4 for RXGFIR3a.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX3CMB4a_5    0x0525
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 4 for RXGFIR3a.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX3CMB4a_6    0x0526
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 4 for RXGFIR3a.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX3CMB4a_7    0x0527
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 4 for RXGFIR3a.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX3CMB0b_0    0x0540
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 0 for RXGFIR3b.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX3CMB0b_1    0x0541
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 0 for RXGFIR3b.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX3CMB0b_2    0x0542
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 0 for RXGFIR3b.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX3CMB0b_3    0x0543
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 0 for RXGFIR3b.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX3CMB0b_4    0x0544
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 0 for RXGFIR3b.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX3CMB0b_5    0x0545
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 0 for RXGFIR3b.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX3CMB0b_6    0x0546
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 0 for RXGFIR3b.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX3CMB0b_7    0x0547
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 0 for RXGFIR3b.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX3CMB1b_0    0x0548
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 1 for RXGFIR3b.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX3CMB1b_1    0x0549
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 1 for RXGFIR3b.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX3CMB1b_2    0x054A
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 1 for RXGFIR3b.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX3CMB1b_3    0x054B
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 1 for RXGFIR3b.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX3CMB1b_4    0x054C
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 1 for RXGFIR3b.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX3CMB1b_5    0x054D
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 1 for RXGFIR3b.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX3CMB1b_6    0x054E
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 1 for RXGFIR3b.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX3CMB1b_7    0x054F
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 1 for RXGFIR3b.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX3CMB2b_0    0x0550
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 2 for RXGFIR3b.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX3CMB2b_1    0x0551
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 2 for RXGFIR3b.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX3CMB2b_2    0x0552
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 2 for RXGFIR3b.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX3CMB2b_3    0x0553
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 2 for RXGFIR3b.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX3CMB2b_4    0x0554
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 2 for RXGFIR3b.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX3CMB2b_5    0x0555
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 2 for RXGFIR3b.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX3CMB2b_6    0x0556
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 2 for RXGFIR3b.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX3CMB2b_7    0x0557
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 2 for RXGFIR3b.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX3CMB3b_0    0x0558
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 3 for RXGFIR3b.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX3CMB3b_1    0x0559
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 3 for RXGFIR3b.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX3CMB3b_2    0x055A
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 3 for RXGFIR3b.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX3CMB3b_3    0x055B
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 3 for RXGFIR3b.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX3CMB3b_4    0x055C
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 3 for RXGFIR3b.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX3CMB3b_5    0x055D
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 3 for RXGFIR3b.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX3CMB3b_6    0x055E
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 3 for RXGFIR3b.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX3CMB3b_7    0x055F
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 3 for RXGFIR3b.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX3CMB4b_0    0x0560
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 4 for RXGFIR3b.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX3CMB4b_1    0x0561
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 4 for RXGFIR3b.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX3CMB4b_2    0x0562
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 4 for RXGFIR3b.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX3CMB4b_3    0x0563
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 4 for RXGFIR3b.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX3CMB4b_4    0x0564
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 4 for RXGFIR3b.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX3CMB4b_5    0x0565
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 4 for RXGFIR3b.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX3CMB4b_6    0x0566
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 4 for RXGFIR3b.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX3CMB4b_7    0x0567
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 4 for RXGFIR3b.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX3CMB0c_0    0x0580
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 0 for RXGFIR3c.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX3CMB0c_1    0x0581
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 0 for RXGFIR3c.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX3CMB0c_2    0x0582
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 0 for RXGFIR3c.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX3CMB0c_3    0x0583
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 0 for RXGFIR3c.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX3CMB0c_4    0x0584
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 0 for RXGFIR3c.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX3CMB0c_5    0x0585
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 0 for RXGFIR3c.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX3CMB0c_6    0x0586
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 0 for RXGFIR3c.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX3CMB0c_7    0x0587
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 0 for RXGFIR3c.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX3CMB1c_0    0x0588
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 1 for RXGFIR3c.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX3CMB1c_1    0x0589
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 1 for RXGFIR3c.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX3CMB1c_2    0x058A
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 1 for RXGFIR3c.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX3CMB1c_3    0x058B
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 1 for RXGFIR3c.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX3CMB1c_4    0x058C
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 1 for RXGFIR3c.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX3CMB1c_5    0x058D
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 1 for RXGFIR3c.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX3CMB1c_6    0x058E
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 1 for RXGFIR3c.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX3CMB1c_7    0x058F
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 1 for RXGFIR3c.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX3CMB2c_0    0x0590
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 2 for RXGFIR3c.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX3CMB2c_1    0x0591
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 2 for RXGFIR3c.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX3CMB2c_2    0x0592
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 2 for RXGFIR3c.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX3CMB2c_3    0x0593
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 2 for RXGFIR3c.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX3CMB2c_4    0x0594
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 2 for RXGFIR3c.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX3CMB2c_5    0x0595
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 2 for RXGFIR3c.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX3CMB2c_6    0x0596
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 2 for RXGFIR3c.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX3CMB2c_7    0x0597
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 2 for RXGFIR3c.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX3CMB3c_0    0x0598
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 3 for RXGFIR3c.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX3CMB3c_1    0x0599
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 3 for RXGFIR3c.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX3CMB3c_2    0x059A
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 3 for RXGFIR3c.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX3CMB3c_3    0x059B
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 3 for RXGFIR3c.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX3CMB3c_4    0x059C
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 3 for RXGFIR3c.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX3CMB3c_5    0x059D
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 3 for RXGFIR3c.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX3CMB3c_6    0x059E
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 3 for RXGFIR3c.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX3CMB3c_7    0x059F
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 3 for RXGFIR3c.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX3CMB4c_0    0x05A0
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 4 for RXGFIR3c.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX3CMB4c_1    0x05A1
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 4 for RXGFIR3c.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX3CMB4c_2    0x05A2
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 4 for RXGFIR3c.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX3CMB4c_3    0x05A3
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 4 for RXGFIR3c.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX3CMB4c_4    0x05A4
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 4 for RXGFIR3c.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX3CMB4c_5    0x05A5
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 4 for RXGFIR3c.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX3CMB4c_6    0x05A6
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 4 for RXGFIR3c.
    ENDBITFIELD
ENDREGISTER

REGISTER    RX3CMB4c_7    0x05A7
    BITFIELD   COEFF<15:0>
        POSITION=<15:0>
        DEFAULT=0000000000000000
        MODE=RW
        #! Coefficients memory bank 4 for RXGFIR3c.
    ENDBITFIELD
ENDREGISTER

REGISTER    DCCAL_CFG    0x05C0
    BITFIELD   DCMODE
        POSITION=15
        DEFAULT=0
        MODE=RW
        #! DC calibration mode.
        #!     0 - Manual (default)
        #!     1 - Automatic
    ENDBITFIELD
    BITFIELD   PD_DCDAC_RXB
        POSITION=7
        DEFAULT=1
        MODE=RW
        #! 0 - block active
        #!     1 - block powered down (default)
    ENDBITFIELD
    BITFIELD   PD_DCDAC_RXA
        POSITION=6
        DEFAULT=1
        MODE=RW
        #! 0 - block active
        #!     1 - block powered down (default)
    ENDBITFIELD
    BITFIELD   PD_DCDAC_TXB
        POSITION=5
        DEFAULT=1
        MODE=RW
        #! 0 - block active
        #!     1 - block powered down (default)
    ENDBITFIELD
    BITFIELD   PD_DCDAC_TXA
        POSITION=4
        DEFAULT=1
        MODE=RW
        #! 0 - block active
        #!     1 - block powered down (default)
    ENDBITFIELD
    BITFIELD   PD_DCCMP_RXB
        POSITION=3
        DEFAULT=1
        MODE=RW
        #! 0 - block active
        #!     1 - block powered down (default)
    ENDBITFIELD
    BITFIELD   PD_DCCMP_RXA
        POSITION=2
        DEFAULT=1
        MODE=RW
        #! 0 - block active
        #!     1 - block powered down (default)
    ENDBITFIELD
    BITFIELD   PD_DCCMP_TXB
        POSITION=1
        DEFAULT=1
        MODE=RW
        #! 0 - block active
        #!     1 - block powered down (default)
    ENDBITFIELD
    BITFIELD   PD_DCCMP_TXA
        POSITION=0
        DEFAULT=1
        MODE=RW
        #! 0 - block active
        #!     1 - block powered down (default)
    ENDBITFIELD
ENDREGISTER

REGISTER    DCCAL_STAT    0x05C1
    BITFIELD   DCCAL_CALSTATUS<7:0>
        POSITION=<15:8>
        DEFAULT=00000000
        MODE=R
        #! Status of automatic calibration loops (Read only)
        #!     DCCAL_CALSTATUS[7] = 0 - RXBQ DC calibration is not running
        #!     DCCAL_CALSTATUS[7] = 1 - RXBQ DC calibration is running
        #!     DCCAL_CALSTATUS[6] = 0 - RXBI DC calibration is not running
        #!     DCCAL_CALSTATUS[6] = 1 - RXBI DC calibration is running
        #!     DCCAL_CALSTATUS[5] = 0 - RXAQ DC calibration is not running
        #!     DCCAL_CALSTATUS[5] = 1 - RXAQ DC calibration is running
        #!     DCCAL_CALSTATUS[4] = 0 - RXAI DC calibration is not running
        #!     DCCAL_CALSTATUS[4] = 1 - RXAI DC calibration is running
        #!     DCCAL_CALSTATUS[3] = 0 - TXBQ DC calibration is not running
        #!     DCCAL_CALSTATUS[3] = 1 - TXBQ DC calibration is running
        #!     DCCAL_CALSTATUS[2] = 0 - TXBI DC calibration is not running
        #!     DCCAL_CALSTATUS[2] = 1 - TXBI DC calibration is running
        #!     DCCAL_CALSTATUS[1] = 0 - TXAQ DC calibration is not running
        #!     DCCAL_CALSTATUS[1] = 1 - TXAQ DC calibration is running
        #!     DCCAL_CALSTATUS[0] = 0 - TXAI DC calibration is not running
        #!     DCCAL_CALSTATUS[0] = 1 - TXAI DC calibration is running
    ENDBITFIELD
    BITFIELD   DCCAL_CMPSTATUS<7:0>
        POSITION=<7:0>
        DEFAULT=00000000
        MODE=R
        #! Status of comparators (Read only)
        #!     DCCAL_CMPSTATUS[7] - RXBQ comparator value
        #!     DCCAL_CMPSTATUS[6] - RXBI comparator value
        #!     DCCAL_CMPSTATUS[5] - RXAQ comparator value
        #!     DCCAL_CMPSTATUS[4] - RXAI comparator value
        #!     DCCAL_CMPSTATUS[3] - TXBQ comparator value
        #!     DCCAL_CMPSTATUS[2] - TXBI comparator value
        #!     DCCAL_CMPSTATUS[1] - TXAQ comparator value
        #!     DCCAL_CMPSTATUS[0] - TXAI comparator value
    ENDBITFIELD
ENDREGISTER

REGISTER    DCCAL_CFG2    0x05C2
    BITFIELD   DCCAL_CMPCFG<7:0>
        POSITION=<15:8>
        DEFAULT=00000000
        MODE=RW
        #! Comparator configuration
        #!     DCCAL_CMPCFG[7] = 0 - RXBQ comparator output not inverted
        #!     (default)
        #!     DCCAL_CMPCFG[7] = 1 - RXBQ comparator output inverted
        #!     DCCAL_CMPCFG[6] = 0 - RXBI comparator output not inverted
        #!     (default)
        #!     DCCAL_CMPCFG[6] = 1 - RXBI comparator output inverted
        #!     DCCAL_CMPCFG[5] = 0 - RXAQ comparator output not inverted
        #!     (default)
        #!     DCCAL_CMPCFG[5] = 1 - RXQQ comparator output inverted
        #!     DCCAL_CMPCFG[4] = 0 - RXAI comparator output not inverted (default)
        #!     DCCAL_CMPCFG[4] = 1 - RXAI comparator output inverted
        #!     DCCAL_CMPCFG[3] = 0 - TXBQ comparator output not inverted (default)
        #!     DCCAL_CMPCFG[3] = 1 - TXBQ comparator output inverted
        #!     DCCAL_CMPCFG[2] = 0 - TXBI comparator output not inverted (default)
        #!     DCCAL_CMPCFG[2] = 1 - TXBI comparator output inverted
        #!     DCCAL_CMPCFG[1] = 0 - TXAQ comparator output not inverted (default)
        #!     DCCAL_CMPCFG[1] = 1 - TXQQ comparator output inverted
        #!     DCCAL_CMPCFG[0] = 0 - TXAI comparator output not inverted (default)
        #!     DCCAL_CMPCFG[0] = 1 - TXAI comparator output inverted
    ENDBITFIELD
    BITFIELD   DCCAL_START<7:0>
        POSITION=<7:0>
        DEFAULT=00000000
        MODE=RW
        #! Start automatic DC calibration
        #!     DCCAL_START[7] = 0 to 1 - Start RXBQ automatic calibration
        #!     DCCAL_START[6] = 0 to 1 - Start RXBI automatic calibration
        #!     DCCAL_START[5] = 0 to 1 - Start RXAQ automatic calibration
        #!     DCCAL_START[4] = 0 to 1 - Start RXAI automatic calibration
        #!     DCCAL_START[3] = 0 to 1 - Start TXBQ automatic calibration
        #!     DCCAL_START[2] = 0 to 1 - Start TXBI automatic calibration
        #!     DCCAL_START[1] = 0 to 1 - Start TXAQ automatic calibration
        #!     DCCAL_START[0] = 0 to 1 - Start TXAI automatic calibration
    ENDBITFIELD
ENDREGISTER

REGISTER    DCCAL_TXAI    0x05C3
    BITFIELD   DCWR_TXAI
        POSITION=15
        DEFAULT=0
        MODE=RW
        #! 0 to 1 - writes the value to TXAI DAC from DC_TXAI register Default: 0
    ENDBITFIELD
    BITFIELD   DCRD_TXAI
        POSITION=14
        DEFAULT=0
        MODE=RW
        #! 0 to 1 - read the value from TXAI DAC to DC_TXAI register Default: 0
    ENDBITFIELD
    BITFIELD   DC_TXAI<10:0>
        POSITION=<10:0>
        DEFAULT=00000000000
        MODE=RW
        #! Stores the value to be written to the TXAI DAC as well as read value from TXAI_DAC. Default: 0
        #!     DC_TXAI[10] - sign
        #!     DC_TXAI[9:0] - magnitude
    ENDBITFIELD
ENDREGISTER

REGISTER    DCCAL_TXAQ    0x05C4
    BITFIELD   DCWR_TXAQ
        POSITION=15
        DEFAULT=0
        MODE=RW
        #! 0 to 1 - writes the value to TXAQ DAC from DC_TXAQ register Default: 0
    ENDBITFIELD
    BITFIELD   DCRD_TXAQ
        POSITION=14
        DEFAULT=0
        MODE=RW
        #! 0 to 1 - read the value from TXAQ DAC to DC_TXAQ register Default: 0
    ENDBITFIELD
    BITFIELD   DC_TXAQ<10:0>
        POSITION=<10:0>
        DEFAULT=00000000000
        MODE=RW
        #! Stores the value to be written to the TXAQ DAC as well as read value from TXAQ_DAC. Default: 0
        #!     DC_TXAQ[10] - sign
        #!     DC_TXAQ[9:0] - magnitude
    ENDBITFIELD
ENDREGISTER

REGISTER    DCCAL_TXBI    0x05C5
    BITFIELD   DCWR_TXBI
        POSITION=15
        DEFAULT=0
        MODE=RW
        #! 0 to 1 - writes the value to TXBI DAC from DC_TXBI register Default: 0
    ENDBITFIELD
    BITFIELD   DCRD_TXBI
        POSITION=14
        DEFAULT=0
        MODE=RW
        #! 0 to 1 - read the value from TXBI DAC to DC_TXBI register Default: 0
    ENDBITFIELD
    BITFIELD   DC_TXBI<10:0>
        POSITION=<10:0>
        DEFAULT=00000000000
        MODE=RW
        #! Stores the value to be written to the TXBI DAC as well as read value from TXBI_DAC. Default: 0
        #!     DC_TXBI[10] - sign
        #!     DC_TXBI[9:0] - magnitude
    ENDBITFIELD
ENDREGISTER

REGISTER    DCCAL_TXBQ    0x05C6
    BITFIELD   DCWR_TXBQ
        POSITION=15
        DEFAULT=0
        MODE=RW
        #! 0 to 1 - writes the value to TXBQ DAC from DC_TXBQ register Default: 0
    ENDBITFIELD
    BITFIELD   DCRD_TXBQ
        POSITION=14
        DEFAULT=0
        MODE=RW
        #! 0 to 1 - read the value from TXBQ DAC to DC_TXBQ register Default: 0
    ENDBITFIELD
    BITFIELD   DC_TXBQ<10:0>
        POSITION=<10:0>
        DEFAULT=00000000000
        MODE=RW
        #! Stores the value to be written to the TXBQ DAC as well as read value from TXBQ_DAC. Default: 0
        #!     DC_TXBQ[10] - sign
        #!     DC_TXBQ[9:0] - magnitude
    ENDBITFIELD
ENDREGISTER

REGISTER    DCCAL_RXAI    0x05C7
    BITFIELD   DCWR_RXAI
        POSITION=15
        DEFAULT=0
        MODE=RW
        #! 0 to 1 - writes the value to RXAI DAC from DC_RXAI register Default: 0
    ENDBITFIELD
    BITFIELD   DCRD_RXAI
        POSITION=14
        DEFAULT=0
        MODE=RW
        #! 0 to 1 - read the value from RXAI DAC to DC_RXAI register Default: 0
    ENDBITFIELD
    BITFIELD   DC_RXAI<6:0>
        POSITION=<6:0>
        DEFAULT=0000000
        MODE=RW
        #! Stores the value to be written to the RXAI DAC as well as read value from RXAI_DAC. Default: 0
        #!     DC_RXAI[6] - sign
        #!     DC_RXAI[5:0] - magnitude
    ENDBITFIELD
ENDREGISTER

REGISTER    DCCAL_RXAQ    0x05C8
    BITFIELD   DCWR_RXAQ
        POSITION=15
        DEFAULT=0
        MODE=RW
        #! 0 to 1 - writes the value to RXAQ DAC from DC_RXAQ register Default: 0
    ENDBITFIELD
    BITFIELD   DCRD_RXAQ
        POSITION=14
        DEFAULT=0
        MODE=RW
        #! 0 to 1 - writes the value from RXAQ DAC to DC_RXAQ register Default: 0
    ENDBITFIELD
    BITFIELD   DC_RXAQ<6:0>
        POSITION=<6:0>
        DEFAULT=0000000
        MODE=RW
        #! Stores the value to be written to the RXAQ DAC as well as read value from RXAQ_DAC. Default: 0
        #!     DC_RXAQ[6] - sign
        #!     DC_RXAQ[5:0] - magnitude
    ENDBITFIELD
ENDREGISTER

REGISTER    DCCAL_RXBI    0x05C9
    BITFIELD   DCWR_RXBI
        POSITION=15
        DEFAULT=0
        MODE=RW
        #! 0 to 1 - writes the value to RXBI DAC from DC_RXBI register Default: 0
    ENDBITFIELD
    BITFIELD   DCRD_RXBI
        POSITION=14
        DEFAULT=0
        MODE=RW
        #! 0 to 1 - writes the value from RXBI DAC to DC_RXBI register Default: 0
    ENDBITFIELD
    BITFIELD   DC_RXBI<6:0>
        POSITION=<6:0>
        DEFAULT=0000000
        MODE=RW
        #! Stores the value to be written to the RXBI DAC as well as read value from RXBI_DAC. Default: 0
        #!     DC_RXBI[6] - sign
        #!     DC_RXBI[5:0] - magnitude
    ENDBITFIELD
ENDREGISTER

REGISTER    DCCAL_RXBQ    0x05CA
    BITFIELD   DCWR_RXBQ
        POSITION=15
        DEFAULT=0
        MODE=RW
        #! 0 to 1 - writes the value to RXBQ DAC from DC_RXBQ register Default: 0
    ENDBITFIELD
    BITFIELD   DCRD_RXBQ
        POSITION=14
        DEFAULT=0
        MODE=RW
        #! 0 to 1 - read the value from RXBQ DAC to DC_RXBQ register Default: 0
    ENDBITFIELD
    BITFIELD   DC_RXBQ<6:0>
        POSITION=<6:0>
        DEFAULT=0000000
        MODE=RW
        #! Stores the value to be written to the RXBQ DAC as well as read value from RXBQ_DAC. Default: 0
        #!     DC_RXBQ[6] - sign
        #!     DC_RXBQ[5:0] - magnitude
    ENDBITFIELD
ENDREGISTER

REGISTER    DCCAL_CLKDIV    0x05CB
    BITFIELD   DC_RXCDIV<7:0>
        POSITION=<15:8>
        DEFAULT=00000000
        MODE=R
        #! Clock division ratio for Rx DC calibration loop
        #! 0 to 255 - Division ratio is n+1 Default: 31
    ENDBITFIELD
    BITFIELD   DC_TXCDIV<7:0>
        POSITION=<7:0>
        DEFAULT=00000000
        MODE=R
        #! Clock division ratio for Tx DC calibration loop
        #! 0 to 255 - Division ratio is n+1 Default: 15
    ENDBITFIELD
ENDREGISTER

REGISTER    DCCAL_HYSTCFG    0x05CC
    BITFIELD   HYSCMP_RXB<2:0>
        POSITION=<11:9>
        DEFAULT=000
        MODE=RW
        #! Comparator hysteresis control, RXB channel
        #!     000 - min hysteresis (default)
        #!     ...
        #!     111 - max hysteresis
    ENDBITFIELD
    BITFIELD   HYSCMP_RXA<2:0>
        POSITION=<8:6>
        DEFAULT=000
        MODE=RW
        #! Comparator hysteresis control, RXA channel
        #!     000 - min hysteresis (default)
        #!     ...
        #!     111 - max hysteresis
    ENDBITFIELD
    BITFIELD   HYSCMP_TXB<2:0>
        POSITION=<5:3>
        DEFAULT=000
        MODE=RW
        #! Comparator hysteresis control, TXB channel
        #!     000 - min hysteresis (default)
        #!     ...
        #!     111 - max hysteresis
    ENDBITFIELD
    BITFIELD   HYSCMP_TXA<2:0>
        POSITION=<2:0>
        DEFAULT=000
        MODE=RW
        #! Comparator hysteresis control, TXA channel
        #!     000 - min hysteresis (default)
        #!     ...
        #!     111 - max hysteresis
    ENDBITFIELD
ENDREGISTER

REGISTER    RPT_CFG0    0x0600
    BITFIELD   DAC_CLKDIV<7:0>
        POSITION=<15:8>
        DEFAULT=00001111
        MODE=RW
        #! Clock division ratio for measurement loop
        #! 0 to 255 - Division ratio is n+1 Default: 15
    ENDBITFIELD
    BITFIELD   MODE
        POSITION=1
        DEFAULT=1
        MODE=RW
        #! Operation mode.
        #!     0 - automatic (default)
        #!     1 - manual
    ENDBITFIELD
    BITFIELD   PD
        POSITION=0
        DEFAULT=1
        MODE=RW
        #! Power down modules.
        #!     0 - blocks active, measurement enabled
        #!     1 - blocks powered down, measurement disabled (default)
    ENDBITFIELD
ENDREGISTER

REGISTER    RPT_CFG1    0x0601
    BITFIELD   CMPSTATUS<5:0>
        POSITION=<5:0>
        DEFAULT=000000
        MODE=R
        #! Status of comparators (Read only)
        #!     CMPSTATUS[5] - Temperature Reference comparator value
        #!     CMPSTATUS[4] - Temperature VPTAT comparator value
        #!     CMPSTATUS[3] - RSSI 2 comparator value
        #!     CMPSTATUS[2] - RSSI 1 comparator value
        #!     CMPSTATUS[1] - Power Detector 2 comparator value
        #!     CMPSTATUS[0] - Power Detector 1 comparator value
    ENDBITFIELD
ENDREGISTER

REGISTER    RPT_CFG2    0x0602
    BITFIELD   BIAS<4:0>
        POSITION=<13:9>
        DEFAULT=10000
        MODE=RW
        #! Controls the reference bias current of the test ADC.
        #! 10000 - (default)
    ENDBITFIELD
    BITFIELD   HYSCMP<2:0>
        POSITION=<8:6>
        DEFAULT=000
        MODE=RW
        #! Comparator hysteresis control.
        #!     000 - min hysteresis (default)
        #!     ...
        #!     111 - max hysteresis
    ENDBITFIELD
    BITFIELD   CMPCFG<5:0>
        POSITION=<5:0>
        DEFAULT=000000
        MODE=RW
        #! Comparator configuration
        #!     CMPCFG[5] = 0 - Temp Ref comparator output not inverted (default)
        #!     CMPCFG[5] = 1 - Temp Ref comparator output inverted
        #!     CMPCFG[4] = 0 - Temp VPTAT comparator output not inverted (default)
        #!     CMPCFG[4] = 1 - Temp VPTAT comparator output inverted
        #!     CMPCFG[3] = 0 - RSSI 2 comparator output not inverted (default)
        #!     CMPCFG[3] = 1 - RSSI 2 comparator output inverted
        #!     CMPCFG[2] = 0 - RSSI 1 comparator output not inverted (default)
        #!     CMPCFG[2] = 1 - RSSI 1 comparator output inverted
        #!     CMPCFG[1] = 0 - Power Det 2comparator output not inverted (default)
        #!     CMPCFG[1] = 1 - Power Det 2 comparator output inverted
        #!     CMPCFG[0] = 0 - Power Det 1 comparator output not inverted (default)
        #!     CMPCFG[0] = 1 - Power Det 1 comparator output inverted
    ENDBITFIELD
ENDREGISTER

REGISTER    RPT_CFG3    0x0603
    BITFIELD   DAC_VAL<7:0>
        POSITION=<7:0>
        DEFAULT=00000000
        MODE=RW
        #! Stores the value to be written to the DAC, when MODE = 1 Default: 0
        #! DAC_VAL[7:0] - magnitude
    ENDBITFIELD
ENDREGISTER

REGISTER    RPT_CFG4    0x0604
    BITFIELD   PDET2_VAL<7:0>
        POSITION=<15:8>
        DEFAULT=00000000
        MODE=R
        #! Power detector 2 value
    ENDBITFIELD
    BITFIELD   PDET1_VAL<7:0>
        POSITION=<7:0>
        DEFAULT=00000000
        MODE=R
        #! Power detector 1 value
    ENDBITFIELD
ENDREGISTER

REGISTER    RPT_CFG5    0x0605
    BITFIELD   RSSI2_VAL<7:0>
        POSITION=<15:8>
        DEFAULT=00000000
        MODE=R
        #! RSSI2 value
    ENDBITFIELD
    BITFIELD   RSSI1_VAL<7:0>
        POSITION=<7:0>
        DEFAULT=00000000
        MODE=R
        #! RSSI1 value
    ENDBITFIELD
ENDREGISTER

REGISTER    RPT_CFG6    0x0606
    BITFIELD   TREF_VAL<7:0>
        POSITION=<15:8>
        DEFAULT=00000000
        MODE=R
        #! Temperature reference value
    ENDBITFIELD
    BITFIELD   TVPTAT_VAL<7:0>
        POSITION=<7:0>
        DEFAULT=00000000
        MODE=R
        #! Voltage proportional to absolute temperature
    ENDBITFIELD
ENDREGISTER

REGISTER    RSSI_DCCAL0    0x0640
    BITFIELD   CMPSTATUS
        POSITION=15
        DEFAULT=0
        MODE=R
        #! Status of comparator
        #!     0/1 - Comparator value
    ENDBITFIELD
    BITFIELD   RSEL<4:0>
        POSITION=<8:4>
        DEFAULT=01010
        MODE=RW
        #! Reference voltage for RSSI output comparator. Default 10.
        #! Voltage range:
        #!     0 - 800mV; 31 - 250mV.
        #!    Step size:
        #!    0 to 4 - 50mV;
        #!    5 to 12 - 21.5mV;
        #!    13 to 31 - 10mV.
    ENDBITFIELD
    BITFIELD   HYSCMP<2:0>
        POSITION=<3:1>
        DEFAULT=000
        MODE=RW
        #! Comparator hysteresis control.
        #!     000 - min hysteresis (default)
        #!      ...
        #!     111 - max hysteresis
    ENDBITFIELD
    BITFIELD   PD
        POSITION=0
        DEFAULT=1
        MODE=RW
        #! Power down modules.
        #!     0 - blocks active, measurement enabled
        #!     1 - blocks powered down, measurement disabled (default)
    ENDBITFIELD
ENDREGISTER

REGISTER    RSSI_DCCAL1    0x0641
    BITFIELD   DCO2<6:0>
        POSITION=<13:7>
        DEFAULT=0100000
        MODE=RW
        #! Value of RSSI offset DAC2. Default: 32.
        #!     DCO2[6] - sign
        #!     DCO2[5:0] - magnitude
    ENDBITFIELD
    BITFIELD   DCO1<6:0>
        POSITION=<6:0>
        DEFAULT=0100000
        MODE=RW
        #! Value of RSSI offset DAC1. Default: 32.
        #!     DCO1[6] - sign
        #!     DCO1[5:0] - magnitude
    ENDBITFIELD
ENDREGISTER

"""
