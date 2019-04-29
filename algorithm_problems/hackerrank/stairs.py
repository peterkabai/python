
def get_cost_iterative(num_steps, input_steps):

    # Add two zero cost steps under the original starting step
    staircase = [0, 0]
    staircase.extend(input_steps)
    
    # For all original steps in the step cost list
    for step in range(2, num_steps+2):

        # Add the cost of the step to the two previous step with the lower cost
        new_cost = min(staircase[step-1], staircase[step-2]) + staircase[step]
        staircase[step] = new_cost

    # Return the cost of the last step
    return staircase[num_steps+1]

def get_cost_recursive(num_steps, input_steps):
    # Add two zero cost steps under the original starting step
    staircase = [0, 0]
    staircase.extend(input_steps)
    return get_cost_recursive_util(num_steps+2, staircase)

def get_cost_recursive_util(num_steps, staircase):

    # If we're below the staircase just looking at the two extra steps
    if num_steps <= 2:
        return 0
    else:
        # Get the cost of the two preveios steps
        down_one = get_cost_recursive_util(num_steps-1, staircase[0:-1])
        down_two = get_cost_recursive_util(num_steps-2, staircase[0:-2])

        # Return the cost of the current step
        return staircase[-1] + min(down_one, down_two)

# Read in the input
num_steps = int(input())
staircase = [int(x) for x in input().split(' ')]

# Print the results
print(get_cost_iterative(num_steps, staircase))
#print(get_cost_recursive(num_steps, staircase))
