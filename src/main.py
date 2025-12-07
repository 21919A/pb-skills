#!/usr/bin/env -S PYTHONPATH=../telemetry python3

from telemetry.config_log import *
from push_back.events import *

# Open log based on config
config_open_log()

calibrate_and_wait()


def driver_function():
    """Function for the driver part of a competition match"""

    log(("Competition", "competition"), "driver_begin")

    # Add driver logic here
    # Note that event handling is initialized outside of this function by init_event_handling()

    log(("Competition", "competition"), "driver_end")


def autonomous_function():
    """Function for the autonomous part of a competition match"""

    log(("Competition", "competition"), "autonomous_begin")

    robot_position.reset(Position(-1600, -450))
    reset_heading_to_aim(Position(-900, -450), FORWARD)
    flap.set(True)

    trigger_mover.move(Position(-1200, -450), FORWARD)
    trigger_turner.turn(90, FRAME_HEADING_RELATIVE)
    trigger_mover.move(Position(-1200, -1200), FORWARD)
    trigger_turner.turn(90, FRAME_HEADING_RELATIVE)
    trigger_turner.turn(-90, FRAME_ABSOLUTE)
    
    # empty loader 1
    matchload.set(True)
    conveyor.spin(REVERSE, FORWARD, FORWARD)
    trigger_driver.drive_for_time(1000, 30, True, 243)
    trigger_driver.drive(-35)
    reset_robot_position_and_heading_to_gps()
    wait(600, MSEC)
    conveyor.spin(REVERSE, FORWARD, STOP)
    wait(600, MSEC)
    trigger_mover.move(Position(-1200, -1200), REVERSE)
    matchload.set(False)

    trigger_turner.turn(-180, FRAME_ABSOLUTE)
    trigger_mover.move(Position(-1200, -1500), FORWARD)
    trigger_turner.turn(-270, FRAME_ABSOLUTE)

    # drive to other side
    trigger_mover.move(Position(1200, -1500), FORWARD)

    trigger_turner.turn(-90, FRAME_HEADING_RELATIVE)
    trigger_turner.turn(0, FRAME_ABSOLUTE)
    trigger_mover.move(Position(1200, -1200), FORWARD)
    trigger_turner.turn(-90, FRAME_HEADING_RELATIVE)
    trigger_turner.turn(-90, FRAME_ABSOLUTE)

    # score load 1 in long goal 1
    conveyor.spin(STOP, STOP, STOP)
    flap.set(False)
    trigger_mover.move(Position(835, -1200), FORWARD)
    trigger_turner.turn(-90, FRAME_ABSOLUTE)
    conveyor.spin(REVERSE, FORWARD, FORWARD)
    wait(3000, MSEC)

    trigger_turner.turn(180, FRAME_HEADING_RELATIVE)
    trigger_turner.turn(90, FRAME_ABSOLUTE)
    trigger_mover.move(Position(1200, -1200), FORWARD)
    flap.set(True)

    # empty loader 2
    matchload.set(True)
    trigger_driver.drive_for_time(1000, 30, True, 243)
    trigger_driver.drive(-35)
    reset_robot_position_and_heading_to_gps()
    wait(600, MSEC)
    conveyor.spin(REVERSE, FORWARD, STOP)
    wait(600, MSEC)
    trigger_mover.move(Position(1200, -1200), REVERSE)
    matchload.set(False)

    trigger_turner.turn(180, FRAME_HEADING_RELATIVE)
    trigger_turner.turn(-90, FRAME_ABSOLUTE)

    # score load 2 in long goal 1
    conveyor.spin(STOP, STOP, STOP)
    flap.set(False)
    trigger_mover.move(Position(835, -1200))
    trigger_turner.turn(-90, FRAME_ABSOLUTE)
    conveyor.spin(REVERSE, FORWARD, FORWARD)
    wait(3000, MSEC)

    trigger_driver.drive(-100)
    trigger_turner.turn(90, FRAME_HEADING_RELATIVE)
    trigger_turner.turn(0, FRAME_ABSOLUTE)
    trigger_driver.drive(400)
    trigger_turner.turn(-90, FRAME_HEADING_RELATIVE)

    # come back over
    trigger_mover.move(Position(-1500, -800), FORWARD)
    trigger_turner.turn(90, FRAME_HEADING_RELATIVE)
    trigger_turner.turn(0, FRAME_ABSOLUTE)
    matchload.set(True)

    # park in red park zone
    trigger_driver.drive_for_time(1000, 100, True, 900)

    log(("Competition", "competition"), "autonomous_end")


