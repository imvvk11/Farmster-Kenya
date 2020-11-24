import logging
import time

logger = logging.getLogger(__name__.split('.')[0])


def timing(f):
    def wrap(*args):
        time1 = time.time()
        ret = f(*args)
        time2 = time.time()
        logger.debug('{:s} function took {:.5f} seconds'.format(f.__name__, (time2-time1)))

        return ret
    return wrap
