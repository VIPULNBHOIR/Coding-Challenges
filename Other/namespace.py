"""def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():

        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)
"""

"""# GET FIRST KEY- VALUE IN Dict

getaways={5:4,3:2,8:7}


winner = list(getaways.items())[0]
print(winner[0])
winner = list(getaways.items())[0][0]
print(winner)
winner = list(getaways.items())[0][1]
print(winner)
first_key = list(getaways.keys())[0]
print(first_key)
first_val = list(getaways.values())[0]
print(first_val)"""

""" SORT THE DICTIONARY
   
myDict = {'ravi': 10, 'rajnish': 9,
        'sanjeev': 15, 'yash': 2, 'suraj': 32}
 
myKeys = list(myDict.keys())
myKeys.sort()
sorted_dict = {i: myDict[i] for i in myKeys}
 
print(sorted_dict)

"""
a=[4,5]
b=[4,4]

print(a<b)


