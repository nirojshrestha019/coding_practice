# Function to print binary number using recursion

def convertToBinary(n, count):
    if n > 1:
        # print("Yes")
        print(count)
        count += 1
        convertToBinary(n//2, count)
    print("########")
    print(n % 2, end='')


# decimal number
dec = 34
count = 0


print("{0:b}".format(dec))

convertToBinary(dec, count)
print()
