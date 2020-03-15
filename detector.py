import tkinter as tk
from tkinter import messagebox


import numpy as np
from cv2 import imshow, waitKey, destroyAllWindows, namedWindow, imwrite, VideoCapture


import shutil
import os


from PIL import ImageTk, Image
from imageai.Detection import ObjectDetection

import pyttsx3



def detect():
    detector = ObjectDetection()

    model_path = "C:/Users/Prayag/PycharmProjects/Detector/models/resnet50_coco_best_v2.0.1.h5"
    input_path = "C:/Users/Prayag/PycharmProjects/Detector/input/img1.png"
    output_path = "C:/Users/Prayag/PycharmProjects/Detector/output/img.png"
    detector.setModelTypeAsRetinaNet()
    detector.setModelPath(model_path)
    detector.loadModel()
    detection = detector.detectObjectsFromImage(input_image=input_path, output_image_path=output_path, minimum_percentage_probability=50)
    for eachItem in detection:
        print(eachItem["name"], " : ", eachItem["percentage_probability"], ":", eachItem["box_points"])
    st = ""
    for x in detection:
        st = st + str(x["name"]) + " "
    print(st)



    engine=pyttsx3.init()
    engine.setProperty('rate',150)
    engine.say("List of objects from your left to right are as follows ")
    engine.setProperty('rate',130)
    final_st = st
    engine.say(final_st)
    engine.runAndWait()



def speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        engine3=pyttsx3.init()
        engine3.setProperty('rate',120)
        engine3.say("Say hello to utilise!")
        engine3.runAndWait()
        print("Detecting...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    print(r.recognize_google(audio))
    if 'hello' in r.recognize_google(audio):
        cam = VideoCapture(0)

        namedWindow("test")

        img_counter = 0

        while True:
            ret, frame = cam.read()
            imshow("test", frame)
            if not ret:
                break
            img_name = "img1.png".format(img_counter)
            imwrite(img_name, frame)
            print("{} written!".format(img_name))
            break
            k = waitKey(1)

            if k % 256 == 27:
                # ESC pressed
                print("Escape hit, closing...")
                break
            elif k % 256 == 32:
                # SPACE pressed
                img_name = "img1.png".format(img_counter)
                imwrite(img_name, frame)
                print("{} written!".format(img_name))
                break
                img_counter += 1

        cam.release()

        destroyAllWindows()
        detect()


    elif sr.RequestError:
        print("Error")
    elif sr.UnknownValueError:
        print("Error")
    else:
        print("Voice not recognised .Try again")


if __name__ == "__main__":

    r= tk.Tk()
    r.geometry("400x400")

    r.title("Start")

    engine2=pyttsx3.init()
    engine2.setProperty('rate',150)
    engine2.say("Hello")
    engine2.setProperty('rate',130)
    engine2.say("Hope you're doing well!")
    engine2.runAndWait()

    img = ImageTk.PhotoImage(Image.open(r"C:\Users\Prayag\PycharmProjects\Detector\mic2.jpg"))
    w = tk.Label(r, image = img)
    w.pack(side = "top", fill = "x", expand = "no")

    button = tk.Button(r, text = "Start", width = 20, command = detect).pack()

    r.mainloop()



