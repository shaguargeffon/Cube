# Learn Cube and Test your reaction time about CFOP
It is implemented using PyQt5 library

# How to install
install python with the version 3.9 or 3.10 (mandatory)
install PyQt5 pip package using the command : pip install PyQt5  (in cmd mode)

# How to run it
Go to the directory of the main.py, run it using the command: python main.py

# How to use it
After openning the GUI you can click the pushbutton "Update", then you will get the random cube snapshots without overlapping.
The showing process is repeated round by round.

# Trouble Shooting
It will throw an exception when the name of the folder "pictures" is changed.
It will throw an exception when the format of pictures can'be be parsed by python

# How to extend it
You don't need to touch the source code. You only need to add your cube pictures into the "pictures" folder

# Continous Development
Now it only supports one learning mode, later it will also support test mode which is also configurable.
In test mode the time out event will be poped up when your solution is over time.
The GUI will be optimized and more features will be added there, for instance to show solution when time out is happening.
Now it only supports CFOP Cube solution, later it will be extended.
