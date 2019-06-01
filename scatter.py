# coding=utf8

import numpy as np 
import matplotlib.pyplot as plt
import tkinter as tk 
from tkinter import ttk
from tkinter.filedialog import askopenfilename
import pandas as pd
from sklearn.neighbors.kde import KernelDensity
import matplotlib.colors as mcolors




def selectfile():
    filename.set(askopenfilename())
    return True
    
def plot():
    if not filename:
        return True
    pf=pd.read_excel(filename.get(),sheet_name='Sheet1')
    data=pf[['BlockDepth','ResTime']].values
    color=KernelDensity(kernel='gaussian',bandwidth=float(x.get())).fit(data).score_samples(data)
    color=(color-np.min(color))/(np.max(color)-np.min(color))
    fig,ax1=plt.subplots(1,1)
    
    rt=ax1.scatter(data[:,0],data[:,1],c=color,cmap=colormap.get(),s=float(pointsize.get()))
    ax1.set_facecolor(background.get())
    fig.colorbar(rt,ax=ax1)
    plt.show()
 

    
    return True

root=tk.Tk()
filename=tk.StringVar()
colormap=tk.StringVar(value='Reds')
background=tk.StringVar(value='white')
x=tk.StringVar(value=0.2)
pointsize=tk.StringVar(value=0.5)
tk.Label(root,text='path:').grid(row=0,column=0)
tk.Entry(root,textvariable=filename).grid(row=0,column=1)
tk.Label(root,text='pointsize').grid(row=3,column=0)
tk.Label(root,text='background color').grid(row=4,column=0)
tk.Entry(root,textvariable=pointsize).grid(row=3,column=1)
tk.Button(root,text='select',command=selectfile).grid(row=0,column=2)
tk.Label(root,text='colormap:').grid(row=1,column=0)
com=ttk.Combobox(root,textvariable=colormap)
com.grid(row=1,column=1)
com['values']=('Greys', 'Purples', 'Blues', 'Greens', 'Oranges', 'Reds',
            'YlOrBr', 'YlOrRd', 'OrRd', 'PuRd', 'RdPu', 'BuPu',
            'GnBu', 'PuBu', 'YlGnBu', 'PuBuGn', 'BuGn', 'YlGn','binary', 'gist_yarg', 'gist_gray', 'gray', 'bone', 'pink',
            'spring', 'summer', 'autumn', 'winter', 'cool', 'Wistia',
            'hot', 'afmhot', 'gist_heat', 'copper')
bg=ttk.Combobox(root,textvariable=background)
bg.grid(row=4,column=1)
bg['values']=list(mcolors.TABLEAU_COLORS)
tk.Label(root,text='smooth 0-n').grid(row=2,column=0)
tk.Entry(root,textvariable=x).grid(row=2,column=1)
tk.Button(root,text='plot',command=plot).grid(row=4,column=2)
root.mainloop()
