# Generator function with yield even no. to a specified limit


def even_generator(limit):
   
   for i in  range(2,limit + 1,2):
      yield i # generate the value and make sure where it is placed in memory and also store it's state
    #   it will place it in state and memory

#  these both function should be inside different memory 

for num in even_generator(10):
   print(num)