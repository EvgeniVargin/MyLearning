#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 23:06:35 2020

@author: administrator
"""

import psycopg2
import pandas as pd

connections = []

def pgSetConnect(inDB,inUser,inPwd,inHost='localhost'):
    connections.append(psycopg2.connect(dbname=inDB, user=inUser,password=inPwd, host=inHost))
    #connections[len(connections) - 1].row_factory = dict_factory
    return connections[len(connections) - 1]
        
def getConnect(num):
    return connections[num]

def closeConnect(num):
    connections[num].close()