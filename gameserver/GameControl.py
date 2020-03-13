import string
import random


# game_state stucture [moves]
# moves stucture [player, tile_scaler]
# gameobj stucture { 'tiles': tiles, 'win': "", 'game_state': game_state }

id_length = 10

games = {}

class backends:
    python_runtime = 0
    database = 1

storage_backend = backends.python_runtime

# ========= Abstractions
def id_exists(game_id):
    if storage_backend == backends.python_runtime:
        try:
            if games[game_id]: pass
            return True
        except:
            return False
    elif storage_backend == backends.database:
        pass

def create_game_impl(game_id, tiles):
    if storage_backend == backends.python_runtime:
        games[game_id] = {
                'tiles': tiles,
                'win': "",
                'game_state': []
                }
    elif storage_backend == backends.database:
        pass

def is_game_ended(game_id):
    if storage_backend == backends.python_runtime:
        if not games[game_id]['win']:
            return False
        return True
    elif storage_backend == backends.database:
        pass

def get_tiles(game_id):
    if storage_backend == backends.python_runtime:
        return games[game_id]['tiles']
    elif storage_backend == backends.database:
        pass

def get_game_state(game_id):
    if storage_backend == backends.python_runtime:
        return games[game_id]['game_state']
    elif storage_backend == backends.database:
        pass

def del_game_cache(game_id):
    if storage_backend == backends.python_runtime:
        del games[game_id]
    elif storage_backend == backends.database:
        pass

def ret_game_impl(game_id):
    if storage_backend == backends.python_runtime:
        try:
            gameobj = games[game_id]
            if is_game_ended(game_id):
                del_game_cache(game_id) # doesn't need to run if the there is some DB as backend
            return gameobj
        except KeyError:
            return None
    elif storage_backend == backends.database:
        pass

def add_move(game_id, move):
    if storage_backend == backends.python_runtime:
        pass
    elif storage_backend == backends.database:
        pass # TODO: Needed replaced to record the move

def end_game(game_id, outcome, player):
    if storage_backend == backends.python_runtime:
        if outcome == True:
            games[game_id]['win'] = player
        elif outcome == -1:
            games[game_id]['win'] = "-1"
    elif storage_backend == backends.database:
        pass

# ======== END Abstractions

# ======== Helper Function
def vec2scal(tiles, x, y):
    return (tiles*y) + x

def scal2vec(tiles, scal):
    x = scal%tiles
    y = scal//tiles
    return (x, y)

def check_set(game_state, scal):
    for i in game_state:
        if (i[1] == scal):
            return True
    return False

def check_win(game_state, tiles, recent_move): # Accepts integers in recent_move parameter

    # Check For Draw
    if (len(game_state) == tiles*tiles):
        return -1

    player, scal = recent_move
    x, y = scal2vec(tiles, scal)

    if y >= 2: # Checks Vertically upwards
        if ([player, vec2scal(tiles, x, y-1)] in game_state) and ([player, vec2scal(tiles, x, y-2)] in game_state):
            return True

        if x >= 2: # Checks Backward Slash Up
            if ([player, vec2scal(tiles, x-1, y-1)] in game_state) and ([player, vec2scal(tiles, x-2, y-2)] in game_state):
                return True

        if x <= tiles-3: # Checks Forward Slash Up
            if ([player, vec2scal(tiles, x+1, y-1)] in game_state) and ([player, vec2scal(tiles, x+2, y-2)] in game_state):
                return True

    if y <= tiles-3: # Checks Vertically downwards
        if ([player, vec2scal(tiles, x, y+1)] in game_state) and ([player, vec2scal(tiles, x, y+2)] in game_state):
            return True

        if x >= 2: # Checks Backward Slash Down
            if ([player, vec2scal(tiles, x-1, y+1)] in game_state) and ([player, vec2scal(tiles, x-2, y+2)] in game_state):
                return True

        if x <= tiles-3: # Checks Forward Slash Down
            if ([player, vec2scal(tiles, x+1, y+1)] in game_state) and ([player, vec2scal(tiles, x+2, y+2)] in game_state):
                return True

    if x >= 2: # Checks Horizonatally left
        if ([player, vec2scal(tiles, x-1, y)] in game_state) and ([player, vec2scal(tiles, x-2, y)] in game_state):
            return True

    if x <= tiles-3: # Checks Horizonatally right
        if ([player, vec2scal(tiles, x+1, y)] in game_state) and ([player, vec2scal(tiles, x+2, y)] in game_state):
            return True

    if (x <= tiles-2) and (x >= 1): # Checks Horizonatally middle
        if ([player, vec2scal(tiles, x+1, y)] in game_state) and ([player, vec2scal(tiles, x-1, y)] in game_state):
            return True

        if (y <= tiles-2) and (y >= 1): # Checks From Middle diagonally
            if ([player, vec2scal(tiles, x+1, y+1)] in game_state) and ([player, vec2scal(tiles, x-1, y-1)] in game_state):
                return True

            if ([player, vec2scal(tiles, x-1, y+1)] in game_state) and ([player, vec2scal(tiles, x+1, y-1)] in game_state):
                return True

    if (y <= tiles-2) and (y >= 1): # Checks Vertically middle
        if ([player, vec2scal(tiles, x, y+1)] in game_state) and ([player, vec2scal(tiles, x, y-1)] in game_state):
            return True

    return False

# ======= END Helper

def create_game(tiles):
    game_id = str(random.choices(string.ascii_letters, k=id_length))
    if id_exists(game_id):
        return create_game(tiles)

    create_game_impl(game_id, tiles)
    return { "gid": game_id }

def move(game_id, gameobj):
    try:
        if not id_exists(game_id):
            return False

        if not is_game_ended(game_id):
            player, scal_val = gameobj
            tiles = get_tiles(game_id)
            scal = int(scal_val)
            x, y = scal2vec(tiles, scal)

            # For right now there are only 2 players available
            if not (int(player) == 0 or int(player) == 1):
                return False

            # Checking if the x, y values are within bounds
            if not ((x >= 0 and x < tiles) and (y >= 0 and y < tiles)):
                return False

            # Getting the last move and checking the player
            game_state = get_game_state(game_id)
            if len(game_state) == 0 or game_state[-1][0] != int(player):

                if check_set(game_state, scal):
                    return False

                game_state.append([int(player), scal])
                add_move(game_id, [int(player), scal]) # For DataBase Only
                outcome = check_win(game_state, tiles, [int(player), scal])
                end_game(game_id, outcome, player) # Does the checking itself

    except KeyError: return False
    except TypeError: return False
    return True


def ret_game(game_id):
    return ret_game_impl(game_id)
