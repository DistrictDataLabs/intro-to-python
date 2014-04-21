#Notes for installing a Python Development environment in Windows 7.

This note is based on the Python 2.7 installation available at [python.org](http://www.python.org), as well as Git version 1.9.0. Most of these instructions also will work on Windows XP, if you're still running it. 

## Installation
We start by downloading Python 2.7.6 from [here](https://www.python.org/downloads/) and installing it. The typical installation is at C:\Python27. Since we're going to work at the command line for development, we need to add some directories to the path. In Windows 7, from the Windows button, search for "environment variables" and then select "Edit the system environment variables" (or "Edit environment variables for your account" if you don't have administrator privileges). Add the following paths to the end of the Path, separating by ";":

+ C:\Python27
+ C:\Python27\Scripts

If you had decided to download Python 3.4.0, change Python27 to Python34 above.

## The Shell
A lot of development happens at the command line. We recommend using **Windows Powershell** for your development work rather than the native command window, since the available commands are more amenable to development work. PowerShell also allows tab-completion of commands, which makes developing much more efficient. Unix commands like `ls` and `pwd` work just fine. Some commands that Unix developers are used to can be translated to Powershell, as follows:

<table>
	<th> Unix </th><th>Windows</th>
	<tr>
	<td> touch __init__.py</td><td>echo $null > __init__.py</td>
	</tr>
</table>
A comprehensive list of PowerShell equivalents of Unix commands can be found [here](http://cecs.wright.edu/~pmateti/Courses/233/Labs/Scripting/bashVsPowerShellTable.html). 

Installing Git (see below) provides an option to include commands like `touch` and other standard Unix commands to Windows. 

You can also customize your PowerShell console using a *profile* file (similar to .bashrc in Unix). This [blog](http://thesoftwaresimpleton.blogspot.com/2011/05/own-your-powershell-profile.html) gives a nice introduction to customizing your console.

## Setting up the Python environment

### Installing Python modules
The easiest way to install Python modules is using `pip`, which is a Python installation manager. This is not installed by default in Python 2.7.6, but is installed by default in Python 3.4. The easiest way to install this is:

1. Right-click and save [get-pip.py](https://raw.github.com/pypa/pip/master/contrib/get-pip.py) (remember where you saved it; I'll assume it's `\Users\yourname\Downloads`)
2. Open PowerShell. Type `cd \Users\yourname\Downloads` (replacing "yourname" with the your username
3. Type `python get-pip.py`. This will install `pip`. Now you're ready to install other Python modules

If you're getting an error when you're typing `python get-pip.py` to the effect of *"The term 'python' is not recognized as the name of a cmdlet, function, script file, or operable program"*, make sure you had added the paths for Python to your computer's Path variable, as described in the previous section.

Now you're ready to install other python modules.

### Installing virtualenv
To install `virtualenv` and `virtualenvwrapper`, you can now type, in PowerShell, the following commands:

    pip install virtualenv
    pip install virtualenvwrapper

### Installing other modules
`pip` is a generic solution for installing modules in Python, and works perfectly well in Unix-like environments. However, Windows has certain idiosyncrasies regarding compilers, paths and the like, 
so it is often easier to install modules using pre-built installers for Windows. In particular, you can find several module installers [here](http://www.lfd.uci.edu/~gohlke/pythonlibs/). 

To install Numpy, download the appropriate installer for your version of Python and your operating system (32-bit or 64-bit) from [here](http://www.lfd.uci.edu/~gohlke/pythonlibs/#numpy), and double-click the downloaded file. This site also has installers for [scipy](http://www.lfd.uci.edu/~gohlke/pythonlibs/#scipy), [pandas](http://www.lfd.uci.edu/~gohlke/pythonlibs/#pandas) and other modules in the scientific Python stack. 

You may also need to download and install the Visual C++ 2008 Redistributable Package ([32-bit](http://www.microsoft.com/en-us/download/details.aspx?id=29) or [64-bit](http://www.microsoft.com/en-us/download/details.aspx?id=15336)). If you installed Python 3.4, you may need the Visual C++ 2010 Redistributable Package ([32-bit](http://www.microsoft.com/en-us/download/details.aspx?id=5555) or [64-bit](http://www.microsoft.com/en-us/download/details.aspx?id=14632)).

### Other distributions
There are other Python distributions available that can be easier to install and start developing on, specially for the scientific Python stack. These include:

+ [Anaconda](https://store.continuum.io/cshop/anaconda/) 
+ [Canopy](https://www.enthought.com/products/canopy/)
+ [Python(x,y)](https://code.google.com/p/pythonxy/)

Anaconda does not require administrative privileges, so it is easier to install for everyone. That installation also automatically adds Python to your path and comes with `pip` included. A more comprehensive list can be found [here](http://www.scipy.org/install.html).

### Integrated Development Environments (IDEs)
Many of us prefer just a text editor with syntax highlighting to write Python code, like [Sublime Text](http://www.sublimetext.com) or [Notepad++](http://www.notepad-plus-plus.org). However, if you really want an IDE, two good choices are 

1. [PyDev](http://www.pydev.org) for Eclipse (free)
2. [WingIDE](http://www.wingware.com) (paid)

Several other IDEs are listed on the Python [Wiki](https://wiki.python.org/moin/IntegratedDevelopmentEnvironments). 

## Installing Git
Git can be downloaded [here](http://git-scm.com/download/win). When running the installer, on the screen "Adjusting your PATH environment", choose *"Run Git  from the Windows Command Prompt"*. You can also choose *"Run Git and included Unix tools from the Windows Command Prompt"* if you're comfortable doing that.

You can now run `git` from PowerShell (you might need to restart PowerShell to make sure `git` can be found). 

You can also run `touch` and other Unix commands in PowerShell if you chose the second option above. Thus `touch __init__.py` works.
