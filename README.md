# My Approach

I used dictionaries because of their constant time complexity properties for pop, push, and insertions.  I used an ordered dictionary so that I can get a queue for the printing priority requirements of the challenge.  I popped the dictionary when entries exceeded their inactivity time to reduce space complexity.  A priority heap could have been used to reduce the time complexity perhaps further.  To make the code more scalable and portable, I would have created a class. 

# My dependacies 
+ helperFunctions
  + Functions for editing, cleaning, formatting
+ sys 
+ collections
+ datetime


