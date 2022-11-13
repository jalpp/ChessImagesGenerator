
# Some methods that generate chess gif using lichess gifs
# based on certain input parameters, useful to create custom lichess gifs by code
# all methods return a string gif links which can be embeded anywhere
# https://lichess1.org/game/export/gif/black/4184QjKy.gif?theme=blue&piece=kosal


# create lichess gif by gameid, boardcolor, piecetype and side

def createGifById(gameid, boardcolor, piecetype, side):
    if (boardcolor == 'brown' and piecetype == 'alpha'):
        if (side == 'white'):
            return "https://lichess1.org/game/export/gif/white/" + gameid + ".gif?theme=brown&piece=alpha"
        else:
            return "https://lichess1.org/game/export/gif/black/" + gameid + ".gif?theme=brown&piece=alpha"
    elif (boardcolor == 'blue' and piecetype == 'horsey'):
        if (side == 'white'):
            return "https://lichess1.org/game/export/gif/white/" + gameid + ".gif?theme=blue&piece=horsey"
        else:
            return "https://lichess1.org/game/export/gif/black/" + gameid + ".gif?theme=blue&piece=horsey"
    else:
        if (side == 'white'):
            return "https://lichess1.org/game/export/gif/white/" + gameid + ".gif?theme=brown&piece=alpha"
        else:
            return "https://lichess1.org/game/export/gif/black/" + gameid + ".gif?theme=brown&piece=alpha"

# create simple lichess gif without worrying about styling


def createSimpleGifById(gameid, side):
    if (side == 'white'):
        return "https://lichess1.org/game/export/gif/white/" + gameid + ".gif?theme=brown&piece=alpha"
    else:
        return "https://lichess1.org/game/export/gif/black/" + gameid + ".gif?theme=brown&piece=alpha"

# create gifs from lichess links rather than passing in game ids


def createGifsByGameLink(link, side):
    if ('https://lichess.org/' not in link):
        return "error!"
    else:
        if (side == 'white'):
            id = link.split('/')
            actualID = id[3]
            return "https://lichess1.org/game/export/gif/white/" + actualID + ".gif?theme=brown&piece=alpha"
        else:
            blackid = link.split('/')
            blackactualID = blackid[3]
            return "https://lichess1.org/game/export/gif/black/" + blackactualID + ".gif?theme=brown&piece=alpha"


print(createSimpleGifById('hi', 'white'))
print(createGifsByGameLink("https://lichess.org/4184QjKy/black", "black"))
