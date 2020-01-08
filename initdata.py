# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 21:27:03 2019

@author: Evgeniy Vargin
"""

import shelve
import pickle as pck

def dictRectangle(inDict):
    result = {}
    #Сформируем список всех Ид
    ids = []
    for (x,xkey) in enumerate(inDict):
        if x > 0:
            break
        for ykey in inDict[xkey]:
            ids.append(ykey)
    #Сформируем словарь с пустыми словарями
    for rw in ids:
        result[rw] = {}
    #Заполним пустую матрицу значениями
    for rw in ids:
        for col in inDict:
            result[rw][col] = inDict[col][rw]
    return result

class EmpPickle:
    def __init__(self,filename='class-pickle'):
        self.filename = filename
    
    def open(filename='class-pickle'):
        result = open(filename,'rb')
        return result
    
    def close(db):
        try:
            db.close()
            result = 'Table closed successfully'
        except:
            result = 'No such table. Table not closed'

    def getRow(key,filename='class-pickle'):
        db = open(filename,'rb')
        try:
            result = db[key]
        except:
            result = None
        db.close()
        return result
    
    def setRow(rec,filename='class-pickle'):
        db = open(filename,'rb')
        try:
            if rec.key in db:
                db[rec.key] = rec
                print('%s proccessed successfully'%rec)
            else:
                db[rec.key] = rec
                print('%s added successfully'%rec)
            result = db[rec.key]
        except AttributeError:
            print('%s not Employee!'%rec)
            result = None
        #except:
        #    print('Unknown error')
        #    result = None
        db.close()
        return result
    
    def delRow(key,filename='class-pickle'):
        db = open(filename,'rb')
        try:
            del db[key]
            result = 'Row (key = %s) deleted successfully'%key
        except:
            result = 'No such row (key = %s). Not deleted'%key
        return result
    
class EmpShelve:
    def __init__(self,name='class-shelve'):
        self.name = name
        
    def open(name='class-shelve'):
        tbl = shelve.open(name)
        return tbl
    
    def close(tbl):
        try:
            tbl.close()
            result = 'Table closed successfully'
        except:
            result = 'No such table. Table not closed'
    
    def getRow(key,name='class-shelve'):
        db = shelve.open(name)
        try:
            result = db[key]
        except:
            result = None
        db.close()
        return result
    
    def setRow(rec,name='class-shelve'):
        db = shelve.open(name)
        try:
            if rec.key in db:
                db[rec.key] = rec
            else:
                db[rec.key] = rec
            result = db[rec.key]
        except AttributeError:
            result = None
        db.close()
        return result
    
    def delRow(key,name='class-shelve'):
        db = shelve.open(name)
        try:
            del db[key]
            result = 'Row (key = %s) deleted successfully'%key
        except:
            result = 'No such row (key = %s). Not deleted'%key
        return result
    
class Employee:
    def __init__(self,Key,Name,Job,Age,Salary,Bonus):
        self.key = Key
        self.name = Name
        self.job = Job
        self.age = Age
        self.salary = Salary
        self.bonus = Bonus
    
    def __str__(self):
        return '%s = "%s => %s: age = %s; salary = %s"'%(self.key,self.name,self.job,self.age,self.salary)
    
    def asDict(self):
        return {'key': self.key,'name': self.name,'job': self.job,'age': self.age,'salary': self.salary,'bonus': self.bonus}
    
    def getKey(self):
        return self.key
    
class Manager(Employee):
    def __init__(self,Key,Name,Age,Salary=80000.0,Bonus=0.1):
        Employee.__init__(self,Key=Key,Name=Name,Age=Age,Job='Manager',Salary=Salary + Salary * Bonus,Bonus=Bonus)

class Developer(Employee):
    def __init__(self,Key,Name,Age,Salary=30000.0,Bonus=0.0):
        Employee.__init__(self,Key=Key,Name=Name,Age=Age,Job='Developer',Salary=Salary + Salary * Bonus,Bonus=Bonus)

class Hardware(Employee):
    def __init__(self,Key,Name,Age,Salary=50000.0,Bonus=0.0):
        Employee.__init__(self,Key=Key,Name=Name,Age=Age,Job='Hardware',Salary=Salary + Salary * Bonus,Bonus=Bonus)

class Engineer(Employee):
    def __init__(self,Key,Name,Age,Salary=60000.0,Bonus=0.0):
        Employee.__init__(self,Key=Key,Name=Name,Age=Age,Job='Engineer',Salary=Salary + Salary * Bonus,Bonus=Bonus)

        
class DataScientist(Employee):
    def __init__(self,Key,Name,Age,Salary=60000.0,Bonus=0.0):
        Employee.__init__(self,Key=Key,Name=Name,Age=Age,Job='DataScientist',Salary=Salary + Salary * Bonus,Bonus=Bonus)
