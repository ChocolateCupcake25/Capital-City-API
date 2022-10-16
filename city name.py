# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 10:50:55 2022

@author: Ziyah
"""
from tkinter import*
import requests
import json

root=Tk()
root.title("Country API")
root.geometry("500x400")
root.configure(bg="mediumspringgreen")

label_title = Label(root,text="Capital City Name",
bg="mediumspringgreen",font=("times",25,"bold","italic"),
fg="darkgreen")
label_title.place(relx=0.5,rely=0.1,anchor=CENTER)

City_input=Entry(root,bg="limegreen",font=("times",20,"bold"))
City_input.place(relx=0.5,rely=0.2,anchor=CENTER)

label_country=Label(root,text="Country",bg="mediumspringgreen",
font=("times",20,"bold","italic"),fg="darkgreen")
label_country.place(relx=0.5,rely=0.4,anchor=CENTER)

label_region=Label(root,text="Region",bg="mediumspringgreen",
font=("times",20,"bold","italic"),fg="darkgreen")
label_region.place(relx=0.5,rely=0.5,anchor=CENTER)

label_language=Label(root,text="Language",bg="mediumspringgreen",
font=("times",20,"bold","italic"),fg="darkgreen")
label_language.place(relx=0.5,rely=0.6,anchor=CENTER)

label_population=Label(root,text="Population",bg="mediumspringgreen",font=("times",20,"bold","italic"),fg="darkgreen")
label_population.place(relx=0.5,rely=0.7,anchor=CENTER)

label_area=Label(root,text="Area",bg="mediumspringgreen",
font=("times",20,"bold","italic"),fg="darkgreen")
label_area.place(relx=0.5,rely=0.8,anchor=CENTER) 

label = Label(root,text="Created by: Ziyah Virani",bg="mediumspringgreen",font=("times",12,"bold","italic"),fg="darkgreen")
label.place(relx=0.5,rely=0.95,anchor=CENTER) 

def city_details():
    api_request = requests.get("https://restcountries.com/v2/capital/"+City_input.get())
    api_output_jason=json.loads(api_request.content)
    
    country = api_output_jason[0]["name"]
    region = api_output_jason[0]["region"]
    language = api_output_jason[0]["languages"][0]["name"]
    population = api_output_jason[0]["population"]
    area = api_output_jason[0]["area"]
    
    
    label_country['text']="Country : " + country
    label_language['text']="Language : " + language
    label_population['text']="Population : " + str(population)
    label_area['text']="Area : " + str(area)
    label_region['text']="Region : " + region
    
    City_input.delete()
    
btn = Button(root,text="City Details",bg="springgreen",fg="darkgreen",font=("times",20,"bold"),command=city_details)
btn.place(relx=0.5,rely=0.3,anchor=CENTER)

root.mainloop()





