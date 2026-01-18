#!/usr/bin/env -S PYTHONPATH=../telemetry python3

from telemetry.config_log import *
from push_back.events import *

# Open log based on config
config_open_log()

calibrate_and_wait()

increment = 200


def driver_function():
    """Function for the driver part of a competition match"""

    log(("Competition", "competition"), "driver_begin")

    # Add driver logic here
    # Note that event handling is initialized outside of this function by init_event_handling()

    log(("Competition", "competition"), "driver_end")

"""
def autonomous_function():
    # Function for the autonomous part of a competition match

    log(("Competition", "competition"), "autonomous_begin")

    robot_position.reset(Position(-1250, -380))
    reset_heading_to_aim(Position(-1250, -1200), FORWARD)
    flap.set(True)
    matchload.set(True)
    conveyor.spin(REVERSE, FORWARD, FORWARD)
    descore.set(True)

    trigger_mover.move(Position(-1250, -1200), FORWARD)
    trigger_turner.turn(90, FRAME_HEADING_RELATIVE)
    trigger_turner.turn(270, FRAME_ABSOLUTE)
    
    # empty loader 1
    matchload.set(True)
    conveyor.spin(REVERSE, FORWARD, FORWARD)
    trigger_driver.drive_for_time(1300, 20, True, 243)  
    # trigger_driver.drive(-15)
    reset_robot_position_and_heading_to_gps()
    wait(650, MSEC)
    conveyor.spin(REVERSE, STOP, FORWARD)
    wait(1105, MSEC)
    trigger_mover.move(Position(-1200, -1200), REVERSE)
    matchload.set(False)

    trigger_turner.turn(-180, FRAME_ABSOLUTE)
    trigger_mover.move(Position(-1200, -1500), FORWARD)
    trigger_turner.turn(-270, FRAME_ABSOLUTE)

    # drive to other side
    trigger_mover.move(Position(900, -1500), FORWARD)

    trigger_turner.turn(-90, FRAME_HEADING_RELATIVE)
    trigger_turner.turn(0, FRAME_ABSOLUTE)
    trigger_mover.move(Position(900, -1200), FORWARD)
    trigger_turner.turn(-90, FRAME_HEADING_RELATIVE)
    trigger_turner.turn(-90, FRAME_ABSOLUTE)

    # score load 1 in long goal 1
    conveyor.spin(STOP, STOP, STOP)
    flap.set(False)
    trigger_mover.move(Position(835, -1200), FORWARD)
    trigger_turner.turn(-90, FRAME_ABSOLUTE)
    conveyor.spin(REVERSE, FORWARD, FORWARD)
    wait(6000, MSEC)
    trigger_driver.drive(-30)

    trigger_turner.turn(180, FRAME_HEADING_RELATIVE)
    matchload.set(True)
    trigger_turner.turn(90, FRAME_ABSOLUTE)
    trigger_mover.move(Position(1200, -1200), FORWARD)
    flap.set(True)

    # empty loader 2
    trigger_driver.drive_for_time(1300, 30, True, 243)
    # trigger_driver.drive(-15)
    reset_robot_position_and_heading_to_gps()
    wait(650, MSEC)
    conveyor.spin(REVERSE, STOP, FORWARD)
    wait(1105, MSEC)
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
    # trigger_driver.drive_for_time(1000, 100, True, 900)

    log(("Competition", "competition"), "autonomous_end")
"""

def autonomous_function():
    """Function for the autonomous part of a competition match"""

    log(("Competition", "competition"), "autonomous_begin")

    robot_position.reset(Position(-1250, -380))
    reset_heading_to_aim(Position(-1250, -1200), FORWARD)
    flap.set(True)
    matchload.set(True)
    conveyor.spin(REVERSE, FORWARD, FORWARD)
    descore.set(True)

    trigger_mover.move(Position(-1250, -1200), FORWARD)
    trigger_turner.turn(90, FRAME_HEADING_RELATIVE)
    trigger_turner.turn(270, FRAME_ABSOLUTE)
    
    # empty loader 1
    matchload.set(True)
    conveyor.spin(REVERSE, FORWARD, FORWARD)
    trigger_driver.drive_for_time(1300, 20, True, 243)  
    trigger_driver.drive(-15)
    trigger_driver.drive(15)
    reset_robot_position_and_heading_to_gps()
    wait(650, MSEC)
    conveyor.spin(REVERSE, STOP, FORWARD)
    wait(1105, MSEC)
    trigger_mover.move(Position(-1200, -1200), REVERSE)
    matchload.set(False)

    # score loader 1
    flap.set(False)
    trigger_turner.turn(270, FRAME_ABSOLUTE)
    conveyor.spin(STOP, STOP, STOP)
    trigger_turner.turn(180, FRAME_HEADING_RELATIVE)
    trigger_turner.turn(90, FRAME_ABSOLUTE)
    trigger_mover.move(Position(-900, -1190))
    trigger_turner.turn(90, FRAME_ABSOLUTE)
    trigger_turner.turn(90, FRAME_ABSOLUTE)
    conveyor.spin(REVERSE, FORWARD, FORWARD)
    wait(6000, MSEC)
    # trigger_driver.drive(30)
    trigger_mover.move(Position(-1200, -1190), REVERSE)
    conveyor.spin(STOP, STOP, STOP)

    trigger_turner.turn(0, FRAME_ABSOLUTE)
    trigger_mover.move(Position(-1200, -600), FORWARD)
    trigger_turner.turn(-270, FRAME_ABSOLUTE)

    # drive to other side
    trigger_mover.move(Position(0, -600), FORWARD)
    trigger_turner.turn(0, FRAME_ABSOLUTE)
    reset_robot_position_and_heading_to_gps()
    trigger_mover.move(Position(900, -600), FORWARD)

    trigger_turner.turn(180, FRAME_ABSOLUTE)
    trigger_mover.move(Position(900, -1190), FORWARD)
    trigger_turner.turn(90, FRAME_ABSOLUTE)
    flap.set(True)

    # empty loader 2
    matchload.set(True)
    conveyor.spin(REVERSE, FORWARD, FORWARD)
    trigger_driver.drive_for_time(2000, 20, True, 500)  
    trigger_driver.drive(-15)
    trigger_driver.drive(15)
    reset_robot_position_and_heading_to_gps()
    wait(650, MSEC)
    conveyor.spin(REVERSE, STOP, FORWARD)
    wait(1105, MSEC)
    trigger_mover.move(Position(1200, -1200), REVERSE)
    matchload.set(False)

    # score loader 2
    flap.set(False)
    trigger_turner.turn(90, FRAME_ABSOLUTE)
    conveyor.spin(STOP, STOP, STOP)
    trigger_turner.turn(180, FRAME_HEADING_RELATIVE)
    trigger_turner.turn(270, FRAME_ABSOLUTE)
    trigger_mover.move(Position(900, -1210))
    trigger_driver.drive(100)
    trigger_turner.turn(270, FRAME_ABSOLUTE)
    trigger_turner.turn(270, FRAME_ABSOLUTE)
    conveyor.spin(REVERSE, FORWARD, FORWARD)
    wait(6000, MSEC)
    # trigger_driver.drive(30)
    trigger_mover.move(Position(1200, -1200), REVERSE)
    conveyor.spin(STOP, STOP, STOP)

    trigger_driver.drive(-500)
    trigger_mover.move(Position(-1500, 0), REVERSE)

    """
    trigger_turner.turn(-180, FRAME_ABSOLUTE)
    trigger_mover.move(Position(-1200, -1500), FORWARD)
    trigger_turner.turn(-270, FRAME_ABSOLUTE)

    # drive to other side
    trigger_mover.move(Position(900, -1500), FORWARD)

    trigger_turner.turn(-90, FRAME_HEADING_RELATIVE)
    trigger_turner.turn(0, FRAME_ABSOLUTE)
    trigger_mover.move(Position(900, -1200), FORWARD)
    trigger_turner.turn(-90, FRAME_HEADING_RELATIVE)
    trigger_turner.turn(-90, FRAME_ABSOLUTE)

    # score load 1 in long goal 1
    conveyor.spin(STOP, STOP, STOP)
    flap.set(False)
    trigger_mover.move(Position(835, -1200), FORWARD)
    trigger_turner.turn(-90, FRAME_ABSOLUTE)
    conveyor.spin(REVERSE, FORWARD, FORWARD)
    wait(6000, MSEC)
    trigger_driver.drive(-30)

    trigger_turner.turn(180, FRAME_HEADING_RELATIVE)
    matchload.set(True)
    trigger_turner.turn(90, FRAME_ABSOLUTE)
    trigger_mover.move(Position(1200, -1200), FORWARD)
    flap.set(True)

    # empty loader 2
    trigger_driver.drive_for_time(1300, 30, True, 243)
    # trigger_driver.drive(-15)
    reset_robot_position_and_heading_to_gps()
    wait(650, MSEC)
    conveyor.spin(REVERSE, STOP, FORWARD)
    wait(1105, MSEC)
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
    # trigger_driver.drive_for_time(1000, 100, True, 900)
    """

# Initialize event handling
init_event_handling()

# Register the competition functions
competition = Competition(driver_function, autonomous_function)
