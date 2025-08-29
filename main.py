#!/usr/bin/env python3
"""
ZorkMUD: Sentinel Realm
A classic text-based adventure game in the spirit of Zork

Main entry point for the game.
"""

import sys
import os
import subprocess
from game_engine import GameEngine
from ansi_graphics import ANSIArt, ANSIColors, colorize_text

def main():
    """Main function to start the game."""
    # Enable ANSI colors
    ANSIArt.enable_ansi_on_windows()
    
    # Show retro BBS-style startup
    print(ANSIColors.CLEAR_SCREEN)
    startup_banner = f"""{ANSIColors.BRIGHT_CYAN}
 ████████████████████████████████████████████████████████████████████████████████
 █                                                                              █
 █  {ANSIColors.BRIGHT_YELLOW}███████╗ ██████╗ ██████╗ ██╗  ██╗    ███╗   ███╗██╗   ██╗██████╗ {ANSIColors.BRIGHT_CYAN}  █
 █  {ANSIColors.BRIGHT_YELLOW}╚══███╔╝██╔═══██╗██╔══██╗██║ ██╔╝    ████╗ ████║██║   ██║██╔══██╗{ANSIColors.BRIGHT_CYAN}  █
 █    {ANSIColors.BRIGHT_YELLOW}███╔╝ ██║   ██║██████╔╝█████╔╝     ██╔████╔██║██║   ██║██║  ██║{ANSIColors.BRIGHT_CYAN}  █
 █   {ANSIColors.BRIGHT_YELLOW}███╔╝  ██║   ██║██╔══██╗██╔═██╗     ██║╚██╔╝██║██║   ██║██║  ██║{ANSIColors.BRIGHT_CYAN}  █
 █  {ANSIColors.BRIGHT_YELLOW}███████╗╚██████╔╝██║  ██║██║  ██╗    ██║ ╚═╝ ██║╚██████╔╝██████╔╝{ANSIColors.BRIGHT_CYAN}  █
 █  {ANSIColors.BRIGHT_YELLOW}╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝    ╚═╝     ╚═╝ ╚═════╝ ╚═════╝ {ANSIColors.BRIGHT_CYAN}  █
 █                                                                              █
 █               {ANSIColors.BRIGHT_MAGENTA}SENTINEL REALM - BULLETIN BOARD SYSTEM{ANSIColors.BRIGHT_CYAN}                  █
 █                                                                              █
 ████████████████████████████████████████████████████████████████████████████████{ANSIColors.RESET}
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
        elif command == 'sync' or command == 'update':
            sync_with_repository()
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

def sync_with_repository():
    """Sync with the GitHub repository to get the latest updates."""
    print(ANSIColors.CLEAR_SCREEN)
    print(colorize_text("🔄 ZORKMUD: SENTINEL REALM - REPOSITORY SYNC", ANSIColors.BRIGHT_CYAN))
    print(colorize_text("=" * 60, ANSIColors.BRIGHT_BLUE))
    print()
    
    # Check if we're in a git repository
    if not os.path.exists('.git'):
        print(colorize_text("❌ Error: Not in a git repository!", ANSIColors.BRIGHT_RED))
        print(colorize_text("This command only works if you cloned the repository with git.", ANSIColors.BRIGHT_YELLOW))
        print()
        print(colorize_text("Manual update instructions:", ANSIColors.BRIGHT_WHITE))
        print_manual_update_instructions()
        return
    
    try:
        print(colorize_text("📡 Checking for updates from GitHub...", ANSIColors.BRIGHT_YELLOW))
        
        # Fetch latest changes
        result = subprocess.run(['git', 'fetch', 'origin'], 
                              capture_output=True, text=True, check=True)
        
        # Check if there are updates
        result = subprocess.run(['git', 'rev-list', 'HEAD..origin/main', '--count'], 
                              capture_output=True, text=True, check=True)
        
        update_count = int(result.stdout.strip())
        
        if update_count == 0:
            print(colorize_text("✅ You already have the latest version!", ANSIColors.BRIGHT_GREEN))
            print(colorize_text(f"Repository is up to date.", ANSIColors.BRIGHT_WHITE))
        else:
            print(colorize_text(f"📥 Found {update_count} update(s) available!", ANSIColors.BRIGHT_YELLOW))
            
            # Show what will be updated
            result = subprocess.run(['git', 'log', '--oneline', 'HEAD..origin/main'], 
                                  capture_output=True, text=True, check=True)
            
            if result.stdout.strip():
                print(colorize_text("\nRecent changes:", ANSIColors.BRIGHT_CYAN))
                for line in result.stdout.strip().split('\n')[:5]:  # Show last 5 commits
                    print(f"  • {colorize_text(line, ANSIColors.BRIGHT_WHITE)}")
                
                if update_count > 5:
                    print(f"  {colorize_text('... and more', ANSIColors.DIM)}")
            
            print()
            response = input(colorize_text("Do you want to download the updates? (y/N): ", ANSIColors.BRIGHT_YELLOW))
            
            if response.lower() in ['y', 'yes']:
                print(colorize_text("⬇️  Downloading updates...", ANSIColors.BRIGHT_BLUE))
                
                # Pull the latest changes
                result = subprocess.run(['git', 'pull', 'origin', 'main'], 
                                      capture_output=True, text=True, check=True)
                
                print(colorize_text("✅ Successfully updated!", ANSIColors.BRIGHT_GREEN))
                print(colorize_text("Repository is now up to date with the latest changes.", ANSIColors.BRIGHT_WHITE))
                
                # Show what was updated
                if result.stdout.strip():
                    print(colorize_text("\nUpdate details:", ANSIColors.BRIGHT_CYAN))
                    print(colorize_text(result.stdout.strip(), ANSIColors.BRIGHT_WHITE))
            else:
                print(colorize_text("❌ Update cancelled.", ANSIColors.BRIGHT_YELLOW))
                print(colorize_text("You can run 'python main.py sync' again later to update.", ANSIColors.BRIGHT_WHITE))
    
    except subprocess.CalledProcessError as e:
        print(colorize_text("❌ Error during git operation:", ANSIColors.BRIGHT_RED))
        print(colorize_text(f"   {e.stderr if e.stderr else str(e)}", ANSIColors.BRIGHT_WHITE))
        print()
        print(colorize_text("Try the manual update method:", ANSIColors.BRIGHT_YELLOW))
        print_manual_update_instructions()
    
    except FileNotFoundError:
        print(colorize_text("❌ Error: Git is not installed or not in PATH!", ANSIColors.BRIGHT_RED))
        print(colorize_text("Please install Git first, then try again.", ANSIColors.BRIGHT_YELLOW))
        print()
        print(colorize_text("Manual update instructions:", ANSIColors.BRIGHT_WHITE))
        print_manual_update_instructions()

def print_manual_update_instructions():
    """Print manual update instructions."""
    print()
    instructions = f"""
{colorize_text("🔧 Manual Update Instructions:", ANSIColors.BRIGHT_CYAN)}

