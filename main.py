import random as rand

#Variables



#Functions
def main():
    mini = int(input("What is the minimum number you would like to be generated? "))
    maxi = int(input("What is the maximum number you would like to be generated? "))
    times = int(input("How many numbers would you like to be generated? "))
    for i in range(times):
        print(rand.randint(mini, maxi))


#Code
main()