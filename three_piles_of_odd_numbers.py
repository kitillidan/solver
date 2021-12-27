import math
from itertools import combinations

marbles = int(input("Enter an odd number of at least 3: "))
piles = 3
N = (marbles-piles)/2 
n = N 
ways = 0

inflection = math.ceil((marbles-3)/2/2)

print("{:<13} : {:<12}".format("Largest pile","ways to put"))

while n>=(N/piles):
    if (N-n)<=n: 
        w = int((N-n)/2) + 1
    elif (N-n)>n: 
        w = int(n - (N-n)/2 + 1) 

    print("{} ({}){:6} : {}".format(int(n*2)+1, int(n), "", w), end="")
    print("  <-- Inflection") if n==inflection else print()

    ways = ways + w 
    n = n - 1

print("There are a total of {ans} ways to put {marbles} marbles in {piles} piles of odd numbers.".format(marbles=marbles, piles=piles, ans=ways))

total_ways = math.ceil( ( len(list(combinations(range(1, int((marbles+1)/2) + 1), 2))) - inflection*3 ) / 6 + inflection )

print("Total ways by formula = {}".format(total_ways))
