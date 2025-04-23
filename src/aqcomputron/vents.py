"""
Abstraction to represent the vent controls.
"""
__author__ = "Josh Reed"

# Project code
import RPi.GPIO as GPIO

# Other libs

# Base python

class Vents():
	"""
	This stateless class represents the vent controls and exists so that tests can override the acting methods.
	"""

	def __init__(self, main_fan_relay_pin: int):
		"""Create a new vent controller instance (only one should ever be needed). Sets up pins etc.

		Args:
			main_fan_relay_pin (int): The BCM pin number of the main fan relay pin.
		"""
		self.pin_main_fan_relay = main_fan_relay_pin

		GPIO.setmode(GPIO.BCM)
		GPIO.setup(self.pin_main_fan_relay, GPIO.OUT)
		GPIO.output(self.pin_main_fan_relay, GPIO.LOW)

		self._state_main_fan_relay = False

	def main_fan_set_state(self, power_state: bool) -> int:
		"""Set the power state of the main fan.

		Args:
			power_state (bool): Whether the fans should be on or off.
		"""
		
		GPIO.output(self.pin_main_fan_relay, GPIO.HIGH if power_state else GPIO.LOW)
		self._state_main_fan_relay = power_state

	@property
	def main_fan_state(self) -> bool:
		"""Returns:
			bool: The power state of the main fan.
		"""
		return self._state_main_fan_relay