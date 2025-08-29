#!/usr/bin/env python3
"""
ANSI Graphics Demo for ZorkMUD: Sentinel Realm
Showcases all the BBS-style graphics and effects
"""

import time
import sys
from ansi_graphics import ANSIArt, ANSIColors, colorize_text, box_text

def demo_pause(seconds=2):
    """Pause for demonstration."""
    time.sleep(seconds)

def clear_and_continue():
    """Clear screen and wait for user input."""
    input(f"\n{colorize_text('[Press ENTER to continue...]', ANSIColors.BRIGHT_YELLOW)}")
    print(ANSIColors.CLEAR_SCREEN)

def main():
    """Run the ANSI graphics demonstration."""
    
    # Enable ANSI support
    ANSIArt.enable_ansi_on_windows()
    
    print(ANSIColors.CLEAR_SCREEN)
    print(colorize_text("=" * 80, ANSIColors.BRIGHT_CYAN))
    print(colorize_text("ZORKMUD: SENTINEL REALM - ANSI GRAPHICS DEMO", ANSIColors.BRIGHT_WHITE).center(80))
    print(colorize_text("=" * 80, ANSIColors.BRIGHT_CYAN))
    print()
    
    demo_features = [
        ("BBS Title Card", lambda: print(ANSIArt.title_card())),
        ("Main Game Logo", lambda: print(ANSIArt.game_logo())),
        ("Room Border Example", lambda: print(ANSIArt.room_border("Kitchen", "a dusty old kitchen"))),
        ("ASCII House Art", lambda: print(ANSIArt.ascii_house())),
        ("ASCII Cave Art", lambda: print(ANSIArt.ascii_cave())),
        ("ASCII Treasure Art", lambda: print(ANSIArt.ascii_treasure())),
        ("Dark Room Warning", lambda: print(ANSIArt.dark_room_warning())),
        ("Victory Banner", lambda: print(ANSIArt.victory_banner())),
        ("Status Bar", lambda: print(ANSIArt.status_bar(85, 45, 127, 3))),
        ("Color Palette", demonstrate_colors),
        ("Text Effects", demonstrate_text_effects),
        ("BBS Footer", lambda: print(ANSIArt.bbs_footer())),
    ]
    
    for name, demo_func in demo_features:
        print(colorize_text(f"🎨 DEMONSTRATING: {name}", ANSIColors.BRIGHT_GREEN))
        print(colorize_text("-" * 60, ANSIColors.BRIGHT_BLUE))
        print()
        
        demo_func()
        
        clear_and_continue()
    
    # Final showcase - simulated game session
    print(colorize_text("🎮 SIMULATED GAME SESSION", ANSIColors.BRIGHT_GREEN))
    print(colorize_text("-" * 60, ANSIColors.BRIGHT_BLUE))
    print()
    
    simulate_game_session()
    
    print()
    print(colorize_text("=" * 80, ANSIColors.BRIGHT_CYAN))
    print(colorize_text("DEMO COMPLETE!", ANSIColors.BRIGHT_WHITE).center(80))
    print(colorize_text("The game now has full BBS-style ANSI graphics!", ANSIColors.BRIGHT_GREEN).center(80))
    print(colorize_text("=" * 80, ANSIColors.BRIGHT_CYAN))

def demonstrate_colors():
    """Show all available colors."""
    colors = [
        ("Basic Colors", [
            ("Black", ANSIColors.BLACK),
            ("Red", ANSIColors.RED),
            ("Green", ANSIColors.GREEN),
            ("Yellow", ANSIColors.YELLOW),
            ("Blue", ANSIColors.BLUE),
            ("Magenta", ANSIColors.MAGENTA),
            ("Cyan", ANSIColors.CYAN),
            ("White", ANSIColors.WHITE),
        ]),
        ("Bright Colors", [
            ("Bright Black", ANSIColors.BRIGHT_BLACK),
            ("Bright Red", ANSIColors.BRIGHT_RED),
            ("Bright Green", ANSIColors.BRIGHT_GREEN),
            ("Bright Yellow", ANSIColors.BRIGHT_YELLOW),
            ("Bright Blue", ANSIColors.BRIGHT_BLUE),
            ("Bright Magenta", ANSIColors.BRIGHT_MAGENTA),
            ("Bright Cyan", ANSIColors.BRIGHT_CYAN),
            ("Bright White", ANSIColors.BRIGHT_WHITE),
        ])
    ]
    
    for category, color_list in colors:
        print(colorize_text(f"{category}:", ANSIColors.BRIGHT_WHITE))
        for name, color_code in color_list:
            print(f"  {colorize_text('●', color_code)} {colorize_text(name, color_code)}")
        print()

