

print("Hello World")


def age():
    print("Enter your name \n")
    name = input()
    print("Enter your age \n")
    age = input()

    if int(age)>=18:
        print(name + " is eligible to vote")
    else:
        print(name + " is not eligible to vote")


def dec_func(st1,st2,st3):
    s1 = list(st1)
    s2= list(st2)
    s3 = list(st3)
    s1.sort(reverse = True)
    s2.sort(reverse = True)
    s3.sort(reverse = True)

    s1 = "".join(s1)
    s2 = "".join(s2)
    s3 = "".join(s3)
    def reverse():
        print(s1+ " , "+s2+ " , ",s3)
    return reverse()

string1 = input()
string2 = input()
string3 = input()

func = dec_func(string1,string2,string3)
