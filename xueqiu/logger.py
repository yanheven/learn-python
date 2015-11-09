__author__ = 'evan'
import  logging
import os

def get_loger():
    # create logger
    logger = logging.getLogger()
    logger.setLevel(logging.WARN)

    # create console handler and set level to debug
    ch = logging.StreamHandler()
    ch.setLevel(logging.WARN)

    # set log file
    file_path = os.path.split(os.path.realpath(__file__))[0]
    file = os.path.join(file_path,'xueqiu.log')
    fh = logging.FileHandler(file)
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