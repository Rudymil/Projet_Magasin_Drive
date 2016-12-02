'''
Module contenant les classes Artcile et Commande

@author: eleve
'''

import metier.utilitaire as util
import metier.gestion as ges
import datetime
   
class Article(object):
    '''
    Classe definissant un article
    
    Elle possede comme attributs :
    reference -- la reference de l'article
    nom -- le nom de l'article
    poids -- le poids de l'article
    volume -- le vilume de l'article
    
    La reference, le nom, le poids et le volume doivent etre passe au constructeur
    '''


    def __init__(self, reference, nom, poids, volume, **kwargs):
        '''
        Constructor
        '''
        super().__init__(**kwargs)
        self._reference = reference
        self._nom = nom
        self._poids = poids
        self._volume = volume
        
    @property
    def reference(self):
        return self._reference

    @reference.setter
    def reference(self,a):
        self._reference = a
        
    @property
    def nom(self):
        return self._nom

    @nom.setter
    def nom(self,a):
        self._nom = a
        
    @property
    def poids(self):
        return self._poids

    @poids.setter
    def poids(self,a):
        self._poids = a
        
    @property
    def volume(self):
        return self._volume

    @volume.setter
    def volume(self,a):
        self._volume = a
        
    def __str__(self):
        return ('%s, %s, %s, %s' % (self.reference,self.nom,self.poids,self.volume))
    
class Commande(object):
    '''
    Classe definissant une commande
    
    Elle possede comme attributs :
    numero -- le numero de la commande
    ddc -- la date de creation de la commande
    ddr -- la date de retrait de la commande
    prete -- booleen savoir si la commande est prete ou non
    payee -- booleen savoir si la commande est payee ou non
    retiree -- booleen savoir si la commande est retiree ou non
    lsa -- la liste des articles composant la comande
    
    Le numero, la ddc, le lsa et le volume doivent etre passe au constructeur
    '''


    def __init__(self, numero, ddc, lsa, **kwargs):
        '''
        Constructor
        '''
        super().__init__(**kwargs)
        self._numero = numero
        self._ddc = ddc
        self._prete = False
        self._retiree = False
        self._payee = False
        self._lsa = lsa
        self._ddr = self.defDdr()
        self._poids = self.calculerPoids()
        self._volume = self.calculerVolume()
        
        
    @property
    def numero(self):
        return self._numero

    @numero.setter
    def numero(self,a):
        self._numero = a
        
    @property
    def ddc(self):
        return self._ddc

    @ddc.setter
    def ddc(self,a):
        self._ddc = a
        
    @property
    def ddr(self):
        return self._ddr

    @ddr.setter
    def ddr(self,a):
        self._ddr = a
        
    @property
    def prete(self):
        return self._prete

    @prete.setter
    def prete(self,a):
        self._prete = a
        
    @property
    def retiree(self):
        return self._retiree

    @retiree.setter
    def retiree(self,a):
        self._retiree = a
        
    @property
    def payee(self):
        return self._payee

    @payee.setter
    def payee(self,a):
        self._payee = a
        
    @property
    def lsa(self):
        return self._lsa

    @lsa.setter
    def lsa(self,a):
        self._lsa = a
        
    @property
    def poids(self):
        return self._poids

    @poids.setter
    def poids(self,p):
        self._poids = p
    
    @property
    def volume(self):
        return self._volume

    @volume.setter
    def volume(self,v):
        self._volume = v
        
    def __str__(self):
        ch = ""
        for art in self.lsa :
            ch = ch + str(art)
            ch = ch + '/'
        return ('%s, %s, %s, %s, %s, %s, %s' % (self.numero,self.ddc,self.ddr,self.prete,self.retiree,self.payee,ch))
   
    def calculerPoids(self):
        '''
        Calcul le poids d'une commande. Cette fonction est utilisé dans le constructeur de la classe
        '''
        lsart = self.lsa
        lsart_split =[]      
        for i in range (0,len(lsart)):
            elem = lsart[i].split(' ')
            lsart_split.append(elem)
        Ptotal = 0
        for j in range(0,len(lsart)):
            nb = int(lsart_split[j][2])
            ref = lsart_split[j][0]
            poids = ges.poidsArticle(ref)
            Ptotal = Ptotal + nb*poids[0]      
        return Ptotal    
            
    def calculerVolume(self):
        '''
        Calcul le volume d'une commande. Cette fonction est utilisé dans le constructeur de la classe
        '''
        lsart = self.lsa
        lsart_split =[]     
        for i in range (0,len(lsart)):
            elem = lsart[i].split(' ')
            lsart_split.append(elem)
        Vtotal = 0
        for j in range(0,len(lsart)):
            nb = int(lsart_split[j][2])
            ref = lsart_split[j][0]
            vol = ges.volumeArticle(ref)
            Vtotal = Vtotal + nb*vol[0]     
        return Vtotal 
    
    def defDdr(self):
        '''
        Calcul la date de retrait d'une commande. Cette fonction est utilisé dans le constructeur de la classe
        '''
        ddc = self.ddc
        lsa = self.lsa
        nbTot = 0
        ddcSplit = ddc.split('/')
        ddcDate = datetime.date(int(ddcSplit[2]),int(ddcSplit[1]),int(ddcSplit[0]))
        lsa_split =[]      
        for i in range (0,len(lsa)):
            elem = lsa[i].split(' ')
            lsa_split.append(elem)
        for j in range(0,len(lsa)):
            nb = int(lsa_split[j][2])
            nbTot = nbTot +nb
        if nbTot<=10:
            ddp = ddcDate + datetime.timedelta(days=3)
        elif nbTot<=30:
            ddp = ddcDate + datetime.timedelta(days=4)
        elif nbTot<=50:
            ddp = ddcDate + datetime.timedelta(days=5)
        elif nbTot<=60:
            ddp = ddcDate + datetime.timedelta(days=6)
        elif nbTot<=70:
            ddp = ddcDate + datetime.timedelta(days=7)
        else:
            ddp = ddcDate + datetime.timedelta(days=9)
        while util.nombreComOk(ddp)==False:
            ddp = ddp + datetime.timedelta(days=1)
        return str(ddp)

