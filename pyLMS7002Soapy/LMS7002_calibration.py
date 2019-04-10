# ***************************************************************
# * Name:      LMS7002_calibration.py
# * Purpose:   Class implementing LMS7002 calibration functions
# * Author:    Lime Microsystems ()
# * Created:   2016-11-14
# * Copyright: Lime Microsystems (limemicro.com)
# * License:
# **************************************************************

from pyLMS7002Soapy.LMS7002_base import LMS7002_base


class LMS7002_calibration(LMS7002_base):

    def __init__(self, chip):
        self.chip = chip
        self.channel = None
        self.prefix = ""

    #
    # Filter calibration
    #

    #
    # DAC calibration
    #

    #
    # RX DC offset and LO leakage
    #

    def calibrateTIAoffset(self, channel):
        """
        Calibrates the TIA offset.
        RFE, RBB and RxTSP should be configured and running.
        SXR and CGEN should be tuned.
        Returns [DCOFFI_RFE, DCOFFQ_RFE]
        """
        chip = self.chip
        RxTSP = chip.RxTSP[channel]
        RFE = chip.RFE[channel]
        maxVal = RxTSP.RSSI
        chip.log('\tStarting TIA offset calibration for channel ' + channel + '. RSSI : ' + str(maxVal), 1)
        ind = 0
        DCOFFQ_RFE = 0
        offsList = [32, 16, 8, 4, 2, 1]
        for offs in offsList:
            for tmp in [ind - offs, ind, ind + offs]:
                RFE.DCOFFQ_RFE = tmp
                val = RxTSP.RSSI
                if val < maxVal:
                    ind = tmp
                    DCOFFQ_RFE = tmp
                    maxVal = val
        RFE.DCOFFQ_RFE = DCOFFQ_RFE

        ind = 0
        offsList = [32, 16, 8, 4, 2, 1]
        DCOFFI_RFE = 0
        for offs in offsList:
            for tmp in [ind - offs, ind, ind + offs]:
                RFE.DCOFFI_RFE = tmp
                val = RxTSP.RSSI
                if val < maxVal:
                    ind = tmp
                    DCOFFI_RFE = tmp
                    maxVal = val
        RFE.DCOFFI_RFE = DCOFFI_RFE
        chip.log(
            '\tEnding TIA calibration. RSSI : ' + str(maxVal) + ', DCOFFI = ' + str(DCOFFI_RFE) + ', DCOFFQ = ' + str(
                DCOFFQ_RFE), 1)
        return [DCOFFI_RFE, DCOFFQ_RFE]

    def calibrateTxOffset(self, channel):
        chip = self.chip
        RxTSP = chip.RxTSP[channel]
        TxTSP = chip.TxTSP[channel]
        DCOFFI = 0
        DCOFFQ = 0
        TxTSP.DCOFFI = 0
        TxTSP.DCOFFQ = 0
        TxTSP.DC_BYP = 'BYP'
        maxVal = RxTSP.RSSI
        chip.log('\tStarting TxTSP offset calibration for channel ' + channel + '. RSSI : ' + str(maxVal))
        ind = 0
        offsList = [64, 32, 16, 8, 4, 2, 1]
        for offs in offsList:
            for tmp in [ind - offs, ind, ind + offs]:
                TxTSP.DCCORRI = tmp
                val = RxTSP.RSSI
                if val < maxVal:
                    ind = tmp
                    DCOFFI = tmp
                    maxVal = val
        TxTSP.DCCORRI = DCOFFI

        ind = 0
        offsList = [64, 32, 16, 8, 4, 2, 1]
        for offs in offsList:
            for tmp in [ind - offs, ind, ind + offs]:
                TxTSP.DCCORRQ = tmp
                val = RxTSP.RSSI
                if val < maxVal:
                    ind = tmp
                    DCOFFQ = tmp
                    maxVal = val
        TxTSP.DCCORRQ = DCOFFQ
        chip.log('\tEnding RSSI : ' + str(maxVal) + ', DCOFFI = ' + str(DCOFFI) + ', DCOFFQ = ' + str(DCOFFQ), 1)
        return [DCOFFI, DCOFFQ]

    def calibrateTxIQ(self, channel):
        chip = self.chip
        RxTSP = chip.RxTSP[channel]
        TxTSP = chip.TxTSP[channel]
        GCORRI = 2047
        GCORRQ = 2047
        TxTSP.GCORRI = GCORRI
        TxTSP.GCORRQ = GCORRQ
        TxTSP.GC_BYP = 'USE'
        maxVal = RxTSP.RSSI
        chip.log('\tStarting TxTSP IQ calibration for channel ' + channel + '. RSSI : ' + str(maxVal))
        # TxTSP.PH_BYP = 'BYP'

        for xx in range(0, 2):
            for tmp in range(1800, 2048):
                TxTSP.GCORRQ = tmp
                val = RxTSP.RSSI
                if val < maxVal:
                    print("Q ", val)
                    GCORRQ = tmp
                    maxVal = val
            TxTSP.GCORRQ = GCORRQ
            maxVal = RxTSP.RSSI
            for tmp in range(1800, 2048):
                TxTSP.GCORRI = tmp
                val = RxTSP.RSSI
                if val < maxVal:
                    print("I ", val)
                    GCORRI = tmp
                    maxVal = val
            TxTSP.GCORRI = GCORRI

        maxVal = RxTSP.RSSI
        for tmp in range(-200, 200):
            TxTSP.IQCORR = tmp
            val = RxTSP.RSSI
            if val < maxVal:
                print("PH ", val)
                IQCORR = tmp
                maxVal = val
                TxTSP.IQCORR = IQCORR

        return

    def rxDCLO(self, channel, lna, lnaGain=15, pgaGain=31):
        """
        Calibrate the RX DC and LO offset for given channel and LNA.
        SXR should be tuned to target frequency.
        CGEN should be running at high frequency, e.g. 320 MHz.
        """
        chip = self.chip

        chip.log('Entering RX DC LO calibration, channel ' + channel + ' LNA ' + lna, 1)

        RFE = chip.RFE[channel]

        if channel == 'B':
            chip.RFE['A'].EN_NEXTRX_RFE = 1

        # Disable feedback paths
        RFE.PD_RLOOPB_1_RFE = 1
        RFE.PD_RLOOPB_2_RFE = 1
        RFE.EN_INSHSW_LB2_RFE = 1
        RFE.EN_INSHSW_LB1_RFE = 1

        RFE.PD_LNA_RFE = 0  # enable LNAs
        RFE.SEL_PATH_RFE = lna  # select the desired LNA
        RFE.PD_QGEN_RFE = 0  # enable LO
        RFE.PD_MXLOBUF_RFE = 0  # enable mixers

        if lna == 'LNAH':
            pass
        elif lna == 'LNAL':
            RFE.EN_INSHSW_L_RFE = 0
            RFE.EN_INSHSW_W_RFE = 1
        else:
            RFE.EN_INSHSW_L_RFE = 1
            RFE.EN_INSHSW_W_RFE = 0
        RFE.G_LNA_RFE = lnaGain

        RFE.PD_TIA_RFE = 0  # enable TIA
        RFE.EN_DCOFF_RXFE_RFE = 1  # enable DC offset cancellation at TIA
        RFE.DCOFFI_RFE = 0
        RFE.DCOFFQ_RFE = 0
        RFE.G_TIA_RFE = 3  # max TIA gain

        RBB = chip.RBB[channel]
        RBB.PD_PGA_RBB = 0  # enable PGA
        RBB.OSW_PGA_RBB = 'ADC'  # route PGA to ADC
        RBB.INPUT_CTL_PGA_RBB = 'LPFBYP'  # bypass LPF
        RBB.G_PGA_RBB = pgaGain

        RxTSP = chip.RxTSP[channel]
        RxTSP.EN = 1
        RxTSP.DCCORR_AVG = 0
        RxTSP.GC_BYP = 'BYP'
        RxTSP.PH_BYP = 'BYP'
        RxTSP.DC_BYP = 'BYP'
        RxTSP.CMIX_BYP = 'BYP'
        RxTSP.HBD_OVR = '32'
        RxTSP.GFIR1_BYP = 'BYP'
        RxTSP.GFIR2_BYP = 'BYP'
        RxTSP.GFIR3_BYP = 'BYP'
        RxTSP.CAPSEL = 'RSSI'
        RxTSP.AGC_MODE = 'RSSI'

        # TODO: Check for ADC overload

        DCOFFI_RFE, DCOFFQ_RFE = self.calibrateTIAoffset(channel)
        # RxTSP.DC_BYP = 'USE'
        # maxVal = RxTSP.RSSI
        # chip.log('\tEnabling RX DC corrector. Residual RSSI = '+str(maxVal),1)

        return [DCOFFI_RFE, DCOFFQ_RFE]

    #
    # TX DC offset and LO leakage
    #

    def txCalibration(self, channel, band):
        """
        Calibrate the TX for a given channel (A, B) and band (1 or 2).
        SXR and SXT should be tuned to target frequency, with SXT>SXR by a few MHz.
        CGEN should be running, e.g. 320 MHz.
        TX DC calibration depends on the TBB gain setting.
        """
        chip = self.chip

        chip.log('Entering TX DC LO calibration, channel ' + channel, 1)

        TxTSP = chip.TxTSP[channel]
        TxTSP.TSGMODE = 'DC'
        TxTSP.INSEL = 'TEST'
        TxTSP.CMIX_BYP = 'BYP'
        TxTSP.GFIR1_BYP = 'BYP'
        TxTSP.GFIR2_BYP = 'BYP'
        TxTSP.GFIR3_BYP = 'BYP'
        TxTSP.GC_BYP = 'BYP'
        TxTSP.DC_BYP = 'BYP'
        TxTSP.PH_BYP = 'BYP'
        I = 0  # 0x7FFF
        Q = 0  # 0x8000
        TxTSP.loadDCIQ(I, Q)

        # Configure TRF
        TRF = chip.TRF[channel]
        TRF.LOSS_MAIN_TXPAD_TRF = 0

        TRF.PD_TLOBUF_TRF = 0
        TRF.PD_TXPAD_TRF = 0
        TRF.EN_LOOPB_TXPAD_TRF = 1
        TRF.L_LOOPB_TXPAD_TRF = 0

        if band == 1:
            TRF.SEL_BAND1_TRF = 1
            TRF.SEL_BAND2_TRF = 0
        else:
            TRF.SEL_BAND1_TRF = 0
            TRF.SEL_BAND2_TRF = 1

        if channel == 'B':
            chip.TRF['A'].EN_NEXTTX_TRF = 1
        else:
            TRF.EN_NEXTTX_TRF = 0

        RFE = chip.RFE[channel]

        if channel == 'B':
            chip.RFE['A'].EN_NEXTRX_RFE = 1
        else:
            RFE.EN_NEXTRX_RFE = 0

        # Enable feedback paths
        if band == 1:
            # Band 1 goes to LNAW path
            RFE.PD_RLOOPB_1_RFE = 0
            RFE.EN_INSHSW_LB1_RFE = 0
            RFE.PD_RLOOPB_2_RFE = 1
            RFE.EN_INSHSW_LB2_RFE = 1
        else:
            # Band 2 goes to LNAL path
            RFE.PD_RLOOPB_1_RFE = 1
            RFE.EN_INSHSW_LB1_RFE = 1
            RFE.PD_RLOOPB_2_RFE = 0
            RFE.EN_INSHSW_LB2_RFE = 0

        RFE.PD_LNA_RFE = 1  # disable LNAs
        RFE.EN_INSHSW_L_RFE = 0
        RFE.EN_INSHSW_W_RFE = 0

        if band == 1:  # select the desired path
            RFE.SEL_PATH_RFE = 'LNAW'
        else:
            RFE.SEL_PATH_RFE = 'LNAL'

        RFE.PD_QGEN_RFE = 0  # enable LO
        RFE.PD_MXLOBUF_RFE = 0  # enable mixers

        RFE.PD_TIA_RFE = 0  # enable TIA
        RFE.EN_DCOFF_RXFE_RFE = 1  # enable DC offset cancellation at TIA
        RFE.G_TIA_RFE = 3  # max TIA gain

        RBB = chip.RBB[channel]
        RBB.PD_PGA_RBB = 0  # enable PGA
        RFE.DCOFFI_RFE = 0
        RFE.DCOFFQ_RFE = 0
        RBB.OSW_PGA_RBB = 'ADC'  # route PGA to ADC
        RBB.G_PGA_RBB = 31  # max PGA gain

        # LPF settings
        RBB.INPUT_CTL_PGA_RBB = 'LPFL'  # use LPFL
        RBB.R_CTL_LPF_RBB = 16
        RBB.RCC_CTL_LPFL_RBB = 0
        RBB.C_CTL_LPFL_RBB = 2047
        RBB.PD_LPFL_RBB = 0
        RBB.PD_LPFH_RBB = 1
        RBB.EN_LB_LPFL_RBB = 1
        RBB.EN_LB_LPFH_RBB = 0

        # Without LPF
        # RBB.INPUT_CTL_PGA_RBB = 'LPFBYP' # do not use LPFL

        RxTSP = chip.RxTSP[channel]
        RxTSP.EN = 1
        RxTSP.DCCORR_AVG = 0
        RxTSP.GC_BYP = 'BYP'
        RxTSP.PH_BYP = 'BYP'
        RxTSP.DC_BYP = 'BYP'
        RxTSP.CMIX_BYP = 'BYP'
        RxTSP.HBD_OVR = '32'
        RxTSP.GFIR1_BYP = 'BYP'
        RxTSP.GFIR2_BYP = 'BYP'
        RxTSP.GFIR3_BYP = 'BYP'
        RxTSP.CAPSEL = 'RSSI'
        RxTSP.AGC_MODE = 'RSSI'

        RFE.G_RXLOOPB_RFE = 0  # min loopback gain

        self.calibrateTIAoffset(channel)

        RxTSP.DC_BYP = 'USE'
        maxVal = RxTSP.RSSI
        chip.log('\tEnabling RX DC corrector. Residual RSSI = ' + str(maxVal), 1)

        RFE.G_RXLOOPB_RFE = 15  # max loopback gain

        TxTSP.CMIX_BYP = 'USE'
        I = 0x7FFF
        Q = 0x8000
        TxTSP.loadDCIQ(I, Q)

        dF = chip.CGEN.getADCFrequency() / 32  # RX is tuned by dF, which is at 0.5 fs after decimation by 32
        # NCO
        TXNCO = chip.NCO["TX" + channel]
        TXNCO.MODE = 0
        TXNCO.setNCOFrequency(0, dF * 0.5)
        TXNCO.SEL = 0

        chip.log('\tEnabling looback and test signal', 1)
        maxVal = RxTSP.RSSI
        chip.log('\tRSSi = ' + str(maxVal), 1)

        while maxVal > 85e3:
            RFE.G_RXLOOPB_RFE -= 1  # reduce loopback gain
            chip.log('\tReducing loopback gain to ' + str(RFE.G_RXLOOPB_RFE), 1)
            maxVal = RxTSP.RSSI

        self.calibrateTxIQ(channel)
        return
        # TxDCOFFI, TxDCOFFQ = self.calibrateTxOffset(channel)

    #    #
    #    # TX DC offset and LO leakage
    #    #

    #    def txDCLO(self, channel, band, DCOFFI_RFE=0, DCOFFQ_RFE=0):
    #        """
    #        Calibrate the TX DC and LO offset for given channel (A, B) and band (1 or 2).
    #        SXR and SXT should be tuned to target frequency, with SXT>SXR by a few MHz.
    #        CGEN should be running, e.g. 320 MHz.
    #        TX DC calibration depends on the TBB gain setting.
    #        """
    #        chip = self.chip
    #
    #        chip.log('Entering TX DC LO calibration, channel '+channel+' DCI = '+str(DCOFFI_RFE)+', DCQ = '+str(DCOFFQ_RFE), 1)
    #
    #        TxTSP = chip.TxTSP[channel]
    #        TxTSP.TSGMODE = 'DC'
    #        TxTSP.INSEL = 'TEST'
    #        TxTSP.CMIX_BYP = 'BYP'
    #        TxTSP.GFIR1_BYP = 'BYP'
    #        TxTSP.GFIR2_BYP = 'BYP'
    #        TxTSP.GFIR3_BYP = 'BYP'
    #        I = 0 #0x7FFF
    #        Q = 0 #0x8000
    #        TxTSP.loadDCIQ(I, Q)
    #
    #        # Configure TRF
    #        TRF = chip.TRF[channel]
    #        TRF.LOSS_MAIN_TXPAD_TRF = 0
    #
    #        TRF.PD_TLOBUF_TRF = 0
    #        TRF.PD_TXPAD_TRF = 0
    #        TRF.EN_LOOPB_TXPAD_TRF = 1
    #        TRF.L_LOOPB_TXPAD_TRF = 3

    #        if band==1:
    #            TRF.SEL_BAND1_TRF=1
    #            TRF.SEL_BAND2_TRF=0
    #        else:
    #            TRF.SEL_BAND1_TRF=0
    #            TRF.SEL_BAND2_TRF=1
    #
    #        if channel=='B':
    #            chip.TRF['A'].EN_NEXTTX_TRF = 1
    #        else:
    #            TRF.EN_NEXTTX_TRF = 0
    #
    #        RFE = chip.RFE[channel]
    #
    #        if channel == 'B':
    #            chip.RFE['A'].EN_NEXTRX_RFE = 1
    #        else:
    #            RFE.EN_NEXTRX_RFE = 0
    #
    #        # Enable feedback paths
    #        if band==1:
    #            # Band 1 goes to LNAW path
    #            RFE.PD_RLOOPB_1_RFE = 0
    #            RFE.EN_INSHSW_LB1_RFE = 0
    #            RFE.PD_RLOOPB_2_RFE = 1
    #            RFE.EN_INSHSW_LB2_RFE = 1
    #        else:
    #            # Band 2 goes to LNAL path
    #            RFE.PD_RLOOPB_1_RFE = 1
    #            RFE.EN_INSHSW_LB1_RFE = 1
    #            RFE.PD_RLOOPB_2_RFE = 0
    #            RFE.EN_INSHSW_LB2_RFE = 0
    #
    #        RFE.PD_LNA_RFE = 1      # disable LNAs
    #        RFE.EN_INSHSW_L_RFE = 0
    #        RFE.EN_INSHSW_W_RFE = 0

    #        if band==1: # select the desired path
    #            RFE.SEL_PATH_RFE = 'LNAW'
    #        else:
    #            RFE.SEL_PATH_RFE = 'LNAL'

    #        RFE.PD_QGEN_RFE = 0     # enable LO
    #        RFE.PD_MXLOBUF_RFE = 0  # enable mixers
    #
    #        RFE.PD_TIA_RFE = 0      # enable TIA
    #        RFE.EN_DCOFF_RXFE_RFE = 1 # enable DC offset cancellation at TIA
    #        RFE.G_TIA_RFE = 3       # max TIA gain
    #
    #        RBB = chip.RBB[channel]
    #        RBB.PD_PGA_RBB = 0      # enable PGA
    #        RFE.DCOFFI_RFE = DCOFFI_RFE
    #        RFE.DCOFFQ_RFE = DCOFFQ_RFE
    #        RBB.OSW_PGA_RBB = 'ADC' # route PGA to ADC
    #        RBB.INPUT_CTL_PGA_RBB = 'LPFBYP' # bypass LPF
    #        RBB.G_PGA_RBB = 31      # max PGA gain
    #
    #        RxTSP = chip.RxTSP[channel]
    #        RxTSP.EN = 1
    #        RxTSP.DCCORR_AVG = 0
    #        RxTSP.GC_BYP = 'BYP'
    #        RxTSP.PH_BYP = 'BYP'
    #        RxTSP.DC_BYP = 'BYP'
    #        RxTSP.CMIX_BYP = 'BYP'
    #        RxTSP.HBD_OVR = '8'
    #        RxTSP.GFIR1_BYP = 'BYP'
    #        RxTSP.GFIR2_BYP = 'BYP'
    #        RxTSP.GFIR3_BYP = 'BYP'
    #        RxTSP.CAPSEL = 'RSSI'
    #        RxTSP.AGC_MODE = 'RSSI'

    #
    #        RFE.G_RXLOOPB_RFE = 15  # max loopback gain
    #
    #        maxVal = RxTSP.RSSI
    #        while maxVal>85e3:
    #            RFE.G_RXLOOPB_RFE -= 1  # reduce loopback gain
    #            maxVal = RxTSP.RSSI

    #        chip.log('\tStarting RSSI : '+str(maxVal))
    #
    #        DCOFFI = 0
    #        DCOFFQ = 0
    #
    #        maxVal = RxTSP.RSSI
    #
    #        ind = 0
    #        offsList = [64, 32, 16, 8, 4, 2, 1]
    #        for offs in offsList:
    #            for tmp in [ind-offs, ind, ind+offs]:
    #                TxTSP.DCCORRI = tmp
    #                val = RxTSP.RSSI
    #                if val < maxVal:
    #                    ind = tmp
    #                    DCOFFI = tmp
    #                    maxVal = val
    #        TxTSP.DCCORRI = DCOFFI

    #        ind = 0
    #        offsList = [64, 32, 16, 8, 4, 2, 1]
    #        for offs in offsList:
    #            for tmp in [ind-offs, ind, ind+offs]:
    #                TxTSP.DCCORRQ = tmp
    #                val = RxTSP.RSSI
    #                if val < maxVal:
    #                    ind = tmp
    #                    DCOFFQ = tmp
    #                    maxVal = val
    #        TxTSP.DCCORRQ = DCOFFQ
    #        chip.log('\tEnding RSSI : ' +str(maxVal) + ', DCOFFI = ' + str(DCOFFI) + ', DCOFFQ = '+ str(DCOFFQ), 1)
    #        return [DCOFFI, DCOFFQ]

    #
    # RX filter response
    #

    def rxFilterResponse(self, channel, filterName, freqPoints=None, DCOFFI_RFE=0, DCOFFQ_RFE=0):
        """
        Measure filter response.
        SXR and SXT should be tuned to the same frequency.
        CGEN should be running, e.g. 320 MHz.
        Filter path and settings should be set.
        For example:
        RBB = lms7002.RBB['A']
        RBB.R_CTL_LPF_RBB = 16
        RBB.RCC_CTL_LPFL_RBB = 0
        RBB.C_CTL_LPFL_RBB = 2047
        """
        chip = self.chip
        chip.log('Entering RX filter response, channel ' + channel + ' DCI = ' + str(DCOFFI_RFE) + ', DCQ = ' + str(
            DCOFFQ_RFE), 1)

        TxTSP = chip.TxTSP[channel]
        TxTSP.TSGMODE = 'DC'
        TxTSP.INSEL = 'TEST'
        TxTSP.CMIX_BYP = 'USE'
        TxTSP.GFIR1_BYP = 'BYP'
        TxTSP.GFIR2_BYP = 'BYP'
        TxTSP.GFIR3_BYP = 'BYP'
        I = 0
        Q = 0
        TxTSP.loadDCIQ(I, Q)

        # Configure TRF
        TRF = chip.TRF[channel]
        TRF.LOSS_MAIN_TXPAD_TRF = 0

        TRF.PD_TLOBUF_TRF = 0
        TRF.PD_TXPAD_TRF = 0
        TRF.EN_LOOPB_TXPAD_TRF = 0
        TRF.L_LOOPB_TXPAD_TRF = 3
        TRF.EN_NEXTTX_TRF = 0

        TBB = chip.TBB[channel]
        TBB.CG_IAMP_TBB = 31
        TBB.EN_G_TBB = 1

        TBB.PD_LPFH_TBB = 0
        # TBB.PD_LPFH_TBB = 1
        TBB.PD_LPFLAD_TBB = 1
        TBB.PD_LPFS5_TBB = 1
        TBB.LOOPB_TBB = 3
        # TBB.LOOPB_TBB = 1

        # NCO
        TXNCO = chip.NCO["TX" + channel]
        TXNCO.MODE = 0
        TXNCO.setNCOFrequency(0, 1e3)
        TXNCO.SEL = 0

        RFE = chip.RFE[channel]
        RFE.EN_NEXTRX_RFE = 0

        # Band 1 goes to LNAW path
        RFE.PD_RLOOPB_1_RFE = 1
        RFE.EN_INSHSW_LB1_RFE = 1
        RFE.PD_RLOOPB_2_RFE = 1
        RFE.EN_INSHSW_LB2_RFE = 1

        RFE.PD_LNA_RFE = 1  # disable LNAs
        RFE.EN_INSHSW_L_RFE = 0
        RFE.EN_INSHSW_W_RFE = 0

        RFE.PD_QGEN_RFE = 1  # disable LO
        RFE.PD_MXLOBUF_RFE = 1  # disable mixers

        RFE.PD_TIA_RFE = 1  # disable TIA
        RFE.EN_DCOFF_RXFE_RFE = 0  # disable DC offset cancellation at TIA

        RBB = chip.RBB[channel]
        RBB.PD_PGA_RBB = 0  # enable PGA
        RBB.OSW_PGA_RBB = 'ADC'  # route PGA to ADC
        RBB.INPUT_CTL_PGA_RBB = filterName  # select filter path
        RBB.G_PGA_RBB = 31  # max PGA gain

        if filterName == 'LPFL':
            RBB.PD_LPFL_RBB = 0
            RBB.PD_LPFH_RBB = 1
            RBB.EN_LB_LPFL_RBB = 1
            RBB.EN_LB_LPFH_RBB = 0
        else:
            RBB.PD_LPFL_RBB = 1
            RBB.PD_LPFH_RBB = 0
            RBB.EN_LB_LPFL_RBB = 0
            RBB.EN_LB_LPFH_RBB = 1

        RxTSP = chip.RxTSP[channel]
        RxTSP.EN = 1
        RxTSP.DCCORR_AVG = 0
        RxTSP.GC_BYP = 'BYP'
        RxTSP.PH_BYP = 'BYP'
        RxTSP.DC_BYP = 'BYP'
        RxTSP.CMIX_BYP = 'BYP'
        RxTSP.HBD_OVR = '8'
        RxTSP.GFIR1_BYP = 'BYP'
        RxTSP.GFIR2_BYP = 'BYP'
        RxTSP.GFIR3_BYP = 'BYP'
        RxTSP.CAPSEL = 'RSSI'
        RxTSP.AGC_MODE = 'RSSI'

        TBB.LOOPB_TBB = 0
        # print RxTSP.RSSI

        TBB.LOOPB_TBB = 3
        # TBB.LOOPB_TBB = 1
        I = 0x7FFF
        Q = 0x8000
        TxTSP.loadDCIQ(I, Q)

        maxVal = RxTSP.RSSI
        while maxVal > 85e3:
            chip.log("\tReducing PGA gain to " + str(RBB.G_PGA_RBB), 1)
            RBB.G_PGA_RBB -= 1  # reduce loopback gain
            maxVal = RxTSP.RSSI

        if freqPoints is None:
            freqs = []
            for decade in range(4, 8):
                for point in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                    freqs.append(point * 10 ** decade)
        else:
            freqs = freqPoints

        mag = []
        for freq in freqs:
            TXNCO.setNCOFrequency(0, freq)
            mag.append(RxTSP.RSSI)

        return [freqs, mag]

    #
    # MCU commands
    #

    @staticmethod
    def _getCommand(cmd):
        if cmd == 'IDLE':
            return 0
        elif cmd == 'CALIBRATE_TX':
            return 1
        elif cmd == 'CALIBRATE_RX':
            return 2
        elif cmd == 'PROGRAM_ID':
            return 255
        else:
            raise ValueError("Unknown command")

    @staticmethod
    def _getStatus(stat):
        if stat == 'MCU_IDLE':
            return 0x80
        elif stat == 'MCU_WORKING':
            return 0xFF
        elif stat == 'CAL_PROG_ID':
            return 1
        else:
            raise ValueError("Unknown command")

    #
    # IQ calibration by on-chip MCU
    #

    def mcuLoadIQcalibration(self):
        """
        Load IQ calibration program to MCU
        """
        chip = self.chip
        immMode = self.chip.SPIImmediate
        chip.SPIImmediate = True

        mspi = chip.mSPI
        mspi.reset()
        mspi.loadHex(self.getIQcalibrationHex(), mode='SRAM', isString=True)

        # Check if MCU is programmed
        if mspi.PROGRAMMED == 0:
            self.chip.SPIImmediate = immMode
            chip.log("MCU programming failed", 1)
            return False

        # Check program ID
        mspi.P0 = self._getCommand('IDLE')
        mspi.P0 = self._getCommand('PROGRAM_ID')
        if mspi.P1 != self._getStatus('MCU_IDLE') + self._getStatus('CAL_PROG_ID'):
            self.chip.SPIImmediate = immMode
            chip.log("Wrong MCU program ID", 1)
            return False
        mspi.P0 = self._getCommand('IDLE')
        self.chip.SPIImmediate = immMode
        return True

    def mcuCalibrateTx(self):
        """
        Use the on-chip MCU to calibrate TX path.
        Channel is set by value of MAC, bandwidth by register 0x002D.
        """
        chip = self.chip
        immMode = self.chip.SPIImmediate
        chip.SPIImmediate = True

        mspi = chip.mSPI
        spiSW = mspi.SPISW_CTRL
        mspi.SPISW_CTRL = 'MCU'

        # Check if MCU is programmed
        if mspi.PROGRAMMED == 0:
            self.chip.SPIImmediate = immMode
            mspi.reset()
            chip.log("MCU not programmed", 1)
            mspi.SPISW_CTRL = spiSW
            return False

        # Check program ID
        mspi.P0 = self._getCommand('IDLE')
        mspi.P0 = self._getCommand('PROGRAM_ID')
        if mspi.P1 != self._getStatus('MCU_IDLE') + self._getStatus('CAL_PROG_ID'):
            self.chip.SPIImmediate = immMode
            chip.log("Wrong MCU program ID", 1)
            mspi.SPISW_CTRL = spiSW
            return False

        mspi.P0 = self._getCommand('IDLE')
        mspi.P0 = self._getCommand('CALIBRATE_TX')
        while mspi.P1 == self._getStatus('MCU_WORKING'):
            pass

        if mspi.P1 != self._getStatus('MCU_IDLE'):
            self.chip.SPIImmediate = immMode
            chip.log("Calibration failed", 1)
            mspi.SPISW_CTRL = spiSW
            return False

        mspi.P0 = self._getCommand('IDLE')

        self.chip.SPIImmediate = immMode
        mspi.SPISW_CTRL = spiSW
        return True

    def mcuCalibrateRx(self):
        """
        Use the on-chip MCU to calibrate RX path.
        Channel is set by value of MAC, bandwidth by register 0x002D,
        active path by SEL_PATH_RFE, which must be > 1.
        """
        chip = self.chip
        immMode = self.chip.SPIImmediate
        chip.SPIImmediate = True

        mspi = chip.mSPI
        spiSW = mspi.SPISW_CTRL
        mspi.SPISW_CTRL = 'MCU'

        # Check if MCU is programmed
        if mspi.PROGRAMMED == 0:
            self.chip.SPIImmediate = immMode
            mspi.reset()
            chip.log("MCU not programmed", 1)
            mspi.SPISW_CTRL = spiSW
            return False

        # Check program ID
        mspi.P0 = self._getCommand('IDLE')
        mspi.P0 = self._getCommand('PROGRAM_ID')
        if mspi.P1 != self._getStatus('MCU_IDLE') + self._getStatus('CAL_PROG_ID'):
            self.chip.SPIImmediate = immMode
            chip.log("Wrong MCU program ID", 1)
            mspi.SPISW_CTRL = spiSW
            return False

        mspi.P0 = self._getCommand('IDLE')
        mspi.P0 = self._getCommand('CALIBRATE_RX')
        while mspi.P1 == self._getStatus('MCU_WORKING'):
            pass

        if mspi.P1 != self._getStatus('MCU_IDLE'):
            self.chip.SPIImmediate = immMode
            chip.log("Calibration failed", 1)
            mspi.SPISW_CTRL = spiSW
            return False

        mspi.SPISW_CTRL = spiSW
        self.chip.SPIImmediate = immMode
        return True

    #
    # MCU hex files
    #

    @staticmethod
    def getIQcalibrationHex():
        return """:1019D400040841F5C28F041140A00000040C40A08B
                :0519E4000000011014D9
                :0619A400C3E53D953EFF86
                :1019AA0074017E00A807088005C333CE33CED8F968
                :0219BA00FF220A
                :101811007F2D7E001217B58E218F22EEC313FD7C22
                :1018210000E41202A68F0B8E0A8D098C08AB0BAA5D
                :101831000AA909A808C000C001C002C0037C00E5D4
                :1018410022547FFDE41202A6E4FBFA79C878421221
                :101851000204D003D002D001D00012000A8F0B8EF7
                :061861000A8D098C08222B
                :1012E6007DA37F897E00121901EF2401FDE43EFCF7
                :1012F600E41202A6C004C005C006C007E4FBFAF962
                :101306007840AF0BAE0AAD09AC08120204D003D088
                :1013160002D001D0001202048F558E548D538C5288
                :101326007DD07F887E00121901E48F598E58F557BB
                :10133600F5567DF07F87FE121901E4FCFDC004C05E
                :1013460005C006C007E559540FFFE4FE78101204E5
                :10135600C9D003D002D001D00012048AE41202A13F
                :10136600E4FBFA79807849120204C004C005C0067D
                :10137600C007AF59AE58AD57AC5678041204B6EF55
                :101386002401FFE43EFEE43DFDE43CFCE41202A140
                :10139600D003D002D001D00012000AAB55AA54A93E
                :0713A60053A8521200FB22C4
                :1016B7001212E68F4D8E4C8D4B8C4A7DCB7F897EE7
                :1016C700001219011219AAAC06AD07E41202A6A866
                :1016D70004A905AA06AB07AF4DAE4CAD4BAC4A12F9
                :1016E70002048F518E508D4F8C4E7DBB7F867E00BE
                :1016F700121901EF4E701F300109AF51AE50AD4FB7
                :10170700AC4E22E4FBFA79807840AF4DAE4CAD4B3E
                :10171700AC4A1202042230010AAF4DAE4CAD4BACBD
                :101727004A8012E4FBFA79807840AF51AE50AD4F52
                :06173700AC4E1202042278
                :101464007B9A7A997979784012000A8F3F8E3E8D63
                :031474003D8C3C70
                :10147700A20092011216B78F438E428D418C4030E5
                :1014870000067E027F4080047E047F408E448F45A5
                :10149700AB43AA42A941A840AF3FAE3EAD3DAC3CED
                :1014A700120204E4FBFA7980784F1200FB1202DF84
                :1014B7008F498E488D478C46E53B75F002A4FFE5C2
                :1014C700452402CDE43544CD2FFFED35F0FEC006AF
                :1014D700C007AF49AE48AD4778101204B6AD07ACA8
                :1014E70006D007D00612193DE53B75F002A4FFE5CB
                :1014F700452403CDE43544CD2FFFED35F0FEAC4850
                :05150700AD4902193D91
                :1010A4007D107F207E001219018F703002047B02B4
                :1010B40080027B017A007D107F207E0012173D7D27
                :1010C400D07F1E7E01121901E48F6B8E6AF569F5DB
                :1010D400687DF07F1D7E01121901E4FCFDC004C08F
                :1010E40005C006C007E56B540FFFE4FE7810120438
                :1010F400C9D003D002D001D00012048A8F6F8E6E43
                :101104008D6D8C6C7D867F1F7E01121901EF04FFAB
                :1011140074017E00A807088005C333CE33CED8F906
                :10112400FDAC06EC1202A6A804A905AA06AB07AFFB
                :101134000BAE0AAD09AC081202048F748E738D7263
                :101144008C717DAA7F1C7E01121901EF2401FDE43C
                :101154003EFCE41202A6C004C005C006C007AF6F7F
                :10116400AE6EAD6DAC6CE41202A1E4FBFA7980784A
                :1011740049120204C004C005C006C007AF6BAE6AC2
                :10118400AD69AC6878041204B6EF2404FFE43EFEB3
                :10119400E43DFDE43CFCE41202A1D003D002D00102
                :1011A400D00012000AAB74AA73A972A8711200FBD2
                :1011B400D003D002D001D0001200FB8F748E738D47
                :1011C400728C71E570FB7A007D107F207E0012170F
                :0A11D4003DAF74AE73AD72AC712232
                :1019EA00C3EE6480948050077CFF7DFF020360226F
                :10198A00AD07C3ED64809480500DED3395E0FE12EF
                :0A199A0019EAEF4440FF22AF0522D6
                :1018B6007D817C007F007E0412193D7D817C807FC6
                :1018C600007E0412193D7F0F7E041217B5EF7802D1
                :1018D600C333CE33CED8F9FFE4FCFDC004C005C047
                :1018E60006C0077D107F0E7E04121901E4FCFDD0B0
                :0B18F60003D002D001D00012048A22AF
                :1019BC007F2D7E001217B5EFD394405003EF7003C8
                :0819CC007F86228F107F80222C
                :100F5B00E510D3940440047F048002AF108F54E457
                :100F6B00FBFA7DEDFF7E0412173DE4F559E559C3FD
                :100F7B00951050191218B6E55925E024C4F582E4F2
                :100F8B003400F583EEF0A3EFF0055980E0E4F5595A
                :100F9B00E51014FFE559C39F4003021035AB59EB25
                :100FAB00C395104003021030EB25E024C4F582E416
                :100FBB003400F583E0FEA3E0FFE55925E024C4F5FA
                :100FCB0082E43400F583E0FCA3E0D39FEC9E405118
                :100FDB00E55925E024C4F582E43400F583E0FEA353
                :100FEB00E0FFE48F588E57F556F555EB25E024C4FA
                :100FFB00F582E43400F583E0FEA3E0FFE55925E03C
                :10100B0024C4F582E43400F583EEF0A3EFF0EB2576
                :10101B00E024C4F582E43400F583E557F0A3E558EA
                :10102B00F00B020FAA0559020F9BE4F558F557F583
                :10103B0056F555F559E559C395545030E55925E00A
                :10104B0024C4F582E43400F583E0FEA3E0FFE4FC66
                :10105B00FDE5582FFFE5573EFEED3556FDEC3555BA
                :10106B008F588E578D56F555055980C9AF58AE57C9
                :10107B00AD56AC55C007AF54AB07E4FAF9F8D0073F
                :10108B001203F88F588E578D568C5578F81204E84A
                :09109B00AF58AE57AD56AC55221A
                :10196400AB0512198AEF75F080A4FFAEF0C007C072
                :1019740006AF0312198AEFFDD0E0FCD0E04DFD7FE5
                :061984000E7E0102193D78
                :10150C007533007534207535007536207B017A00F3
                :10151C007D227F0C7E0412173DE4FBFA7DEDFF7EED
                :10152C000412173DAF34AD361219647B007A007982
                :10153C0033753D06120A147B007A007935753D0629
                :10154C007D60120A167B007A007933753D04120A0D
                :10155C00147B007A007935753D047D60120A16758E
                :10156C003D01753E0E753F6075400075410075423A
                :10157C00357543077B007A0079337DD77F0E7E016A
                :10158C00120802AF34AD36121964E4FBFA7D227FE7
                :06159C000C7E0402173D65
                :060A14007DD77F0E7E017C
                :100A1A008E378F388D398B3A8A3B893CE4F53E1202
                :100A2A000372F54885F047E538640E7004E53764CB
                :100A3A0001600AAE47AF48AA06AB078009AF481261
                :100A4A00198A7A00AB07AD39AF38AE3712173DE4D1
                :100A5A00F53EE53D14FFE53EC39F4003020B361207
                :100A6A000F5B8F428E418D408C3F1219A4C3E5481B
                :100A7A009FF548E5479EF547E538640E7004E5376B
                :100A8A006401600AAE47AF48AA06AB078009AF48BF
                :100A9A0012198A7A00AB07AD39AF38AE3712173D53
                :100AAA00120F5B8F468E458D448C43AB42AA41A9F7
                :100ABA0040A83FC31204A54017E53D24FEC3953E56
                :100ACA00FF1219AAEF2548F548EE3547F547802F5A
                :100ADA001219A4E5482FFDE5473EFCE53D14C395F0
                :100AEA003EFF1219AAEF2DFDEE3CFCE53D24FEC3A4
                :100AFA00953EFF1219AAC3ED9FF548EC9EF547E50E
                :100B0A0038640E7004E5376401600AAE47AF48AA3C
                :100B1A0006AB078009AF4812198A7A00AB07AD39CC
                :100B2A00AF38AE3712173D053E020A5C1219A4C34C
                :100B3A00E5489FF548E5479EF547120F5B8F428EC1
                :100B4A00418D408C3FE538640E7004E5376401C37B
                :100B5A00600E1219A5C3E5489FFBE5479EFA800F70
                :100B6A001219A5C3E5489FFF12198AEFFB7A00AD57
                :100B7A0039AF38AE3712173D120F5B8F468E458D4F
                :100B8A00448C43AB42AA41A940A83FC31204A550D2
                :100B9A00080548E54870020547E538640E7004E523
                :100BAA00376401600AAE47AF48AA06AB078009AFAF
                :100BBA004812198A7A00AB07AD39AF38AE37121727
                :100BCA003D120F5B8F468E458D448C43AB42AA4142
                :100BDA00A940A83FC31204A550300548E548700251
                :100BEA000547E538640E7004E5376401600AAE47CC
                :100BFA00AF48AA06AB078009AF4812198A7A00AB38
                :100C0A0007AD39AF38AE3712173DAB3AAA3BA93C0C
                :080C1A00E5478548F002039D47
                :100802008E378F388D398B3A8A3B893C74FFF54796
                :10081200F546F545F544120372F54D85F04CAB40B3
                :10082200AA41A942120372F54F85F04EE4F548F54C
                :1008320049C3E54995437480F86548984003020925
                :10084200B4E4F54AF54BC3E54B95437480F8654A29
                :100852009840030209A9E543C313FF7E00C3E5499B
                :100862009FFDE5489EFCE54D2DF551E54C3CF550CC
                :10087200C3E54B9FFFE54A9EFEE54F2FF553E54E3C
                :100882003EF552E538640E7004E5376401600AAE45
                :1008920050AF51AA06AB078009AF5112198A7A00EC
                :1008A200AB07AD39AF38AE3712173DE53E640E7077
                :1008B20004E53D6401600AAE52AF53AA06AB07805D
                :1008C20009AF5312198A7A00AB07AD3FAF3EAE3D76
                :1008D20012173D120F5BC004C005C006C007E54BEE
                :1008E200AE4A7802C333CE33CED8F9FBAA069000C3
                :1008F2000075F01CE549120500E54875F01CA425B9
                :1009020083F583E5822BF582E5833AF583D007D020
                :1009120006D005D0041204F490000075F01CE549DD
                :10092200120500E54875F01CA42583F583E5822BAA
                :10093200F582E5833AF5831204DCAB47AA46A94562
                :10094200A844D31204A54054AB3AAA3BA93CE550B3
                :100952008551F012039DAB40AA41A942E55285534D
                :10096200F012039DE54BAE4A7802C333CE33CED8A4
                :10097200F9FF90000075F01CE549120500E5487585
                :10098200F01CA42583F583E5822FF582E5833EF5ED
                :10099200831204DC8F478E468D458C44054BE54B14
                :1009A2007002054A0208480549E5497002054802F5
                :1009B2000833E538640E7004E5376401AB3AAA3BAC
                :1009C200A93C600A120372AEF0AA06FB800B120366
                :1009D20072FF12198A7A00AB07AD39AF38AE3712FF
                :1009E200173DE53E640E7004E53D6401AB40AA414B
                :1009F200A942600A120372AEF0AA06FB800B120330
                :100A020072FF12198A7A00AB07AD3FAF3EAE3D02CC
                :020A1200173D8E
                :1011DE00E4FBFA7D227F0C7E0412173DE4FBFA7DC0
                :1011EE00777F0C7E0412173DC200E4F53BAB0FAACD
                :1011FE000EA90DA80CAF14AE13AD12AC1112020451
                :10120E00E4FBFAF978401200FB121464120F5B8FA4
                :10121E00328E318D308C2F7D407F197E0112190157
                :10122E008F337D527F137E011219018F34E4FF7EBE
                :10123E00B0FDFCAB32AA31A930A82FC31204A550C1
                :10124E0070C3E5346480948F5067120F5B8F328EBB
                :10125E00318D308C2FE4FF7EB0FDFCAB32AA31A96C
                :10126E0030A82FC31204A550480534E534FB33953E
                :10127E00E0FA7D527F137E0112173D80B0C3E53335
                :10128E00648094925038E534640F7032FF7EB0FD66
                :10129E00FCAB32AA31A930A82FC31204A5501F05EA
                :1012AE0033E533FB3395E0FA7D407F197E0112174B
                :1012BE003D1218B68F328E318D308C2F80BF7B0150
                :1012CE007A007D777F0C7E0412173D7B017A007DBC
                :0812DE00227F0C7E0402173D83
                :1013AD00752F007530407531007532407B017A0024
                :1013BD00E4FDFF7E0112173DE4FBFA7D777F0C7E85
                :1013CD000412173DC200E4F53BAB0FAA0EA90DA800
                :1013DD000CAF14AE13AD12AC11120204121464E46E
                :1013ED00FBFA7D707F047E0212173D7B007A007937
                :1013FD002F753D077DF87F047E02120A1A7B007A55
                :10140D00007931753D077D707F047E02120A1A7BCB
                :10141D00007A00792F753D047DF87F047E02120A53
                :10142D001A7B007A007931753D047D707F047E0250
                :10143D00120A1A753D02753E04753F7075400075B0
                :10144D0041007542317543077B007A00792F7DF895
                :07145D007F047E0202080279
                :100C22007525077526BF7F2D7E001217B5AC06AD60
                :100C320007E41202A68F148E138D128C111211DE8C
                :100C4200E4FBFAFDFF7E0112173D12150C1213ADE3
                :100C52007B017A00E4FDFF7E0112173DE4FBFA7D81
                :100C6200887F087E0212173DC200E4F53B753F9A69
                :100C7200753E99753D79753C401214777BBF7A07B2
                :100C82007DA07402FFFE12173D7BFF7A077DA07FD5
                :100C9200017E0212173D120F5B8F2A8E298D288C3E
                :100CA200277BFF7A077DA07402FFFE12173D7BBFF0
                :100CB2007A077DA07F017E0212173D120F5B8F2EF5
                :100CC2008E2D8D2C8C2B7BFF7A077DA07402FFFE6C
                :100CD20012173D7BFF7A077DA07F017E0212173D2E
                :100CE200AF2EAE2DAD2CAC2BAB2AAA29A928A82752
                :100CF200C31204A57E0250047F0280027F018E216E
                :100D02008F227B007A007925753D077DA0120A1A91
                :100D12007B0F7A007DB07F037E0212173D120F5BBC
                :100D22008F2A8E298D288C277BF17AFF7DB07F0355
                :100D32007E0212173D120F5B8F2E8E2D8D2C8C2B67
                :100D4200AB2AAA29A928A827D31204A540057523EE
                :100D5200FF8019AF2EAE2DAD2CAC2BAB2AAA29A940
                :100D620028A827C31204A550087523007524C08043
                :100D7200067523007524407B007A007923753D07B0
                :100D82007DB07F037E02120A1A7B007A00792575F4
                :100D92003D047DA0AF22AE21120A1A753D02753EB6
                :100DA20003753FB0754000754100754223754307D6
                :100DB2007B007A0079257DA0AF22AE211208027F46
                :020DC20080228D
                :100DC4007DFA7F087E011219018E378F38E4FBFA11
                :100DD4007DDD7F0C7E0412173DE4FBFA7D777F0CEA
                :100DE4007E0412173DC200E4F53BAB0FAA0EA90D19
                :100DF400A80CAF14AE13AD12AC111202047BCD7A61
                :100E0400CC79CC78BD12146C120F5B8F368E358D75
                :100E1400348C337D527F137E011219018E398F3A3F
                :100E2400E4FF7EB0FDFCAB36AA35A934A833C31267
                :100E340004A5505AC3E53A940FE539648094805070
                :100E44004D1218B68F368E358D348C33E4FF7EB058
                :100E5400FDFCAB36AA35A934A833C31204A5500B44
                :100E64007402253AF53AE43539F539E4FF7EB0FDEC
                :100E7400FCAB36AA35A934A833D31204A5500FAB62
                :100E84003AAA397D527F137E0112173D8092E4FF06
                :100E94007E10FDFCAB36AA35A934A833C31204A5D1
                :100EA400505AC3E5389439E53764809480504D1224
                :100EB4000F5B8F368E358D348C33E4FF7E10FDFC52
                :100EC400AB36AA35A934A833C31204A5500B740455
                :100ED4002538F538E43537F537E4FF7E10FDFCABF3
                :100EE40036AA35A934A833D31204A5500FAB38AAB7
                :100EF400377DFA7F087E0112173D8092E4FF7EB0B1
                :100F0400FDFCAB36AA35A934A833C31204A5504658
                :100F1400C3E538943EE537648094805039120F5B02
                :100F24008F368E358D348C33E4FF7EB0FDFCAB36CA
                :100F3400AA35A934A833C31204A5500B740225386A
                :100F4400F538E43537F537AB38AA377DFA7F087EB4
                :070F54000112173D80A622E7
                :10050C00E4F521F522F525F5267D107F20FE121944
                :10051C00018F297D877F0D7E011219018F2AE52A13
                :10052C0064016004E52A70037F81227F2D7E001216
                :10053C0017B5AC06AD07E41202A68F148E138D12FC
                :10054C008C1112150C7B017A007DFE7F0C7E04123F
                :10055C00173D7B017A00E4FDFF7E0112173DE52A71
                :10056C00B40218E4FBFA7D557F0C7E0112173DE4B2
                :10057C00FBFA7D337F0D7E0112173DE52AB403187B
                :10058C00E4FBFA7D667F0C7E0112173DE4FBFA7DDD
                :10059C00447F0D7E0112173DE4FBFA7D227F0C7E19
                :1005AC000412173D7B027A007D107F207E0012170B
                :1005BC003D7D667F1C7E01121901EF4E70257B017B
                :1005CC00FA7D667F1C7E0112173D7B017A007D103F
                :1005DC007F207E0012173DE4FBFA7D117F1C7E010B
                :1005EC0012173DE529FB7A007D107F207E00121743
                :1005FC003D120DC47B017A007DDD7F0C7E04121749
                :10060C003DE4FBFA7D777F0C7E0412173DC200E4BB
                :10061C00F53BAB0FAA0EA90DA80CAF14AE13AD127F
                :10062C00AC111202047BCD7ACC79CC783D12146CCF
                :10063C00E4FBFA7DB07F037E0412173D7BFF7A0743
                :10064C007DA07F027E0412173D7BFF7A077DA07F81
                :10065C00017E0412173D7BBF7A077DA07F027E04CA
                :10066C0012173D7BFF7A077DA07F017E0412173D98
                :10067C001218B68F2E8E2D8D2C8C2B7BFF7A077D2E
                :10068C00A07F027E0412173D7BBF7A077DA07F01FD
                :10069C007E0412173D1218B68F328E318D308C2F8E
                :1006AC007BFF7A077DA07F027E0412173D7BFF7AC9
                :1006BC00077DA07F017E0412173D7523077524BFAB
                :1006CC00AF32AE31AD30AC2FAB2EAA2DA92CA82B4E
                :1006DC00C31204A55010752504752602AB24AA2359
                :1006EC007DA07F02800E752504752601AB24AA23FC
                :1006FC007DA07F017E0412173D7B007A0079237563
                :10070C003D077DA0AF26AE25120A1A7B0F7A007D1D
                :10071C00B07F037E0412173D1218B68F2E8E2D8DCE
                :10072C002C8C2B7BF17AFF7DB07F037E0412173D5E
                :10073C001218B68F328E318D308C2FAB2EAA2DA97C
                :10074C002CA82BD31204A540057527FF8019AF32B6
                :10075C00AE31AD30AC2FAB2EAA2DA92CA82BC312C9
                :10076C0004A550087527007528C0800675270075EC
                :10077C002840AB28AA277DB07F037E0412173D7B4F
                :10078C00007A007927753D077DB07F037E04120A3D
                :10079C001A7B007A007923753D047DA0AF26AE2527
                :1007AC00120A1A7B007A007927753D047DB07F030D
                :1007BC007E04120A1A753D04753E03753FB07540F0
                :1007CC00007541007542277543077B007A00792339
                :1007DC007DA0AF26AE25120802AB24AA237DA0AFC4
                :1007EC0026AE2512173DAB28AA277DB07F037E04C9
                :0607FC0012173D7F802270
                :10162E007581D0E4F5A27591FF75A107F5A9C2A049
                :10163E00D2A178FE7601759080858016858015E59D
                :10164E0015651660F7851516E51570028036E515D9
                :10165E00B4010A7590FF120C228F9080DFE515B44D
                :10166E00020A7590FF12050C8F9080D0E515B40319
                :10167E00087590FF120F5B800BE515B4040B759087
                :10168E00FF12181175908080B3E515B4050A759098
                :10169E00FF1219BC8F9080A4E515F4709F7590FF12
                :0916AE0078FEE64480F59080937B
                :101867008E668F679001457480F0A3E4F090014481
                :101877007410F0C2A0900145E0FEA3E0FFE5665EAC
                :10188700FCE5675F4C24FF92A2EEC313FEEF13FF44
                :10189700900145EEF0A3EFF01219FAD2A01219FA4F
                :0F18A700C2A0900144E014F0E0D3940050C52299
                :10193D008E5F8F608C618D62435F80C2A0C2A112E9
                :10194D0019FAAF60AE5F121867AF62AE6112186719
                :07195D00D2A1D2A20219FA87
                :1017B5008E5F8F60C2A0C2A1535F7F1219FAAF601E
                :1017C500AE5F121867D2A2E4F562F563756480F521
                :1017D500657561101219FAD2A030A308E565426358
                :1017E500E5644262E564C313F564E56513F56512C6
                :1017F50019FAC2A01561E561D3940050D71219FA00
                :0C180500D2A1D2A21219FAAE62AF632287
                :10173D008E5A8F5B8D5C8A5D8B5E1217B5AD07ACD3
                :10174D0006E55CC4540FFFE55C540FFBC3EF9B042F
                :10175D00FF74FFFEA807088005C333CE33CED8F93A
                :10176D00F4FFEEF4FEEFA803088005C333CE33CEAD
                :10177D00D8F9FBAA06E55C540FFFE55EAE5DA80740
                :10178D00088005C333CE33CED8F9FFEE5AFEEF5B9A
                :10179D00FFEBF4FBEAF45CFCEB5DFDEC4EFCED4F76
                :0817AD00FDAF5BAE5A02193DCD
                :101901008D5A1217B5AC06AD07E55AC4540F04FF42
                :1019110074FFFEA807088005C333CE33CED8F9F48F
                :10192100FFEEF45CFEED5FFFE55A540FFDEFA805F5
                :0C193100088005CEC313CE13D8F9FF22A6
                :1019FA0000000000000000000000000000000022BB
                :1000030002034BE86480F8E933E83360110460F0DD
                :10001300ED33EC337009E8FCE9FDEAFEEBFF220463
                :1000230060DED3EB9FEA9EE99DE8C2E78CF0C2F75E
                :1000330095F0400CE8CCF8E9CDF9EACEFAEBCFFB2A
                :1000430012031685D0F05804700320D5B3E804706A
                :10005300075002B2D502035592D5EC0460F7E4CC05
                :10006300C0E0C398F8603B94186008400DD0E0FBF3
                :1000730002032DE4FBFAC9FC8028E830E406E4C956
                :10008300FBE4CAFCE830E305E4C9CACBFCE8540747
                :100093006010F8C3E913F9EA13FAEB13FBEC13FC52
                :1000A300D8F130F52FC3E49CFCEF9BFFEE9AFEEDF5
                :1000B30099FDD0E0FBEF4E4D4C701222DB0302039F
                :1000C30052EC2CFCEF33FFEE33FEED33FDED30E766
                :1000D300EB02032DEF2BFFEE3AFEED39FDD0E0FBF3
                :1000E30050130BBB0003020355ED13FDEE13FEEF9C
                :0800F30013FFEC13FC02032DC6
                :1000FB00EC4D6011E8497017ED33EC3304600DE4FF
                :10010B00FCFFFEFD22E933E8330470F802034B12C7
                :10011B00031658046009E4CC2481500628500902C8
                :10012B000355284003020352C0E0EB4A7044B980E8
                :10013B0006D0E0FB020341EF4E701CBD8008EBFFC5
                :10014B00EAFEE9FD80EBE98DF0A4FEE5F00201E4A7
                :10015B00E9CDF9EAFEEBFFEF89F0A4FCE5F0CE89DF
                :10016B00F0A42EFFE435F0CD89F0A42DFEE435F09C
                :10017B008067EF4E7005BD80D780C3EF8BF0A4ACCA
                :10018B00F0EE8BF0A42CFCE435F0F8EF8AF0A42C05
                :10019B00E5F038FCE433CB8DF0A42CFCE5F03BF818
                :1001AB00EE8AF0A42CFCE5F038F8E433CF89F0A408
                :1001BB002CFCE5F038CF3400CE89F0A42FFFE5F00E
                :1001CB003EFEE433C98DF0A42EFEE5F039CD8AF066
                :1001DB00A42FFFE5F03EFEE43DFD33D0E0FB5007DE
                :1001EB000BBB000F020355EC2CFCEF33FFEE33FE81
                :0601FB00ED33FD02032DAF
                :10020100020355EC5D046005E85904700302034BD9
                :10021100120316580460F6EC4860F2EC7004FDFE1F
                :10022100FF22C860DB2481C85009C39860025006D0
                :100231000203529850CAF582E9294B4A7005AB82F4
                :1002410002034175F0007C1A7880C3EF9BEE9AEDB2
                :1002510099400DC3EF9BFFEE9AFEED99FDE842F048
                :10026100DC23ACF0D0E0FFD0E0FED0E0FDAB82209B
                :10027100E7101BEB60BAEC2CFCEF33FFEE33FEED25
                :1002810033FD02032DE803F830E705C0F075F000F7
                :10029100EF2FFFEE33FEED33FD40B830E7C280AA09
                :1002A10075F020800E75F010800575F0087D007ED8
                :1002B100007F003392D530D503120497EC33401000
                :1002C100EF33FFEE33FEED33FDEC33FCD5F0ED22E1
                :0E02D100E5F0247EA2D513CC92E7CDCEFF221D
                :1002DF00EDD2E7CD33EC3392D524814006E4FFFE17
                :1002EF00FDFC22FCE4CFCECDCC24E0501174FF8076
                :1002FF00EDC3CC13CCCD13CDCE13CECF13CF047013
                :07030F00F030D5DE02049777
                :10031600E9D2E7C933E833F892D5EDD2E7CD33EC2D
                :0703260033FC5002B2D522A6
                :10032D00EC30E7100FBF000C0EBE00080DBD000431
                :10033D000BEB6014A2D5EB13FCED92E7FD2274FFDD
                :10034D00FCFDFEFF22E480F8A2D574FF13FC7D8036
                :03035D00E480EF4A
                :030000000215A244
                :0C15A200787FE4F6D8FD7581FE0215E9A3
                :10036000EF8DF0A4A8F0CF8CF0A428CE8DF0A42EB1
                :02037000FE226B
                :10037200BB010A89828A83E0F5F0A3E02250068756
                :10038200F009E71922BBFE07E3F5F009E319228918
                :0B039200828A83E493F5F0740193224B
                :10039D00BB010A89828A83F0E5F0A3F0225006F7AB
                :0F03AD0009A7F01922BBFE06F3E5F009F31922A8
                :1003BC0075F008758200EF2FFFEE33FECD33CDCCF8
                :1003CC0033CCC58233C5829BED9AEC99E58298407B
                :1003DC000CF582EE9BFEED9AFDEC99FC0FD5F0D658
                :1003EC00E4CEFBE4CDFAE4CCF9A88222B800C1B982
                :1003FC000059BA002DEC8BF084CFCECDFCE5F0CBC0
                :10040C00F97818EF2FFFEE33FEED33FDEC33FCEBF8
                :10041C0033FB10D703994004EB99FB0FD8E5E4F9B3
                :10042C00FA227818EF2FFFEE33FEED33FDEC33FCA0
                :10043C00C933C910D7059BE99A4007EC9BFCE99A94
                :10044C00F90FD8E0E4C9FAE4CCFB2275F010EF2FD9
                :10045C00FFEE33FEED33FDCC33CCC833C810D707D9
                :10046C009BEC9AE899400AED9BFDEC9AFCE899F814
                :0E047C000FD5F0DAE4CDFBE4CCFAE4C8F922A7
                :0D048A00EF4BFFEE4AFEED49FDEC48FC2271
                :0E049700C3E49FFFE49EFEE49DFDE49CFC2276
                :1004A500EB9FF5F0EA9E42F0E99D42F0E89C45F0AD
                :0104B5002224
                :1004B600E8600FECC313FCED13FDEE13FEEF13FF24
                :0304C600D8F12248
                :1004C900E8600FEFC333FFEE33FEED33FDEC33FC91
                :0304D900D8F12235
                :0C04DC00E0FCA3E0FDA3E0FEA3E0FF2293
                :0C04E800ECF608EDF608EEF608EFF62240
                :0C04F400ECF0A3EDF0A3EEF0A3EFF0227B
                :0C050000A42582F582E5F03583F5832206
                :1015AE0002162EE493A3F8E493A34003F68001F20F
                :1015BE0008DFF48029E493A3F85407240CC8C3333E
                :1015CE00C4540F4420C8834004F456800146F6DF0D
                :1015DE00E4800B01020408102040809019D4E47EB0
                :1015EE00019360BCA3FF543F30E509541FFEE49302
                :1015FE00A360010ECF54C025E060A840B8E493A3C9
                :10160E00FAE493A3F8E493A3C8C582C8CAC583CAF3
                :10161E00F0A3C8C582C8CAC583CADFE9DEE780BEAB
                :0119E90000FD
                :00000001FF"""
