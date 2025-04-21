

# Other libs
from hacutils import config as hac_config
import structlog

# Base python
import pathlib
import os


project_path = pathlib.Path(__file__).parent.parent.resolve()
"""This is the root path to the project and git repository.
"""

from aqcomputron.cfg import Config, CONFIG_DEFAULTS

# Import the config
try:
	config: Config = hac_config.load_config(hac_config.find_config(project_path, 'aqcomputron'))
except ValueError as e:
	hac_config.generate_from_defaults("./aqcomputron.default.cfg", CONFIG_DEFAULTS)
	print(f"A default config file has been placed at {os.path.abspath('./aqcomputron.default.cfg')}")
	raise
hac_config.defaults_apply(config, CONFIG_DEFAULTS)

# Configure the logger
import aqcomputron.logger
logger: structlog.stdlib.BoundLogger = structlog.get_logger()


# Import structure
from aqcomputron.exc import RequestNon200Exception
from aqcomputron.sensor import Sensor
from aqcomputron.sensor_awair import SensorAwair
from aqcomputron.vents import Vents
from aqcomputron.regulator import Regulator