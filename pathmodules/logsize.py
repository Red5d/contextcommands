def paths():
    return ['/var/log']

def context(path, word):
    if word == 'size':
        return 'ls -lahS'
    else:
        return None
