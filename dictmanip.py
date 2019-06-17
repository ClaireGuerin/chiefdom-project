#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 17:17:51 2019

@author: claire
"""

def extract(d, keys):
    """creates a subset of a given dictionary, keeping requested keys only"""
    return dict((k, d[k]) for k in keys if k in d)