# 1
favs = ['cookie', 'banana', 'pie', 'apple', 'beer']
print(favs)
print(favs[2])
favs[2] = 'valhalla'
favs.append('whiskey')
print(favs)
favs.insert(0, 'rye')
print(favs)
favs.pop()
favs.pop(0)
print(favs)
favs.pop(2)
favs = ','.join(favs)
print(favs)

# 2
taxa = 'sapiens, erectus, neanderthalensis'
species = taxa.split(",")
print(species)
species = sorted(species)
species = sorted(species, key=len)
print(species[1])
type(species)
species = sorted(species)
print(species)

# 3
my_list = ['a', 'bb', 'ccc']
list_copy = my_list
print(my_list)
['a', 'bb', 'ccc']
print(list_copy)
list_copy.append('dddd')
print(my_list)
['a', 'bb', 'ccc', 'dddd']

my_list2 = ['a', 'bb', 'ccc']
list_copy2 = my_list2.copy()
print(my_list2)

# 4
counter = 1
while counter <= 100:
    print(counter)
    counter += 1

# 5
counter = 1
factorial = 1
while counter <= 1000:
    factorial *= counter
    counter += 1
print(factorial)

# 6
nums = [101,2,15,22,95,33,2,27,72,15,52]
for i in nums:
    if i % 2 == 0:
        print(i)

#7
evens = []
odds = []
nums = sorted(nums)
print(nums)
for i in nums:
    print(i)
    if i % 2 == 0:
        print(i)
        evens.append(i)
    else:
        print(i)
        odds.append(i)
print('Sum of even numbers:' , sum(evens))
print('Sum of odd numbers:', sum(odds))

#8
for i in range(1,101):
    print(i)

# 9
print([i for i in range(1,101)])

#10
import sys
arg1 = sys.argv[1]
arg2 = sys.argv[2]

arg1 = 3
arg2 = 10

for i in range(1,101):
    if i == arg1 or arg2:
        print(i)
    else:
        break

# 11


