#!/usr/bin/python

num = int(raw_input("Introduzca numero para tabla ") )
max = range(1,20)

for i in max :
    print str(i) + " * " + str(i) + " = " + str(i*num)
