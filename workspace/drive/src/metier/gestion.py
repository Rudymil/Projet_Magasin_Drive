'''
Module contenant les fonctions de connexion à une base de données

@author: eleve
'''

import bdd.accesBdd as bdd
import metier.exceptions as exceptions
from psycopg2 import DatabaseError

#---------------------Utile pour Client-----------------------------#

def sauvegardeClient(Client):
    '''
    Sauvegarde un client dans la base de données
    '''
    nom1 = Client.nom
    prenom1 = Client.prenom
    if nom1 != "" and prenom1!="":
        (cur, conn) = bdd.ouvrirConnexion()
        try:
            bdd.executerReq(cur, "INSERT INTO clients (nom, prenom)\
             VALUES (%s, %s);",(nom1, prenom1))
            bdd.validerModifs(conn)
        except Exception:
            raise
        finally:
            bdd.fermerConnexion(cur, conn)
    else:
        raise exceptions.ExceptionEntreeVide()
          
def supprClient(Client):
    '''
    Supprime un client dans la base de données
    '''
    nom = Client.nom
    prenom = Client.prenom
    cur, conn = bdd.ouvrirConnexion()
    bdd.executerReq(cur, "SELECT id FROM clients WHERE nom=%s AND prenom=%s;",(nom, prenom))
    id_Cli = cur.fetchone()
    if id_Cli != None :
        bdd.executerReq(cur, "DELETE FROM clients WHERE id=%d;" % (int(id_Cli[0]),))
        bdd.validerModifs(conn)
    bdd.fermerConnexion(cur, conn)
        
def sauvegardeClientmodif(Client1,Client2):
    '''
    Sauvegarde les modifications apportées à un client dans la base de données
    '''
    nom1 = Client1.nom
    prenom1 = Client1.prenom
    nom2 = Client2.nom
    prenom2 = Client2.prenom
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

def visCli():
    '''
    Affiche dans le terminal la liste des clients présents dans la base de données
    '''
    (cur, conn) = bdd.ouvrirConnexion()
    try:
        bdd.executerReq(cur, "SELECT * FROM clients;")
        for cli in cur:
            for i in range(0,len(cli)):
                print(cli[i])
            print('---------')
        bdd.validerModifs(conn)
    except DatabaseError:
            raise
    finally:
        bdd.fermerConnexion(cur, conn)
        
def visUnCli(Client):
    '''
    Affiche dans le terminal un client spécifique présents dans la base de données
    '''
    nom = Client.nom
    prenom = Client.prenom  
    (cur, conn) = bdd.ouvrirConnexion()  
    try:
        bdd.executerReq(cur, "SELECT * FROM clients WHERE nom=%s AND prenom=%s;",(nom, prenom))
        for cli in cur:
            for i in range(0,len(cli)):
                print(cli[i])
            print('---------')
        bdd.validerModifs(conn)
    except DatabaseError:
            raise
    finally:
        bdd.fermerConnexion(cur, conn)
        
def verifComCli(Client,Commande):
    '''
    Verifie qu'une commande a bien était passées par Client
    '''
    nom = Client.nom
    prenom = Client.prenom
    numero = Commande.numero
    pk = None
    if nom != "" and prenom !="" and numero != "":
        (cur, conn) = bdd.ouvrirConnexion()
        try:
            bdd.executerReq(cur, "SELECT id FROM clients WHERE nom = %s AND prenom = %s;",(nom, prenom))
            id_cli = cur.fetchone()
            bdd.executerReq(cur, "SELECT idc,idcli FROM commandes_clients WHERE idc=%s AND idcli=%s;",(numero,id_cli))
            pk = cur.fetchone()
        except DatabaseError:
            raise
        finally:
            bdd.fermerConnexion(cur, conn)
            return pk != None

