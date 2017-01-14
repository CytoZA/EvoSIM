import logging;

class object:
    id
    logger
    name
    location

    def __init__(self, logger, id):
        self.logger = logger or logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)
        logger.info("Begin")
        self.id = id;
        logger.info("End")

    def printObject(self):
        self.logger.info(self.__class__+": printObject(): Begin")
        print("Object[ID:"+self.id+",Name:"+self.name+",Location:"+self.location)
        self.logger.info(self.__class__ + ": printObject(): End")