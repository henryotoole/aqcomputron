"""
A file where we declare and typehint the config.
"""
__author__ = "Josh Reed"

# Our code

# Other libs

from hacutils.config import CfgEntry

# Base python
from typing import TypedDict

# This exists only to typehint the config object.
class Config(TypedDict):
	AWAIR_IP: str
	PIN_MAIN_FAN_RELAY: int
	CO2_PPM_MAX: int
	CO2_PPM_MIN: int

CONFIG_DEFAULTS = [
	CfgEntry('AWAIR_IP', default=None, comment="The IP address of the Awair Element on the local network."),
	CfgEntry('PIN_MAIN_FAN_RELAY', default=14, comment="BCM-Number of pin that controls the Main Fan Relay."),
	CfgEntry('CO2_PPM_MAX', default=1200, comment="If the PPM goes above this number, fans are turned on."),
	CfgEntry('CO2_PPM_MIN', default=900, comment="Fans stay on until PPM dips below this number.")
]