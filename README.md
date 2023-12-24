# Learn Cube and Test your reaction time about CFOP
It is implemented using PyQt5 library

# How to clone the repository from GitHub
Install git on Windows
Create one folder locally, open the git bash, run the command : git clone https://github.com/shaguargeffon/Cube.git

# How to get the latest version of the Software
Open the git bash, run the command : git pull
Don't edit any .py file, or the pull will be failed.
Pictures folder can be extended/modified

# How to install
install python with the version 3.9 or 3.10 (mandatory)
install PyQt5 pip package using the command : pip install PyQt5  (in cmd mode)
install schedule pip package using the command : pip install schedule

# How to run it
Go to the directory of the main.py, run it using the command: python main.py

# How to use it
Now it supports two modes : learning mode and test mode
For the learn mode:
  After opening the GUI you can click the pushbutton "Next Picture". Then you will get one random cube
  picture without overlapping.
  The button "Switch to Learn mode" is not useful in this use case since it is used only for switching game mode.
  The showing process is repeat round by round.

For the test mode:
  After opening the GUI you can click the pushbutton "Switch to Test mode". Then you will get one random cube
  picture without overlapping periodic.

When you want to switch the mode, just click the pushbutton "Switch to Learn mode" or "Switch to Test mode"


# Trouble Shooting
It will throw an exception when the name of the folder "pictures" is changed.
It will throw an exception when the format of pictures can't be parsed by python

# How to extend it
You don't need to touch the source code. You only need to add your cube pictures into the "pictures" folder

# Continuous Development
In test mode the time out event will be popped up when your solution is over time.
The GUI will be optimized and more features will be added there, for instance to show solution when time out is happening.
Now it only supports CFOP Cube solution, later it will be extended.
