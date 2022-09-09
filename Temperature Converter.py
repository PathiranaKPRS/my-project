#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Degree = float(input("Input the Degree of the temperature:"))
Measure = str(input("Input the Type of your degree ( F or C ):"))

if Measure =="C":
    
    Calc = float(Degree * 9/5) + 32
    print("The temperature is",str(Calc) ,"in Fahrenheit.")

elif Measure =="F":
    
    Calc = float((Degree)- 32) * 5/9
    print("The temperature is",str(Calc) ,"in Celsius.")
    
else:
    
    print("Wrong input. Try again") 

