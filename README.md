# Logging

## Python has a built-in library called logging
to log program's execution to file

```
    import logging
    
    # Create the logger with __name__
    # Set logging severity level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.WARNING)
 
    # Create file handler for logging messages to file python_logging
    filehandler = logging.FileHandler('python_logging.log')
    filehandler.setLevel(logging.WARNING)
 
    # Create a Formatter for formatting the log messages
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
 
    # Add the Formatter to the Handler
    filehandler.setFormatter(formatter)
 
    # Add the Handler to the Logger
    logger.addHandler(filehandler)
    logger.info('Completed configuring logger()!')
    
    # close and remove handler
    filehandler.close()
    logger.removeHandler(filehandler)
```
