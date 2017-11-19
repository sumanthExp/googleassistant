import os
def open(args):
	os.system("gnome-terminal -e 'bash -c \"firefox "+args+";exec bash\"'")

if __name__ == "__main__":
	open(args)