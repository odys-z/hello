def x():
    b = 3

print(b) # NameError: name 'b' is not defined

def fn(a):
    for n in range(len(a)):
        a[n] = n

b = [0] * 10
fn(b)

c = [0] * 20
fn(c)