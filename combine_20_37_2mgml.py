# %%
from datetime import time
from matplotlib import markers
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns
from glob import glob
from seaborn import palettes
from seaborn.categorical import swarmplot
from tqdm import tqdm
import json
from scipy.signal import detrend
from scipy.ndimage import gaussian_filter1d
import os
import re
import math
import matplotlib.ticker as tck
import argparse

#%%
data_all=[]
data_20=[]
data_37=[]
data_all= pd.read_csv('C:/Users/srboval1/IPN_revision/revision.csv',delimiter=',')
data_20 = (data_all.loc[data_all['temperature'] == 20])
data_37 = (data_all.loc[data_all['temperature'] == 37])
#%%
grid = plt.GridSpec(1, 2, wspace=0.25, hspace = 0.5)
plt.figure(figsize = (25, 10),facecolor='white',dpi=300)
plt.subplot(grid[0, 0])
ax=sns.boxplot(data=data_20,x='crosslinker',y='G_abs',palette="colorblind",hue ='collagen',showfliers=False, )
ax=sns.stripplot(data=data_20,x='crosslinker',y='G_abs',size = 6,color='0',hue ='collagen',dodge=True)
ax.yaxis.set_minor_locator(tck.AutoMinorLocator(3))
plt.xlabel("Crosslinker concentration [mM]", fontsize= 38,labelpad=5)
plt.ylabel("|G*|", fontsize= 40, labelpad=5)
plt.xticks(fontsize= 37) 
plt.yticks(fontsize= 37) 
plt.ylim (1,10000)
plt.yscale("log")
ax.tick_params('y', length=8, width=2, which='major')
ax.tick_params('y', length=6, width=1, which='minor')
handles,labels = ax.get_legend_handles_labels()
l = plt.legend(handles[:2],labels[:2])
l.remove()
plt.subplot(grid[0, 1])
ax=sns.boxplot(data=data_20,x='crosslinker',y='phi_(rad)',palette="colorblind",hue ='collagen',showfliers=False, )
ax=sns.stripplot(data=data_20,x='crosslinker',y='phi_(rad)',size = 6,color='0',hue ='collagen',dodge=True)
ax.yaxis.set_minor_locator(tck.AutoMinorLocator(3))
plt.xlabel("Crosslinker concentration [mM]", fontsize= 38,labelpad=5)
plt.ylabel("\u03A6 (rad)", fontsize= 40,labelpad=5)
plt.xticks(fontsize= 37) 
plt.yticks(fontsize= 37)
plt.ylim (-0.05,0.5)
ax.tick_params('y', length=8, width=2, which='major')
ax.tick_params('y', length=6, width=1, which='minor')
handles,labels = ax.get_legend_handles_labels()
l = plt.legend(handles[:1],labels[:1], fontsize = 25, title_fontsize = 25, title = "collagen [mg/ml]",loc='upper right', frameon=False)
plt.savefig('C:/Users/srboval1/IPN_revision/IPN_compared_20C.tif', bbox_inches='tight',dpi=300)

#%%
grid = plt.GridSpec(1, 2, wspace=0.25, hspace = 0.5)
plt.figure(figsize = (25, 10),facecolor='white',dpi=300)
plt.subplot(grid[0, 0])
ax=sns.boxplot(data=data_37,x='crosslinker',y='G_abs',palette="colorblind",hue ='collagen',showfliers=False, )
ax=sns.stripplot(data=data_37,x='crosslinker',y='G_abs',size = 6,color='0',hue ='collagen',dodge=True)
plt.xlabel("Crosslinker concentration [mM]", fontsize= 38,labelpad=5)
plt.ylabel("|G*| (Pa)", fontsize= 40, labelpad=5)
plt.xticks(fontsize= 37) 
plt.yticks(fontsize= 37) 
plt.ylim (1,10000)
plt.yscale("log")
ax.tick_params('y', length=8, width=2, which='major')
ax.tick_params('y', length=6, width=1, which='minor')
handles,labels = ax.get_legend_handles_labels()
l = plt.legend(handles[:2],labels[:2],fontsize = 28, loc='upper right', frameon=False)
l.remove()

plt.subplot(grid[0, 1])
ax=sns.boxplot(data=data_37,x='crosslinker',y='phi_(rad)',palette="colorblind",hue ='collagen',showfliers=False, )
ax=sns.stripplot(data=data_37,x='crosslinker',y='phi_(rad)',size = 6,color='0',hue ='collagen',dodge=True)
ax.yaxis.set_minor_locator(tck.AutoMinorLocator(3))
plt.xlabel("Crosslinker concentration [mM]", fontsize= 38,labelpad=5)
plt.ylabel("\u03A6 (rad)", fontsize= 40,labelpad=5)
plt.xticks(fontsize= 37) 
plt.yticks(fontsize= 37)
plt.ylim (-0.05,0.5)
ax.tick_params('y', length=8, width=2, which='major')
ax.tick_params('y', length=6, width=1, which='minor')
handles,labels = ax.get_legend_handles_labels()
l = plt.legend(handles[:2],labels[:2], fontsize = 25, title_fontsize = 25, title = "collagen [mg/ml]", loc='upper right', frameon=False)
plt.savefig('C:/Users/srboval1/IPN_revision/IPN_compared_20C.tif', bbox_inches='tight',dpi=300)

plt.savefig('C:/Users/srboval1/IPN_revision/IPN_compared_37C.tif', bbox_inches='tight',dpi=300)

# %%