if __name__ == "__main__" :
    #art1 = Article('0002','Banane','1','1')
    #art2 = Article('0005','Coca 6*33','1,8','2')
    #print(art1)
    #print(art2)
    #ls = util.readCommande('commande')
    #print(ls)
    #co1 = Commande('5','24/05/2015',ls)
    #print(co1)
    #ges.enregistrerArticle(art1)
    #ges.enregistrerCommande(co1)
    #ges.supprimerArticle(art1)
    #util.estPrete(co1)
    #util.defDdr(co1,'12/05/2015')
    #ges.remplirCommandes_Articles(co1)
    #idcli1=util.readIdClient('commande')
    #ges.remplirCommandes_Clients(co1,idcli1)
    
    ls1 = util.readCommande('commande_01')
    if util.nombreArtOk(ls1):
        co1 = Commande('1','10/02/2015',ls1)
        ges.enregistrerCommande(co1)
        ges.remplirCommandes_Articles(co1)
        idcli1 = util.readIdClient('commande_01')
        ges.remplirCommandes_Clients(co1,idcli1)
        util.estPayee(co1)
    
    ls2 = util.readCommande('commande_02')
    if util.nombreArtOk(ls2):
        co_2 = Commande('2','24/02/2015',ls2)
        ges.enregistrerCommande(co_2)
        ges.remplirCommandes_Articles(co_2)
        idcli2 = util.readIdClient('commande_02')
        ges.remplirCommandes_Clients(co_2,idcli2)
        util.estPayee(co_2)
    
    ls3 = util.readCommande('commande_03')
    if util.nombreArtOk(ls3):
        co_3 = Commande('3','02/03/2015',ls3)
        ges.enregistrerCommande(co_3)
        ges.remplirCommandes_Articles(co_3)
        idcli3 = util.readIdClient('commande_03')
        ges.remplirCommandes_Clients(co_3,idcli3)
    
    ls4 = util.readCommande('commande_04')
    if util.nombreArtOk(ls4):
        co_4 = Commande('4','13/03/2015',ls4)
        ges.enregistrerCommande(co_4)
        ges.remplirCommandes_Articles(co_4)
        idcli4 = util.readIdClient('commande_04')
        ges.remplirCommandes_Clients(co_4,idcli4)
        util.estPayee(co_4)
    
    ls5 = util.readCommande('commande_05')
    if util.nombreArtOk(ls5):
        co_5 = Commande('5','24/03/2015',ls5)
        ges.enregistrerCommande(co_5)
        ges.remplirCommandes_Articles(co_5)
        idcli5 = util.readIdClient('commande_05')
        ges.remplirCommandes_Clients(co_5,idcli5)
        util.estPayee(co_5)
    
    ls6 = util.readCommande('commande_06')
    if util.nombreArtOk(ls6):
        co_6 = Commande('6','26/03/2015',ls6)
        ges.enregistrerCommande(co_6)
        ges.remplirCommandes_Articles(co_6)
        idcli6 = util.readIdClient('commande_06')
        ges.remplirCommandes_Clients(co_6,idcli6)
    
    ls7 = util.readCommande('commande_07')
    if util.nombreArtOk(ls7):
        co_7 = Commande('7','01/04/2015',ls7)
        ges.enregistrerCommande(co_7)
        ges.remplirCommandes_Articles(co_7)
        idcli7 = util.readIdClient('commande_07')
        ges.remplirCommandes_Clients(co_7,idcli7)
        util.estPayee(co_7)
    

    
