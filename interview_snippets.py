# closure
def my_counter():
    counter: int = 0
    def inner_func() -> int:
        nonlocal counter
        counter += 1
        return counter
    return inner_func

#f = my_counter()
print(f := my_counter())
print(f())

print(f())

print(f())


# return reversed input without reversed function
def myrevert (input_val: str) -> str:
    pass

# sort dictionary
def sort_dict(mydict: dict) -> dict:
    #by key
   # return { k:mydict[k] for k in sorted(mydict.keys()) }

    # by value 
    return dict(sorted(mydict.items(),key= lambda item: item[1]))

# merge sorted arrays
def merge_sorted_arrays(list_a: list[int], list_b: list[int])-> list[int]:
    i, j = 0, 0  
    res: list[int] = []
    while i < len(list_a) and j < len(list_b):
        if list_a[i] < list_b[j]:
            res.append(list_a[i])
            i += 1
        else:
            res.append(list_b[j])
            j += 1
    else:
        res.extend(list_a[i:])
        res.extend(list_b[j:])

    return res


# fibonachi
# 0,1,1,2,3,5,8,13,21
# return N-th value
def fibo(n: int) -> int:
    if n == 0:
        return 0
    elif n < 2:
        return 1
    
    return fibo(n-1) + fibo(n-2)
        


# factorial
# returns n*n-1*n-2*
# 5! = 5*4*3*2*1 = 120  


# fizzbuzz
# [4, 12, 25, 6, 5, 11, 2, 5, 0, 9, 15, 30]
# print fizz if devidable to 3, bizz - if to 5, fizzbizz - if both


# missing item list difference
# find out the missing item?
# there is better solution with set(first)-set(second)
# and next with xor
# or just with sums of arrays and substraction 
#  list(missing)[:]

def missing_item():
    pass

# coin change
# For example, if you have coins of denominations [1, 2, 5]
# and you want to make change for 5 units, the possible combinations are:
##
##    1 + 1 + 1 + 1 + 1
##    1 + 1 + 1 + 2
##    1 + 2 + 2
##    5
##
##So, there are 4 possible combinations.
def coin_change(coins, cents):
    if cents < 1:
        return 0
 #   coins = [25, 10, 5, 1]
    # coins = [1, 2, 5]
    num_of_coins = 0
    for coin in coins:
        num_of_coins += cents/coin
        cents = cents%coin
        if cents == 0:
            break
    return num_of_coins

def coin_change_with_itertool(stuff,Target):
    import itertools

  #  stuff = [25, 10, 5, 1] #[1, 2, 3]
   # Target = 31
    for L in range(0, len(stuff)+1):
        for subset in itertools.combinations(stuff, L):
            if sum(subset) == Target:
                print(subset)

def coin_change_chatgpt(coins, amount): # there is an error - returns 1 less
    # Initialize a list to store the number of combinations for each
    # amount from 0 to amount
    dp = [0] * (amount + 1)
    dp[0] = 1  # Base case: there's one way to make change for amount 0
    
    # Iterate through each coin denomination
    for coin in coins:
        # Update dp array for each amount from coin to amount
        for i in range(coin, amount + 1):
            dp[i] += dp[i - coin]
    
    return dp[amount]


def coin_change_myself(coins: list[int], amount: int) -> int:
    import itertools
    
    res: set = set()

    for i in range(len(coins) + 1):
        for subset in itertools.combinations(coins,i):
            if sum(subset) == amount:
               print (subset) 
               subset = sorted(subset)
               res.add(tuple(subset))

    print ("res: ",res)
    return len(res)

# Example usage:
coins = [25, 10, 10, 1,5,5,2,3,2,31]
amount = 31
print ("Number of combinations mycoin: " ,coin_change_myself(coins,amount))

# print("Number of combinations chatgpt:", coin_change_chatgpt(coins, amount))


#print("Number of combinations itertools ",coin_change_with_itertool(coins, amount))

#print(f"coin change: " , coin_change(coins,amount))


# reverse integer number
# custom case of search for polindroms
def reverse_int():
    pass


# alien language
# alphabet : b f g q
# bgq
# fpq
# fqf
# seems over my head

def alien_lang():
    pass

my_dict1 = {'a' : 1, 'b' : 2, 'c' : 3} 
my_dict2 = {'d' : 4, 'e' : 5, 'f' : 6} 

print (my_dict1 | my_dict2) # merge dicts

# print(factoreal(5))
#
#f=6
#print(f"fibibach: {f}th element is ",fibo(f))

#print (merge_sorted_arrays([1, 5, 5, 6, 7, 9, 11],[3, 4, 5, 7, 8, 10]))


print("Sorted dict:" , sort_dict({ "c":6,"b":4,"a":3,"f":6}))

#fizzbuzz([4, 12, 25, 6, 5, 11, 2, 5, 0, 9, 15, 30])
#print(missing_with_xor())
#missing_item()
#print(myrevert(""))
# perfect_squer() # check if base is perfect корень
# Define a function to sort the dictionary
# def sort_dict_with_inner_order(dictionary):
# Sample dictionary
my_dict = {
    'banana': 3,
    'apple': 2,
    'orange': 5,
    'grape': 1,
    'kiwi': 4
}

def revert_input(a: str) -> str:
    return a[::-1]

def revert_number(num):
 """Reverts the digits of a positive integer.

 Args:
     num: A positive integer.

 Returns:
     The reverted integer.
 """
 reversed_num = 0
 while num > 0:
   digit = num % 10
   reversed_num = reversed_num * 10 + digit
   num //= 10
 return reversed_num

# Example usage
number = 1234
reversed_number = revert_number(number)
print(reversed_number)  # Output: 4321


print(revert_input('abcd'))