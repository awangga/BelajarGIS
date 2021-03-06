import shapefile

class Ciwidey:

    def __init__(self):
        self.kelurahan = shapefile.Writer(
            'kelurahan_ciwidey', shapeType=shapefile.POLYGON)
        self.kelurahan.shapeType
        self.kelurahan.field('kelurahan_di_ciwidey', 'C')

        self.kantor = shapefile.Writer(
            'kantor_kelurahan_ciwidey', shapeType=shapefile.POINT)
        self.kantor.shapeType
        self.kantor.field('kantor_kelurahan_di_ciwidey', 'C')

        self.jalan = shapefile.Writer(
            'jalan_ciwidey', shapeType=shapefile.POLYLINE)
        self.jalan.shapeType
        self.jalan.field('jalan_di_ciwidey', 'C')

    # Kelurahan
    def kelurahanLebakmuncang(self, nama):
        self.kelurahan.record(nama)
        self.kelurahan.poly([[
            [107.4428282,-7.0777244],
            [107.4402533,-7.0791724],
            [107.4364767,-7.078491],
            [107.4339877,-7.0810463],
            [107.4323569,-7.081387],
            [107.4308119,-7.0832608],
            [107.428752,-7.0826646],
            [107.4267779,-7.079939],
            [107.4248896,-7.0803649],
            [107.4228297,-7.0843681],
            [107.4198256,-7.0838571],
            [107.4204264,-7.0781503],
            [107.418624,-7.0776392],
            [107.418624,-7.0790872],
            [107.4145041,-7.0830905],
            [107.4127875,-7.0826646],
            [107.4114142,-7.0838571],
            [107.410985,-7.085305],
            [107.4095259,-7.0859864],
            [107.4103413,-7.0868409],
            [107.4100838,-7.0887147],
            [107.4082384,-7.0894786],
            [107.406951,-7.0915228],
            [107.4073801,-7.0929708],
            [107.4089251,-7.0947594],
            [107.41047,-7.1016584],
            [107.4095259,-7.1023398],
            [107.4091826,-7.1092387],
            [107.4065218,-7.1140082],
            [107.406436,-7.116904],
            [107.4037753,-7.1202256],
            [107.4021445,-7.1214179],
            [107.4038611,-7.1235471],
            [107.4033461,-7.1248247],
            [107.4041186,-7.1262725],
            [107.4019728,-7.1297644],
            [107.4036036,-7.1365777],
            [107.4033461,-7.1386217],
            [107.3981104,-7.1394733],
            [107.396823,-7.1410915],
            [107.3938189,-7.1433909],
            [107.3997841,-7.1472259],
            [107.4154482,-7.1442425],
            [107.4192248,-7.1385365],
            [107.4127016,-7.1368332],
            [107.4126158,-7.1340227],
            [107.4268637,-7.1152858],
            [107.4261664,-7.1143941],
            [107.4321639,-7.1071998],
            [107.4326575,-7.1014986],
            [107.4367788,-7.0989731],
            [107.4376814,-7.0991624],
            [107.4386282,-7.098008],
            [107.4398352,-7.0979135],
            [107.4400175,-7.0963617],
            [107.4453604,-7.0947914],
            [107.4542437,-7.086242],
            [107.4547587,-7.0824943],
            [107.455617,-7.0795983],
            [107.4532137,-7.0798538],
            [107.4493513,-7.0795983],
            [107.4469481,-7.0780651],
            [107.4457465,-7.0817277],
            [107.4441157,-7.082835],
            [107.4425707,-7.081387],
            [107.4428282,-7.0777244],
        ]])

    def kelurahanPanundaan(self, nama):
        self.kelurahan.record(nama)
        self.kelurahan.poly([[
            [107.4261664,-7.1143941],
            [107.42785,-7.1135672],
            [107.4290087,-7.1142485],
            [107.4305108,-7.1136524],
            [107.4315407,-7.1133543],
            [107.4331286,-7.1144189],
            [107.433944,-7.1141634],
            [107.4347165,-7.1148447],
            [107.4341586,-7.1153558],
            [107.434974,-7.1161223],
            [107.4353173,-7.1154835],
            [107.435961,-7.1163352],
            [107.4356606,-7.1167185],
            [107.4361327,-7.117996],
            [107.4367764,-7.1177831],
            [107.4378064,-7.1188051],
            [107.4387076,-7.1183367],
            [107.4382784,-7.119231],
            [107.4388792,-7.1196994],
            [107.4389222,-7.1203382],
            [107.4394801,-7.1207214],
            [107.4402525,-7.1200826],
            [107.4418404,-7.1185496],
            [107.4426987,-7.1191032],
            [107.4429133,-7.1179108],
            [107.4439433,-7.1176127],
            [107.4442437,-7.1169314],
            [107.4454882,-7.1156113],
            [107.4463036,-7.1153983],
            [107.4468186,-7.1147596],
            [107.4474623,-7.1148447],
            [107.4479773,-7.1141208],
            [107.449136,-7.1141208],
            [107.4505522,-7.1126303],
            [107.4515822,-7.1123748],
            [107.4520543,-7.1113953],
            [107.4516251,-7.1106714],
            [107.4520543,-7.10999],
            [107.4512818,-7.10999],
            [107.4510243,-7.1090106],
            [107.4500802,-7.1087976],
            [107.4503806,-7.1082014],
            [107.4499514,-7.1073923],
            [107.4492218,-7.1078608],
            [107.4484923,-7.1075627],
            [107.4493935,-7.1065406],
            [107.448621,-7.1058592],
            [107.4477198,-7.1070516],
            [107.447119,-7.1062851],
            [107.4478915,-7.1058592],
            [107.4477198,-7.1053056],
            [107.4499514,-7.1027505],
            [107.445617,-7.1047946],
            [107.443042,-7.1049649],
            [107.4428704,-7.103517],
            [107.4427845,-7.1026653],
            [107.4421837,-7.102495],
            [107.4417546,-7.1031763],
            [107.4406388,-7.1036448],
            [107.4394801,-7.1030486],
            [107.4387505,-7.102495],
            [107.4378064,-7.1006638],
            [107.4360039,-7.1000675],
            [107.4350169,-7.100025],
            [107.4326575,-7.1014986],
            [107.4321639,-7.1071998],
            [107.4261664,-7.1143941],
        ]])

    def kelurahanNengkelan(self, nama):
        self.kelurahan.record(nama)
        self.kelurahan.poly([[
            [107.4469481,-7.0780651],
            [107.4493513,-7.0795983],
            [107.4536111,-7.0798498],
            [107.455617,-7.0795983],
            [107.4567237,-7.0810821],
            [107.4618735,-7.082232],
            [107.4633756,-7.0790805],
            [107.4628606,-7.0778029],
            [107.4632897,-7.0772918],
            [107.4634185,-7.0764826],
            [107.4630751,-7.0760141],
            [107.4621083,-7.0744411],
            [107.4603917,-7.0740831],
            [107.4594047,-7.0741683],
            [107.4581601,-7.0751904],
            [107.4554136,-7.0700797],
            [107.4539544,-7.0658208],
            [107.4547269,-7.062371],
            [107.4544694,-7.0611359],
            [107.455199,-7.0587935],
            [107.4555423,-7.0534271],
            [107.4564435,-7.0519111],
            [107.4553933,-7.0517381],
            [107.4477544,-7.0476068],
            [107.4449649,-7.04914],
            [107.4427535,-7.0493983],
            [107.4408021,-7.0498641],
            [107.438828,-7.0506733],
            [107.438313,-7.0514825],
            [107.4384417,-7.052164],
            [107.4389567,-7.0516529],
            [107.4394288,-7.0519084],
            [107.4402215,-7.0516556],
            [107.4419608,-7.0518233],
            [107.4437203,-7.0508437],
            [107.443892,-7.0502048],
            [107.4445357,-7.0509288],
            [107.4452653,-7.0506307],
            [107.4453082,-7.0497789],
            [107.445909,-7.0505455],
            [107.4454799,-7.0514825],
            [107.4442353,-7.0517807],
            [107.4440636,-7.0523769],
            [107.4441495,-7.0540806],
            [107.4434199,-7.0541657],
            [107.4432053,-7.0548472],
            [107.4437203,-7.055486],
            [107.4430766,-7.0558268],
            [107.442862,-7.0564656],
            [107.4437632,-7.0573174],
            [107.4448361,-7.0579563],
            [107.4447074,-7.0589784],
            [107.4441697,-7.0597052],
            [107.443892,-7.0606394],
            [107.4448361,-7.061619],
            [107.4444499,-7.0621301],
            [107.4444499,-7.0631097],
            [107.4435916,-7.0644299],
            [107.4441924,-7.0647281],
            [107.4437203,-7.0651965],
            [107.4442353,-7.065665],
            [107.4441495,-7.066389],
            [107.4446215,-7.0663465],
            [107.4455228,-7.0668149],
            [107.4451794,-7.0684759],
            [107.4463811,-7.069924],
            [107.4459948,-7.0707331],
            [107.4465098,-7.0710739],
            [107.4476256,-7.0702221],
            [107.4483123,-7.0709035],
            [107.4480548,-7.0714572],
            [107.4477114,-7.073757],
            [107.4466386,-7.0744384],
            [107.4463584,-7.0752077],
            [107.4469481,-7.0780651],
        ]])

    def kelurahanPanyocokan(self, nama):
        self.kelurahan.record(nama)
        self.kelurahan.poly([[
            [107.4350169,-7.100025],
            [107.4373361,-7.1005637],
            [107.4378082,-7.100223],
            [107.4401256,-7.1004785],
            [107.440469,-7.099712],
            [107.441456,-7.099499],
            [107.443001,-7.098477],
            [107.445533,-7.0982215],
            [107.4463913,-7.0984344],
            [107.4471208,-7.0980511],
            [107.4476787,-7.0985621],
            [107.4492237,-7.097753],
            [107.4500391,-7.0980511],
            [107.4508545,-7.0971994],
            [107.4507257,-7.0980085],
            [107.4512836,-7.1006489],
            [107.4509832,-7.1015858],
            [107.4524853,-7.1009044],
            [107.4544594,-7.1012877],
            [107.4557039,-7.1023523],
            [107.4583217,-7.1036299],
            [107.4608537,-7.1022246],
            [107.4623558,-7.1003508],
            [107.4640295,-7.098988],
            [107.4657032,-7.0988177],
            [107.4659178,-7.0981363],
            [107.4672052,-7.0975827],
            [107.4680206,-7.0958792],
            [107.4680206,-7.0944312],
            [107.4685785,-7.0947719],
            [107.4695656,-7.0939628],
            [107.4705097,-7.0941331],
            [107.4699518,-7.0908114],
            [107.4687931,-7.0893634],
            [107.4659607,-7.0900022],
            [107.4651453,-7.0900022],
            [107.4627849,-7.0882987],
            [107.4585363,-7.0873618],
            [107.4581501,-7.0859564],
            [107.4601242,-7.0849769],
            [107.4629137,-7.084551],
            [107.4628278,-7.083103],
            [107.4618735,-7.082232],
            [107.4567237,-7.0810821],
            [107.455617,-7.0795983],
            [107.4547587,-7.0824943],
            [107.4542437,-7.086242],
            [107.4453604,-7.0947914],
            [107.4400175,-7.0963617],
            [107.4398352,-7.0979135],
            [107.4386282,-7.098008],
            [107.4376814,-7.0991624],
            [107.4367788,-7.0989731],
            [107.4350169,-7.100025],
        ]])

    def kelurahanRawabogo(self, nama):
        self.kelurahan.record(nama)
        self.kelurahan.poly([[
            [107.418624,-7.0776392],
            [107.4204264,-7.0781503],
            [107.4198256,-7.0838571],
            [107.4228297,-7.0843681],
            [107.4248896,-7.0803649],
            [107.4267779,-7.079939],
            [107.428752,-7.0826646],
            [107.4308119,-7.0832608],
            [107.4323569,-7.081387],
            [107.4339877,-7.0810463],
            [107.4364767,-7.078491],
            [107.4402533,-7.0791724],
            [107.4428282,-7.0777244],
            [107.4425707,-7.081387],
            [107.4441157,-7.082835],
            [107.4457465,-7.0817277],
            [107.4469481,-7.0780651],
            [107.4463584,-7.0752077],
            [107.4466386,-7.0744384],
            [107.4477114,-7.073757],
            [107.4480548,-7.0714572],
            [107.4483123,-7.0709035],
            [107.4476256,-7.0702221],
            [107.4465098,-7.0710739],
            [107.4459948,-7.0707331],
            [107.4463811,-7.069924],
            [107.4451794,-7.0684759],
            [107.4455228,-7.0668149],
            [107.4446215,-7.0663465],
            [107.4441495,-7.066389],
            [107.4442353,-7.065665],
            [107.4437203,-7.0651965],
            [107.4441924,-7.0647281],
            [107.4435916,-7.0644299],
            [107.4444499,-7.0631097],
            [107.4444499,-7.0621301],
            [107.4448361,-7.061619],
            [107.443892,-7.0606394],
            [107.4441697,-7.0597052],
            [107.4447074,-7.0589784],
            [107.4448361,-7.0579563],
            [107.4437632,-7.0573174],
            [107.442862,-7.0564656],
            [107.4430766,-7.0558268],
            [107.4437203,-7.055486],
            [107.4432053,-7.0548472],
            [107.4434199,-7.0541657],
            [107.4441495,-7.0540806],
            [107.4440636,-7.0523769],
            [107.4442353,-7.0517807],
            [107.4454799,-7.0514825],
            [107.445909,-7.0505455],
            [107.4453082,-7.0497789],
            [107.4452653,-7.0506307],
            [107.4445357,-7.0509288],
            [107.443892,-7.0502048],
            [107.4437203,-7.0508437],
            [107.4419608,-7.0518233],
            [107.4402215,-7.0516556],
            [107.4394288,-7.0519084],
            [107.4389567,-7.0516529],
            [107.4384417,-7.052164],
            [107.4297648,-7.0549486],
            [107.4278336,-7.0553745],
            [107.4276191,-7.0572485],
            [107.4269324,-7.0575466],
            [107.4263745,-7.0571207],
            [107.4253445,-7.0570781],
            [107.4243146,-7.058441],
            [107.4236279,-7.0598465],
            [107.4216967,-7.0605705],
            [107.4205809,-7.0617204],
            [107.4212676,-7.0624444],
            [107.4203234,-7.0634666],
            [107.4207526,-7.0652979],
            [107.4199372,-7.0673422],
            [107.4208384,-7.068918],
            [107.4218255,-7.0710475],
            [107.421568,-7.0718993],
            [107.4214392,-7.0731343],
            [107.4219113,-7.0736028],
            [107.4221688,-7.0752638],
            [107.4216538,-7.0756897],
            [107.4203664,-7.0757748],
            [107.4189072,-7.0768821],
            [107.418624,-7.0776392],
        ]])

    def kelurahanSukawening(self, nama):
        self.kelurahan.record(nama)
        self.kelurahan.poly([[
            [107.4628278,-7.083103],
            [107.463743,-7.082478],
            [107.4658458,-7.0826058],
            [107.4663608,-7.0832446],
            [107.4666612,-7.0842667],
            [107.4671333,-7.0838409],
            [107.4689357,-7.0848204],
            [107.4695795,-7.0843519],
            [107.4700515,-7.0848204],
            [107.4715965,-7.0843945],
            [107.4724548,-7.0849907],
            [107.473871,-7.0845648],
            [107.4755447,-7.0855444],
            [107.4761026,-7.0849055],
            [107.4758451,-7.0842667],
            [107.4763172,-7.084139],
            [107.4773901,-7.0833724],
            [107.4788492,-7.0832446],
            [107.4799221,-7.0821373],
            [107.4805229,-7.0809875],
            [107.4800508,-7.0803061],
            [107.4807375,-7.0798376],
            [107.4797075,-7.0784322],
            [107.4792354,-7.079795],
            [107.4786346,-7.0791136],
            [107.4780338,-7.0794969],
            [107.4768751,-7.0796246],
            [107.4761455,-7.0789006],
            [107.4755447,-7.0796672],
            [107.4737852,-7.0792414],
            [107.4736564,-7.0785599],
            [107.4727981,-7.0784748],
            [107.4733131,-7.0774101],
            [107.472326,-7.0774952],
            [107.4715107,-7.0763453],
            [107.4710386,-7.0763879],
            [107.471339,-7.0773249],
            [107.4705236,-7.0774952],
            [107.4702232,-7.0766861],
            [107.4696224,-7.0767712],
            [107.4691503,-7.0763453],
            [107.4684208,-7.0762602],
            [107.4679058,-7.075238],
            [107.4708669,-7.0735771],
            [107.4752014,-7.0717884],
            [107.4766605,-7.0684664],
            [107.4767463,-7.0658685],
            [107.4752443,-7.0647611],
            [107.4757164,-7.0637816],
            [107.4801796,-7.0624613],
            [107.4800937,-7.0614817],
            [107.4809949,-7.0599485],
            [107.4806945,-7.0551784],
            [107.4790638,-7.0564987],
            [107.4766176,-7.0569672],
            [107.4726694,-7.0525804],
            [107.4704378,-7.0530063],
            [107.4691074,-7.0536877],
            [107.4663608,-7.0519415],
            [107.4652879,-7.0524952],
            [107.4638288,-7.0520267],
            [107.462713,-7.0521971],
            [107.460181,-7.051473],
            [107.4601381,-7.0524526],
            [107.4564435,-7.0519111],
            [107.4555423,-7.0534271],
            [107.455199,-7.0587935],
            [107.4544694,-7.0611359],
            [107.4547269,-7.062371],
            [107.4539544,-7.0658208],
            [107.4554136,-7.0700797],
            [107.4581601,-7.0751904],
            [107.4594047,-7.0741683],
            [107.4603917,-7.0740831],
            [107.4621083,-7.0744411],
            [107.4634185,-7.0764826],
            [107.4633997,-7.0770132],
            [107.4628606,-7.0778029],
            [107.4633756,-7.0790805],
            [107.4618735,-7.082232],
            [107.4628278,-7.083103],
        ]])

    def kelurahanCiwidey(self, nama):
        self.kelurahan.record(nama)
        self.kelurahan.poly([[
            [107.4583217,-7.1036299],
            [107.4557039,-7.1023523],
            [107.4544594,-7.1012877],
            [107.4524853,-7.1009044],
            [107.4509832,-7.1015858],
            [107.4512836,-7.1006489],
            [107.4507257,-7.0980085],
            [107.4508545,-7.0971994],
            [107.4500391,-7.0980511],
            [107.4492237,-7.097753],
            [107.4476787,-7.0985621],
            [107.4471208,-7.0980511],
            [107.4463913,-7.0984344],
            [107.445533,-7.0982215],
            [107.443001,-7.098477],
            [107.441456,-7.099499],
            [107.440469,-7.099712],
            [107.4401256,-7.1004785],
            [107.4378082,-7.100223],
            [107.4373361,-7.1005637],
            [107.4378064,-7.1006638],
            [107.4387505,-7.102495],
            [107.4392053,-7.1028488],
            [107.4406388,-7.1036448],
            [107.4417546,-7.1031763],
            [107.4421837,-7.102495],
            [107.4427845,-7.1026653],
            [107.443042,-7.1049649],
            [107.445617,-7.1047946],
            [107.4499514,-7.1027505],
            [107.4477198,-7.1053056],
            [107.4478915,-7.1058592],
            [107.447119,-7.1062851],
            [107.4477198,-7.1070516],
            [107.448621,-7.1058592],
            [107.4493935,-7.1065406],
            [107.4484923,-7.1075627],
            [107.4492218,-7.1078608],
            [107.4499514,-7.1073923],
            [107.4503806,-7.1082014],
            [107.4500802,-7.1087976],
            [107.4510243,-7.1090106],
            [107.4512818,-7.10999],
            [107.4520543,-7.10999],
            [107.4516251,-7.1106714],
            [107.4520543,-7.1113953],
            [107.4537106,-7.1100458],
            [107.4551698,-7.1080443],
            [107.456071,-7.1083424],
            [107.4571009,-7.1072351],
            [107.4574872,-7.1062557],
            [107.4587746,-7.1050633],
            [107.4583217,-7.1036299],
        ]])

    # Kantor Kelurahan
    def kantorDesaRawabogo(self, nama):
        self.kantor.record(nama)
        self.kantor.point(107.4449894,-7.0764887)

    def kantorDesaSukawening(self, nama):
        self.kantor.record(nama)
        self.kantor.point(107.4694392,-7.0780572)

    def kantorDesaLebakMuncang(self, nama):
        self.kantor.record(nama)
        self.kantor.point(107.4357456,-7.0968795)

    def kantorDesaNengkelan(self, nama):
        self.kantor.record(nama)
        self.kantor.point(107.4561278,-7.0765655)

    def kantorDesaCiwidey(self, nama):
        self.kantor.record(nama)
        self.kantor.point(107.4337255,-7.0984424)

    def kantorDesaPanyocokan(self, nama):
        self.kantor.record(nama)
        self.kantor.point(107.4652599,-7.0905498)

    def kantorDesaPanundaan(self, nama):
        self.kantor.record(nama)
        self.kantor.point(107.4431267,-7.113793)

    # Jalan
    def jalanLebakmuncang(self, nama):
        self.jalan.record(nama)
        self.jalan.line([[
          [107.4094056,-7.1452145],
          [107.408719,-7.144959],
          [107.4082898,-7.1451293],
          [107.4066591,-7.1443203],
          [107.4056291,-7.1450016],
          [107.4048995,-7.1445332],
          [107.402625,-7.1444054],
          [107.4017667,-7.1445758],
          [107.401123,-7.1444054],
          [107.4002647,-7.1450868],
          [107.3992776,-7.1445758],
          [107.3988055,-7.1440648],
          [107.3981618,-7.1437667],
          [107.3976468,-7.1430428],
          [107.3976039,-7.1417228],
          [107.3973035,-7.141084],
          [107.3996639,-7.140275],
          [107.4013376,-7.1398491],
          [107.401595,-7.139253],
          [107.4025821,-7.1388697],
          [107.4033461,-7.1386217],
          [107.4036979,-7.1368683],
          [107.4055003,-7.1366554],
          [107.4067878,-7.1352928],
          [107.4085902,-7.1349095],
          [107.4100923,-7.1348669],
          [107.4113368,-7.1329507],
          [107.412753,-7.13261],
          [107.4134397,-7.1321842],
          [107.4133538,-7.1314603],
          [107.4119806,-7.1310345],
          [107.4118518,-7.1261373],
          [107.4131822,-7.125456],
          [107.4142122,-7.1255838],
          [107.4155425,-7.1254986],
          [107.4160146,-7.1251153],
          [107.4198341,-7.1245192],
          [107.4197053,-7.1238804],
          [107.4194478,-7.1233268],
          [107.420392,-7.1223474],
          [107.4216365,-7.1208995],
          [107.4223661,-7.1193665],
          [107.4222802,-7.1181741],
          [107.4228381,-7.1150228],
          [107.4240398,-7.1104236],
          [107.4253272,-7.109359],
          [107.4258851,-7.1091035],
          [107.425456,-7.1085925],
          [107.4262284,-7.1065484],
          [107.4256276,-7.1068465],
          [107.424941,-7.1064206],
          [107.4250697,-7.1060799],
          [107.4257993,-7.1055689],
          [107.426443,-7.1054837],
          [107.4311637,-7.101651],
          [107.4339532,-7.0993939],
          [107.435584,-7.0974775],
          [107.4339532,-7.0923245],
          [107.4324941,-7.0911747],
          [107.4326228,-7.0903655],
          [107.4335241,-7.088875],
          [107.4337386,-7.0872566],
          [107.4330949,-7.0853402],
          [107.4326228,-7.0847014],
          [107.4339103,-7.0836793],
          [107.4353694,-7.0812092],
          [107.4365281,-7.0814221],
          [107.4358415,-7.0799741],
          [107.436571,-7.0796334],
        ]])
        
    def jalanRawaBogo(self, nama):
        self.jalan.record(nama)
        self.jalan.line([[
          [107.4437632,-7.0573174],
          [107.4428257,-7.0589606],
          [107.4434265,-7.0603235],
          [107.4429115,-7.0611327],
          [107.4432549,-7.0637733],
          [107.4435124,-7.0647954],
          [107.4424395,-7.0643695],
          [107.4417528,-7.0645825],
          [107.4403366,-7.0662435],
          [107.4392208,-7.0661583],
          [107.4382767,-7.0660731],
          [107.437633,-7.0664564],
          [107.4367747,-7.066712],
          [107.4357876,-7.0662435],
          [107.4348864,-7.0653917],
          [107.434586,-7.0660731],
          [107.4332985,-7.0670953],
          [107.4317536,-7.0678193],
          [107.4306378,-7.0676915],
          [107.4303803,-7.066499],
          [107.4282774,-7.0665416],
          [107.4279341,-7.0650084],
          [107.4289211,-7.0641992],
          [107.4293074,-7.0643695],
          [107.430509,-7.0637307],
          [107.4323544,-7.0640714],
          [107.4333414,-7.0643695],
          [107.4341997,-7.0637307],
          [107.4361738,-7.0623252],
          [107.4369463,-7.061516],
          [107.4366888,-7.0608772],
          [107.4374613,-7.0618993],
          [107.43862,-7.0615586],
          [107.4390062,-7.0609624],
          [107.4409804,-7.061729],
          [107.4425253,-7.0623252],
          [107.4420532,-7.0639436],
          [107.4399933,-7.0675212],
          [107.4418816,-7.0679896],
          [107.441667,-7.0701191],
        ]])

    def jalanNengkelan(self, nama):
        self.jalan.record(nama)
        self.jalan.line([[
          [107.4516243,-7.050129],
          [107.4505085,-7.0502994],
          [107.4493927,-7.0514919],
          [107.4457019,-7.0540474],
          [107.4468177,-7.0544733],
          [107.4489635,-7.0548992],
          [107.450251,-7.0551547],
          [107.4500793,-7.056688],
          [107.4510234,-7.0577101],
          [107.4512809,-7.0592434],
          [107.4527401,-7.059073],
          [107.4521392,-7.0602655],
          [107.4534267,-7.0612877],
          [107.45377,-7.0632468],
          [107.4538559,-7.0693797],
          [107.4518817,-7.0705722],
          [107.450251,-7.0715091],
          [107.4485343,-7.0727016],
          [107.4482769,-7.0744903],
          [107.4482769,-7.0766198],
          [107.4493068,-7.0773864],
          [107.4510234,-7.0767901],
          [107.4524826,-7.0769605],
          [107.4563449,-7.0769605],
          [107.458319,-7.075768],
          [107.4603917,-7.0740831],
          [107.4595207,-7.0769605],
          [107.4590915,-7.0783233],
          [107.4620098,-7.0811341],
        ]])

    def jalanSukawening(self, nama):
        self.jalan.record(nama)
        self.jalan.line([[
          [107.4621083,-7.0744411],
          [107.4639401,-7.0727596],
          [107.4645838,-7.0718652],
          [107.4649271,-7.0708431],
          [107.4650559,-7.0688414],
          [107.4649271,-7.0676489],
          [107.4646267,-7.0661157],
          [107.4637255,-7.0656046],
          [107.4624809,-7.0652639],
          [107.4625668,-7.0643695],
          [107.462438,-7.0634326],
          [107.4632105,-7.0627511],
          [107.4652275,-7.0628363],
          [107.4661717,-7.0627937],
          [107.4667725,-7.0629641],
          [107.466515,-7.0637307],
          [107.4684891,-7.0662009],
          [107.4687037,-7.0668823],
          [107.4699482,-7.067223],
          [107.4705919,-7.0650936],
          [107.4712357,-7.0641992],
          [107.470034,-7.06339],
          [107.4689612,-7.0627085],
          [107.468532,-7.0613883],
          [107.469047,-7.0607494],
          [107.4704203,-7.0612179],
          [107.4712357,-7.0607494],
          [107.4716219,-7.0613457],
          [107.4723086,-7.0609624],
          [107.4729523,-7.0612179],
          [107.4734673,-7.0629215],
          [107.4732956,-7.0641992],
          [107.4723086,-7.0652213],
          [107.4709782,-7.0660305],
          [107.4696049,-7.0669249],
          [107.4699053,-7.0691821],
          [107.470034,-7.0710561],
          [107.4692616,-7.0717375],
          [107.468532,-7.0723337],
          [107.463983,-7.0717375],
          [107.4636397,-7.0726318],
          [107.4681029,-7.0739947],
          [107.4678883,-7.0749316],
          [107.4689612,-7.0783813],
          [107.468532,-7.0794886],
          [107.469047,-7.0801274],
          [107.4681458,-7.0809366],
          [107.4671587,-7.0808088],
          [107.4668583,-7.0834919],
          [107.4689612,-7.0825549],
          [107.4696478,-7.0831086],
          [107.4702486,-7.0822994],
          [107.4720081,-7.0827253],
          [107.4731239,-7.0822994],
          [107.4734673,-7.0813625],
          [107.4727377,-7.0808514],
          [107.4712786,-7.0793608],
          [107.4706349,-7.0783387],
          [107.4694761,-7.0784239],
          [107.4699053,-7.0768055],
        ]])

    def jalanPanunadaan(self, nama):
        self.jalan.record(nama)
        self.jalan.line([[
          [107.4359702,-7.1165985],
          [107.4395322,-7.1132343],
          [107.4412917,-7.1118715],
          [107.4434375,-7.1141711],
          [107.4440812,-7.1153209],
          [107.444682,-7.1153635],
          [107.4465274,-7.1137027],
          [107.4512481,-7.1104237],
          [107.4491882,-7.1085073],
          [107.4468707,-7.106591],
          [107.4454974,-7.106378],
          [107.44421,-7.1098275],
          [107.4408197,-7.1100404],
          [107.439618,-7.1105514],
          [107.4337386,-7.1040358],
          [107.4330091,-7.1038229],
        ]])

    def jalanPanyocokan(self, nama):
        self.jalan.record(nama)
        self.jalan.line([[
          [107.461966,-7.0826998],
          [107.4593481,-7.083296],
          [107.4580177,-7.0841052],
          [107.4571594,-7.085255],
          [107.4566874,-7.0870437],
          [107.4555287,-7.0880232],
          [107.4541983,-7.0890879],
          [107.4530396,-7.0898119],
          [107.451795,-7.0903655],
          [107.4515804,-7.0910043],
          [107.4527821,-7.0916431],
          [107.4532541,-7.0929633],
          [107.4547133,-7.0930485],
          [107.4555287,-7.0921968],
          [107.4565157,-7.0918987],
          [107.4591335,-7.0905359],
          [107.4599489,-7.0906211],
          [107.4603352,-7.0901952],
          [107.4609789,-7.0903229],
          [107.4613222,-7.0899397],
          [107.4625668,-7.0901526],
          [107.4633392,-7.0894712],
          [107.4643263,-7.0897693],
          [107.4640688,-7.0905785],
          [107.466,-7.0904081],
          [107.4660429,-7.0912173],
          [107.4654421,-7.0928356],
          [107.4659142,-7.0973924],
          [107.4642834,-7.0980312],
          [107.4627813,-7.0971794],
          [107.4598631,-7.1014381],
          [107.458404,-7.1010974],
          [107.4572024,-7.1008419],
          [107.4567732,-7.1000327],
          [107.4547991,-7.1012677],
        ]])

    def jalanCiwidey(self, nama):
        self.jalan.record(nama)
        self.jalan.line([[
          [107.4520543,-7.10999],
          [107.4581679,-7.1050579],
          [107.4539193,-7.1039932],
          [107.4510439,-7.1031841],
          [107.4503573,-7.1037803],
          [107.4498852,-7.1036525],
          [107.4497994,-7.1044617],
          [107.4492844,-7.1049727],
          [107.4488982,-7.1050579],
        ]])

    def jalanRawaBogo2(self, nama):
        self.jalan.record(nama)
        self.jalan.line([[
          [107.441667,-7.0701191],
          [107.4433836,-7.06997],
          [107.4447569,-7.0709922],
          [107.4451861,-7.0727383],
          [107.4448427,-7.074527],
          [107.4433836,-7.0753788],
          [107.4429545,-7.0764435],
          [107.443684,-7.0772101],
          [107.4435982,-7.0786155],
          [107.4439844,-7.0792543],
          [107.4432549,-7.0803616],
          [107.4435124,-7.081767],
          [107.4432549,-7.0821503],
          [107.4435553,-7.0818522],
          [107.4433836,-7.0821503],
        ]])

    def close(self):
        self.kelurahan.close()
        self.kantor.close()
        self.jalan.close()
