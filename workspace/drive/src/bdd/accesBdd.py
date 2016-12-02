'''
Module regroupant l'ensemble des fonctions permettant la connexion a une base de donnee

@author: eleve
'''

import psycopg2
import bdd.exceptions as excpBdd

#conf = configparser.ConfigParser()
#import os
#print(os.getcwd())
#conf.read('./connect_bdd.conf') # déploiement
#conf.read('../../connect_bdd.conf') # tests
#host = conf['serveur']['Host']
#port = conf['serveur']['Port']
#dbname = conf['base']['DBname']
#user = conf['utilisateur']['User']
#password = keyring.get_password(host+"_"+dbname, user)

host = 'localhost'     #'valilab.ensg.eu'
port = '5432'
dbname = 'db_hugo'
user = 'hugo'
password = 'hugo'


def ouvrirConnexion():
    """
    Connexion à une base de données
    """
    conn = psycopg2.connect("host=%s port=%s dbname=%s user=%s password=%s" % (host,port,dbname,user,password))
    # création d'un curseur pour accéder à cette base
    cur = conn.cursor()
    return (cur, conn)
    
def executerReq(cur, req, variables=None):
    """ 
    Requête à la base de données
    """
    try:
        cur.execute(req, variables)
    except psycopg2.DataError as de:
        raise excpBdd.ExceptionFormatInadequat() from de
    except psycopg2.IntegrityError as ie:
        raise excpBdd.ExceptionContrainte() from ie
    
def validerModifs(conn):
    conn.commit()
    
    
def fermerConnexion(cur, conn):
    """
    Fermeture de la connexion
    """
    cur.close()
    conn.close()
    
if __name__ == "__main__" :
    (cur, conn) = ouvrirConnexion()
    fermerConnexion(cur, conn)