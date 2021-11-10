"""Sample API Client."""
import logging
import asyncio
import socket
from typing import Optional
import aiohttp
import async_timeout

TIMEOUT = 10


_LOGGER: logging.Logger = logging.getLogger(__package__)


class IntegrationGoldApiClient:
    def __init__(
        self, api_key: str, amount: str, session: aiohttp.ClientSession
    ) -> None:
        """Sample API Client."""
        self.headers = {
        'x-access-token': api_key,
        'Content-Type': 'application/json'
        }
        self.amount = amount
        self._session = session

    async def async_get_data(self) -> float:
        """Get data from the API."""
        url = "https://www.goldapi.io/api/XAU/EUR"
        return await self.api_wrapper("get", url)


    async def api_wrapper(
        self, method: str, url: str, data: dict = {}, headers: dict = {}
    ) -> float:
        """Get information from the API."""
        try:
            async with async_timeout.timeout(TIMEOUT, loop=asyncio.get_event_loop()):
                if method == "get":
                    response = await self._session.get(url, headers=self.headers)
                    json =  await response.json()
                    return round(float(json["price"]) * 0.035274 * float(self.amount), 2)

        except asyncio.TimeoutError as exception:
            _LOGGER.error(
                "Timeout error fetching information from %s - %s",
                url,
                exception,
            )

        except (KeyError, TypeError) as exception:
            _LOGGER.error(
                "Error parsing information from %s - %s",
                url,
                exception,
            )
        except (aiohttp.ClientError, socket.gaierror) as exception:
            _LOGGER.error(
                "Error fetching information from %s - %s",
                url,
                exception,
            )
        except Exception as exception:  # pylint: disable=broad-except
            _LOGGER.error("Something really wrong happened! - %s", exception)
