from os import mkdir
from os.path import exists, join


RES_FOLEDR = "res"
RES_BACKGROUND = join(RES_FOLEDR, "background.png")


def init_resources():
    if not exists(RES_FOLEDR):
        mkdir(RES_FOLEDR)