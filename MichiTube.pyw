from tkinter import *
from tkinter.ttk import *
import subprocess, os

class MichiDLFrame(Frame):
  def __init__(self, code, master=None):
    Frame.__init__(self, master)
    self.pack()
    self.excode = code
    self.createWidgets()
  def createWidgets(self):
    self.label = Label(self)
    if self.excode != 0:
      self.label["text"] = "Pobieranie nie zakonczylo sie pomydlnie. Nie wiem czemu, bo jeszcze slaby ze mnie program."
    else:
      self.label["text"] = "Plik zapisany w folderze %s." % os.getcwd()
    self.label.pack()

class MichiTube(Frame):
  def __init__(self, master=None):
    Frame.__init__(self, master)
    self.masterer = master
    self.pack()
    self.status = StringVar()
    self.status.set("Pobierz")
    self.createWidgets()
  def createWidgets(self):
    self.entrylabel = Label(self, text="Tu wpisz adres")
    self.entrylabel.pack()
    self.entry = Entry(self, text="http://youtube.com/watch?v=")
    self.entry.pack()
    self.downloadbtn = Button(self, textvariable=self.status, command=self.download)
    self.downloadbtn.pack(side="left")
    self.quitbtn = Button(self, text="Koniec", command=root.destroy)
    self.quitbtn.pack(side="right")
  def download(self):
    MichiDLFrame(subprocess.call(["youtube-dl",self.entry.get()]), master=self.masterer).mainloop()

root = Tk()
root.title("MichiTube")
app = MichiTube(master=root)
app.mainloop()
