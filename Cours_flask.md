# Exercices Flask

Conseil: utiliser un environement Linux <3

But de l'exercice:

- Comprendre Flask
- Comprendre le json
- Apprendre mongoDB
- Utilisation de Postman

Requis:

- Python 3.5+
- Docker <3
- Postman

## Exo1

Faire une route `GET /`

### Retourne

```json
{
    "msg": "Hello World"
}
```

## Exo2

Faire une route `GET /hello?name=<name>` qui retourne:

```json
{
    "msg": "Hello <name>"
}
```

### Example1

`GET /hello?name=romain`

```json
{
    "msg": "Hello romain"
}
```

### Example2

`GET /hello?name=chloe`

```json
{
    "msg": "Hello chloe"
}
```

## Exo3

Faire une route `POST /new`

### Parametre

`body`

```json
{
  "FirstName": "<firstname>",
  "LastName": "<lastname>"
}
```

### Retourne

```json
{
  "FirstName": "<firstname>",
  "LastName": "<lastname>"
}
```

### Example1

#### Parametre

`body`

```json
{
  "FirstName": "Romain",
  "LastName": "Chassaigne"
}
```

#### Retourne

```json
{
  "FirstName": "Romain",
  "LastName": "Chassaigne"
}
```

## Useful commands

### Virtual env Python

- Créer un nouveau dossier vide
- Executer la commande suivante:  
```bash
cd <dossier>
python3 -m venv .
```
- Commande à faire a **chaque réouverture du projet**:
```bash
source ./bin/activate
```
- Installer tout les requis (flask, pymongo):  
```bash
pip install flask
pip install pymongo
```

### Docker & mongo

- Installer Docker (avec compatibilité WSL)
- Dans WSL, executer la commande:
```bash
docker run -d -p 27017:27017 --name mongo mongo:latest
```
- A chaque redémarrage du PC (si vous voulez retravailler sur le projet), utilisez la commande:
```bash
docker start mongo
```