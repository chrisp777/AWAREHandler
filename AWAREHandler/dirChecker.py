'''
Created on 23 Oct 2014

@author: Chris
'''
import pyinotify

class TrackModifications(pyinotify.ProcessEvent):
    def process_IN_MODIFY(selfself, Event):
        print 'IN_MODIFY'
        
class Empty(pyinotify.processEvent):
    self._mesg = msg
    print msg

# Instanciate a new WatchManager (will be used to store watches).
wm = pyinotify.WatchManager()
# Associate this WatchManager with a Notifier (will be used to report and
# process events).
handler = Empty(TrackModifications())
notifier = pyinotify.Notifier(wm)
# Add a new watch on /test for ALL_EVENTS.
wm.add_watch('/test', pyinotify.ALL_EVENTS)
# Loop forever and handle events.
notifier.loop()