def payementAJour(Client):
    '''
    Retroune la liste des attriubts payee des commadnes passées par un client
    '''
    nom = Client.nom
    prenom = Client.prenom
    ls = list()
    if nom != "" and prenom !="":
        (cur, conn) = bdd.ouvrirConnexion()
        try:
            bdd.executerReq(cur, "SELECT id FROM clients WHERE nom = %s AND prenom = %s;",(nom, prenom))
            id_cli = cur.fetchone()
            bdd.executerReq(cur, "SELECT commandes.payee FROM commandes,clients,commandes_clients \
            WHERE commandes.numero=commandes_clients.idc\
            AND commandes_clients.idcli=clients.id\
            AND clients.id = %s;",(id_cli))
            for pay in cur:
                ls.append(pay)
        except DatabaseError:
            raise
        finally:
            bdd.fermerConnexion(cur, conn)
            return ls
    
def retraitAJour(Client):
    '''
    Retroune la liste des attriubts retiree des commadnes passées par un client
    '''
    nom = Client.nom
    prenom = Client.prenom
    ls = list()
    if nom != "" and prenom !="":
        (cur, conn) = bdd.ouvrirConnexion()
        try:
            bdd.executerReq(cur, "SELECT id FROM clients WHERE nom = %s AND prenom = %s;",(nom, prenom))
            id_cli = cur.fetchone()
            bdd.executerReq(cur, "SELECT commandes.retiree FROM commandes,clients,commandes_clients \
            WHERE commandes.numero=commandes_clients.idc\
            AND commandes_clients.idcli=clients.id\
            AND clients.id = %s AND commandes.prete=True;",(id_cli))
            for pay in cur:
                ls.append(pay)
        except DatabaseError:
            raise
        finally:
            bdd.fermerConnexion(cur, conn)
            return ls
        
def historiqueCommande(Client):
    '''
    Retorune la liste des commandes passées par un client
    '''
    nom = Client.nom
    prenom = Client.prenom
    ls = list()
    if nom != "" and prenom !="":
        (cur, conn) = bdd.ouvrirConnexion()
        try:
            bdd.executerReq(cur, "SELECT id FROM clients WHERE nom = %s AND prenom = %s;",(nom, prenom))
            id_cli = cur.fetchone()
            bdd.executerReq(cur, "SELECT commandes.numero,commandes.ddc,commandes.ddr FROM commandes,clients,commandes_clients \
            WHERE commandes.numero=commandes_clients.idc\
            AND commandes_clients.idcli=clients.id\
            AND clients.id = %s;",(id_cli))
            for pay in cur:
                for ele in pay:
                    ls.append(str(ele))
        except DatabaseError:
            raise
        finally:
            bdd.fermerConnexion(cur, conn)
            return ls
        
#---------------------Utile pour Commande-----------------------------#

def supprCommande(Commande):
    '''
    Supprime si elle existe une commande de la base de données
    '''
    numero = Commande.numero
    cur, conn = bdd.ouvrirConnexion()
    id_Com = numero
    if id_Com != None :
        bdd.executerReq(cur, "DELETE FROM commandes WHERE numero=%d;" % (int(id_Com[0])))
        bdd.validerModifs(conn)
    bdd.fermerConnexion(cur, conn)
    
def sauvegardeModifComPrete(Commande):
    '''
    Sauvegarde dans la base de données les modifications apportées à l'attribut prete d'une commande
    '''
    prete = Commande.prete
    numero = Commande.numero
    if prete !="":
        (cur, conn) = bdd.ouvrirConnexion()
        try:
            bdd.executerReq(cur, "UPDATE commandes SET prete=%s\
            WHERE numero = %s;",(prete,numero))
            bdd.validerModifs(conn)
        except Exception:
            raise
        finally:
            bdd.fermerConnexion(cur, conn)
    else:
        raise exceptions.ExceptionEntreeVide()

