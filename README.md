## On clone
```bash
git clone https://github.com/chdem/tp_docker_python.git
```  
## On build et on lance
(depuis la racine)
```bash
docker compose up -d
```
## On peut faire quoi ?
### On peut lancer une console depuis le conteneur read 

```bash
docker compose exec -it read sh
```

Et une fois connecté au shell du conteneur :
```python
python main.py
```

Et là tu peux faire quoi ?

1. Afficher les films
2. Récupérer depuis le titre 
3. Récupérer les films sous une limite d'âge :
4. Récupérer les films selon un genre
5. Récupérer les films entre deux années (incluses)
6. Exit

Evite de mettre des vessies dans des lanternes, des lettres dans des années (t'es pas un Romain ?) et tout devrait bien se passer sinon t'auras un truc comme ça (ou pire !!)

```bash
Choisir votre action : 3
Entrez l\'age minimum : Jean-Michel
Age invalide
```

Allez un exemple :

```bash
1. Afficher les films
2. Récupérer depuis le titre
3. Récupérer les films sous une limite d\'âge :
4. Récupérer les films selon un genre
5. Récupérer les films entre deux années (incluses)
6. Exit
Choisir votre action : 2
Entrez le nom du film cherché : Lord
[\'9\', \'The Lord of the Rings: The Return of the King\', \'2003\', \'Aventure\', \'12\']
[\'12\', \'The Lord of the Rings: The Fellowship of the Ring\', \'2001\', \'Aventure\', \'12\']    
```


### On peut aussi lancer le write

```bash
docker compose exec -it write sh
```

Et une fois connecté au shell du conteneur, pareil :
```python
python main.py   
```

Et ici on peut faire :

```bash
1. Afficher les films
2. Ajouter un film
3. Modifier un film
4. Supprimer un film
5. Exit
```