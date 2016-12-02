'''
Module contenant les fonctions de connexion à la base de donnees utile à l'ihm

@author: eleve
'''
import bdd.accesBdd as bdd
import metier.exceptions as exceptions
import metier.trajet as traj
import metier.utilitaire as util
from psycopg2 import DatabaseError

def sauvegardeClient(nom,prenom):
    '''
    Sauvegarde un client dans la base de donnees à l'aide du nom et du prenom du client
    '''
    if nom != "" and prenom!="":
        (cur, conn) = bdd.ouvrirConnexion()
        try:
            bdd.executerReq(cur, "INSERT INTO clients (nom, prenom)\
             VALUES (%s, %s);",(nom, prenom))
            bdd.validerModifs(conn)
        except Exception:
            raise
        finally:
            bdd.fermerConnexion(cur, conn)
    else:
        raise exceptions.ExceptionEntreeVide()
        
def modifClient(nom1,prenom1,nom2,prenom2):
    '''
    Modifie le client (nom1,prenom1) si il existe en client(nom2,prenom2)
    '''
    if nom1 != "" and prenom1 !="" and nom2 !="" and prenom2 !="":
        (cur, conn) = bdd.ouvrirConnexion()
        try:
            bdd.executerReq(cur, "SELECT id FROM clients WHERE nom = %s AND prenom = %s;",(nom1, prenom1))
            id_cli1 = cur.fetchone()
            if id_cli1!=None:
                    bdd.executerReq(cur, "UPDATE clients SET nom = %s,prenom=%s \
                    WHERE nom = %s AND prenom = %s;",(nom2, prenom2, nom1, prenom1))
            bdd.validerModifs(conn)
        except Exception:
            raise
        finally:
            bdd.fermerConnexion(cur, conn)
    else:
        raise exceptions.ExceptionEntreeVide()
        
def listeClient():
    '''
    Retourne la liste des clients présents dans la base de données
    '''
    (cur, conn) = bdd.ouvrirConnexion()
    lst = list()
    try:
        bdd.executerReq(cur, "SELECT * FROM clients;")
        for cli in cur:
            for i in range(0,len(cli)):
                lst.append(cli[i])
        bdd.validerModifs(conn)
    except DatabaseError:
            raise
    finally:
        bdd.fermerConnexion(cur, conn)
    return lst

def listeArt():
    '''
    Retourne la liste des articles présents dans la base de données
    '''
    (cur, conn) = bdd.ouvrirConnexion()
    lst = list()
    try:
        bdd.executerReq(cur, "SELECT * FROM articles;")
        for cli in cur:
            for i in range(0,len(cli)):
                lst.append(cli[i])
        bdd.validerModifs(conn)
    except DatabaseError:
            raise
    finally:
        bdd.fermerConnexion(cur, conn)
    return lst

def listeCom():
    '''
    Retourne la liste des commandes présentes dans la base de données
    '''
    (cur, conn) = bdd.ouvrirConnexion()
    lst = list()
    try:
        bdd.executerReq(cur, "SELECT * FROM commandes;")
        for cli in cur:
            for i in range(0,len(cli)):
                lst.append(cli[i])
        bdd.validerModifs(conn)
    except DatabaseError:
            raise
    finally:
        bdd.fermerConnexion(cur, conn)
    return lst

def creerIti(numero, poids, volume):
    '''
    Focntion qui crée l'itinéraire sous format texte d'un itinéraire pour le chariot(numero,poids,volume)
    '''
    char = traj.Chariot(int(numero),int(poids),int(volume))
    util.creerIt(char)
