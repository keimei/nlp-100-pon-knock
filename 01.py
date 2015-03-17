#!/usr/bin/python
# coding=utf-8
p=u'パタトクカシーー'
print "".join([p[i] for i in range(len(p)) if not i%2])
