import sys


#COLORED TEXT FROMAT '\033[1;32;40m'
# \033 is escape code
# 1 is the text style (in this case bold)
# 32 is the color (in this case green)
# 40m is the background color (in this case black)

#TEXT COLOR	CODE	TEXT STYLE	CODE	BACKGROUND COLOR	CODE
#Black	     30	    No effect	 0	    Black	             40
#Red	     31	    Bold	     1	    Red	                 41
#Green	     32	    Underline	 2	    Green	             42
#Yellow	     33	    Negative1	 3	    Yellow	             43
#Blue	     34	    Negative2	 5	    Blue	             44
#Purple	     35			                Purple	             45
#Cyan	     36			                Cyan	             46
#White     	 37			                White	             47

#the actual progress bar
def progressBar(current, total, full_progbar_length):
     frac = current/total
     filled_progbar = round(frac * full_progbar_length)
     #to prevent the print function freezing from time to time
     sys.stdout.flush()
     #special characters \r and :>7.2% are used to overwrite the previous print and have the % at the end the same length at all times, respectively
     print('\r \033[0;32;40m | ', '#'*filled_progbar + '-'*(full_progbar_length-filled_progbar), ' | [{:>7.2%}]'.format(frac), end ="")

def function():
    #set the count for each iteration in the for loop
    count = 0
    #open a test file
    with open('test.txt', 'r') as test_file:
        #get the number of lines in the file
        num_lines = sum(1 for line in test_file)
        test_file.seek(0)
        for i in test_file:
            #length of the list we are iterating through
            total = num_lines
            #increse the count for each iteration in the loop
            count += 1
            #call the progressBar function with current step, total length and set a length for the progress bar
            progressBar(count, total, 20)
        print("\n \033[0;37;40m Iterated through a total of: " + str(total) + " lines.")
function()
