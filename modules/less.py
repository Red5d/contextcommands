# Super-simple example module for the 'less' command.
#
# Use case is reading a file with less, then wanting to edit it.
# A quick "c <editor of choice>" command after running the less 
# command will replace 'less' in cmd (a list containing the command parts) 
# with <editor of choice> and re-run.

def context(cmd, word):
    cmd_loc = cmd.index('less')
    
    cmd[cmd_loc] = word
    return ' '.join(cmd)
