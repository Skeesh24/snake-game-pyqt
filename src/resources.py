from os import mkdir
from os.path import exists, join
from random import randint

RES_FOLEDR = "res"


def get_next_background():
    index = randint(1, 10)
    path = join(RES_FOLEDR, "map%d.jpg" % index)
    return path if exists(path) else join(RES_FOLEDR, "map%d.png" % index)


# =========== module initialization ===========
if not exists(RES_FOLEDR):
    mkdir(RES_FOLEDR)
