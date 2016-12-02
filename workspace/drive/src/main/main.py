'''
Module créant un itinéraire avec bdd défini par main.prelim (lancer prelim avant main)

@author: eleve
'''
import metier.trajet as traj
import metier.utilitaire as util

newchariot = traj.Chariot(18,175,175)
util.creerIt(newchariot)