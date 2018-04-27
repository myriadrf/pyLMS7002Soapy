/*--------------------------------------------------------------------------
LMS7002_REGx51.h (Ver 1.0)

Header file for the LIME MCU chip.
Copyright (c) 2013 LIME, Inc.  All rights reserved.
--------------------------------------------------------------------------*/

/*------------------------------------------------
Make sure that this file gets included only once.
------------------------------------------------*/
#ifndef __LMS7002_H__
#define __LMS7002_H__

/*------------------------------------------------
Byte Registers
------------------------------------------------*/
__sfr __at (0x80) P0;
__sfr __at (0x81) SP;
__sfr __at (0x82) DPL0; 
__sfr __at (0x83) DPH0; 
__sfr __at (0x84) DPL1; 
__sfr __at (0x85) DPH1;
__sfr __at (0x86) DPS; 
__sfr __at (0x87) PCON; 
__sfr __at (0x88) TCON; 
__sfr __at (0x89) TMOD;
__sfr __at (0x8A) TL0;
__sfr __at (0x8B) TL1;
__sfr __at (0x8C) TH0;
__sfr __at (0x8D) TH1;
__sfr __at (0x8E) PMSR; 
__sfr __at (0x90) P1; 
__sfr __at (0x91) DIR1; 
__sfr __at (0x98) SCON;
__sfr __at (0x99) SBUF;
__sfr __at (0xA0) P2;
__sfr __at (0xA1) DIR2; 
__sfr __at (0xA2) DIR0; 
__sfr __at (0xA8) IEN0; 
__sfr __at (0xA9) IEN1; 
__sfr __at (0xB0) EECTRL; 
__sfr __at (0xB1) EEDATA; 
__sfr __at (0xB8) IP0; 
__sfr __at (0xB9) IP1; 
__sfr __at (0xBF) USR2; 
__sfr __at (0xC0) IRCON; 
__sfr __at (0xC8) T2CON; 
__sfr __at (0xCA) RCAP2L; 
__sfr __at (0xCB) RCAP2H; 
__sfr __at (0xCC) TL2; 
__sfr __at (0xCD) TH2; 
__sfr __at (0xD0) PSW;
__sfr __at (0xE0) ACC;
__sfr __at (0xEC) REG0; 
__sfr __at (0XED) REG1; 
__sfr __at (0xEE) REG2; 
__sfr __at (0xEF) REG3; 
__sfr __at (0xF0) B; 
__sfr __at (0xF4) REG4; 
__sfr __at (0xF5) REG5; 
__sfr __at (0xF6) REG6; 
__sfr __at (0xF7) REG7; 
__sfr __at (0xFC) REG8; 
__sfr __at (0xFD) REG9; 

/*------------------------------------------------
P0 bits 
------------------------------------------------*/
__sbit __at (0x80) P0_0;
__sbit __at (0x81) P0_1;
__sbit __at (0x82) P0_2;
__sbit __at (0x83) P0_3;
__sbit __at (0x84) P0_4;
__sbit __at (0x85) P0_5;
__sbit __at (0x86) P0_6;
__sbit __at (0x87) P0_7;

/*------------------------------------------------
TCON bits
------------------------------------------------*/
__sbit __at (0x88) IT0;
__sbit __at (0x89) IE0;
__sbit __at (0x8A) IT1;
__sbit __at (0x8B) IE1;
__sbit __at (0x8C) TR0;
__sbit __at (0x8D) TF0;
__sbit __at (0x8E) TR1;
__sbit __at (0x8F) TF1;

/*------------------------------------------------
P1 bits
------------------------------------------------*/
__sbit __at (0x90) P1_0;
__sbit __at (0x91) P1_1;
__sbit __at (0x92) P1_2;
__sbit __at (0x93) P1_3;
__sbit __at (0x94) P1_4;
__sbit __at (0x95) P1_5;
__sbit __at (0x96) P1_6;
__sbit __at (0x97) P1_7;

/*------------------------------------------------
SCON bits
------------------------------------------------*/
__sbit __at (0x98) RI;
__sbit __at (0x99) TI;
__sbit __at (0x9A) RB8;
__sbit __at (0x9B) TB8;
__sbit __at (0x9C) REN;
__sbit __at (0x9D) SM2;
__sbit __at (0x9E) SM1;
__sbit __at (0x9F) SM0;

/*------------------------------------------------
P2 bits
------------------------------------------------*/
__sbit __at (0xA0) P2_0;
__sbit __at (0xA1) P2_1;
__sbit __at (0xA2) P2_2;
__sbit __at (0xA3) P2_3;
/// reserved for SPI
__sbit __at (0xA0) ucSCLK;
__sbit __at (0xA1) ucSEN;
__sbit __at (0xA2) ucSDIN;
__sbit __at (0xA3) ucSDOUT;


/*------------------------------------------------
IEN0 bits
------------------------------------------------*/
__sbit __at (0xA8) EX0;       /* 1=Enable External interrupt 0 */
__sbit __at (0xA9) ET0;       /* 1=Enable Timer 0 interrupt */
__sbit __at (0xAA) EX1;       /* 1=Enable External interrupt 1 */
__sbit __at (0xAB) ET1;       /* 1=Enable Timer 1 interrupt */
__sbit __at (0xAC) ES0;       /* 1=Enable Serial port 0 interrupt */
__sbit __at (0xAD) ET2;		/* 1=Enable Timer 2 interrupt */
//sbit XX   = 0xAE; /* Don't Care */
__sbit __at (0xAF) EA;       /* 0=Disable all interrupts */

