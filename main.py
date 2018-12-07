freq_change_list = []

with open("input.txt", "r") as input_file:
    for line in input_file:
        freq_change_list.append(input_file.readline())

print(freq_change_list)