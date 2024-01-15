import random
import cv2
import numpy as np

class image:
    def __init__(self,fileName,nameWindow):
        self.__fileName=fileName
        self.__nameWindow=nameWindow
        self.__img=cv2.imread(fileName)#אובייקט מסוג התמונה
        #self.__generator = self.affect_iterator()
        # mouse event
        #cv2.setMouseCallback(nameWindow, self.affect)
        self.positionImg()
        self.__original = self.__img  # שומר את תמונת המקור

    #מיקום וגודל החלון
    def positionImg(self):
        height,width,channels=self.__img.shape
        height=int(height*80/100)
        width=int(width*80/100)
        dim=(width,height)
        self.__img=cv2.resize(self.__img,dim)
        cv2.imshow(self.__nameWindow,self.__img)

    #properties
    @property
    def img(self):
        return self.__img

    @img.setter
    def img(self, i):
        self.__img = i

    @property
    def nameWindow(self):
        return self.__nameWindow

    @nameWindow.setter
    def name_windows(self, i):
        self.__nameWindow = i

    #################
    # #עיבודים על התמונה

    # def affect(self, event, x, y, flags, param):
    #     if event == cv2.EVENT_LBUTTONUP:
    #         next(self.__generator)
    #
    # def affect_iterator(self):
    #     global img2
    #     while True:
    #         # grey
    #         img1 = self.__img
    #         img2 = self.__img = cv2.cvtColor(self.__img, cv2.COLOR_RGB2GRAY)
    #         cv2.imshow(self.__nameWindow, self.__img)
    #         self.__img = img1
    #         yield
    #         # edges-
    #         # מציאת קצוות של התמונה
    #         img1 = self.__img
    #         img2 = self.__img = cv2.Canny(self.__img, 50, 300)
    #         cv2.imshow(self.__nameWindow, self.__img)
    #         self.__img = img1
    #         yield
    #         # erusion
    #         img1 = self.__img
    #         mask = np.ones((10, 10), np.uint8)
    #         img2 = self.__img = cv2.erode(self.__img, mask, iterations=1)
    #         cv2.imshow(self.__nameWindow, self.__img)
    #         self.__img = img1
    #         yield
    #         # delution
    #         img1 = self.__img
    #         img2 = self.__img = cv2.dilate(self.__img, mask, iterations=1)
    #         cv2.imshow(self.__nameWindow, self.__img)
    #         self.__img = img1
    #         yield

#חיתוך או ציור
    def getType(self,typ):
        global shapeDraw
        shapeDraw=typ
        cv2.setMouseCallback(self.__nameWindow,self.drawOrCut)

    def drawOrCut(self, event, x, y, flags, param):
        global ix, iy, drawing
        if event==cv2.EVENT_LBUTTONDOWN:
            drawing = True
            ix = x
            iy = y
        elif event == cv2.EVENT_LBUTTONUP:
            drawing = False
            if shapeDraw == "circle":
                cv2.circle(self.__img, (ix, iy), max(abs(x - ix), abs(y - iy)), (179 ,222 ,255), 3)
                cv2.imshow(self.__nameWindow, self.__img)
            if shapeDraw== "rectangle":
                cv2.rectangle(self.__img, (ix, iy), (x, y), (0, 140, 255), 3)
                cv2.imshow(self.__nameWindow, self.__img)
            if shapeDraw == "line":
                cv2.line(self.__img, (ix, iy), (x, y), (0, 69 ,255), 8, cv2.LINE_AA)
                cv2.imshow(self.__nameWindow, self.__img)
            if shapeDraw=='triangular':
                p1 = (ix,iy)
                p2 = (x, y)
                p3 = (x + 150, y + 20)
                cv2.line(self.__img, p1, p2, (255, 255, 255), 8)
                cv2.line(self.__img, p2, p3, (255, 255, 255), 8)
                cv2.line(self.__img, p1, p3, (255, 255, 255), 8)
                cv2.imshow(self.__nameWindow, self.__img)
            if shapeDraw=="cut":
                #cv2.rectangle(self.__img, (ix, iy), (x, y), (255, 100, 0),1)
                self.__img = self.__img[iy:y, ix:x]
                #self.__original=self.__img
                cv2.imshow(self.__nameWindow, self.__img)

    # add text
    def putText(self,event,x,y,param,txt='noText'):
        global ix,iy,writing
        writing = True
        if event==cv2.EVENT_LBUTTONDOWN:
                writing=False
                ix=x
                iy=y
        #elif  event == cv2.EVENT_LBUTTONUP:
                cv2.putText(self.__img,txt,(ix, iy), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,2, (147, 112, 219), 4)
                cv2.imshow(self.__nameWindow,self.__img)



    #-----------filters----------
    #filter1
    def filterBlack(self):
        img2 = self.__img = cv2.cvtColor(self.__img, cv2.COLOR_RGB2GRAY)
        cv2.imshow(self.name_windows, self.__img)
        self.__img = img2
    #filter2
    def filterSharpen(self):
        kernel=np.array([[-1,-1,-1],[-1,9.5,-1],[-1,-1,-1]])
        img2=self.img=cv2.filter2D(self.__img,-1,kernel)
        cv2.imshow(self.name_windows, img2)
        self.__img = img2
    #filter3
    def filterInvert(self):
        img2 = cv2.bitwise_not(self.__img)
        cv2.imshow(self.nameWindow,img2)
        self.__img = img2
    #filter4
    def filterSepia(self):
        img2 = np.array(self.__img, dtype=np.float64)
        img2 = cv2.transform(img2, np.matrix([[0.272, 0.534, 0.131],
                                                        [0.349, 0.686, 0.168],
                                                        [0.393, 0.769,
                                                         0.189]]))
        img2[np.where(img2 > 255)] = 255
        img2 = np.array(img2, dtype=np.uint8)
        cv2.imshow(self.__nameWindow, img2)
        self.__img = img2
    #filter5
    def filterBlur(self):
        img2 = cv2.blur(self.__img, (10, 10))
        cv2.imshow(self.__nameWindow, img2)
        self.__img = img2
    #filter6
    def filterEmboss(self):
        kernel = np.array([[0, -1, -1],
                            [1, 0, -1],
                            [1, 1, 0]])
        img2= cv2.filter2D(self.__img, -1, kernel)
        cv2.imshow(self.__nameWindow, img2)
        self.__img = img2
    #filter7
    def filterRotate(self):
        h, w = self.__img.shape[:2]
        ratio = 800 / w
        dim = (800, int(h * ratio))
        center = (w // 2, h // 2)
        matrix = cv2.getRotationMatrix2D(center, -20, 1.0)
        rotated = cv2.warpAffine(self.__img, matrix, (w, h))
        self.__img=rotated
        cv2.imshow(self.__nameWindow,self.__img)
    #none filter
    def noneFilter(self):
        self.__img=self.__original
        cv2.imshow(self.__nameWindow, self.__img)
    #frame:
    def frame(self):
        self.__img = cv2.copyMakeBorder(self.__img, 10, 10, 10, 10, cv2.BORDER_CONSTANT, None, value=(
        random.randint(0, 255), random.randint(0, 255),random.randint(0, 255)))
        cv2.imshow(self.__nameWindow, self.__img)




#מופע מסוג מחלקת תמונה בשביל הצגת תמונה לדוגמה
# image1=image("Image.jpg","Photo Designer")
# img2=image1.img
