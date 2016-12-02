'''
Module servant à faire des tests unitaires

@author: eleve
'''
import unittest

import test.gestionBdd

import metier.utilitaire as util
import metier.gestion as ges
import metier.produit as prod
import metier.trajet as traj
import metier.utilisateur as utilisateur
import datetime

class Test(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        test.gestionBdd.creation()
    
    @classmethod
    def tearDownClass(cls):
        test.gestionBdd.suppression()
        
    def testInsertCommandes(self):
        ls1 = util.readCommande('commande_01')
        print(ls1)
        co1 = prod.Commande('1','10/02/2015',ls1)
        print(co1)
        ges.enregistrerCommande(co1)
        ges.remplirCommandes_Articles(co1)
        idcli1 = util.readIdClient('commande_01')
        ges.remplirCommandes_Clients(co1,idcli1)
    
        ls2 = util.readCommande('commande_02')
        co_2 = prod.Commande('2','24/02/2015',ls2)
        ges.enregistrerCommande(co_2)
        ges.remplirCommandes_Articles(co_2)
        idcli2 = util.readIdClient('commande_02')
        ges.remplirCommandes_Clients(co_2,idcli2)
    
        ls3 = util.readCommande('commande_03')
        co_3 = prod.Commande('3','02/03/2015',ls3)
        ges.enregistrerCommande(co_3)
        ges.remplirCommandes_Articles(co_3)
        idcli3 = util.readIdClient('commande_03')
        ges.remplirCommandes_Clients(co_3,idcli3)
    
        ls4 = util.readCommande('commande_04')
        co_4 = prod.Commande('4','13/03/2015',ls4)
        ges.enregistrerCommande(co_4)
        ges.remplirCommandes_Articles(co_4)
        idcli4 = util.readIdClient('commande_04')
        ges.remplirCommandes_Clients(co_4,idcli4)
    
        ls5 = util.readCommande('commande_05')
        co_5 = prod.Commande('5','24/03/2015',ls5)
        ges.enregistrerCommande(co_5)
        ges.remplirCommandes_Articles(co_5)
        idcli5 = util.readIdClient('commande_05')
        ges.remplirCommandes_Clients(co_5,idcli5)
    
        ls6 = util.readCommande('commande_06')
        co_6 = prod.Commande('6','26/03/2015',ls6)
        ges.enregistrerCommande(co_6)
        ges.remplirCommandes_Articles(co_6)
        idcli6 = util.readIdClient('commande_06')
        ges.remplirCommandes_Clients(co_6,idcli6)
    
        ls7 = util.readCommande('commande_07')
        print(ls7)
        co_7 = prod.Commande('7','01/04/2015',ls7)
        ges.enregistrerCommande(co_7)
        ges.remplirCommandes_Articles(co_7)
        idcli7 = util.readIdClient('commande_07')
        ges.remplirCommandes_Clients(co_7,idcli7)
        
    def insertClient(self):
        newclient = utilisateur.Client('BALMAND','Samuel')
    
           
    def creerChariot(self):
        newchariot = traj.Chariot(18,175,175)
        
if __name__ == "__main__":
    unittest.main()
    
