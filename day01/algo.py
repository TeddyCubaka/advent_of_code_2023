with open("input.txt") as f:
    data = f.read().strip()

data = data.split('\n')

# step one

first_step = []
for l in data:
    first_step.append([i for i in l if i.isdigit()])

first_sum = [int(i[0] + i[-1]) for i in first_step]

print("first step : ", sum(first_sum))

# step 2

str_numbers = ['one', 'two', 'three', 'four',
               'five', 'six', 'seven', 'eight', 'nine']


def first_int(str, reverse=False):
    for i in range(len([*str])):
        if str[i].isdigit():
            return str[i]
        else:
            count = i+2
            while (count < i+6):
                if reverse and str[i:count+1][::-1] in str_numbers:
                    return str_numbers.index(str[i:count+1][::-1]) + 1
                if str[i:count+1] in str_numbers:
                    return str_numbers.index(str[i:count+1]) + 1
                count += 1


second_step = [int(str(first_int(line)) + str(first_int(line[::-1], reverse=True)))
               for line in data]

print("second step : ", sum(second_step))
