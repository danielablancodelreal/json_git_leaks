from git import Repo
import re #signal
import time
from tqdm import tqdm



REPO_DIR = './skale/skale-manager'
KEY_WORDS = ['credentials','password','key'] #,'password','username','key'

def extract(repo_dir):
    repo = Repo(repo_dir)
    commits = list(repo.iter_commits('develop'))
    return commits

def load():
    
    time.sleep(1)
    

if __name__ == '__main__':
    commits = extract(REPO_DIR)
    for commit in commits:
        for word in KEY_WORDS:
            if re.search(word, commit.message, re.IGNORECASE):
                print('Commit: {} - {}'.format(commit.hexsha, commit.message))
                
                

    