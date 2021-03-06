from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player1 = Player(room['outside'])
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
running = True

while running:
    print(player1.room.name)
    print(player1.room.description)
    rawcommand = input("$")
    command = rawcommand.split('')
    if len(command) is 1:

        if command.lower() in ["n", "s", "e", "w"]:
            concatenated = command + '_to'
            if hasattr(player1.room, concatenated):
                player1.room = getattr(player1.room, concatenated)
            else:
                print('You can\'t go that way!')

        elif command.lower() in ["q"]:
            running = False

        elif command.lower() is 'look':
            print(player1.room.name)
            print(player1.room.description)

        elif command.lower is 'get':
            print("What are you trying to get?")

        elif command.lower is 'drop':
            print("What are you trying to drop?")
        
        else:
            print('I don\'t understand what you are trying to do. Type help for a list of valid commands.')


    elif len(command) is 2:
        if command.lower[0] is 'look':
            if player1.items.find(command.lower[1]) is not -1:
                print(player1.items.index(command.lower[1]).description)
            else:
                print('No items.')

            
    
