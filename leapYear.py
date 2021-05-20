def leap(inputVal):
        if(isValid(inputVal) == False):
                return "Invalid Input Type"
        if(inputVal % 4 != 0):
                #if it isn't then it is not a leap year
                return False
        else:
                #if it is, then check if it is divisible by 100
                if(inputVal % 100 == 0):
                        #if it is divisible by 100, see if it is also divisible by 400
                        if(inputVal % 400 != 0):
                                #if not then it isn't a leap year
                                return False
                        else:
                                #otherwise it is a leap year
                                return True
                else:
                        #if not divisible by 100, then it is a leap year
                        return True


def isValid(inputVal):
        if(type(inputVal) is int):
                if(inputVal >= 0):
                        return True

        return False
