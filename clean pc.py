import os
try:
    import requests
    import socket as s
    import webbrowser
    from sys import platform
    import colorama

except ModuleNotFoundError:
    os.system("pip install requests")
    os.system("pip install socket")
    os.system("pip install webbrowser")
    os.system("pip install sys")
    os.system("pip install platform")
    os.system("pip install colorama")
    os.system("pip install Today")
    os.system("pip install Date")
    os.system("pip install os")
import webbrowser
url = "https://t.me/HEXiN1K"
webbrowser.open(url)
from sys import platform
from colorama import *
import socket
import requests
from datetime import datetime

now = datetime.now()

current_time = now.strftime

name = socket.gethostname()

myHostName = socket.gethostname()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("\n===========================================================")
name = ("""\n                    Hello sir """ +name+Style.RESET_ALL)
print(name)

import datetime
e = datetime.datetime.now()
print (Fore.CYAN+"""\n                   Your Day is """+"%s/%s/%s" % (e.day, e.month, e.year))
print ("""\n                   The time is """+ "%s:%s:%s" % (e.hour, e.minute, e.second))

host = (Fore.WHITE+"""\n                  Your platform is """+ platform+Style.RESET_ALL)
print(host)

api = "https://api.ipify.org/?format=json"
req = requests.get(api)
response = req.json()
a = response["ip"]

IP = ("""\n                Your Local iP is """+Fore.RED+a+Style.RESET_ALL)
print(IP)

v = (Fore.RED+"""\n                    Your iNFO PROXY is\n"""+Style.RESET_ALL)

print(v)
print(s)

print("\n===========================================================")


import webbrowser
import tkinter
import tkinter.messagebox
import os
import os.path
import threading
url = "https://instagram.com/hxn.py/"
webbrowser.open(url)

rubbishExt = ['.tmp', '.bak', '.old', '.wbk', '.xlk', '_mp', '.gid',
              '.chk', '.syd', '.$$$', '.@@@', ".~*"]


def GetDrives():
    drives = []
    for i in range(65, 91):
        vol = chr(i) + ":/"
        if os.path.isdir(vol):
            drives.append(vol)
    return tuple(drives)