/*------------------------------------------------
EECTRL bits
------------------------------------------------*/
__sbit __at (0xB0) CMD0;       /* Command 0 bit */
__sbit __at (0xB1) CMD1;       /* Command 1 bit */
__sbit __at (0xB2) CMD2;       /* Command 2 bit */
__sbit __at (0xB3) CMD3;       /* Command 3 bit */
__sbit __at (0xB4) TX_ACK;       /* 1= ACK Transmited to EEPROM */
__sbit __at (0xB5) RX_ACK;	  /* 1= ACK Received from EEPROM */
__sbit __at (0xB6) BUSY;	  /* 1= Serial Data BUS is busy */
__sbit __at (0xB7) ERROR;       /* 1= Illegal Command Received */

/*------------------------------------------------
IP0 bits
------------------------------------------------*/
__sbit __at (0xB8) PX0; /* External iterrupt 0 priority bit */
__sbit __at (0xB9) PT0; /* Timer 0 iterrupt priority bit */
__sbit __at (0xBA) PX1; /* External iterrupt 1 priority bit */
__sbit __at (0xBB) PT1; /* Timer 1 iterrupt priority bit */
__sbit __at (0xBC) PS0; /* Serial port 0 iterrupt priority bit */
__sbit __at (0xBD) PT2; /* Timer 2 iterrupt priority bit */
//sbit XX   = 0xBE; /* Don't Care */
//sbit XX   = 0xBF; /* Don't Care */

/*------------------------------------------------
IRCON bits
------------------------------------------------*/
//sbit XX   = 0xCO; /* Don't Care */
//sbit XX   = 0xC1; /* Don't Care */
__sbit __at (0xC2) IE2; /* External iterrupt 2 flag bit */
__sbit __at (0xC3) IE3; /* External iterrupt 3 flag bit */
__sbit __at (0xC4) IE4; /* External iterrupt 4 flag bit */
__sbit __at (0xC5) IE5; /* External iterrupt 5 flag bit */
//sbit XX   = 0xC6; /* Don't Care */
//sbit XX   = 0xC7; /* Don't Care */

/*------------------------------------------------
T2CON bits
------------------------------------------------*/
__sbit __at (0xC8) CP_RL2; /* Capture/Reload Flag */
__sbit __at (0xC9) C_T2; /* 0/1 - Timer/Counter select */
__sbit __at (0xCA) TR2; /* 0/1 - Stop/Strat Timer */
__sbit __at (0xCB) EXEN2; /* Timer 2 enable Flag */
__sbit __at (0xCC) TCLK; /* Transmit Clock Flag */
__sbit __at (0xCD) RCLK; /* Receive Clock Flag */
__sbit __at (0xCE) EXF2; /* Timer 2 External Flag */
__sbit __at (0xCF) TF2; /* Timer 2 Overflow Flag */ 

/*------------------------------------------------
PSW bits
------------------------------------------------*/
__sbit __at (0xD0) P; /* Parity Flag */
//sbit XX	  = 0xD1; /* Don't Care */
__sbit __at (0xD2) OV; /* Overflow Flag */
__sbit __at (0xD3) RS0; /* Register Bank Select 0 */
__sbit __at (0xD4) RS1; /* Register Bank Select 0 */
//sbit XX   = 0xD5; /* Don't Care */
__sbit __at (0xD6) AC; /* Auxiliary Carry Flag */
__sbit __at (0xD7) CY; /* Carry Flag */


/*------------------------------------------------
TMOD Bit Values - Defines the bit position in the reg!!!
------------------------------------------------*/
#define T0_M0_   0x01 /* 0000 0001 = T0_M0 */
#define T0_M1_   0x02 /* 0000 0010 = T0_M1 */
#define T0_CT_   0x04 /* 0000 0100 = T0_CT */
#define T0_GATE_ 0x08 /* 0000 1000 = T0_GATE */
#define T1_M0_   0x10 /* 0001 0000 = T1_M0 */
#define T1_M1_   0x20 /* 0010 0000 = T1_M1 */
#define T1_CT_   0x40 /* 0100 0000 = T1_CT */
#define T1_GATE_ 0x80 /* 1000 0000 = T1_GATE */

#define T1_MASK_ 0xF0
#define T0_MASK_ 0x0F

/*------------------------------------------------
PCON Bit Values - Defines the bit position in the reg!!!
------------------------------------------------*/
#define IDL_    0x01
#define STOP_   0x02
#define SMOD_   0x80

/*------------------------------------------------
PMSR Bit Values - Defines the bit position in the reg!!!
------------------------------------------------*/
#define SEL_DIV_0_ 0x01
#define SEL_DIV_1_ 0x02
#define SEL_DIV_2_ 0x04

/*------------------------------------------------
Interrupt Vectors:
Interrupt Address = (Number * 8) + 3 
------------------------------------------------*/

#define IE0_VECTOR      0  /* 0x03 External Interrupt 0 */
#define TF0_VECTOR      1  /* 0x0B Timer 0 */
#define IE1_VECTOR      2  /* 0x13 External Interrupt 1 */
#define TF1_VECTOR      3  /* 0x1B Timer 1 */
#define SIO_VECTOR	4  /* 0x23 Serial channel 0 interrupt! (RI0/TI0) */
#define TF2_VECTOR      5  /* 0x2B Timer 2 */
//  SKIPPED #define X	6  /* RESERVED*/
#define IEX2_VECTOR	7    /* 0x3B External interrupt 2 */
#define IEX3_VECTOR	8    /* 0x43 External interrupt 3 */
#define IEX4_VECTOR	9    /* 0x4B External interrupt 4 */
#define IEX5_VECTOR	10   /* 0x53 External interrupt 5 */

/*------------------------------------------------
------------------------------------------------*/
#endif
