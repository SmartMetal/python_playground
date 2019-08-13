#defines the function and variables
def cheese_and_crackers(cheese_count, boxes_of_crackers):
				print "You have %d cheeses!" % cheese_count
				print "You have %d boxes of crackers!" %  boxes_of_crackers
				print "Man that's enough for a party!"
				print "Get a blanket.\n"

#Feeds numbers directly into the function				
print "We can just give the function number directly:"
cheese_and_crackers(20, 30)

#this assigns numbers to the variables				
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

#this creats the VARIABLE for 'cheese_and_crackers'
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

#Does math with the cheese and crackers variable
print "We can even do math inside too:"
cheese_and_crackers(10+20, 5+6)

#Uses math on the variables
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

print "Here we'll do some multiplication:"
cheese_and_crackers(amount_of_cheese * 100, amount_of_crackers * 23)

print "And we'll try some division as well:"
cheese_and_crackers(amount_of_cheese / .2, amount_of_crackers / 23)
