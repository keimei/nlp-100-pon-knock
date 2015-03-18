v="Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
ini=[1, 5, 6, 7, 8, 9, 15, 16, 19]
d={}
v=v.split(" ")
for i in range(len(v)):
    if i+1 in ini:
        d[i] = v[i][:1]
    else:
        d[i] = v[i][:2]
print d
