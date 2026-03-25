"""Configuration and key management for Atia Shrine Automation."""

import json
from pathlib import Path
from typing import Any, Dict, List

# Path to private keys file
KEYS_FILE = Path("privateKeys")


def get_keys(key: str) -> Any:
    """Load a specific key from the privateKeys configuration file.
    
    Args:
        key: The key name to retrieve (e.g., 'keys', 'delegateeAddresses')
    
    Returns:
        The value associated with the key from the JSON config
    """
    with open(KEYS_FILE, "r") as f:
        return json.load(f)[key]


def validate_keys() -> None:
    """Validate that the privateKeys file exists and contains valid keys.
    
    Raises:
        Exception: If privateKeys file is missing or no keys are defined
    """
    if not KEYS_FILE.exists():
        raise Exception("privateKeys file not found")
    
    try:
        keys = get_keys("keys")
        if not isinstance(keys, list) or len(keys) <= 0:
            raise Exception("No keys defined")
    except KeyError:
        raise Exception("No keys defined in privateKeys file")
