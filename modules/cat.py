def context(cmd, word):
    cmd_loc = cmd.index('cat')
    
    cmd[cmd_loc] = word
    return ' '.join(cmd)
