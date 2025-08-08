"""TradeByte - Algorithmic Trading Framework for CU Quants"""
from importlib.metadata import version
from typing import Union

# Version management
__version__ = "0.1.0-dev"  # Must match pyproject.toml
try:
    __version__ = version(__name__)  # Override with installed version if available
except ImportError:
    pass  # Use hardcoded version if metadata not available

# Core API exports
from tradebyte.core import TradeByteCore
from tradebyte.core.command_handler import CommandRegistry
from tradebyte.strategies import BaseStrategy  # Your base strategy class

# Type definitions for public API
__all__ = [
    'TradeByteCore',
    'CommandRegistry',
    'BaseStrategy',
    '__version__',
]

# Package initialization checks
def _check_dependencies():
    """Verify critical dependencies are present"""
    required = {
        'numpy': '1.21+',
        'pandas': '1.3+',
        'aiohttp': '3.8+'
    }
    
    missing = []
    for pkg, req_version in required.items():
        try:
            pkg_version = version(pkg)
            if pkg_version < req_version:
                missing.append(f"{pkg}>={req_version} (found {pkg_version})")
        except ImportError:
            missing.append(f"{pkg}>={req_version}")
    
    if missing:
        raise ImportError(
            f"Missing required dependencies:\n"
            f"{', '.join(missing)}\n"
            f"Install with: pip install {' '.join(required.keys())}"
        )

# Run checks on import (optional)
_check_dependencies()