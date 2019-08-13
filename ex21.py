def add(a, b):
				print "ADDING %d + %d" % (a, b)
				return a + b

def subtract(a, b):
				print "SUBTRACTING %d - %d" % (a, b)
				return a - b

def multiply(a, b):
				print "MULTIPLYING %d * %d" % (a, b)
				return a * b

def divide(a, b):
				print "DIVIDING %d / %d" % (a, b)
				return a / b
				
print "Let's do some math with just functions!"


age = add(30, 5)
height = subtract(78, 4)
weight = multiply (90, 2)
iq = divide(100, 2)
x = "unreal"
s = raw_input(x)

 "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)
print "this is a test of stuff %s" % (s)

# A puzzle for the extra credit, type it in anyway
print "Here is a puzzle.\n"

#just personal testing, not in the lesson plan
y = raw_input("give it all you got.")
print "%r" % (y)

#need to understand, formulas are written 'inside out' with the center operating before the outer. 
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "Can you do it by hand?"


	
				