def sauvegardeModifComPayee(Commande):
    '''
    Sauvegarde dans la base de données les modifications apportées à l'attribut payee d'une commande
    '''
    payee = Commande.payee
    numero = Commande.numero
    if payee != "" :
        (cur, conn) = bdd.ouvrirConnexion()
        try:
            bdd.executerReq(cur, "UPDATE commandes SET payee=%s\
            WHERE numero = %s;",(payee, numero))
            bdd.validerModifs(conn)
        except Exception:
            raise
        finally:
            bdd.fermerConnexion(cur, conn)
    else:
        raise exceptions.ExceptionEntreeVide()
        
def sauvegardeModifComRetiree(Commande):
    '''
    Sauvegarde dans la base de données les modifications apportées à l'attribut retiree d'une commande
    '''
    retiree = Commande.retiree
    numero = Commande.numero
    if retiree!="":
        (cur, conn) = bdd.ouvrirConnexion()
        try:
            bdd.executerReq(cur, "UPDATE commandes SET retiree=%s\
            WHERE numero = %s;",(retiree,numero))
            bdd.validerModifs(conn)
        except Exception:
            raise
        finally:
            bdd.fermerConnexion(cur, conn)
    else:
        raise exceptions.ExceptionEntreeVide()

def enregistrerCommande(Commande):
    '''
    Sauvegarde une commmande ans la base de données
    '''
    ddc = Commande.ddc
    ddr = Commande.ddr
    if ddc!="" and ddr!="":
        ddcSplit = ddc.split('/')
        ddrSplit = ddr.split('-')
        (cur, conn) = bdd.ouvrirConnexion()
        try:
            bdd.executerReq(cur, "INSERT INTO commandes (ddc,ddr,poids,volume) \
            VALUES (to_date('%s/%s/%s', 'DD/MM/YYYY'),to_date('%s/%s/%s', 'DD/MM/YYYY'),%s,%s);",(int(ddcSplit[0]),int(ddcSplit[1]),int(ddcSplit[2]),int(ddrSplit[2]),int(ddrSplit[1]),int(ddrSplit[0]),Commande.poids,Commande.volume))
            bdd.validerModifs(conn)
        except Exception:
            raise
        finally:
            bdd.fermerConnexion(cur, conn)
    else:
        raise exceptions.ExceptionEntreeVide()
    
def visCom():
    '''
    Affiche dans le terminal la liste des commandes présentes dans la base de données
    '''
    (cur, conn) = bdd.ouvrirConnexion()
    try:
        bdd.executerReq(cur, "SELECT * FROM commandes;")
        for com in cur:
            for i in range(0,len(com)):
                print(com[i])
            print('---------')
        bdd.validerModifs(conn)
    except DatabaseError:
            raise
    finally:
        bdd.fermerConnexion(cur, conn)
        
def visUnCom(Commande):
    '''
    Affiche dans le terminal la liste une commande spécifique présents dans la base de données
    '''
    numero = Commande.numero  
    (cur, conn) = bdd.ouvrirConnexion()  
    try:
        bdd.executerReq(cur, "SELECT * FROM commandes WHERE numero = %s;",(numero))
        for cli in cur:
            for i in range(0,len(cli)):
                print(cli[i])
            print('---------')
        bdd.validerModifs(conn)
    except DatabaseError:
            raise
    finally:
        bdd.fermerConnexion(cur, conn)
        
def creerListeCommandesEnAttente():
    '''
    Retorune la liste des comandes(numeros,poids,volume) qui ne sont pas encore traité (dont l'attribut prete en à False)
    '''
    (cur, conn) = bdd.ouvrirConnexion()   
    try:
            bdd.executerReq(cur, "SELECT numero, poids ,volume FROM commandes \
                                WHERE prete=False \
                                ORDER BY ddc;")
            lca = []
            for com in cur:
                lca.append(com)
            bdd.validerModifs(conn)
    except DatabaseError:
        raise
    finally:
        return lca
        bdd.fermerConnexion(cur, conn) 
    
