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

parser = argparse.ArgumentParser(
                    prog='gen',
                    description='gen csv')
parser.add_argument('-p','--path',required=True,help='Path to the root H:/Linda/SoftMatter_new/rewievs/20')
parser.add_argument('--collagen','-c',required=True,
                    action="store")
parser.add_argument('--temperature','-t',required=True,
                    action="store")

args = parser.parse_known_args()[0]
paths = glob(os.path.join(args.path,'*/S*/results/summary_ID_level.csv'))
collagen = args.collagen
temperature = args.temperature
print(paths)

a = []
names2 = []
day_repeats = []
for i in paths:
    splitted = os.path.split(os.path.split(i)[0])[0]
    j = glob(os.path.join(splitted,'24*'))[0]
    k = os.path.split(j)[-1][2:4]
    tmp = pd.read_csv(i)
    tmp['info'] = i
    names2.extend([k]*tmp.shape[0])
    print(int(os.path.split(splitted)[1][-1:])-1)
    day_repeats.extend([int(os.path.split(splitted)[1][-1:])-1]*tmp.shape[0])
    a.append(tmp)

a = pd.concat(a)
a['radius_(m)'] *= 1e6
a = a.rename(columns={'radius_(m)':'radius_(um)'})

names = np.stack(a['info'].apply(lambda x: x.split('\\')[-4:-2]).values)
        
a['day2'] = names2
a['size'] = 30
a['coating_type'] = 'plain'
a['crosslinker'] = np.array([float(i.split('_')[-1].strip('mM')) for i in names[:,0]])
a['day_repeat'] = day_repeats
a['type'] = 'ipn'
a['collagen'] = collagen
a['temperature'] = temperature

if os.path.exists('C:/Users/srboval1/IPN_revision/revision.csv'):
    a_new = pd.DataFrame(a)
    a_new.to_csv('C:/Users/srboval1/IPN_revision/revision.csv', mode='a', index=False, header=False)
else:
    a.to_csv("C:/Users/srboval1/IPN_revision/revision.csv", index=False)
    
