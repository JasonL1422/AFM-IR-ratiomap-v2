#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#https://matplotlib.org/stable/gallery/index.html

"""
@author: jongcheol1422@gmail.com
"""
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#inputs---import---'directory--------------------------------------------------
lx = 5 # um (scanned area)
ly = 5 # um (scanned area)
nx = 256 #sample / line
ny = 256 #lines
cur_dir = os.getcwd()
dat_dir = os.path.join(cur_dir,'sample data') #file directory
all_files = os.listdir(dat_dir)
#print(cur_dir)
#print(dat_dir)
#print(all_files)

#file read---txt---------------------------------------------------------------
dat_frame=[]
dat_filename=[]
for ind_file in all_files:                         
    file_path = os.path.join(dat_dir,ind_file)     #os.path.join(a,b) to read ind files in the dir
    if ind_file.endswith('.txt'):                  
        df = pd.read_table(file_path)              
        dat_frame.append(df)                       
        dat_filename.append(ind_file)

#rearrange data---save---inf---------------------------------------------------
reshaped_alldat = []
for i, df in enumerate(dat_frame):      #enumerate adds a counter --> index (i) and value (df)
    print(f"---------------[{dat_filename[i]}]---------------")
    print(f"dim: {df.shape}")
    #print(f"info:{df.info()}")
    #print(df.head())
    #print(f"dimension: ({df.shape[0]},{df.shape[1]})")
    reshaped_data = df.to_numpy().reshape((ny, nx))
    reshaped_alldat.append(reshaped_data)
    print(f"reshaped data dim: {reshaped_data.shape}")

r1151 = reshaped_alldat[0]
r1034 = reshaped_alldat[1]
r1160 = reshaped_alldat[2]
print(f"dimension: {r1151.shape}")

#ratio---function---def---cuts-------------------------------------------------
def ratio(aa, bb):
    cut1=0
    cut2=1000
    ny, nx = aa.shape
    temp = np.zeros((ny, nx))  # matrix with zeros

    for i in range(ny):
        for j in range(nx):
            if cut1 < aa[i, j] / bb[i, j] < cut2:
                temp[i, j] = aa[i, j] / bb[i, j]
            else:
                temp[i, j] = 0

    return temp

ir1034ov1160 = ratio(r1034, r1160)
ir1034ov1151 = ratio(r1034, r1151)
ir1151ov1160 = ratio(r1151, r1160)

#plot---def--------------------------------------------------------------------
def plot1(ddd,name,gap):
    plt.figure(figsize=(6, 6), dpi=300)
    plt.contourf(ddd, cmap='rainbow', levels=gap)
    plt.colorbar(label='Intensity', shrink=0.8)
    plt.title(f"{name}")
    plt.xticks(np.linspace(-1, nx-1, num=6), np.linspace(0, lx, num=6))
    plt.yticks(np.linspace(0, ny, num=6), np.linspace(0, ly, num=6))
    plt.xlabel('X (µm)')
    plt.ylabel('Y (µm)')
    aratio = nx/ny
    plt.gca().set_aspect(aratio, adjustable='box')
    plt.show()

def plot2(ddd,name,min_val,max_val,gap):
    plt.figure(figsize=(6, 6), dpi=300)
    lev=np.linspace(min_val,max_val,gap)
    plt.contourf(ddd, cmap='rainbow', levels=lev)
    plt.colorbar(label='Intensity', shrink=0.8)
    plt.title(f"{name}")
    plt.xticks(np.linspace(0, nx, num=6), np.linspace(0, lx, num=6))
    plt.yticks(np.linspace(0, ny, num=6), np.linspace(0, ly, num=6))
    plt.xlabel('X (µm)')
    plt.ylabel('Y (µm)')
    aratio = nx/ny
    plt.gca().set_aspect(aratio, adjustable='box')
    plt.show()
    
#plot--------------------------------------------------------------------------

plot1(r1034,"1034 cm-1",100)
plot1(r1160,"1160 cm-1",100)
plot1(r1151,"1151 cm-1",100)

plot2(ir1034ov1160,"1034 cm-1/1160 cm-1",0.5,2,100)


#storage-----------------------------------------------------------------------
"""
#plot all
for i, jj in enumerate(reshaped_alldat):    
    plt.figure(figsize=(6, 6))
    plt.contourf(jj, cmap='rainbow', levels=50)
    plt.colorbar(label='Intensity')
    plt.title(f"{dat_filename[i].split('.')[0]} cm-1")
    plt.xticks(np.linspace(-1, nx-1, num=6), np.linspace(0, lx, num=6))
    plt.yticks(np.linspace(0, ny, num=6), np.linspace(0, ly, num=6))
    plt.xlabel('X (µm)')
    plt.ylabel('Y (µm)')
    plt.gca().set_aspect('equal', adjustable='box') #aspect ratio=1
    plt.show()

def iplot(ddd,gap):
    plt.figure(figsize=(6, 6))
    plt.contourf(ddd, cmap='rainbow', levels=gap)
    plt.colorbar(label='Intensity')
    plt.title(f"{dat_filename[i].split('.')[0]} cm-1")
    plt.xticks(np.linspace(-1, nx-1, num=6), np.linspace(0, lx, num=6))
    plt.yticks(np.linspace(0, ny, num=6), np.linspace(0, ly, num=6))
    plt.xlabel('X (µm)')
    plt.ylabel('Y (µm)')
    plt.gca().set_aspect('equal', adjustable='box') #aspect ratio=1
    plt.show()

"""
