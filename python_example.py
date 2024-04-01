import requests

URL = "https://www.amazon.com/nothing_here"

def call_url(URL: str) -> None:
    
# https://www.w3schools.com'

    try:
        ret = requests.get(URL)
        ret.raise_for_status()
        print(f'{ret.status_code}')
    except requests.exceptions.HTTPError as err: 
        print(ret)
        print(err)


def fuzzBuzz(n: int) -> None:
    for i in range(1,n+1):
        if i % 3 == 0 and i % 5 == 0:
            print("fuzzbuzz")
        elif i % 3 == 0:
            print("fuzz")
        elif i % 5 == 0 :
            print("buzz")    
        else:
            print(str(i))

# fuzzBuzz(30)
            
         #   https://realpython.com/sort-python-dictionary/#rediscovering-dictionary-order-in-python

# Sort a dictionary alphabetically with an inner order 
mydict = {"c" : "third",
    "a" : "first",
    "d" : "fourth",
    "f" : "sixth",
    "e" : "fith",
    "b" : "second",
}

sorted_keys=sorted(mydict)
sorted_mydict= { k: mydict[k] for k in sorted_keys }

print("Sorted by value: ",dict(sorted(mydict.items(), key=lambda item: item[1])))


print("sprtted dict ",sorted_mydict)



""" mydict["z"] = "seventh"
del(mydict["c"])
mydict["c"] = "third" """
print (mydict)

people = {3: "Jim", 2: "Jack", 4: "Jane", 1: "Jill"}

numbers = [5, 3, 4, 3, 6, 7, 3, 2, 3, 4, 1]
sorted_num = sorted(numbers)

print(sorted_num)


# Sample dictionary
my_dict = {
    'banana': 3,
    'apple': 2,
    'orange': 5,
    'grape': 1,
    'kiwi': 4
}

# Define a function to sort the dictionary
def sort_dict_with_inner_order(dictionary):
    # First, sort the keys alphabetically
    sorted_keys = sorted(dictionary.keys())
    
    # Then, sort the values based on the inner order (ascending in this case)
    sorted_dict = {key: dictionary[key] for key in sorted_keys}
    
    return sorted_dict

# Call the function to sort the dictionary
sorted_dict = sort_dict_with_inner_order(my_dict)

# Print the sorted dictionary
for key, value in sorted_dict.items():
    print(key, ':', value)

from operator import itemgetter

print("sorted array: ", dict(sorted(mydict.items(),key=lambda value: value[1])))


class Monkey:
    def patch(self):
          print ("patch() is being called")

def monk_p(self):
    print ("monk_p() is being called")

def monkey_patch(self):
    print(f"monkey {monkey_patch.__name__}")

# replacing address of "patch" with "monk_p"
Monkey.patch = monk_p
Monkey.patch = monkey_patch

obj = Monkey()

obj.patch()
# monk_p() is being called

def is_perfect_square(num):
    # Edge case: if num is negative, it's not a perfect square
    if num < 0:
        return False
    
    # Take the square root of num
    sqrt_num = num ** 0.5
    
    # Check if the square root is an integer
    if sqrt_num.is_integer():
        return True
    else:
        return False


# Example usage:
print(is_perfect_square(25))  # Output: True
print(is_perfect_square(8))  # Output: False