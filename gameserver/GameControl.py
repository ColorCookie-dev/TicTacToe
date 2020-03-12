import string
import random

id_length = 5

games = {}

def CreateGame(tiles):
    game_id = str(random.choices(string.ascii_letters, k=id_length))
    try:
        if games[game_id]: pass
        return CreateGame(tiles)
    except:
        games[game_id] = {
                'tiles': tiles,
                'win': "",
                'game_state': []
                }
        return {
                "gid": game_id
                }

def CheckSet(game_state, x, y):
    for i in game_state:
        if (i[1] == x) and (i[2] == y):
            return True
    return False

def CheckWin(game_state, tiles, recent_move): # Accepts integers in recent_move parameter

    # Check For Draw
    if (len(game_state) == tiles*tiles):
        return -1

    player, x, y = recent_move

    if y >= 2: # Checks Vertically upwards
        if ([player, x, y-1] in game_state) and ([player, x, y-2] in game_state):
            return True

        if x >= 2: # Checks Backward Slash Up
            if ([player, x-1, y-1] in game_state) and ([player, x-2, y-2] in game_state):
                return True

        if x <= tiles-3: # Checks Forward Slash Up
            if ([player, x+1, y-1] in game_state) and ([player, x+2, y-2] in game_state):
                return True

    if y <= tiles-3: # Checks Vertically downwards
        if ([player, x, y+1] in game_state) and ([player, x, y+2] in game_state):
            return True

        if x >= 2: # Checks Backward Slash Down
            if ([player, x-1, y+1] in game_state) and ([player, x-2, y+2] in game_state):
                return True

        if x <= tiles-3: # Checks Forward Slash Down
            if ([player, x+1, y+1] in game_state) and ([player, x+2, y+2] in game_state):
                return True

    if x >= 2: # Checks Horizonatally left
        if ([player, x-1, y] in game_state) and ([player, x-2, y] in game_state):
            return True

    if x <= tiles-3: # Checks Horizonatally right
        if ([player, x+1, y] in game_state) and ([player, x+2, y] in game_state):
            return True

    if (x <= tiles-2) and (x >= 1): # Checks Horizonatally middle
        if ([player, x+1, y] in game_state) and ([player, x-1, y] in game_state):
            return True

        if (y <= tiles-2) and (y >= 1): # Checks From Middle diagonally
            if ([player, x+1, y+1] in game_state) and ([player, x-1, y-1] in game_state):
                return True

            if ([player, x-1, y+1] in game_state) and ([player, x+1, y-1] in game_state):
                return True

    if (y <= tiles-2) and (y >= 1): # Checks Vertically middle
        if ([player, x, y+1] in game_state) and ([player, x, y-1] in game_state):
            return True

    return False

def Move(game_id, gameobj):
    try:
        if not games[game_id]['win']:
            player, x, y = gameobj
            x = int(x)
            y = int(y)

            # For right now there are only 2 players available
            if not (int(player) == 0 or int(player) == 1):
                return False

            # Checking if the x, y values are within bounds
            tiles = games[game_id]['tiles']
            if not ((x >= 0 and x < tiles) and (y >= 0 and y < tiles)):
                return False

            # Getting the last move and checking the player
            if len(games[game_id]['game_state']) == 0 or games[game_id]['game_state'][-1][0] != int(player):

                game_state = games[game_id]['game_state']
                if CheckSet(game_state, x, y):
                    return False

                game_state.append([int(player), x, y])
                outcome = CheckWin(game_state, games[game_id]['tiles'], [int(player), x, y])
                if outcome == True:
                    games[game_id]['win'] = player
                elif outcome == -1:
                    games[game_id]['win'] = "-1"

    except KeyError: return False
    except TypeError: return False
    return True


def RetGame(game_id):
    try:
        gameobj = games[game_id]
        if gameobj['win'] != "":
            del games[game_id]
        return gameobj
    except KeyError:
        return None
