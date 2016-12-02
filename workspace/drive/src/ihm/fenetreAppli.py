'''
Module gérant l'affichage de l'ihm

@author: eleve
'''

import tkinter
import tkinter.ttk as ttk
import tkinter.messagebox as messagebox

import ihm.utilitaire_ihm as util
import metier.exceptions as excpMetier
import bdd.exceptions as excpBdd

class FenetreAppli(tkinter.Tk):
    '''
    Fenêtre principale de l'application.
    '''


    def __init__(self, parent):
        '''
        Constructeur à partir de la fenêtre parente.
        '''
        super().__init__()
        self.parent = parent
        self.affiche()
        
        
        
    def affiche(self):
        self.title("Drive")
        
        cadreAffichage = ttk.Frame(self)
        cadreAffichage.pack(side=tkinter.TOP,fill=tkinter.BOTH, expand=0)
        
        # create a toplevel menu
        menubar = tkinter.Menu(self)

        # create a pulldown menu, and add it to the menu bar
        filemenu = tkinter.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Ajouter un client", command=lambda : self.ajouterClient(cadreAffichage))
        filemenu.add_command(label="Modifier un client", command=lambda : self.modifierClient(cadreAffichage))
        filemenu.add_command(label="Lister les clients", command=lambda : self.afficherClients(cadreAffichage))
        menubar.add_cascade(label="Gestion client", menu=filemenu)
        
        menubar.add_command(label="Lister les articles", command=lambda : self.afficherArticles(cadreAffichage))
        
        menubar.add_command(label="Lister les commandes", command=lambda : self.afficherCommandes(cadreAffichage))
        
        menubar.add_command(label="Créer un itinéraire", command=lambda : self.creerItineraire(cadreAffichage))
        
        menubar.add_command(label="Quitter", command=self.destroy)
        
        # display the menu
        self.config(menu=menubar)
        
        largeurEcran = self.winfo_screenwidth()
        hauteurEcran = self.winfo_screenheight()
        
            
        # self.overrideredirect(1) # pour supprimer titre et menus
        self.geometry("%dx%d+0+0" % (largeurEcran, hauteurEcran))

        #root.focus_set()
        self.mainloop()
        
        
    def ajouterClient(self,frame):
        '''
        Fonction gérant l'affichage du formulaire de l'ajout d'un client
        '''
        for child in frame.winfo_children():
                child.destroy()
                
        nom = tkinter.StringVar()
        prenom = tkinter.StringVar()
        
        nom_entry = ttk.Entry(frame, width=7, textvariable=nom)
        nom_entry.grid(column=1, row=2, sticky=(tkinter.W, tkinter.E))
        prenom_entry = ttk.Entry(frame, width=7, textvariable=prenom)
        prenom_entry.grid(column=2, row=2, sticky=(tkinter.W, tkinter.E))
        
        ttk.Label(frame, text="Nom").grid(column=1, row=1, sticky=tkinter.W)
        ttk.Label(frame, text="Prenom").grid(column=2, row=1, sticky=tkinter.W)
        
        ttk.Button(frame, text="Ajouter", command=lambda : self.ajoutCliEffectif(frame, nom.get(), prenom.get())).grid(column=1, row=3, sticky=tkinter.W)
        
        nom_entry.focus()
        self.bind('<Return>', lambda paraNonUtilise: self.ajoutCliEffectif(frame, nom.get(), prenom.get())) # le paramètre non utilisé est une instance de la classe Event
    
    def ajoutCliEffectif(self, frame, nom, prenom):
        '''
        Fonction qui ajoute un client à la base de donnees
        '''
        try:
            util.sauvegardeClient(nom,prenom)
            for child in frame.winfo_children():
                child.destroy()
            messConfirmation = tkinter.StringVar()
            ttk.Label(frame, textvariable=messConfirmation, foreground="dark green").grid(column=1, row=1, sticky=tkinter.W)
            messConfirmation.set("Le client %s a été ajouté." % (nom.upper(), ))
        except excpMetier.ExceptionEntreeVide:
            messagebox.showinfo(title="Champ(s) vide(s)", message="Le client n'a pu être ajouté", parent=self)
        except excpBdd.ExceptionFormatInadequat:
            messagebox.showinfo(title="Champ(s) trop long(s)", message="Le client n'a pu être ajouté", parent=self)
        frame.mainloop()

    def modifierClient(self,frame):
        '''
        Fonction gérant l'affichage du formulaire de la modification d'un client
        '''
        for child in frame.winfo_children():
                child.destroy()
                
        nom1 = tkinter.StringVar()
        prenom1 = tkinter.StringVar()
        nom2 = tkinter.StringVar()
        prenom2 = tkinter.StringVar()
        
        nom1_entry = ttk.Entry(frame, width=7, textvariable=nom1)
        nom1_entry.grid(column=1, row=2, sticky=(tkinter.W, tkinter.E))
        prenom1_entry = ttk.Entry(frame, width=7, textvariable=prenom1)
        prenom1_entry.grid(column=2, row=2, sticky=(tkinter.W, tkinter.E))
        
        nom2_entry = ttk.Entry(frame, width=7, textvariable=nom2)
        nom2_entry.grid(column=1, row=4, sticky=(tkinter.W, tkinter.E))
        prenom2_entry = ttk.Entry(frame, width=7, textvariable=prenom2)
        prenom2_entry.grid(column=2, row=4, sticky=(tkinter.W, tkinter.E))
        
        ttk.Label(frame, text="Ancien nom").grid(column=1, row=1, sticky=tkinter.W)
        ttk.Label(frame, text="Ancien prenom").grid(column=2, row=1, sticky=tkinter.W)
        
        ttk.Label(frame, text="Nouveau nom").grid(column=1, row=3, sticky=tkinter.W)
        ttk.Label(frame, text="Nouveau Prenom").grid(column=2, row=3, sticky=tkinter.W)
        
        ttk.Button(frame, text="Modifer", command=lambda : self.modifCliEffectif(frame, nom1.get(), prenom1.get(), nom2.get(), prenom2.get())).grid(column=1, row=5, sticky=tkinter.W)
        
        nom1_entry.focus()
        self.bind('<Return>', lambda paraNonUtilise: self.modifCliEffectif(frame, nom1.get(), prenom1.get(), nom1.get(), prenom1.get())) # le paramètre non utilisé est une instance de la classe Event
    
    def modifCliEffectif(self, frame, nom1, prenom1, nom2, prenom2):
        '''
        Fonction qui modifie un client à la base de donnees
        '''
        try:
            util.modifClient(nom1,prenom1, nom2, prenom2)
            for child in frame.winfo_children():
                child.destroy()
            messConfirmation = tkinter.StringVar()
            ttk.Label(frame, textvariable=messConfirmation, foreground="dark green").grid(column=1, row=1, sticky=tkinter.W)
            messConfirmation.set("Le client %s a été modifié." % (nom1.upper(), ))
        except excpMetier.ExceptionEntreeVide:
            messagebox.showinfo(title="Champ(s) vide(s)", message="Le client n'a pu être modifié", parent=self)
        except excpBdd.ExceptionFormatInadequat:
            messagebox.showinfo(title="Champ(s) trop long(s)", message="Le client n'a pu être modifié", parent=self)
        frame.mainloop() 
        
    def afficherClients(self,frame):
        '''
        Fonction qui affiche dans l'ihm les clients présents dans la base de donees
        '''
        for child in frame.winfo_children():
                child.destroy()
        lst = util.listeClient() 
        i = 1
        j = 2
        ttk.Label(frame, text="Reference").grid(column=1, row=1, sticky=tkinter.W)
        ttk.Label(frame, text="Nom").grid(column=2, row=1, sticky=tkinter.W)
        ttk.Label(frame, text="Prenom").grid(column=3, row=1, sticky=tkinter.W)
        for cli in lst:    
            ttk.Label(frame, text="%s"%(cli)).grid(column=i, row=j, sticky=tkinter.W)
            i +=1
            if i%3==1:
                j+=1
                i=1
                      
    def afficherArticles(self,frame):
        '''
        Fonction qui affiche dans l'ihm les articles présents dans la base de donees
        '''
        for child in frame.winfo_children():
                child.destroy()
        lst = util.listeArt() 
        ttk.Label(frame, text="Reference").grid(column=1, row=1, sticky=tkinter.W)
        ttk.Label(frame, text="Nom").grid(column=2, row=1, sticky=tkinter.W)
        ttk.Label(frame, text="Poids en kg").grid(column=3, row=1, sticky=tkinter.W)
        ttk.Label(frame, text="Volume en L").grid(column=4, row=1, sticky=tkinter.W)
        ttk.Label(frame, text="Rayon").grid(column=5, row=1, sticky=tkinter.W)
        i = 1
        j = 2
        for art in lst:    
            ttk.Label(frame, text="%s"%(art)).grid(column=i, row=j, sticky=tkinter.W)
            i +=1
            if i%5==1:
                j+=1
                i=1
                
    def afficherCommandes(self,frame):
        '''
        Fonction qui affiche dans l'ihm les commandes présents dans la base de donees
        '''
        for child in frame.winfo_children():
                child.destroy()
        lst = util.listeCom() 
        ttk.Label(frame, text="Numero").grid(column=1, row=1, sticky=tkinter.W)
        ttk.Label(frame, text="Date de commande").grid(column=2, row=1, sticky=tkinter.W)
        ttk.Label(frame, text="Date de retrait").grid(column=3, row=1, sticky=tkinter.W)
        ttk.Label(frame, text="Prete").grid(column=4, row=1, sticky=tkinter.W)
        ttk.Label(frame, text="Retiree").grid(column=5, row=1, sticky=tkinter.W)
        ttk.Label(frame, text="Payee").grid(column=6, row=1, sticky=tkinter.W)
        ttk.Label(frame, text="Poids en kg").grid(column=7, row=1, sticky=tkinter.W)
        ttk.Label(frame, text="Volume en L").grid(column=8, row=1, sticky=tkinter.W)
        i = 1
        j = 2
        for com in lst:    
            ttk.Label(frame, text="%s"%(com)).grid(column=i, row=j, sticky=tkinter.W)
            i +=1
            if i%8==1:
                j+=1
                i=1
    
    def creerItineraire(self,frame):
        '''
        Fonction gérant l'affichage du formulaire de la création d'un itnéraire
        '''
        for child in frame.winfo_children():
                child.destroy()
                
        numero = tkinter.StringVar()
        poids = tkinter.StringVar()
        volume = tkinter.StringVar()
        
        numero_entry = ttk.Entry(frame, width=7, textvariable=numero)
        numero_entry.grid(column=1, row=2, sticky=(tkinter.W, tkinter.E))
        poids_entry = ttk.Entry(frame, width=7, textvariable=poids)
        poids_entry.grid(column=2, row=2, sticky=(tkinter.W, tkinter.E))
        volume_entry = ttk.Entry(frame, width=7, textvariable=volume)
        volume_entry.grid(column=3, row=2, sticky=(tkinter.W, tkinter.E))
        
        ttk.Label(frame, text="Numero du chariot").grid(column=1, row=1, sticky=tkinter.W)
        ttk.Label(frame, text="Poids maximal du chariot").grid(column=2, row=1, sticky=tkinter.W)
        ttk.Label(frame, text="Volume maximal du chariot").grid(column=3, row=1, sticky=tkinter.W)
        
        ttk.Button(frame, text="Créer", command=lambda : self.creerItEffectif(frame, numero.get(), poids.get(), volume.get())).grid(column=1, row=3, sticky=tkinter.W)
        
        numero_entry.focus()
        self.bind('<Return>', lambda paraNonUtilise: self.creerItEffectif(frame, numero.get(), poids.get(), volume.get())) # le paramètre non utilisé est une instance de la classe Event
        
    def creerItEffectif(self, frame, numero, poids, volume):
        '''
        Fonction qui crée l'itinéraire sous format texte
        '''
        try:
            util.creerIti(numero, poids, volume)
            for child in frame.winfo_children():
                child.destroy()
            messConfirmation = tkinter.StringVar()
            ttk.Label(frame, textvariable=messConfirmation, foreground="dark green").grid(column=1, row=1, sticky=tkinter.W)
            messConfirmation.set("Le trajet pour le chariot n° %s a été créé." % (numero.upper(), ))
        except excpMetier.ExceptionEntreeVide:
            messagebox.showinfo(title="Champ(s) vide(s)", message="Le trajet n'a pu être créé", parent=self)
        except excpBdd.ExceptionFormatInadequat:
            messagebox.showinfo(title="Champ(s) trop long(s)", message="Le trajet n'a pu être créé", parent=self)
        frame.mainloop() 
          
if __name__ == '__main__':
    fen = FenetreAppli(None)