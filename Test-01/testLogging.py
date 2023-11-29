import logging.config
import yaml
from typing import Callable

def function_call_tracking_decorator(function: Callable[[str], None]):
    def wrapper_accepting_arguments(*args):
        print('Function arguments are:')
        for arg in args:
            print(arg)
        function(*args)
    return wrapper_accepting_arguments

@function_call_tracking_decorator
def testFunction(myMode:str) -> None:
    myLogger = logging.getLogger(myMode) 

    # Log some messages
    myLogger.debug('This is a debug message')
    myLogger.info('This is an info message')
    myLogger.warning('This is a warning message')
    myLogger.error('This is an error message')
    myLogger.critical('This is a critical message')
   
def main():
    # Load the config file
    print('Loading config file ...')
    with open('loggingDef.yaml', 'rt') as f:
        config = yaml.safe_load(f.read())

    # Configure the logging module with the config file
    logging.config.dictConfig(config)

    myModes: list[str] = ['development','staging','production', 123]

    try:
        for i in myModes:
           testFunction(i) 
        testFunction(12345)
    except:
        print("An exception occurred")
    

main()