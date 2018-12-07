freq_change_list = []
base_freq = 0

with open("Input Files/input.txt", "r") as input_file:
    for line in input_file:
        if line.endswith('\n'):
            freq_change_list.append(int(line.rstrip('\n')))
        else:
            freq_change_list.append(int(line))

print(freq_change_list)
for freq_change in freq_change_list:
    base_freq += freq_change

print(base_freq)