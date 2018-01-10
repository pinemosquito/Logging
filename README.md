# Logging

## Python has a built-in library called logging
to log program's execution to file

```
    import logging
    
    # Create the ###logger with __name__
    # Set logging severity level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.WARNING)
 
    # Create file Handler for logging messages (WARNING, DEBUG) to file python_logging
    fh = logging.FileHandler('python_logging.log')
    fh.setLevel(logging.WARNING)
 
    # Create a Formatter for formatting the log messages
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
 
    # Add the Formatter to the Handler
    fh.setFormatter(formatter)
 
    # Add the Handler to the Logger
    logger.addHandler(fh)
    logger.info('Completed configuring logger()!')
    
```