class Window:
    def __init__(self):
        self.root = tkinter.Tk()

        menu = tkinter.Menu(self.root)

        submenu = tkinter.Menu(menu, tearoff=0)
        submenu.add_command(label="About...", command=self.MenuAbout)
        submenu.add_separator()
        submenu.add_command(label="Quit", command=self.MenuExit)
        menu.add_cascade(label="System", menu=submenu)

        submenu = tkinter.Menu(menu, tearoff=0)
        submenu.add_command(label="Scan", command=self.MenuScanRubbish)
        submenu.add_command(label="Delete", command=self.MenuDelRubbish)
        menu.add_cascade(label="Clean", menu=submenu)

        submenu = tkinter.Menu(menu, tearoff=0)
        submenu.add_command(label="Search Big Files",
                            command=self.MenuScanBigFile)
        submenu.add_separator()
        submenu.add_command(label="Search Big Files By Name",
                            command=self.MenuSearchFile)
        menu.add_cascade(label="Search", menu=submenu)

        self.root.config(menu=menu)

        self.progress = tkinter.Label(self.root, anchor=tkinter.W,
                                      text='Status', bitmap='hourglass',
                                      compound='left')
        self.progress.place(x=10, y=370, width=480, height=15)

        self.flist = tkinter.Text(self.root)
        self.flist.place(x=10, y=10, width=480, height=350)

        self.vscroll = tkinter.Scrollbar(self.flist)
        self.vscroll.pack(side='right', fill='y')
        self.flist['yscrollcommand'] = self.vscroll.set
        self.vscroll['command'] = self.flist.yview

    def MainLoop(self):
        self.root.title("Clean Your PC ~ insta @hxn.py")
        self.root.minsize(500, 400)
        self.root.maxsize(500, 400)
        self.root.mainloop()

    def MenuAbout(self):
        tkinter.messagebox.showinfo("Clean Your PC ~ insta @hxn.py",
                                    "Hello sir, this program is special for you to clean your disk of suspicious and large files :)")

    def MenuExit(self):
        self.root.quit()

    def MenuScanRubbish(self):
        result = tkinter.messagebox.askquestion("Clean Your PC ~ insta @hxn.py", "Scaning" +
                                                " junk files may cost much time. Continue?")
        if result == 'no':
            return
        tkinter.messagebox.showinfo("Clean Your PC ~ insta @hxn.py", "Scaning in no time!")

        self.drives = GetDrives()
        t = threading.Thread(target=self.ScanRubbish, args=(self.drives,))
        t.start()

    def MenuDelRubbish(self):
        result = tkinter.messagebox.askquestion("Clean Your PC ~ insta @hxn.py",
                                                "Deleting junk files may cost much time. Continue?")
        if result == 'no':
            return
        tkinter.messagebox.showinfo("Clean Your PC ~ insta @hxn.py", "Deleting in no time!")
        self.drives = GetDrives()
        t = threading.Thread(target=self.DeleteRubbish, args=(self.drives,))
        t.start()

    def MenuScanBigFile(self):
        result = tkinter.messagebox.askquestion("Clean Your PC ~ insta @hxn.py",
                                                "Scaning big files may cost much time. Continue?")
        if result == 'no':
            return
        tkinter.messagebox.showinfo("Clean Your PC ~ insta @hxn.py", "Scaning in no time!")

    def MenuSearchFile(self):
        result = tkinter.messagebox.askquestion("Clean Your PC ~ insta @hxn.py,"
                                                "Searching big files by name may cost much time. Continue?")
        if result == 'no':
            return
        tkinter.messagebox.showinfo("Clean Your PC ~ insta @hxn.py", "Searching in no time!")

    def ScanRubbish(self, scanpath):
        global rubbishExt
        total = 0
        filesize = 0
        for drive in scanpath:
            for root, dirs, files in os.walk(drive):
                try:
                    for fil in files:
                        filesplit = os.path.splitext(fil)
                        if filesplit[1] == '':
                            continue
                        try:
                            if rubbishExt.index(filesplit[1]) >= 0:
                                fname = os.path.join(
                                    os.path.abspath(root), fil)
                                filesize += os.path.getsize(fname)
                                if total % 20 == 0:
                                    self.flist.delete(0.0, tkinter.END)
                                self.flist.insert(tkinter.END, fname + '\n')
                                l = len(fname)
                                if l > 60:
                                    self.progress['text'] = fname[:30] + '...' + \
                                                            fname[l - 30:l]
                                else:
                                    self.progress['text'] = fname
                                total += 1
                        except ValueError:
                            pass
                except Exception as e:
                    print(e)
                    pass
        self.progress['text'] = "Find %s junk files, occupy %.2f M disk space" \
                                % (total, filesize / 1024 / 1024)

    def DeleteRubbish(self, scanpath):
        global rubbishExt
        total = 0
        filesize = 0
        for drive in scanpath:
            for root, dirs, files in os.walk(drive):
                try:
                    for fil in files:
                        filesplit = os.path.splitext(fil)
                        if filesplit[1] == '':
                            continue
                        try:
                            if rubbishExt.index(filesplit[1]) >= 0:
                                fname = os.path.join(
                                    os.path.abspath(root), fil)
                                filesize += os.path.getsize(fname)
                                try:
                                    os.remove(fname)
                                    l = len(fname)
                                    if l > 50:
                                        fname = fname[:25] + "..." + \
                                                fname[l - 25:l]
                                    if total % 15 == 0:
                                        self.flist.delete(0.0, tkinter.END)
                                    self.flist.insert(tkinter.END, 'Deleted '
                                                      + fname + '\n')
                                    self.progress['text'] = fname
                                    total += 1
                                except:
                                    pass
                        except ValueError:
                            pass
                except Exception as e:
                    print(e)
                    pass
        self.progress['text'] = f"Deleted {total} junk files, recover {filesize / 1024 / 1024} M disk space"


if __name__ == "__main__":
    window = Window()
    window.MainLoop()