def demonstrate_text_effects():
    """Show text formatting effects."""
    effects = [
        ("Bold", ANSIColors.BOLD),
        ("Dim", ANSIColors.DIM),
        ("Italic", ANSIColors.ITALIC),
        ("Underline", ANSIColors.UNDERLINE),
        ("Reverse", ANSIColors.REVERSE),
    ]
    
    for name, effect in effects:
        print(f"{effect}This text demonstrates {name} formatting{ANSIColors.RESET}")
    
    print()
    print("Box text example:")
    print(box_text("This text is in a box!\nWith multiple lines!"))

def simulate_game_session():
    """Simulate a brief game session with all graphics."""
    # Title screen
    print(ANSIArt.title_card())
    demo_pause(1)
    input()
    print(ANSIColors.CLEAR_SCREEN)
    
    # Game logo
    print(ANSIArt.game_logo())
    demo_pause(1)
    
    # Welcome message
    print(colorize_text("Welcome to ZorkMUD: Sentinel Realm!", ANSIColors.BRIGHT_GREEN))
    print("A classic text adventure in the spirit of Zork")
    print()
    demo_pause(1)
    
    # Room description
    print(ANSIArt.room_border("Open Field", "an open field"))
    print(colorize_text("You are standing in an open field west of a white house...", ANSIColors.BRIGHT_WHITE))
    print()
    print(colorize_text("You can see:", ANSIColors.BRIGHT_CYAN))
    print(f"  {colorize_text('mailbox', ANSIColors.BRIGHT_GREEN)}")
    print()
    print(f"Exits: {colorize_text('north', ANSIColors.BRIGHT_MAGENTA)}, {colorize_text('east', ANSIColors.BRIGHT_MAGENTA)}, {colorize_text('south', ANSIColors.BRIGHT_MAGENTA)}")
    print()
    print(ANSIArt.status_bar(100, 0, 1, 0))
    demo_pause(2)
    
    # Command prompt
    print(f"{ANSIArt.command_prompt()}examine mailbox")
    demo_pause(1)
    print(colorize_text("It's a small mailbox, typical of those found in front of houses.", ANSIColors.BRIGHT_WHITE))
    print()
    
    # Taking an item with score
    print(f"{ANSIArt.command_prompt()}open mailbox")
    demo_pause(1)
    print(colorize_text("You open the mailbox.", ANSIColors.BRIGHT_GREEN))
    print(colorize_text("[+5 points] Total Score: 5", ANSIColors.BRIGHT_YELLOW))
    print()
    
    # Moving to another room
    print(f"{ANSIArt.command_prompt()}east")
    demo_pause(1)
    print(ANSIArt.room_border("White House", "the white house"))
    print(ANSIArt.ascii_house())
    demo_pause(2)
    
    # Using lamp in dark room
    print(f"{ANSIArt.command_prompt()}north")
    print(f"{ANSIArt.command_prompt()}east")  
    print(f"{ANSIArt.command_prompt()}take lamp")
    print(f"{ANSIArt.command_prompt()}east")
    demo_pause(1)
    print(ANSIArt.dark_room_warning())
    demo_pause(2)
    
    print(f"{ANSIArt.command_prompt()}use lamp")
    demo_pause(1)
    print(f"{ANSIArt.lamp_glow()} {colorize_text('The lamp is now on, providing a warm glow.', ANSIColors.BRIGHT_YELLOW)}")
    print()
    print(ANSIArt.room_border("Dark Hallway", "a dark hallway"))
    print(colorize_text("You are in a dark hallway. Your lamp illuminates the darkness.", ANSIColors.BRIGHT_WHITE))
    demo_pause(2)
    
    # Final treasure room
    print(f"{ANSIArt.command_prompt()}east")
    demo_pause(1)
    print(ANSIArt.room_border("Living Room", "a dusty living room"))
    print(ANSIArt.ascii_treasure())
    demo_pause(2)
    
    # Victory
    print(f"{ANSIArt.command_prompt()}take golden treasure")
    demo_pause(1)
    print(ANSIArt.victory_banner())
    demo_pause(2)
    
    print(ANSIArt.bbs_footer())

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{colorize_text('Demo interrupted!', ANSIColors.BRIGHT_RED)}")
        sys.exit(0)