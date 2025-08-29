"""
ANSI Graphics Module for ZorkMUD: Sentinel Realm
Provides classic BBS-style ANSI art and color formatting
"""

import os
import sys

class ANSIColors:
    """ANSI color codes for terminal formatting."""
    
    # Basic colors
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    
    # Bright colors
    BRIGHT_BLACK = '\033[90m'
    BRIGHT_RED = '\033[91m'
    BRIGHT_GREEN = '\033[92m'
    BRIGHT_YELLOW = '\033[93m'
    BRIGHT_BLUE = '\033[94m'
    BRIGHT_MAGENTA = '\033[95m'
    BRIGHT_CYAN = '\033[96m'
    BRIGHT_WHITE = '\033[97m'
    
    # Background colors
    BG_BLACK = '\033[40m'
    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'
    BG_YELLOW = '\033[43m'
    BG_BLUE = '\033[44m'
    BG_MAGENTA = '\033[45m'
    BG_CYAN = '\033[46m'
    BG_WHITE = '\033[47m'
    
    # Text formatting
    RESET = '\033[0m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    ITALIC = '\033[3m'
    UNDERLINE = '\033[4m'
    BLINK = '\033[5m'
    REVERSE = '\033[7m'
    STRIKETHROUGH = '\033[9m'
    
    # Special effects
    CLEAR_SCREEN = '\033[2J\033[H'
    CLEAR_LINE = '\033[2K'

class ANSIArt:
    """Collection of ANSI art for the game."""
    
    @staticmethod
    def enable_ansi_on_windows():
        """Enable ANSI support on Windows terminals."""
        if os.name == 'nt':
            try:
                import ctypes
                kernel32 = ctypes.windll.kernel32
                kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
            except:
                pass
    
    @staticmethod
    def game_logo():
        """Main game logo in classic BBS style."""
        logo = f"""{ANSIColors.BRIGHT_CYAN}
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║  {ANSIColors.BRIGHT_YELLOW}███████╗ ██████╗ ██████╗ ██╗  ██╗    ███╗   ███╗██╗   ██╗██████╗ {ANSIColors.BRIGHT_CYAN}  ║
║  {ANSIColors.BRIGHT_YELLOW}╚══███╔╝██╔═══██╗██╔══██╗██║ ██╔╝    ████╗ ████║██║   ██║██╔══██╗{ANSIColors.BRIGHT_CYAN}  ║
║    {ANSIColors.BRIGHT_YELLOW}███╔╝ ██║   ██║██████╔╝█████╔╝     ██╔████╔██║██║   ██║██║  ██║{ANSIColors.BRIGHT_CYAN}  ║
║   {ANSIColors.BRIGHT_YELLOW}███╔╝  ██║   ██║██╔══██╗██╔═██╗     ██║╚██╔╝██║██║   ██║██║  ██║{ANSIColors.BRIGHT_CYAN}  ║
║  {ANSIColors.BRIGHT_YELLOW}███████╗╚██████╔╝██║  ██║██║  ██╗    ██║ ╚═╝ ██║╚██████╔╝██████╔╝{ANSIColors.BRIGHT_CYAN}  ║
║  {ANSIColors.BRIGHT_YELLOW}╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝    ╚═╝     ╚═╝ ╚═════╝ ╚═════╝ {ANSIColors.BRIGHT_CYAN}  ║
║                                                                              ║
║            {ANSIColors.BRIGHT_MAGENTA}═══════════ SENTINEL REALM ═══════════{ANSIColors.BRIGHT_CYAN}                ║
║                                                                              ║
║  {ANSIColors.BRIGHT_GREEN}A Classic Text Adventure in the Spirit of the Great Underground Empire{ANSIColors.BRIGHT_CYAN} ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝{ANSIColors.RESET}
"""
        return logo
    
    @staticmethod
    def room_border(room_name, short_desc=""):
        """Create a bordered room header."""
        # Use fixed width for consistency
        width = 78
        
        border = f"""{ANSIColors.BRIGHT_BLUE}
┌{'─' * (width - 2)}┐
│ {ANSIColors.BRIGHT_WHITE}{ANSIColors.BOLD}{room_name.center(width - 4)}{ANSIColors.RESET}{ANSIColors.BRIGHT_BLUE} │"""
        
        if short_desc:
            border += f"""
│ {ANSIColors.CYAN}{short_desc.center(width - 4)}{ANSIColors.BRIGHT_BLUE} │"""
        
        border += f"""
└{'─' * (width - 2)}┘{ANSIColors.RESET}
"""
        return border
    
    @staticmethod
    def status_bar(health, score, moves, inventory_count):
        """Create a status bar."""
        status = f"""{ANSIColors.BRIGHT_BLUE}
┌─ STATUS ──────────────────────────────────────────────────────────────────────┐
│ {ANSIColors.BRIGHT_GREEN}Health: {health:3d}/100{ANSIColors.BRIGHT_BLUE} │ {ANSIColors.BRIGHT_YELLOW}Score: {score:4d}{ANSIColors.BRIGHT_BLUE} │ {ANSIColors.BRIGHT_CYAN}Moves: {moves:4d}{ANSIColors.BRIGHT_BLUE} │ {ANSIColors.BRIGHT_MAGENTA}Items: {inventory_count:2d}{ANSIColors.BRIGHT_BLUE} │
└───────────────────────────────────────────────────────────────────────────────┘{ANSIColors.RESET}
"""
        return status
    
    @staticmethod
    def command_prompt():
        """Stylized command prompt."""
        return f"{ANSIColors.BRIGHT_GREEN}>{ANSIColors.BRIGHT_WHITE} "
    
    @staticmethod
    def title_card():
        """Classic BBS-style title card."""
        card = f"""{ANSIColors.CLEAR_SCREEN}
{ANSIColors.BRIGHT_CYAN}
 ████████████████████████████████████████████████████████████████████████████████
 █                                                                              █
 █  {ANSIColors.BRIGHT_YELLOW}██████╗ ██████╗ ███████╗    ████████╗██╗███╗   ███╗███████╗{ANSIColors.BRIGHT_CYAN}          █
 █  {ANSIColors.BRIGHT_YELLOW}██╔══██╗██╔══██╗██╔════╝    ╚══██╔══╝██║████╗ ████║██╔════╝{ANSIColors.BRIGHT_CYAN}          █
 █  {ANSIColors.BRIGHT_YELLOW}██████╔╝██████╔╝███████╗       ██║   ██║██╔████╔██║█████╗  {ANSIColors.BRIGHT_CYAN}          █
 █  {ANSIColors.BRIGHT_YELLOW}██╔══██╗██╔══██╗╚════██║       ██║   ██║██║╚██╔╝██║██╔══╝  {ANSIColors.BRIGHT_CYAN}          █
 █  {ANSIColors.BRIGHT_YELLOW}██████╔╝██████╔╝███████║       ██║   ██║██║ ╚═╝ ██║███████╗{ANSIColors.BRIGHT_CYAN}          █
 █  {ANSIColors.BRIGHT_YELLOW}╚═════╝ ╚═════╝ ╚══════╝       ╚═╝   ╚═╝╚═╝     ╚═╝╚══════╝{ANSIColors.BRIGHT_CYAN}          █
 █                                                                              █
 █              {ANSIColors.BRIGHT_RED}║{ANSIColors.BRIGHT_MAGENTA} BULLETIN BOARD SYSTEM {ANSIColors.BRIGHT_RED}║{ANSIColors.BRIGHT_CYAN}                       █
 █              {ANSIColors.BRIGHT_RED}║{ANSIColors.BRIGHT_WHITE} Est. 1980 - Running Strong {ANSIColors.BRIGHT_RED}║{ANSIColors.BRIGHT_CYAN}                      █
 █                                                                              █
 █        {ANSIColors.BRIGHT_GREEN}Welcome to the Underground Empire, Adventurer!{ANSIColors.BRIGHT_CYAN}                  █
 █        {ANSIColors.WHITE}Your quest awaits in the mysterious Sentinel Realm...{ANSIColors.BRIGHT_CYAN}            █
 █                                                                              █
 ████████████████████████████████████████████████████████████████████████████████

        {ANSIColors.BRIGHT_YELLOW}[{ANSIColors.BRIGHT_WHITE}PRESS ENTER TO CONTINUE{ANSIColors.BRIGHT_YELLOW}]{ANSIColors.RESET}
"""
        return card
    
    @staticmethod
    def ascii_house():
        """ASCII art of the white house."""
        house = f"""{ANSIColors.BRIGHT_WHITE}
                    {ANSIColors.YELLOW}.-""""""-.{ANSIColors.BRIGHT_WHITE}
                   {ANSIColors.YELLOW}/          \\{ANSIColors.BRIGHT_WHITE}
                  {ANSIColors.YELLOW}/_            _\\{ANSIColors.BRIGHT_WHITE}
                 {ANSIColors.YELLOW}// \\          / \\\\{ANSIColors.BRIGHT_WHITE}
                 {ANSIColors.YELLOW}|\\_/|        |\\_/|{ANSIColors.BRIGHT_WHITE}
                 {ANSIColors.YELLOW}|   |        |   |{ANSIColors.BRIGHT_WHITE}
                 {ANSIColors.YELLOW}|___|________|___|{ANSIColors.BRIGHT_WHITE}
                   {ANSIColors.YELLOW}|  _        _  |{ANSIColors.BRIGHT_WHITE}
                   {ANSIColors.YELLOW}| |X|      |X| |{ANSIColors.BRIGHT_WHITE}
                   {ANSIColors.YELLOW}|_|_|______|_|_|{ANSIColors.BRIGHT_WHITE}
                   {ANSIColors.YELLOW}[________________]{ANSIColors.BRIGHT_WHITE}

        {ANSIColors.BRIGHT_BLUE}The mysterious white house stands before you...{ANSIColors.RESET}
"""
        return house
    
    @staticmethod
    def ascii_cave():
        """ASCII art of the underground cave."""
        cave = f"""{ANSIColors.BRIGHT_BLACK}
            {ANSIColors.YELLOW}∩{ANSIColors.BRIGHT_BLACK}     {ANSIColors.YELLOW}∩∩∩{ANSIColors.BRIGHT_BLACK}        {ANSIColors.YELLOW}∩{ANSIColors.BRIGHT_BLACK}
          {ANSIColors.YELLOW}∩∩∩{ANSIColors.BRIGHT_BLACK}   {ANSIColors.YELLOW}∩∩∩∩∩{ANSIColors.BRIGHT_BLACK}      {ANSIColors.YELLOW}∩∩∩{ANSIColors.BRIGHT_BLACK}
         {ANSIColors.YELLOW}∩∩∩∩∩{ANSIColors.BRIGHT_BLACK} {ANSIColors.YELLOW}∩∩∩∩∩∩∩{ANSIColors.BRIGHT_BLACK}    {ANSIColors.YELLOW}∩∩∩∩∩{ANSIColors.BRIGHT_BLACK}
        {ANSIColors.BRIGHT_MAGENTA}≋≋≋≋≋≋≋≋≋≋≋≋≋≋≋≋≋≋≋≋≋≋≋≋≋≋≋{ANSIColors.BRIGHT_BLACK}
        {ANSIColors.BRIGHT_MAGENTA}≋{ANSIColors.GREEN} ◊ {ANSIColors.BRIGHT_MAGENTA}≋{ANSIColors.GREEN} ♦ {ANSIColors.BRIGHT_MAGENTA}≋{ANSIColors.GREEN} ◊ {ANSIColors.BRIGHT_MAGENTA}≋{ANSIColors.GREEN} ♦ {ANSIColors.BRIGHT_MAGENTA}≋{ANSIColors.GREEN} ◊ {ANSIColors.BRIGHT_MAGENTA}≋{ANSIColors.GREEN} ♦ {ANSIColors.BRIGHT_MAGENTA}≋{ANSIColors.GREEN} ◊ {ANSIColors.BRIGHT_MAGENTA}≋{ANSIColors.BRIGHT_BLACK}
        {ANSIColors.BRIGHT_MAGENTA}≋≋≋≋≋≋≋≋≋≋≋≋≋≋≋≋≋≋≋≋≋≋≋≋≋≋≋{ANSIColors.BRIGHT_BLACK}

        {ANSIColors.BRIGHT_CYAN}Ancient symbols glow on the cave walls...{ANSIColors.RESET}
"""
        return cave
    
    @staticmethod
    def ascii_treasure():
        """ASCII art of the treasure chest."""
        treasure = f"""{ANSIColors.YELLOW}
                   .-""""""-.
                  /  {ANSIColors.BRIGHT_YELLOW}______{ANSIColors.YELLOW}  \\
                 |  {ANSIColors.BRIGHT_YELLOW}/      \\{ANSIColors.YELLOW}  |
                 | {ANSIColors.BRIGHT_YELLOW}|  $$$$ |{ANSIColors.YELLOW}  |
                 | {ANSIColors.BRIGHT_YELLOW}|  $$$$ |{ANSIColors.YELLOW}  |
                 | {ANSIColors.BRIGHT_YELLOW}| $$$$$ |{ANSIColors.YELLOW}  |
                 | {ANSIColors.BRIGHT_YELLOW}\\______/{ANSIColors.YELLOW}  |
                  \\__________/
                  [__________]

        {ANSIColors.BRIGHT_YELLOW}The magnificent treasure chest gleams!{ANSIColors.RESET}
"""
        return treasure
    
    @staticmethod
    def victory_banner():
        """Victory celebration banner."""
        banner = f"""{ANSIColors.BRIGHT_YELLOW}{ANSIColors.BLINK}
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║   {ANSIColors.BRIGHT_RED}██╗   ██╗██╗ ██████╗████████╗ ██████╗ ██████╗ ██╗   ██╗██╗{ANSIColors.BRIGHT_YELLOW}   ║
║   {ANSIColors.BRIGHT_RED}██║   ██║██║██╔════╝╚══██╔══╝██╔═══██╗██╔══██╗╚██╗ ██╔╝██║{ANSIColors.BRIGHT_YELLOW}   ║
║   {ANSIColors.BRIGHT_RED}██║   ██║██║██║        ██║   ██║   ██║██████╔╝ ╚████╔╝ ██║{ANSIColors.BRIGHT_YELLOW}   ║
║   {ANSIColors.BRIGHT_RED}╚██╗ ██╔╝██║██║        ██║   ██║   ██║██╔══██╗  ╚██╔╝  ╚═╝{ANSIColors.BRIGHT_YELLOW}   ║
║    {ANSIColors.BRIGHT_RED}╚████╔╝ ██║╚██████╗   ██║   ╚██████╔╝██║  ██║   ██║   ██╗{ANSIColors.BRIGHT_YELLOW}   ║
║     {ANSIColors.BRIGHT_RED}╚═══╝  ╚═╝ ╚═════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝{ANSIColors.BRIGHT_YELLOW}   ║
║                                                                              ║
║            {ANSIColors.BRIGHT_GREEN}*** CONGRATULATIONS, BRAVE ADVENTURER! ***{ANSIColors.BRIGHT_YELLOW}              ║
║                                                                              ║
║              {ANSIColors.BRIGHT_WHITE}You have conquered the Sentinel Realm!{ANSIColors.BRIGHT_YELLOW}                  ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝{ANSIColors.RESET}
"""
        return banner
    
    @staticmethod
    def lamp_glow():
        """Animated lamp glow effect."""
        return f"{ANSIColors.BRIGHT_YELLOW}✦{ANSIColors.YELLOW}◈{ANSIColors.BRIGHT_YELLOW}✦{ANSIColors.RESET}"
    
    @staticmethod
    def dark_room_warning():
        """Scary dark room warning."""
        warning = f"""{ANSIColors.BRIGHT_RED}
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║     {ANSIColors.BRIGHT_RED}▄▄▄▄▄  ██▀▀▀██  ██▀▀██▀▀██  ███▀▀▀  ██    ██ ███▀▀▀▀ ███▀▀▀    {ANSIColors.BRIGHT_RED}║
║    {ANSIColors.BRIGHT_RED}██   ██ ██   ██  ██  ██  ██  ██      ██    ██ ██      ██        {ANSIColors.BRIGHT_RED}║
║    {ANSIColors.BRIGHT_RED}██   ██ ██▄▄▄██  ██  ██  ██  ██▄▄▄   ██▄▄▄▄██ ██▄▄▄   ██▄▄▄     {ANSIColors.BRIGHT_RED}║
║    {ANSIColors.BRIGHT_RED}██   ██ ██▀▀▀██  ██  ██  ██  ██▀▀▀   ██▀▀▀▀██ ██▀▀▀   ██▀▀▀     {ANSIColors.BRIGHT_RED}║
║     {ANSIColors.BRIGHT_RED}▀▀▀▀▀  ██   ██  ▀▀  ▀▀  ▀▀  ▀▀▀▀▀▀▀ ▀▀    ▀▀ ▀▀▀▀▀▀▀ ▀▀▀▀▀     {ANSIColors.BRIGHT_RED}║
║                                                                              ║
║               {ANSIColors.BRIGHT_WHITE}It is pitch black. You are likely to be               {ANSIColors.BRIGHT_RED}║
║                         {ANSIColors.BRIGHT_WHITE}eaten by a grue.                           {ANSIColors.BRIGHT_RED}║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝{ANSIColors.RESET}
"""
        return warning
    
    @staticmethod
    def bbs_footer():
        """Classic BBS-style footer."""
        footer = f"""{ANSIColors.BRIGHT_BLUE}
┌──────────────────────────────────────────────────────────────────────────────┐
│ {ANSIColors.BRIGHT_WHITE}░▒▓█ SENTINEL REALM BBS █▓▒░  │  Type 'help' for commands  │  'quit' to exit{ANSIColors.BRIGHT_BLUE} │
└──────────────────────────────────────────────────────────────────────────────┘{ANSIColors.RESET}
"""
        return footer

def colorize_text(text, color):
    """Add color to text and reset afterwards."""
    return f"{color}{text}{ANSIColors.RESET}"

def center_text(text, width=80):
    """Center text within specified width."""
    return text.center(width)

def box_text(text, color=ANSIColors.BRIGHT_CYAN):
    """Put text in a box."""
    lines = text.split('\n')
    max_width = max(len(line) for line in lines)
    
    box = f"{color}┌{'─' * (max_width + 2)}┐\n"
    for line in lines:
        box += f"│ {line.ljust(max_width)} │\n"
    box += f"└{'─' * (max_width + 2)}┘{ANSIColors.RESET}"
    
    return box

# Enable ANSI support when module is imported
ANSIArt.enable_ansi_on_windows()