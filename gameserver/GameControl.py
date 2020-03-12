import string
import random


# game_state stucture [moves]
# moves stucture [player, tile_scaler]
# gameobj stucture { 'tiles': tiles, 'win': "", 'game_state': game_state }

id_length = 10

games = {}

# ========= Abstractions
def IdExists(game_id):
    try:
        if games[game_id]: pass
        return True
    except:
        return False

def CreateGameImpl(game_id, tiles):
    games[game_id] = {
            'tiles': tiles,
            'win': "",
            'game_state': []
            }

def isGameEnded(game_id):
    if not games[game_id]['win']:
        return False
    return True

def getTiles(game_id):
    return games[game_id]['tiles']

def getGameState(game_id):
    return games[game_id]['game_state']

def RetGameImpl(game_id):
    try:
        gameobj = games[game_id]
        return gameobj
    except KeyError:
        return None

def addMove(game_id, move):
    pass

def EndGame(game_id, outcome, player):
    if outcome == True:
        games[game_id]['win'] = player
    elif outcome == -1:
        games[game_id]['win'] = "-1"

# ======== END Abstractions

# ======== Helper Function
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

# ======= END Helper

def CreateGame(tiles):
    game_id = str(random.choices(string.ascii_letters, k=id_length))
    if IdExists(game_id):
        return CreateGame(tiles)

    CreateGameImpl(game_id, tiles)
    return { "gid": game_id }

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
        if not IdExists(game_id):
            return False
        if not isGameEnded(game_id):
            player, scal_val = gameobj
            tiles = getTiles(game_id)
            scal = int(scal_val)
            x, y = Scal2Vec(tiles, scal)

            # For right now there are only 2 players available
            if not (int(player) == 0 or int(player) == 1):
                return False

            # Checking if the x, y values are within bounds
            if not ((x >= 0 and x < tiles) and (y >= 0 and y < tiles)):
                return False

            # Getting the last move and checking the player
            game_state = getGameState(game_id)
            if len(game_state) == 0 or game_state[-1][0] != int(player):

                if CheckSet(game_state, scal):
                    return False

                game_state.append([int(player), scal])
                addMove(game_id, [int(player), scal]) # For DataBase Only
                outcome = CheckWin(game_state, tiles, [int(player), scal])
                EndGame(game_id, outcome, player) # Does the checking itself

    except KeyError: return False
    except TypeError: return False
    return True


def RetGame(game_id):
    return RetGameImpl(game_id)
