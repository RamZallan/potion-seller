""" potion_seller.machine

Simple objects based on the current implementation of drink pi.

Access to w1 devices mounted by owfs should happen here.

Slot status can be found by attempting to access::

    $OWFS_MNT/<address>/id

Slot motors can be enabled by echoing 1 into::

    $OWFS_MNT/<address>/PIO

Little Drink should have like a 1s drop time, big drink should only be enabled for .5s

"""
import subprocess
import time

class Machine():
    def __init__(self, name, slot_addresses, temp_sensor=None):
        self.name = name
        self.slots = [Slot(address) for address in slot_addresses]
        self.temp = temp_sensor
        print('Creating machine ' + self.name + ' with addresses: ' + ', '.join([str(s) for s in self.slots]))

    def drop(self, slot_num):
        if slot_num > len(self.slots) or slot_num < 1:
            raise ValueError('{} is an invalid slot number for {}'.format(slot_num, self.name))
        return self.slots[slot_num-1].drop()


class Slot():
    def __init__(self, w1_id):
        self.w1_id = w1_id;
        self.lock = False

    def __repr__(self):
        return str('<Slot [{}]>'.format(self.w1_id))

    def __str__(self):
        return self.w1_id

    def get_status(self):
        pass

    def get_lock(self):
        return self.lock

    def lock(self):
        self.lock = True

    def unlock(self):
        self.lock = False

    def drop(self):
        pass

