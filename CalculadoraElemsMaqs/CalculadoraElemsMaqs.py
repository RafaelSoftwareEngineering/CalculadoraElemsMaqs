import sys
import PySide6
from PySide6 import QtWidgets, QtGui, QtCore
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *



class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculadora Elementos de Máquinas v1.0")
        self.setGeometry(150, 75, 1280, 720)
        self.setWindowIcon(QIcon("gear-icon-vector"))
        self.setStyleSheet("background-color: rgb(51, 51, 53)")
        #space for function calls
        self.MWSkeleton()
        self.MWSceneanView()
        self.LinhaofTempo()
        self.MainWindowBtns()
        self.show()


#########################################################################
#MainWindow:
    def MWSkeleton (self):

        self.LabelTtl = QLabel("Calculadora de Elementos de Máquinas", self)
        self.LabelTtl.setFont(QFont("Arial", 20, 8, True))
        self.LabelTtl.move(350, 10)
        self.LabelTtl.setStyleSheet("color: rgb(17, 11, 26)")
        self.LabelInfo1 = QLabel("Escolha o Elemento:", self)
        self.LabelInfo1.setFont(QFont("Arial", 16, 2, True))
        self.LabelInfo1.setStyleSheet("color: rgb(17, 11, 26)")
        self.LabelInfo1.move(800, 70)

#MainWindow Scene and View
    def MWSceneanView (self):

        self.CenaMain = QGraphicsScene(self)
        #pixmaps prep:
        self.pixmap1 = QGraphicsPixmapItem(QPixmap("engine"))
        self.pixmap1.setFlag(QGraphicsItem.ItemIsMovable)
        self.pixmap1.setScale(0.26)

        self.pixmap2 = QGraphicsPixmapItem(QPixmap("chave-parafuso"))
        self.pixmap2.setFlag(QGraphicsItem.ItemIsMovable)
        self.pixmap2.setScale(0.4)

        self.thehammer = QGraphicsPixmapItem(QPixmap("thor-hammer-icon"))
        self.thehammer.setFlag(QGraphicsItem.ItemIsMovable)
        self.thehammer.setScale(0.4)

        self.sparkpix = QGraphicsPixmapItem(QPixmap("sparky"))
        self.sparkpix.setScale(0.5)

        self.planepix = QGraphicsPixmapItem(QPixmap("plane"))
        self.planepix.setFlag(QGraphicsItem.ItemIsMovable)
        self.planepix.setScale(0.8)

        self.shippix = QGraphicsPixmapItem(QPixmap("cargoship"))
        self.shippix.setFlag(QGraphicsItem.ItemIsMovable)
        self.shippix.setScale(1.0)

        self.gearpix = QGraphicsPixmapItem(QPixmap("gear-icon-vector"))
        self.gearpix.setFlag(QGraphicsItem.ItemIsMovable)
        self.gearpix.setScale(0.1)

        self.enginepic = QGraphicsPixmapItem(QPixmap("enginewallpaper"))
        self.enginepic.setFlag(QGraphicsItem.ItemIsMovable)
        self.enginepic.setScale(0.05)

        self.trainpix = QGraphicsPixmapItem(QPixmap("trainpic"))
        self.trainpix.setFlag(QGraphicsItem.ItemIsMovable)
        self.trainpix.setScale(0.2)

        self.furnacepix = QGraphicsPixmapItem(QPixmap("furnace"))
        self.furnacepix.setFlag(QGraphicsItem.ItemIsMovable)
        self.furnacepix.setScale(0.7)

        self.naviopix = QGraphicsPixmapItem(QPixmap("cargoshippic"))
        self.naviopix.setFlag(QGraphicsItem.ItemIsMovable)
        self.naviopix.setScale(0.4)

        self.aviaopix = QGraphicsPixmapItem(QPixmap("planepic"))
        self.aviaopix.setFlag(QGraphicsItem.ItemIsMovable)
        self.aviaopix.setScale(0.12)

        self.Titulopix = QGraphicsPixmapItem(QPixmap("tituloELM"))
        self.Titulopix.setFlag(QGraphicsItem.ItemIsMovable)
        self.Titulopix.setScale(0.1)


        self.CenaMain.addItem(self.pixmap1)
        self.CenaMain.addItem(self.pixmap2)
        self.CenaMain.addItem(self.thehammer)
        self.CenaMain.addItem(self.sparkpix)
        self.CenaMain.addItem(self.planepix)
        self.CenaMain.addItem(self.shippix)
        self.CenaMain.addItem(self.gearpix)
        self.CenaMain.addItem(self.enginepic)
        self.CenaMain.addItem(self.trainpix)
        self.CenaMain.addItem(self.furnacepix)
        self.CenaMain.addItem(self.naviopix)
        self.CenaMain.addItem(self.aviaopix)
        self.CenaMain.addItem(self.Titulopix)

        #logic test:
        def MWView (self):
            self.MainView = QGraphicsView(self.CenaMain, self)
            self.MainView.setGeometry(0, 45, 500, 675)
        MWView(self)


