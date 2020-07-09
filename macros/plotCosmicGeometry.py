import ROOT as r
from ROOT import gROOT
import include.Canvas as Canvas

_file = r.TFile("/eos/user/f/fernance/Cosmics/SmallVolume/GENSIM/gencosmic_NTuples.root")
_tree = _file.Get("Events")

gROOT.ProcessLine('.L include/tdrstyle.C')
gROOT.SetBatch(1)
r.setTDRStyle()

yvsz_slice = r.TMultiGraph()
CMS3Dpointmap = r.TGraph2D()
CMS3Dpointmap.SetMarkerStyle(24)
CMS3Dpointmap.SetMarkerColor(r.kAzure-7)
CMSXYmap = r.TGraph()
CMSXYmap.SetMarkerStyle(24)
CMSXYmap.SetMarkerColor(r.kAzure-7)

for _e,ev in enumerate(_tree):

    if _e > 1000: break

    # Look for the status = 1 generated muon
    m1 = 0
    for m in range(_tree.nM):
        if _tree.Muon_status[m] == 1:
            m1 = m
            break

    x1 = ev.Muon_vx[m1]/100.0
    z1 = ev.Muon_vz[m1]/100.0
    y1 = ev.Muon_vy[m1]/100.0
    y2 = -9.0
    z2 = abs(y2 - y1)/abs(ev.Muon_py[m1])*ev.Muon_pz[m1] + z1

    muon_gr = r.TGraph()
    muon_gr.SetPoint(0, z1, y1)
    muon_gr.SetPoint(1, z2, y2)
    muon_gr.SetMarkerStyle(20)
    muon_gr.SetMarkerSize(0.5)
    muon_gr.SetMarkerColor(r.kAzure-7)
    muon_gr.SetLineColor(r.kAzure-7)
    yvsz_slice.Add(muon_gr)
    

    CMS3Dpointmap.SetPoint(_e, z1, x1, y1)
    CMSXYmap.SetPoint(_e, x1, y1)

### Tracker slice
tr_r = 1.1
tr_z = 2.8
tr_yzslice = r.TGraph()
tr_yzslice.SetLineColor(r.kRed+2)
tr_yzslice.SetLineWidth(2)
tr_yzslice.SetPoint(0, -tr_z/2.0, tr_r/2.0)
tr_yzslice.SetPoint(1, tr_z/2.0, tr_r/2.0)
tr_yzslice.SetPoint(2, tr_z/2.0, -tr_r/2.0)
tr_yzslice.SetPoint(3, -tr_z/2.0, -tr_r/2.0)
tr_yzslice.SetPoint(4, -tr_z/2.0, tr_r/2.0)


### CMS slice
CMS_xyslice = r.TEllipse(0.0, 0.0, 7.5, 7.5)
CMS_xyslice.SetFillColor(0)
CMS_xyslice.SetLineColor(r.kRed+2)
CMS_xyslice.SetLineWidth(2)


c1 = r.TCanvas("c1", "", 800, 600)
yvsz_slice.Draw("APL")
yvsz_slice.GetXaxis().SetLimits(-15.0, 15.0)
yvsz_slice.SetMinimum(-9.0)
yvsz_slice.SetMaximum(9.0)
yvsz_slice.GetXaxis().SetTitle("CMS detector z axis (m)")
yvsz_slice.GetYaxis().SetTitle("CMS detector y axis (m)")
tr_yzslice.Draw('L,same')
c1.Update()
c1.SaveAs('yvsz.png')
c1.SaveAs('yvsz.pdf')


c2 = r.TCanvas("c2", "", 800, 600)
h3 = r.TH3F("dummyh3", ";CMS detector z axis (m);CMS detector x axis (m);CMS detector y axis (m)", 30, -15, 15, 18, -9, 9, 18, -9, 9)
h3.GetXaxis().SetTitleSize(0.04)
h3.GetXaxis().SetTitleOffset(1.7)
h3.GetYaxis().SetTitleSize(0.04)
h3.GetYaxis().SetTitleOffset(1.7)
h3.GetZaxis().SetTitleSize(0.04)
h3.GetZaxis().SetTitleOffset(1.2)
h3.Draw()
CMS3Dpointmap.Draw("P,SAME")
c2.SaveAs("CMS3Dmappoint.png")
c2.SaveAs("CMS3Dmappoint.pdf")


c3 = r.TCanvas("c2", "", 600, 600)
h2 = r.TH2F("dummyh2", ";CMS detector x axis (m);CMS detector y axis (m)", 18, -9, 9, 18, -9, 9)
h2.Draw()
CMS_xyslice.Draw("L,SAME")
CMSXYmap.Draw("P,SAME")
c3.SaveAs("CMSXYmap.png")
c3.SaveAs("CMSXYmap.pdf")






