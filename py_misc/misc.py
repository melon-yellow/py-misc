##########################################################################################################################
#                                                         REFERENCE                                                      #
##########################################################################################################################

# Get Miscellaneous Reference
def misc():
    import py_misc
    return py_misc

# Reference to Miscellaneous
class Misc:
    @property
    def misc(self): return misc()
    @property
    def __locale__(self):
        return self.misc.locale(self)

##########################################################################################################################
#                                                         REFERENCE                                                      #
##########################################################################################################################
