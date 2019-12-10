import shapefile

class Kedua:

    def __init__(self):
        self.kedua = shapefile.Writer('kedua', shapeType = shapefile.POLYGON)
        self.kedua.shapeType
        self.kedua.field('nama_ruangan', 'C')

    #Luthfi Muhammad Nabil - 1174035
    def tanggaBawahKiri(self, label):
        self.kedua.record(label)
        self.kedua.poly([[[-3, -2], [4, -2], [4, 1], [-3, 1], [-3, -2]]])
    
    #Luthfi Muhammad Nabil - 1174035
    def tanggaBawahKanan(self, label):
        self.kedua.record(label)
        self.kedua.poly([[[22, -2], [29, -2], [29, 1], [22, 1], [22, -2]]])

    #Luthfi Muhammad Nabil - 1174035
    def tanggaAtasKiri(self, label):
        self.kedua.record(label)
        self.kedua.poly([[[-3, 40], [4, 40], [4, 43], [-3, 43], [-3, 40]]])
    
    #Luthfi Muhammad Nabil - 1174035
    def tanggaAtasKanan(self, label):
        self.kedua.record(label)
        self.kedua.poly([[[22, 40], [29, 40], [29, 43], [22, 43], [22, 40]]])

    #Luthfi Muhammad Nabil - 1174035
    def tamanKosongTengah(self, label):
        self.kedua.record(label)
        self.kedua.poly([[[7, 11], [19, 11], [19, 30], [7, 30], [7, 11]]])
    #Pasang fungsi baru diatas close()
    def close(self):
        self.kedua.close()