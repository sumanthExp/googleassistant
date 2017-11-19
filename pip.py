import os

def show():
	os.system("gnome-terminal -e 'bash -c \"pip list;exec bash\"'")

if __name__ == '__main__':
	show()