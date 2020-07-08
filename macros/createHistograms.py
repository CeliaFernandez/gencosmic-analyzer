import ROOT as r
from ROOT import gROOT
import optparse

class Histo:

    def __init__(self, variables, key, xlabel, bins, color):

        self.variables = variables

        self.histo = r.TH1F(key, '', bins[0], bins[1], bins[2])
        self.histo.GetXaxis().SetTitle(xlabel)
        self.histo.SetLineColor(color)
        self.histo.SetLineWidth(2)
        


if __name__=='__main__':


    #########################
    ###   Parser object   ###   
    #########################
    parser = optparse.OptionParser(usage='usage: %prog [opts] FilenameWithSamples', version='%prog 1.0')
    parser.add_option('-i', '--input', action='store', type=str, dest='inputFile', default='launchWithGridui/merged.root', help='the input file. default \'merged.root\'')
    parser.add_option('-t', '--tag', action='store', type=str, dest='tag', default='launchWithGridui/merged.root', help='the input file. default \'merged.root\'')
    (opts, args) = parser.parse_args()

    ############# Set the TDR plot style
    gROOT.ProcessLine('.L ' +'include/tdrstyle.C')
    gROOT.SetBatch(1)
    r.setTDRStyle()


    #################################
    ###   Get the file and tree   ###   
    #################################
    _input = r.TFile(opts.inputFile)
    _tree = _input.Get('Events')


    #################################
    ###   Initialize histograms   ###   
    #################################
    Lxy_bins = [40, 0, 200]
    dxy_bins = [40, 0, 100]
    pt_bins = [40, 0, 400]
    eta_bins = [40, -4, 4]

    histos = {}
    histos['h_LLP_Lxy'] = Histo(['LLP1_Lxy', 'LLP2_Lxy'], opts.tag + '_h_LLP_Lxy', 'Gen X L_{xy} (cm)', Lxy_bins, r.kRed) 
    histos['h_dxy_Lxy'] = Histo(['lep11_dxy', 'lep12_dxy', 'lep21_dxy', 'lep22_dxy'], opts.tag + '_h_lep_dxy', 'Gen lepton d_{xy} (cm)', dxy_bins, r.kRed) 
    histos['h_pt_Lxy'] = Histo(['lep11_pt', 'lep12_pt', 'lep21_pt', 'lep22_pt'], opts.tag + '_h_lep_pt', 'Gen lepton p_{T} (cm)', pt_bins, r.kRed) 
    histos['h_eta_Lxy'] = Histo(['lep11_eta', 'lep12_eta', 'lep21_eta', 'lep22_eta'], opts.tag + '_h_lep_eta', 'Gen lepton #eta (cm)', eta_bins, r.kRed) 

 
    ################################
    ###   Loop over the events   ###   
    ################################

    for _e, event in enumerate(_tree):

       for hname in histos.keys():
           for var in histos[hname].variables:
               value = eval('event.'+var)
               histos[hname].histo.Fill(value)


    ###########################
    ###   Save histograms   ###   
    ###########################
    _out = r.TFile('outHist_'+opts.tag + '.root', 'RECREATE')
    _out.cd()

    for hname in histos.keys():
        histos[hname].histo.Write()

    _out.Close()
    _input.Close()


