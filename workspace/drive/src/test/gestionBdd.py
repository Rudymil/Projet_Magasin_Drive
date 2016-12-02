'''
Module gérant la création et la suppresion des tables dans la base de données

@author: eleve
'''

import bdd.accesBdd as bdd
#from pbkdf2 import crypt

def creation():
    '''
    Crée les différentes tables dans la base de données
    '''
    cur, conn = bdd.ouvrirConnexion()
    
    # articles
    bdd.executerReq(cur, "CREATE TABLE articles (\
                        reference    serial CONSTRAINT pk_art PRIMARY KEY,\
                        nom          varchar(50) NOT NULL,\
                        poids        float NOT NULL,\
                        volume       float NOT NULL,\
                        rayon        int NOT NULL\
                    );")
    
    # commandes
    bdd.executerReq(cur, "CREATE TABLE commandes (\
                        numero    serial CONSTRAINT pk_com PRIMARY KEY ,\
                        ddc       date NOT NULL,\
                        ddr       date,\
                        prete     boolean DEFAULT False,\
                        retiree   boolean DEFAULT False,\
                        payee     boolean DEFAULT False,\
                        poids     float,\
                        volume     float\
                    );")
    
    
    # commandes_articles (table de liens entre les commandes et les articles)
    bdd.executerReq(cur, "CREATE TABLE commandes_articles (\
                        idc       int,\
                        ida       int,\
                        quantite  int,\
                        PRIMARY KEY (idc,ida),\
                        FOREIGN KEY (idc) REFERENCES commandes (numero),\
                        FOREIGN KEY (ida) REFERENCES articles (reference)\
                    );")
        
    # clients
    bdd.executerReq(cur, "CREATE TABLE clients (\
                        id        serial CONSTRAINT pk_cli PRIMARY KEY ,\
                        nom       varchar(50) NOT NULL,\
                        prenom    varchar(50) NOT NULL\
                    );")
    
    
    # commandes_clients (table de liens entre les commandes et les clients)
    bdd.executerReq(cur, "CREATE TABLE commandes_clients (\
                        idc       int ,\
                        idcli     int,\
                        PRIMARY KEY (idc,idcli),\
                        FOREIGN KEY (idc) REFERENCES commandes (numero),\
                        FOREIGN KEY (idcli) REFERENCES clients (id)\
                    );")
    
    
    # Insertions articles:
    bdd.executerReq(cur, "INSERT INTO articles (nom, poids, volume, rayon) VALUES\
                        ('vodka smirnoff', 1, 1.3, 1),\
                        ('whisky ballantines', 0.75, 1, 1),\
                        ('vin nuit saint georges', 1, 0.75, 1),\
                        ('vin chateau margaux', 1, 0.75, 1),\
                        ('vin chablis', 1, 0.75, 1),\
                        ('vin gevrey chambertin', 1, 0.75, 1),\
                        ('coca 6x33cL', 1.8, 2, 2),\
                        ('orangina 6x33cL', 1.8, 2, 2),\
                        ('oasis 2L', 2, 2, 2),\
                        ('volvic 6x1,5L', 9, 10, 3),\
                        ('evian 6x1,5L', 9, 10, 3),\
                        ('perrier 6x1,5L', 9, 10, 3),\
                        ('lait', 1, 1, 4),\
                        ('beurre', 0.25, 0.2, 5),\
                        ('activia 12x125g', 1, 1.2, 5),\
                        ('danette chocolat 8x125g', 1.875, 1.2, 5),\
                        ('pain 500g', 0.5, 0.8, 6),\
                        ('spaghetti 500g', 0.5, 0.5, 7),\
                        ('penne rigate 500g', 0.5, 0.7, 7),\
                        ('riz basmati', 1, 1, 7),\
                        ('sucre en poudre', 1, 1, 7),\
                        ('farine', 1, 1, 7),\
                        ('pommes de terre 10kg', 10, 10, 8),\
                        ('pommes de terre 2,5kg', 2.5, 2.5, 8),\
                        ('oranges filet 3kg', 3, 3, 9),\
                        ('lessive omo', 4, 3.5, 10),\
                        ('head & shoulders', 0.4, 0.3, 11)\
                    ;")
    
    # Insertions clients:
    bdd.executerReq(cur, "INSERT INTO clients (nom, prenom) VALUES\
                        ('DUPONCHEL', 'Gauthier') ,\
                        ('BALTZ', 'Hugo') ,\
                        ('MILLET', 'Rudolf'),\
                        ('DURAND', 'Pierre'),\
                        ('MOREAU', 'Jeanne'),\
                        ('LEDOYEN', 'Virginie'),\
                        ('BRASSEUR', 'Pierre'),\
                        ('HENO', 'Raphaele'),\
                        ('LEBRUN', 'Pierre')\
                    ;")
    
    bdd.validerModifs(conn)
    bdd.fermerConnexion(cur, conn)
    
    
def suppression():
    '''
    Supprime les différentes tables dans la base de données
    '''
    cur, conn = bdd.ouvrirConnexion()
   
    
    # commandes_clients
    bdd.executerReq(cur, "DROP TABLE commandes_clients;")
    # clients
    bdd.executerReq(cur, "DROP TABLE clients;")
    # commandes_articles
    bdd.executerReq(cur, "DROP TABLE commandes_articles;")
    # commandes
    bdd.executerReq(cur, "DROP TABLE commandes;")
    # articles
    bdd.executerReq(cur, "DROP TABLE articles;") 
    
    
    bdd.validerModifs(conn)
    bdd.fermerConnexion(cur, conn)

if __name__ == "__main__":
    creation()
    #suppression()