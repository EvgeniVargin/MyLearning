# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 21:27:03 2019

@author: Evgeniy Vargin
"""

import shelve

class EmpTable:
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
    
class Manager(Employee):
    def __init__(self,key,name,age,salary=80000.0,bonus=0.1):
        Employee.__init__(self,key=key,name=name,age=age,job='Manager',salary=salary + salary * bonus,bonus=bonus)

class Developer(Employee):
    def __init__(self,key,name,age,salary=30000.0,bonus=0.0):
        Employee.__init__(self,key=key,name=name,age=age,job='Developer',salary=salary + salary * bonus,bonus=bonus)

class Hardware(Employee):
    def __init__(self,key,name,age,salary=50000.0,bonus=0.0):
        Employee.__init__(self,key=key,name=name,age=age,job='Hardware',salary=salary + salary * bonus,bonus=bonus)

class Engineer(Employee):
    def __init__(self,key,name,age,salary=60000.0,bonus=0.0):
        Employee.__init__(self,key=key,name=name,age=age,job='Engineer',salary=salary + salary * bonus,bonus=bonus)

        
class DataScientist(Employee):
    def __init__(self,key,name,age,salary=60000.0,bonus=0.0):
        Employee.__init__(self,key=key,name=name,age=age,job='DataScientist',salary=salary + salary * bonus,bonus=bonus)
