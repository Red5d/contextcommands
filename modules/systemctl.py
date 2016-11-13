def context(cmd, word):
    actions = ['start', 'stop', 'restart', 'reload', 'show', 'status']
    cmd_loc = cmd.index('systemctl')
    
    # If the context command word is one of the defined actions for systemctl...
    if word in actions:
        # ...swap it into the correct place in the previous command
        cmd[cmd_loc+1] = word
        return ' '.join(cmd)
    else:
        # ...if not, assume that it's a service name and swap it into the correct place
        cmd[cmd_loc+2] = word
        return ' '.join(cmd)
        
