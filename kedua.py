import shapefile

class Kedua:

    def __init__(self):
        self.kedua = shapefile.Writer('kedua', shapeType = shapefile.POLYGON)
        self.kedua.shapeType
        self.kedua.field('nama_ruangan', 'C')

    #Luthfi Muhammad Nabil - 1174035
    def tanggaBawahKiri(self, label):
        self.kedua.record(label)
        self.kedua.poly([[[107.575778,-6.873632],[107.575815,-6.873637],[107.5758234,-6.8735497], [107.5757866,-6.8735447],[107.575778,-6.873632]]])
    
    #Luthfi Muhammad Nabil - 1174035
    def tanggaBawahKanan(self, label):
        self.kedua.record(label)
        self.kedua.poly([[[107.5758232,-6.8733192],[107.5758605,-6.8733248],[107.575871,-6.873225], [107.575834,-6.87322],[107.5758232,-6.8733192]]])

    #Luthfi Muhammad Nabil - 1174035
    def tanggaAtasKiri(self, label):
        self.kedua.record(label)
        self.kedua.poly([[[107.57526,-6.873562],[107.575297,-6.873567],[107.5753082,-6.8734797], [107.5752714,-6.8734747],[107.57526,-6.873562]]])
    
    #Luthfi Muhammad Nabil - 1174035
    def tanggaAtasKanan(self, label):
        self.kedua.record(label)
        self.kedua.poly([[[107.575301,-6.8732408],[107.5753383,-6.8732464],[107.575353,-6.873155], [107.575316,-6.87315],[107.575301,-6.8732408]]])

    #Luthfi Muhammad Nabil - 1174035
    def tamanKosongTengah(self, label):
        self.kedua.record(label)
        self.kedua.poly([[[107.575424,-6.873434 ], [107.575689,-6.873473], [107.575707, -6.873354], [107.575440, -6.873317], [107.575424,-6.873434 ]]])

    #Hagan Rowlenstino - 1174040
    def R213(self, label):
        self.kedua.record(label)
        self.kedua.poly([[[107.5753629,-6.8734129], [107.5752825,-6.8733978],  [107.5752862,-6.8733748], [107.5753707,-6.8733889], [107.5753629,-6.8734129]]])
        
    #Hagan Rowlenstino - 1174040
    def IRC(self, label):
        self.kedua.record(label)
        self.kedua.poly([[[107.5753707,-6.8733889], [107.5752862,-6.8733748], [107.5752899,-6.8733451], [107.5753756,-6.8733618],  [107.5753707,-6.8733889]]])

    #Hagan Rowlenstino - 1174040
    def RLabBisnis(self, label):
        self.kedua.record(label)
        self.kedua.poly([[[107.5752899,-6.8733451], [107.5753756,-6.8733618],   [107.5753806,-6.8733353],[107.5752930,-6.8733266], [107.5752899,-6.8733451]]])

    #Hagan Rowlenstino - 1174040
    def RLabComprehensive(self, label):
        self.kedua.record(label)
        self.kedua.poly([[[107.5752930,-6.8733266], [107.5753806,-6.8733353],   [107.5753772,-6.8733132],[107.5752939,-6.8733028], [107.5752930,-6.8733266]]])

    #Kevin Natanael Nainggolan-1174059
    def ruang208(self, label):
        self.kedua.record(label)
        self.kedua.poly([[[-3, 22], [4, 22], [4, 25], [-3, 25], [-3, 22]]])

    #Kevin Natanael Nainggolan-1174059
    def ruang209(self, label):
        self.kedua.record(label)
        self.kedua.poly([[[-3, 25], [4, 25], [4, 28], [-3, 28], [-3, 25]]])

    #Kevin Natanael Nainggolan-1174059
    def ruang210(self, label):
        self.kedua.record(label)
        self.kedua.poly([[[-3, 28], [4, 28], [4, 31], [-3, 31], [-3, 28]]])

    #Irvan Rizkiansyah - 1174043
    def ruangan205(self, label):
        self.kedua.record(label)
        self.kedua.poly([[[-3, 13], [4, 13], [4, 16], [-3, 16], [-3, 13]]])

    #Irvan Rizkiansyah - 1174043
    def ruangan206(self, label):
        self.kedua.record(label)
        self.kedua.poly([[[-3, 16], [4, 16], [4, 19], [-3, 19], [-3, 16]]])

    #Irvan Rizkiansyah - 1174043
    def ruangan207(self, label):
        self.kedua.record(label)
        self.kedua.poly([[[-3, 19], [4, 19], [4, 22], [-3, 22], [-3, 19]]])
        
    #Liyana Majdah Rahma - 1174039
    def ruangan201(self, label):
        self.kedua.record(label)
        self.kedua.poly([[[-3, 1], [4, 1], [4, 4], [-3, 4], [-3, 1]]])
        
    #Liyana Majdah Rahma - 1174039
    def ruangan202(self, label):
        self.kedua.record(label)
        self.kedua.poly([[[-3, 4], [4, 4], [4, 7], [-3, 7], [-3, 4]]])

    #Alit Fajar Kurniawan - 1174057
    def RServer(self, label):
        self.kedua.record(label)
        self.kedua.poly([[[107.5753756,-6.873252],[107.5754129,-6.8732576],[107.575427,-6.873165], [107.57539,-6.87316],[107.5753756,-6.873252]]])

    #Alit Fajar Kurniawan - 1174057
    def LabLogistik(self, label):
        self.kedua.record(label)
        self.kedua.poly([[[107.5754129,-6.8732576],[107.5754502,-6.8732632],[107.575464,-6.87317], [107.575427,-6.873165],[107.5754129,-6.8732576]]])

    #Dika Sukma Pradana - 1174050
    def ruangan219(self, label):
        self.kedua.record(label)
        self.kedua.poly([[[107.5754502,-6.8732632],[107.5755248,-6.8732744],[107.575538,-6.87318], [107.575464,-6.87317],[107.5754502,-6.8732632]]])

    #Dika Sukma Pradana - 1174050
    def ruangan220(self, label):
        self.kedua.record(label)
        self.kedua.poly([[[107.5755248,-6.8732744],[107.5755621,-6.87328],[107.575575,-6.873185], [107.575538,-6.87318],[107.5755248,-6.8732744]]])
		
	#Faisal Najib Abdullah - 1174042
    def toiletdosen(self, label):
        self.kedua.record(label)
        self.kedua.poly([[[22, 38.5], [29, 38.5], [29, 40], [22, 40], [22, 38.5]]])
	
	#Faisal Najib Abdullah - 1174042
    def toiletcowo(self, label):
        self.kedua.record(label)
        self.kedua.poly([[[22, 37], [29, 37], [29, 38.5], [22, 38.5], [22, 37]]])
		
	#Faisal Najib Abdullah - 1174042
    def prodiak(self, label):
        self.kedua.record(label)
        self.kedua.poly([[[7, 1], [19, 1], [19, 8], [7, 8], [7, 1]]])
    
    #Rangga Putra Ramdhani - 1174056
    def ruangan203(self, label):
        self.kedua.record(label)
        self.kedua.poly([[[-3, 7], [4, 7], [4, 10], [-3, 10], [-3, 7]]])

    #Rangga Putra Ramdhani - 1174056
    def ruangan204(self, label):
        self.kedua.record(label)
        self.kedua.poly([[[-3, 10], [4, 10], [4, 13], [-3, 13], [-3, 10]]])

    #Teddy Gideon Manik - 1174038
    def prodiD3MB(self, label):
        self.kedua.record(label)
        self.kedua.poly([[[22, 7], [29, 7], [29, 10], [22, 10], [22, 7]]])

    #Teddy Gideon Manik - 1174038
    def prodiD3LB(self, label):
        self.kedua.record(label)
        self.kedua.poly([[[22, 1], [29, 1], [29, 7], [22, 7], [22, 1]]])
                
    #Muhammad Afra Faris-1174041
    def ruangan211(self, label):
        self.kedua.record(label)
        self.kedua.poly([[[-3, 31], [4, 31], [4, 34], [-3, 34], [-3, 31]]])

    #Muhammad Afra Faris-1174041
    def ruangan212(self, label):
        self.kedua.record(label)
        self.kedua.poly([[[-3, 34], [4, 34], [4, 37], [-3, 37], [-3, 34]]])

	#Ichsan Hizman Hardy - 1174034
    def ruangan221(self, label):
        self.kedua.record(label)
        self.kedua.poly([[[22, 19], [29, 19], [29, 22], [22, 22], [22, 19]]])
		
	#Ichsan Hizman Hardy - 1174034
    def ruangan222(self, label):
        self.kedua.record(label)
        self.kedua.poly([[[22, 16], [29, 16], [29, 19], [22, 19], [22, 16]]])
        
    #Pasang fungsi baru diatas close()
    def close(self):
        self.kedua.close()