def autonomous_function2():
    """Different skills path with no ball scoring"""
    robot_position.reset(Position(-1600, -450))
    reset_heading_to_aim(Position(-900, -450), FORWARD)
    flap.set(True)

    trigger_mover.move(Position(-1200, -450), FORWARD)
    trigger_turner.turn(90, FRAME_HEADING_RELATIVE)
    trigger_mover.move(Position(-1200, -1200), FORWARD)
    trigger_turner.turn(90, FRAME_HEADING_RELATIVE)
    trigger_turner.turn(-90, FRAME_ABSOLUTE)
    
    # empty loader 1
    matchload.set(True)
    conveyor.spin(REVERSE, FORWARD, FORWARD)
    trigger_driver.drive_for_time(1000, 30, True, 243)
    trigger_driver.drive(-35)
    reset_robot_position_and_heading_to_gps()
    wait(600, MSEC)
    conveyor.spin(REVERSE, FORWARD, STOP)
    wait(600, MSEC)
    trigger_mover.move(Position(-1200, -1200), REVERSE)
    matchload.set(False)

    trigger_turner.turn(-180, FRAME_ABSOLUTE)
    trigger_mover.move(Position(-1200, -1500), FORWARD)
    trigger_turner.turn(-270, FRAME_ABSOLUTE)

    # drive to other side
    conveyor.spin(REVERSE, FORWARD, FORWARD)
    flap.set(False) # empty balls out
    trigger_mover.move(Position(1200, -1500), FORWARD)

    trigger_turner.turn(-90, FRAME_HEADING_RELATIVE)
    trigger_turner.turn(0, FRAME_ABSOLUTE)
    trigger_mover.move(Position(1200, -1200), FORWARD)
    flap.set(True)
    trigger_turner.turn(90, FRAME_HEADING_RELATIVE)
    trigger_turner.turn(90, FRAME_ABSOLUTE)

    # empty loader 2
    matchload.set(True)
    trigger_driver.drive_for_time(1000, 30, True, 243)
    trigger_driver.drive(-35)
    reset_robot_position_and_heading_to_gps()
    wait(600, MSEC)
    conveyor.spin(REVERSE, FORWARD, STOP)
    wait(600, MSEC)
    trigger_mover.move(Position(1200, -1200), REVERSE)
    matchload.set(False)

    trigger_turner.turn(-90, FRAME_HEADING_RELATIVE)
    trigger_turner.turn(0, FRAME_ABSOLUTE)
    flap.set(False) # empty balls out
    conveyor.spin(REVERSE, FORWARD, FORWARD)
    trigger_mover.move(Position(1200, 1200), FORWARD)

    trigger_turner.turn(90, FRAME_HEADING_RELATIVE)
    trigger_turner.turn(90, FRAME_ABSOLUTE)
    flap.set(True)

    # empty loader 3
    matchload.set(True)
    trigger_driver.drive_for_time(1000, 30, True, 243)
    trigger_driver.drive(-35)
    reset_robot_position_and_heading_to_gps()
    wait(600, MSEC)
    conveyor.spin(REVERSE, FORWARD, STOP)
    wait(600, MSEC)
    trigger_mover.move(Position(1200, 1200), REVERSE)
    matchload.set(False)
    conveyor.spin(STOP, STOP, STOP)

    trigger_turner.turn(90, FRAME_HEADING_RELATIVE)
    trigger_turner.turn(0, FRAME_ABSOLUTE)
    conveyor.spin(REVERSE, FORWARD, FORWARD)
    flap.set(False) # empty balls out
    trigger_mover.move(Position(1200, 1500), FORWARD)
    trigger_turner.turn(-90, FRAME_HEADING_RELATIVE)
    trigger_turner.turn(270, FRAME_ABSOLUTE)

    # drive to other side
    trigger_mover.move(Position(-1200, 1500), FORWARD)
    trigger_turner.turn(90, FRAME_HEADING_RELATIVE)
    trigger_turner.turn(180, FRAME_ABSOLUTE)
    trigger_mover.move(Position(-1200, 1200), FORWARD)
    trigger_turner.turn(-90, FRAME_HEADING_RELATIVE)
    trigger_turner.turn(270, FRAME_ABSOLUTE)

    # empty loader 4
    matchload.set(True)
    trigger_driver.drive_for_time(1000, 30, True, 243)
    trigger_driver.drive(-35)
    reset_robot_position_and_heading_to_gps()
    wait(600, MSEC)
    conveyor.spin(REVERSE, FORWARD, STOP)
    wait(600, MSEC)
    trigger_mover.move(Position(-1200, 1200), REVERSE)
    matchload.set(False)
    conveyor.spin(STOP, STOP, STOP)

    trigger_mover.move(Position(-1600, -150), FORWARD)

# Initialize event handling
init_event_handling()

# Register the competition functions
competition = Competition(driver_function, autonomous_function)
