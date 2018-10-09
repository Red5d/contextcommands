# Super-simple example module for the 'ls' command.
#

def context(cmd, word):
    cmd_loc = cmd.index('ls')
    
    cmd[cmd_loc] = word
    return ' '.join(cmd)
