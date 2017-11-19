import os
def mode():
	os.system("gnome-terminal -e 'bash -c \"cd /home/sumanth;libreoffice inputCarDetails.csv; exec bash\"'")

if __name__=='__main__':
	mode()