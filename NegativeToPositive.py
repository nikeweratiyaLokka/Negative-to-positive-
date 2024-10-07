def Modulus(number):
    numStr = str(number)
    numberChar = list(numStr) #converts number into an array of characters
    if numberChar[0] == "-":
        numberChar.pop(0) #removes the first element if there is a minus symbol
    positiveNumStr = "".join(numberChar) #converts the array back to a string without the minus symbol if it was there in the first place
    positiveNum = int(positiveNumStr)

    return positiveNum

