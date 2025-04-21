"""
Implementation of Sensor for tests that enables custom control of data.
"""
__author__ = "Josh Reed"

# Project code
from aqcomputron import Sensor

# Other libs

# Base python

class SensorTest(Sensor):

	def __init__(self, initial_val: int):
		"""Create a new abstract class to represent and interact with an Awair Element.

		Args:
			initial_val (int): initial value of CO2 ppm
		"""
		self.co2_ppm = initial_val

	def get_co2_ppm(self) -> int:
		"""Returns:
			int: The air CO2 PPM
		"""
		return self.co2_ppm

	def set_co2_ppm(self, val):
		self.co2_ppm = val