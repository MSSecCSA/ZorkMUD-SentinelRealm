"""
Main game engine for ZorkMUD: Sentinel Realm
Handles game state, command processing, and core game logic.
"""

import json
import pickle
import os
from player import Player
from room import Room
from item import Item
from parser import Parser
from ansi_graphics import ANSIArt, ANSIColors, colorize_text, box_text

class GameEngine:
    """Main game engine that manages the game state and processes commands."""
    
    def __init__(self):
        """Initialize the game engine."""
        self.player = None
        self.rooms = {}
        self.items = {}
        self.messages = {}
        self.parser = Parser()
        self.running = False
        self.lamp_on = False
        self.game_won = False
        
        # Score values for different actions
        self.score_values = {
            'take_leaflet': 5,
            'open_mailbox': 5,
            'take_lamp': 10,
            'take_key': 15,
            'read_scroll': 10,
            'open_chest': 20,
            'take_treasure': 50
        }
        
        self.scored_actions = set()  # Track which actions have been scored
        
    def load_data(self):
        """Load game data from JSON files."""
        try:
            # Load rooms
            with open('data/rooms.json', 'r') as f:
                rooms_data = json.load(f)
            
            for room_id, data in rooms_data.items():
                room = Room(data['name'], data['description'], data.get('short_description'))
                room.exits = data.get('exits', {})
                self.rooms[room_id] = room
            
            # Load items
            with open('data/items.json', 'r') as f:
                items_data = json.load(f)
            
            for item_id, data in items_data.items():
                item = Item(
                    data['name'],
                    data['description'],
                    data.get('synonyms', []),
                    data.get('takeable', True),
                    data.get('readable', False),
                    data.get('useable', False),
                    data.get('openable', False),
                    data.get('key_required')
                )
                
                item.read_text = data.get('read_text', '')
                self.items[item_id] = item
            
            # Load messages
            with open('data/messages.json', 'r') as f:
                self.messages = json.load(f)
            
            # Place items in rooms and containers
            self._setup_items()
            
        except FileNotFoundError as e:
            print(f"Error loading data files: {e}")
            return False
        except json.JSONDecodeError as e:
            print(f"Error parsing JSON data: {e}")
            return False
        
        return True
    
    def _setup_items(self):
        """Place items in their initial locations."""
        items_data = {}
        with open('data/items.json', 'r') as f:
            items_data = json.load(f)
        
        for item_id, data in items_data.items():
            item = self.items[item_id]
            
            if 'room' in data:
                # Item starts in a room
                room_id = data['room']
                if room_id in self.rooms:
                    self.rooms[room_id].add_item(item)
            
            elif 'container' in data:
                # Item starts inside another item
                container_id = data['container']
                if container_id in self.items:
                    self.items[container_id].add_content(item)
    
    def start_game(self):
        """Start a new game."""
        if not self.load_data():
            return False
        
        self.player = Player("Adventurer", "field")
        self.running = True
        self.lamp_on = False
        self.game_won = False
        self.scored_actions = set()
        
        # Show the BBS-style title card
        print(ANSIArt.title_card())
        input()  # Wait for user to press enter
        print(ANSIColors.CLEAR_SCREEN)
        
        # Show main game logo
        print(ANSIArt.game_logo())
        
        print(colorize_text(self.messages['welcome'], ANSIColors.BRIGHT_GREEN))
        print(ANSIArt.bbs_footer())
        self.look_around()
        return True
    
    def save_game(self, filename='savegame.pkl'):
        """Save the current game state."""
        try:
            if not os.path.exists('saves'):
                os.makedirs('saves')
            
            save_data = {
                'player': self.player,
                'rooms': self.rooms,
                'items': self.items,
                'lamp_on': self.lamp_on,
                'scored_actions': self.scored_actions,
                'game_won': self.game_won
            }
            
            with open(f'saves/{filename}', 'wb') as f:
                pickle.dump(save_data, f)
            
            return True
        except Exception as e:
            print(f"Error saving game: {e}")
            return False
    
    def load_game(self, filename='savegame.pkl'):
        """Load a saved game state."""
        try:
            if not self.load_data():  # Load base data first
                return False
            
            with open(f'saves/{filename}', 'rb') as f:
                save_data = pickle.load(f)
            
            self.player = save_data['player']
            self.rooms = save_data['rooms']
            self.items = save_data['items']
            self.lamp_on = save_data.get('lamp_on', False)
            self.scored_actions = save_data.get('scored_actions', set())
            self.game_won = save_data.get('game_won', False)
            self.running = True
            
            return True
        except Exception as e:
            print(f"Error loading game: {e}")
            return False
    
    def process_command(self, input_text):
        """Process a user command."""
        command, args = self.parser.parse(input_text)
        
        if command is None:
            return
        
        # Handle special cases and Easter eggs
        input_lower = input_text.lower().strip()
        if input_lower in ['xyzzy', 'plugh', 'hello', 'zork', 'author']:
            print(self.messages['easter_eggs'].get(input_lower, ''))
            return
        
        # Dispatch to appropriate command handler
        if command == 'move':
            self.move_player(args)
        elif command == 'look':
            self.look_around()
        elif command == 'examine':
            self.examine_object(args)
        elif command == 'inventory':
            self.show_inventory()
        elif command == 'take':
            self.take_object(args)
        elif command == 'drop':
            self.drop_object(args)
        elif command == 'use':
            self.use_object(args)
        elif command == 'open':
            self.open_object(args)
        elif command == 'read':
            self.read_object(args)
        elif command == 'help':
            print(self.parser.get_help_text())
        elif command == 'quit':
            self.quit_game()
        elif command == 'save':
            if self.save_game():
                print(self.messages['game']['save_success'])
            else:
                print(self.messages['game']['save_error'])
        elif command == 'load':
            if self.load_game():
                print(self.messages['game']['load_success'])
                self.look_around()
            else:
                print(self.messages['game']['load_error'])
        elif command == 'score':
            self.show_score()
        elif command == 'health':
            self.show_health()
        elif command == 'status':
            print(self.player.show_status())
        elif command == 'unknown':
            print(self.messages['game']['unknown_command'])
    
    def move_player(self, direction):
        """Move the player in the specified direction."""
        if not direction:
            print(self.messages['movement']['no_exit'])
            return
        
        current_room = self.rooms[self.player.current_room]
        next_room_id = current_room.get_exit(direction)
        
        if not next_room_id:
            print(self.messages['movement']['no_exit'])
            return
        
        # Check if moving into dark room without light
        if next_room_id == 'hallway' and not self.lamp_on:
            print(self.messages['dark_room']['movement_blocked'])
            return
        
        self.player.move_to(next_room_id)
        self.look_around()
    
    def look_around(self):
        """Show the current room description."""
        current_room = self.rooms[self.player.current_room]
        
        # Handle dark room with special ANSI graphics
        if self.player.current_room == 'hallway' and not self.lamp_on:
            print(ANSIArt.dark_room_warning())
            print(colorize_text(self.messages['dark_room']['description'], ANSIColors.BRIGHT_RED))
            return
        
        # Show room with ANSI border
        print(ANSIArt.room_border(current_room.name, current_room.short_description))
        
        # Add special ASCII art for certain rooms
        if self.player.current_room == 'house':
            print(ANSIArt.ascii_house())
        elif self.player.current_room == 'cave':
            print(ANSIArt.ascii_cave())
        elif self.player.current_room == 'living_room':
            # Check if treasure chest is still there
            chest = current_room.get_item('treasure chest')
            if chest:
                print(ANSIArt.ascii_treasure())
        
        # Show room description with color
        description = current_room.description
        if self.lamp_on and self.player.current_room == 'hallway':
            description += f" {ANSIArt.lamp_glow()} Your lamp illuminates the darkness."
        
        print(colorize_text(description, ANSIColors.BRIGHT_WHITE))
        
        # Show items in room with color
        if current_room.items:
            print(colorize_text("\nYou can see:", ANSIColors.BRIGHT_CYAN))
            for item in current_room.items:
                if item.name == 'lamp' and self.lamp_on:
                    print(f"  {ANSIArt.lamp_glow()} {colorize_text(item.name, ANSIColors.BRIGHT_YELLOW)} (glowing)")
                else:
                    print(f"  {colorize_text(item.name, ANSIColors.BRIGHT_GREEN)}")
        
        # Show exits with color
        exits = current_room.exits
        if exits:
            exit_text = "Exits: " + ", ".join([colorize_text(direction, ANSIColors.BRIGHT_MAGENTA) for direction in exits.keys()])
            print(f"\n{exit_text}")
        
        # Show status bar
        print(ANSIArt.status_bar(self.player.health, self.player.score, self.player.moves, len(self.player.inventory)))
    
    def examine_object(self, object_name):
        """Examine an object in detail."""
        if not object_name:
            print("Examine what?")
            return
        
        # Check if in dark room
        if self.player.current_room == 'hallway' and not self.lamp_on:
            print(self.messages['dark_room']['action_blocked'])
            return
        
        object_name = self.parser.normalize_object_name(object_name)
        
        # Check inventory first
        item = self.player.get_item(object_name)
        if item:
            print(item.examine())
            return
        
        # Check current room
        current_room = self.rooms[self.player.current_room]
        item = current_room.get_item(object_name)
        if item:
            print(item.examine())
            return
        
        # Check inside open containers in the room
        for room_item in current_room.items:
            if room_item.is_open:
                for content_item in room_item.contents:
                    if content_item.matches_name(object_name):
                        print(content_item.examine())
                        return
        
        print(self.messages['interaction']['nothing_special'])
    
    def show_inventory(self):
        """Show the player's inventory."""
        inventory_text = self.player.show_inventory()
        print(box_text(inventory_text, ANSIColors.BRIGHT_CYAN))
    
    def take_object(self, object_name):
        """Take an object from the current room."""
        if not object_name:
            print("Take what?")
            return
        
        # Check if in dark room
        if self.player.current_room == 'hallway' and not self.lamp_on:
            print(colorize_text(self.messages['dark_room']['action_blocked'], ANSIColors.BRIGHT_RED))
            return
        
        object_name = self.parser.normalize_object_name(object_name)
        current_room = self.rooms[self.player.current_room]
        
        # Check if item is in room
        item = current_room.get_item(object_name)
        if item and item.takeable:
            current_room.remove_item(object_name)
            self.player.add_item(item)
            print(colorize_text(self.messages['inventory']['taken'], ANSIColors.BRIGHT_GREEN))
            
            # Award points for specific items
            self._check_scoring('take', item.name)
            return
        
        # Check inside open containers
        for room_item in current_room.items:
            if room_item.is_open:
                for content_item in room_item.contents:
                    if content_item.matches_name(object_name) and content_item.takeable:
                        room_item.contents.remove(content_item)
                        self.player.add_item(content_item)
                        print(colorize_text(self.messages['inventory']['taken'], ANSIColors.BRIGHT_GREEN))
                        
                        # Award points 
                        self._check_scoring('take', content_item.name)
                        return
        
        print(colorize_text(self.messages['inventory']['not_here'], ANSIColors.BRIGHT_RED))
    
    def drop_object(self, object_name):
        """Drop an object in the current room."""
        if not object_name:
            print("Drop what?")
            return
        
        object_name = self.parser.normalize_object_name(object_name)
        item = self.player.remove_item(object_name)
        
        if item:
            current_room = self.rooms[self.player.current_room]
            current_room.add_item(item)
            print(self.messages['inventory']['dropped'])
        else:
            print(self.messages['inventory']['not_carrying'])
    
    def use_object(self, object_name):
        """Use an object."""
        if not object_name:
            print("Use what?")
            return
        
        object_name = self.parser.normalize_object_name(object_name)
        item = self.player.get_item(object_name)
        
        if not item:
            print(self.messages['inventory']['not_carrying'])
            return
        
        # Special case for lamp with ANSI effects
        if item.matches_name('lamp') or item.matches_name('lantern'):
            if not self.lamp_on:
                self.lamp_on = True
                print(f"{ANSIArt.lamp_glow()} {colorize_text(self.messages['lamp']['turn_on'], ANSIColors.BRIGHT_YELLOW)}")
                # If in dark hallway, show the room description
                if self.player.current_room == 'hallway':
                    self.look_around()
            else:
                self.lamp_on = False
                print(colorize_text(self.messages['lamp']['turn_off'], ANSIColors.DIM))
            return
        
        # Generic use
        if item.useable:
            success, message = item.use()
            print(colorize_text(message, ANSIColors.BRIGHT_GREEN if success else ANSIColors.BRIGHT_RED))
        else:
            print(colorize_text(self.messages['interaction']['cant_use'], ANSIColors.BRIGHT_RED))
    
    def open_object(self, object_name):
        """Open an object."""
        if not object_name:
            print("Open what?")
            return
        
        # Check if in dark room
        if self.player.current_room == 'hallway' and not self.lamp_on:
            print(self.messages['dark_room']['action_blocked'])
            return
        
        object_name = self.parser.normalize_object_name(object_name)
        
        # Check current room for object
        current_room = self.rooms[self.player.current_room]
        item = current_room.get_item(object_name)
        
        if not item:
            # Check inventory
            item = self.player.get_item(object_name)
        
        if not item:
            print(self.messages['inventory']['not_here'])
            return
        
        if not item.openable:
            print(self.messages['interaction']['cant_open'])
            return
        
        # Try to open with player's items as keys
        success, message = item.open(self.player.inventory)
        print(message)
        
        if success:
            self._check_scoring('open', item.name)
            
            # Special case: if treasure chest is opened, add treasure to room
            if item.name == 'treasure chest' and item.contents:
                current_room = self.rooms[self.player.current_room]
                for content_item in item.contents:
                    current_room.add_item(content_item)
                item.contents = []  # Remove from chest since they're now in room
    
    def read_object(self, object_name):
        """Read an object."""
        if not object_name:
            print("Read what?")
            return
        
        # Check if in dark room
        if self.player.current_room == 'hallway' and not self.lamp_on:
            print(self.messages['dark_room']['action_blocked'])
            return
        
        object_name = self.parser.normalize_object_name(object_name)
        
        # Check inventory first
        item = self.player.get_item(object_name)
        if item:
            print(item.read())
            if item.readable:
                self._check_scoring('read', item.name)
            return
        
        # Check current room
        current_room = self.rooms[self.player.current_room]
        item = current_room.get_item(object_name)
        if item:
            print(item.read())
            if item.readable:
                self._check_scoring('read', item.name)
            return
        
        print(self.messages['inventory']['not_here'])
    
    def _check_scoring(self, action, item_name):
        """Check if an action should award points."""
        action_key = f"{action}_{item_name.lower().replace(' ', '_')}"
        
        if action_key not in self.scored_actions:
            points = 0
            
            if action_key == 'take_leaflet':
                points = self.score_values['take_leaflet']
            elif action_key == 'open_mailbox':
                points = self.score_values['open_mailbox']
            elif action_key == 'take_lamp':
                points = self.score_values['take_lamp']
            elif action_key == 'take_brass_key':
                points = self.score_values['take_key']
            elif action_key == 'read_ancient_scroll':
                points = self.score_values['read_scroll']
            elif action_key == 'open_treasure_chest':
                points = self.score_values['open_chest']
            elif action_key == 'take_golden_treasure':
                points = self.score_values['take_treasure']
                # Win condition - taking the treasure wins the game!
                self._win_game()
            
            if points > 0:
                self.player.add_score(points)
                self.scored_actions.add(action_key)
                score_msg = f"[+{points} points] Total Score: {self.player.score}"
                print(colorize_text(score_msg, ANSIColors.BRIGHT_YELLOW))
    
    def _win_game(self):
        """Handle winning the game."""
        self.game_won = True
        print(ANSIArt.victory_banner())
        print(colorize_text(self.messages['game']['win_message'].format(
            score=self.player.score,
            moves=self.player.moves
        ), ANSIColors.BRIGHT_YELLOW))
    
    def show_score(self):
        """Show the player's current score."""
        max_score = sum(self.score_values.values())
        print(f"Score: {self.player.score}/{max_score}")
        print(f"Moves: {self.player.moves}")
    
    def show_health(self):
        """Show the player's health."""
        print(f"Health: {self.player.health}/100")
    
    def quit_game(self):
        """Quit the game."""
        print(self.messages['game']['quit_confirm'])
        self.running = False
    
    def run(self):
        """Main game loop."""
        while self.running and not self.game_won:
            try:
                print(ANSIArt.command_prompt(), end="")
                user_input = input().strip()
                if user_input:
                    self.process_command(user_input)
            except (EOFError, KeyboardInterrupt):
                print(f"\n{colorize_text(self.messages['game']['quit_confirm'], ANSIColors.BRIGHT_YELLOW)}")
                break