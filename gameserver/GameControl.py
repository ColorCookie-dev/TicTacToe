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

def Vec2Scal(tiles, x, y):
    return (tiles*y) + x

def Scal2Vec(tiles, scal):
    x = scal%tiles
    y = scal//tiles
    return (x, y)

def CheckSet(game_state, scal):
    for i in game_state:
        if (i[1] == scal):
            return True
    return False

def CheckWin(game_state, tiles, recent_move): # Accepts integers in recent_move parameter

    # Check For Draw
    if (len(game_state) == tiles*tiles):
        return -1

    player, scal = recent_move
    x, y = Scal2Vec(tiles, scal)

    if y >= 2: # Checks Vertically upwards
        if ([player, Vec2Scal(tiles, x, y-1)] in game_state) and ([player, Vec2Scal(tiles, x, y-2)] in game_state):
            return True

        if x >= 2: # Checks Backward Slash Up
            if ([player, Vec2Scal(tiles, x-1, y-1)] in game_state) and ([player, Vec2Scal(tiles, x-2, y-2)] in game_state):
                return True

        if x <= tiles-3: # Checks Forward Slash Up
            if ([player, Vec2Scal(tiles, x+1, y-1)] in game_state) and ([player, Vec2Scal(tiles, x+2, y-2)] in game_state):
                return True

    if y <= tiles-3: # Checks Vertically downwards
        if ([player, Vec2Scal(tiles, x, y+1)] in game_state) and ([player, Vec2Scal(tiles, x, y+2)] in game_state):
            return True

        if x >= 2: # Checks Backward Slash Down
            if ([player, Vec2Scal(tiles, x-1, y+1)] in game_state) and ([player, Vec2Scal(tiles, x-2, y+2)] in game_state):
                return True

        if x <= tiles-3: # Checks Forward Slash Down
            if ([player, Vec2Scal(tiles, x+1, y+1)] in game_state) and ([player, Vec2Scal(tiles, x+2, y+2)] in game_state):
                return True

    if x >= 2: # Checks Horizonatally left
        if ([player, Vec2Scal(tiles, x-1, y)] in game_state) and ([player, Vec2Scal(tiles, x-2, y)] in game_state):
            return True

    if x <= tiles-3: # Checks Horizonatally right
        if ([player, Vec2Scal(tiles, x+1, y)] in game_state) and ([player, Vec2Scal(tiles, x+2, y)] in game_state):
            return True

    if (x <= tiles-2) and (x >= 1): # Checks Horizonatally middle
        if ([player, Vec2Scal(tiles, x+1, y)] in game_state) and ([player, Vec2Scal(tiles, x-1, y)] in game_state):
            return True

        if (y <= tiles-2) and (y >= 1): # Checks From Middle diagonally
            if ([player, Vec2Scal(tiles, x+1, y+1)] in game_state) and ([player, Vec2Scal(tiles, x-1, y-1)] in game_state):
                return True

            if ([player, Vec2Scal(tiles, x-1, y+1)] in game_state) and ([player, Vec2Scal(tiles, x+1, y-1)] in game_state):
                return True

    if (y <= tiles-2) and (y >= 1): # Checks Vertically middle
        if ([player, Vec2Scal(tiles, x, y+1)] in game_state) and ([player, Vec2Scal(tiles, x, y-1)] in game_state):
            return True

    return False

def Move(game_id, gameobj):
    try:
        if not games[game_id]['win']:
            player, scal_val = gameobj
            tiles = games[game_id]['tiles']
            scal = int(scal_val)
            x, y = Scal2Vec(tiles, scal)

            # For right now there are only 2 players available
            if not (int(player) == 0 or int(player) == 1):
                return False

            # Checking if the x, y values are within bounds
            if not ((x >= 0 and x < tiles) and (y >= 0 and y < tiles)):
                return False

            # Getting the last move and checking the player
            game_state = games[game_id]['game_state']
            if len(game_state) == 0 or game_state[-1][0] != int(player):

                if CheckSet(game_state, scal):
                    return False

                game_state.append([int(player), scal])
                outcome = CheckWin(game_state, tiles, [int(player), scal])
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
