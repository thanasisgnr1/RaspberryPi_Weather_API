import time
import requests
from tkinter import *
import tkinter as tk # exw kanei lathos sto import tu tkinter
import os

import io
from urllib.request import urlopen

from PIL import ImageTk,Image  


window = Tk()

window.attributes('-fullscreen', True)


settings = {'city name':'255274','api_key':'939fcf09a4313e07e6c851fd043837c6'} 

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?id={0}&appid={1}&units=metric"

while True:
    
    final_url = BASE_URL.format(settings["city name"],settings["api_key"])
    weather_data = requests.get(final_url).json()
    town=weather_data["name"]
    weather_descri = weather_data["weather"][0]["description"]
   
    thermokra = weather_data["main"]["temp"]
    weather_image = weather_data["weather"][0]["icon"]
    localtime = time.asctime( time.localtime(time.time()) )

    #what i see to the console for checks
    print("Thermokrasia =",thermokra, "°C", localtime)
    print(weather_image)
    
    
    if weather_image == "01d":      
        pic_url = "http://openweathermap.org/img/wn/01d@2x.png"
        my_page = urlopen(pic_url)
        my_picture = io.BytesIO(my_page.read())
        pil_img = Image.open(my_picture)
        tk_img = ImageTk.PhotoImage(pil_img)
        label02d = Label(image=tk_img)
        label02d.grid(row=1, column=1)
        
    #Open weather API only have only 18 diffirent images for the condition , 9 for day and 9 for night
        
    elif weather_image == "01n":      
        pic_url = "http://openweathermap.org/img/wn/01n@2x.png"
        my_page = urlopen(pic_url)
        my_picture = io.BytesIO(my_page.read())
        pil_img = Image.open(my_picture)
        tk_img = ImageTk.PhotoImage(pil_img)
        label02d = Label(image=tk_img)
        label02d.grid(row=1, column=1)
    
    
    elif weather_image == "02d":      
        pic_url = "http://openweathermap.org/img/wn/02d@2x.png"
        my_page = urlopen(pic_url)
        my_picture = io.BytesIO(my_page.read())
        pil_img = Image.open(my_picture)
        tk_img = ImageTk.PhotoImage(pil_img)
        label02d = Label(image=tk_img)
        label02d.grid(row=1, column=1)
        
    elif weather_image == "02n":
        pic_url = "http://openweathermap.org/img/wn/02n@2x.png"
        my_page = urlopen(pic_url)
        my_picture = io.BytesIO(my_page.read())
        pil_img = Image.open(my_picture)
        tk_img = ImageTk.PhotoImage(pil_img)
        label02d = Label(image=tk_img)
        label02d.grid(row=1, column=1)
        
    elif weather_image == "03d":
        pic_url = "http://openweathermap.org/img/wn/03d@2x.png"
        my_page = urlopen(pic_url)
        my_picture = io.BytesIO(my_page.read())
        pil_img = Image.open(my_picture)
        tk_img = ImageTk.PhotoImage(pil_img)
        label02d = Label(image=tk_img)
        label02d.grid(row=1, column=1) 
        
        
    elif weather_image == "03n":
        pic_url = "http://openweathermap.org/img/wn/03n@2x.png"
        my_page = urlopen(pic_url)
        my_picture = io.BytesIO(my_page.read())
        pil_img = Image.open(my_picture)
        tk_img = ImageTk.PhotoImage(pil_img)
        label02d = Label(image=tk_img)
        label02d.grid(row=1, column=1)
        
        
        
    elif weather_image == "04d":
        pic_url = "http://openweathermap.org/img/wn/04d@2x.png"
        my_page = urlopen(pic_url)
        my_picture = io.BytesIO(my_page.read())
        pil_img = Image.open(my_picture)
        tk_img = ImageTk.PhotoImage(pil_img)
        label02d = Label(image=tk_img)
        label02d.grid(row=1, column=1) 
        
        
    elif weather_image == "04n":
        pic_url = "http://openweathermap.org/img/wn/04n@2x.png"
        my_page = urlopen(pic_url)
        my_picture = io.BytesIO(my_page.read())
        pil_img = Image.open(my_picture)
        tk_img = ImageTk.PhotoImage(pil_img)
        label02d = Label(image=tk_img)
        label02d.grid(row=1, column=1)
        
        
    elif weather_image == "09d":
        pic_url = "http://openweathermap.org/img/wn/09d@2x.png"
        my_page = urlopen(pic_url)
        my_picture = io.BytesIO(my_page.read())
        pil_img = Image.open(my_picture)
        tk_img = ImageTk.PhotoImage(pil_img)
        label02d = Label(image=tk_img)
        label02d.grid(row=1, column=1) 
        
        
    elif weather_image == "09n":
        pic_url = "http://openweathermap.org/img/wn/09n@2x.png"
        my_page = urlopen(pic_url)
        my_picture = io.BytesIO(my_page.read())
        pil_img = Image.open(my_picture)
        tk_img = ImageTk.PhotoImage(pil_img)
        label02d = Label(image=tk_img)
        label02d.grid(row=1, column=1)
        
        
        
    elif weather_image == "10d":
        pic_url = "http://openweathermap.org/img/wn/10d@2x.png"
        my_page = urlopen(pic_url)
        my_picture = io.BytesIO(my_page.read())
        pil_img = Image.open(my_picture)
        tk_img = ImageTk.PhotoImage(pil_img)
        label02d = Label(image=tk_img)
        label02d.grid(row=1, column=1) 
        
        
    elif weather_image == "10n":
        pic_url = "http://openweathermap.org/img/wn/10n@2x.png"
        my_page = urlopen(pic_url)
        my_picture = io.BytesIO(my_page.read())
        pil_img = Image.open(my_picture)
        tk_img = ImageTk.PhotoImage(pil_img)
        label02d = Label(image=tk_img)
        label02d.grid(row=1, column=1)
        
    elif weather_image == "11d":
        pic_url = "http://openweathermap.org/img/wn/11d@2x.png"
        my_page = urlopen(pic_url)
        my_picture = io.BytesIO(my_page.read())
        pil_img = Image.open(my_picture)
        tk_img = ImageTk.PhotoImage(pil_img)
        label02d = Label(image=tk_img)
        label02d.grid(row=1, column=1) 
        
        
    elif weather_image == "11n":
        pic_url = "http://openweathermap.org/img/wn/11n@2x.png"
        my_page = urlopen(pic_url)
        my_picture = io.BytesIO(my_page.read())
        pil_img = Image.open(my_picture)
        tk_img = ImageTk.PhotoImage(pil_img)
        label02d = Label(image=tk_img)
        label02d.grid(row=1, column=1)
        
        
        
    elif weather_image == "13d":
        pic_url = "http://openweathermap.org/img/wn/13d@2x.png"
        my_page = urlopen(pic_url)
        my_picture = io.BytesIO(my_page.read())
        pil_img = Image.open(my_picture)
        tk_img = ImageTk.PhotoImage(pil_img)
        label02d = Label(image=tk_img)
        label02d.grid(row=1, column=1) 
        
        
    elif weather_image == "13n":
        pic_url = "http://openweathermap.org/img/wn/13n@2x.png"
        my_page = urlopen(pic_url)
        my_picture = io.BytesIO(my_page.read())
        pil_img = Image.open(my_picture)
        tk_img = ImageTk.PhotoImage(pil_img)
        label02d = Label(image=tk_img)
        label02d.grid(row=1, column=1)
        
    #there is only one diffirent image of "mist" but i want to make sure that there is no poblem in the weather so i choose else     
    else:
        pic_url = "http://www.clker.com/cliparts/W/e/g/Q/0/K/question-mark-purple-yellow-th.png"
        my_page = urlopen(pic_url)
        my_picture = io.BytesIO(my_page.read())
        pil_img = Image.open(my_picture)
        tk_img = ImageTk.PhotoImage(pil_img)
        label02d = Label(image=tk_img)
        label02d.grid(row=1, column=1) 

       
    label1 = Label(text= town)
    label1.grid(row=2, column=1, columnspan = 2)

    label2 = Label( text = thermokra )
    label2.grid(row=3, column=1)
    
    label4 = Label(window, text = "°C")
    label4.grid(row=3, column=2)
    
    label3 = Label(window, text= localtime )
    label3.grid(row=4, column=1, columnspan = 2)
    
    if thermokra > 20:
        #LOCAL
        #image = Image.open("/home/pi/Pictures/nozaketa2.png")
        #photo = ImageTk.PhotoImage(image)
        #img_label = tk.Label(image=photo)
        # Store a reference to a PhotoImage object, to avoid it
        # being garbage collected! This is necesary to display the image!
        #img_label.image = photo
        #img_label.grid(row=4, column=1, columnspan=2 , sticky = N)
        #img_label.grid(row=1, column=2)
        #label5 = Label(window,   text = "Zaketa Min Pareis")
        #label5.grid(row= 5, column = 1, columnspan = 2)
        
        pic_url_nozak = "https://i.ibb.co/6v2hF6G/nozaketa2.png"
        my_page2_nozak = urlopen(pic_url_nozak)
        my_picture2no = io.BytesIO(my_page2_nozak.read())
        pil_img2no = Image.open(my_picture2no)
        tk_img2no = ImageTk.PhotoImage(pil_img2no)
        label02d2no = Label(image=tk_img2no)
        label02d2no.grid(row=1, column=2) 
        label5 = Label(window, text = "Zaketa Min Pareis") #Dosent Need To Wear A Jacket
        label5.grid(row= 5, column = 1, columnspan = 2)        
        

    else:
        #LOCAL 
        #image = Image.open("/home/pi/Pictures/paikse.png")
        #photo = ImageTk.PhotoImage(image)
        #img_label = tk.Label(image=photo)
        #img_label.image = photo
        #img_label.grid(row=1, column=2)
        #label5 = Label(window, text = "Zaketa Na Pareis")
        #label5.grid(row= 5, column = 1, columnspan = 2)
        
        
        pic_url2 = "https://i.ibb.co/Gk1bwCN/paikse.png"
        my_page2_zak = urlopen(pic_url2)
        my_picture2 = io.BytesIO(my_page2_zak.read())
        pil_img2 = Image.open(my_picture2)
        tk_img2 = ImageTk.PhotoImage(pil_img2)
        label02d2 = Label(image=tk_img2)
        label02d2.grid(row=1, column=2) 
        label5 = Label(window, text = "Zaketa Na Pareis") # Must Wear A Jacket
        label5.grid(row= 5, column = 1, columnspan = 2)
        
        
    # because i use the raspberry pi 3.5 inces lcd screen i want the data to be at the center    
    window.grid_rowconfigure(0, weight=1)
    window.grid_rowconfigure(6, weight=1)
    window.grid_columnconfigure(0, weight=1)
    window.grid_columnconfigure(6, weight=1)
    time.sleep(2) # because i dont want to call API all the time
    window.update()      

window.mainloop() 
