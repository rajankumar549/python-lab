import random

random.seed( -25 )
print ("Random number with seed 10 : ", random.random())

# It will generate same random number
random.seed( 5 )
print( "Random number with seed 10 : ", random.random())

# It will generate same random number
random.seed( 11 )
print ("Random number with seed 10 : ", random.random())