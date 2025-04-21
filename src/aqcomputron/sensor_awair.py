"""
Implementation of Sensor that uses and Awair Element to get AQ data.
"""
__author__ = "Josh Reed"

# Project code
from aqcomputron import RequestNon200Exception, Sensor

# Other libs
import requests

# Base python

class SensorAwair(Sensor):
	"""
	Sensor is a stateless class that exists to allow implementations and tests to overwrite its methods.
	"""

	def __init__(self, awair_ip: str):
		"""Create a new abstract class to represent and interact with an Awair Element.

		Args:
			awair_ip (str): the IP address of the awair element
		"""
		self.awair_ip = awair_ip

	def get_co2_ppm(self) -> int:
		"""Returns:
			int: The air CO2 PPM
		"""
		latest_data = self._get_current_report()

		return latest_data['co2']

	def _get_current_report(self) -> dict:
		"""Sends request to get data from the machine. All network errors simply raise.
		
		Returns:
			dict: Key/value pairs from the Awair Element's air-data / latest.
		"""
		url = f"http://{self.awair_ip}/air-data/latest"

		response = requests.get(url, timeout=5)

		if response.status_code != 200:
			raise RequestNon200Exception(url, response)

		return response.json()
