# Defining strings & a variable
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"

#inserting strings in strings
y = "Those who know %s and those who %s." % (binary, do_not)

#printing strings
print x
print y

#quoting a string	
print "I said: %r." % x
print "I also said: '%s'." % y

#Humor with a raw data string %r = raw 
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

#Printing the humor
print joke_evaluation % hilarious

#More string making
w = "This is the left side of..."
e = "a string with a right side."

#Producing a string defined by its locations described above
print w + e

