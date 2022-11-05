#!/usr/bin/env python
# coding: utf-8

# In[9]:


import numpy as np
number = np.random.randint(1,101)     # the computure guessed the number
predict = int(input())                # I guessed the number
def guess_number(number, predict):    # the function compeares numbers
    high = 100
    low = 1 
    count = 0
    
    while True:
        if predict > number:           # if my number bigger, than the number of computure
            high = predict              # my number becomes the largest number in the range
            predict = (predict // 2)    # devide my number by 2, and compeare one more time 
            print("Your number is lower than predict", low, predict, high)
            count += 1                 # count times of compearing
        
        elif number > predict:         # if my number less, than the number of computure
            low = predict              # my number becomes the smallest number of the range
            predict = low + ((high-low) // 2)  # sum my number with hulf of it
            print("Your number is higher than predict", low, predict, high)
            count += 1                 # count times of compearing
        else:
            print(number)                        # we able to know, what is the computure number
            return("You had", count, "guesses")  # we able to know, how many times code tryed guessing the computure number
            break
            
print(guess_number(number, predict))


# In[ ]:





# In[ ]:





# In[ ]:




