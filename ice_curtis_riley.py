
### PYTHON VARIABLES ###
hometown = "Wylie"
x = 298784

j = 5
l = 10
print(j + l)

z = j + l
print (z)

t = q = r = s = "education"

print(t)
print(q)
print(r)
print(s)

### PYTHON DATA TYPES ###

x = ["apple", "banana", "cherry"] 
y = ("apple", "banana", "cherry") 
f = False
g = 'covid-19'

type(x)
type(y)
type(f)
type(g)

### PYTHON LOCAL AND GLOBAL ###

x = 0
j = 3

def funky(arg1, arg2):
	x = 1
	j = 5
	if arg1 > arg2:
		print('arg1 is greater than arg2')
	else:
		print('arg1 is not greater than arg2')
	print(j)

funky(x, j)

print(x)
print(j)

### Given this code, the output should be "arg1 is not greater than arg2", "5", "0", "3".

x = 0
j = 3

def funky(arg1, arg2):
	global x
	global j	
	x = 1
	j = 5
	if arg1 > arg2:
		print('arg1 is greater than arg2')
	else:
		print('arg1 is not greater than arg2')
	print(j)

funky(x, j)

print(x)
print(j)

### PYTHON ITERATION ###

lunches = ['burger','apple','soba','chahan']
for x in lunches: 
	print(x)
	if x is "apple":
		break
