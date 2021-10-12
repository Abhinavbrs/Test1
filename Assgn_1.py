from Myfunc import *

import numpy

class MyError(Exception):

    def __init__(self, value):
        self.value = value
 
    def __str__(self):
        return(repr(self.value))

#main
if __name__=="__main__":
    
    generate("./empdata",10)
    
    try:
        empdata=read("./empdata")
    except FileNotFoundError:
        print("File path doesn't exist")

    func=lambda x: (x,empdata[x])
    lt=[func(x) for x in empdata]
    print(lt)

    emplist=mergeSort(list(empdata.items()))

    try:
        Empid=int(input("Enter ID"))
    except ValueError:
        print("Invalid ID")
        Empid=int(input("Enter valid ID"))

    while True:
        try:
            if search(emplist, 0, len(emplist)-1, Empid)==-1:
                raise MyError("Wrong ID")
            else:
                print(search(emplist, 0, len(emplist)-1, Empid))
                break
        except MyError:
            print("Nonexistent ID")
            Empid=int(input("Enter existing ID"))