############################AnimationSection(MainWindow)#################################


    def LinhaofTempo (self):
        #def timeline and timer

        self.linha = QTimeLine(70000)
        self.linha.setFrameRange(0, 20000)
        self.linha.setLoopCount(3)

        def reloginho (self):

            self.timer = QTimer()
            self.timer.isSingleShot()

        reloginho(self) #call timer

        #MainWindow anims, animation1:

        def Anime (self):

            self.animenation = QGraphicsItemAnimation(self)
            self.animenation.setTimeLine(self.linha)
            self.animenation.setItem(self.pixmap1)
            self.animenation.setPosAt(0.0, QPointF(150.0, 480.0))
            self.animenation.setRotationAt(0.0001, -5)
            self.animenation.setRotationAt(0.00015, 0)
            self.animenation.setRotationAt(0.00022, -5)
            self.animenation.setRotationAt(0.00027, 0)
            self.animenation.setRotationAt(0.00035, -5)
            self.animenation.setRotationAt(0.00045, 0)
            self.animenation.setRotationAt(0.00052, -5)
            self.animenation.setRotationAt(0.00060, 0)
            self.animenation.setRotationAt(0.00075, -5)
            self.animenation.setRotationAt(0.00085, 0)
            self.animenation.setRotationAt(0.00092, -5)
            self.animenation.setRotationAt(0.001, 0)
            self.animenation.setPosAt(0.0012, QPointF(150.0, 520.0))
            self.animenation.setPosAt(0.0014, QPointF(150, 600.0))
            self.animenation.setPosAt(0.0017, QPointF(150, 800))

        #animation2:
        
        def Ani2 (self):

            self.animation2 = QGraphicsItemAnimation(self)
            self.animation2.setTimeLine(self.linha)
            self.animation2.setItem(self.pixmap2)
            self.animation2.setPosAt(0.0, QPointF(-150.0, 170.0))
            self.animation2.setRotationAt(0.0, -33.0)
            self.animation2.setPosAt(0.0003, QPointF(-180.0, 100.0))
            self.animation2.setRotationAt(0.0004, -3.0)
            self.animation2.setPosAt(0.0004, QPointF(-180.0, 70.0))
            self.animation2.setPosAt(0.00041, QPointF(-180.0, 50.0))
            self.animation2.setPosAt(0.0007, QPointF(-150.0, 170.0))
            self.animation2.setRotationAt(0.0007, -33.0)
            self.animation2.setPosAt(0.0008, QPointF(-180.0, 100.0))
            self.animation2.setRotationAt(0.0008, -3.0)
            self.animation2.setPosAt(0.0008, QPointF(-180.0, 70.0))
            self.animation2.setPosAt(0.00081, QPointF(-180.0, 50.0))
            self.animation2.setPosAt(0.00091, QPointF(-150.0, 170.0))
            self.animation2.setRotationAt(0.00091, -33.0)
            self.animation2.setPosAt(0.00096, QPointF(-180.0, 100.0))
            self.animation2.setRotationAt(0.00097, -3.0)
            self.animation2.setPosAt(0.00098, QPointF(-180.0, 70.0))
            self.animation2.setPosAt(0.0010, QPointF(-180.0, 50.0))
            self.animation2.setPosAt(0.0012, QPointF(-140.0, 10.0))
            self.animation2.setPosAt(0.0014, QPointF(-90, -80))
            self.animation2.setPosAt(0.0017, QPointF(-90, -250))


        #animation3(the hammer):

        def HammerAni (self):

            self.hammerAnim = QGraphicsItemAnimation(self)
            self.hammerAnim.setTimeLine(self.linha)
            self.hammerAnim.setItem(self.thehammer)
            self.hammerAnim.setPosAt(0.0, QPointF(420.0, 300.0))
            self.hammerAnim.setRotationAt(0.0, -160.0)
            self.hammerAnim.setRotationAt(0.00015, -100.0)
            self.hammerAnim.setPosAt(0.00016, QPointF(320.0, 350.0))
            self.hammerAnim.setPosAt(0.0003, QPointF(420.0, 300.0))
            self.hammerAnim.setRotationAt(0.0003, -160.0)
            self.hammerAnim.setRotationAt(0.00035, -100.0)
            self.hammerAnim.setPosAt(0.00036, QPointF(320.0, 350.0))
            self.hammerAnim.setPosAt(0.0006, QPointF(420.0, 300.0))
            self.hammerAnim.setRotationAt(0.0006, -160.0)
            self.hammerAnim.setRotationAt(0.00065, -100.0)
            self.hammerAnim.setPosAt(0.00066, QPointF(320.0, 350.0))
            self.hammerAnim.setPosAt(0.00090, QPointF(420.0, 300.0))
            self.hammerAnim.setRotationAt(0.00090, -160.0)
            self.hammerAnim.setRotationAt(0.0010, -100.0)
            self.hammerAnim.setPosAt(0.0010, QPointF(320.0, 350.0))
            self.hammerAnim.setPosAt(0.0012, QPointF(360.0, 350.0))
            self.hammerAnim.setPosAt(0.0014, QPointF(420.0, 380))
            self.hammerAnim.setPosAt(0.0017, QPointF(580, 380))

        #animation4:

        def SparkAni (self):

            self.sparkanim = QGraphicsItemAnimation(self)
            self.sparkanim.setTimeLine(self.linha)
            self.sparkanim.setItem(self.sparkpix)
            self.sparkanim.setPosAt(0.0, QPointF(385.0, 198.0))
            self.sparkanim.setPosAt(0.000155, QPointF(385.0, 198.0))
            self.sparkanim.setPosAt(0.00016, QPointF(385.0, 210.0))
            self.sparkanim.setPosAt(0.00017, QPointF(385.0, 200.0))
            self.sparkanim.setPosAt(0.000355, QPointF(385.0, 198.0))
            self.sparkanim.setPosAt(0.00036, QPointF(385.0, 210.0))
            self.sparkanim.setPosAt(0.00037, QPointF(385.0, 200.0))
            self.sparkanim.setPosAt(0.000655, QPointF(385.0, 198.0))
            self.sparkanim.setPosAt(0.00066, QPointF(385.0, 210.0))
            self.sparkanim.setPosAt(0.00067, QPointF(385.0, 200.0))
            self.sparkanim.setPosAt(0.000955, QPointF(385.0, 198.0))
            self.sparkanim.setPosAt(0.0010, QPointF(385.0, 210.0))
            self.sparkanim.setPosAt(0.0010, QPointF(385.0, 200.0))
            self.sparkanim.setPosAt(0.0012, QPointF(410.0, 200.0))
            self.sparkanim.setPosAt(0.0014, QPointF(500.0, 200))

        #animation5:

        def PlaneAni (self):

            self.planeanimation = QGraphicsItemAnimation(self)
            self.planeanimation.setTimeLine(self.linha)
            self.planeanimation.setItem(self.planepix)
            self.planeanimation.setPosAt(0.0, QPointF(40.0, 320.0))
            self.planeanimation.setRotationAt(0.0, 90.0)
            self.planeanimation.setPosAt(0.0001, QPointF(150, 320))
            self.planeanimation.setPosAt(0.0002, QPointF(260, 320))
            self.planeanimation.setPosAt(0.0003, QPointF(450, 320))
            self.planeanimation.setPosAt(0.0004, QPointF(690, 320))
            
        #animation6:

        def ShipAni (self):

            self.shipanimation = QGraphicsItemAnimation(self)
            self.shipanimation.setTimeLine(self.linha)
            self.shipanimation.setItem(self.shippix)
            self.shipanimation.setPosAt(0.0, QPointF(500.0, 320))
            self.shipanimation.setPosAt(0.0004, QPointF(500.0, 320))
            self.shipanimation.setPosAt(0.0005, QPointF(400, 320))
            self.shipanimation.setPosAt(0.00065, QPointF(300, 320))
            self.shipanimation.setPosAt(0.0008, QPointF(180, 310))
            self.shipanimation.setPosAt(0.0009, QPointF(40, 320))
            self.shipanimation.setPosAt(0.0010, QPointF(-120, 320))
            self.shipanimation.setPosAt(0.0012, QPointF(-160, 320))
            self.shipanimation.setPosAt(0.0014, QPointF(-250, 320))

        #animation7:

        def GearAni (self):

            self.gearanimation1 = QGraphicsItemAnimation(self)
            self.gearanimation1.setTimeLine(self.linha)
            self.gearanimation1.setItem(self.gearpix)
            self.gearanimation1.setPosAt(0.0, QPointF(300.0, 20.0))
            self.gearanimation1.setRotationAt(0.001, 25)
            self.gearanimation1.setPosAt(0.00009, QPointF(315.0, 13.0))
            self.gearanimation1.setRotationAt(0.0002, 50)
            self.gearanimation1.setPosAt(0.00019, QPointF(330.0, 10.0))
            self.gearanimation1.setRotationAt(0.0003, 75)
            self.gearanimation1.setPosAt(0.00029, QPointF(345.0, 15.0))
            self.gearanimation1.setRotationAt(0.0004, 90)
            self.gearanimation1.setPosAt(0.00039, QPointF(355.0, 20.0))
            self.gearanimation1.setRotationAt(0.0005, 105)
            self.gearanimation1.setPosAt(0.00049, QPointF(360.0, 30.0))
            self.gearanimation1.setRotationAt(0.0006, 145)
            self.gearanimation1.setPosAt(0.00059, QPointF(365.0, 55.0))
            self.gearanimation1.setRotationAt(0.0007, 190)
            self.gearanimation1.setPosAt(0.00069, QPointF(340.0, 80.0))
            self.gearanimation1.setRotationAt(0.0008, 240)
            self.gearanimation1.setPosAt(0.00079, QPointF(320.0, 82.0))
            self.gearanimation1.setRotationAt(0.0010, 360)
            self.gearanimation1.setPosAt(0.00099, QPointF(305.0, 35.0))
            self.gearanimation1.setPosAt(0.0012, QPointF(305.0, 10.0))
            self.gearanimation1.setPosAt(0.0014, QPointF(305.0, -50))

        #animation8:

        def Pic1Ani (self):

            self.engineanim = QGraphicsItemAnimation(self)
            self.engineanim.setTimeLine(self.linha)
            self.engineanim.setItem(self.enginepic)
            self.engineanim.setPosAt(0.0, QPointF(0.0, 0.0))
            self.engineanim.setScaleAt(0.0, 0.1, 0.1)
            self.engineanim.setPosAt(0.0012, QPointF(100, 100))
            self.engineanim.setPosAt(0.00125, QPointF(200, 200))
            self.engineanim.setScaleAt(0.00129, 0.1, 0.1)
            self.engineanim.setScaleAt(0.0014, 0.35, 0.35)
            self.engineanim.setPosAt(0.0014, QPointF(260, 260))
            self.engineanim.setScaleAt(0.0017, 0.55, 0.55)
            self.engineanim.setScaleAt(0.0019, 1.2, 1.2)
            self.engineanim.setPosAt(0.0021, QPointF(240, 240))
            self.engineanim.setScaleAt(0.0034, 2.2, 2.2)
            self.engineanim.setPosAt(0.0033, QPointF(180, 180))
            self.engineanim.setScaleAt(0.0047, 4.4, 4.4)
            self.engineanim.setPosAt(0.0047, QPointF(90, 130))
            self.engineanim.setPosAt(0.0048, QPointF(40, 130))
            self.engineanim.setScaleAt(0.0048, 6.2, 6.2)
            self.engineanim.setPosAt(0.00520, QPointF(20, 80))
            self.engineanim.setScaleAt(0.0540, 7.1, 7.1)
            self.engineanim.setPosAt(0.0140, QPointF(0, 20))
            self.engineanim.setScaleAt(0.0160, 8, 8)
            self.engineanim.setPosAt(0.0160, QPointF(-30, 15))
            self.engineanim.setScaleAt(0.0190, 8, 8)
            self.engineanim.setPosAt(0.0190, QPointF(-30, 15))
            self.engineanim.setScaleAt(0.0210, 8, 8)
            self.engineanim.setPosAt(0.0210, QPointF(-30, 15))
            self.engineanim.setPosAt(0.0225, QPointF(-888, -888))
            self.engineanim.setPosAt(0.77, QPointF(-888, -888))
            self.engineanim.setPosAt(0.79, QPointF(-38, 22))

        #animation9

        def Trainn (self):

            self.trainanim = QGraphicsItemAnimation(self)
            self.trainanim.setTimeLine(self.linha)
            self.trainanim.setItem(self.trainpix)
            self.trainanim.setPosAt(0.0, QPointF(600, 0))
            self.trainanim.setPosAt(0.0225, QPointF(600, 0))
            self.trainanim.setPosAt(0.0232, QPointF(100, 200))
            self.trainanim.setScaleAt(0.0238, 1.4, 1.4)
            self.trainanim.setPosAt(0.025, QPointF(30, 150))
            self.trainanim.setScaleAt(0.025, 1.9, 1.9)
            self.trainanim.setScaleAt(0.04, 3.1, 3.1)
            self.trainanim.setPosAt(0.04, QPointF(-150, -50))
            self.trainanim.setScaleAt(0.048, 4, 4)
            self.trainanim.setPosAt(0.048, QPointF(-290, -160))
            self.trainanim.setPosAt(0.052, QPointF(-320, -200))
            self.trainanim.setPosAt(0.07, QPointF(-500, -200))
            self.trainanim.setPosAt(0.088, QPointF(-770, -200))
            self.trainanim.setPosAt(0.095, QPointF(-1500, -600))

        #animation10:

        def FurnAn (self):

            self.fornonimation = QGraphicsItemAnimation(self)
            self.fornonimation.setTimeLine(self.linha)
            self.fornonimation.setItem(self.furnacepix)
            self.fornonimation.setPosAt(0.0, QPointF(-800, -600))
            self.fornonimation.setPosAt(0.095, QPointF(-800, -600))
            self.fornonimation.setPosAt(0.1, QPointF(100.0, 100.0))
            self.fornonimation.setScaleAt(0.1, 1.4, 1.4)
            self.fornonimation.setPosAt(0.125, QPointF(30, 130))
            self.fornonimation.setScaleAt(0.125, 1.9, 1.9)
            self.fornonimation.setPosAt(0.150, QPointF(-90, -20))
            self.fornonimation.setScaleAt(0.150, 2.3, 2.3)
            self.fornonimation.setPosAt(0.170, QPointF(-90, -20))
            self.fornonimation.setScaleAt(0.170, 2.3, 2.3)
            self.fornonimation.setPosAt(0.175, QPointF(-600, -20))
            self.fornonimation.setPosAt(0.180, QPointF(-980, -20))

        #animation11:

        def NavioAni (self):

            self.navionimation = QGraphicsItemAnimation(self)
            self.navionimation.setTimeLine(self.linha)
            self.navionimation.setItem(self.naviopix)
            self.navionimation.setPosAt(0.0, QPointF(-800, -600))
            self.navionimation.setPosAt(0.180, QPointF(-800, -600))
            self.navionimation.setPosAt(0.185, QPointF(-20.0, -20.0))
            self.navionimation.setScaleAt(0.186, 1.4, 1.4)
            self.navionimation.setPosAt(0.2, QPointF(20, 20))
            self.navionimation.setScaleAt(0.2, 1.9, 1.9)
            self.navionimation.setPosAt(0.225, QPointF(-20, 20))
            self.navionimation.setPosAt(0.250, QPointF(-50, 20))
            self.navionimation.setPosAt(0.275, QPointF(-80, 20))
            self.navionimation.setPosAt(0.3, QPointF(-110, 20))
            self.navionimation.setPosAt(0.325, QPointF(-140, 20))
            self.navionimation.setPosAt(0.350, QPointF(-170, 20))
            self.navionimation.setPosAt(0.375, QPointF(-200, 20))
            self.navionimation.setPosAt(0.400, QPointF(-230, 20))
            self.navionimation.setPosAt(0.410, QPointF(-1200, 20))

        #animation12:

        def AviaoAni (self):

            self.aviaoani = QGraphicsItemAnimation(self)
            self.aviaoani.setTimeLine(self.linha)
            self.aviaoani.setItem(self.aviaopix)
            self.aviaoani.setPosAt(0.0, QPointF(-800, -500))
            self.aviaoani.setPosAt(0.410, QPointF(-800, -500))
            self.aviaoani.setPosAt(0.415, QPointF(0, 0))
            self.aviaoani.setScaleAt(0.445, 1.8, 1.8)
            self.aviaoani.setPosAt(0.485, QPointF(-200, 0))
            self.aviaoani.setScaleAt(0.485, 2.4, 2.4)
            self.aviaoani.setPosAt(0.5, QPointF(-300, 20))
            self.aviaoani.setScaleAt(0.530, 2.0, 2.0)
            self.aviaoani.setPosAt(0.560, QPointF(0, 20))
            self.aviaoani.setPosAt(0.570, QPointF(-1200, 20))

        #animation12:

        def TituloAni (self):

            self.tituloani = QGraphicsItemAnimation(self)
            self.tituloani.setTimeLine(self.linha)
            self.tituloani.setItem(self.Titulopix)
            self.tituloani.setPosAt(0.0, QPointF(800, 0))
            self.tituloani.setPosAt(0.570, QPointF(800, 0))
            self.tituloani.setScaleAt(0.575, 9, 9)
            self.tituloani.setPosAt(0.576, QPointF(650, 0))
            self.tituloani.setPosAt(0.77, QPointF(-1100, 0))
            self.tituloani.setPosAt(0.85, QPointF(-2000, 0))

        #animations finalization: 
           
        Anime(self)
        Ani2(self)
        HammerAni(self)
        SparkAni(self)
        PlaneAni(self)
        ShipAni(self)
        GearAni(self)
        Pic1Ani(self)
        Trainn(self)
        FurnAn(self)
        NavioAni(self)
        AviaoAni(self)
        TituloAni(self)
        #TimelineCall:
        self.linha.start()

