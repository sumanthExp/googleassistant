import os
import time
def open(argc):

	lookfor=argc
	for root, dirs, files in os.walk('./'):
		if lookfor in files:
			os.system('xdg-open "%s"' % root)
			os.system('xdg-open "%s"' % lookfor)
			
			os.system("gnome-terminal -e 'bash -v \"lpr lookfor;exec bash\"'")
			
			

if __name__ == '__main__':
	open()