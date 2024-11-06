# Import the required libraries
from tkinter import *
from tkinter import font as tkFont
import requests
import json

# Create an instance of tkinter frame
win = Tk()
win.geometry("700x350")
win.title("It's Just Predecessor Now")




# Create a text box to display the response body
text = Text(win, height=10, width=50, wrap="word")
text.config(font="Arial, 12")

# Create a label widget
label = Label(win, text="Okay It's Just Predecessor")
label.config(font="Calibri, 14")





# Add the API URL
api_url = "https://omeda.city/dashboard/hero_statistics.json"
api_url2 = "https://omeda.city/heroes.json"
# Define a function to retrieve the response
# and text attribute from the JSON response
def get_herostats():
   response = requests.get(api_url).text
   response_info = json.loads(response)
   Hero_Statistics = response_info["hero_statistics"]
   text.delete('1.0', END)
   text.insert(END, Hero_Statistics)


 

   
  

# Create Next and Exit Button
b1 = Button(win, text="Hero Stats", command=get_herostats)
b2 = Button(win, text="Exit", command=win.destroy)



v=Scrollbar(win, orient='vertical')
v.pack(side=RIGHT, fill='y')

v.config(command=text.yview)
label.pack()
text.pack()
b1.pack()
b2.pack()


get_herostats()


win.mainloop()