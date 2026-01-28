"""
Shared configuration and constants for OnePlus ARB Checker.
"""

from typing import Dict, TypedDict

# Constants
BASE_URL = "https://roms.danielspringer.at/index.php?view=ota"
OOS_API_URL = "https://oosdownloader-gui.fly.dev/api/oneplus"
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
HISTORY_DIR = "data/history"

# Type definitions
class DeviceModels(TypedDict, total=False):
    GLO: str
    EU: str
    IN: str
    CN: str

class DeviceMeta(TypedDict):
    name: str
    models: DeviceModels

# Device Metadata
# Used for display names, model numbers, and mapping internal IDs to names
DEVICE_METADATA: Dict[str, DeviceMeta] = {
    "15": {
        "name": "OnePlus 15",
        "models": {
            "GLO": "CPH2747",
            "EU": "CPH2747",
            "IN": "CPH2745",
            "CN": "PLK110"
        }
    },
    "15R": {
        "name": "OnePlus 15R", 
        "models": {
            "GLO": "CPH2741",
            "EU": "CPH2741",
            "IN": "CPH2741"
        }
    },
    "13": {
        "name": "OnePlus 13",
        "models": {
            "GLO": "CPH2649",
            "EU": "CPH2649",
            "IN": "CPH2649",
            "CN": "PJZ110"
        }
    },
    "12": {
        "name": "OnePlus 12",
        "models": {
            "GLO": "CPH2573", 
            "EU": "CPH2573", 
            "IN": "CPH2573", 
            "CN": "PJD110"
        }
    }
}

# Mapping for fetching firmware (roms.danielspringer.at expects these names)
SPRING_MAPPING = {
    "oneplus_15": "OP 15",
    "oneplus_15r": "OP 15R",
    "oneplus_13": "OP 13",
    "oneplus_12": "OP 12"
}

# Mapping for OOS Downloader API (oosdownloader-gui.fly.dev)
# It seems to use snake_case ids directly, but let's be explicit if needed.
# If keys match the input 'oneplus_XX', we might just pass them through.
# But for consistency, let's keep them here.
OOS_MAPPING = {
    "15": "oneplus_15",
    "15R": "oneplus_15r",
    "13": "oneplus_13",
    "12": "oneplus_12"
}

def get_display_name(device_id: str) -> str:
    """Get the human-readable display name for a device ID."""
    return DEVICE_METADATA.get(device_id, {}).get("name", f"OnePlus {device_id}")

def get_model_number(device_id: str, region: str) -> str:
    """Get the model number for a specific device and region."""
    return DEVICE_METADATA.get(device_id, {}).get("models", {}).get(region, "Unknown")
