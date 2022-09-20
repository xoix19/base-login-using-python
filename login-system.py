import os, sys

os.system("cls")
print ("Login System Based.")
username = 'xoix' # username
password = 'github' # password

def restart():
	restarts = sys.executable
	os.execl(restart, restart, *sys.argv)

def main():
	uname = input("Username : ")
	if uname == username:
		pwd = input("password : ")

		if pwd == password:
			print("Succes Login"),
			sys.exit()

		else:
			print("Invalid Password")
			print("Back Login")
			restart()

	else:
		print("Invalid Username")
		print("Back Login")
		restart()

try:
	main()
except KeyboardInterrupt:
	os.system('cls')
	restart()
