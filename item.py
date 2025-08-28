"""
Item class for the ZorkMUD game engine.
Represents interactive objects in the game world.
"""

class Item:
    """Represents an interactive item in the game world."""
    
    def __init__(self, name, description, synonyms=None, takeable=True, 
                 readable=False, useable=False, openable=False, key_required=None):
        """
        Initialize an item.
        
        Args:
            name (str): Primary name of the item
            description (str): Description when examined
            synonyms (list): Alternative names for the item
            takeable (bool): Whether the item can be taken
            readable (bool): Whether the item can be read
            useable (bool): Whether the item can be used
            openable (bool): Whether the item can be opened
            key_required (str): Name of key required to open (if openable)
        """
        self.name = name
        self.description = description
        self.synonyms = synonyms or []
        self.takeable = takeable
        self.readable = readable
        self.useable = useable
        self.openable = openable
        self.key_required = key_required
        self.is_open = False
        self.contents = []  # Items inside this item (if openable)
        self.read_text = ""  # Text shown when read
        
    def matches_name(self, name):
        """Check if the given name matches this item."""
        name_lower = name.lower()
        return (name_lower == self.name.lower() or 
                name_lower in [syn.lower() for syn in self.synonyms])
    
    def take(self):
        """Attempt to take the item."""
        if self.takeable:
            return True, f"You take the {self.name}."
        else:
            return False, f"You can't take the {self.name}."
    
    def examine(self):
        """Examine the item."""
        return self.description
    
    def read(self):
        """Read the item if possible."""
        if self.readable:
            return self.read_text or f"There's nothing to read on the {self.name}."
        else:
            return f"You can't read the {self.name}."
    
    def open(self, key_items=None):
        """Open the item if possible."""
        if not self.openable:
            return False, f"You can't open the {self.name}."
        
        if self.is_open:
            return False, f"The {self.name} is already open."
        
        if self.key_required:
            key_items = key_items or []
            has_key = any(item.matches_name(self.key_required) for item in key_items)
            if not has_key:
                return False, f"The {self.name} is locked. You need {self.key_required}."
        
        self.is_open = True
        if self.contents:
            contents_str = ", ".join([item.name for item in self.contents])
            return True, f"You open the {self.name}. Inside you find: {contents_str}."
        else:
            return True, f"You open the {self.name}. It's empty."
    
    def use(self):
        """Use the item if possible."""
        if self.useable:
            return True, f"You use the {self.name}."
        else:
            return False, f"You can't use the {self.name}."
    
    def add_content(self, item):
        """Add an item to this item's contents."""
        self.contents.append(item)
    
    def remove_content(self, item_name):
        """Remove an item from this item's contents."""
        for i, item in enumerate(self.contents):
            if item.matches_name(item_name):
                return self.contents.pop(i)
        return None