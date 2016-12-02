'''
Module ontenant la classe Chariot

@author: eleve
'''
import metier.gestion as ges
import metier.utilitaire as util
import metier.produit as prod
import metier.utilisateur as utr

class Chariot(object):
    '''
    Classe definissant un chariot
    
    Elle possede comme attributs :
    numero -- le numero du chariot
    poids -- le poids du chariot en kg
    volume -- le volume du chariot en L
    lsc -- la liste des numeros des commandes du chariot
    lsr -- la liste des rayons que le chariot devra visiter
    
    Le numero, la contenance et la doivent etre passe au constructeur
    '''
    
    def __init__(self, numero, poids, volume, **kwargs):
        '''
        Constructor
        '''
        super().__init__(**kwargs)
        self._numero = numero
        self._poids = poids
        self._volume = volume
        self._lsc = self.remplirChariot()
        self._lsr = self.creerItineraire()
        
    @property
    def numero(self):
        return self._numero

    @numero.setter
    def numero(self,a):
        self._numero = a
        
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
    
    @property
    def lsc(self):
        return self._lsc

    @lsc.setter
    def lsc(self,a):
        self._lsc = a
        
    @property
    def lsr(self):
        return self._lsr

    @lsr.setter
    def lsr(self,a):
        self._lsr = a
        
    def __str__(self):
        chcom = ' Liste des commandes : '
        for com in self._lsc :
            chcom = chcom + str(com)
            chcom = chcom + ' ; '
            
        chray = ' Liste des rayons : '
        for ray in self._lsr :
            chray = chray + str(ray)
            chray = chray + ' ; '    
        return ('%s / %s / %s / %s / %s' % (self.numero,self.poids,self.volume,chcom,chray))

    def remplirChariot(self):
        '''
        Methode de l'objet chariot.
        elle permet de remplir l'attribut lsc (liste des numero de commandes contenus dans l'objet chariot)
        '''
        lsc = []
        mch = self._poids
        vch = self._volume
        lsca = ges.creerListeCommandesEnAttente()
        i = 0
        #and mch>=0 and vch>=0
        while i<len(lsca) :
            lscli = ges.cliByCom(lsca[i][0]) 
            client = utr.Client(lscli[0][0],lscli[0][1])
            payee = client.estAJourPaiement()
            retiree = client.estAJourRetrait()
            if lsca[i][1]<=mch and lsca[i][2]<=vch and payee and retiree:
                lsc.append(lsca[i][0])
                co = prod.Commande (lsca[i][0],'17/04/2015','')
                util.estPrete(co)
                mch = mch - lsca[i][1]
                vch = vch - lsca[i][2]
            i+=1
        return lsc
        
    def creerItineraire(self):
        '''
        Methode de l'objet chariot.
        elle permet de remplir l'attribut lsr (liste des rayons à visiter par l'objet chariot
        '''
        lsc = self._lsc
        if len(lsc)!=0:
            return ges.creerListeItineraire(lsc)        
        else:
            return []        
  
if __name__ == "__main__" :  
        
    char2 = Chariot(18,175,175)
    
    #print(char2.lsc)
    #print(char2.lsr)  
    
    
    util.creerIt(char2)
    