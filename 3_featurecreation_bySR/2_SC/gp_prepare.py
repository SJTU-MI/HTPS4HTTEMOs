#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import os, re
import shutil

# Source path 
source_py = './copy_file/gp_SC.py'


# In[2]:


def alter(filename,old_str,new_str):

    file_data = ""
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            if old_str in line:
                line = line.replace(old_str,new_str)
                # print(filename,' has been converted successfully')
            file_data += line
    with open(filename,"w",encoding="utf-8") as f:
        f.write(file_data)


# In[3]:


dir_i = 1
for pc in np.arange(0.40,0.86,0.05):
    pc_round = (round(pc,2))
    max_value = (0.99-pc_round)/2
    min_value = (0.99-pc_round)/3
    for ps in np.arange(min_value,max_value,0.01):
        ps_round = (round(ps,2))
        for ph in np.arange(min_value,max_value,0.01):
            for random_state_i in range(0,3):
                ph_round = (round(ph,2))
                pp_round = round(0.99-pc_round-ps_round-ph_round,2)
                file_dir = './'+str(dir_i)
                os.makedirs(file_dir,exist_ok=True)
                print(dir_i,random_state_i,pc_round,ps_round,ph_round,pp_round)
                file_dir_py = file_dir+'/'+'gp_SC.py'
                shutil.copy(source_py,file_dir_py)
                alter(file_dir_py,"pc_round_set",str(pc_round))
                alter(file_dir_py,"ps_round_set",str(ps_round))
                alter(file_dir_py,"ph_round_set",str(ph_round))
                alter(file_dir_py,"pp_round_set",str(pp_round))
                alter(file_dir_py,"random_state_set",str(random_state_i))
                dir_i = dir_i+1

