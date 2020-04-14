#!/opt/local/bin/python2.7
# -*- coding: utf-8 -*

# The first line is my shebang...
# With this shebang, I use my version of python2.7
# It will not be the same for you, so remove or change it, accordingly.

# The second line is the utf-8 encoding line


A = raw_input("Entrer une valeur de verite pour A: ")
B = raw_input("Entrer une valeur de verite pour B: ")
C = raw_input("Entrer une valeur de verite pour C: ")
expr = raw_input("Entrer une expression Boolenne (exprimee avec des ""non"", ""ou"", ""et"" et des parentheses)\n")

expr = expr.replace("non","not")
expr = expr.replace("et","and")
expr = expr.replace("ou","or")
# Note that the expr.replace(...) does not modify expr, it returns a new list.
# Hence, we have to reassign this modified string to some variable;
# Instead of introducing new variables, we keep expr all the time.

print "L'evaluation de votre expression Booleenne est: ", bool(expr)
