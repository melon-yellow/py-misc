
##########################################################################################################################

# Imports
from threading import Thread

# Modules
from ..call import Safe, Resolvable

##########################################################################################################################

# Daemon Class
class Daemon(Resolvable):

    # Init Daemon
    def __init__(self, function, start=True, log=True):
        # Check Parameters
        if (not callable(function) or
            not isinstance(log, bool) or
            not isinstance(start, bool)):
            self = False
            return None
        # Init Resolvable
        function = Safe(function, log)
        super().__init__(function, log)
        # Set Thread
        self.__thread__ = Thread(target=self.__callable__)
        self.__thread__.daemon = True
        # Start Thread
        if start: self.start()

    @property
    def start(self):
        return self.__thread__.start

    @property
    def is_alive(self):
        return self.__thread__.is_alive

    @property
    def join(self):
        return self.__thread__.join

##########################################################################################################################
