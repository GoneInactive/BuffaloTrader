#!/usr/bin/env python3
import asyncio

class TradeByteCore:
    """Minimal core for development"""
    async def handle_command(self, command: str):
        if command == "version":
            return {"version": "0.1.0-dev"}
        elif command == "help":
            return {"help": "Available commands: version, help"}
        return {"error": f"Unknown command: {command}"}

async def cli_loop():
    core = TradeByteCore()
    print("TradeByte Development Console (type 'exit' to quit)")
    
    while True:
        try:
            cmd = input("TradeByte > ").strip()
            if cmd in ("exit", "quit"):
                break
                
            result = await core.handle_command(cmd)
            for k, v in result.items():
                print(f"{k}: {v}")
                
        except KeyboardInterrupt:
            print("\nUse 'exit' to quit")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    asyncio.run(cli_loop())