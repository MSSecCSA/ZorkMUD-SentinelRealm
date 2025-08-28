"""
Command parser for the ZorkMUD game engine.
Handles natural language input and command interpretation.
"""

import re

class Parser:
    """Handles command parsing and interpretation."""
    
    def __init__(self):
        """Initialize the parser with command mappings."""
        self.commands = {
            # Movement commands
            'movement': {
                'patterns': [
                    r'^(go\s+)?(north|n)$',
                    r'^(go\s+)?(south|s)$', 
                    r'^(go\s+)?(east|e)$',
                    r'^(go\s+)?(west|w)$',
                    r'^(go\s+)?(up|u)$',
                    r'^(go\s+)?(down|d)$',
                ],
                'directions': {
                    'north': 'north', 'n': 'north',
                    'south': 'south', 's': 'south',
                    'east': 'east', 'e': 'east',
                    'west': 'west', 'w': 'west',
                    'up': 'up', 'u': 'up',
                    'down': 'down', 'd': 'down'
                }
            },
            
            # Observation commands
            'look': [r'^(look|l)$', r'^look\s+around$', r'^examine\s+room$'],
            'examine': [r'^(examine|x)\s+(.+)$', r'^look\s+at\s+(.+)$', r'^inspect\s+(.+)$'],
            
            # Inventory commands  
            'inventory': [r'^(inventory|i)$', r'^inv$'],
            'take': [r'^(take|get)\s+(.+)$', r'^pick\s+up\s+(.+)$'],
            'drop': [r'^drop\s+(.+)$', r'^put\s+down\s+(.+)$'],
            
            # Interaction commands
            'use': [r'^use\s+(.+)$'],
            'open': [r'^open\s+(.+)$'],
            'read': [r'^read\s+(.+)$'],
            
            # System commands
            'help': [r'^help$', r'^\?$', r'^commands$'],
            'quit': [r'^(quit|exit|q)$', r'^bye$'],
            'save': [r'^save$', r'^save\s+game$'],
            'load': [r'^load$', r'^load\s+game$', r'^restore$'],
            'score': [r'^score$'],
            'health': [r'^health$', r'^hp$'],
            'status': [r'^status$', r'^stat$'],
        }
    
    def parse(self, input_text):
        """
        Parse user input and return command and arguments.
        
        Args:
            input_text (str): Raw user input
            
        Returns:
            tuple: (command, arguments)
        """
        if not input_text:
            return None, None
        
        input_text = input_text.strip().lower()
        
        # Handle movement commands specially
        for pattern in self.commands['movement']['patterns']:
            match = re.match(pattern, input_text)
            if match:
                direction_word = match.group(2)  # The direction part
                direction = self.commands['movement']['directions'].get(direction_word)
                return 'move', direction
        
        # Handle other commands
        for command, patterns in self.commands.items():
            if command == 'movement':
                continue  # Already handled above
                
            for pattern in patterns:
                match = re.match(pattern, input_text)
                if match:
                    if len(match.groups()) > 0:
                        # Command with arguments
                        args = match.groups()[-1]  # Get the last group (the object)
                        return command, args
                    else:
                        # Command without arguments
                        return command, None
        
        # No command matched
        return 'unknown', input_text
    
    def get_help_text(self):
        """Return help text showing available commands."""
        help_text = """
Available Commands:

MOVEMENT:
  north, south, east, west (or n, s, e, w)
  go <direction>

OBSERVATION:
  look (or l) - Look around the current room
  examine <object> (or x <object>) - Examine an object closely

INVENTORY:
  inventory (or i) - Show what you're carrying
  take <object> (or get <object>) - Pick up an object
  drop <object> - Drop an object

INTERACTION:
  use <object> - Use an object
  open <object> - Open a container
  read <object> - Read text on an object

SYSTEM:
  help (or ?) - Show this help
  score - Show your current score
  health - Show your health status
  quit (or q) - Exit the game
  save - Save your game
  load - Load a saved game

Examples:
  > north
  > take lamp
  > examine mailbox
  > open door
  > use key
"""
        return help_text.strip()
    
    def normalize_object_name(self, name):
        """Normalize object names for comparison."""
        if not name:
            return ""
        return name.strip().lower().replace("the ", "").replace("a ", "").replace("an ", "")