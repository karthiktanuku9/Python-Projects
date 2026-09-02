#Password generator
# import random module

import random

# User defined number of characters in that password

n=int(input("Enter a number : "))

#List of all small alphabet

l1=['a', 'b', 'c', 'd', 'e', 'f', 'g','h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#List of all captial alphabet

l2=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

#List of all Symbols

l3=['!','@','#','$','^','&','*','(',')','>','<',':',';','/','+','-','|']

# To not skip any type of characters 
if n < 4:
    print("Password length must be 4 or more.For stronger Password")
    exit()
# Total number charcters assigned to a dummy variable 
remaining=n

if remaining>=3:                                   # remaining >= 3 because we still got 3 more types to the password, so we leave 3 positions 
    n_A=random.randint(1,remaining-3)              # Considers a random number for capital letters
    print("Total number of Capital letters  :",n_A)
    after_n_A=remaining-n_A                        # no.of positions left after taking capital letters

if after_n_A>=2:                                   # after_n_A >= 2 because we still got 2 more types to the password, so we leave 2 positions
    n_a=random.randint(1,after_n_A-2)              # Considers a random number for small letters
    print("Total number of Small letters :",n_a)
    after_n_a=after_n_A-n_a                        # No. of positions left after taking small letters

if  after_n_a>=1:                                  # after_n_a >= 1 because we still got 1 more type (digits), so we leave 1 position
    n_s=random.randint(1,after_n_a-1)              # Considers a random number for symbols
    print("Total number of Symbols :",n_s)
    after_n_s=after_n_a-n_s                        # No. of positions left after taking symbol
d=after_n_s                                        # Rest of the positions for digits
print("Total number of digits :",d)

l4=[]                                              # Empty list to append and shuffle the output

for i in range(1,n_a+1):                           
        sa=random.choice(l1)                       # Randomly chooses an alphabet from list 1
        l4.append(sa)                              # Append all small letters

for i in range(1,n_A+1):                           
        cA=random.choice(l2)                       # Randomly chooses an alphabet from list 2
        l4.append(cA)                              # Append all capital letters
    
for i in range(1,n_s+1):                          
        sy=random.choice(l3)                       # Randomly chooses an symbol from list 3
        l4.append(sy)                              # Append all symbol
        
for i in range(1,d+1):                             
        di=random.randint(0,9)                     # Randomly chooses a number from range (0,9)
        k=str(di)                                  # Converts integer to string for joining
        l4.append(k)                               # Append all digits
print("\n")
random.shuffle(l4)
j="".join(l4)                                      # Joins the list elements into a single password string                                 
print("Final Password =",j)