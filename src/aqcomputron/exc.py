"""
Exceptions
"""
__author__ = "Josh Reed"


class RequestNon200Exception(ValueError):
	"""A request returned a response with a non-200 response code.
	"""

	def __init__(self, url, response, **kwargs):
		"""Args:
			url (str): The URL of the request
			response (Response): The response to the request
		"""
		self.url = url
		self.code = response.status_code
		self.text = response.text
		self.msg = f"POST {url} yields non-200 status code: {response.status_code} {response.text}"
		super().__init__(self.msg, **kwargs)