#############################################################################
#Main-Window Buttons:

    def MainWindowBtns (self):

        self.GearsBtn = QPushButton("Cálculo de Engrenagens", self)
        self.GearsBtn.setFont(QFont("Arial", 20, 8, True))
        self.GearsBtn.setStyleSheet("color: rgb(17, 11, 26)")
        self.GearsBtn.setIcon(QIcon("gear-icon-vector"))  
        self.GearsBtn.setIconSize(QSize(40, 40))
        self.GearsBtn.move(515, 140)
        self.GearsBtn.clicked.connect(self.CreateNewWin)

        self.ParafBtn = QPushButton("Cálculo de Parafusos", self)
        self.ParafBtn.setFont(QFont("Arial", 20, 8, True))
        self.ParafBtn.setStyleSheet("color: rgb(17, 11, 26)")
        self.ParafBtn.setIcon(QIcon("ParafusoIcon"))
        self.ParafBtn.setIconSize(QSize(40, 40))
        self.ParafBtn.move(915, 140)
        self.ParafBtn.clicked.connect(self.CreateScrewWindow)

        self.RoscaBtn = QPushButton("Cálculo de Roscas", self)
        self.RoscaBtn.setFont(QFont("Arial", 20, 8, True))
        self.RoscaBtn.setStyleSheet("color: rgb(17, 11, 26)")
        self.RoscaBtn.setIcon(QIcon("roscaIcon"))
        self.RoscaBtn.setIconSize(QSize(40, 40))
        self.RoscaBtn.move(525, 240)
        self.RoscaBtn.clicked.connect(self.CreateRosca)

        self.MolasBtn = QPushButton("Cálculo de Molas", self)
        self.MolasBtn.setFont(QFont("Arial", 20, 8, True))
        self.MolasBtn.setStyleSheet("color: rgb(17 ,11, 26)")
        self.MolasBtn.setIcon(QIcon("MolaIcon"))
        self.MolasBtn.setIconSize(QSize(55, 55))
        self.MolasBtn.move(915, 240)
        self.MolasBtn.clicked.connect(self.CreateMolaW)

        self.EixoBtn = QPushButton("Cálculo de Eixos", self)
        self.EixoBtn.setFont(QFont("Arial", 20, 8, True))
        self.EixoBtn.setStyleSheet("color: rgb(17, 11, 26)")
        self.EixoBtn.setIcon(QIcon("eixoIcon"))
        self.EixoBtn.setIconSize(QSize(50, 50))
        self.EixoBtn.move(520, 340)
        self.EixoBtn.clicked.connect(self.CreateEixo)

        self.SoldaBtn = QPushButton("Cálculo de Solda", self)
        self.SoldaBtn.setFont(QFont("Arial", 20, 8, True))
        self.SoldaBtn.setStyleSheet("color: rgb(17, 11, 26)")
        self.SoldaBtn.setIcon(QIcon("SoldaIcon"))
        self.SoldaBtn.setIconSize(QSize(61, 61))
        self.SoldaBtn.move(915, 340)
        self.SoldaBtn.clicked.connect(self.CreateSolda)

        self.PorcasBtn = QPushButton("Cálculo de Porcas", self)
        self.PorcasBtn.setFont(QFont("Arial", 20, 8, True))
        self.PorcasBtn.setStyleSheet("color: rgb(17, 11, 26)")
        self.PorcasBtn.setIcon(QIcon("PorcasIcon"))
        self.PorcasBtn.setIconSize(QSize(40, 40))
        self.PorcasBtn.move(520, 440)
        self.PorcasBtn.clicked.connect(self.CreatePorcas)

        self.MancaisBtn = QPushButton("Cálculo de Mancais", self)
        self.MancaisBtn.setFont(QFont("Arial", 20, 8, True))
        self.MancaisBtn.setStyleSheet("color: rgb(17, 11, 26)")
        self.MancaisBtn.setIcon(QIcon("mancalIcon"))
        self.MancaisBtn.setIconSize(QSize(61, 61))
        self.MancaisBtn.move(915, 440)
        self.MancaisBtn.clicked.connect(self.CreateMancais)

        self.CaboBtn = QPushButton("Cálculo de Cabos de Aço", self)
        self.CaboBtn.setFont(QFont("Arial", 20, 8, True))
        self.CaboBtn.setStyleSheet("color: rgb(17, 11, 26)")
        self.CaboBtn.setIcon(QIcon("CaboAlma"))
        self.CaboBtn.setIconSize(QSize(50, 50))
        self.CaboBtn.move(515, 540)
        self.CaboBtn.clicked.connect(self.CreateCabo)

        self.ChaveBtn = QPushButton("Cálculo de Chavetas", self)
        self.ChaveBtn.setFont(QFont("Arial", 20, 8, True))
        self.ChaveBtn.setStyleSheet("color: rgb(17, 11, 26)")
        self.ChaveBtn.setIcon(QIcon("chavetaIcon"))
        self.ChaveBtn.setIconSize(QSize(55, 55))
        self.ChaveBtn.move(920, 540)
        self.ChaveBtn.clicked.connect(self.CreateChave)
        
        

