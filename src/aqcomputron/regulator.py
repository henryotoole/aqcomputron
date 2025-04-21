"""
Class that does the actual work. Singleton.
"""
__author__ = "Josh Reed"

# My code
from aqcomputron import SensorAwair, Vents, config, logger

# Other libs

# Base python
import time
import traceback

class Regulator:
	"""
	Singleton class to perform regulation. Does not start till 'start()' is called. Pulls all intersting values
	from config.
	"""

	def __init__(self):
		"""
		"""
		self.ts_last_switch = 0
		"""Timestamp of last time the power switch was toggled."""
		self.power_switch_cooldown = 60
		"""Min time after switch is toggled that it can be toggled again."""
		self.co2_ppm_max = config['CO2_PPM_MAX']
		"""If the PPM goes above this number, fans are turned on."""
		self.co2_ppm_min = config['CO2_PPM_MIN']
		"""Fans stay on until PPM dips below this number."""

		self.sensor = SensorAwair(config['AWAIR_IP'])
		self.vent_control = Vents(config['PIN_MAIN_FAN_RELAY'])

	def start(self):
		"""Start the main loop of the Regulator, which will proceed until the process is killed. All exceptions
		are handled and printed via structlog to STDOUT."""
		logger.info("Starting aqcomputron main loop.")
		while True:
			try:
				self.operation()
			except Exception:
				logger.error(traceback.format_exc())
			time.sleep(15)

	@property
	def can_toggle(self):
		"""Test whether or not can toggle power switch (there's a cooldown)"""
		return (time.time() - self.ts_last_switch) > self.power_switch_cooldown

	def operation(self):
		"""Perform actions for this loop of the regulator."""

		co2_ppm = self.sensor.get_co2_ppm()
		logger.info(f"CO2 level is: {co2_ppm}")

		# If the fans are on, we are waiting for the lower PPM to be reached.
		if self.vent_control.main_fan_state:
			if co2_ppm < self.co2_ppm_min:
				self.set_fan_state(False)
		# If they are off, we're checking for the levels to exceed max.
		else:
			if co2_ppm > self.co2_ppm_max:
				self.set_fan_state(True)

	def set_fan_state(self, state: bool):
		"""Wraps the fan state set function with some state control. This will not actually set fan state unless
		the cooldown from last toggle has expired."""
		if self.can_toggle:
			verb = "on" if state else "off"
			logger.info(f"Turning fans {verb}")
			self.vent_control.main_fan_set_state(state)
			self.ts_last_switch = time.time()