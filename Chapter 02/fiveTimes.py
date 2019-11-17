# Use a for loop to print "Jimmy Five Times" five times
print('My name is')
for i in range(5):
    print('Jimmy Five Times (' + str(i) + ')')

# Add up all the numbers from 1 to 100
total = 0
for num in range(101):
    total = total + num
    print(total)

# Use a while loop to print "Jimmy Five Times" five times
print('My name is')
i = 0
while i < 5:
    print('Jimmy Five Times (' + str(i) + ')')
    i = i + 1

# Calling a range from 12 to 16
for i in range(12, 16):
    print(i)

# Calling range from zero to eight by intervals of two
for i in range(0, 10, 2):
    print(i)
    
# Use a for loop to count down from 5 in intervals of 1
for i in range(5, -1, -1):
    print(i)
