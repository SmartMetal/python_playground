from sys import argv

#Defines the inputs, including the script and file 
script, input_file = argv

#Function for creating print_all Function and 
#A  variable named 'f' to be able to manipulate the 
#file with .read() 
def print_all(f):
				print f.read()

#creates function that has a seek ability with the variable f
def rewind (f):
				f.seek(0)

#creating a function with the variables line_count
#and line_count is linked to f readline 
def print_a_line(line_count, f):
				print line_count, f.readline()

#creates a variable named current_file, opening the text file
current_file = open(input_file)

print "First let's print the whole file:\n"

#creates variable using the function printall to read the input file defined earlier 
print_all(current_file)

print "Now let's rewind, kind of like a tape."

#uses the rewind function designed earlier to  manipulate the inputted file
rewind(current_file)

print "Let's print three lines:"

#defines current line and current file in order 
#to create a printed line count x3
current_line = 1
print_a_line(current_line, current_file)

current_line = current_line +1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
