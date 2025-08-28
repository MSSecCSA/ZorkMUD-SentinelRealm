"""
Room class for the ZorkMUD game engine.
Represents locations in the game world.
"""

class Room:
    """Represents a room/location in the game world."""
    
    def __init__(self, name, description, short_description=None):
        """
        Initialize a room.
        
        Args:
            name (str): Name of the room
            description (str): Full description shown on 'look'
            short_description (str): Brief description for movement messages
        """
        self.name = name
        self.description = description
        self.short_description = short_description or name
        self.exits = {}  # direction -> room_id mapping
        self.items = []  # items in the room
        self.visited = False
        
    def add_exit(self, direction, room_id):
        """Add an exit to another room."""
        self.exits[direction.lower()] = room_id
    
    def get_exit(self, direction):
        """Get the room ID for a given direction."""
        return self.exits.get(direction.lower())
    
    def add_item(self, item):
        """Add an item to the room."""
        self.items.append(item)
    
    def remove_item(self, item_name):
        """Remove an item from the room by name."""
        for i, item in enumerate(self.items):
            if item.matches_name(item_name):
                return self.items.pop(i)
        return None
    
    def get_item(self, item_name):
        """Get an item from the room by name."""
        for item in self.items:
            if item.matches_name(item_name):
                return item
        return None
    
    def look(self):
        """Get the full room description."""
        desc = self.description
        
        # Add items in room
        if self.items:
            visible_items = []
            for item in self.items:
                if item.is_open and item.contents:
                    # Show opened containers and their contents
                    contents_str = ", ".join([i.name for i in item.contents])
                    visible_items.append(f"{item.name} (open, containing {contents_str})")
                else:
                    visible_items.append(item.name)
            
            if visible_items:
                desc += "\n\nYou can see: " + ", ".join(visible_items) + "."
        
        # Add exits
        if self.exits:
            exit_list = []
            for direction in sorted(self.exits.keys()):
                exit_list.append(direction)
            desc += f"\n\nExits: {', '.join(exit_list)}"
        
        self.visited = True
        return desc
    
    def get_items_description(self):
        """Get description of items in the room."""
        if not self.items:
            return ""
        
        items_desc = []
        for item in self.items:
            if item.is_open and item.contents:
                contents_str = ", ".join([i.name for i in item.contents])
                items_desc.append(f"There is {item.name} here (open, containing {contents_str}).")
            else:
                items_desc.append(f"There is {item.name} here.")
        
        return "\n".join(items_desc)