#---------------------Utile pour Article-----------------------------#
    
def enregistrerArticle(Article):
    '''
    Sauvegarde un article dans la base de données
    '''
    nom = Article.nom
    poids = Article.poids
    volume = Article.volume
    if nom != "" and poids!="" and volume!="":
        (cur, conn) = bdd.ouvrirConnexion()
        try:
            bdd.executerReq(cur, "INSERT INTO articles (nom ,poids , volume) \
            VALUES (%s,%s,%s);",(nom, poids, volume))
            bdd.validerModifs(conn)
        except Exception:
            raise
        finally:
            bdd.fermerConnexion(cur, conn)
    else:
        raise exceptions.ExceptionEntreeVide()
  
def supprimerArticle(Article):
    '''
    Supprime si il existe un article dans la base de données
    '''
    nom = Article.nom
    poids = Article.poids
    volume = Article.volume
    if nom!="" and poids!="" and volume!="" :
        (cur, conn) = bdd.ouvrirConnexion()
        bdd.executerReq(cur, "SELECT reference FROM articles WHERE nom=%s AND poids=%s AND volume=%s;",(nom, poids, volume))  
        id_Art = cur.fetchone()
        if id_Art != None :
            bdd.executerReq(cur, "DELETE FROM articles WHERE reference=%d;" % (int(id_Art[0])))
            bdd.validerModifs(conn)
        bdd.fermerConnexion(cur, conn)
        
def poidsArticle(ref):
    '''
    Retourne le poids d'un article
    '''
    (cur, conn) = bdd.ouvrirConnexion()
    try:
        bdd.executerReq(cur, "SELECT poids FROM articles WHERE reference=%s;",(ref,))
        poids = cur.fetchone()
        if poids == None :
            raise Exception("Article non present")
        bdd.validerModifs(conn)
    except DatabaseError:
            raise
    finally:
        bdd.fermerConnexion(cur, conn)
    return poids

def volumeArticle(ref):
    '''
    Retourne le volume d'un article
    '''
    (cur, conn) = bdd.ouvrirConnexion()
    try:
        bdd.executerReq(cur, "SELECT volume FROM articles WHERE reference=%s;",(ref,))
        vol = cur.fetchone()
        if vol == None :
            raise Exception("Article non present")
        bdd.validerModifs(conn)
    except DatabaseError:
            raise
    finally:
        bdd.fermerConnexion(cur, conn)
    return vol

def visArt():
    '''
    Affiche dans le terminal la liste des artilces présents dans la base de données
    '''
    (cur, conn) = bdd.ouvrirConnexion()
    try:
        bdd.executerReq(cur, "SELECT * FROM articles;")
        for com in cur:
            for i in range(0,len(com)):
                print(com[i])
            print('---------')
        bdd.validerModifs(conn)
    except DatabaseError:
            raise
    finally:
        bdd.fermerConnexion(cur, conn)
        
def visUnArt(Article):
    '''
    Affiche dans le terminal la liste un article spécifique présent dans la base de données
    '''
    reference = Article.reference  
    (cur, conn) = bdd.ouvrirConnexion()  
    try:
        bdd.executerReq(cur, "SELECT * FROM articles WHERE reference = %s;",(reference))
        for cli in cur:
            for i in range(0,len(cli)):
                print(cli[i])
            print('---------')
        bdd.validerModifs(conn)
    except DatabaseError:
            raise
    finally:
        bdd.fermerConnexion(cur, conn)
        
#---------------------Utile pour les liens entre les tables-----------------------------#
        
def remplirCommandes_Articles(commande):
    '''
    Remplir la table de liens commandes_articles à partir d'un objet Commande   
    '''
    (cur, conn) = bdd.ouvrirConnexion()  
    idc = commande.numero
    try:
        for elem in commande.lsa :
            splitelem = elem.split(' ')
            ida = splitelem[0]
            qte = splitelem[2]
            bdd.executerReq(cur, "INSERT INTO commandes_articles (idc,ida,quantite) VALUES (%s,%s,%s);",(idc, ida, qte))
            bdd.validerModifs(conn)
    except DatabaseError:
        raise
    finally:
        bdd.fermerConnexion(cur, conn)
        
