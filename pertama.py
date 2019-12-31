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
        self.pertama.poly([[[-16, 8], [-16, 12], [-9, 12], [-9, 8], [-16, 8]]])
    #dwisep
    def ruang115(self, nama):
        self.pertama.record(nama)
        self.pertama.poly([[[-16, 0], [-16, 4], [-9, 4], [-9, 0], [-16, 0]]])
        
    #habib
    def ruang103(self, nama):
        self.pertama.record(nama)
        self.pertama.poly([[[18, 0], [18, 4], [25, 4], [25, 0], [18, 0]]])
    
     #felix
    def ruang107(self, nama):
        self.pertama.record(nama)
        self.pertama.poly([[[18, -16], [18, -12], [25, -12], [25, -16], [18, -16]]])

    def ruang108(self, nama):
        self.pertama.record(nama)
        self.pertama.poly([[[18, -16], [18, -24], [25, -24], [25, -16], [18, -16]]])

    #Evietania 1174051
    def gudangL(self, nama):
        self.pertama.record(nama)
        self.pertama.poly([[[-16,14], [-16, 16], [-9, 16], [-9, 14], [-16,14]]])

    def tanggaL(self, nama):
        self.pertama.record(nama)
        self.pertama.poly([[[-16, 12], [-16, 14], [-9, 14], [-9, 12], [-16, 12]]])
        
     #Arjun Yuda Firwanda 1174008
    def gudangR(self, nama):
        self.pertama.record(nama)
        self.pertama.poly([[[18, 14], [18, 16], [25, 16], [25, 14], [18, 14]]])

    def tanggaR(self, nama):
        self.pertama.record(nama)
        self.pertama.poly([[[18, 12], [18, 14], [25, 14], [25, 12], [18, 12]]])
        
    #Damara Benedikta 1174012
    def ruang102(self, nama):
        self.pertama.record(nama)
        self.pertama.poly([[[18, 4], [18, 8], [25, 8], [25, 4], [18, 4]]])
        
        # oni
    def ruang104(self, nama):
        self.pertama.record(nama)
        self.pertama.poly([[[18, -4], [18, 0], [25, 0], [25, -4], [18, -4]]])
        
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
        self.pertama.poly([[[18, -12], [18, -8], [25, -8], [25, -12], [18, -12]]])
        
        #Choirul Anam 1174004
    def ruang114(self, nama):
        self.pertama.record(nama)
        self.pertama.poly([[[-16, -4], [-16, 0], [-9, 0], [-9, -4], [-16, -4]]])

        #Muh. Rifky Prananda 1174017
    def ruang112(self, nama):
        self.pertama.record(nama)
        self.pertama.poly([[[-16, -20], [-16, -28], [-9, -28], [-9, -20], [-16, -20]]])

    #Muhammad Fahmi - 1174021
    def ruang109(self, nama):
        self.pertama.record(nama)
        self.pertama.poly([[[18, -28], [18,-36], [25,-36], [25, -28], [18,-28]]])

    #Muhammad Fahmi - 1174021
    def wcBL2(self, nama):
        self.pertama.record(nama)
        self.pertama.poly([[[18, -36], [18, -40], [25, -40], [25, -36], [18, -36]]])

    #Muhammad Fahmi - 1174021
    def tanggaBL2(self, nama):
        self.pertama.record(nama)
        self.pertama.poly([[[18, -40], [18, -42], [25, -42], [25, -40], [18, -40]]])

    #Muhammad Fahmi - 1174021
    def gudangBL2(self, nama):
        self.pertama.record(nama)
        self.pertama.poly([[[18, -42], [18, -44], [25, -44], [25, -42], [18, -42]]])
    
    def close(self):
        self.pertama.close()