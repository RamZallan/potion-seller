import time
from unittest.mock import MagicMock


def delay(return_value, seconds):
    time.sleep(seconds)
    return return_value


def mock_sensor(sensor):
    sensor.temperature = MagicMock(return_value=delay(42.0, 0.1))
    return sensor


def mock_slot(slot, stocked=False, drop=True):
    slot.get_status = MagicMock(side_effect=lambda: delay(stocked, 0.1))
    slot.drop = MagicMock(side_effect=lambda timing: delay(drop, timing + 2))
    return slot


def mock_machine(machine):
    for idx, slot in enumerate(machine.slots):
        stocked = idx != 1  # The second slot will appear to be empty
        drop = idx not in (1, 2)  # The second and third slots will fail to drop
        machine.slots[idx] = mock_slot(slot, stocked, drop)

    machine.temp = mock_sensor(machine.temp)
    return machine
