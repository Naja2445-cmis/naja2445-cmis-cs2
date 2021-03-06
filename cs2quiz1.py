#Part 1: Terminology (15 points)
#1 1pt) What is the symbol "=" used for?
#The symbol "=" is an assignment opperator and it is use for defining the value of the function.
#
# +1 Assignment operator is clearly explained.
#2 3pts) Write a technical definition for 'function'
#A technical definition of 'function' is like a variable that the value has been put in already. 
#
# -3 Calculation wasn't explained well.
#3 1pt) What does the keyword "return" do?
#The word "return" sets a variable to be a value from a function.
#
# +1 The definition of 'return' was clearly explained.
#4 5pts) We know 5 basic data types. Write the name for each one and provide two
#   examples of each below
#	1:interger
#	2:float
#	3:string
#	4:boolean
#	5:len 
# +2 Len isn't a data type, and all data type has no example.
#5 2pts) What is the difference between a "function definition" and a 
#       "function call"?
#a "function definition" is a when we write "def" to define a function, or like to put a value in a variable, and "function call" is when you're telling the program to execute that function. 
#
# +2 The definition is clearly explained.
#
#6 3pts) What are the 3 phases that every computer program has? What happens in
#        each of them
#	1:input
#	2:output
#	3:process

# +1.5 No explanation of the definition.


#Part 2: Programming (25 points)
#Write a program that asks the user for the areas of 3 circles.
#It should then calculate the diameter of each and the sum of the diameters 
#of the 3 circles.
#Finally, it should produce output like this:

#1 pt for header line
#3 pt for correct formula
#1 pt for return value
#1 pt for parameter name
#1 pt for function name
import math

def diameter(x):
	 return 2*(math.sqrt(x/math.pi))
def all_diameter(dia1,dia2,dia3):
	return dia1+dia2+dia3
#1pt for header line
#1pt for parameter names
#1pt for return value
#1pt for correct output format
#3pt for correct use of format function
def output(dia1,dia2,dia3,total):
	 out="""

Circle      Diameter
c1             {}
c2             {}
c3             {}
Totals        {}

""".format(dia1,dia2,dia3,total)
   return out

def main():
   C1=raw_input("Area of cr1: ")
   C2=raw_input("Area of cr2: ")
   C3=raw_input("Area of cr3: ")
  
   dia1=diameter(float(C1))
   dia2=diameter(float(C2))
   dia3=diameter(float(C3))
   total=all_diameter(dia1,dia2,dia3)
  
   out=output(dia1,dia2,dia3,total)
   print out

main ()
#1pt header line
#0pt getting input
#0pt converting input
#0pt for calling output function
#2pt for correct diameter formula
#1pt for variable names

#1pt for calling main
#0pt explanatory comments
#1pt code format

#Circle  Diameter
#c1      ...
#c2      ...
#c3      ...
#TOTALS  ...
# Hint: Radius is the square root of the area divided by pi
