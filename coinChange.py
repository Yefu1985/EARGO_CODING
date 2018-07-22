# This is the coding for the coin problem.
# The tricky part is that the coins has "1" (penny) in the list, so for any target (amount you needed), there would
# be a valid result.So, this piece of code can be used to solve the coins which has "pennies" in it.
# Based on this, I will get the maximum count of coins from the largest one (such as 25 cents), then the maximum
# count of the coins from the second largest one, until from pennies.

# Because there are only a few (o(n), where n is the length of coins here, 4) calculations. So, we can consider this
# function would cost only o(constant) time.
# And, the result list is the same length of the coins list, so o(n) extra memory was used. Or say, almost o(constant).

# The inputs for the coins and target are in line 21 and 22. Running the code will give you the result of how many
# coins are needed respectively.

def coinChange(coins, target): # The coins are the types of coins in the descending order; target is the amount you need
    result = [0] * len(coins) # Variable to save the count of coins corresponding to the coin in the coins list;
    for i in range(len(coins)):
        result[i] = int(target / coins[i]) # Get the max number of coins for the ith coin
        target = target % coins[i] # Calculate the remaining amount needed;
        if target == 0: # If the need amount is 0, return result
            return result

coins = [25, 10, 5, 1]
target = 80
result = coinChange(coins, target)
print("The number of needed quarters(25c), dime(10c), nickel(5c) and penny(1c) is: ", result, "respectively.")
#


# Motivated by the above thoughts, I am thinking another problem: what if the coins list is flexible, particularly,
# if there is no "penny" in the coins list? Will there be a valid combination to achieve the target?

# In the codes below, I developed a function to keep the coins very flexible. So, it can be any values.
# I used the backtracking algorithm to find the possible paths. And, once I found one, I will just stop the recursion.
# The backtracking method can give us the result list which contains the coins combinations based on the coins
# provided. If there is no a valid combination to achieve the target, the code will print a message to imply this.

# The recursion method is very slow, it is dependent on the coins list and the target. For each recursion,
# it will have o(n) (length of coins list) possible values; and the depth depends on the target value.
# The memory cost for this code is implicit, because the stack was essentially applied during recursion. So,
# it is the depth of the recursion.

# Recursion Method, very slow.
def coinChange(coins, target):
    def DFS(coins, target, path, result):
        if target == 0:
            result.append(path[:])
        if target < 0:
            return
        for coin in coins:
            path.append(coin)
            DFS(coins, target-coin, path, result)
            if result:
                break
            else:
                path.pop()
    path, result = [], []
    DFS(coins, target, path, result) # Get one possible result for the coin combinations to achieve the target;
    if len(result) == 0: # If there is no possible combination, then return []
        return []

    count = [0] * len(coins)
    for i in range(len(coins)):
        count[i] = result[0].count(coins[i])
    return count

coins = [25, 10, 5, 2] # Input for the function, please enter the coin values, the best way is descending order;
target = 81 # Input for the function, the value of target
result = coinChange(coins, target)
if len(result) == 0:
    print("It is impossible to get the target amount by the given coins!")
else:
    print("The number of needed coins", coins, "is:", result, "respectively.")
