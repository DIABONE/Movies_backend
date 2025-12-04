###### Classe ######

#%%
class Chien:
    pass

### Objet #####
#%%

mon_chien  = Chien()
type(mon_chien)

##### Attributs ######

#%%

class Chien:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age


# %%

mon_chien = Chien("Ricky", 2)
print(mon_chien.nom)
print(mon_chien.age)

###### Méthodes #########

#%%

class Chien:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age
    
    def aboyer(self):
        print(f"{self.nom} aboie !")



# %%

ricky = Chien("Ricky", 2)
print(ricky.aboyer())
# %%
