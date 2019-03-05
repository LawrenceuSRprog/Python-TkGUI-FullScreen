# alter_corner as corn
# - Alternative wayscto set up Top Left Hand Corner
import tkinter as tk
from tkinter import ttk # Theme Widgits from tk
from tkinter import messagebox as mbx
from tkinter import Widget as tkw
import alter_corner as corn # Alternative corners Lines 48 and
import Subframe_obj as sbf

def make_corner_textEntry(cur_frame,Fields):
       cur_frame.ldc_rowlabel(pcaption= "Cust Name",prow=0)
       # as Page_redTitle
       Fields["page_FirstName"]=cur_frame.ldc_entry(pcaption="           First",prow=1)
       page_MidlName=cur_frame.ldc_entry(pcaption="      Middle",prow=2)
       page_LastName=cur_frame.ldc_entry(pcaption="         Fam",prow=3)
       return None
       
'''
def make_corner_singleListbox(cur_frame,Fields):
          cur_frame.ldc_rowlabel(pcaption= "Cust clothing",prow=0)
          display_seq=["socks","shoes","shirt","gloves","hat"]
          Fields["page_clothes"]=cur_frame.ldc_singlebox(display_seq)

'''
def make_corner_singleListboxCoded(cur_frame,Fields):
          cur_frame.ldc_rowlabel(pcaption= "Cust clothing",prow=0)
          display_seq=["Diesel","Petrol","Hibred","Electric"]
          code_seq=["ds","pt","hb","ec"]
          Fields["page_engine"]=cur_frame.ldc_singlebox(display_seq,code_seq)

        

