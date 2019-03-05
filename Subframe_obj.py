import tkinter as tk
from tkinter import ttk # Theme Widgits from tk
from tkinter import messagebox as mbx
from tkinter import Widget as tkw

#import qrt_codinglib as algo

Fields={}
myWindow = tk.Tk()


class SinglelboVar(tk.Listbox):
	
  def __init__(self,parent_window,display_seq,code_seq=None):
      tk.Listbox.__init__(self,parent_window,selectmode=tk.SINGLE)
      # Set up codes
      self.string_usecodes=not bool(code_seq==None)
      if self.string_usecodes :
      	       self.string_coded = \
                            [tuple([c,code])  for c,code in enumerate(code_seq) ] 
      # Produce the widget
      self._populate(display_seq)
    
  def _populate(self,display_seq):
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
	def __init__(self,parent_window,req_bg="yellow"):
		super().__init__()
		self["height"]=200
		self["width"]=270
		self["bd"]=2
		self["bg"]=req_bg
		# Internal - reuse
		self._bg=req_bg
		self._count=0
		
		self.spacer = [ tk.Label(self,text=" ", \
		                               bg=self._bg)\
		                               for b in range(12)]
#
		# Protect from overiding by internal members
		self.grid_propagate(False)
			 	
	def match_label(self,caption):
	     return tk.Label(self,text=caption,bg=self._bg)
	     	     
	def blank_label(self):
	     return tk.Label(self,text=" ",bg=self._bg)
	     
	def  ldc_gridit(self,sml,entry_ret,prow):
		sml.grid(row=prow,column=0)
		entry_ret.grid(row=prow,column=1,columnspan=3)
		tk.Label(self,text=8*" ",bg=self._bg).grid(row=prow,column=3)




	def ldc_rowlabel(self,pcaption,prow):
            sml=self.match_label(pcaption)
            sml.grid(row=prow,column=0)
            return None

	def ldc_cmdbtn(self,pcaption,prow,callback=None):
            cmd_ret = tk.Button(self,text=pcaption,command=callback)
            cmd_ret.grid(row=prow,column=0)
            return cmd_ret

	def ldc_entry(self,pcaption,prow):
            ret_text=tk.StringVar()
            sml=self.match_label(pcaption)
            entry=ttk.Entry(self,textvariable=ret_text)  
            self.ldc_gridit(sml,entry,prow)
            return ret_text
 
	def  ldc_gridpoint(self,point,prow):
		tk.Label(self,text=" ",bg=self._bg).grid(row=prow,column=0)
		point.grid(row=prow,column=1)     
 

	def ldc_radiolist(self,pcap_List):
          watching_this=tk.IntVar()
          holding={}
          for p,pcap in enumerate(pcap_List):
              q=p+1
              point= tk.Radiobutton(self,text=pcap,variable=watching_this,\
                               value=q)
              holding[q]=point
              if q==1: point.select()
              self.ldc_gridpoint(point,prow=q)
     
          return watching_this


	def ldc_singlebox(self,display_seq,code_seq=None):
          '''
          list2see=tk.Listbox(self,selectmode=tk.SINGLE)
          for br,member in enumerate(display_seq):
              list2see.insert(br,member)

          list2see.grid(row=1,column=1)

          return list2see
          '''
         
          mbx.showinfo("Should see", "About to give back - listbox",icon="info")
          return SinglelboVar(self,display_seq,code_seq)
               
