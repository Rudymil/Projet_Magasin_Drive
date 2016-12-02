'''
Created on 27 mars 2015

@author: eleve
'''

import metier.gestion as ges
import os

def readCommande(commande):
    '''
    Création d'une liste d'articles à partir d'un fichier .txt de commandes avec en première ligne le numéro de commande et en ensuite en ligne Quantité et articles
    '''
    
    try :
        ls = []
        i  = 0
        com = open("{}.txt".format(commande),"r")
        com.readline() # Pour ne pas prendre le numero de commande
        com.readline() # Pour ne pas prendre la reference du client
        ch = com.readline()
        while ch != "":
            splitCh = ch.split('\n')
            ls.append(splitCh[0])
            ch = com.readline()
            i += 1
        return(ls)
    except :
        raise
    finally :
        com.close()
        
def readIdClient(commande):
    '''
    Création d'une liste d'articles à partir d'un fichier .txt de commandes avec en première ligne le numéro de commande et en ensuite en ligne Quantité et articles
    '''
    try :
        com = open("{}.txt".format(commande),"r")
        com.readline() # Pour ne pas prendre le numero de commande
        idCli = com.readline() # Pour récupere la reference du client
        return(idCli)
    except :
        raise
    finally :
        com.close()
                
def estPayee(commande): 
    '''
    Passe l'attribut payee d'une commande de False à True
    '''
    commande.payee = True
    ges.sauvegardeModifComPayee(commande)
    
def nonPayee(commande): 
    '''
    Passe l'attribut payee d'une commande de True à False
    '''
    commande.payee = False
    ges.sauvegardeModifComPayee(commande)
    
def estPrete(commande): 
    '''
    Passe l'attribut prete d'une commande de False à True
    '''
    commande.prete = True
    ges.sauvegardeModifComPrete(commande)
    
def nonPrete(commande): 
    '''
    Passe l'attribut prete d'une commande de True à False
    '''
    commande.prete = False
    ges.sauvegardeModifComPrete(commande)
    
def estRetiree(commande): 
    '''
    Passe l'attribut retiree d'une commande de False à True
    '''
    commande.retiree = True
    ges.sauvegardeModifComRetiree(commande)

def nonRetiree(commande): 
    '''
    Passe l'attribut retiree d'une commande de True à False
    '''
    commande.payee = False
    ges.sauvegardeModifComRetiree(commande)
    
def nombreArtOk(lsa):
    '''
    Fonction qui verifie si le nombre d'article d'une commande n'est pas trop important
    ''' 
    lsa_split =[]      
    for i in range (0,len(lsa)):
        elem = lsa[i].split(' ')
        lsa_split.append(elem)
    for j in range(0,len(lsa)):
        nb = int(lsa_split[j][2])
        if nb>150:
            return False
    return True

def nombreComOk(ddr):
    '''
    Fonction qui verifie si le nombre de commande avec une meme heure de retrait n'est pas trop important
    ''' 
    nb = ges.commandeNb(ddr)
    if nb>20:
        return False
    return True

def creerIt(Chariot):
    '''
    Fonction qui cree un fichier sous format texte qui presente l'itineraire que doit suivre l'employee
    '''
    try :
        com = open("itineraire_{}.txt".format(Chariot.numero),"w")
        os.remove("itineraire_{}.txt".format(Chariot.numero))
        com = open("itineraire_{}.txt".format(Chariot.numero),"w")
        com.write("            ---    VOICI L'ITINERAIRE DU CHARIOT {} :     ---\n\n".format(Chariot.numero))
        lsr = Chariot.lsr
        lsc = Chariot.lsc
        for ray in lsr:
            com.write("\n")
            com.write("----------------------------------------------------------------------------------------------------\n")
            com.write("Rayon n°{} :\n".format(ray))
            for elem in lsc:
                com.write("\n")
                lsa = ges.artByCom(str(elem),str(ray))
                com.write("  Commande n°{} : \n ".format(elem))
                for art in lsa:
                    ref = art[1]
                    qt=ges.qtByCom(elem, ref)
                    com.write("                  {} X {} \n ".format(art[0],qt))
                com.write("\n")
    except :
        raise
    finally :
        com.close()