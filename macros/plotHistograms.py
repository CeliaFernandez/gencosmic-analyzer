import ROOT as r
from ROOT import gROOT
import optparse
import copy
import include.Canvas as Canvas


def plotSelection(histoList, name, log = False, xlabel = '', normed = False):

    plot = Canvas.Canvas(name, 'png', 0.15, 0.77, 0.9, 0.88, 1)

    sel = []
    ymax = 0.0
    for histo in histoList:
        _f = r.TFile(histo[0])
        aux_h = copy.deepcopy(_f.Get(histo[1]))
        if normed: aux_h.Scale(1/aux_h.Integral())
        if aux_h.GetMaximum() > ymax: ymax = aux_h.GetMaximum()


    for h,histo in enumerate(histoList):
        _f = r.TFile(histo[0])
        _h = copy.deepcopy(_f.Get(histo[1]))
        _f.Close()
        _h.GetXaxis().SetTitle(xlabel)

        if normed: 
            _h.Scale(1/_h.Integral())
            _h.GetYaxis().SetTitle('Event density')
        else:
            _h.GetYaxis().SetTitle('Events')

        if log: _h.SetMaximum(10.0*ymax)
        else: _h.SetMaximum(1.3*ymax)

        option = 'HIST'
        if h != 0: option = 'HIST, SAME'

        plot.addHisto(_h, option, histo[3], 'l', histo[2], 1, h)        

    plot.save(1, 0, log, '', '', outputDir = 'plots')


if __name__=='__main__':


    #########################
    ###   Parser object   ###   
    #########################
    """
    parser = optparse.OptionParser(usage='usage: %prog [opts] FilenameWithSamples', version='%prog 1.0')
    parser.add_option('-i', '--input', action='store', type=str, dest='inputFile', default='launchWithGridui/merged.root', help='the input file. default \'merged.root\'')
    parser.add_option('-t', '--tag', action='store', type=str, dest='tag', default='launchWithGridui/merged.root', help='the input file. default \'merged.root\'')
    (opts, args) = parser.parse_args()
    """

    ############# Set the TDR plot style
    gROOT.ProcessLine('.L ' +'include/tdrstyle.C')
    gROOT.SetBatch(1)
    r.setTDRStyle()


    ###########################
    ###   Drawing objects   ###   
    ###########################
    
    """ format: [file, name, color, label] """
    dummy = []
    dummy.append( ['outHist_400_150_400.root', '400_150_400_h_LLP_Lxy', r.kBlue+-4, 'm_{H} = 400 GeV, m_{X} = 150 GeV, c#tau = 40 cm'] )
    plotSelection(dummy, name = 'dummy', log = True, xlabel = 'Gen X decay length (cm)', normed = True)


    LxyPlot = []
    LxyPlot.append( ['outHist_400_150_400.root', '400_150_400_h_LLP_Lxy', r.kBlue+-4, 'm_{H} = 400 GeV, m_{X} = 150 GeV, c#tau = 40 cm'] )
    LxyPlot.append( ['outHist_400_150_40.root', '400_150_40_h_LLP_Lxy', r.kBlue-9, 'm_{H} = 400 GeV, m_{X} = 150 GeV, c#tau = 4 cm'] )
    LxyPlot.append( ['outHist_1000_150_100.root', '1000_150_100_h_LLP_Lxy', r.kRed+1, 'm_{H} = 1000 GeV, m_{X} = 150 GeV, c#tau = 10 cm'] )
    LxyPlot.append( ['outHist_1000_150_10.root', '1000_150_10_h_LLP_Lxy', r.kRed-7, 'm_{H} = 1000 GeV, m_{X} = 150 GeV, c#tau = 1 cm'] )
    plotSelection(LxyPlot, name = 'X_decayLength', log = True, xlabel = 'Gen X decay length (cm)', normed = True)


    dxyPlot = []
    dxyPlot.append( ['outHist_400_150_400.root', '400_150_400_h_lep_dxy', r.kBlue+-4, 'm_{H} = 400 GeV, m_{X} = 150 GeV, c#tau = 40 cm'] )
    dxyPlot.append( ['outHist_400_150_40.root', '400_150_40_h_lep_dxy', r.kBlue-9, 'm_{H} = 400 GeV, m_{X} = 150 GeV, c#tau = 4 cm'] )
    dxyPlot.append( ['outHist_1000_150_100.root', '1000_150_100_h_lep_dxy', r.kRed+1, 'm_{H} = 1000 GeV, m_{X} = 150 GeV, c#tau = 10 cm'] )
    dxyPlot.append( ['outHist_1000_150_10.root', '1000_150_10_h_lep_dxy', r.kRed-7, 'm_{H} = 1000 GeV, m_{X} = 150 GeV, c#tau = 1 cm'] )
    plotSelection(dxyPlot, name = 'lep_dxy', log = True, xlabel = 'Gen lepton d_{xy} (cm)', normed = True)

    ptPlot = []
    ptPlot.append( ['outHist_400_150_400.root', '400_150_400_h_lep_pt', r.kBlue+-4, 'm_{H} = 400 GeV, m_{X} = 150 GeV, c#tau = 40 cm'] )
    ptPlot.append( ['outHist_400_150_40.root', '400_150_40_h_lep_pt', r.kBlue-9, 'm_{H} = 400 GeV, m_{X} = 150 GeV, c#tau = 4 cm'] )
    ptPlot.append( ['outHist_1000_150_100.root', '1000_150_100_h_lep_pt', r.kRed+1, 'm_{H} = 1000 GeV, m_{X} = 150 GeV, c#tau = 10 cm'] )
    ptPlot.append( ['outHist_1000_150_10.root', '1000_150_10_h_lep_pt', r.kRed-7, 'm_{H} = 1000 GeV, m_{X} = 150 GeV, c#tau = 1 cm'] )
    plotSelection(ptPlot, name = 'lep_pt', log = False, xlabel = 'Gen lepton p_{T} (cm)', normed = True)

    etaPlot = []
    etaPlot.append( ['outHist_400_150_400.root', '400_150_400_h_lep_eta', r.kBlue+-4, 'm_{H} = 400 GeV, m_{X} = 150 GeV, c#tau = 40 cm'] )
    etaPlot.append( ['outHist_400_150_40.root', '400_150_40_h_lep_eta', r.kBlue-9, 'm_{H} = 400 GeV, m_{X} = 150 GeV, c#tau = 4 cm'] )
    etaPlot.append( ['outHist_1000_150_100.root', '1000_150_100_h_lep_eta', r.kRed+1, 'm_{H} = 1000 GeV, m_{X} = 150 GeV, c#tau = 10 cm'] )
    etaPlot.append( ['outHist_1000_150_10.root', '1000_150_10_h_lep_eta', r.kRed-7, 'm_{H} = 1000 GeV, m_{X} = 150 GeV, c#tau = 1 cm'] )
    plotSelection(etaPlot, name = 'lep_eta', log = False, xlabel = 'Gen lepton #eta (cm)', normed = True)
