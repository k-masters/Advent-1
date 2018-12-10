# initialize variables
freq_change_list = []
current_freq = 0
freq_history = []
found_match = False
iteration_num = 1

# read file line by line adn strip off newline character if it is present, append the line to a list.
with open("Input Files/input.txt", "r") as input_file:
    for line in input_file:
        if line.endswith('\n'):
            freq_change_list.append(int(line.rstrip('\n')))
        else:
            freq_change_list.append(int(line))

# we know we are going to go through the freq_change_list once, so the while statement evaluates to true at least once.
# we then evaluate all freq changes and add the result to the freq history list and check to see if the list contains
# the current freq result. If it does we have found a duplicate and the inner for and outer while loops can be
# stopped. If we reach the end of the freq_change_list and a match still hasn't been found we start over from the
# of the list.
while not found_match:
    print("Looking for match on iteration: {}".format(str(iteration_num)))
    for freq in freq_change_list:
        current_freq += freq
        if current_freq in freq_history:
            freq_history.append(current_freq)
            print("The calibrated frequency is: {}".format(freq_history[-1]))
            found_match = True
            break
        else:
            freq_history.append(current_freq)

    iteration_num += 1
