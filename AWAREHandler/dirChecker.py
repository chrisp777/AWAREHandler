'''
Created on 23 Oct 2014

@author: Chris
'''
import pyinotify

# The watch manager stores the watches and provides operations on watches
wm = pyinotify.WatchManager()

mask = pyinotify.IN_DELETE | pyinotify.IN_CREATE  # watched events

class EventHandler(pyinotify.ProcessEvent):
    def process_IN_CREATE(self, event):
        print "Creating:", event.pathname

    def process_IN_DELETE(self, event):
        print "Removing:", event.pathname
         
handler = EventHandler()
notifier = pyinotify.Notifier(wm, handler)
# Internally, 'handler' is a callable object which on new events will be called like this: handler(new_event)
 
wdd = wm.add_watch('test', mask, rec=True)
notifier.loop()