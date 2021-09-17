#Printing the number of letters in a string
def most_frequent(str) :
    d=dict()
    for key in str:
        if key in d:
            d[key]+=1
        else:
            d[key]=1
    return d
name = input("Please enter a string ")
print(most_frequent(name))
