##########################################################################################################################
#                                                          CALLABLE                                                      #
##########################################################################################################################

# Cyclic Reference
from .. import misc

##########################################################################################################################
#                                                          CALLABLE                                                      #
##########################################################################################################################

# Callable Class
class Callable(misc.Misc):

    # Init Callable
    def __init__(self, function):
        # Check Parameters
        if not callable(function):
            self = False
            return None
        # Nest Objects
        self.__callable__ = function

    @property
    def __proxy__(self):
        return self.__callable__

    @property
    def __locale__(self):
        return self.misc.locale(self)

##########################################################################################################################
#                                                          CALLABLE                                                      #
##########################################################################################################################
