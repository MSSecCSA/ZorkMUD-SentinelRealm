#!/usr/bin/env python3
"""
ZorkMUD: Sentinel Realm
A classic text-based adventure game in the spirit of Zork

Main entry point for the game.
"""

import sys
import os
from game_engine import GameEngine

def main():
    """Main function to start the game."""
    print("=" * 50)
    print("    ZorkMUD: Sentinel Realm")
    print("    A Classic Text Adventure")
    print("=" * 50)
    
    # Create game engine
    game = GameEngine()
    
    # Start new game or handle command line options
    if len(sys.argv) > 1:
        command = sys.argv[1].lower()
        if command == 'load':
            if game.load_game():
                print("Game loaded successfully!")
                game.run()
            else:
                print("Could not load saved game. Starting new game...")
                if game.start_game():
                    game.run()
        elif command == 'help' or command == '--help':
            print_help()
        else:
            print(f"Unknown command: {command}")
            print_help()
    else:
        # Start new game
        if game.start_game():
            game.run()
        else:
            print("Error: Could not start game. Check that data files exist.")
            sys.exit(1)

def print_help():
    """Print command line help."""
    help_text = """
Usage: python main.py [command]

Commands:
  (no command)  Start a new game
  load         Load a saved game
  help         Show this help message

Game Commands (during play):
  Type 'help' in-game for a full list of available commands.

Examples:
  python main.py          # Start new game
  python main.py load     # Load saved game
  python main.py help     # Show this help
"""
    print(help_text)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nGoodbye!")
        sys.exit(0)
    except Exception as e:
        print(f"\nAn error occurred: {e}")
        print("Please check that all required files are present and try again.")
        sys.exit(1)