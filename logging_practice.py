"""Logging means recording information about what is happening inside the program
It is useful for degugging,monitoring,and finding errors in applications
Instead of using only print(),we can use Python built-in logging module"""

import logging
logging.basicConfig(filename="app.log",level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")
logging.debug("Debug information")#Used for detailed information while debugging.
logging.info("Program Started") #Used for normal program information.
logging.warning("This is a warning")#Something unexpected may happen
logging.error("Something went wrong")#Used when something goes wrong.
logging.critical("System crashed")#Used for very serious problems.

#print:Mainly displays information on the console.
"""Logging:show messages on the console
         save messages to files
         include timestamps"""

# Debugging means finding and fixing errors (bugs) in a program.

