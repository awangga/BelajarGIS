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
            [[[107.5757388, -6.8736215], [107.5757417, -6.8735590], [107.5757809, -6.8735617], [107.5757781, -6.8736228], [107.5757388, -6.8736215]]])

    def r301(self, nama):
        self.ketiga.record(nama)
        self.ketiga.poly(
            [[[107.5756935, -6.873619], [107.5756972, -6.8735564], [107.5757417, -6.8735590], [107.5757388, -6.8736215], [107.5756935, -6.873619]]])

    # Alvan Alvanzah 1174077

    def r302(self, nama):
        self.ketiga.record(nama)
        self.ketiga.poly(
            [[[107.5756935, -6.873619], [107.5756972, -6.8735564], [107.5756550, -6.8735543], [107.5756510, -6.8736155], [107.5756935, -6.873619]]])

    # Advent Nopele Sihite 1184089
    def r304(self, nama):
        self.ketiga.record(nama)
        self.ketiga.poly([[[107.575566, -6.8736059], [107.5755714, -6.8735426], [107.5756093, -6.8735469], [107.5756059, -6.8736083], [107.575566, -6.8736059]]])

    # Difa Al Fansha 1174076
    def r303(self, nama):
        self.ketiga.record(nama)
        self.ketiga.poly(
            [[[107.5756510, -6.8736155], [107.5756550, -6.8735543], [107.5756093, -6.8735469], [107.5756059, -6.8736083], [107.5756510, -6.8736155]]])

    # Muhammad Reza Syachrani 1174084
    def r307(self, nama):
        self.ketiga.record(nama)
        self.ketiga.poly(
            [[[107.5754835, -6.8735373], [107.5754792, -6.8736004], [107.5754378, -6.8735978], [107.5754432, -6.8735341], [107.5754835, -6.8735373]]])

    def r308(self, nama):
        self.ketiga.record(nama)
        self.ketiga.poly(
            [[[107.5754432, -6.8735341], [107.5754378, -6.8735978], [107.5753949, -6.8735946], [107.5754013, -6.8735299], [107.5754432, -6.8735341]]])
   
    # Kaka Kamaludin 1174067
    def r305(self, nama):
        self.ketiga.record(nama)
        self.ketiga.poly([[[107.5755252,-6.8736033], [107.5755670,-6.8736055], [107.5755724,-6.8735441], [107.5755290,-6.8735419], [107.5755252,-6.8736033]]])

    def r306(self, nama):
        self.ketiga.record(nama)
        self.ketiga.poly([[[107.5754795,-6.8736006], [107.5755256,-6.8736035], [107.5755295,-6.8735421], [107.5754838,-6.8735378], [107.5754795,-6.8736006]]])

    # Arrizal Furqona Gifary 1174070
    def r309(self, nama):
        self.ketiga.record(nama)
        self.ketiga.poly(
            [[[107.5753949, -6.8735946], [107.5754013, -6.8735299], [107.5753588, -6.8735263], [107.5753531, -6.8735916], [107.5753949, -6.8735946]]])

    # Fanny Shafira 1174069
    def r310(self, nama):
        self.ketiga.record(nama)
        self.ketiga.poly(
            [[[20, 20], [16.4, 20], [16.4, 24], [20, 24], [20, 20]]])

    # Chandra Kirana Poetra 1174079
    def rwccewek2(self, nama):
        self.ketiga.record(nama)
        self.ketiga.poly([[[107.57578,-6.87326], [107.57576,-6.87326], [107.575751,-6.87334], [107.57577,-6.87334], [107.57578,-6.87326]]])
    
    def rwccewek3(self, nama):
        self.ketiga.record(nama)
        self.ketiga.poly([[[107.57576,-6.87326], [107.57574,-6.87326], [107.57573,-6.87334], [107.57575,-6.87334], [107.57576,-6.87326]]])

    # Mochamad Arifqi Ramadhan 1174074
    def tanggaB2(self, nama):
        self.ketiga.record(nama)
        self.ketiga.poly([[[107.5752291,-6.8735757], [107.5752730, -6.8735719], [107.5752784, -6.8735194], [107.5752337, -6.8735155], [107.5752291,-6.8735757]]])

    # Handi Hermawan 1174080
    def r311(self, nama):
        self.ketiga.record(nama)
        self.ketiga.poly([[[107.5752774, -6.8733220], [107.5753526, -6.8733334], [107.5753473, -6.8734068], [107.5752696, -6.8733972], [107.5752774, -6.8733220]]])


    # Bakti Qilan Mufid 1174083

    def tanggaB1(self, nama):
        self.ketiga.record(nama)
        self.ketiga.poly(
            [[[107.5752537,-6.8732763], [107.575292247, -6.873281007], [107.5752956, -6.8732206], [107.5752573, -6.8732173], [107.5752537,-6.8732763]]])
            
    def r312(self, nama):
        self.ketiga.record(nama)
        self.ketiga.poly(
            [[[107.5752456, -6.8733733], [107.5753314, -6.8733814], [107.5753390, -6.8732867], [107.5752537,-6.8732763], [107.5752456, -6.8733733]]])

        
    #Ainul Filiani 1174073
    def rwccewek1(self, nama):
        self.ketiga.record(nama)
        self.ketiga.poly([[[24, 0], [22, 0], [22, 4], [24, 4], [24, 0]]])

    # Aulyardha Anindita 1174054
    def rwccowok(self, nama):
        self.ketiga.record(nama)
        self.ketiga.poly([[[107.5753278, -6.8732237], [107.5753622, -6.8732266], [107.5753575, -6.8732885], [107.5753241, -6.8732845], [107.5753278, -6.8732237]]])
    
    # Nurul Izza Hamka 1174062
    def rteknisi(self, nama):
            self.ketiga.record(nama)
            self.ketiga.poly([[[107.5753611, -6.8732261], [107.5754018, -6.8732289], [107.5753963, -6,8732930], [107.5753577, -6.8732875], [107.5753611, -6.8732261]]])
    
    #Tia Nur Candida 1174086
            
    def r314(self, nama):
        self.ketiga.record(nama)
        self.ketiga.poly([[[14, 0], [8, 0], [8, 4], [14, 4], [14, 0]]])

    # D.Irga B. Naufal Fakhri 1174066
    def r315(self, nama):
        self.ketiga.record(nama)
        self.ketiga.poly([[[107.57559,-6.87332],[107.5756,-6.87325], [107.5755044,-6.8732367],[107.5754922,-6.8733076],[107.57559,-6.87332]]])
    
    def r316(self, nama):
        self.ketiga.record(nama)
        self.ketiga.poly([[[107.57559,-6.87332],[107.5756,-6.87325], [107.5756888,-6.8732624], [107.5756791,-6.8733334], [107.57559,-6.87332]]])

    # Muhammad Abdul Gani Wijaya 1174071
    def r319(self, nama):
        self.ketiga.record(nama)
        self.ketiga.poly([[[-8, 6], [-13, 6], [-13, 10], [-8, 10], [-8, 6]]])

    def r320(self, nama):
        self.ketiga.record(nama)
        self.ketiga.poly([[[-8, 10], [-13, 10], [-13, 14], [-8, 14], [-8, 10]]])
        

    #Alfadian Owen 1174091
    def r321(self, nama):
        self.ketiga.record(nama)
        self.ketiga.poly([[[-8, 14], [-13, 14], [-13, 18], [-8, 18], [-8, 14]]])

    def center(self, nama):
        self.ketiga.record(nama)
        self.ketiga.poly([[[12, 7], [12, 17], [-4, 17], [-4, 7], [12, 7]]])

    #Dini Permata Putri 1174053
    def r317(self, nama):
        self.ketiga.record(nama)
        self.ketiga.poly([[[-4, 0], [-10, 0], [-10, 4], [-4, 4], [-4, 0]]])
    
    def r318(self, nama):
        self.ketiga.record(nama)
        self.ketiga.poly([[[-10, 0], [-16, 0], [-16, 4], [-10, 4], [-10, 0]]])

#-------------------- BATAS END KODING ------------------#

    def close(self):
        self.ketiga.close()
