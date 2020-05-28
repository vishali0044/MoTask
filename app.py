import tkinter as tk  #Tkinter is basically a package to run python code, this will help to create GUI
from tkinter import filedialog, Text # it will help to pick the Apps
import os 

root = tk.Tk() 
apps = []
if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
     tempApps = f.read()
     tempApps = tempApps.split(',') #it will remove space, but split files 
     apps = [x for x in tempApps if x.strip()]
def addApp(): #It will open file directories ,which we want to select
    for widget in frame.winfo_children(): # widget will give us  access to everything which is attached to frame
        widget.destroy() #It will destroy or remove previous file and attach updated one
        #It will allows to specifies things 
    filename = filedialog.askopenfilename(initialdir="/", title="Select File", filetypes=(("executables", "*.exe"), ("all files", "*.*"))) 
    apps.append(filename)  #It will give the location of file
    print(filename)
    for app in apps:
         label = tk.Label(frame, text=app, bg="gray")
         label.pack()
def runApps():
      for app in apps: 
          os.startfile(app)    
canvas = tk.Canvas(root, height=600, width=600, bg="#263D42") 
canvas.pack() 

frame = tk.Frame(root, bg="white") 
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1) 
#This line will add button on App and it will attach to root(Button name is Open file)
openFile = tk.Button(root, text="Open File", padx=10, pady=5, fg="white", bg="#263D42", command=addApp)
openFile.pack()

runApps = tk.Button(root, text="Run Apps", padx=10, pady=5, fg="white", bg="#263D42", command=runApps)
runApps.pack()

for app in apps:
    label = tk.Label(frame, text=app)
    label.pack()
root.mainloop()

with open('save.txt', 'w') as f:  #It will generate save.txt file so all files or app wll be saved
    for app in apps:
        f.write(app + ',')