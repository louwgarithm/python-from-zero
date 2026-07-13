def biggest_number(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(biggest_number(3,4,5))

# Faster method
def biggest_number(num1, num2, num3):
    return max(num1, num2, num3)

print(biggest_number(3,4,5))