#gears Window:

    def CreateNewWin (self):
        self.GearsWindow = QWidget()
        self.GearsWindow.setGeometry(150, 150, 1280, 650)
        self.GearsWindow.setStyleSheet("background-color: rgb(51, 51, 53)")
        self.GearsWindow.setWindowTitle("Seção das Engrenagens")
        self.GearsWindow.setWindowIcon(QIcon("gear-icon-vector"))
        #space for function calls:
        self.MWSk()
        self.SomaFields()
        self.GearsWindowViewandScene()
        self.timeofGears()
        self.GearsWindow.show()

#gears window functions and more:

    def GearsWindowViewandScene (self):
        
        self.SceneGears = QGraphicsScene(self.GearsWindow)
        #pixmaps prep:
        self.GPix1 = QGraphicsPixmapItem(QPixmap("beaugears"))
        self.GPix1.setFlag(QGraphicsItem.ItemIsMovable)
        self.GPix1.setScale(0.2)

        self.G2Pix = QGraphicsPixmapItem(QPixmap("gearbefore"))
        self.G2Pix.setFlag(QGraphicsItem.ItemIsMovable)
        self.G2Pix.setScale(0.3)

        self.g3Pix = QGraphicsPixmapItem(QPixmap("gearafter"))
        self.g3Pix.setFlag(QGraphicsItem.ItemIsMovable)
        self.g3Pix.setScale(0.28)

        self.g5pix = QGraphicsPixmapItem(QPixmap("gears1"))
        self.g5pix.setFlag(QGraphicsItem.ItemIsMovable)
        self.g5pix.setScale(0.3)

        self.gear2pix = QGraphicsPixmapItem(QPixmap("gears2"))
        self.gear2pix.setFlag(QGraphicsItem.ItemIsMovable)
        self.gear2pix.setScale(0.3)

        self.gears3pix = QGraphicsPixmapItem(QPixmap("gears3"))
        self.gears3pix.setFlag(QGraphicsItem.ItemIsMovable)
        self.gears3pix.setScale(0.0)

        self.g4pix = QGraphicsPixmapItem(QPixmap("gears4"))
        self.g4pix.setFlag(QGraphicsItem.ItemIsMovable)
        self.g4pix.setScale(0.5)

        self.grwpix = QGraphicsPixmapItem(QPixmap("gears5"))
        self.grwpix.setFlag(QGraphicsItem.ItemIsMovable)
        self.grwpix.setScale(0.1)

        self.g6pix = QGraphicsPixmapItem(QPixmap("gears6"))
        self.g6pix.setFlag(QGraphicsItem.ItemIsMovable)
        self.g6pix.setScale(0.25)

        #pix add:
        self.SceneGears.addItem(self.GPix1)
        self.SceneGears.addItem(self.G2Pix)
        self.SceneGears.addItem(self.g3Pix)
        self.SceneGears.addItem(self.g5pix)
        self.SceneGears.addItem(self.gear2pix)
        self.SceneGears.addItem(self.gears3pix)
        self.SceneGears.addItem(self.g4pix)
        self.SceneGears.addItem(self.grwpix)
        self.SceneGears.addItem(self.g6pix)

        def GearsWinView(self):
            self.GearsView = QGraphicsView(self.SceneGears, self.GearsWindow)
            self.GearsView.setGeometry(0, 0, 500, 650)
        GearsWinView(self)

    def MWSk (self):

        self.LabelT = QLabel("Calculadora de Elementos de Máquinas", self.GearsWindow)
        self.LabelT.move(600, 0)
