def add_three_nums(a, b, c):
    try:
        result = a + b + int(c)
        print(result)
    except:
        print("caught error in add_three_nums func!")
    else:
        print("add went well!")


a = 1
b = 1
c = input("please enter a number: ")
add_three_nums(a, b, c)

try:
    f = open("testfile.txt", "w")
    f.write("write a test line\nAnother test line")
except TypeError:
    print("There was a type error!")
except OSError:
    print("Hey you have an IO error!")
except:
    print("I catch ALL errors!!!")
finally:
    print("I always run!")
