import shapefile

class Pertama:

    def __init__(self):
        self.pertama = shapefile.Writer('pertama', shapeType = shapefile.POLYGON)
        self.pertama.shapeType
        self.pertama.field('nama_ruangan', 'C')

    #Harun Ar - Rasyid - 1174027
    def bauk(self, nama):
        self.pertama.record(nama)
        self.pertama.poly([[[107.575807,-6.873297],[107.575712,-6.873282],[107.575703,-6.873356],[107.575799,-6.873359],[107.575807,-6.873297]]])

    #Harun Ar - Rasyid - 1174027
    def baak(self, nama):
        self.pertama.record(nama)
        self.pertama.poly([[[107.575799,-6.873359],[107.575703,-6.873356],[107.575681,-6.873551],[107.575770,-6.873563],[107.575799,-6.873359]]])

    #dzihan
    def ruang116(self, nama):
        self.pertama.record(nama)
        self.pertama.poly([[[107.575714,-6.873283], [107.575727,-6.873227], [107.575669,-6.873219], [107.575660,-6.873273], [107.575714,-6.873283]]])

    #Nico Ekklesia Sembiring - 1174096
    def ruangan113(self, nama):
        self.pertama.record(nama)
        self.pertama.poly([[[107.575476, -6.873235], [107.575608, -6.873246], [107.575603, -6.873329], [107.575470, -6.873320], [107.575476, -6.873235]]])

    #Kadek Diva Krishna Murti - 1174006
    def ruangan111(self, nama):
        self.pertama.record(nama)
        #self.pertama.poly([[[-16, -28], [-16, -36], [-9, -36], [-9, -28], [-16, -28]]])
        self.pertama.poly([[[107.575345, -6.873225], [107.575407, -6.873229], [107.57540, -6.873319], [107.5753382, -6.8733146], [107.575345, -6.873225]]])
    #Kadek Diva Krishna Murti - 1174006
    def wcBL(self, nama):
        self.pertama.record(nama)
        #self.pertama.poly([[[-16, -36], [-16, -40], [-9, -40], [-9, -36], [-16, -36]]])
        self.pertama.poly([[[107.5753045, -6.8732222], [107.575345, -6.873225], [107.5753382, -6.8733146], [107.5752986, -6.8733113], [107.5753045, -6.8732222]]])
    #Kadek Diva Krishna Murti - 1174006
    def tanggaBL(self, nama):
        self.pertama.record(nama)
        self.pertama.poly([[[107.5752819, -6.8732203], [107.5753045, -6.8732222], [107.5752986, -6.8733113], [107.5752767, -6.8733098], [107.5752819, -6.8732203]]])
    #Kadek Diva Krishna Murti - 1174006
    def gudangBL(self, nama):
        self.pertama.record(nama)
        self.pertama.poly([[[107.5752576, -6.8732188], [107.5752819, -6.8732203], [107.5752767, -6.8733098], [107.5752512, -6.8733073], [107.5752576, -6.8732188]]])
    #Kadek Diva Krishna Murti - 1174006
    def haloPos(self, nama):
        self.pertama.record(nama)
        self.pertama.poly([[[107.5752475, -6.8733551], [107.5753716, -6.8733654], [107.5753604, -6.8734993], [107.5752363, -6.8734896], [107.5752475, -6.8733551]]])
		
    #Dwi Yulianingsih - 1174009
    def ruang117(self, nama):
        self.pertama.record(nama)
        self.pertama.poly([[[107.5757276, -6.8732357], [107.5757198, -6.8733199], [107.5757700, -6.8733185], [107.5757828, -6.8732406], [107.5757276, -6.8732357]]])
        
    #Dwi Septiani Tsaniyah - 1174003
    def ruang115(self, nama):
        self.pertama.record(nama)
        self.pertama.poly([[[107.5756064, -6.8732302], [107.5755946, -6.8733002], [107.5756508, -6.8733111], [107.5756626, -6.8732342], [107.5756064, -6.8732302]]])
           
    #habib
    def ruang103(self, nama):
        self.pertama.record(nama)
        self.pertama.poly([[[107.575659, -6.873549], [107.575623, -6.873544], [107.575618, -6.873617], [107.575656, -6.873618], [107.575659, -6.873549]]])
    
     #felix
    def ruang107(self, nama):
        self.pertama.record(nama)
        #
        #self.pertama.poly([[[18, -16], [18, -12], [25, -12], [25, -16], [18, -16]]])
        self.pertama.poly([[[107.575448, -6.873518], [107.575485, -6.873523], [107.575479, -6.873590], [107.575392, -6.873579], [107.575448, -6.873518]]])

    def ruang108(self, nama):
        self.pertama.record(nama)
        #self.pertama.poly([[[18, -16], [18, -24], [25, -24], [25, -16], [18, -16]]])
        self.pertama.poly([[[107.575408, -6.873510], [107.575448, -6.873518], [107.575435, -6.873584], [107.575392, -6.873579], [107.575408, -6.873510]]])
        
    #Evietania 1174051
    def gudangL(self, nama):
        self.pertama.record(nama)
        self.pertama.poly([[[107.575854,-6.873303], [107.575831, -6.873297], [107.575840, -6.873223], [107.575867, -6.873229], [107.575854,-6.873303]]])

    def tanggaL(self, nama):
        self.pertama.record(nama)
        self.pertama.poly([[[107.575831, -6.873297], [107.575840, -6.873223], [107.575822, -6.873223], [107.575808, -6.873297], [107.575831, -6.873297]]])
        
    #Arjun Yuda Firwanda 1174008
    def gudangR(self, nama):
        self.pertama.record(nama)
        self.pertama.poly([[[107.5757921,-6.8735487], [107.5757856,-6.8736337], [107.5757491,-6.8736308], [107.5757547,-6.8735455], [107.5757921,-6.8735487]]])

    def tanggaR(self, nama):
        self.pertama.record(nama)
        self.pertama.poly([[[107.5757547,-6.8735455], [107.5757491,-6.8736308], [107.5757185,-6.8736261], [107.5757218,-6.8735441], [107.5757547,-6.8735455]]])
        
    #Damara Benedikta 1174012
    def ruang102(self, nama):
        self.pertama.record(nama)
        self.pertama.poly([[[107.575706, -6.873555], [107.575663, -6.873547], [107.575656,-6.873617 ], [107.575694, -6.873621], [107.575706, -6.873555]]])
        
        # oni
    def ruang104(self, nama):
        self.pertama.record(nama)
        self.pertama.poly([[[107.575619,-6.873535], [107.575613,-6.873610], [107.575575,-6.873608], [107.575573,-6.873540], [107.575619,-6.873535]]])
        
        #Srir
    def ruang105(self, nama):
        self.pertama.record(nama)
        self.pertama.poly([[[18, -8], [18, -4], [25, -4], [25, -8], [18, -8]]])

     #Dezha Aidil Martha 1174025
    def ruang101(self, nama):
        self.pertama.record(nama)
        self.pertama.poly([[[18, 8], [18, 12], [25, 12], [25, 8], [18, 8]]])

        #Muhammad Tomy Nur Maulidy 1174031
    def ruang106(self, nama):
        self.pertama.record(nama)
        self.pertama.poly([[[107.575485, -6.873523], [107.5755327, -6.8735332], [107.5755284, -6.8736001], [107.575479, -6.873590],[107.575485, -6.873523]]])
        
        #Choirul Anam 1174004
    def ruang114(self, nama):
        self.pertama.record(nama)
        self.pertama.poly([[[107.575561, -6.873189], [107.575607, -6.873195], [107.575590, -6.873262], [107.575540, -6.873255], [107.575561, -6.873189]]])

        #Muh. Rifky Prananda 1174017
    def ruang112(self, nama):
        self.pertama.record(nama)
        self.pertama.poly([[[107.575407, -6.873229], [107.575476, -6.873235], [107.575470, -6.873320], [107.57540, -6.873319], [107.575407, -6.873229]]])

    #Muhammad Fahmi - 1174021
    def ruang109(self, nama):
        self.pertama.record(nama)
        self.pertama.poly([[[107.5753864, -6.8735276], [107.5753854, -6.8735992], [107.5753179, -6.8735945], [107.5753237, -6.8735176], [107.5753864, -6.8735276]]])

    #Muhammad Fahmi - 1174021
    def wcBL2(self, nama):
        self.pertama.record(nama)
        self.pertama.poly([[[107.5753237, -6.8735176], [107.5753179, -6.8735945], [107.5752824, -6.8735924], [107.5752876, -6.8735208], [107.5753237, -6.8735176]]])

    #Muhammad Fahmi - 1174021
    def tanggaBL2(self, nama):
        self.pertama.record(nama)
        self.pertama.poly([[[107.5752876, -6.8735208], [107.5752824, -6.8735924], [107.5752559, -6.8735910], [107.5752629, -6.8735275], [107.5752876, -6.8735208]]])

    #Muhammad Fahmi - 1174021
    def gudangBL2(self, nama):
        self.pertama.record(nama)
        self.pertama.poly([[[107.5752629, -6.8735275], [107.5752559, -6.8735910], [107.5752276, -6.8735853], [107.5752329, -6.8735267], [107.5752629, -6.8735275]]])
    
    def close(self):
        self.pertama.close()