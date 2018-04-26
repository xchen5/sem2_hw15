def isGoodPassword(password):
        upper = [char for char in password if char.isupper()]
        lower = [char for char in password if char.islower()]
        number = [char for char in password if char.isdigit()]
        if (len(upper) >= 1 and len(lower) >= 1 and len(number) >= 1):
            return True
        else:
            return False

print(isGoodPassword("X12323"))

def passwordStrength(password):
    upper = [char for char in password if char.isupper()]
    lower = [char for char in password if char.islower()]
    number = [char for char in password if char.isdigit()]
    nonalphanumeric = [char for char in password if not char.isalnum()]
    score = len(nonalphanumeric) + len(number) + len(lower) + len(upper)
    if (score >= 10):
        score = 10
    if(len(nonalphanumeric) <= 1):
        score = score + (len(nonalphanumeric) - 2)
    if(len(upper) <= 1):
        score = score + (len(upper) - 2)
    if(len(lower) <= 1):
        score = score + (len(lower) - 2)
    if(len(number) <= 1):
        score = score + (len(number) - 2)
    if(score <= 0):
        score = 1
    return score

print(passwordStrength('34r5tn%RR@'))
