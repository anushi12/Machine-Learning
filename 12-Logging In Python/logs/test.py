from logger import logging

def addition(a,b):
    logging.debug("the addition operation is taking place")
    return a + b

logging.debug("addition function is called")
addition(10,15)