#def timeline and timer:
    def timeofGears(self):

        self.lineGears = QTimeLine(70000, self.GearsWindow)
        self.lineGears.setFrameRange(0, 20000)
        self.lineGears.setLoopCount(2)

        def GearsTimerfunc(self):
            self.Geartimer = QTimer()
            self.Geartimer.isSingleShot()

        GearsTimerfunc(self)

        #def animations:
        #ani1:
        def GAnime1 (self):

            self.g1ani = QGraphicsItemAnimation(self.GearsWindow)
            self.g1ani.setTimeLine(self.lineGears)
            self.g1ani.setItem(self.GPix1)
            self.g1ani.setPosAt(0.0, QPointF(0.0, 0.0))
            self.g1ani.setScaleAt(0.0015, 1.9, 1.9)
            self.g1ani.setPosAt(0.0016, QPointF(0.0, 0.0))
            self.g1ani.setPosAt(0.0040, QPointF(-300.0, 0.0))
            self.g1ani.setPosAt(0.110, QPointF(-1400.0, 0.0))

        #ani2:

        def GA2nime (self):

            self.g2ani = QGraphicsItemAnimation(self.GearsWindow)
            self.g2ani.setTimeLine(self.lineGears)
            self.g2ani.setItem(self.G2Pix)
            self.g2ani.setPosAt(0.0, QPointF(1200.0, 0.0))
            self.g2ani.setPosAt(0.0044, QPointF(1200.0, 0.0))
            self.g2ani.setPosAt(0.0045, QPointF(0.0, 0.0))
            self.g2ani.setScaleAt(0.0050, 1.7, 1.7)
            self.g2ani.setScaleAt(0.0055, 2.3, 2.3)
            self.g2ani.setScaleAt(0.0065, 3.0, 3.0)
            self.g2ani.setPosAt(0.0085, QPointF(-150.0, 0.0))
            self.g2ani.setPosAt(0.01, QPointF(-300.0, 0.0))
            self.g2ani.setPosAt(0.011, QPointF(-1200.0, 0.0))

        #ani3:

        def G3Ani (self):

            self.g3anim = QGraphicsItemAnimation(self.GearsWindow)
            self.g3anim.setTimeLine(self.lineGears)
            self.g3anim.setItem(self.g3Pix)
            self.g3anim.setPosAt(0.0, QPointF(800, 200))
            self.g3anim.setPosAt(0.011, QPointF(800, 200))
            self.g3anim.setPosAt(0.013, QPointF(0.0, 300))
            self.g3anim.setScaleAt(0.012, 1.0, 1.0)
            self.g3anim.setScaleAt(0.0132, 1.8, 1.8)
            self.g3anim.setScaleAt(0.015, 3.0, 3.0)
            self.g3anim.setPosAt(0.02, QPointF(0.0, 0.0))
            self.g3anim.setPosAt(0.043, QPointF(-350.0, 0.0))
            self.g3anim.setPosAt(0.094,QPointF(-1450, 0))

        #ani4:

        def G4Ani (self):

            self.g4ani = QGraphicsItemAnimation(self.GearsWindow)
            self.g4ani.setTimeLine(self.lineGears)
            self.g4ani.setItem(self.g5pix)
            self.g4ani.setPosAt(0.0, QPointF(800, 200))
            self.g4ani.setPosAt(0.053, QPointF(800, 200))
            self.g4ani.setPosAt(0.055, QPointF(0.0, 200.0))
            self.g4ani.setScaleAt(0.075, 2.5, 2.5)
            self.g4ani.setPosAt(0.075, QPointF(0.0, 50.0))
            self.g4ani.setScaleAt(0.095, 3.7, 3.7)
            self.g4ani.setPosAt(0.095, QPointF(-50.0, -10.0))
            self.g4ani.setPosAt(0.110, QPointF(-300, -10.0))
            self.g4ani.setPosAt(0.130, QPointF(-700.0, -10.0))
            self.g4ani.setPosAt(0.175, QPointF(-1600.0, -10.0))

        def gears5Ani (self):

            self.g5ani = QGraphicsItemAnimation(self.GearsWindow)
            self.g5ani.setTimeLine(self.lineGears)
            self.g5ani.setItem(self.gear2pix)
            self.g5ani.setPosAt(0.0, QPointF(800, 200))
            self.g5ani.setPosAt(0.110, QPointF(800, 200))
            self.g5ani.setPosAt(0.121, QPointF(0, 0))
            self.g5ani.setScaleAt(0.150, 1.6, 1.6)
            self.g5ani.setScaleAt(0.170, 3.6, 3.6)
            self.g5ani.setPosAt(0.171, QPointF(0, 0))
            self.g5ani.setPosAt(0.210, QPointF(-350, 0))
            self.g5ani.setPosAt(0.250, QPointF(-1200.0, 0))

        def gears6Ani (self):

            self.g6ani = QGraphicsItemAnimation(self.GearsWindow)
            self.g6ani.setTimeLine(self.lineGears)
            self.g6ani.setItem(self.gears3pix)
            self.g6ani.setPosAt(0.0, QPointF(800, 200))
            self.g6ani.setPosAt(0.248, QPointF(800.0, 200.0))
            self.g6ani.setPosAt(0.255, QPointF(0.0, 0.0))
            self.g6ani.setScaleAt(0.275, 2.2, 2.2)
            self.g6ani.setPosAt(0.32, QPointF(-300.0, 0.0))
            self.g6ani.setPosAt(0.45, QPointF(-1800.0, 0.0))

        def g7Ani (self):

            self.g7ani = QGraphicsItemAnimation(self.GearsWindow)
            self.g7ani.setTimeLine(self.lineGears)
            self.g7ani.setItem(self.g4pix)
            self.g7ani.setPosAt(0.0, QPointF(1200.0, 800))
            self.g7ani.setPosAt(0.28, QPointF(0.0, 0.0))
            self.g7ani.setScaleAt(0.30, 1.8, 1.8)
            self.g7ani.setPosAt(0.30, QPointF(0.0, 0.0))
            self.g7ani.setScaleAt(0.32, 2.5, 2.5)
            self.g7ani.setPosAt(0.37, QPointF(-420, -10))
            self.g7ani.setPosAt(0.41, QPointF(-1200, -10))

        def g8Ani (self):

            self.g8Ani = QGraphicsItemAnimation(self.GearsWindow)
            self.g8Ani.setTimeLine(self.lineGears)
            self.g8Ani.setItem(self.grwpix)
            self.g8Ani.setPosAt(0.0, QPointF(800.0, -350.0))
            self.g8Ani.setPosAt(0.35, QPointF(800.0, -350.0))
            self.g8Ani.setPosAt(0.38, QPointF(0.0, 0.0))
            self.g8Ani.setScaleAt(0.38, 2.0, 2.0)
            self.g8Ani.setScaleAt(0.4, 4.0, 4.0)
            self.g8Ani.setPosAt(0.45, QPointF(-450.0, 0.0))
            self.g8Ani.setPosAt(0.5, QPointF(-900.0, 0.0))
            self.g8Ani.setPosAt(0.55, QPointF(-1350.0, 0.0))

        def g9ani (self):

            self.g9ani = QGraphicsItemAnimation(self.GearsWindow)
            self.g9ani.setTimeLine(self.lineGears)
            self.g9ani.setItem(self.g6pix)
            self.g9ani.setPosAt(0.0, QPointF(800, -200))
            self.g9ani.setPosAt(0.55, QPointF(800, -200))
            self.g9ani.setPosAt(0.56, QPointF(0.0, 0.0))
            self.g9ani.setScaleAt(0.6, 3.5, 3.5)
            self.g9ani.setPosAt(0.8, QPointF(-250.0, -250.0))
            self.g9ani.setPosAt(0.98, QPointF(-650, -300.0))

        #animations finalization:
        GAnime1(self)
        GA2nime(self)
        G3Ani(self)
        G4Ani(self)
        gears5Ani(self)
        gears6Ani(self)
        g7Ani(self)
        g8Ani(self)
        g9ani(self)
        self.lineGears.start()


