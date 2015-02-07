'''
Created on Jan 9, 2013

@author: Ming
'''
import logging
import os


class LoggerFactory(object):
    '''
    Refactor at July, 2013.
    Updates:
        1. Support custom logging method for Svoice bridge. Custom logging send formatted log to port 7299.
        
    Useage:
        1. Get logger:
            > import LoggerFactory
            > logger = LoggerFactory.getLogger(logger_name)
            
        2. Common logging:
            > logger.debug()
            > logger.info()
            > logger.warning() / logger.warn()
            > logger.error()
            > logger.exception()
            > logger.critical() / logger.fatal()
            > logger.log()
        
        3. Svoice custom logging, supports 2 types of log, "strlog" and "metric". 6 methods available for custom logging:
           For "strlog" logging:
                > logger.strlog.gauge("gauge", 1)
                > logger.strlog.timing("timing", 2)
                > logger.strlog.set("set", 3)
                > logger.strlog.counter("counter", 4)
                > logger.strlog.increment("increment", 5)
                > logger.strlog.decrement("decrement", 6)
           
           For "metric" logging:
                > logger.metric.gauge("gauge", 1)
                > logger.metric.timing("timing", 2)
                > logger.metric.set("set", 3)
                > logger.metric.counter("counter", 4)
                > logger.metric.increment("increment", 5)
                > logger.metric.decrement("decrement", 6)
            
            
    '''

    def __init__(self):
        '''
        Constructor
        '''

    @staticmethod
    def getLogger(logger_name):
        autoops_handlers = AutoopsLoggerFactory.getHandler()
        rm_handlers = RMLoggerFactory.getHandler()
        # Dont use memory logger handler.
        rm_memory_handler = RMMemoryLoggerFactory.getHandler()
        logger = PortalLogger(logger_name, autoops_handlers, rm_handlers)
        return logger


    pass


class PortalLogger(object):

    def __init__(self, logger_name=None, *args):
        self.logger = logging.getLogger(logger_name)
        if len(args) > 0:
            for arg in args:
                if type(arg) is list:
                    for handler in arg:
                        self.logger.addHandler(handler)
                else:
                    self.logger.addHandler(arg)

    def debug(self, msg, *args, **kwargs):
        self.logger.debug(msg, *args, **kwargs)

    def info(self, msg, *args, **kwargs):
        self.logger.info(msg, *args, **kwargs)
        pass

    def warning(self, msg, *args, **kwargs):
        self.logger.warning(msg, *args, **kwargs)

    warn = warning

    def error(self, msg, *args, **kwargs):
        self.logger.error(msg, *args, **kwargs)

    def exception(self, msg, *args):
        self.logger.exception(msg, *args)

    def critical(self, msg, *args, **kwargs):
        self.logger.critical(msg, *args, **kwargs)

    fatal = critical

    def log(self, level, msg, *args, **kwargs):
        self.logger.log(level, msg, *args, **kwargs)

    def getRecords(self):
        logPath = '/var/log/rm.log'
        if os.path.exists(logPath):
            logFile = open(logPath)
            fileLines = logFile.readlines()
            result = ""
            for line in fileLines:
                result = result + line
            return result
        else:
            return "logs not exists"

    def flushRecords(self):
        #if self.autoops_logger:
        #    logPath = '/var/log/autoops.log'
        #    if os.path.exists(logPath):
        #        logFile = open(logPath)
        #        logFile.truncate()
        logPath = '/var/log/rm.log'
        if os.path.exists(logPath):
            logFile = open(logPath, 'w')
            logFile.truncate()

    # Custom 'strlog' & 'metric' log functions for Svoice

    @staticmethod
    def getCustomLogger(custom_logger_name):
        custom_logger = None

        try:
            from infrastructure.plugin.svoicelogger.SvoiceLoggerFactory import SvoiceLoggerFactory

            if custom_logger_name == "strlog":
                custom_logger = SvoiceLoggerFactory.getLogger('strlog')
            elif custom_logger_name == "metric":
                custom_logger = SvoiceLoggerFactory.getLogger('metric')
            pass

        except Exception, e:
            logging.error("Cannot create custom '%s' logger! Cannot find 'SvoiceLoggerFactory' ! ERROR: %s" % (custom_logger_name, str(e)))

        return custom_logger

    class strlog(object):

        @classmethod
        def info(cls, msg):
            custom_logger = PortalLogger.getCustomLogger(cls.__name__)
            if custom_logger:
                custom_logger.info(msg)
            pass

        @classmethod
        def gauge(cls, msg, v):
            custom_logger = PortalLogger.getCustomLogger(cls.__name__)
            if custom_logger:
                custom_logger.gauge(msg, v)
            pass

        @classmethod
        def timing(cls, msg, v):
            custom_logger = PortalLogger.getCustomLogger(cls.__name__)
            if custom_logger:
                custom_logger.timing(msg, v)
            pass

        @classmethod
        def set(cls, msg, v):
            custom_logger = PortalLogger.getCustomLogger(cls.__name__)
            if custom_logger:
                custom_logger.set(msg, v)
            pass

        @classmethod
        def counter(cls, msg, v):
            custom_logger = PortalLogger.getCustomLogger(cls.__name__)
            if custom_logger:
                custom_logger.counter(msg, v)
            pass

        @classmethod
        def increment(cls, msg, v):
            custom_logger = PortalLogger.getCustomLogger(cls.__name__)
            if custom_logger:
                custom_logger.increment(msg, v)
            pass

        @classmethod
        def decrement(cls, msg, v):
            custom_logger = PortalLogger.getCustomLogger(cls.__name__)
            if custom_logger:
                custom_logger.decrement(msg, v)
            pass

        pass

    class metric(strlog):
        '''
        Inherited from [Class]::PortalLogger.strlog
        '''
        pass
