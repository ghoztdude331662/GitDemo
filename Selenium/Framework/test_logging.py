import logging


#wrap this in a method

def test_loggingDemo():


    logger=logging.getLogger(__name__)   #object creation and name will print test method name

    fileHandler=logging.FileHandler('logfile.log')#path for file
    formatter=logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s") #for formatting text
    fileHandler.setFormatter(formatter) #passing format to file handler ,so that logger can access
    logger.addHandler(fileHandler) #determines what file and format and file handler object


    logger.setLevel(logging.INFO)
#level of each logs.More the level of log,it will print other logs after
#for instance, we put warning,it will print warning,error,critical
    logger.debug("Used for printing")
    logger.info("used for info")
    logger.warning("used for alerts")
    logger.error("used for error")
    logger.critical("used for critical")


