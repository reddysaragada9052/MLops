import logging
logging.basicConfig(
    format="%(asctime)s-%(name)s-%(levelname)s-%(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    level= logging.DEBUG,
    handlers= [
        logging.FileHandler("app1.log"),
        logging.StreamHandler()
    ]
    )

logger = logging.getLogger("ArithmaticApp")

def sum(a, b):
    result = a+b
    logger.debug(f" Sum of {a} & {b} = {result}")
    return result

def subtract(a,b):
    result = a - b
    logger.debug(f"subtraction of {a} & {b} = {result}")

    return result

def mul(a,b):
    result = a*b
    logger.debug(f"multiple of {a} & {b} = {result}")
    return result


sum(1,2)
subtract(2,3)
mul(4,5)