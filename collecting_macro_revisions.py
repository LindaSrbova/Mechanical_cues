# %%
from datetime import time
from matplotlib import markers
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns
import glob  
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
paths = glob.glob('C:/Users/srboval1/IPN_revision/macro/*.csv')
print(paths)
new =[]
for path in paths:
    x = pd.read_csv(path,encoding='utf-8', sep=';',decimal=',')
    x['repeat']=path.split("_")[-1].strip('.csv')
    x['crosslinker']=path.split("_")[-2].strip('mM')
    x['type']='ipn'
    x['temperature']='20'

    df = pd.DataFrame(x)
    new.append(df)
new = pd.concat(new)
new = new.drop(columns=['Strain Hardening Index','Shear Strain.1','Shear Stress'])

new_80 = (new.loc[new['Time'] == 80])

new_80.to_csv("C:/Users/srboval1/IPN_revision/revision_macro_collagen2_temperature20.csv", index=False)
#%%
grid = plt.GridSpec(1, 2, wspace=0.25, hspace = 0.5)
plt.figure(figsize = (25, 10),facecolor='white',dpi=300)
plt.subplot(grid[0, 0])
order = ['5', '10', '20'] 
ax=sns.scatterplot(data=new_70,x='crosslinker',y='Complex Shear Modulus',palette="colorblind",hue ='crosslinker')

ax.yaxis.set_minor_locator(tck.AutoMinorLocator(3))
plt.xlabel("Crosslinker concentration [mM]", fontsize= 38,labelpad=5)
plt.ylabel("|G*|", fontsize= 40, labelpad=5)
plt.xticks(fontsize= 37) 
plt.yticks(fontsize= 37) 
plt.ylim (1,1500)
#plt.yscale("log")
ax.tick_params('y', length=8, width=2, which='major')
ax.tick_params('y', length=6, width=1, which='minor')
handles,labels = ax.get_legend_handles_labels()
l = plt.legend(handles[:2],labels[:2])
l.remove()

#%%
sns.lineplot(data=(new.loc[new['crosslinker'] == '5']),x='Time', y='Complex Shear Modulus', legend=False)
sns.lineplot(data=(new.loc[new['crosslinker'] == '10']),x='Time', y='Complex Shear Modulus', legend=False)
sns.lineplot(data=(new.loc[new['crosslinker'] == '20']),x='Time', y='Complex Shear Modulus', legend=False)

plt.ylim (1,1200)
plt.xlim (1,90)

z<# %%
