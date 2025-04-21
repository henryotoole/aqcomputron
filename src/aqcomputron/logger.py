"""
Setup / configuration for logging.

Some notes on the strategy here:
I'm experimenting with the principles set down here:
https://www.structlog.org/en/stable/logging-best-practices.html
https://12factor.net/logs

In development, of course, it shall simply hit the terminal.
"""
__author__ = "Josh Reed"

# Our code

# Other libs
import structlog
from structlog.stdlib import LoggerFactory

# Base python
import sys

### Configure Structlog ###
# Processors that have nothing to do with output, e.g., add timestamps or log level names.
shared_processors = [
	# None yet
]

if sys.stderr.isatty():
	# Pretty printing when we run in a terminal session.
	# Automatically prints pretty tracebacks when "rich" is installed
	processors = shared_processors + [
		structlog.dev.ConsoleRenderer(),
	]
else:
	# Print JSON when we run, e.g., in a Docker container.
	# Also print structured tracebacks.
	processors = shared_processors + [
		structlog.processors.dict_tracebacks,
		structlog.processors.JSONRenderer(),
	]

structlog.configure(
	processors=processors
)