#test:

    def SomaFields (self):

        self.field1 = QLineEdit("teste", self.GearsWindow)
        self.field1.move(600, 20)
        self.field2 = QLineEdit("teste2", self.GearsWindow)
        self.field2.move(750, 20)
        self.Calcular = QPushButton("soma", self.GearsWindow)
        self.Calcular.move(600, 50)
        self.Calcular.clicked.connect(self.TesteSoma)
        #test:
        self.Butao = QPushButton("teste3", self.GearsWindow)
        self.Butao.move(760, 90)
        self.Butao.clicked.connect(self.WindowInWindow)

    def WindowInWindow (self):

        self.Windowisidewindow = QWidget()
        self.testLabel()
        self.Windowisidewindow.show()

    def TesteSoma (self):

        self.Input1 = self.field1.text()
        self.Input2 = self.field2.text()
        self.a = float(self.Input1)
        self.b = float(self.Input2)
        self.res = self.a + self.b
        self.ResultadoField = QLabel("teste" , self.GearsWindow)
        self.ResultadoField.setText(str(self.res))
        self.ResultadoField.move(75, 80)
        self.ResultadoField.show()
        
    def testLabel (self):

        self.testeeeee = QLabel("teste", self.Windowisidewindow)

#########################ScrewsWindow########################################

    def CreateScrewWindow (self):

        self.ScrewWindow = QWidget()
        self.ScrewWindow.setGeometry(150, 150, 1280, 650)
        self.ScrewWindow.setStyleSheet("background-color: rgb(51, 51, 53)")
        self.ScrewWindow.setWindowTitle("Seção dos Parafusos")
        self.ScrewWindow.setWindowIcon(QIcon("ParafusoIcon"))
        self.testeeeee2 = QLabel("teste2", self.ScrewWindow)
        #space for function calls
        self.ScrewSceneandView()
        self.ScrewLine()

        self.ScrewWindow.show()

    def ScrewSceneandView (self):

        self.ParafScene = QGraphicsScene(self.ScrewWindow)
        #pixmap prep
        self.Ppix1 = QGraphicsPixmapItem(QPixmap("screwhist1"))
        self.Ppix1.setFlag(QGraphicsItem.ItemIsMovable)
        self.Ppix1.setScale(0.5)

        self.PPix2 = QGraphicsPixmapItem(QPixmap("screwhist2"))
        self.PPix2.setFlag(QGraphicsItem.ItemIsMovable)
        self.PPix2.setScale(0.3)

        self.PPix3 = QGraphicsPixmapItem(QPixmap("screwhist3"))
        self.PPix3.setFlag(QGraphicsItem.ItemIsMovable)
        self.PPix3.setScale(0.3)

        self.PPix4 = QGraphicsPixmapItem(QPixmap("screwhist4"))
        self.PPix4.setFlag(QGraphicsItem.ItemIsMovable)
        self.PPix4.setScale(0.3)

        self.PPIx5 = QGraphicsPixmapItem(QPixmap("screwhist5"))
        self.PPIx5.setFlag(QGraphicsItem.ItemIsMovable)
        self.PPIx5.setScale(0.3)

        self.PPix6 = QGraphicsPixmapItem(QPixmap("screwhist6"))
        self.PPix6.setFlag(QGraphicsItem.ItemIsMovable)
        self.PPix6.setScale(0.4)

        self.PPix7 = QGraphicsPixmapItem(QPixmap("screwhist7"))
        self.PPix7.setFlag(QGraphicsItem.ItemIsMovable)
        self.PPix7.setScale(0.4)
        

        self.PPix8 = QGraphicsPixmapItem(QPixmap("screwhist8"))
        self.PPix8.setFlag(QGraphicsItem.ItemIsMovable)
        self.PPix8.setScale(0.3)



        #pix add
        self.ParafScene.addItem(self.Ppix1)
        self.ParafScene.addItem(self.PPix2)
        self.ParafScene.addItem(self.PPix3)
        self.ParafScene.addItem(self.PPix4)
        self.ParafScene.addItem(self.PPIx5)
        self.ParafScene.addItem(self.PPix6)
        self.ParafScene.addItem(self.PPix7)
        self.ParafScene.addItem(self.PPix8)


        #view def
        def ScrewWindowView (self):

            ParafView = QGraphicsView(self.ParafScene, self.ScrewWindow)
            ParafView.setGeometry(0, 0, 500, 650)

        ScrewWindowView(self)

