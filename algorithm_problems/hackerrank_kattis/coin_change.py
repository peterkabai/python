def coin_itterative(coins, total):
    # First the list of coin values are sorted, because we have to
    # itterate through them smallest to largest.
    coins.sort()

    # The combinations have a length of total plus one
    # because we can also have one way of selecting a value of zero.
    # So, the zero index is also set.
    combinations = [0] * (total + 1)
    combinations[0] = 1

    # We itterate through each coin, smallest to largest.
    for value in coins:
        # Convert the str from the input to an int
        value = int(value)
        # For each coin we see how many ways we can get each total
        for index in range(len(combinations)):
            # If the value of the coin is less than the total we want, 
            # then we can possibly use it in a combination
            if index >= value:
                # The number of combinations is increased
                combinations[index] += combinations[index - value] 
    
    return combinations[total]



def coin_recursive(coins, total):
    combinations = [0] * (total + 1)
    combinations = coin_recursive(coins, combinations, total)
    return combinations[-1]



def coin_recursive_util(coins, combinations, index):
    print("Not yet implimented")
    combinations[index] = 
    return combinations


# Read the input
total = int(input())
num_coins = int(input())
coins = input().split(" ")

print(coin_itterative(coins, total))
