#
# Calculates Lyrchrel number
#
# https://en.wikipedia.org/wiki/Lychrel_number
# https://www.youtube.com/watch?v=bN8PE3eljdA
#

original_num = 0
counter = 0
while original_num == 0:
    user_input = raw_input("Enter number above 0: ")
    if user_input.isdigit():
        original_num = int(user_input)
num = original_num
while str(num) != str(num)[::-1]:
    num = num + int(str(num)[::-1])
    counter += 1
    print counter

print "original num = {}".format(original_num)
print "num steps = {}".format(counter)
print "final value = {}".format(num)