#def timeline and timer:

    def ScrewLine (self):

        self.linhaparaf = QTimeLine(70000, self.ScrewWindow)
        self.linhaparaf.setFrameRange(0, 20000)
        self.linhaparaf.setLoopCount(0)
        def ScrewTimer (self):
            self.parafusotimer = QTimer()
            self.parafusotimer.isSingleShot()
        ScrewTimer(self)
        #def animations:
        #ani1:

        def SAnim1 (self):

            self.sani1 = QGraphicsItemAnimation(self.ScrewWindow)
            self.sani1.setTimeLine(self.linhaparaf)
            self.sani1.setItem(self.Ppix1)
            self.sani1.setPosAt(0.0, QPointF(32.0, 0.0))
            self.sani1.setPosAt(0.02, QPointF(-750, 0.0))

        def SAnim2 (self):

            self.sani2 = QGraphicsItemAnimation(self.ScrewWindow)
            self.sani2.setTimeLine(self.linhaparaf)
            self.sani2.setItem(self.PPix2)
            self.sani2.setPosAt(0.0, QPointF(1000.0, 0.0))
            self.sani2.setScaleAt(0.0155, 2.1, 2.1)
            self.sani2.setPosAt(0.02, QPointF(0.0, 0.0))
            self.sani2.setPosAt(0.04, QPointF(-1000.0, 0.0))

        def SAnim3 (self):

            self.sani3 = QGraphicsItemAnimation(self.ScrewWindow)
            self.sani3.setTimeLine(self.linhaparaf)
            self.sani3.setItem(self.PPix3)
            self.sani3.setPosAt(0.0, QPointF(1500.0, 0.0))
            self.sani3.setScaleAt(0.025, 2.5, 2.5)
            self.sani3.setPosAt(0.04, QPointF(0.0, 0.0))
            self.sani3.setPosAt(0.06, QPointF(-1100.0, 0.0))

        def SAnim4 (self):

            self.sani4 = QGraphicsItemAnimation(self.ScrewWindow)
            self.sani4.setTimeLine(self.linhaparaf)
            self.sani4.setItem(self.PPix4)
            self.sani4.setPosAt(0.0, QPointF(1500.0, 0.0))
            self.sani4.setScaleAt(0.035, 3.0, 3.0)
            self.sani4.setPosAt(0.065, QPointF(200.0, 0.0))
            self.sani4.setPosAt(0.095, QPointF(-1300.0, 0.0))

        def SAnim5 (self):

            self.sani5 = QGraphicsItemAnimation(self.ScrewWindow)
            self.sani5.setTimeLine(self.linhaparaf)
            self.sani5.setItem(self.PPIx5)
            self.sani5.setPosAt(0.0, QPointF(1500.0, 0.0))
            self.sani5.setScaleAt(0.07, 2.8, 2.8)
            self.sani5.setPosAt(0.099, QPointF(500.0, 0.0))
            self.sani5.setPosAt(0.15, QPointF(-500.0, 0.0))
            self.sani5.setPosAt(0.2, QPointF(-1800.0, 0.0))

        def SAnim6 (self):

            self.sani6 = QGraphicsItemAnimation(self.ScrewWindow)
            self.sani6.setTimeLine(self.linhaparaf)
            self.sani6.setItem(self.PPix6)
            self.sani6.setPosAt(0.0, QPointF(1000.0, 0.0))
            self.sani6.setPosAt(0.14, QPointF(850.0, 0.0))
            self.sani6.setScaleAt(0.145, 2.1, 2.1)
            self.sani6.setPosAt(0.2, QPointF(0.0, 0.0))
            self.sani6.setPosAt(0.23, QPointF(-100.0, 0.0))
            self.sani6.setPosAt(0.28, QPointF(-1500.0, 0.0))

        def ScrewAnim7 (self):

            self.sani7 = QGraphicsItemAnimation(self.ScrewWindow)
            self.sani7.setTimeLine(self.linhaparaf)
            self.sani7.setItem(self.PPix7)
            self.sani7.setPosAt(0.0, QPointF(1800.0, 0.0))
            self.sani7.setPosAt(0.028, QPointF(1800.0, 0.0))
            self.sani7.setScaleAt(0.32, 1.55, 1.55)
            self.sani7.setPosAt(0.33, QPointF(0.0, 0.0))
            self.sani7.setPosAt(0.35, QPointF(-1500.0, 0.0))

        def ScrAni8 (self):

            self.sani8 = QGraphicsItemAnimation(self.ScrewWindow)
            self.sani8.setTimeLine(self.linhaparaf)
            self.sani8.setItem(self.PPix8)
            self.sani8.setPosAt(0.0, QPointF(1500.0, 0.0))
            self.sani8.setScaleAt(0.35, 2.7, 2.7)
            self.sani8.setPosAt(0.034, QPointF(1500.0, 0.0))
            self.sani8.setPosAt(0.35, QPointF(800.0, 0.0))
            self.sani8.setPosAt(0.365, QPointF(100.0, 0.0))
            self.sani8.setPosAt(0.49, QPointF(-1400.0, 0.0))


        #animations finalization:
        SAnim1(self)
        SAnim2(self)
        SAnim3(self)
        SAnim4(self)
        SAnim5(self)
        SAnim6(self)
        ScrewAnim7(self)
        ScrAni8(self)
        self.linhaparaf.start()


