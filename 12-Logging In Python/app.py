import logging

logger = logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler("app1.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("ArithmeticApp")

def add(a,b):
    result = a + b
    logger.debug(f"Addition {a} + {b} = {result}")
    return result

def sub(a,b):
    result = a - b
    logger.debug(f"Subtraction {a} - {b} = {result}")
    return result
def multiply(a,b):
    result = a * b
    logger.debug(f"Addition {a} * {b} = {result}")
    return result
def div(a,b):
    try:
        result = a / b
        logger.debug(f"Division {a} / {b} = {result}")
        return result
    except ZeroDivisionError:
        logger.error("Division by Zero")
        return None
    
add(10,15)
sub(15,10)
multiply(10,10)
div(12,6)
div(23,0)