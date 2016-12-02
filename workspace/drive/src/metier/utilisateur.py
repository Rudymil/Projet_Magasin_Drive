'''
Module contenant les classes Personnel et Client

@author: eleve
'''

import metier.exceptions as exceptions
import metier.gestion as ges
import metier.produit as prod
import datetime


class Personnel(object):
    '''
    Classe definissant un personnel
    
    Elle possede comme attributs :
    nom -- le nom de la personne
    prenom -- le prenom de la personne
    
    Le nom et le prenom doivent etre passe au constructeur
    '''


    def __init__(self, nom, prenom, **kwargs):
        '''
        Constructor
        '''
        super().__init__(**kwargs)
        self._nom = nom
        self._prenom = prenom
        
    @property
    def nom(self):
        return self._nom

    @nom.setter
    def nom(self,a):
        self._nom = a
        
    @property
    def prenom(self):
        return self._prenom

    @prenom.setter
    def prenom(self,a):
        self._prenom = a
        
    def __str__(self):
        return ('%s, %s' % (self.nom, self.prenom))

    def ajouterClient(self,nom, prenom):
        '''
        Ajoute un client dans la base de données
        '''
        if nom != "" and prenom!=""  :
            cli1 = Client('%s' % (nom),'%s' % (prenom))
            ges.sauvegardeClient(cli1)

    def supprimerClient(self,nom, prenom):
        '''
        Supprime si il existe un client dans la base de données
        '''
        if nom != "" and prenom!="":
            cli1 = Client('%s' % (nom),'%s' % (prenom))
            ges.supprClient(cli1)
            
    def modifierClient(self,nom1, prenom1, nom2, prenom2):
        '''
        Modifie si il existe un client(nom1,prenom1) en (nom2,prenom2) dans la base de données
        '''
        if nom1 != "" and prenom1 !=""and nom2 !="" and prenom2 !="":
            cli1 = Client('%s' % (nom1),'%s' % (prenom1))
            cli2 = Client('%s' % (nom2),'%s' % (prenom2))
            ges.sauvegardeClientmodif(cli1,cli2)
            
    def voirListeCommandes(self):
        '''
        Affiche dans le terminal la liste des commandes présentes dans la base de données
        '''
        ges.visCom()
        
    def visualiserCommande(self,numero):
        '''
        Affiche dans le terminal la liste une commande spécifique présente dans la base de données
        '''
        cli1 = prod.Commande('%s' % (numero),None,None)
        ges.visUnCom(cli1)
        
    def voirListeClients(self):
        '''
        Affiche dans le terminal la liste des clients présents dans la base de données
        '''
        ges.visCli()
    
    def visualiserClient(self,nom,prenom):
        '''
        Affiche dans le terminal la liste un client spécfiique présent dans la base de données
        '''
        cli1 = Client('%s' % (nom),'%s' % (prenom))
        ges.visUnCli(cli1)
  
    def voirListeArticles(self):
        '''
        Affiche dans le terminal la liste des articles présents dans la base de données
        '''
        ges.visArt()
        
    def visualiserArticle(self,reference):
        '''
        Affiche dans le terminal la liste un article spécifique présent dans la base de données
        '''
        cli1 = prod.Article('%s' % (reference),None,None,None)
        ges.visUnArt(cli1)
    
class Client(object):
    '''
    Classe definissant un client
    
    Elle possede comme attributs :
    nom -- le nom du client
    prenom -- le prenom du client
    
    Le nom et le prenom doivent etre passe au constructeur
    '''


    def __init__(self, nom, prenom, **kwargs):
        '''
        Constructor
        '''
        super().__init__(**kwargs)
        self._nom = nom
        self._prenom = prenom
        
    @property
    def nom(self):
        return self._nom

    @nom.setter
    def nom(self,a):
        self._nom = a
        
    @property
    def prenom(self):
        return self._prenom

    @prenom.setter
    def prenom(self,a):
        self._prenom = a
        
    def __str__(self):
        return ('%s, %s' % (self.nom, self.prenom))

    def annulerCommande(self,numero): 
        '''
        Annule une commande si i s'agit bien d'une commande passée par le client
        '''
        if numero != "":
            com1 = prod.Commande('%s' % (numero),'','')
            prs = ges.verifComCli(self, com1)
            if prs:
                ges.supprCommande(com1)
                
    def estAJourPaiement(self):
        '''
        Vérfie que le client est à jour de ses paiements
        '''
        ls = ges.payementAJour(self)
        for pay in ls:
            if pay[0]==False:
                return False
        return True
    
    def estAJourRetrait(self):
        '''
        Vérfie que le client est à jour de ses retraits
        '''
        ls = ges.retraitAJour(self)
        for pay in ls:
            if pay[0]==False:
                return False
        return True
    
    def historiqueCom(self):
        '''
        Retorune la liste des commandes passées par le client
        '''
        ls = ges.historiqueCommande(self)
        return ls

if __name__ == "__main__" :
    pers1 = Personnel("BALTZ", "Hugo")
    print(pers1)
    pers1.nom = "Dujardin"
    pers1.prenom = "Jean"
    print(pers1)
    #pers1.ajouterClient('TEST', 'Marcel')
    #pers1.supprimerClient('TEST', 'Marcel')
    #pers1.modifierClient('TEST','Marcel','TROP','Cool')
    #pers1.voirListeCommandes()
    #pers1.voirListeClients()
    #pers1.voirListeArticles()
    #pers1.visualiserClient('MILLET', 'Rudolf')
    #pers1.visualiserArticle('2')
    #pers1.visualiserCommande('2')
    #com = prod.Commande('1','24/05/2015','')
    cli = Client('DUPONCHEL','Gauthier')
    #t = ges.verifComCli(cli, com)
    #print(t)
    #cli.annulerCommande('1')
    pay=cli.estAJourPaiement()
    print(pay)
    ret = cli.estAJourRetrait()
    print(ret)
    his = cli.historiqueCom()
    print(his)
    print(his[0][1])
    print(his[0])
    
