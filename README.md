# Logging

## Python has a built-in library called logging
Python enables a **standardized** and **flexibile** framework for logging a program's execution

To emit a log message, a caller first requests a __name__ logger.

This logger can be used to emit messages at different log levels (DEBUG, INFO, WARNING, ERROR, CRITICAL)


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
    logger.info('Creating an instance of log')
    
    # close and remove handler
    filehandler.close()
    logger.removeHandler(filehandler)
    
```

### 2018-01-10 11:06:09,464 - __main__ - INFO - creating an instance of log
