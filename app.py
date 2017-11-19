import os
def open(args):
	os.system("gnome-terminal -e 'bash -c \"cd /usr/share/applications;"+args+";exec bash\"'")

if __name__ == "__main__":
	open(args)