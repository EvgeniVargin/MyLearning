#Created by Evgeniy Vargin for learning

from tkinter import *
from initdata import *
#import pandas as pd

flds = {'key': 'Ид:','name': 'Ф.И.О.:','job': 'Дожность:','age': 'Возраст:','salary': 'Заработная плата:','bonus': 'Бонус:'}

class SaveBtn(Button):
    def __init__(self,Owner,Text,Rn):
        Button.__init__(self,Owner,text=Text)
        self.owner = Owner
        self.text = Text
        self.rn = Rn
    
    def getRn(self):
        return self.rn

class Container:
    def __init__(self):
        self.items = []
    
    def items(self):
        return self.items
    
    def addItem(self,obj):
        self.items.append(obj)
        return len(self.items) - 1
    
    def getItemByNum(self,num):
        try:
            return self.items[num]
        except:
            return None
    
    def getItemAsString(self,num):
        try:
            return str(self.items[num])
        except:
            return None
        
    

class MainGrid(Frame):
    def __init__(self,Owner,Dataset,Fields):
        Frame.__init__(self,Owner)
        self.owner = Owner
        self.dataset = Dataset
        self.fields = Fields
        self.cont = Container()
        self.rebuild()
    
    def getContainer(self):
        return self.cont
        
    def rebuild(self):
        tk = self.owner
        tk.title("Список сотрудников:")
        self.pack(fill=BOTH,expand=1)
        self.columnconfigure(len(self.fields) + 1,weight=1)
        self.rowconfigure(len(self.dataset) + 2,weight=1)
        rownum = self.cont.addItem([])
        for (num,key) in enumerate(self.fields):
            self.cont.getItemByNum(rownum).append(Label(self,text=self.fields[key]).grid(row = 0,column=num,padx=1,pady=1))
        for (idx,key) in enumerate(self.dataset):
            rownum = self.cont.addItem([])
            self.cont.getItemByNum(rownum).append(self.dataset[key])
            e = []
            for (num,field) in enumerate(self.fields):
                #r.append(self.dataset[key].asDict()[field])
                ent = Entry(self)
                ent.grid(row = idx+1,column=num,padx=1,pady=1)
                ent.insert(0,self.dataset[key].asDict()[field])
                e.append(ent)
            self.cont.getItemByNum(rownum).append(e)
            b = SaveBtn(self,Text='Save (%s)'%key,Rn=rownum)
            b.bind('<Button-1>',saveRecord)
            b.grid(row=rownum,column=len(self.fields) + 1,padx=1,pady=1)
            self.cont.getItemByNum(rownum).append(b)

def saveRecord(event):
    for (num,field) in enumerate(flds):
        setattr(event.widget.owner.getContainer().getItemByNum(event.widget.getRn())[0],field,event.widget.owner.getContainer().getItemByNum(event.widget.getRn())[1][num].get())
    EmpTable.setRow(event.widget.owner.getContainer().getItemByNum(event.widget.getRn())[0])
    #print(event.widget.owner.getContainer().getItemByNum(event.widget.getRn())[0])
    #print(event.widget.getRn())

def main():
    root = Tk()
    root.geometry("1024x768")
    tbl = EmpShelve
    ds = tbl.open()
    #bob = tbl.setRow(Developer('bob','Bob Smith',42))
    #sue = tbl.setRow(Hardware('sue','Sue Johns',45))
    #tom = tbl.setRow(Manager('tom','Tom Kite',50,salary=100000.0,bonus=0.05))
    #john = tbl.setRow(Engineer('john','John Doe',42))
    #kate = tbl.setRow(DataScientist('kate','Kate Patrow',22))
    app = MainGrid(root,ds,flds)
    
    ds.close()
    #
    root.mainloop()

if __name__ == '__main__':
    
    main()

    """
    tbl = EmpTable
    print('*************** Table Begin ***************')
    db = tbl.open()
    for key in db:
        print(db[key])
    db.close()
    print('***************  Table End  ***************')
    """

