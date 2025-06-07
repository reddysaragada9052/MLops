import logging
logging.basicConfig(
    filename= "logs",
    filemode="w",
    format="%(asctime)s-%(name)s-%(levelname)s-%(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    level= logging.DEBUG
    )