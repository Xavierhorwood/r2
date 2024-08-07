from hub import light_matrix
import runloop
import uos
import hub
from hub import button
import motor_pair
from hub import port
import force_sensor
import uasyncio as asyncio
import motor

import random

head = port.B
left = port.E
right = port.F
button_2 = port.A

async def move_head_at_random():
    #motor.run(head, 1000)
    #make it move at random speeds and directions
    while True:
        await motor.run_for_time(head, 1000, random.randint(1000, 2000))
        #await asyncio.sleep(2)

async def play_sound():
    #play r2d2 sound at a random time in a loop
    while True:
        await asyncio.sleep(random.randint(1, 5))
        #in beep(frequency: int = 440, duration: int = 500, volume: int = 100, *, attack: int = 0, decay: int = 0, sustain: int = 100, release: int = 0, transition: int = 10, waveform: int = WAVEFORM_SINE, channel: int = DEFAULT) -> Awaitable

async def main4():
    motor_pair.pair(motor_pair.PAIR_1, left, right)
    start = False
    while True:
        if force_sensor.pressed(button_2):
            start = True
        while start:
            if force_sensor.pressed(button_2):
                start = False
            #motor_pair.move(motor_pair.PAIR_1, 0, velocity=-1000, acceleration=5000)
            motor_pair.move_tank_for_time(motor_pair.PAIR_1, -10000, -10000, 6655, acceleration=10000, duration=100)
            #yield
        #yield

        await asyncio.sleep(0.1)

async def main():
    await asyncio.gather(
            move_head_at_random(),
            main4()
        )

asyncio.run(main())
