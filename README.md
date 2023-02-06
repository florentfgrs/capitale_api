# Objectif 
Apprendre a créer simplement une API 

# Fonctionnement 

On lui passe un pays et l'api renvoie la capitale de ce pays

# Installation

## Créer un virtual env 
```
python3 -m venv env
```

## Activer le virtual env 
```
source env/bin/activate
```

## Installer les lib 

```
python3 -m pip install -r requirements.txt
```

## Lancer l'api 

```
python3 main.py
```

## Tester l'api 
http://localhost:5000/api/capital?country=France