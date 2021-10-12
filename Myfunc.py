import random
import os
import shutil
import re
import string

#generation
def generate(mypath,N):
    if(os.path.exists(mypath)):
        shutil.rmtree(mypath)
    os.mkdir(mypath)
    for i in range(N):
        empname=''.join(random.choices(string.ascii_lowercase, k = 7))
        empid=random.randint(1000000000,9999999999)
        empsal=random.randint(100000,99999999)
        f=open(f"{mypath}/{empname}.txt",'w')
        f.write(f"This is employee record for {empid} for which {empsal} amount has been credited to his account.")
        f.close()

#read
def read(mypath):
    empdata={}
    for file in os.listdir(mypath):
        if file.endswith(".txt"):
            f2=open(f"{mypath}/{file}",'r')
            line=f2.readline()
            matches=re.findall(r"[1-9][0-9]*",line)
            empdata[matches[0]]=(file[:-4],int(matches[1]))
            f2.close()
    return empdata

#sort
def mergeSort(arr):
    l=len(arr)
    if l > 1:
  
        mid = len(arr)//2
  
        L = arr[:mid]
  
        R = arr[mid:]
  
        mergeSort(L)
  
        mergeSort(R)
  
        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i][0] < R[j][0]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
  
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

#search
def search(arr, l, r, x):
    filtlist=[]
    while l <= r:
        mid = l + (r - l) // 2;
        if int(arr[mid][0]) == x:
            return arr[mid]
        elif int(arr[mid][0]) < x:
            l = mid + 1
        else:
            r = mid - 1
    return -1