#########################RoscaWindow########################################

    def CreateRosca (self):

        self.RoscaWindow = QWidget()
        self.RoscaWindow.setGeometry(150, 150, 1280, 650)
        self.RoscaWindow.setStyleSheet("background-color: rgb(51, 51, 53)")
        self.RoscaWindow.setWindowTitle("Seção das Roscas")
        self.RoscaWindow.setWindowIcon(QIcon("roscaIcon"))
        self.testeeeee2 = QLabel("teste2", self.RoscaWindow)
        #space for function calls
        self.RoscaSceneandView()

        self.RoscaWindow.show()

    def RoscaSceneandView (self):

        self.RScene = QGraphicsScene(self.RoscaWindow)
        #pixmap prep

        #pix add

        #view def
        def RScanVi (self):

            self.RView = QGraphicsView(self.RScene, self.RoscaWindow)
            self.RView.setGeometry(0, 0, 500, 650)

        RScanVi(self)


#########################MolaWindow########################################

    def CreateMolaW (self):

        self.molaWindow = QWidget()
        self.molaWindow.setGeometry(150, 150, 1280, 650)
        self.molaWindow.setStyleSheet("background-color: rgb(51, 51, 53)")
        self.molaWindow.setWindowTitle("Seção das Molas")
        self.molaWindow.setWindowIcon(QIcon("MolaIcon"))
        self.testeeeee2 = QLabel("teste2", self.molaWindow)
        #space for function calls
        self.MoSceneandView()

        self.molaWindow.show()

    def MoSceneandView (self):

        self.MolaScene = QGraphicsScene(self.molaWindow)
        #pixmap prep

        #pix add

        #view def
        def MolView (self):

            MolaView = QGraphicsView(self.MolaScene, self.molaWindow)
            MolaView.setGeometry(0, 0, 500, 650)

        MolView(self)


#########################PorcasWindow########################################

    def CreatePorcas (self):

        self.PorcasWindow = QWidget()
        self.PorcasWindow.setGeometry(150, 150, 1280, 650)
        self.PorcasWindow.setStyleSheet("background-color: rgb(51, 51, 53)")
        self.PorcasWindow.setWindowTitle("Seção das Porcas")
        self.PorcasWindow.setWindowIcon(QIcon("PorcasIcon"))
        self.testeeeee2 = QLabel("teste2", self.PorcasWindow)
        #space for function calls
        self.PorScanView()

        self.PorcasWindow.show()

    def PorScanView (self):

        self.Porscene = QGraphicsScene(self.PorcasWindow)
        #pixmap prep

        #pix add

        #view def
        def PorcView (self):

            self.PorcaViewVar = QGraphicsView(self.Porscene, self.PorcasWindow)
            self.PorcaViewVar.setGeometry(0, 0, 500, 650)

        PorcView(self)


#########################EixoWindow########################################

    def CreateEixo (self):

        self.EixoWindow = QWidget()
        self.EixoWindow.setGeometry(150, 150, 1280, 650)
        self.EixoWindow.setStyleSheet("background-color: rgb(51, 51, 53)")
        self.EixoWindow.setWindowTitle("Seção dos Eixos")
        self.EixoWindow.setWindowIcon(QIcon("roscaIcon"))
        self.testeeeee2 = QLabel("teste2", self.EixoWindow)
        #space for function calls
        self.EixoSceneandView()

        self.EixoWindow.show()

    def EixoSceneandView (self):

        self.EixoScene = QGraphicsScene(self.EixoWindow)
        #pixmap prep

        #pix add

        #view def
        def EixoViewf (self):

            self.EixoView = QGraphicsView(self.EixoScene, self.EixoWindow)
            self.EixoView.setGeometry(0, 0, 500, 650)

        EixoViewf(self)


#########################ChaveWindow########################################

    def CreateChave (self):

        self.ChaveWindow = QWidget()
        self.ChaveWindow.setGeometry(150, 150, 1280, 650)
        self.ChaveWindow.setStyleSheet("background-color: rgb(51, 51, 53)")
        self.ChaveWindow.setWindowTitle("Seção das Chavetas")
        self.ChaveWindow.setWindowIcon(QIcon("chavetaIcon"))
        self.testeeeee2 = QLabel("teste2", self.ChaveWindow)
        #space for function calls

        self.ChaveWindow.show()


#########################SoldaWindow########################################

    def CreateSolda (self):

        self.SoldaWindow = QWidget()
        self.SoldaWindow.setGeometry(150, 150, 1280, 650)
        self.SoldaWindow.setStyleSheet("background-color: rgb(51, 51, 53)")
        self.SoldaWindow.setWindowTitle("Seção da Solda")
        self.SoldaWindow.setWindowIcon(QIcon("SoldaIcon"))
        self.testeeeee2 = QLabel("teste2", self.SoldaWindow)
        #space for function calls

        self.SoldaWindow.show()


#########################MancaisWindow########################################

    def CreateMancais (self):

        self.MancaisWindow = QWidget()
        self.MancaisWindow.setGeometry(150, 150, 1280, 650)
        self.MancaisWindow.setStyleSheet("background-color: rgb(51, 51, 53)")
        self.MancaisWindow.setWindowTitle("Seção dos Macais")
        self.MancaisWindow.setWindowIcon(QIcon("mancalIcon"))
        self.testeeeee2 = QLabel("teste2", self.MancaisWindow)
        #space for function calls

        self.MancaisWindow.show()


#########################CaboWindow########################################

    def CreateCabo (self):

        self.CaboWindow = QWidget()
        self.CaboWindow.setGeometry(150, 150, 1280, 650)
        self.CaboWindow.setStyleSheet("background-color: rgb(51, 51, 53)")
        self.CaboWindow.setWindowTitle("Seção dos Cabos")
        self.CaboWindow.setWindowIcon(QIcon("CaboAlma"))
        self.testeeeee2 = QLabel("teste2", self.CaboWindow)
        #space for function calls

        self.CaboWindow.show()



 
############################Ending###########################################


if __name__ == "__main__":
    app = QApplication([])
    janela = MainWindow()
    sys.exit(app.exec_())