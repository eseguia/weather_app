import requests
import tkinter as tk
from PIL import Image, ImageTk

# url = 'https://www.meteored.com.ar/tiempo-en_Buenos+Aires-America+Sur-Argentina-Ciudad+Autonoma+de+Buenos+Aires-SABE-1-13584.html'
# source = requests.get(url)
# soup = BeautifulSoup(source.text, 'html.parser')
# # print(soup.prettify())
# weath = soup.find(class_='dato-temperatura changeUnitT').text
# print(weath)

def results(weather):
    name,description = weather['name'],weather['weather'][0]['description']
    temp,feels = weather['main']['temp'],weather['main']['feels_like']
    tmin,tmax = weather['main']['temp_min'],weather['main']['temp_max']
    humidity,pressure = weather['main']['humidity'],weather['main']['pressure']
    strfinal = 'City: %s \nConditions: %s \nTemperature: %s °C \nFeels Like: %s °C \nMax Temperature: %s °C \nMin Temperature: %s °C \nHumidity: %s \nPressure: %s hPa'% (name,description,temp,feels,tmax,tmin,humidity,pressure)
    return strfinal

def give_weather(city):
    key = '5af00c276c3b71e2b22795d9d34806cb'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    parameters = {'APPID':key,'q':city,'units':'metric'}
    response = requests.get(url, params = parameters)
    weather = response.json()
    label['text'] = results(weather)
    label['font'] = 'Cambria 18'

root = tk.Tk()
root.title('Weather')
root.iconbitmap('C:/Users/Emilio/Documents/JUPYTER NOTEBOOKS/weather_icon.ico')
HEIGHT, WIDTH = 700,800
canvas = tk.Canvas(root,height=HEIGHT,width=WIDTH)
canvas.pack()

back_img = tk.PhotoImage(file='C:/Users/Emilio/Documents/JUPYTER NOTEBOOKS/sky_background_weather.png')
back_img= back_img.subsample(2, 2)
background = tk.Label(root, image = back_img)
background.place(relwidth=1,relheight=1)

frame = tk.Frame(root,bg = '#46B9E0')
frame.place(relx=0.5,rely=0.1,relwidth=0.75,relheight=0.08,anchor='n')
entry = tk.Entry(frame,font='Arial 16')
entry.place(relx=0.02,rely=0.1,relwidth=0.55,relheight=0.8)
entry['bg']='#BDC1EA'
button = tk.Button(frame,text='Get Weather',font = 30,command=lambda:give_weather(entry.get()))
button.place(relx=0.6,rely=0.1,relheight=0.8,relwidth=0.35)
button['bg']='#B3E5F7'

sec_frame = tk.Frame(root,bg='#46B9E0')
sec_frame.place(relx=0.5,rely=0.22,relwidth=0.75,relheight=0.6,anchor='n')
label =  tk.Label(sec_frame,bg = '#D3F4FF')
label.place(relx=0.025,rely=0.025,relwidth=0.95,relheight=0.95)

root.mainloop()