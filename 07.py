#!/usr/bin/python
# coding=utf-8


def how_about_that_time(x, y, z):
    t = '%s時の%sは%s'
    return t % tuple(map(str, [x, y, z]))

if __name__ == '__main__':
    print how_about_that_time(x=12, y="気温", z=22.4)