{colorize_text("Since you cloned to C:\\Stuff\\VSCode\\ZorkMUD-SentinelRealm:", ANSIColors.BRIGHT_WHITE)}

{colorize_text("1. Open PowerShell/Command Prompt", ANSIColors.BRIGHT_GREEN)}
{colorize_text("2. Navigate to your repository:", ANSIColors.BRIGHT_GREEN)}
   {colorize_text("cd C:\\Stuff\\VSCode\\ZorkMUD-SentinelRealm", ANSIColors.BRIGHT_YELLOW)}

{colorize_text("3. Pull the latest changes:", ANSIColors.BRIGHT_GREEN)}
   {colorize_text("git pull origin main", ANSIColors.BRIGHT_YELLOW)}

{colorize_text("Alternative - Full refresh:", ANSIColors.BRIGHT_GREEN)}
   {colorize_text("git fetch origin", ANSIColors.BRIGHT_YELLOW)}
   {colorize_text("git reset --hard origin/main", ANSIColors.BRIGHT_YELLOW)}

{colorize_text("4. Verify the update:", ANSIColors.BRIGHT_GREEN)}
   {colorize_text("git log --oneline -5", ANSIColors.BRIGHT_YELLOW)}
"""
    print(instructions)

def print_help():
    """Print command line help."""
    help_text = f"""
{colorize_text("ZorkMUD: Sentinel Realm - Command Line Help", ANSIColors.BRIGHT_CYAN)}

{colorize_text("Usage:", ANSIColors.BRIGHT_YELLOW)} python main.py [command]

{colorize_text("Commands:", ANSIColors.BRIGHT_GREEN)}
  {colorize_text("(no command)", ANSIColors.BRIGHT_WHITE)}  Start a new game
  {colorize_text("load", ANSIColors.BRIGHT_WHITE)}         Load a saved game
  {colorize_text("sync", ANSIColors.BRIGHT_WHITE)}         Sync with GitHub repository (download updates)
  {colorize_text("update", ANSIColors.BRIGHT_WHITE)}       Same as sync
  {colorize_text("help", ANSIColors.BRIGHT_WHITE)}         Show this help message

{colorize_text("Game Commands (during play):", ANSIColors.BRIGHT_GREEN)}
  Type {colorize_text("'help'", ANSIColors.BRIGHT_MAGENTA)} in-game for a full list of available commands.

{colorize_text("Examples:", ANSIColors.BRIGHT_YELLOW)}
  {colorize_text("python main.py", ANSIColors.BRIGHT_WHITE)}          # Start new game
  {colorize_text("python main.py load", ANSIColors.BRIGHT_WHITE)}     # Load saved game
  {colorize_text("python main.py sync", ANSIColors.BRIGHT_WHITE)}     # Check for and download updates
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