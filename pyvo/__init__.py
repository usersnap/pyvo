VERSION = 0, 1, 0
DEV_STATUS = 3 # Alpha

from .client import Client, ResourceNotFound

__all__ = (Client, ResourceNotFound)
