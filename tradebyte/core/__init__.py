from .command_handler.registry import CommandRegistry
from .command_handler.builtins import system, version

class TradeByteCore:
    def __init__(self):
        self.command_registry = CommandRegistry()
        self._register_core_commands()
        
    def _register_core_commands(self):
        self.command_registry.register("help", system.HelpCommand)
        self.command_registry.register("status", system.StatusCommand)
        self.command_registry.register("version", version.VersionCommand)
        # Additional commands here

    async def handle_command(self, raw_input: str):
        """Entry point for command execution"""
        parts = raw_input.split()
        if not parts:
            return {"error": "Empty command"}
            
        cmd_name, *args = parts
        try:
            cmd = self.command_registry.get(cmd_name)
            if isinstance(cmd, AsyncCommand):
                return await cmd.execute(args)
            return cmd.execute(args)
        except Exception as e:
            return {"error": str(e)}