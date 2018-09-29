import tkinter
import luvaGUI

def main():
    root = tkinter.Tk()
    app = luvaGUI.Application(master=root)
    app.master.title("Configuração Luva")
    app.master.minsize(765,680)
    icone = tkinter.PhotoImage(file = 'Imagens/icone.png')
    root.tk.call("wm","iconphoto",root._w,icone)
    root.geometry("720x640+0+0")
    app.master.resizable(False,False)
    app.mainloop()

if __name__ == '__main__':
    main()
