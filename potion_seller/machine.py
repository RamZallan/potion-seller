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
    def __init__(self, name, slot_addresses, temp_sensor=None, drop_timing=0.5):
        self.name = name
        self.slots = [Slot(address) for address in slot_addresses]
        self.temp = Sensor(temp_sensor, drop_timing)

        print('Creating machine ' + self.name + ' with addresses: ' + ', '.join([str(s) for s in self.slots]))

    def drop(self, slot_num):
        if slot_num > len(self.slots) or slot_num < 1:
            raise ValueError('{} is an invalid slot number for {}'.format(slot_num, self.name))
        return self.slots[slot_num-1].drop()

    def get_status(self):
        buff = ''
        for i in range(len(self.slots)):
            buff += "Slot {} ({}) is ".format(i+1, str(self.slots[i]))
            if self.slots[i].get_status():
                buff += "active\n"
            else:
                buff += "disabled\n"

        return buff

    def temperature(self):
        return self.temp.temperature()


class Slot():
    def __init__(self, w1_id, timing):
        self.w1_id = w1_id
        self._lock = False
        self.timing = timing

    def __repr__(self):
        return str('<Slot [{}]>'.format(self.w1_id))

    def __str__(self):
        return self.w1_id

    def get_status(self):
        try:
            file = open("/mnt/w1/{}/id".format(self.w1_id))
            print('Slot {} active'.format(self.w1_id))
            file.close()
        except:
            print('Slot {} disabled'.format(self.w1_id))
            return False
        return True

    def get_lock(self):
        return self._lock

    def lock(self):
        self._lock = True

    def unlock(self):
        self._lock = False

    def drop(self):
        if self.get_status():
            if not self.get_lock():
                self.lock()
                try:
                    subprocess.call("echo '1' > /mnt/w1/{}/PIO".format(self.w1_id), shell=True)
                    time.sleep(self.timing)
                    subprocess.call("echo '0' > /mnt/w1/{}/PIO".format(self.w1_id), shell=True)
                except IOError:
                    print('bad')
                time.sleep(2)
                self.unlock()
                return True

        return False


class Sensor():
    def __init__(self, w1_id):
        self.w1_id = w1_id

    def temperature(self):
        try:
            with open('/mnt/w1/{}/temperature12'.format(self.w1_id), 'r') as temp_file:
                temperature = temp_file.read().rstrip()
                f_temperature = float(temperature) * (9.0/5.0) + 32.0
        except IOError as e:
            return -1
        return f_temperature

