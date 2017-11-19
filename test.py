from __future__ import print_function
import os
import signal
import json
import terminal
from urllib2 import Request, urlopen, URLError
import web
import signal
import argparse
import os.path
import json
from pygame import mixer 
import google.oauth2.credentials
import app
from google.assistant.library import Assistant
from google.assistant.library.event import EventType
from google.assistant.library.file_helpers import existing_file
import pip
import voip
from gi.repository import Gtk as gtk
from gi.repository import AppIndicator3 as appindicator
from gi.repository import Notify as notify
from gi.repository import GdkPixbuf
import re
import time
import fila
l=os.listdir('/usr/share/applications')

local_commands  = ['boss mode', 'power off','take a pic', 'take a picture', 'kill all process', 'play music', 'list all my apps','list all apps','list all my applications', 'restart', 'search open print hello', 'my python packages','Hangouts']
li=[y.split('.')[0] for y in l]
APPINDICATOR_ID = 'myappindicator'
notification1=notify.Notification.new("Google Assistant ")
notification2=notify.Notification.new("Success and saved in home directory ")
gif = GdkPixbuf.Pixbuf.new_from_file("google_assistant.svg")
notification1.set_icon_from_pixbuf(gif)
notification1.set_image_from_pixbuf(gif)
def process_event(event):
   
    if event.type == EventType.ON_CONVERSATION_TURN_STARTED:
        mixer.init()
        mixer.music.load('mario.mp3')
        mixer.music.play()
        notification1.show()
  
    if (event.type == EventType.ON_CONVERSATION_TURN_FINISHED and
            event.args and not event.args['with_follow_on_turn']):
        print()
def parse(): #personal credentials
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawTextHelpFormatter)
    
    args = parser.parse_args()
    with open(args.credentials, 'r') as f:
        credentials = google.oauth2.credentials.Credentials(token=None,
                                                            **json.load(f))

    with Assistant(credentials) as assistant:
        for event in assistant.start():
            print (event.type)

            if event.type==EventType.ON_RECOGNIZING_SPEECH_FINISHED:
                
                print (event.args['text'])
               
                text1= event.args['text'].lower()

                for i in li:
                    if text1 in i:
                        assistant.stop_conversation()
                        x= i
                
                if event.args['text'] in local_commands:
                    assistant.stop_conversation()

                    if(event.args['text']=='list all apps' or event.args['text']=='list all my apps' or event.args['text']=='list all my applications'):
                        print (li)
                        continue

                    if(event.args['text']=='boss mode'):
                        terminal.mode()
                    if(event.args['text']=='power off'):
                        terminal.off()
                   
                    if(event.args['text']=='take a pic' or event.args['text']=='take a picture'):
                        notification2.show()
                        terminal.pic()
                        continue
                    if(event.args['text']=='kill all process' or event.args['text']=='kill all apps' or event.args['text']=='kill all '):
                        terminal.all()
                    if(event.args['text']=='play music'):
                        terminal.play()
                        continue
                    
                    
                    if(event.args['text']=='my python packages'):
                        pip.show()
                        continue
                    if(event.args['text']=='Hangouts'):
                        voip.mobile()

                    if(event.args['text']=='search open print hello'):
                        fila.open('hello.txt')
                    


                    

                try:
                    app.open(x)
                except:
                    continue
                        
            process_event(event)
def main():
    indicator = appindicator.Indicator.new(APPINDICATOR_ID, os.path.abspath('google_assistant.svg'), appindicator.IndicatorCategory.SYSTEM_SERVICES)
    indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
    indicator.set_menu(build_menu())
    notify.init(APPINDICATOR_ID)
    gtk.main()

def build_menu():
    menu = gtk.Menu()
    item_notification = gtk.MenuItem('Google Assistant')
    item_notification.connect('activate', notification)

    menu.append(item_notification)
    item_quit = gtk.MenuItem('Quit')
    item_quit.connect('activate', quit)
    menu.append(item_quit)
    menu.show_all()
    return menu

def notification(_):
    
    mixer.init()
    mixer.music.load('google_female.mp3')
    mixer.music.play()

    notification1.show()
    parse()



def quit(_):
    notify.uninit()
    gtk.main_quit()

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal.SIG_DFL)
main()
