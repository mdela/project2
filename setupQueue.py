# GOAL OF THIS PROJECT:
# program is intended to serve customers in a queue-based system
# FIRST IN FIRST OUT 
# program should offer a menu of options

# option 1: add a customer in line
# option 2: delete a customer in line
# option 3: serve the next customer
# option 4: view the queue

# run on terminal: python3 setupQueue.py

import random

# option 1: make appointments
def createQueue():

	newQueue = []
	continueOption = "start"

	# this while loop creats a list of dictionaries
	# this list appends onto the existing list
	while (continueOption.lower() != "finish"):
		customerName = input("Customer's name: ")
		reason = input("Reason: ")
		customerIDnumber = (random.randrange(100,999,1))
		newCustomer = {
			"name": customerName,
			"reason": reason,
			"customerID": customerIDnumber
		}
		print ("\nCreating appointment...")
		queue.append(newCustomer)  
		print ("Appointment created.\n")

		# prompt user to either continue or make a new appointment
		while (True):
			continueOption = input("Make another appointment?"
			"\nTo continue, press enter."
			+ "\nTo quit, enter 'finish'.\n")

			if (continueOption.lower() == "finish"):
				print ("\nDone.\n")
				break;
			elif (continueOption.lower() == ""):
				break;
			else:
				print ("\nInvalid input, try again.\n")

	queue.extend(newQueue)

# option 2: serve the next customer in the queue
def serveNext():
	
	if queue:
		print ("------------------------------"
			f"\n{queue[0]['name']} will be helped next.\n"
			"------------------------------")
		queue.pop(0)	
	else:
		print ("------------------------------"
					"Queue is empty."
			"------------------------------")

# option 3: view appointments
def viewQueue():
	# displays every customer from first to last -- name, reason, and ID
	if queue:
		print ("------------------------------")
		for person in queue:
			print (f"\nName: {person['name']}"
				f"\nReason: {person['reason']}"
				f"\nCustomer ID: {person['customerID']}\n")
		print ("------------------------------")
	else:
		print ("------------------------------"
					"Queue is empty."
			"------------------------------")		

# option 4: remove customer
def removeCustomer():
	# first displays all the existing customers in the queue
	# removes the customers based on ID
	if queue:
		print ("Viewing all entries...")
		viewQueue()
		removeInput = int(input("To remove, enter the customer ID: "))
		for n in range(len(queue)):
		    if queue[n]['customerID'] == removeInput:
		        del queue[n]
		        break
	else:
		print ("------------------------------"
					"Queue is empty."
			"------------------------------")			

# MAIN
# start with an empty list of dictionaries. 
queue = []

# the options should be offered in a while loop

while (True):
	print("Select an option:"
		"\n1: Add customer to the line"
		"\n2: Remove a customer in line"
		"\n3: Serve the next customer"
		"\n4: View the queue\n")
	option = input("To exit program, enter 0\nOption: ")
	option = int(option)
	if (option == 1):
		createQueue()
	elif (option == 2):
		removeCustomer()
	elif (option == 3):
		serveNext()
	elif (option == 4):
		viewQueue()
	elif (option == 0):
		print("Ending program...")
		break
	else:
		print("Invalid entry, try again.\n")

print("Proram finished.")
