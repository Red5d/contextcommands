def context(cmd, word):
    actions = ['start', 'stop', 'restart', 'pause', 'unpause', 'rm', 'top', 'attach', 'events', 'inspect']
    cmd_loc = cmd.index('docker')
    
    # if the context command word is 'ps', change the action in the cmd to 'ps' and exclude any command parts past 'ps'
    if word == "ps":
        cmd[cmd_loc+1] = word
        return ' '.join(cmd[0:cmd_loc+2])
    elif word in actions:
        # ...else, put the new action in place
        cmd[cmd_loc+1] = word
        return ' '.join(cmd)
    else:
        return None

