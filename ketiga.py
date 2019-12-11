import shapefile


class ketiga:
    
    def __init__(self):
        self.ketiga = shapefile.Writer('ketiga', shapeType=shapefile.POLYGON)
        self.ketiga.shapeType
        self.ketiga.field('nama_ruangan', 'C')

#-------------------- KODING ------------------#
    
    #Ilham Muhammad Ariq 1174087
    def tanggaD2(self, nama):
        self.ketiga.record(nama)
        self.ketiga.poly([[[-16, 20], [-19, 20], [-19, 27], [-16, 27], [-16, 20]]])

    def r301(self, nama):
        self.ketiga.record(nama)
        self.ketiga.poly([[[-12.4, 20], [-16, 20], [-16, 24], [-12.4, 24], [-12.4, 20]]])


    #Alvan Alvanzah 1174077
    def r302(self, nama):
        self.ketiga.record(nama)
        self.ketiga.poly([[[-8.8, 20], [-12.4, 20], [-12.4, 24], [-8.8, 24], [-8.8, 20]]])

    # Advent Nopele Sihite 1184089
    def r304(self, nama):
        self.ketiga.record(nama)
        self.ketiga.poly([[[-1.6, 20], [-5.2, 20], [-5.2, 24], [-1.6, 24], [-1.6, 20]]])
	
	#Difa 
    def r303(self, nama):
        self.ketiga.record(nama)
        self.ketiga.poly([[[-5.2, 20], [-8.8, 20], [-8.8, 24], [-5.2, 24], [-5.2, 20]]])
    
    #Muhammad Reza Syachrani 1174084
    def r307(self, nama):
        self.ketiga.record(nama)
        self.ketiga.poly([[[9.2, 20], [5.6, 20], [5.6, 24], [9.2, 24], [9.2, 20]]])
    
    def r308(self, nama):
        self.ketiga.record(nama)
        self.ketiga.poly([[[12.8, 20], [9.2, 20], [9.2, 24], [12.8, 24], [12.8, 20]]])

    #Kaka Kamaludin 1174067
    def r305(self, nama):
        self.ketiga.record(nama)
        self.ketiga.poly([[[2, 20], [-1.6, 20], [-1.6, 24], [2, 24], [2, 20]]])

    def r306(self, nama):
        self.ketiga.record(nama)
        self.ketiga.poly([[[5.6, 20], [2, 20], [2, 24], [5.6, 24], [5.6, 20]]])




    #lanjutkan

#-------------------- BATAS END KODING ------------------#

    def close(self):
        self.ketiga.close()
        
