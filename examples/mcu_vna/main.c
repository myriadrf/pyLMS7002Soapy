#include "LMS7002_REGx51_SDCC.h"
#include "spi.h"	  
#include "LMS7002M_parameters_compact.h"

#define cordic_1K 0x000026DD
#define half_pi 0x00006487
#define MUL 16384.000000
#define CORDIC_NTAB 16


uint8_t currentInstruction;
uint8_t lastInstruction;

uint8_t __idata __at (0xFE) firmwareID;

enum
{
	MCU_WORKING = 0xFF,
	MCU_IDLE = 0x80,
	MCU_FAILURE = 0x81,
};

const int16_t cordic_ctab [] = {0x00003243, 0x00001DAC, 0x00000FAD, 0x000007F5, 0x000003FE, 0x000001FF, 0x000000FF, 0x0000007F, 0x0000003F, 0x0000001F, 0x0000000F, 0x00000007, 0x00000003, 0x00000001 };

// Calculate approximate sin(theta) and cos(theta) with CORDIC algorithm
// abs(theta) <= half_pi (0x6487)
void cordic(int16_t theta, int16_t *s, int16_t *c)
{
  int16_t tx, ty, tz;
  int16_t x=cordic_1K,y=0,z=theta;
  uint8_t n = 14;
  uint8_t k;
  int8_t d;
  
  for (k=0; k<n; ++k)
  {
    d = z>=0 ? 0 : -1;
    tx = x - (((y>>k) ^ d) - d);
    ty = y + (((x>>k) ^ d) - d);
    tz = z - ((cordic_ctab[k] ^ d) - d);
    x = tx; y = ty; z = tz;
  }  
 *c = x*2; *s = y*2;
}


#define x400reg 0x0081
#define x400reg_ADC (0x0081 | 1<<13)
uint32_t GetRSSI()
{
    uint32_t RSSI;
	//flip capture
	SPI_write(0x0400, x400reg);
	SPI_write(0x0400, x400reg | 0x8000);
    RSSI = SPI_read(0x040F);
    RSSI <<= 2;
    RSSI += SPI_read(0x040E);
    return RSSI;
}

int16_t GetADCI()
{
	//flip capture
	SPI_write(0x0400, x400reg_ADC);
	SPI_write(0x0400, x400reg_ADC | 0x8000);
    return (SPI_read(0x040E));
}

void loadIQ(int16_t I, int16_t Q)
{
    Modify_SPI_Reg_bits(DC_REG_TXTSP, I);
    Modify_SPI_Reg_bits(TSGDCLDI_TXTSP, 0);
    Modify_SPI_Reg_bits(TSGDCLDI_TXTSP, 1);
    Modify_SPI_Reg_bits(DC_REG_TXTSP, Q);
    Modify_SPI_Reg_bits(TSGDCLDQ_TXTSP, 0);
    Modify_SPI_Reg_bits(TSGDCLDQ_TXTSP, 1);
}

//
// Find a phase with minimum RSSI
// 180 deg is 0x6487
//
int16_t findPhase(void)
{
    int16_t startAngle, stopAngle, angle, dAngle, phase;
    int16_t s, c;
    uint32_t minRSSI, RSSI;
    int cnt;
    
    Modify_SPI_Reg_bits(CAPSEL, 0); // RSSI output
    
    minRSSI = ((uint32_t)1)<<31;
    
    startAngle = -half_pi;
    stopAngle = half_pi;
    phase = 0;

    // Determine the phase in the range +- 90 deg
    for (dAngle = 1024; dAngle > 16; dAngle=dAngle/4)
    {
        cordic(startAngle, &s, &c);  // Calculate sin(angle), cos(angle)    
        for(angle = startAngle; angle <= stopAngle; angle+=dAngle)
        {
            loadIQ(s, c);
            cordic(angle+dAngle, &s, &c);  // Calculate sin and cos while waiting for RSSI to settle
            RSSI = 0;
            for (cnt = 0; cnt<8; cnt++)
                RSSI += GetRSSI();
            RSSI /= 8;
            if(minRSSI > RSSI) {
                minRSSI = RSSI;
                phase = angle;
            }        
        }
        startAngle = phase - 2*dAngle;
        if (((phase < 0) && (startAngle>0)) || (startAngle<-half_pi))  // Check for overflow
            startAngle = -half_pi;
        stopAngle = phase + 2*dAngle;
        if ((phase > 0) && (stopAngle<0) || (startAngle>half_pi))  // Check for overflow
            stopAngle = half_pi;
     }
     
     // Phase needs to be divided by 2 to avoid overflow if 180 deg is added
     phase = phase/2;
     
     // Check if we need to add 180 deg
     if (GetADCI() > 511)
        if (phase>0)
            phase -= half_pi; // half_pi now represents pi since the phase is divided by two
        else
            phase += half_pi; // half_pi now represents pi since the phase is divided by two
    Modify_SPI_Reg_bits(CAPSEL, 0); // RSSI output
    loadIQ((int16_t)0x7FFF, (int16_t)0x8000);
     
     return phase;   
}

// Return averaged RSSI
uint32_t AverageRSSI(void){
    int i;
    uint32_t RSSI = 0;
    Modify_SPI_Reg_bits(CAPSEL, 0); // RSSI output
    for(i=0; i<64; i++){
        RSSI += GetRSSI();
    }
    RSSI = RSSI/64;
    return(RSSI);
}

/*
	P1[7] : 0-MCU idle, 1-MCU_working
	P1[6:0] : return status (while working = 0x3F)
*/

void main()  //main routine
{
    uint8_t t0, t1, t2, t3;
    t0 = t1 = t2 = t3 = 0;
	//SP=0xD0; // Set stack pointer
	DIR0=0x00; // ;DIR0 - Configure P0 as all inputs
  	DIR1=0xFF;  // ;DIR1 - Configure P1 as all outputs
  	DIR2=0x07;  // ;DIR2 -  Configure P2_3 is input
	IEN1=0;//0x04;  //EX2=1 enable external interrupt 2

	ucSCLK=0; //repairs external SPI
	ucSEN=1;//
	
	firmwareID = 0x31;	

	//P1 returns MCU status	
	P1 = MCU_IDLE; 
	lastInstruction = P0;
	while(1) 
	{				
		currentInstruction = P0;
		if(currentInstruction != lastInstruction)
		{
			lastInstruction = currentInstruction;
			if(currentInstruction == 0)
				P1 = MCU_IDLE;
			else if(currentInstruction == 1)  // Measure averaged RSSI
			{
			    uint32_t RSSI;
				P1 = MCU_WORKING;
				RSSI = AverageRSSI();
				t0 = RSSI & 0xFF;
				t1 = (RSSI>>8) & 0xFF;
				t2 = (RSSI>>16) & 0xFF;
				P1 = MCU_IDLE;				
			}
			else if(currentInstruction == 2)  // Measure phase
			{
				int16_t phase;
				P1 = MCU_WORKING;				
				phase = findPhase();
				t0 = phase & 0xFF;
				t1 = (phase>>8) & 0xFF;
				P1 = MCU_IDLE;
			}
			else if(currentInstruction == 0x10) // Read t0
			{
				P1 = t0;
			}
			else if(currentInstruction == 0x11) // Read t1
			{
				P1 = t1;
			}
			else if(currentInstruction == 0x12) // Read t2
			{
				P1 = t2;
			}
			else if(currentInstruction == 0x13) // Read t3
			{
				P1 = t3;
			}
			else if(currentInstruction == 255) // return program ID
			{	
				P1 = MCU_IDLE | firmwareID;
			}
		} 		
	}
}

