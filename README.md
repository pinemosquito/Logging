# Logging

## 

```

setting the logging severity level
setting the file to log messages to
setting the format of the log messages

   # Create the Logger
    self.logger = logging.getLogger(__name__)
    self.logger.setLevel(logging.WARNING)
 
    # Create the Handler for logging data to a file
    logger_handler = logging.FileHandler('python_logging.log')
    logger_handler.setLevel(logging.WARNING)
 
    # Create a Formatter for formatting the log messages
    logger_formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
 
    # Add the Formatter to the Handler
    logger_handler.setFormatter(logger_formatter)
 
    # Add the Handler to the Logger
    self.logger.addHandler(logger_handler)
    self.logger.info('Completed configuring logger()!')
    
```
