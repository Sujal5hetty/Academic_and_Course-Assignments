def isrot(s1,s2):
    if len(s1)!=len(s2):
        return False
    else:
        return s2 in (s1+s1)


a="left"
b="ftle"

E="asfgt"
T="gtfas"

S="tenet"
I="etet"
print(isrot(a,b))
print(isrot(E,T))

print(isrot(S,I))
