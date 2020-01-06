import shapefile

class SumurBandung:

    def __init__(self):
        self.kelurahan = shapefile.Writer(
            'kelurahan_sumur_bandung', shapeType=shapefile.POLYGON)
        self.kelurahan.shapeType
        self.kelurahan.field('kelurahan_di_sumur_bandung', 'C')

        self.kantor = shapefile.Writer(
            'kantor_kelurahan_sumur_bandung', shapeType=shapefile.POINT)
        self.kantor.shapeType
        self.kantor.field('kantor_kelurahan_di_sumur_bandung', 'C')

        self.jalan = shapefile.Writer(
            'jalan_sumur_bandung', shapeType=shapefile.POLYLINE)
        self.jalan.shapeType
        self.jalan.field('jalan_di_sumur_bandung', 'C')

    # Kelurahan
    def kelurahanBabakanCiamis(self, nama):
        self.kelurahan.record(nama)
        self.kelurahan.poly([[
            [107.6044177,-6.9070643],
            [107.60401,-6.9126454],
            [107.6046966,-6.9126667],
            [107.6045035,-6.9143708],
            [107.6137732,-6.9158832],
            [107.6140307,-6.9146478],
            [107.6132582,-6.9132205],
            [107.6130008,-6.9131992],
            [107.6130437,-6.9128158],
            [107.6130222,-6.912475],
            [107.6125716,-6.9112395],
            [107.6125072,-6.9098975],
            [107.6123356,-6.9096845],
            [107.6105975,-6.9097697],
            [107.610619,-6.9090667],
            [107.6105546,-6.9069578],
            [107.6078295,-6.9064253],
            [107.6074432,-6.9077034],
            [107.6061343,-6.9070643],
            [107.6044177,-6.9070643],
        ]])

    def kelurahanBraga(self, nama):
        self.kelurahan.record(nama)
        self.kelurahan.poly([[
            [107.6045035,-6.9143708],
            [107.6042353,-6.9207186],
            [107.6119601,-6.9217198],
            [107.6124965,-6.9179921],
            [107.613269,-6.917779],
            [107.6137732,-6.9158832],
            [107.6045035,-6.9143708],
        ]])

    def kelurahanKebonPisang(self, nama):
        self.kelurahan.record(nama)
        self.kelurahan.poly([[
            [107.6137732,-6.9158832],
            [107.613269,-6.917779],
            [107.6124965,-6.9179921],
            [107.6119601,-6.9217198],
            [107.6175391,-6.9224227],
            [107.6247274,-6.9185033],
            [107.6137732,-6.9158832],
        ]])

    def kelurahanMerdeka(self, nama):
        self.kelurahan.record(nama)
        self.kelurahan.poly([[
            [107.6123356,-6.9096845],
            [107.6125072,-6.9098975],
            [107.6125716,-6.9112395],
            [107.6130222,-6.912475],
            [107.6130008,-6.9131992],
            [107.6132582,-6.9132205],
            [107.6140307,-6.9146478],
            [107.6137732,-6.9158832],
            [107.6247274,-6.9185033],
            [107.6301132,-6.9157341],
            [107.6290618,-6.9132844],
            [107.627195,-6.9112182],
            [107.626959,-6.9112182],
            [107.6259719,-6.9102596],
            [107.6211869,-6.9091945],
            [107.6210796,-6.9094075],
            [107.618848,-6.908811],
            [107.6138483,-6.9103235],
            [107.6123356,-6.9096845],
        ]])


    # Kantor Kelurahan
    def kantorKelurahanBabakanCiamis(self, nama):
        self.kantor.record(nama)
        self.kantor.point(107.6056471, -6.9126961)

    def kantorKelurahanBraga(self, nama):
        self.kantor.record(nama)
        self.kantor.point(107.6130535, -6.9158274)

    def kantorKelurahanKebonPisang(self, nama):
        self.kantor.record(nama)
        self.kantor.point(107.6188516, -6.9187593)

    def kantorKelurahanMerdeka(self, nama):
        self.kantor.record(nama)
        self.kantor.point(107.6232184, -6.9122072)

    # Jalan
    def jalanBraga(self, nama):
        self.jalan.record(nama)
        self.jalan.line([[
            [107.6078295,-6.9064253],
            [107.6075827,-6.9078525],
            [107.6090418,-6.9104513],
            [107.6091062,-6.9162879],
            [107.6099216,-6.9197388],
            [107.6097928,-6.9214003],
        ]])

    def jalanMerdeka(self, nama):
        self.jalan.record(nama)
        self.jalan.line([[
            [107.6106031,-6.9100583],
            [107.6100773,-6.9164914],    
        ]])

    def jalanLembong(self, nama):
        self.jalan.record(nama)
        self.jalan.line([[
            [107.609101,-6.9161186],
            [107.6100773,-6.9164914],
            [107.6127381,-6.9179825],   
        ]])

    def jalanVeteran(self, nama):
        self.jalan.record(nama)
        self.jalan.line([[
            [107.6127381,-6.9179825],
            [107.6194543,-6.9213677],  
        ]])

    def jalanSunda(self, nama):
        self.jalan.record(nama)
        self.jalan.line([[
            [107.6175391,-6.9224227],
            [107.6181454,-6.916887],
        ]])

    def jalanSumbawa(self, nama):
        self.jalan.record(nama)
        self.jalan.line([[
            [107.6181454,-6.916887],
            [107.6184566,-6.9157473],
            [107.6162142,-6.9116042],
            [107.6155383,-6.9098255],
        ]])

    def jalanAceh(self, nama):
        self.jalan.record(nama)
        self.jalan.line([[
            [107.6123356,-6.9096845],
            [107.6106093,-6.9098565],
            [107.6093325,-6.9103039],
            [107.60797,-6.9104636],
            [107.6062963,-6.9102506],
            [107.6056526,-6.910453],
            [107.6053414,-6.9098352],
            [107.6051805,-6.9097287],
            [107.6052556,-6.9092814],
            [107.6042364,-6.9093027],
        ]])

    def jalanBabakanCiamis(self, nama):
        self.jalan.record(nama)
        self.jalan.line([[
            [107.6072123,-6.9075933],
            [107.606987,-6.9079235],
            [107.6066758,-6.9079021],
            [107.6067831,-6.9099365],
            [107.6064934,-6.9110335],
            [107.6078882,-6.9119388],
            [107.6081457,-6.9125033],
            [107.6079311,-6.9126631],
            [107.6076414,-6.9131637],
            [107.6080491,-6.9139945],
        ]])

    def jalanKBJukut(self, nama):
        self.jalan.record(nama)
        self.jalan.line([[
            [107.6044764,-6.9144631],
            [107.6067831,-6.9148039],
            [107.607105,-6.9143779],
            [107.6080491,-6.9139945],
            [107.6089289,-6.9138134],
            [107.6099803,-6.9139732],
            [107.6103022,-6.9137388],
        ]])

    def jalanGangHRapli(self, nama):
        self.jalan.record(nama)
        self.jalan.line([[
            [107.6053803,-6.9118249],
            [107.6057009,-6.9118648],
            [107.6057169,-6.911769],
            [107.6061381,-6.9118009],
        ]])

    def jalanKebonSirih(self, nama):
        self.jalan.record(nama)
        self.jalan.line([[
            [107.6057384,-6.9104283],
            [107.6061568,-6.9113762],
            [107.6060817,-6.9123455],
            [107.6053736,-6.9123934],
            [107.6053307,-6.9120952],
            [107.6054273,-6.9119833],
            [107.6055775,-6.9103378],
        ]])

    def jalanJalan(self, nama):
        self.jalan.record(nama)
        self.jalan.line([[
            [107.6046719,-6.912729],
            [107.6052995,-6.912729],
            [107.6053736,-6.9123934],
        ]])

    def jalanLabas(self, nama):
        self.jalan.record(nama)
        self.jalan.line([[
            [107.6040496,-6.9119409],
            [107.6046021,-6.9120474],
            [107.6053307,-6.9120952],
        ]])

    def jalanPurnawarman(self, nama):
        self.jalan.record(nama)
        self.jalan.line([[
            [107.6082743,-6.9090873],
            [107.6085881,-6.9091379],
            [107.6093069,-6.9090926],
            [107.6093391,-6.9067174],
        ]])

    def jalanSegitiga(self, nama):
        self.jalan.record(nama)
        self.jalan.line([[
            [107.6078762,-6.9083836],
            [107.6080827,-6.9083024],
            [107.608351,-6.9076501],
            [107.6081646,-6.9075915],
            [107.6080211,-6.9074903],
            [107.6076643,-6.9073691],
        ]])

    def jalanSukamulya(self, nama):
        self.jalan.record(nama)
        self.jalan.line([[
            [107.6090667,-6.9126461],
            [107.6094315,-6.9126647],
            [107.6094369,-6.9118845],
            [107.6094932,-6.9118126],
            [107.6094664,-6.9114292],
            [107.6096139,-6.9113653],
            [107.609917,-6.9113839],
            [107.6100994,-6.9114825],
            [107.6100457,-6.9127286],
            [107.6103783,-6.9127659],
        ]])

    def jalanTembus(self, nama):
        self.jalan.record(nama)
        self.jalan.line([[
            [107.6075741,-6.9117305],
            [107.6078718,-6.9112885],
            [107.6080569,-6.9111181],
            [107.608014,-6.9106308],
            [107.6079255,-6.9104577],
        ]])

    def jalanKenari(self, nama):
        self.jalan.record(nama)
        self.jalan.line([[
            [107.6115964,-6.9097521],
            [107.6116286,-6.9115095],
            [107.6104806,-6.9114136],
        ]])

    def jalanJawa(self, nama):
        self.jalan.record(nama)
        self.jalan.line([[
            [107.6102553,-6.9141602],
            [107.6106415,-6.9144904],
            [107.6185058,-6.9159176],
            [107.6188384,-6.915875],
        ]])

    def jalanKalimantan(self, nama):
        self.jalan.record(nama)
        self.jalan.line([[
            [107.6138483,-6.9103235],
            [107.6156626,-6.9144371],
            [107.6155124,-6.9153957],
        ]])

    def jalanBelitung(self, nama):
        self.jalan.record(nama)
        self.jalan.line([[
            [107.6130126,-6.9125413],
            [107.6132915,-6.9126052],
            [107.6164351,-6.9116253],
            [107.6184736,-6.9114443],
            [107.6200507,-6.9119022],
        ]])

    def jalanBanda(self, nama):
        self.jalan.record(nama)
        self.jalan.line([[
            [107.6173899,-6.9092554],
            [107.6176044,-6.9101075],
            [107.6176044,-6.9118862],
            [107.6178941,-6.9131004],
        ]]) 

    def jalanLombok(self, nama):
        self.jalan.record(nama)
        self.jalan.line([[
            [107.6172826,-6.913569],
            [107.6178941,-6.9131004],
            [107.618216,-6.9128128],
            [107.6183554,-6.9114495],
            [107.6184736,-6.9114443],
            [107.6190421,-6.908872],
        ]])

    def jalanBawean(self, nama):
        self.jalan.record(nama)
        self.jalan.line([[
            [107.6175508,-6.9099371],
            [107.6183233,-6.9098625],
            [107.6187631,-6.9099584],
        ]])

    def jalanBangka(self, nama):
        self.jalan.record(nama)
        self.jalan.line([[
            [107.6184736,-6.9114443],
            [107.6188275,-6.9129406],
            [107.6188384,-6.915875],
            [107.618967,-6.9168282],
        ]])

    def jalanGudangSelatan(self, nama):
        self.jalan.record(nama)
        self.jalan.line([[
            [107.618967,-6.9168282],
            [107.6250073,-6.9183512],
        ]])

    def jalanBali(self, nama):
        self.jalan.record(nama)
        self.jalan.line([[
            [107.6157111,-6.9118682],
            [107.6165908,-6.9138279],
            [107.6171273,-6.9143285],
            [107.6169556,-6.9156279],
        ]])

    def jalanGudangUtara(self, nama):
        self.jalan.record(nama)
        self.jalan.line([[
            [107.6188224,-6.9151273],
            [107.6196485,-6.9152871],
            [107.6198095,-6.9152445],
            [107.6273304,-6.9171723],
        ]])

    def jalanGandapura(self, nama):
        self.jalan.record(nama)
        self.jalan.line([[
            [107.6252275,-6.9182373],
            [107.626959,-6.9112182],
        ]])

    def jalanTongkeng(self, nama):
        self.jalan.record(nama)
        self.jalan.line([[
            [107.6221484,-6.9158196],
            [107.6237577,-6.9097806],
        ]])

    def jalanMenado(self, nama):
        self.jalan.record(nama)
        self.jalan.line([[
            [107.6196485,-6.9152871],
            [107.6203245,-6.9126031],
            [107.6200507,-6.9119022],
            [107.6205283,-6.9114208],
            [107.6206463,-6.9113995],
            [107.6210796,-6.9094075],
        ]])

    def jalanErmawar(self, nama):
        self.jalan.record(nama)
        self.jalan.line([[
            [107.6228994,-6.9128906],
            [107.6213652,-6.9125605],
            [107.6212901,-6.9128161],
            [107.6203245,-6.9126031],
        ]])

    def jalanPotrakomala(self, nama):
        self.jalan.record(nama)
        self.jalan.line([[
            [107.6206463,-6.9113995],
            [107.6215261,-6.9116125],
            [107.6216012,-6.9119001],
            [107.6276415,-6.9134019],
        ]])

    def jalanAnggrek(self, nama):
        self.jalan.record(nama)
        self.jalan.line([[
            [107.6285642,-6.9127202],
            [107.6276415,-6.9134019],
            [107.6268691,-6.9140303],
            [107.6265686,-6.9157557],
        ]])

    def jalanKamuning(self, nama):
        self.jalan.record(nama)
        self.jalan.line([[
            [107.6266652,-6.9131569],
            [107.6280814,-6.9157451],
            [107.6284569,-6.9165545],
        ]])

    def jalanSoka(self, nama):
        self.jalan.record(nama)
        self.jalan.line([[
            [107.6297015,-6.9148397],
            [107.6271695,-6.9161604],
            [107.6265686,-6.9157557],
            [107.6258927,-6.9155747],
        ]])

    def jalanDahlia(self, nama):
        self.jalan.record(nama)
        self.jalan.line([[
            [107.6266966,-6.9122756],
            [107.6275388,-6.9125952],
            [107.6279787,-6.9131543],
        ]])

    def jalanPudak(self, nama):
        self.jalan.record(nama)
        self.jalan.line([[
            [107.6277748,-6.9132875],
            [107.6288209,-6.9153005],
        ]])

    def jalanCulan(self, nama):
        self.jalan.record(nama)
        self.jalan.line([[
            [107.6267288,-6.9148585],
            [107.6271204,-6.914917],
            [107.6275066,-6.9159715],
        ]])

    def jalanTongkeng2(self, nama):
        self.jalan.record(nama)
        self.jalan.line([[
            [107.6233143,-6.9114139],
            [107.6239634,-6.912487],
        ]])

    def jalanPutraKomalaDalam(self, nama):
        self.jalan.record(nama)
        self.jalan.line([[
            [107.6258195,-6.9127879],
            [107.6259992,-6.9119438],
            [107.6250497,-6.9116909],
            [107.6251704,-6.9111823],
            [107.6242182,-6.9109426],
            [107.6239768,-6.9117521],
            [107.6236308,-6.9119305],
        ]])

    def jalanSumarsana(self, nama):
        self.jalan.record(nama)
        self.jalan.line([[
            [107.6237181,-6.9124241],
            [107.6240721,-6.9133082],
            [107.6255849,-6.9135957],
            [107.6258195,-6.9127879],
        ]])

    def jalanSrigading(self, nama):
        self.jalan.record(nama)
        self.jalan.line([[
            [107.6226422,-6.9159681],
            [107.6232216,-6.9135929],
            [107.6227495,-6.9134651],
        ]])

    def jalanSumarsono(self, nama):
        self.jalan.record(nama)
        self.jalan.line([[
            [107.6244524,-6.9164371],
            [107.624785,-6.9148128],
            [107.6243343,-6.9147063],
            [107.6244524,-6.914275],
            [107.624742,-6.9142537],
            [107.6248601,-6.9136785],
            [107.6255574,-6.9138543],
            [107.6255849,-6.9135957],
        ]])

    def jalanVijayaKusuma(self, nama):
        self.jalan.record(nama)
        self.jalan.line([[
            [107.6188189,-6.9129047],
            [107.6201573,-6.9132508],
        ]])

    def jalanAyamPenyet(self, nama):
        self.jalan.record(nama)
        self.jalan.line([[
            [107.6217131,-6.917513],
            [107.6220377,-6.9161391],
            [107.6221262,-6.9161178],
            [107.6222657,-6.9158834],
        ]])

    def jalanBaranangSiang(self, nama):
        self.jalan.record(nama)
        self.jalan.line([[
            [107.6218682,-6.9200506],
            [107.621482,-6.9193903],
            [107.6179575,-6.9185968],
        ]])

    def jalanKartini(self, nama):
        self.jalan.record(nama)
        self.jalan.line([[
            [107.6179575,-6.9185968],
            [107.6166433,-6.918469],
            [107.6154631,-6.9180217],
            [107.615168,-6.9172761],
            [107.6151305,-6.9166105],
        ]])

    def jalanNatuna(self, nama):
        self.jalan.record(nama)
        self.jalan.line([[
            [107.6181078,-6.9172708],
            [107.6162409,-6.9168075],
            [107.6161283,-6.9168448],
            [107.6151305,-6.9166105],
            [107.6146209,-6.9163761],
            [107.6136821,-6.9162537],
        ]])

    def jalanRakata(self, nama):
        self.jalan.record(nama)
        self.jalan.line([[
            [107.6138134,-6.9156334],
            [107.6182068,-6.9166718],
        ]])

    def jalanButon(self, nama):
        self.jalan.record(nama)
        self.jalan.line([[
            [107.6148112,-6.9164477],
            [107.6149024,-6.9181092],
            [107.6152511,-6.9185139],
            [107.6155783,-6.9186311],
            [107.6157715,-6.9184607],
            [107.6157876,-6.9181305],
        ]])

    def jalanVanDeventer(self, nama):
        self.jalan.record(nama)
        self.jalan.line([[
            [107.6138702,-6.9185256],
            [107.6161283,-6.9168448],
        ]])

    def jalanCibunutDalam(self, nama):
        self.jalan.record(nama)
        self.jalan.line([[
            [107.6142135,-6.9182753],
            [107.6140204,-6.9180091],
            [107.6142189,-6.9170612],
            [107.6148358,-6.9170132],
        ]])

    def jalanPanaitan(self, nama):
        self.jalan.record(nama)
        self.jalan.line([[
            [107.6178184,-6.919628],
            [107.6168957,-6.9192978],
            [107.6172283,-6.9170399],
        ]])

    def jalanCibunut(self, nama):
        self.jalan.record(nama)
        self.jalan.line([[
            [107.6178184,-6.9197451],
            [107.6189342,-6.920054],
            [107.6189664,-6.9201605],
            [107.6198354,-6.9201925],
            [107.6201573,-6.92097],
        ]])

    def jalanKosambi(self, nama):
        self.jalan.record(nama)
        self.jalan.line([[
            [107.6228395,-6.9194789],
            [107.6224104,-6.9187014],
            [107.6215413,-6.9191807],
            [107.621482,-6.9193903],
        ]])

    def jalanAlani(self, nama):
        self.jalan.record(nama)
        self.jalan.line([[
            [107.6211391,-6.9193106],
            [107.6214503,-6.9180964],
            [107.6196371,-6.9176491],
            [107.6194869,-6.9182296],
            [107.619739,-6.9185651],
            [107.6198088,-6.9190124],
        ]])

    def jalanGangAlani1(self, nama):
        self.jalan.record(nama)
        self.jalan.line([[
            [107.6213376,-6.9184745],
            [107.6223783,-6.9185172],
            [107.6224104,-6.9187014],
        ]])

    def jalanSuniaraja(self, nama):
        self.jalan.record(nama)
        self.jalan.line([[
            [107.6044321,-6.915826],
            [107.6066744,-6.9154425],
            [107.6074576,-6.9154425],
            [107.6083159,-6.9163266],
            [107.609101,-6.9161186],
        ]])

    def jalanABC(self, nama):
        self.jalan.record(nama)
        self.jalan.line([[
            [107.6043219,-6.9183047],
            [107.6066286,-6.9190822],
            [107.6077122,-6.91921],
            [107.6083559,-6.9195615],
            [107.6099216,-6.9197388],
        ]])

    def jalanNaripan(self, nama):
        self.jalan.record(nama)
        self.jalan.line([[
            [107.6099216,-6.9197388],
            [107.6194543,-6.9213677],
        ]])

    def jalanBenceuy(self, nama):
        self.jalan.record(nama)
        self.jalan.line([[
            [107.6065378,-6.9154526],
            [107.6062267,-6.9164751],
            [107.6063662,-6.9176679],
            [107.6067309,-6.9188715],
            [107.6064949,-6.920991],
        ]])

    def jalanBelakangFactory(self, nama):
        self.jalan.record(nama)
        self.jalan.line([[
            [107.6066049,-6.919992],
            [107.6081981,-6.9202503],
            [107.6083559,-6.9195615],
        ]])

    def jalanKejaksaan(self, nama):
        self.jalan.record(nama)
        self.jalan.line([[
            [107.6096436,-6.9185553],
            [107.6108881,-6.9184594],
            [107.6142248,-6.9190985],
        ]])

    def jalanSaad(self, nama):
        self.jalan.record(nama)
        self.jalan.line([[
            [107.6137312,-6.9219209],
            [107.6142248,-6.9190985],
            [107.6143428,-6.9188002],
        ]])

    def jalanEmbong(self, nama):
        self.jalan.record(nama)
        self.jalan.line([[
            [107.6149221,-6.9220593],
            [107.6156517,-6.9194499],
        ]])

    def close(self):
        self.kelurahan.close()
        self.kantor.close()
        self.jalan.close()
