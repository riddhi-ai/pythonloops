"""
i =0
while i < 10:
    if i == 5:
        continue
    print(i)
    i +=1  
    (this contains bug it runs infinite loop)
"""
#to solve bug we need to add increment before continue keyword

i =0
while i < 10:
 if i==5:
  i+=1
  continue
 print(i)
 i +=1 
    
  
   