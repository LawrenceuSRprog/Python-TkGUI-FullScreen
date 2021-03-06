import tkinter as tk
from tkinter.font import Font
from tkinter import ttk # Theme Widgits from tk
from tkinter import messagebox as mbx
from tkinter import Widget as tkw
import alter_corner as corn # Alternative corners Lines 48 and
import Subframe_obj as sbf
import qrt_codinglib as algo

def maketile_Template():
	       return {
	            "height":200,"width":270,\
	            "bg":"yellow","bd":2,\
	            "font":Font(family="Helvetica", size=8) }
	        
Fields={}
myWindow = tk.Tk()
	
def open_window():
	
	return None
       
def close_window():
      myWindow.destroy()
      exit()
 
def push_button(source):
	    if source=="EXIT":
	           ureq=mbx.askquestion("Exit",\
	                       "Are you sure you want to go",icon="info")
	           if ureq=="yes" :
	           	myWindow.destroy()
	           	exit()
	           else:
	       	    mbx.showinfo("continuing")
	    	    
	    if source=="LOAD" : algo.proc_load(Fields)
	  
	    if source=="SAVE" : algo.proc_save(Fields)          
                                                                                
def frb_footerPush_A(): push_button("LOAD")  
def frb_footerPush_B(): push_button("SAVE")  
def frb_footerPush_C(): push_button("EXIT")                                                                                      
                                                                                                                                
def keep_fixed_frame(framep):
	framep.grid_propagate(False)
	
open_window()
myWindow.maxsize(600,400)
myWindow.minsize(600,400)
ft = maketile_Template()  # currently below line 100
ft["bg"]="red"
frb_red=sbf.Subframe_builder(myWindow,ft ,allow_inner=True) # This is where the experiment exists
corn.make_corner_singleListboxCoded(frb_red,Fields)

# =======================================
# And again for the blue
# =======================================z
ft["bg"]="blue"
frb_blue=sbf.Subframe_builder(myWindow,ft)
frb_blue.ldc_rowlabel(pcaption="Delivary ad",prow=0) # as Page_blueTitle
Fields["page_Street"]=frb_blue.ldc_entry(pcaption="     Street",prow=1)
page_Town=frb_blue.ldc_entry(pcaption= "      Town",prow=2)
page_County=frb_blue.ldc_entry(pcaption=" County",prow=3)

# =======================================
# And again for the green and pink footers
# =======================================
ft["bg"]="green"
frb_footer=sbf.Subframe_builder(myWindow,ft)

ft["bg"]="pink"
frb_optio=sbf.Subframe_builder(myWindow,ft)

frb_optio.ldc_rowlabel(pcaption="Cooking",prow=0) # as Radio Header
Fields["page_optio"]=\
frb_optio.ldc_radiolist(["Boiled          ",\
                                        "Fried             ",\
                                        "Scrambled "])

frb_footer.ldc_rowlabel(pcaption=" ",prow=3) # as page_Skip

page_cmdLoad=\
      frb_footer.ldc_cmdbtn(pcaption=" << Load >> ",prow=1,\
      callback=frb_footerPush_A)
page_cmdSave=\
      frb_footer.ldc_cmdbtn(pcaption=" << Save >> ",prow=2,\
      callback=frb_footerPush_B)
page_cmdExit=\
     frb_footer.ldc_cmdbtn(pcaption="  << Exit >> ",prow=4,\
     callback=frb_footerPush_C)

# mbx.showinfo("Continuing")

# =======================================
# Assemble Childen of myWindow
# =======================================

frb_red.grid(row=0,column=0)
frb_blue.grid(row=0,column=1)
frb_optio.grid(row=1,column=0)
frb_footer.grid(row=1,column=1)

myWindow.mainloop()
