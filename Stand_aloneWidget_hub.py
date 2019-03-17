import tkinter as tk
from tkinter.font import Font
from tkinter import ttk # Theme Widgits from tk
from tkinter import messagebox as mbx
from tkinter import Widget as tkw
'''
=============================================
cross-ref this with line 47 in qrt_driver

also lines: 47,54,62,64,73,

frb_red=sbf.Subframe_builder(myWindow,"red")
corn.make_corner_singleListboxCoded(frb_red,Fields)

This affects : 
class Subframe_builder(tk.Frame):
	def __init__(self,parent_window,req_bg="yellow"):  => change it to |
                                                                                                                    /
	def __init__(self,parent_window,frame_template):  <==:== /
	
	


=============================================
'''
mw = tk.Tk() # main window 
mw.geometry("480x250")

def maketile_Template():
	       return {
	            "height":141,"width":150,"bg":"red",\
	            "font":Font(family="Helvetica", size=8) }
	            
def _begin_tile(parent_window,ft):
           tileFrame= tk.Frame(parent_window,\
                height=ft["height"],width=ft["width"],\
                bg=ft["bg"])
 
           tileFrame.grid_propagate(False)
           return tileFrame
             
def _continue_inner(tileFrame,ft,title_caption):
                       	
      if title_caption is None:
      	   inheight=ft["height"] -8      
      else:
        	inheight=ft["height"] -(8+3 * ft["font"]["size"])
        	title=tk.Label(tileFrame,text=title_caption,bg=ft["bg"])
        	title.grid(row=0,column=0)
        		        
      innerFrame=tk.Frame(tileFrame,\
              height=inheight,width=ft["width"]- 24,bg=ft["bg"])
               
      innerFrame.place(x=36, y=ft["height"]-innerFrame["height"])
      
      return innerFrame
        
def _framed_pairs(parent_window,ft,title_caption=None):
      tile =_begin_tile(parent_window,ft)
      inner= _continue_inner(tile,ft,title_caption)
      return tile,inner
 
def _generate_list(innerFrame, ft,lis_display,lis_code):
      #innerFrame.pack_propagate(False) # insides by packing
      height_factor=round(ft["font"]["size"] * 2.6)                                 
      row_height=int(innerFrame["height"]/height_factor)
      width_factor=int(ft["font"]["size"] * 1.7)
      col_width=int(innerFrame["width"]/width_factor) 
      
      listNodes = tk.Listbox(innerFrame,width=col_width,\
                                              height=row_height, font=ft["font"])
                    
      listNodes.pack(side="left", fill="y")
      
      scrollbar = tk.Scrollbar(innerFrame, orient="vertical")
      scrollbar.config(command=listNodes.yview)
      scrollbar.pack(side="right", fill="y")
      #scrollbar.grid(row=0,column=1)
      

      listNodes.config(yscrollcommand=scrollbar.set)
                      
      for x in lis_display:
          listNodes.insert(tk.END, x)
      
      return listNodes
	
                      
def make_listbox_tile(parent_window,ft,lis_display,\
                    lis_code=None,title_caption=None):
     
      tileFrame, innerFrame=_framed_pairs(parent_window,ft,title_caption)
                       
      widget_hub =_generate_list(innerFrame, ft,lis_display,lis_code)
      
      return tileFrame,widget_hub

lis_display=["half-boots","full-boots","sandles","slippers","casual shoes",\
                        "smart shoes","slippers","sports-run",\
                        "sports-hike","sports-climb"]
ft = maketile_Template()
tile_area,widget_hub=make_listbox_tile(mw,ft,lis_display,title_caption="Things to see") # line 12
tile_area.grid(row=0,column=0)

mw.mainloop()
