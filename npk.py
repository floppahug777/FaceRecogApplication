#импортируем необходимые библиотеки
from os import *
import cv2
from PIL import Image, ImageDraw
from tkinter import *
import mediapipe as mp
'''
direct = 'E:\\npk_FFP\videos\\'
files = listdir(direct)
print(files)
'''
'''
window = Tk()
window.title("Application Defender++ Max Online No Ads")

lbl = Label(window, text="Приветствуем вас в приложении A.D.M.O.N.A.", font=("Arial Bold", 20))
lbl.grid(column=0, row=0)
lbl = Label(window, text="Для начала работы потребуется считать ваше лицо,", font=("Arial Bold", 20))
lbl.grid(column=1, row=0)
lbl = Label(window, text="для этого нажмите кнопку ниже", font=("Arial Bold", 20))
lbl.grid(column=2, row=0)

window.geometry('400x250')
window.mainloop()

'''
'''
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+'data/haarcascades/haarcascade_frontalface_default.xml')
image = cv2.imread('example')
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow('rezult', image_gray)
cv2.waitKey(0)
'''
'''
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+'data/haarcascades/haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)

while True:
    sucess, image = cap.read()
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(image_gray, 1.1, 19)
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
    
    cv2.imshow('rezult', image)
    cv2.waitKey()
'''
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)
while True:
    ret, img = cap.read()
    img_f_disp = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    faces = face_cascade.detectMultiScale(img_f_disp, scaleFactor=1.05, minNeighbors=5) #список координат получается
    for (x, y, wi, he) in faces:
        cv2.rectangle(img, (x, y), (x + wi, y + he), (0,0,255), 5)
    cv2.imshow('CAM', img)
    cv2.waitKey()
    #if cv2.waitKey(10) == 27:
        #break
#cap.release()
#cv2.destroyAllWindows()
