"""Coding: utf-8 ."""
from threading import Thread
import state
import queues
from semaphores import kivyuisignaler


class UIkivySignaler(Thread):
    """UI kivy Signaler Class."""

    def run(self):
        """Run Signal Thread."""
        kivyuisignaler.acquire()
        while state.shutdown == 0:
            try:
                command, data = queues.UISignalQueue.get()
                if command == 'writeNewAddressToTable':
                    label, address, streamNumber = data
                    state.kivyapp.variable_1.append(address)
                elif command == 'rerenderAddressBook':
                    state.kivyapp.obj_1.refreshs()
                elif command == 'updateSentItemStatusByAckdata':
                    state.kivyapp.status_dispatching(data)

            except Exception as e:
                print(e)
