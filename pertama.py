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
    
    def close(self):
        self.pertama.close()