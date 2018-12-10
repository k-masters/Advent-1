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

while not found_match:
    print("Looking for match on iteration: {}".format(str(iteration_num)))
    iteration_num += 1
    for freq in freq_change_list:
        current_freq += freq
        if current_freq in freq_history:
            freq_history.append(current_freq)
            print("The calibrated frequency is: {}".format(freq_history[-1]))
            found_match = True
            break
        else:
            freq_history.append(current_freq)