# contextcommands

This tool allows for running context-sensitive commands that will look at the previous command you ran to determine how it should act. It was inspired by Google Now's context-sensitive capabilities.

## Installation

This tool requires Python 3.x

Clone this repo to your local system, then run the **install.sh** script. It will copy the files into ~/.local/bin/contextcommands and give you a line to put in your ~/.bashrc file to add the 'c' function to your environment.

##Example usage:

    sudo systemctl restart apache2
    c status

In this example, the 'c' command is a bash function in **context.bash** that takes the argument of 'status' in this case, grabs the previous command from history, then feeds both to the **context.py** Python script to determine what kind of action to take. 

The `systemctl` command is detected because of the **systemctl.py** module under **modules/** and that module checks to see if the argument ('status') is one of several defined actions for the `systemctl` command. Since 'status' is in the defined list of actions, it takes the previous command, replaces 'restart' with 'status', and sends the command text back to the 'c' function for display, adding to the bash history, and finally running the command. The 'systemctl' module also allows for changing the service name in the previous command as well. Any context command that doesn't match a defined systemctl action will be assumed to be a service name.

The other initial modules that I've added are for the 'less', 'cat', and 'docker' commands. The 'less' and 'cat' modules are basically the same. After running either of those, a context command like `c nano` or `c vim` will replace `less` or `cat` with the command after the 'c'. This is for the common use case of needing to edit a file after viewing it with `less` or `cat`. The 'docker' module is similar to the 'systemctl' module and can change the action in commands like `docker start container1`.

## Creating Modules

I'll be adding more modules and refining/extending the ones that I have as I find more use cases for this. If you want to make your own modules, take a look at the **less.py** and **systemctl.py** files in the `modules` folder as examples. Both are commented.

Modules will be auto-detected when the 'c' command is invoked.

The 3 requirements for a module are:

1. It must have a `context()` function like the examples that takes in the list item containing the previous command, and the context command word.
2. The `context()` function must return either a command string or `None`.
3. It should not be possible for the returned command string to contain an unintentionally destructive action. For example, if you make a module for `rm` (which I probably won't do), make sure that it won't replace the file name with something like '*'.

## Contributing

I welcome useful module additions and enhancements. Please make sure to test your code and add comments where appropriate.
