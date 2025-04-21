"""
Entry point into the CLI interface.
"""
__author__ = "Josh Reed"

# My code
from aqcomputron import Regulator, Vents, config

# Other libs

# Base python
import fire

def run():
	reg = Regulator()
	reg.start()

def override(val):
	"""Override the current main power relay status. This will last until the program next makes a change.
	
	Args:
		val (str): Either 'on' or 'off'
	"""
	if not val in ['on', 'off']:
		print("Valid power states are 'on' and 'off'")

	vent_control = Vents(config['PIN_MAIN_FAN_RELAY'])
	
	if val == 'on':
		vent_control.main_fan_set_state(True)
	if val == 'off':
		vent_control.main_fan_set_state(False)

if __name__ == '__main__':
	
	options = {
		'run': run,
		'override': override
	}
	
	fire.Fire(options)