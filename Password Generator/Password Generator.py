import random
import string

if __name__ == "__main__":
    #Characters ka set
    s1 = string.ascii_uppercase  
    s2 = string.ascii_lowercase
    s3 = string.digits
    #s4 = string.punctuation
    #Password lenght input
    length = int(input("Enter password lenght (Minimum 4): \n"))

    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    #s.extend(list(s4))

    #shuffle for randomness
    random.shuffle(s)

    #Final password
    print("Your strong password: ")
    print("".join(s[0:length]))





    

