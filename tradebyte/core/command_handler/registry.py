# tradebyte/core/command_handler/registry.py
class CommandRegistry:
    def __init__(self):
        self._commands = {}
    
    def register(self, name: str, command_class):
        self._commands[name.lower()] = command_class