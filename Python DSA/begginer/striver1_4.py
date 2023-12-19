# palindrom number
num = 12521
str_num = str(num)
strip_string_len = len(str_num)//2
striped = str_num[:strip_string_len]
status_of_mirror = 1
for i , ch in enumerate(striped):
    if ch != str_num[-(i+1)] :
        status_of_mirror = 0
        break
if status_of_mirror == 0:
    print("Not a palindrom number")
else:
    print("It is a palindrom number")
# from striver1_2 import br
# br()
# GCD or HCF for 12 and 8 the gdc or hcf is 4
num1 = 423425
num2 = 23425
if num1 < num2:
    small= num1
    large= num2
else:
    large = num1
    small = num2
sm_factors = []
sm_factors.append(1)
for i in range(2,small):
    if small % i == 0:
        sm_factors.append(i)
sm_factors.append(small)
print(sm_factors)
for i in reversed(sm_factors):
    if large%i == 0:
        print(f"The GCD for the given two numbers are {i}")
        break
