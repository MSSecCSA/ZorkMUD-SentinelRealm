#!/usr/bin/env python3
"""
Quick test script to verify ANSI graphics are working correctly
"""

from ansi_graphics import ANSIArt, ANSIColors, colorize_text

def test_graphics():
    """Test all the major ANSI graphics components."""
    
    print(ANSIColors.CLEAR_SCREEN)
    print(colorize_text("🧪 TESTING CLEANED UP ANSI GRAPHICS", ANSIColors.BRIGHT_GREEN))
    print("=" * 60)
    print()
    
    # Test title card
    print("1. Title Card:")
    print(ANSIArt.title_card())
    input("Press ENTER to continue...")
    print(ANSIColors.CLEAR_SCREEN)
    
    # Test game logo  
    print("2. Game Logo:")
    print(ANSIArt.game_logo())
    input("Press ENTER to continue...")
    
    # Test room border
    print("3. Room Border:")
    print(ANSIArt.room_border("Test Room", "a test location"))
    print()
    
    # Test status bar
    print("4. Status Bar:")
    print(ANSIArt.status_bar(85, 42, 15, 3))
    print()
    
    # Test ASCII art
    print("5. ASCII House:")
    print(ANSIArt.ascii_house())
    input("Press ENTER to continue...")
    
    print("6. ASCII Cave:")
    print(ANSIArt.ascii_cave())
    input("Press ENTER to continue...")
    
    print("7. ASCII Treasure:")
    print(ANSIArt.ascii_treasure())
    input("Press ENTER to continue...")
    
    # Test dark room warning
    print("8. Dark Room Warning:")
    print(ANSIArt.dark_room_warning())
    input("Press ENTER to continue...")
    
    # Test footer
    print("9. BBS Footer:")
    print(ANSIArt.bbs_footer())
    print()
    
    # Test command prompt
    print("10. Command Prompt:")
    print(f"{ANSIArt.command_prompt()}look around")
    print(f"{ANSIArt.command_prompt()}take lamp")
    print(f"{ANSIArt.command_prompt()}north")
    print()
    
    print(colorize_text("✅ All ANSI graphics tests completed!", ANSIColors.BRIGHT_GREEN))
    print(colorize_text("Graphics should now be clean and properly formatted.", ANSIColors.BRIGHT_CYAN))

if __name__ == "__main__":
    ANSIArt.enable_ansi_on_windows()
    test_graphics()