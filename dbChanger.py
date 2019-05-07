#python3
#very simple list to add or remove objects from database

import mysql.connector , sys


manu = " 0 >> exit \n 1 >> add to db \n 2 >> remove from db \n 3 >> to check db \n 4 >> to check for specific object \n Your choice >>"


#connection to db with testint purpose values
mydb = mysql.connector.connect( 
	host = "localhost",
	user = "admin" , 
	passwd = "password",
	database = "testbase" 
)

add_values = "INSERT INTO employees (name , position) VALUES (%s , %s)"

employees_val = ""

mysqlcursor = mydb.cursor()

def check_val_emptiness(value):
	if value



def add_fun():

	#fun first take num of how much employee there will be added

	try:
		num_data = int(input("How much employees going to be added? >> "))
	except ValueError:
		print("Error in answer")
		return console()

	sum = 0

	while num_data> sum:	#do add amount of employees to db
		qqq = input(">>")

		if qqq == "":
			print("uansdsa")

		sum+=1

def exit_script():
	print("GoodBye")
	sys.exit()


def user_input_checker(user_answ):
	if user_answ == "0":
		exit_script()
	elif user_answ == "1":
		add_fun()
	elif user_answ == "2":
		print("2")
	elif user_answ == "3":
		print("3")
	elif user_answ == "4":
		print("4")
	else :
		print("Incorrect choice!")
		console()


def console():
	user_answ = input(manu)

	user_input_checker(user_answ)


def main():
	console()


if __name__ == "__main__":
	main()