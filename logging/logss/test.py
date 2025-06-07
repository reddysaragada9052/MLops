from logger import logging

def sum(a, b):
    logging.debug("Sum function is taking place....")

    return a+b
logging.debug("function is called successfully")
sum(1,2)