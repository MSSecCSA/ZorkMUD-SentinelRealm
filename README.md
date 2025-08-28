# ZorkMUD: Sentinel Realm

A classic text-based adventure game inspired by the legendary Zork series and 90's BBS games. This POC implementation provides a foundational MUD engine with classic gameplay mechanics designed for future integration with Sentinel learning scenarios.

## Features

- **Classic Zork-style gameplay** with natural language command processing
- **Room-based exploration** with atmospheric descriptions
- **Interactive objects** and inventory management
- **Puzzle solving** requiring keys, light sources, and logical thinking
- **Save/load functionality** to preserve your progress
- **Score system** tracking your achievements
- **Modular design** for easy extension and modification

## Quick Start

1. **Run the game:**
   ```bash
   python main.py
   ```

2. **Basic commands:**
   - `look` - Examine your surroundings
   - `north`, `south`, `east`, `west` (or `n`, `s`, `e`, `w`) - Move around
   - `take <object>` - Pick up items
   - `inventory` (or `i`) - See what you're carrying
   - `help` - Full command reference

3. **Your goal:** Find the treasure hidden somewhere in the world!

## Installation

### Requirements
- Python 3.6 or higher
- No additional dependencies required

### Setup
1. Clone or download this repository
2. Navigate to the game directory
3. Run `python main.py` to start playing

## Game World

You begin your adventure in an **open field west of a white house**. From here, you can explore:

- **The White House** - A mysterious boarded-up building
- **Forest areas** - Dark woods with hidden secrets  
- **Underground caves** - Ancient chambers with carved symbols
- **Gardens and pathways** - Scenic areas with useful items

### Key Locations
- **Open Field** - Your starting point with a mailbox
- **Kitchen** - Inside the house, contains useful items
- **Dark Hallway** - Too dark to navigate safely without light
- **Living Room** - Contains the treasure chest (goal!)
- **Forest Clearing** - Ancient ruins with a hidden entrance
- **Underground Cave** - Mysterious symbols and ancient scroll

## Gameplay Guide

### Essential Commands

**Movement:**
- `north`, `south`, `east`, `west` (or `n`, `s`, `e`, `w`)
- `go <direction>`

**Observation:**
- `look` (or `l`) - Look around the current room
- `examine <object>` (or `x <object>`) - Examine objects closely

**Inventory Management:**
- `inventory` (or `i`) - Show what you're carrying
- `take <object>` (or `get <object>`) - Pick up items
- `drop <object>` - Drop items

**Interaction:**
- `open <object>` - Open containers like boxes or doors
- `read <object>` - Read text on papers, signs, etc.
- `use <object>` - Use items (like turning on a lamp)

**System:**
- `help` - Show all available commands
- `save` - Save your current progress
- `load` - Load a previously saved game
- `score` - Check your current score
- `quit` - Exit the game

### Walkthrough Hints

**Getting Started:**
1. Start by examining the mailbox in the field
2. Open it to find something to read
3. Explore all the rooms to map out the world
4. Collect useful items as you find them

**Key Items to Find:**
- **Leaflet** - Contains welcome message and hints
- **Lamp** - Essential for navigating dark areas
- **Brass Key** - Opens locked containers
- **Ancient Scroll** - Provides important clues
- **Golden Treasure** - Your ultimate goal!

**Solving the Main Puzzle:**
1. Find and take the lamp from the kitchen
2. Use the lamp to illuminate dark areas
3. Locate the brass key hidden in the garden
4. Find the treasure chest in the living room
5. Use the key to open the chest and claim the treasure!

### Scoring System

You earn points for completing various tasks:
- Reading the leaflet: 5 points
- Opening the mailbox: 5 points
- Taking the lamp: 10 points
- Finding the key: 15 points
- Reading the scroll: 10 points
- Opening the treasure chest: 20 points
- **Taking the treasure: 50 points (WINNER!)**

**Maximum possible score:** 115 points

## Technical Details

### File Structure
```
/
├── main.py              # Main game entry point
├── game_engine.py       # Core game logic and command processing
├── player.py           # Player class (inventory, health, location)
├── room.py             # Room class (descriptions, exits, items)
├── item.py             # Item class (interactive objects)
├── parser.py           # Command parser (natural language processing)
├── data/
│   ├── rooms.json      # Room definitions and connections
│   ├── items.json      # Item properties and initial locations  
│   └── messages.json   # Game text and responses
├── saves/              # Directory for saved games
└── README.md           # This file
```

### Modular Design

The game is built with object-oriented design principles:

- **GameEngine**: Manages overall game state and command dispatch
- **Player**: Tracks player location, inventory, health, and score
- **Room**: Represents game locations with descriptions and exits
- **Item**: Interactive objects with various properties (takeable, readable, etc.)
- **Parser**: Interprets natural language commands into game actions

### Data Files

Game content is stored in JSON files for easy modification:

- **rooms.json**: Defines all game locations, descriptions, and connections
- **items.json**: Defines all interactive objects and their properties
- **messages.json**: Contains game text, responses, and flavor messages

### Save System

The game uses Python's pickle module to save complete game state:
- Player status (location, inventory, health, score)
- Room states (visited status, item locations)
- Item states (opened containers, lamp status)
- Progress tracking (scored actions, win condition)

## Future Integration Points

This POC is designed for future integration with Sentinel learning scenarios:

- **Modular command system** - Easy to add educational challenges
- **Flexible parsing** - Can handle domain-specific terminology
- **Score/progress tracking** - Ready for learning analytics
- **Save/load system** - Supports checkpoint-based learning
- **Extensible item system** - Can add interactive learning objects

## Development

### Adding New Content

**New Rooms:**
1. Add room definition to `data/rooms.json`
2. Define exits to connect with existing rooms
3. Test navigation and descriptions

**New Items:**
1. Add item definition to `data/items.json`
2. Set properties (takeable, readable, etc.)
3. Place in room or container
4. Add any special interactions to game engine

**New Commands:**
1. Add command patterns to `parser.py`
2. Implement command handler in `game_engine.py`
3. Test with various input variations

### Testing

Run the game and test all major features:
```bash
python main.py
```

Test sequence:
1. Movement between all rooms
2. Taking and dropping items
3. Opening containers and reading text
4. Using the lamp in dark areas
5. Solving the main puzzle
6. Save and load functionality

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.

## Contributing

This is a proof-of-concept implementation. Future development will focus on:
- Integration with Sentinel learning platforms
- Multiplayer capabilities
- Enhanced command parsing
- Educational scenario frameworks

---

**Enjoy your adventure in ZorkMUD: Sentinel Realm!**

*Remember: The goal is not just to find the treasure, but to explore, learn, and enjoy the classic adventure game experience.*