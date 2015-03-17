#!/usr/bin/python
# coding=utf-8
p=u'パトカー'
t=u'タクシー'
print "".join(map(unicode, ["".join(x) for x in zip(p,t)]))
