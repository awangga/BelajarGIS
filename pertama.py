import shapefile

class Pertama:

    def __init__(self):
        self.pertama = shapefile.Writer('pertama', shapeType = shapefile.POLYGON)
        self.pertama.shapeType
        self.pertama.field('nama_ruangan', 'C')

    #Harun Ar - Rasyid - 1174027
    def bauk(self, nama):
        self.pertama.record(nama)
        self.pertama.poly([[[-4, 0], [2, 0], [2, 8], [-4, 8], [-4, 0]]])

    #Harun Ar - Rasyid - 1174027
    def baak(self, nama):
        self.pertama.record(nama)
        self.pertama.poly([[[2, 0], [13, 0], [13, 8], [2, 8], [2, 0]]])

    #Kadek Diva Krishna Murti - 1174006
    def ruangan111(self, nama):
        self.pertama.record(nama)
        self.pertama.poly([[[-16, -28], [-16, -36], [-9, -36], [-9, -28], [-16, -28]]])
    #Nico Ekklesia Sembiring - 1174096
    def ruangan113(self, nama):
        self.pertama.record(nama)
        self.pertama.poly([[[-16, -20], [-16, -4], [-9, -4], [-9, -20], [-16, -20]]])
    #Kadek Diva Krishna Murti - 1174006
    def wcBL(self, nama):
        self.pertama.record(nama)
        self.pertama.poly([[[-16, -36], [-16, -40], [-9, -40], [-9, -36], [-16, -36]]])
    #Kadek Diva Krishna Murti - 1174006
    def tanggaBL(self, nama):
        self.pertama.record(nama)
        self.pertama.poly([[[-16, -40], [-16, -42], [-9, -42], [-9, -40], [-16, -40]]])
    #Kadek Diva Krishna Murti - 1174006
    def gudangBL(self, nama):
        self.pertama.record(nama)
        self.pertama.poly([[[-16, -42], [-16, -44], [-9, -44], [-9, -42], [-16, -42]]])
    #Kadek Diva Krishna Murti - 1174006
    def haloPos(self, nama):
        self.pertama.record(nama)
        self.pertama.poly([[[-4, -32], [-4, -40], [13, -40], [13, -32], [-4, -32]]])
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

    def close(self):
        self.pertama.close()