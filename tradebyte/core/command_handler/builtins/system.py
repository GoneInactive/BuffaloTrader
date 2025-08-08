from ..base import Command

class HelpCommand(Command):
    @property
    def help_text(self) -> str:
        return "Lists all available commands"

    def execute(self, args) -> dict[str, str]:
        return self._context.command_registry.available_commands

class StatusCommand(Command):
    @property
    def help_text(self) -> str:
        return "Shows system health status"

    def execute(self, args) -> dict:
        return {
            "strategies_running": len(self._context.strategy_engine.running),
            "exchange_connections": self._context.exchange_manager.connection_status()
        }