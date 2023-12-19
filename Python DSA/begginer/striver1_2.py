def br(str= " ^_^ "):
    print(str*20)
# q 11
for i in range(0, 5):
    for j in range(0, i+1):
        print((i+j+1)%2, end="")
    print()
# q 12
# missed up in looping again and again
br()
for i in range(0,4):
    # for j in range(0, i+1):
    for k in range(0, i+1):
        print(k+1,end="")
    print(" "*((4 - (i+1))*2),end="")
    for k in range(i+1, 0, -1):
        print(k,end="")
    print()
# q 15
br()
for i in range(5, 0, -1):
    for j in range(i):
        # here staring character is A
        stating_chr_index = 65
        print(chr(j+stating_chr_index), end="")
    print()
# q 17
br()
for i in range(4, 0, -1):
    print(" "*(i-1), end="")
    # here staring character is A
    stating_chr_index = 65
    for j in range(-(i - 5)):
        print(chr(j+65), end="")
        end_chr_index = j+65
    if i != 4 :
        for j in range(-(i - 4)):
            print(chr(end_chr_index - (j+1)), end="")
    print()
#q 19
br()
starter = 0  
# max_stars = int(input())
max_stars = 8
for i in range(max_stars):
    if i < max_stars//2 :    
        no_of_stars = max_stars - starter*2
        print("*"*(no_of_stars//2), end="")
        print(" "*(starter*2), end="" )
        print("*"*(no_of_stars//2), end="")
        starter=starter+1
        print()
    else:
        no_of_stars = ((i+1) - max_stars//2)*2
        no_of_spaces = max_stars - no_of_stars
        print("*"*(no_of_stars//2), end="")
        print(" "*(no_of_spaces), end="" )
        print("*"*(no_of_stars//2), end="")
        print()            
br()  
# q 21
for i in range(4):
    for j in range(4):
        if (i == 0) or (i  == 3) or (j == 0) or (j  == 3):
            print("*", end="")
        else:
            print(" ", end="")
    print()
