#
# Calculates Lyrchrel numbers for all integers 0...max_int (max_int = 1000)
# Unless it takes more than max steps (max = 10,000)
#
# https://en.wikipedia.org/wiki/Lychrel_number
# https://www.youtube.com/watch?v=bN8PE3eljdA
#

max_int = 10000
max_steps = 10000
for x in range(0, max_int):
    original_num = x
    counter = 0
    num = original_num
    while (str(num) != str(num)[::-1]) and (counter < max_steps):
        num = num + int(str(num)[::-1])
        counter += 1
    if counter == max_steps:
        print x, "Not Found"
    else:
        print x, counter, num

