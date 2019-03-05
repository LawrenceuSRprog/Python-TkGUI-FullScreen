
import tkinter as tk
from tkinter import ttk # Theme Widgits from tk
from tkinter import messagebox as mbx
from tkinter import Widget as tkw

import qrt_codinglib as algo


def proc_load(Fields):
         mbx.showinfo("Loading")
         Fields["page_Street"].set("Old Kent Road") # Street as text Entry
         #Fields["page_FirstName"].set("Harold") # fName  as text Entry
         #Fields["page_clothes"].set(2)
         Fields["page_engine"].set("pt")
         Fields["page_optio"].set(3)# Btn index starts 1

def proc_save(Fields):
     s1=Fields["page_Street"].get() # Street as text
     t1=str(Fields["page_optio"].get() )# Btn index starts 1
     t2=str(Fields["page_engine"].get())
     s = "Street: " + s1 + "\n" + \
           "Cook: " + t1+"\n" + \
            "Engine: " +t2+"\n" + \
            "-- That's all people'"
     mbx.showinfo("Saving Data", s,icon="info")

