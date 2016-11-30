def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "you have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers" % boxes_of_crackers
	print "Man, thats enough for a party"
	print "Get a blanket. \n"

#directly passing values to the function
print "We can just the functions numbers directly :"
cheese_and_crackers(20,30)


print "Or we can use variables from the script:"
amount_of_cheese = 10
amount_of_crackers = 50

#passing variables as parameters to the function
cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print "We can do even maths inside too:"
cheese_and_crackers (10 + 20, 5 + 6)


print "and we can combine the two, variables and maths"
cheese_and_crackers (amount_of_cheese + 100, amount_of_crackers + 1000)




