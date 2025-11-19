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

# Motor Calibration
odrv0.axis0.config.startup_motor_calibration
odrv0.axis0.config.startup_encoder_index_search
odrv0.axis0.config.startup_encoder_offset_calibration
odrv0.axis0.config.startup_closed_loop_control 