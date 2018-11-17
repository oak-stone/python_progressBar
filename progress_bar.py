import sys

def progressBar(current, total, full_progbar_length):
     frac = current/total
     filled_progbar = round(frac * full_progbar_length)
     #to prevent the print function freezing from time to time
     sys.stdout.flush()
     #special characters \r and :>7.2% are used to overwrite the previous print and have the % at the end the same length at all times, respectively
     print('\r | ', '#'*filled_progbar + '-'*(full_progbar_length-filled_progbar), ' | [{:>7.2%}]'.format(frac), end ="")

def function():
    #set the count for each iteration in the for loop
    count = 0
    #open a test file 
    with open('test.txt', 'r') as test_file:
        num_lines = sum(1 for line in test_file)
        test_file.seek(0)
        for i in test_file:
            #length of the list we are iterating through
            total = num_lines
            #increse the count for each iteration in the loop
            count += 1
            #call the progressBar function with current step, total length and set a length for the progress bar
            progressBar(count, total, 20)
        print("\n Iterated through a total of: " + str(total) + " lines.")
function()
