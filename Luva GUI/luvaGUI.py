import os
import _thread
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pyautogui
import serial

class Application(Frame):

    def combobox_handler(self,event):
        self.porta = self.porta_cb.get()
        self.baud = (int)(self.baud_cb.get())

    def Abrir_Serial(self):
        try:
            self.ser = serial.Serial(self.porta, self.baud, timeout=None)
            self.serial_aberta = True
            self.Atribuir_Atalhos()
            self.abrir.lower(self.frame)
            self.fechar.lift(self.frame)
            self.info_label["text"] = str("Lendo a porta " + self.porta + " a " + str(self.baud) + " bps.")
            try:
                _thread.start_new_thread(self.Ler_Porta,())
            except:
                pass
        except:
            if(not self.ser.is_open):
                self.info_label["text"] = str("Não foi possível abrir a porta " + self.porta + ".")

    def Fechar_Serial(self):
        self.ser.close()
        self.serial_aberta = False
        self.fechar.lower(self.frame)
        self.abrir.lift(self.frame)
        self.info_label["text"] = ""

    def Atribuir_Atalhos(self):
        self.x_mais = str(self.x_mais_entry.get())
        self.x_menos = self.x_menos_entry.get()
        self.y_mais = self.y_mais_entry.get()
        self.y_menos = self.y_menos_entry.get()
        self.z_mais = self.z_mais_entry.get()
        self.z_menos = self.z_menos_entry.get()
        self.bt1 = self.bt1_entry.get()
        self.bt2 = self.bt2_entry.get()

    def Ler_Porta(self):
        try:
            while(self.serial_aberta == True):
                bytesToRead = self.ser.inWaiting()
                c = self.ser.read(bytesToRead)
                
                if(c == b'a'):
                    pyautogui.keyDown(self.x_menos)
                if(c == b'd'):
                    pyautogui.keyDown(self.x_mais)
                if(c == b'w'):
                    pyautogui.keyDown(self.y_mais)
                if(c == b'j'):
                    pyautogui.keyDown(self.bt1)
                if(c == b'k'):
                    pyautogui.keyDown(self.bt2)
                if(c == b's'):
                    pyautogui.keyDown(self.y_menos)
                if(c == b'X'):
                    pyautogui.keyUp(self.x_mais)
                    pyautogui.keyUp(self.x_menos)
                if(c == b'Y'):
                    pyautogui.keyUp(self.y_mais)
                    pyautogui.keyUp(self.y_menos)
                if(c == b'J'):
                    pyautogui.keyUp(self.bt1)
                if(c == b'K'):
                    pyautogui.keyUp(self.bt2)
                if(c == b'p'):
                    pyautogui.keyDown(self.z_mais)
                    pyautogui.keyUp(self.z_mais)
                if(c == b'b'):
                    pyautogui.keyDown(self.z_menos)
                    pyautogui.keyUp(self.z_menos)
        except:
            pass

    def createWidgets(self):
        self.ser = serial.Serial()
        bg = "#d8d8d8"
        self.MainFrame = tkinter.Frame(self)
        self.MainFrame.pack(side = "top", fill = "both", expand = "true")
        self.MainFrame.configure(background = "#2a2a2a")
        self.frame = tkinter.Canvas(self,width = 720,height = 640)
        self.frame["relief"] = RIDGE
        self.frame["borderwidth"] = 10
        self.frame["background"] = bg
        self.file = tkinter.PhotoImage(file = "Imagens/luva.png")
        self.frame.create_image(10,10,image = self.file,anchor = NW)
        self.frame.grid(in_ = self.MainFrame,padx = 10,pady = 10)
        frame_id = self.frame.create_window(0,0,anchor = NW)

        self.portaLabel = ttk.Label(self.frame,text = "PORTA COM: ")
        self.frame.itemconfigure(frame_id,window = self.portaLabel)
        self.portaLabel.place(in_ = self.frame,x = 30, y = 570)
        self.portaLabel.configure(background = bg, foreground = self.MainFrame.cget("bg"))

        self.porta = "COM3"
        self.baud = 9600
        self.serial_aberto = False

        self.porta_cb = ttk.Combobox(self.frame)
        self.porta_cb["values"] = ["COM3","COM5","COM6","COM12"]
        self.porta_cb.current(0)
        self.porta_cb["width"] = 15
        self.frame.itemconfigure(frame_id,window = self.porta_cb)
        self.porta_cb.place(in_ = self.frame,x = 17, y = 600)
        self.porta_cb.bind('<<ComboboxSelected>>',self.combobox_handler)

        self.baudLabel = ttk.Label(self.frame,text = "BAUD RATE: ")
        self.frame.itemconfigure(frame_id,window = self.baudLabel)
        self.baudLabel.place(in_ = self.frame,x = 235, y = 570)
        self.baudLabel.configure(background = bg, foreground = self.MainFrame.cget("bg"))

        self.baud_cb = ttk.Combobox(self.frame)
        self.baud_cb["values"] = ["1200","9600","19200","38400", "57600", "115200"]
        self.baud_cb.current(1)
        self.baud_cb["width"] = 15
        self.frame.itemconfigure(frame_id,window = self.baud_cb)
        self.baud_cb.place(in_ = self.frame,x = 217, y = 600)
        self.baud_cb.bind('<<ComboboxSelected>>',self.combobox_handler)

        self.abrir = tkinter.Button(self)
        self.frame.itemconfigure(frame_id, window=self.abrir)
        self.abrir["text"] = "ABRIR"
        self.abrir.place(in_ = self.MainFrame, x = 400, y = 606)
        self.abrir["cursor"] = "hand1"
        self.abrir["command"] = lambda: self.Abrir_Serial()

        self.fechar = tkinter.Button(self)
        self.frame.itemconfigure(frame_id, window=self.fechar)
        self.fechar["text"] = "FECHAR"
        self.fechar.place(in_ = self.MainFrame, x = 400, y = 606)
        self.fechar["cursor"] = "hand1"
        self.fechar["command"] = lambda: self.Fechar_Serial()
        self.fechar.lower(self.frame)

        self.info_label = ttk.Label(self,text = "")
        self.frame.itemconfigure(frame_id,window = self.info_label)
        self.info_label.place(in_ = self.MainFrame,x = 520, y = 607)
        self.info_label.configure(background = bg, foreground = self.MainFrame.cget("bg"))

        self.x_mais = "right"
        self.x_menos = "left"
        self.y_mais = "up"
        self.y_menos = "down"
        self.z_mais = "enter"
        self.z_menos = "esc"
        self.bt1 = "j"
        self.bt2 = "k"

        self.x_mais_entry = ttk.Entry(self.frame)
        self.frame.itemconfigure(frame_id,window = self.x_mais_entry)
        self.x_mais_entry["width"] = 10
        self.x_mais_entry["justify"] = "center"
        self.x_mais_entry.insert(0,"right")
        self.x_mais_entry.place(in_ = self.frame,x = 595, y = 240)

        self.x_menos_entry = ttk.Entry(self.frame)
        self.frame.itemconfigure(frame_id,window = self.x_menos_entry)
        self.x_menos_entry["width"] = 10
        self.x_menos_entry["justify"] = "center"
        self.x_menos_entry.insert(0,"left")
        self.x_menos_entry.place(in_ = self.frame,x = 25, y = 250)

        self.y_mais_entry = ttk.Entry(self.frame)
        self.frame.itemconfigure(frame_id,window = self.y_mais_entry)
        self.y_mais_entry["width"] = 10
        self.y_mais_entry["justify"] = "center"
        self.y_mais_entry.insert(0,"up")
        self.y_mais_entry.place(in_ = self.frame,x = 80, y = 40)

        self.y_menos_entry = ttk.Entry(self.frame)
        self.frame.itemconfigure(frame_id,window = self.y_menos_entry)
        self.y_menos_entry["width"] = 10
        self.y_menos_entry["justify"] = "center"
        self.y_menos_entry.insert(0,"down")
        self.y_menos_entry.place(in_ = self.frame,x = 145, y = 500)

        self.z_mais_entry = ttk.Entry(self.frame)
        self.frame.itemconfigure(frame_id,window = self.z_mais_entry)
        self.z_mais_entry["width"] = 10
        self.z_mais_entry["justify"] = "center"
        self.z_mais_entry.insert(0,"enter")
        self.z_mais_entry.place(in_ = self.frame,x = 615, y = 40)

        self.z_menos_entry = ttk.Entry(self.frame)
        self.frame.itemconfigure(frame_id,window = self.z_menos_entry)
        self.z_menos_entry["width"] = 10
        self.z_menos_entry["justify"] = "center"
        self.z_menos_entry.insert(0,"esc")
        self.z_menos_entry.place(in_ = self.frame,x = 590, y = 480)

        self.bt1_entry = ttk.Entry(self.frame)
        self.frame.itemconfigure(frame_id,window = self.bt1_entry)
        self.bt1_entry["width"] = 10
        self.bt1_entry["justify"] = "center"
        self.bt1_entry.insert(0,"space")
        self.bt1_entry.place(in_ = self.frame,x = 23, y = 100)

        self.bt2_entry = ttk.Entry(self.frame)
        self.frame.itemconfigure(frame_id,window = self.bt2_entry)
        self.bt2_entry["width"] = 10
        self.bt2_entry["justify"] = "center"
        self.bt2_entry.insert(0,"backspace")
        self.bt2_entry.place(in_ = self.frame,x = 127, y = 177)

    def __init__(self, master=None):
        Frame.__init__(self, master)
        pyautogui.FAILSAFE = False
        self.grid()
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.createWidgets()
