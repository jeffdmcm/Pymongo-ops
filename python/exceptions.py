
class Error(Exception):
   """Base class for other exceptions"""
   pass


class InvalidEnvironmentError(Error):
    '''
    Raised when referencing an invalid environment
    Environment must be one of: 'sandbox', 'qa-graphql', 'production'
    '''
    pass


class InvalidDBError(Error):
    '''
    Raised when Mongo connection isnt successful
    '''
    pass
