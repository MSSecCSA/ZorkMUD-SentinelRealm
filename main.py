#!/usr/bin/env python3
"""
ZorkMUD: Sentinel Realm
A classic text-based adventure game in the spirit of Zork

Main entry point for the game.
"""

import sys
import os
from game_engine import GameEngine
from ansi_graphics import ANSIArt, ANSIColors, colorize_text

def main():
    """Main function to start the game."""
    # Enable ANSI colors
    ANSIArt.enable_ansi_on_windows()
    
    # Show retro BBS-style startup
    print(ANSIColors.CLEAR_SCREEN)
    startup_banner = f"""{ANSIColors.BRIGHT_GREEN}
    ████████████████████████████████████████████████████████████████████████████
    █                                                                          █
    █  {ANSIColors.BRIGHT_CYAN}███████╗ ██████╗ ██████╗ ██╗  ██╗    ███╗   ███╗██╗   ██╗██████╗ {ANSIColors.BRIGHT_GREEN}  █
    █  {ANSIColors.BRIGHT_CYAN}╚══███╔╝██╔═══██╗██╔══██╗██║ ██╔╝    ████╗ ████║██║   ██║██╔══██╗{ANSIColors.BRIGHT_GREEN}  █
    █    {ANSIColors.BRIGHT_CYAN}███╔╝ ██║   ██║██████╔╝█████╔╝     ██╔████╔██║██║   ██║██║  ██║{ANSIColors.BRIGHT_GREEN}  █
    █   {ANSIColors.BRIGHT_CYAN}███╔╝  ██║   ██║██╔══██╗██╔═██╗     ██║╚██╔╝██║██║   ██║██║  ██║{ANSIColors.BRIGHT_GREEN}  █
    █  {ANSIColors.BRIGHT_CYAN}███████╗╚██████╔╝██║  ██║██║  ██╗    ██║ ╚═╝ ██║╚██████╔╝██████╔╝{ANSIColors.BRIGHT_GREEN}  █
    █  {ANSIColors.BRIGHT_CYAN}╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝    ╚═╝     ╚═╝ ╚═════╝ ╚═════╝ {ANSIColors.BRIGHT_GREEN}  █
    █                                                                          █
    █               {ANSIColors.BRIGHT_YELLOW}SENTINEL REALM - BULLETIN BOARD SYSTEM{ANSIColors.BRIGHT_GREEN}                  █
    █                                                                          █
    ████████████████████████████████████████████████████████████████████████████{ANSIColors.RESET}
    """
    print(startup_banner)
    
    # Create game engine
    game = GameEngine()
    
    # Start new game or handle command line options
    if len(sys.argv) > 1:
        command = sys.argv[1].lower()
        if command == 'load':
            if game.load_game():
                print(colorize_text("Game loaded successfully!", ANSIColors.BRIGHT_GREEN))
                game.run()
            else:
                print(colorize_text("Could not load saved game. Starting new game...", ANSIColors.BRIGHT_YELLOW))
                if game.start_game():
                    game.run()
        elif command == 'help' or command == '--help':
            print_help()
        else:
            print(colorize_text(f"Unknown command: {command}", ANSIColors.BRIGHT_RED))
            print_help()
    else:
        # Start new game
        if game.start_game():
            game.run()
        else:
            print(colorize_text("Error: Could not start game. Check that data files exist.", ANSIColors.BRIGHT_RED))
            sys.exit(1)

def print_help():
    """Print command line help."""
    help_text = f"""
{colorize_text("ZorkMUD: Sentinel Realm - Command Line Help", ANSIColors.BRIGHT_CYAN)}

{colorize_text("Usage:", ANSIColors.BRIGHT_YELLOW)} python main.py [command]

{colorize_text("Commands:", ANSIColors.BRIGHT_GREEN)}
  {colorize_text("(no command)", ANSIColors.BRIGHT_WHITE)}  Start a new game
  {colorize_text("load", ANSIColors.BRIGHT_WHITE)}         Load a saved game
  {colorize_text("help", ANSIColors.BRIGHT_WHITE)}         Show this help message

{colorize_text("Game Commands (during play):", ANSIColors.BRIGHT_GREEN)}
  Type {colorize_text("'help'", ANSIColors.BRIGHT_MAGENTA)} in-game for a full list of available commands.

{colorize_text("Examples:", ANSIColors.BRIGHT_YELLOW)}
  {colorize_text("python main.py", ANSIColors.BRIGHT_WHITE)}          # Start new game
  {colorize_text("python main.py load", ANSIColors.BRIGHT_WHITE)}     # Load saved game
  {colorize_text("python main.py help", ANSIColors.BRIGHT_WHITE)}     # Show this help
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