def remplirCommandes_Clients(commande,idcli):
    '''
    Remplir la table de liens commandes_clients à partir d'un objet commande
    '''
    (cur, conn) = bdd.ouvrirConnexion()  
    idc = commande.numero
    try:
            bdd.executerReq(cur, "INSERT INTO commandes_clients (idc,idcli) VALUES (%s,%s);",(idc, idcli))
            bdd.validerModifs(conn)
    except DatabaseError:
        raise
    finally:
        bdd.fermerConnexion(cur, conn)  
              
def creerListeItineraire(ls):
    '''
    Retorune la liste des rayons des articles présents dans ls
    '''
    result =[]
    for com in ls:
        (cur, conn) = bdd.ouvrirConnexion()
        try:
            bdd.executerReq(cur, "SELECT distinct articles.rayon  FROM articles, commandes_articles \
                        WHERE articles.reference = commandes_articles.ida \
                        AND commandes_articles.idc = %s ORDER BY articles.rayon;",(com,))
            for ray in cur:
                if ray[0] not in result:
                    result.append(ray[0])                
        except DatabaseError:
            raise
        finally:
            bdd.fermerConnexion(cur, conn)    
    result.sort()
    return result       
         
def commandeNb(ddr):
    '''
    Retouren le nombre de commande ayant la même date de retrait que Commande
    '''
    ls = list()
    if ddr !="":
        (cur, conn) = bdd.ouvrirConnexion()
        try:
            bdd.executerReq(cur, "SELECT numero FROM commandes WHERE ddr=%s;",(ddr))
            for pay in cur:
                ls.append(pay)
        except DatabaseError:
            raise
        finally:
            bdd.fermerConnexion(cur, conn)
            return len(ls)

def artByCom(numero,rayon):
    '''
    Récupére la liste des articles étant présent dans la commande(numero) et dans le rayon(rayon)
    '''
    ls = list()
    if numero !="":
        (cur, conn) = bdd.ouvrirConnexion()
        try:
            
            bdd.executerReq(cur, "SELECT articles.nom, articles.reference FROM articles,commandes_articles \
            WHERE commandes_articles.idc = %s \
            AND   commandes_articles.ida = articles.reference \
            AND   articles.rayon= %s;",(numero,rayon))
            for elem in cur:
                ls.append(elem)
        except DatabaseError:
            raise
        finally:
            bdd.fermerConnexion(cur, conn)
            return ls
        
def cliByCom(numero):
    '''
    Récupére les informations sur un client à partir du numero d'une commande
    '''
    ls = list()
    if numero !="":
        (cur, conn) = bdd.ouvrirConnexion()
        try:
            bdd.executerReq(cur, "SELECT clients.nom,clients.prenom FROM clients,commandes_clients\
            WHERE commandes_clients.idc = %s\
            AND clients.id = commandes_clients.idcli;",(str(numero)))
            for elem in cur:
                ls.append(elem)
        except DatabaseError:
            raise
        finally:
            bdd.fermerConnexion(cur, conn)
            return ls
        
def qtByCom(numero,reference):
    '''
    Récupére la quantité d'un article(refence) présent dans la commande(numero)
    '''
    qtt = 0
    if numero !="":
        (cur, conn) = bdd.ouvrirConnexion()
        try:
            bdd.executerReq(cur, "SELECT commandes_articles.quantite FROM commandes_articles \
            WHERE  commandes_articles.idc= %s AND commandes_articles.ida= %s;",(numero,reference))
            qtt = cur.fetchone()
        except DatabaseError:
            raise
        finally:
            bdd.fermerConnexion(cur, conn)
            return qtt[0]