#!/usr/bin/env python3
import math
import time

import odrive
from odrive.enums import AxisState, ControlMode, InputMode
from odrive.utils import dump_errors, request_state

# Find a connected ODrive (this will block until you connect one)
print("waiting for ODrive...")
odrv0 = odrive.find_sync()
print(f"found ODrive {odrv0._dev.serial_number}")


# BLDC Config (Works in odrivetool)

odrv0.erase_configuration

odrv0.config.brake_resistance = 2

odrv0.config.dc_max_positive_current = 10

odrv0.config.dc_max_negative_current = -2.0

odrv0.config.max_regen_current = 0

odrv0.save_configuration

odrv0.axis0.controller.config.pos_gain = 20

odrv0.axis0.controller.config.vel_gain = 0.02

odrv0.axis0.controller.config.vel_integrator_gain = 0.01

odrv0.axis0.controller.config.control_mode = 2 #ControlMode.VELOCITY_CONTROL

odrv0.axis0.controller.config.vel_limit = 100

odrv0.axis0.motor.config.current_lim = 50

odrv0.axis0.motor.config.pole_pairs = 7

odrv0.axis0.motor.config.direction = 1

odrv0.axis0.sensorless_estimator.config.pm_flux_linkage = 5.51328895422/(7*730)

odrv0.axis0.requested_state = 4 #AxisState.MOTOR_CALIBRATION

odrv0.axis0.motor

print(f"{odrv0.axis0.motor}")

#Sensorless Control (Doesn't Work)

odrv0.axis0.motor.config.pre_calibrated = True

odrv0.axis0.requested_state = AxisState.SENSORLESS_CONTROL

odrv0.axis0.config.startup_sensorless_control = True

odrv0.save_configuration

odrv0.reboot

odrv0.axis0.controller.input_vel = 1

print(f"{odrv0.axis0.controller.input_vel}")
print(f"{odrv0.axis0.sensorless_estimator.vel_estimate}")
