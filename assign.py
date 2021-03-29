#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 10:02:32 2020

@author: dhruv
"""

marks = int(input('Enter your marks: '))

if(marks>=75):
    print('Distinction')
elif(marks>=65 and marks<75):
    print('Firstclass')  
elif(marks>=55 and marks<65):
    print('2nd class')    
elif(marks>=45 and marks<55):
    print('3rd class')  
elif(marks>=35 and marks<45):
    print('Passing marks')     
elif(marks>=1 and marks<35):
    print('You are failed')    
else:
    print('You are enter wrong imformation')     
    
cname = input('Enter your city name: ')   
count = int(input('Enter total number of positive cases: '))

if(count>=1000000):
    print('Your city '+cname+)
    
1 1 1 1 1
2 2 2 2 2 
3 3 3 3 3 
4 4 4 4 4 
5 5 5 5 5     
    
for i in range(1,6):
    for j in range(1,6):
        print(i,end=" ")
      print()
      
      
#
@ @
# # #
@ @ @ @
# # # # # 
@ @ @ @ @ @ 

for i in range(1,7):
    for j in range(1,i+1):
        if(i%2==1):
            print('#',end=" ")
        else: 
            print('@',end=" ")   

i = 1
while(i<6):
   print('i= ',i)
   i += 1
print('Out of loop')  





1 1 1 1 1
2 2 2 2 2 
3 3 3 3 3 
4 4 4 4 4 
5 5 5 5 5     
    
for i in range(1,6):
        for j in range(1,6):
                    print(i,end=" ")
        print()
                
num = int(input('Enter your number: '))
temp = 0        
for i in range(2,num):
    if(num % i == 0):
        temp = 1
        break
if(temp == 1):
    print('Number is not prime')
else:
    print('Number is prime')


    
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
            
m,n = 1,1
print(m,n,end=" ")

for i in range(1,9):
    o = m + n
    m = n
    n = o
    print(o,end=" ")
    
m,n = 4,5
temp = m
m = n
n = temp

print("m = ",m)
print("n = ",n)   

l1 = [1,"GUNI",90.5,"Mehsana"] 
t1 = (1,"GUNI",90.5,"Mehsana") 

l1.insert(2,"CE IT CE-AI")    
print(l1)                   
del l1[2]
print(l1)
            
 
            
t1.insert(2,"CE IT CE-AI")                       
print(t1)   
            
t1 = (1,"GUNI",90.5,"Mehsana","Python","UVPCE",1997)       
print(t1[0:4])    
            
print(t1[5:])
            
t1 =  t1[0:4] + t1[5:]   
print(t1) 

d1 ={"rank":1,"UNI_name":"GUNI","Year":1997}    
print(type(d1))  
print(d1.keys())
print(d1.values())
d1["clg"] = "UVPCE"
print(d1)

d1.pop("clg")
d1.popitem()
print(d1.items())
print(d1)

a = 1
b = 2
a = a + b
b = a - b
print(a)
print(b)         
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
    