#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 18:14:05 2018

@author: rohankamath
"""

import matplotlib.pyplot as plt
import numpy as np


mercury_pos=[7.86, 7.96, 11.77, 28.2 ,36.6, 48.95, 72.35, 73.15, 83.14, 108.35, 120.22]
Mercury = [2.22471E-7, 2.25279E-7, 2.26222E-7, 2.53652E-7, 2.84768E-7, 2.96728E-7, 3.13155E-7, 3.13184E-7, 3.20817E-7, 3.53259E-7, 3.65015E-7]
A= np.polyfit(mercury_pos, Mercury, 4)


def fit(x,coeff):
    return coeff[0]*(x**4) +coeff[1]*(x**3) + coeff[2]*(x**2) + coeff[3]*(x**1) + coeff[4]

pos = np.linspace(0,140,100)
wave = fit(pos,A)

#plt.plot(pos, wave, color = 'r', )
#plt.scatter(mercury_pos, Mercury)
#plt.ylim(2e-7,4e-7)
#plt.xlabel("Position (mm)")
#plt.ylabel("Wavelength (m)")
#plt.title("Mercury Calibration Curve")
#plt.savefig("Mercury.png")

"""
The following wavelengths were found on running the values of positions (ref Lab book) through the 
fit function
lam1 and lam3 could not be identified, but have been included for completeness sake.
"""
lam1 = 2.2613225615918783e-07 #No ID
lam2 = 2.5692901474038756e-07 #5 - 2s
lam3 = 2.6895371464826016e-07 #No ID
lam4 = 2.7997984128703803e-07 # 4 - 2s
lam5  = 2.8220850594625837e-07 #CNBI
lam6 = 3.392310181973236e-07 #3- 2s
lam7 = 2.5074125938245427e-07 # 6 - 2s
lam8 = 3.793822661802875e-07 #6-2p
lam9 = 3.9149278924280027e-07 #5-2p
lam10 = 4.132295190125242e-07# 4- 2p


lamerr = 1.18e-8 #error in lambda
lamdiffuse =  [lam8,lam9,lam10] #diffuse spectra
lamprincipal = [lam7, lam2, lam4, lam6] #principal spectra
oneoverlamerrprincipal = []
oneoverlamdiffuse  = []
oneoverlamerrdiffuse = []
oneoverlamprincipal = []
for i in lamdiffuse:
    oneoverlamerrdiffuse.append(lamerr/((i)**2))
    oneoverlamdiffuse.append((1/i))
oneoverndiffuse = [(1/36), (1/25),(1/16)]

for i in lamprincipal:
    oneoverlamerrprincipal.append(lamerr/((i)**2))
    oneoverlamprincipal.append((1/i))  
oneovernprincipal = [(1/36), (1/25),(1/16),(1/9)]

diffuse = np.polyfit(oneoverlamdiffuse, oneoverndiffuse, 1)
principal = np.polyfit(oneoverlamprincipal, oneovernprincipal, 1)
ryd = 10973731.6
quants = 2 - np.sqrt(ryd/(-1*principal[1]/principal[0]))
quantp = 2 - np.sqrt(ryd/(-1*diffuse[1]/diffuse[0]))

print(quants)
print(quantp)