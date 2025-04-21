"""
Tests for the Awair Sensor class. Note that these all require a working Awair Elementon the network.
"""

# Project code
from aqcomputron import SensorAwair, config

# Other libs
import pytest

# Base python

def test_get_co2():

	sensor = SensorAwair(config['AWAIR_IP'])
	assert int(sensor.get_co2_ppm()) > 0
	print(f"Sensor currently reads {sensor.get_co2_ppm()}ppm CO2")