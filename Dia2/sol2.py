


inpt = open("input.txt").read().strip()
data = [i for i in inpt.split(",")]
data2 = [ i.split('-') for i in data]

seen_numbers = set()
def check_pattern(mn,mx,pattern_length):
   tot = 0
   range_min, range_max = int(mn[:pattern_length]), int(mx[:pattern_length])

   if len(mn) < len(mx): range_min,range_max = 10**(pattern_length-1), range_max*10
   print("a",mn,mx,range_min,range_max)
   for i in range(range_min, range_max+1):
       for nrep in range(2,len(mx)+1):
           product_id = int(str(i)*nrep)
           if product_id > int(mx):
               break
           if product_id >= int(mn) and product_id not in seen_numbers:
               print(product_id)
               seen_numbers.add(product_id)
               tot += product_id
   return tot

tot = 0
for mn,mx in data2:
    if len(mx) > len(mn): print(mn,mx,len(mn),len(mx))
    for i in range(1,len(mx)//2 + 1):
        tot += check_pattern(mn,mx,i)

print(tot)