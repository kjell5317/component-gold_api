"""Constants for gold_api."""
# Base component constants
NAME = "GoldAPI"
DOMAIN = "gold_api"
DOMAIN_DATA = f"{DOMAIN}_data"
VERSION = "0.0.1"
ATTRIBUTION = "Data provided by https://www.goldapi.io/"
ISSUE_URL = "https://github.com/kjell5317/component-gold_api/issues"

# Icons
ICON = "mdi:gold"

# Platforms
SENSOR = "sensor"
PLATFORMS = [SENSOR]

# Unit
UNIT = "€"

# Configuration and options
CONF_AMOUNT = "amount"

# Defaults
DEFAULT_NAME = "gold"

STARTUP_MESSAGE = f"""
-------------------------------------------------------------------
{NAME}
Version: {VERSION}
This is a custom integration!
If you have any issues with this you need to open an issue here:
{ISSUE_URL}
-------------------------------------------------------------------
"""
