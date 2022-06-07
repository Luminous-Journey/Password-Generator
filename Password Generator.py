#imports
import random  
import string  
import pyperclip

#code
while True:
	numchar = input("How long would you like your password to be? ")

	def getIntegers(string):
		numbers = [int(x) for x in string.split() if x.isnumeric()]
		return numbers

	def random_string(letter_count, digit_count):  
			str1 = ''.join((random.choice(string.ascii_letters) for x in range(letter_count)))  
			str1 += ''.join((random.choice(string.digits) for x in range(digit_count)))  
		
			sam_list = list(str1) # it converts the string to list.  
			random.shuffle(sam_list) # It uses a random.shuffle() function to shuffle the string.  
			final_string = ''.join(sam_list)  
			pyperclip.copy(final_string)
			return final_string  
	

	# define the length of the password
	try: 
		if int(numchar) > 255:
			print("The number of characters is too large please select a number between 8 and 255")
			continue
		elif int(numchar) < 8:
			print("Your password length is too short to be an effective password, please select a number between 8 and 255")
			continue 
		else:
			print("Your randomly generated password is:", random_string(int(numchar), int(numchar)), "\nYour newly generated password has been coppied to you're clipboard")
			Yes = input("Would you like to exit the app? Enter Yes or No: ")
			if Yes == "yes" or Yes == "Yes" or Yes == "y":
				break
			else:
				continue
	except ValueError:
		print("Please only enter numbers") 
