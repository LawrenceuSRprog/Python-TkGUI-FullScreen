import tkinter as tk
from tkinter import ttk # Theme Widgits from tk
from tkinter import messagebox as mbx
from tkinter import Widget as tkw

#import qrt_codinglib as algo

Fields={}
myWindow = tk.Tk()

class SinglelboVar(tk.Listbox):

    def __init__(self,inner_Frame,display_seq,code_seq=None):
      tk.Listbox.__init__(self,inner_Frame,selectmode=tk.SINGLE)
      # Set up codes
      self.string_usecodes=not bool(code_seq==None)
      if self.string_usecodes :
      	       self.string_coded = \
                            [tuple([c,code])  for c,code in enumerate(code_seq) ] 
      # Produce the widget
      self._populate(display_seq)

    def _populate(self,display_seq):
       s="Make house for listbox and its scrollbar" + "\n" + "mainly from _generate_list"
               
       mbx.showinfo("Listbox inner working",s,icon="info") 
       for g,gotit in enumerate(display_seq):
              self.insert(g,gotit)
       self.grid(row=1,column=1)

    def _index_fromcode(self,code):
         idx_out=-1
         for pair in self.string_coded:
             if pair[1]==code: idx_out=pair[0]
         return idx_out

    def _code_fromindex(self,index):
       code_out="DONT"
       for pair in self.string_coded:
           if pair[0]==index: code_out=pair[1]
       return code_out

    def set(self,value_tomatch):
       if self.string_usecodes:
           index=self._index_fromcode(value_tomatch)
       else:
           index=value_tomatch
       # ==== End If
       len = self.size()
       self.selection_clear(0,len)# List Index removed
       self.selection_set(index)
       return None


    def get(self):
         result=None
         index=int( self.curselection()[0])
         if self.string_usecodes:
            result=self._code_fromindex(index)
         else:
            result=index
      # === End If
         return result
### End of Class ###

class Subframe_builder(tk.Frame):
    def __init__(self,parent_window,frame_target,allow_inner=False):
            super().__init__()
            for idx in frame_target.keys():
                  if idx != "font":
                    self[idx]=frame_target[idx]
            # Internal - reuse
            
            self._bodytext= frame_target["font"]
            self._bg= self["bg"]
            self._allowinner= allow_inner
            self._count=0
            self.grid_propagate(False)
        
    def match_label(self,caption):
	     return tk.Label(self,text=caption,bg=self._bg,font=self._bodytext)
	     
    def blank_label(self):
	     return tk.Label(self,text=" ",bg=self._bg,font=self._bodytext)
	     
    def  ldc_gridit(self,sml,entry_ret,prow):
        sml.grid(row=prow,column=0)
        entry_ret.grid(row=prow,column=1,columnspan=3)
        tk.Label(self,text=8*" ",bg=self._bg,font=self._bodytext).grid(row=prow,column=3)

    def ldc_rowlabel(self,pcaption,prow):
            sml=self.match_label(pcaption)
            sml.grid(row=prow,column=0)
            return None

    def ldc_cmdbtn(self,pcaption,prow,callback=None):
            cmd_ret = tk.Button(self,text=pcaption,command=callback,font=self._bodytext)
            cmd_ret.grid(row=prow,column=0)
            return cmd_ret

    def ldc_entry(self,pcaption,prow):
            ret_text=tk.StringVar()
            sml=self.match_label(pcaption)
            entry=ttk.Entry(self,textvariable=ret_text,font=self._bodytext)
            self.ldc_gridit(sml,entry,prow)
            return ret_text
            
    def ldc_gridpoint(self,point,prow):
         tk.Label(self,text=" ",bg=self._bg).grid(row=prow,column=0)
         point.grid(row=prow,column=1)
         return None
    
    def ldc_radiolist(self,pcap_List):
          watching_this=tk.IntVar()
          holding={}
          for p,pcap in enumerate(pcap_List):
              q=p+1
              point= tk.Radiobutton(self,text=pcap,variable=watching_this,\
                               value=q,font=self._bodytext)
              holding[q]=point
              if q==1: point.select()
              self.ldc_gridpoint(point,prow=q)

          return watching_this
          
    def tiled_frame():
    	   pass    
    	   
    def _display_FrameDims(self,title,line):                	
       head=str(title)
       s="Caption = "+ head +"\n"
       s+= "Tile ="    + str(line[0]) + "," + str(line[1]) + "\n"
       s+= "Inner ="  + str(line[2]) + "," + str(line[3]) + "\n"
       s+= "Offset ="+str(line[4]) + "," + str(line[5])
       
       mbx.showinfo("Window inner Stats",s,icon="info")
       return None	   
    	     

    
    def _continue_inner(self,title_caption):
                       	
          if title_caption is None:
                 inheight=self["height"] -8      
          else:
                 inheight=self["height"] -(8+3 * self._bodytext["size"]) 
                 title=tk.Label(self,text=title_caption,bg=self["bg"])
                 title.grid(row=0,column=0)
          # self is the tileFrame we are building in		        
          innerFrame=tk.Frame(self,\
                      height=inheight,width=self["width"]- 24,bg=self["bg"])
              
          off_x=  self["width"]-8 # close to RHS border
          off_y = self["height"]-innerFrame["height"]
      
          innerFrame.place(anchor=tk.NE,x=off_x,y=off_y)
          line=[ self["width"],self["height"],
          innerFrame["width"],\
          innerFrame["height"],off_x,off_y]
          
          self._display_FrameDims(title_caption,line)
          return innerFrame
 
    def _generate_list(self,innerFrame,lis_display,lis_code):
  	 
                  height_factor=round(self._bodytext["size"] * 2.6)                                 
                  row_height=int(innerFrame["height"]/height_factor)
                  width_factor=int(self._bodytext["size"] * 1.7)
                  col_width=int(innerFrame["width"]/width_factor) 
      
                  listNodes = tk.Listbox(innerFrame,width=col_width,\
                                              height=row_height, font=self._bodytext)
                    
                  listNodes.pack(side="left", fill="y")
      
                  scrollbar = tk.Scrollbar(innerFrame, orient="vertical")
                  scrollbar.config(command=listNodes.yview)
                  scrollbar.pack(side="right", fill="y")
                  #scrollbar.grid(row=0,column=1)
      

                  listNodes.config(yscrollcommand=scrollbar.set)
                      
                  for x in lis_display:
                       listNodes.insert(tk.END, x)
                  return listNodes
      
    def ldc_singlebox(self,display_seq,code_seq=None):
       if self._allowinner:
                mbx.showinfo("Newer Code",\
                        "Something new should have started",icon="info")
                title_caption=None #  "bung in title!"
                innerFrame=self._continue_inner(title_caption)
                #listbox_out=self._generate_list(innerFrame,display_seq,code_seq)
                listbox_out= SinglelboVar(innerFrame,display_seq,code_seq)

       else:
               mbx.showinfo("Older Code",\
                 "About to give back - listbox",icon="info")
               listbox_out= SinglelboVar(self,display_seq,code_seq)
          
       return listbox_out

