'''
Module gérant les execptions de connexion à la base de donnees

@author: eleve
'''


class ExceptionContrainte(Exception):
    '''
    Gere les execptions de contraintes
    '''


    def __init__(self, message = None):
        '''
        Constructor
        '''
        super().__init__(message)


class ExceptionFormatInadequat(Exception):
    '''
    Gere les execptions de format inadequat
    '''


    def __init__(self, message = None):
        '''
        Constructor
        '''
        super().__init__(message)