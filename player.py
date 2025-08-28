"""
Player class for the ZorkMUD game engine.
Manages player state including location, inventory, and health.
"""

class Player:
    """Represents the player character."""
    
    def __init__(self, name="Adventurer", starting_room="field"):
        """
        Initialize the player.
        
        Args:
            name (str): Player's name
            starting_room (str): ID of the starting room
        """
        self.name = name
        self.current_room = starting_room
        self.inventory = []
        self.health = 100
        self.score = 0
        self.moves = 0
        
    def move_to(self, room_id):
        """Move the player to a new room."""
        self.current_room = room_id
        self.moves += 1
    
    def add_item(self, item):
        """Add an item to the player's inventory."""
        self.inventory.append(item)
    
    def remove_item(self, item_name):
        """Remove an item from inventory by name."""
        for i, item in enumerate(self.inventory):
            if item.matches_name(item_name):
                return self.inventory.pop(i)
        return None
    
    def has_item(self, item_name):
        """Check if player has an item."""
        for item in self.inventory:
            if item.matches_name(item_name):
                return True
        return False
    
    def get_item(self, item_name):
        """Get an item from inventory by name."""
        for item in self.inventory:
            if item.matches_name(item_name):
                return item
        return None
    
    def show_inventory(self):
        """Display the player's inventory."""
        if not self.inventory:
            return "You are carrying nothing."
        
        items_list = []
        for item in self.inventory:
            items_list.append(f"  {item.name}")
        
        return "You are carrying:\n" + "\n".join(items_list)
    
    def show_status(self):
        """Display player status."""
        return f"""Player: {self.name}
Health: {self.health}/100
Score: {self.score}
Moves: {self.moves}
Location: {self.current_room}"""
    
    def add_score(self, points):
        """Add points to the player's score."""
        self.score += points
    
    def take_damage(self, damage):
        """Reduce player health."""
        self.health = max(0, self.health - damage)
        return self.health <= 0  # Returns True if player died
    
    def heal(self, amount):
        """Restore player health."""
        self.health = min(100, self.health + amount)
    
    def is_alive(self):
        """Check if player is alive."""
        return self.health > 0