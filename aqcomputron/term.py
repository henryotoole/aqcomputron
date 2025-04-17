"""
Toplevel control terminal.
"""

# My code

# Other libs
import fire

# Base python

def regulate():
	"""Run the standard reglation loop to govern the AQ. Pulls values from config.
	"""
	pass

def fire_term():
	"""Fire off the Fire() command that translates command line utility into action within this module.
	"""
	available = {
		'regulate': regulate,
	}

	fire.Fire(available)