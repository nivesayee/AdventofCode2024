with open('input.txt', 'r') as file:
    input = file.readlines()

input1 = []
input2 = []

for line in input:
    input1.append(int(line.split()[0]))
    input2.append(int(line.split()[1]))

input1.sort()
input2.sort()

diff_list = [abs(i-j) for i, j in zip(input1, input2)]
print(sum(diff_list))