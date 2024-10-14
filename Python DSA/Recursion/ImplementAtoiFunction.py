# Implement Atoi Function 

from typing import Optional

def createAtoi(s: str) -> int:
    sign = "+"
    signUpdated = False
    number = []
    for i in s:
        if i == " ":
            pass
        else:
            if i == "+":
                if signUpdated == False:
                    sign = "+"
                    signUpdated = True
                else:
                    break
            elif i == "-":
                if signUpdated == False:
                    sign = "-"
                    signUpdated = True
                else:
                    break
            else:
                try:
                    if int(i)+1:
                        number.append(i)
                        signUpdated = True
                except:
                    break
    number = "".join(number)
    if number == "":
        number = 0
    # if int(number) > (2147483647):
    #     number = 2147483647
    if sign == "+":
        if int(number) > (2147483647):
            number = 2147483647
        return int(number)
    else:
        if int(number) > (2147483647):
            number = 2147483648
        return -int(number)