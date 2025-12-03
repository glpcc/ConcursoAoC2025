inpt = open("input.txt").readlines()
battery_banks = [i.strip() for i in inpt]





total_energy = 0
for brow in battery_banks:
    contructed_power = ''
    right_index = 0
    for digits_remain in range(11,-1,-1):
        #print(digits_remain)
        possible_digits = brow[right_index:len(brow)-digits_remain]
        temp_max = -1
        temp_indx = 0
        for i,dig in enumerate(possible_digits):
            if int(dig) > temp_max:
                temp_max = int(dig)
                temp_indx = i
        # print(temp_indx,temp_max)
        right_index += temp_indx + 1
        contructed_power += str(temp_max)
        #print(contructed_power)
    print(contructed_power)
    total_energy += int(contructed_power)
print(total_energy)