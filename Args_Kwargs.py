def args(*args):
    print(args)

def kwargs(**kwargs):
    print(kwargs)


args(1,2,"vipul","bhoir")
args(1,2,3)

kwargs(name = "vipul", age = 21, qualification = 'BE')
kwargs(name = "sahil", stream = float(5))



ans = lambda x,y: x+y
print(ans(9,58))