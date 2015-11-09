__author__ = 'evan'
import  logging

def get_loger():
    # create logger
    logger = logging.getLogger()
    logger.setLevel(logging.WARN)

    # create console handler and set level to debug
    ch = logging.StreamHandler()
    ch.setLevel(logging.WARN)

    # set log file
    fh = logging.FileHandler('xueqiu.log')
    fh.setLevel(logging.DEBUG)

    # create formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # add formatter to ch
    ch.setFormatter(formatter)
    fh.setFormatter(formatter)

    # add ch to logger
    logger.addHandler(ch)
    logger.addHandler(fh)

    # 'application' code
    logger.debug('initalized get logger')
    return logger