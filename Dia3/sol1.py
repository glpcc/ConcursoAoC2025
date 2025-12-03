inpt = open("input.txt").readlines()
battery_banks = [i.strip() for i in inpt]    

total_energy = 0
for brow in battery_banks:
    #print(brow)
    maximum_till_n = [0 for i in brow]
    maximum_till_n[-1] = int(brow[-1])
    for i in range(2,len(brow)):
        if maximum_till_n[-(i-1)] > int(brow[-i]):
            maximum_till_n[-i] = maximum_till_n[-(i-1)]
        else:
            maximum_till_n[-i] = int(brow[-i])
    maximum_till_n[0] = maximum_till_n[1]
    #print(maximum_till_n)
    max_power = -1
    for max_possible,val in zip(maximum_till_n[1:],brow[:-1]):
        val = int(val)
        posible_power = val*10 + max_possible
        if posible_power > max_power:
            max_power = posible_power
    total_energy += max_power

print(total_energy)