"""
Test abstraction to represent the vent controls.
"""
__author__ = "Josh Reed"

# Project code
from aqcomputron import Vents

# Other libs

# Base python

class VentsTest(Vents):
	"""
	This stateless class represents the vent controls and exists so that tests can override the acting methods.
	"""

	def __init__(self):
		"""Create a new vent controller instance for tests.
		"""
		self._state_main_fan_relay = False

	def main_fan_set_state(self, power_state: bool) -> int:
		"""Set the power state of the main fan.

		Args:
			power_state (bool): Whether the fans should be on or off.
		"""
		self._state_main_fan_relay = power_state