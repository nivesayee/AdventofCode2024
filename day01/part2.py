with open('input.txt', 'r') as file:
    input = file.readlines()

input1 = []
input2 = []

for line in input:
    input1.append(int(line.split()[0]))
    input2.append(int(line.split()[1]))

output=0

for i in input1:
    output += i*input2.count(i)

print(output)
