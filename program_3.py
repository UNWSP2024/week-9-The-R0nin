# Program #3: Average Numbers
# Assume a file containing a series of integers is named numbers.txt and exists on the computer's disk.
# (please use the provided numbers.txt)
# Write a program that reads all of the numbers stored in the file and calculates their total.  

# The program should handle the following exceptions: 

# It should handle any IOError exceptions that are raised.
# It should handle any ValueError exceptions that are raised when the items that are read from the file 
# are converted to a number.
def sum_numbers_from_file():
    total = 0.0
    
    try:
        numbers = open('numbers.txt', 'r')
        for line in numbers:
            number = float(line)
            total = total + number

        numbers.close()

        print('In the sum_numbers_from_file function')
        print(total)

    except IOError:
        print('error occurred while tring to read the file')

    except ValueError:
        print('non number value(data) found in the file')


# You don't need to change anything below this line:
if __name__ == '__main__':
    sum_numbers_from_file()
