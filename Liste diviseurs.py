#Crée une liste avec les diviseurs du nombre puis l'affiche

n = int(input("Entrez le nombre"))
liste = []

for i in range (1,n+1):
    if n % i == 0:
      liste.append(i)
      liste.append(-i)
print(liste)
