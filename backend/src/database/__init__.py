"""MongoDB database package for the AI textbook platform."""

from .connection import (
    get_database,
    connect_to_mongo,
    close_mongo_connection,
    get_sync_client,
    client
)

__all__ = [
    "get_database",
    "connect_to_mongo",
    "close_mongo_connection",
    "get_sync_client",
    "client"
]