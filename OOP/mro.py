# Method Resolution Order
# it tells the order of the preferences for classes

class A:
    num = 10

class B(A):
    pass

class C(A):
    num = 1

class D(B,C):     
    pass

print(D.num)

print(D.mro())
print(D.__mro__)
# both the above are same

class X:pass
class Y:pass
class Z:pass
class A(X,Y):pass
class B(Y,Z):pass
class M(B,A,Z):pass

print(M.mro())

# avoid using this in codes, because MRO rules are very confusing to understand.