#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 12:44:07 2019

@author: claire
"""
import numpy as np
import lifecycle as lc
                 
# Initial conditions and parameters     
phen = [np.array([[0.4],[0.5]]),np.array([[0.1],[0.2],[0.3]]),np.array([[0.6],[0.7],[0.8],[0.9]])]
env = []
for i in phen: env.append([len(i)])
                
parsDict = {'probability mutation':0.5, 
            'mutation step':[0.2], 
            'density competition':0.1, 
            'basal fertility':2, 
            'cooperation cost':0.05, 
            'cooperation benefit':0.5, 
            'dispersal rate':0.5, 
            'demes number':len(phen), 
            'mutation correlation coefficient':0}    

lc.lifeCycle([phen,env],parsDict)