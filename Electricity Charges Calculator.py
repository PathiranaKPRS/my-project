#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Units = int(input("enter the number of units consumed === "))
Fixed_Charge = 540.00
if(Units<=26):
    Cost = Units * 7.85
elif(Units<=52):
    Cost = 204.10 + ((Units-26) * 7.85)
elif(Units<=78):
    Cost = 408.20 + ((Units-52) * 10.00)
elif(Units<=104):
    Cost = 668.2 + ((Units-78) * 27.75)
elif(Units<=156):
    Cost = 1389.70 + ((Units-104) * 32.00)
elif(Units>=157):
    Cost = 3053.70 + ((Units-156) * 45.00)
Total = Fixed_Charge + Cost
print("Your Electricity Bill for the Month is Rs.",Total)


# In[ ]:





# In[ ]:




