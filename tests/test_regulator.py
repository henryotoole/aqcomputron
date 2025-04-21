"""Test the main regulator class state changes"""

# Project code
from tests.fixtures import VentsTest, SensorTest
from aqcomputron import Regulator

# Other libs
import pytest

# Base python
import time

@pytest.fixture
def regulator():

	reg = Regulator()
	reg.sensor = SensorTest(400)
	reg.vent_control = VentsTest()

	return reg

def test_regulator_operation(regulator):
	"""Test state throughout regular operation."""

	regulator.co2_ppm_max = 1200
	regulator.co2_ppm_min = 900

	regulator.sensor.set_co2_ppm(600)

	assert regulator.vent_control.main_fan_state == False

	# Perform an operation where nothing should change as levels are low.
	regulator.operation()
	assert regulator.vent_control.main_fan_state == False

	# Now raise levels past min. Nothing should change.
	regulator.sensor.set_co2_ppm(1000)
	regulator.operation()
	assert regulator.vent_control.main_fan_state == False

	# Now raise past max. Fan should come on.
	regulator.sensor.set_co2_ppm(1500)
	regulator.operation()
	assert regulator.vent_control.main_fan_state == True

	# Lower below max. Nothing should change
	regulator.sensor.set_co2_ppm(1000)
	regulator.operation()
	assert regulator.vent_control.main_fan_state == True

	# Lower below min. Nothing should change, as the timeout has not expired.
	regulator.sensor.set_co2_ppm(600)
	regulator.operation()
	assert regulator.vent_control.main_fan_state == True

	# Alter the timeout and wait a moment. Now it should change.
	regulator.power_switch_cooldown = 0.1
	time.sleep(0.25)
	regulator.operation()
	assert regulator.vent_control.main_fan_state == False