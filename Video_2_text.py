import cv2 as cv 
import numpy as np
import math
import time

beg=time.time()
def readimg (xmin,xmax,ymin,ymax):
   ymins=ymin 
   n=(xmax-xmin+1)*(ymax-ymin+1)*21.25
   target=0
   while xmin<xmax :
        while ymin<ymax :
            target = target+img[xmin,ymin]
            ymin += 1
        xmin += 1
        ymin=ymins
   target=math.floor(target/n)
   return target

def basicTransform(input):
    dictionary=['鑪','罚','朋','同','团','田','口','厂','十','一','、','。','，']
    goal=dictionary[input]

    return goal

def imageTransform(xCharN,yCharN):
    xStep = size[1]/xCharN 
    yStep = size[0]/yCharN
    print(xStep,yStep)
    i=0
    j=0
    finalstr=''
    while i < size[0]:
        while j < size[1] :
            finalstr=finalstr+basicTransform(readimg(math.ceil(i),math.ceil(i+xStep),math.ceil(j),math.ceil(j+yStep)))
            j=j+xStep
        i=i+yStep
        j=0
    return finalstr

def textwrite(name,msg):
    file_path = 'D:/TestFiles/'
    full_path = file_path + name + '.txt'
    file = open(full_path,'w')
    file.write(msg)
    file.close()
    print('Done')
number=10000
while number <=13595:
    print(number)
    img = cv.imread("D:/[WPF]JJDown/Download/rua/"+str(number)+".jpg",cv.IMREAD_GRAYSCALE)
    size=np.shape(img)
    print (size)
    text = imageTransform(157,77)
    textwrite(str(number),text)
    number+=1

end=time.time()
runTime=beg-end
print(runTime)