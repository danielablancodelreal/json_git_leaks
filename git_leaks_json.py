#! user/bin/python3

from git.repo import Repo
import re
import json


REPO_DIR = './skale/skale-manager-develop'
KEY_WORDS = ['identification','credentials','username','password','key']
        #Palabras clave que estamos buscando en los commits del repositorio

def extract(repo_dir):
    repositorio = Repo(repo_dir)
    commits = list(repositorio.iter_commits('develop'))
    return commits

def load(dict_leaks):
    with open("fichero_leaks.json", "w") as outfile:    #Creamos un fichero json con los commits
        json.dump(dict_leaks, outfile)                  

if __name__ == '__main__':
    commits = extract(REPO_DIR)

    dict_leaks = {}
    keys = []
    values = []

    for commit in commits:          #Iteramos por los commits y usamos regex para buscar las palabras clave
        for word in KEY_WORDS:
            if re.search(word, commit.message, re.IGNORECASE):
                print('Id del commit: ',commit.hexsha,' | Mensaje: ',commit.message)
                keys.append(commit.hexsha)
                values.append(commit.message)

    for i in range(len(keys)-1):
        dict_leaks[keys[i]] = values[i]     #Creamos un diccionario con los IDs y los mensajes 

    load(dict_leaks)                              
                
                

    