"""
Abstraction to represent the air quality sensor.
"""
__author__ = "Josh Reed"

# Project code

# Other libs

# Base python
from abc import abstractmethod

class Sensor():
	"""
	Sensor is a stateless class that exists to allow implementations and tests to overwrite its methods.
	"""

	def __init__(self):
		pass

	@abstractmethod
	def get_co2_ppm(self) -> int:
		"""Returns:
			int: The air CO2 PPM
		"""
		pass