'''
Created on 23 Oct 2014

@author: Chris
'''
# Mostly based on the examples given in the pyinotify github

import pyinotify

# The watch manager stores the watches and provides operations on watches
wm = pyinotify.WatchManager()

# Mask for the two events that we will watch for
mask = pyinotify.IN_DELETE | pyinotify.IN_CREATE  # watched events

# Class to handle the events thrown by the framework
class EventHandler(pyinotify.ProcessEvent):
    def process_IN_CREATE(self, event):
        # print out the message and the name of the file in question
        print "Creating:", event.pathname

    def process_IN_DELETE(self, event):
        print "Removing:", event.pathname
        # print out the message and the name of the file in question
         
# Start a new handler object
handler = EventHandler()
# Add a notifier to the event handler to pass the event through to the event handler
notifier = pyinotify.Notifier(wm, handler)
# Internally, 'handler' is a callable object which on new events will be called like this: handler(new_event)
 
# Start watching a new directory
wdd = wm.add_watch('test', mask, rec=True)
# Loop forever catching and dealing wth the events
notifier.loop()