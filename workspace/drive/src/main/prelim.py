'''
Module a lancer en premier pour crééer la base de données pour les tests

@author: eleve
'''

import test.gestionBdd as gBdd
import metier.produit as prod
import metier.utilitaire as util
import metier.gestion as ges

if __name__ == "__main__" : 
    
    gBdd.creation()
    
    ls1 = util.readCommande('commande_01')
    if util.nombreArtOk(ls1):
        co1 = prod.Commande('1','10/02/2015',ls1)
        ges.enregistrerCommande(co1)
        ges.remplirCommandes_Articles(co1)
        idcli1 = util.readIdClient('commande_01')
        ges.remplirCommandes_Clients(co1,idcli1)
        util.estPayee(co1)
    
    ls2 = util.readCommande('commande_02')
    if util.nombreArtOk(ls2):
        co_2 = prod.Commande('2','24/02/2015',ls2)
        ges.enregistrerCommande(co_2)
        ges.remplirCommandes_Articles(co_2)
        idcli2 = util.readIdClient('commande_02')
        ges.remplirCommandes_Clients(co_2,idcli2)
        util.estPayee(co_2)
    
    ls3 = util.readCommande('commande_03')
    if util.nombreArtOk(ls3):
        co_3 = prod.Commande('3','02/03/2015',ls3)
        ges.enregistrerCommande(co_3)
        ges.remplirCommandes_Articles(co_3)
        idcli3 = util.readIdClient('commande_03')
        ges.remplirCommandes_Clients(co_3,idcli3)
    
    ls4 = util.readCommande('commande_04')
    if util.nombreArtOk(ls4):
        co_4 = prod.Commande('4','13/03/2015',ls4)
        ges.enregistrerCommande(co_4)
        ges.remplirCommandes_Articles(co_4)
        idcli4 = util.readIdClient('commande_04')
        ges.remplirCommandes_Clients(co_4,idcli4)
        util.estPayee(co_4)
    
    ls5 = util.readCommande('commande_05')
    if util.nombreArtOk(ls5):
        co_5 = prod.Commande('5','24/03/2015',ls5)
        ges.enregistrerCommande(co_5)
        ges.remplirCommandes_Articles(co_5)
        idcli5 = util.readIdClient('commande_05')
        ges.remplirCommandes_Clients(co_5,idcli5)
        util.estPayee(co_5)
    
    ls6 = util.readCommande('commande_06')
    if util.nombreArtOk(ls6):
        co_6 = prod.Commande('6','26/03/2015',ls6)
        ges.enregistrerCommande(co_6)
        ges.remplirCommandes_Articles(co_6)
        idcli6 = util.readIdClient('commande_06')
        ges.remplirCommandes_Clients(co_6,idcli6)
    
    ls7 = util.readCommande('commande_07')
    if util.nombreArtOk(ls7):
        co_7 = prod.Commande('7','01/04/2015',ls7)
        ges.enregistrerCommande(co_7)
        ges.remplirCommandes_Articles(co_7)
        idcli7 = util.readIdClient('commande_07')
        ges.remplirCommandes_Clients(co_7,idcli7)
        util.estPayee(co_7)