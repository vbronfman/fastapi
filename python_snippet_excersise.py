# python snippets memorising 
from itertools import combinations

def coins_charge(coins: list[int], total_amount: int) -> None:
  ''' Calculates number of possible charge back with given set of coins
      Requires itertools combinations
  '''
  res = set()

  for num_of_coins in range(1,len(coins)+1):
    print(f"{num_of_coins=}")
    
    for subset in combinations(coins,num_of_coins):
     # print("{0}".format(list(subset)))
      if sum(subset) == total_amount:
        print(subset)
        res.add(subset)
        
  print(len(res))
   

coins = [5,5,3,1,1,2,1,2]

coins_charge(coins,15) # +

fizz_buzz 
