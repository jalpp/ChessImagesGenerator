# this file contains methods that generate chess board images from FEN

# create gif images from fens

def createImageByGif(fen):
    return "https://lichess1.org/export/fen.gif?fen" + "=" + fen

# create png images from fens


def createImageByPng(fen):
    return "https://chessboardimage.com/" + fen + ".png"
