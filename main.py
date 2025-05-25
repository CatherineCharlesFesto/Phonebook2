# importing the module 
import sys 

# this function will be the first to run as soon as the main function executes 
def initial_phonebook(): 
	rows, cols = int(input("Please enter initial number of contacts: ")), 5
	
	# We are collecting the initial number of contacts the user wants to have in the 
	# phonebook already. User may also enter 0 if he doesn't wish to enter any. 
	phone_book = [] 
	print(phone_book) 
	for i in range(rows): 
		print("\nEnter contact %d details in the following order (ONLY):"% (i+1)) 
		print("NOTE: * indicates mandatory fields") 
		print("....................................................................") 
		temp = [] 
		for j in range(cols):
		# We have taken the conditions for values of j only for the personalized fields 
		# such as name, number, e-mail id, dob, category etc 
			if j == 0: 
				temp.append(str(input("Enter name*: ")))
				# We need to check if the user has left the name empty as its mentioned that 
				# name & number are mandatory fields. 
				# So implement a condition to check as below. 
				if temp[j] == '' or temp[j] == ' ': 
					sys.exit( 
						"Name is a mandatory field. Process exiting due to blank field...") 
					# This will exit the process if a blank field is encountered.
			if j == 1: 
				temp.append(int(input("Enter number*: "))) 
				# We do not need to check if user has entered the number because int automatically 
				# takes care of it. Int value cannot accept a blank as that counts as a string. 
				# So process automatically exits without us using the sys package.				
			if j == 2: 
				temp.append(str(input("Enter e-mail address: "))) 
				# Even if this field is left as blank, None will take the blank's place 
				if temp[j] == '' or temp[j] == ' ': 
					temp[j] = None
					
			if j == 3: 
				temp.append(str(input("Enter date of birth(dd/mm/yy): "))) 
				# Whatever format the user enters dob in, it won't make a difference to the compiler 
				# Only while searching the user will have to enter query exactly the same way as 
				# he entered during the input so as to ensure accurate searches 
				if temp[j] == '' or temp[j] == ' ':
				# Even if this field is left as blank, None will take the blank's place 
					temp[j] = None
			if j == 4: 
				temp.append( 
					str(input("Enter category(Family/Friends/Work/Others): "))) 
				# Even if this field is left as blank, None will take the blank's place 
				if temp[j] == "" or temp[j] == ' ': 
					temp[j] = None
					
		phone_book.append(temp) 
		# By this step we are appending a list temp into a list phone_book 
		# That means phone_book is a 2-D array and temp is a 1-D array 
	
	print(phone_book) 
	return phone_book 

def menu():
    print("********************************************************************") 
    print("\t\t\tSMARTPHONE DIRECTORY", flush=False) 
    print("********************************************************************") 
    print("\tYou can now perform the following operations on this phonebook\n") 
    print("1. Add a new contact") 
    print("2. Remove an existing contact") 
    print("3. Delete all contacts") 
    print("4. Search for a contact") 
    print("5. Display all contacts") 
    print("6. Exit phonebook") 

def add_contact(pb): 
	# Adding a contact is the easiest because all you need to do is: 
	# append another list of details into the already existing list 
	dip = [] 
	for i in range(len(pb[0])): 
		if i == 0: 
			dip.append(str(input("Enter name: "))) 
		if i == 1: 
			dip.append(int(input("Enter number: "))) 
		if i == 2: 
			dip.append(str(input("Enter e-mail address: "))) 
		if i == 3: 
			dip.append(str(input("Enter date of birth(dd/mm/yy): "))) 
		if i == 4: 
			dip.append( 
				str(input("Enter category(Family/Friends/Work/Others): "))) 
	pb.append(dip) 
	# And once you modify the list, you return it to the calling function wiz main, here. 
	return pb
# Main function code 
print("....................................................................") 
print("Hello dear user, welcome to our smartphone directory system") 
print("You may now proceed to explore this directory") 
print("....................................................................") 
# This is solely meant for decoration purpose only. 
# You're free to modify your interface as per your will to make it look interactive 

ch = 1
pb = initial_phonebook() 
menu()
choice=int(input("Enter your choice : (1-6)"))
if choice==1:
	pb=add_contact(pb)

