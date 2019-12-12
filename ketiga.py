import shapefile


class ketiga:

    def __init__(self):
        self.ketiga = shapefile.Writer('ketiga', shapeType=shapefile.POLYGON)
        self.ketiga.shapeType
        self.ketiga.field('nama_ruangan', 'C')

#-------------------- KODING ------------------#

    # Ilham Muhammad Ariq 1174087
    def tanggaD2(self, nama):
        self.ketiga.record(nama)
        self.ketiga.poly(
            [[[-16, 20], [-19, 20], [-19, 27], [-16, 27], [-16, 20]]])

    def r301(self, nama):
        self.ketiga.record(nama)
        self.ketiga.poly(
            [[[-12.4, 20], [-16, 20], [-16, 24], [-12.4, 24], [-12.4, 20]]])

    # Alvan Alvanzah 1174077

    def r302(self, nama):
        self.ketiga.record(nama)
        self.ketiga.poly(
            [[[-8.8, 20], [-12.4, 20], [-12.4, 24], [-8.8, 24], [-8.8, 20]]])

    # Advent Nopele Sihite 1184089
    def r304(self, nama):
        self.ketiga.record(nama)
        self.ketiga.poly(
            [[[-1.6, 20], [-5.2, 20], [-5.2, 24], [-1.6, 24], [-1.6, 20]]])

        # Difa
    def r303(self, nama):
        self.ketiga.record(nama)
        self.ketiga.poly(
            [[[-5.2, 20], [-8.8, 20], [-8.8, 24], [-5.2, 24], [-5.2, 20]]])

    # Muhammad Reza Syachrani 1174084
    def r307(self, nama):
        self.ketiga.record(nama)
        self.ketiga.poly(
            [[[9.2, 20], [5.6, 20], [5.6, 24], [9.2, 24], [9.2, 20]]])

    def r308(self, nama):
        self.ketiga.record(nama)
        self.ketiga.poly(
            [[[12.8, 20], [9.2, 20], [9.2, 24], [12.8, 24], [12.8, 20]]])

    # Kaka Kamaludin 1174067
    def r305(self, nama):
        self.ketiga.record(nama)
        self.ketiga.poly([[[2, 20], [-1.6, 20], [-1.6, 24], [2, 24], [2, 20]]])

    def r306(self, nama):
        self.ketiga.record(nama)
        self.ketiga.poly([[[5.6, 20], [2, 20], [2, 24], [5.6, 24], [5.6, 20]]])

    # Arrizal Furqona Gifary 1174070
    def r309(self, nama):
        self.ketiga.record(nama)
        self.ketiga.poly(
            [[[16.4, 20], [12.8, 20], [12.8, 24], [16.4, 24], [16.4, 20]]])

    # Fanny Shafira 1174069
    def r310(self, nama):
        self.ketiga.record(nama)
        self.ketiga.poly(
            [[[20, 20], [16.4, 20], [16.4, 24], [20, 24], [20, 20]]])

    # Chandra Kirana Poetra 1174079
    def rwccewek2(self, nama):
        self.ketiga.record(nama)
        self.ketiga.poly([[[22, 20], [20, 20], [20, 24], [22, 24], [22, 20]]])

    def rwccewek3(self, nama):
        self.ketiga.record(nama)
        self.ketiga.poly([[[24, 20], [22, 20], [22, 24], [24, 24], [24, 20]]])

    # Mochamad Arifqi Ramadhan 1174074
    def tanggaB2(self, nama):
        self.ketiga.record(nama)
        self.ketiga.poly([[[27, 20], [24, 20], [24, 27], [27, 27], [27, 20]]])

    # Handi Handi Hermawan 1174080
    def r311(self, nama):
        self.ketiga.record(nama)
        self.ketiga.poly([[[16, 12], [16, 18], [22, 18], [22, 12], [16, 12]]])

    # Bakti Qilan Mufid 1174083
    def r312(self, nama):
        self.ketiga.record(nama)
        self.ketiga.poly([[[16, 6], [16, 12], [22, 12], [22, 6], [16, 6]]])

    def tanggaB1(self, nama):
        self.ketiga.record(nama)
        self.ketiga.poly([[[27, -3], [24, -3], [24, 4], [27, 4], [27, -3]]])
        
    #Ainul Filiani 1174073
    def rwccewek1(self, nama):
        self.ketiga.record(nama)
        self.ketiga.poly([[[24, 0], [22, 0], [22, 4], [24, 4], [24, 0]]])

    # Aulyardha Anindita 1174054
    def rwccowok(self, nama):
        self.ketiga.record(nama)
        self.ketiga.poly([[[22, 0], [20, 0], [20, 4], [22, 4], [22, 0]]])
    
    # Nurul Izza Hamka 1174062
    def rteknisi(self, nama):
            self.ketiga.record(nama)
            self.ketiga.poly([[[20, 0], [14, 0], [14, 4], [20, 4], [20, 0]]])
    
    #Tia Nur Candida 1174086
            
    def r314(self, nama):
        self.ketiga.record(nama)
        self.ketiga.poly([[[14, 0], [8, 0], [8, 4], [14, 4], [14, 0]]])

    # D.Irga B. Naufal Fakhri 1174066
    def r315(self, nama):
        self.ketiga.record(nama)
        self.ketiga.poly([[[8, 0], [2, 0], [2, 4], [8, 4], [8, 0]]])
    
    def r316(self, nama):
        self.ketiga.record(nama)
        self.ketiga.poly([[[2, 0], [-4, 0], [-4, 4], [2, 4], [2, 0]]])

    #Dini Permata Putri 1174053
    def r317(self, nama):
        self.ketiga.record(nama)
        self.ketiga.poly([[[-4, 0], [-10, 0], [-10, 4], [-4, 4], [-4, 0]]])
    
    def r318(self, nama):
        self.ketiga.record(nama)
        self.ketiga.poly([[[-10, 0], [-16, 0], [-16, 4], [-10, 4], [-10, 0]]])

    # Muhammad Abdul Gani Wijaya 1174071
    def r319(self, nama):
        self.ketiga.record(nama)
        self.ketiga.poly([[[-8, 6], [-13, 6], [-13, 10], [-8, 10], [-8, 6]]])

    def r320(self, nama):
        self.ketiga.record(nama)
        self.ketiga.poly([[[-8, 10], [-13, 10], [-13, 14], [-8, 14], [-8, 10]]])
        

   

    # lanjutkan

#-------------------- BATAS END KODING ------------------#

    def close(self):
        self.ketiga.close()
