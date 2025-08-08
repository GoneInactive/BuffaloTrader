from ..base import Command
from importlib.metadata import version  

class VersionCommand(Command):
    """Displays the current TradeByte version"""
    
    @property
    def help_text(self) -> str:
        return "Returns the current TradeByte version and core dependencies"

    def execute(self, args: dict) -> dict:
        try:
            # Modern Python (3.8+) approach
            tb_version = version("tradebyte")
        except ImportError:
            # Fallback for older Python
            raise ImportError('Cannot Import Version')

        return {
            "tradebyte": tb_version,
            "python": self._get_python_version(),
            "core_dependencies": self._get_core_deps()
        }

    def _get_python_version(self) -> str:
        import sys
        return f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"

    def _get_core_deps(self) -> dict:
        """Returns versions of critical dependencies"""
        deps = ['numpy', 'pandas', 'aiohttp']
        versions = {}
        
        for dep in deps:
            try:
                versions[dep] = version(dep)
            except:
                versions[dep] = "Not found"
                
        return versions