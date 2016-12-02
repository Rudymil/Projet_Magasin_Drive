'''
Module gérant les exceptions propres à metier

@author: eleve
'''

class ExceptionEntreeVide(Exception):
    '''
    Gére les exceptions d'entree vide
    '''


    def __init__(self, message = None):
        '''
        Constructor
        '''
        super().__init__(message)