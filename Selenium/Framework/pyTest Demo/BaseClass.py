import inspect
import logging


class BaseClass:
    def getLogger(self):
        loggername=inspect.stack()[1][3]#to print the exact method during inheritance
        logger = logging.getLogger(loggername)  # object creation and name will print test method name
        fileHandler = logging.FileHandler('logfile.log')  # path for file
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")  # for formatting text
        fileHandler.setFormatter(formatter)  # passing format to file handler ,so that logger can access
        logger.addHandler(fileHandler)  # determines what file and format and file handler object
        logger.setLevel(logging.DEBUG)

        return logger