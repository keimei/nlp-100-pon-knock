# coding=utf-8
import n_gram

src_x = "paraparaparadise"
src_y = "paragraph"

X = set(n_gram.n_gram(src_x, 2))
Y = set(n_gram.n_gram(src_y, 2))

union = X | Y
intersect = X & Y
comp_x = X - Y
comp_y = Y - X


print "和集合:",  union
print "積集合:", intersect
print "差集合(X-Y):", comp_x
print "差集合(Y-X):", comp_y

