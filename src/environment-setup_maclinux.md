---
title: Configuring a Development Environment
---

For this course we will all use the same software, namely
[Python](#python), [Git](#git), and [Visual Studio
Code](#visual-studio-code), so that we all have nearly the same
experience, regardless of platform (Windows, macOS, Linux). We will also
create a [workspace](#workspace) on our computers for storing work,
Python dependencies, software preferences, etc.; test out the creation
of a [virtual environment](#virtual-environment); and [make sure it all
works](#test-it-out). Our goal by the end is to have a coding environment
that enables a programmer's [workflow](#workflow) so we can learn to
code efficiently and write programs that function.

In the instructions below, the headings are intended to help organize the
text. Some instructions will be different depending on your operating system
(Windows/Mac/Linux) so make sure you are following the relevant instructions.
Our end result should be the same: a single course folder that we can open
in VSCode as a workspace, and three windows in the workspace for viewing,
editing, and running Python scripts.

## Mac and Linux

For running the code we write, we will need a [Python][python]
interpreter. This is perhaps the most challenging to set up because each
platform does it differently. For smooth sailing in this course, try to install
Python version 3.10 since that is what has been tested (3.13.5 is the highest
stable version as of this writing). At the current time, NLTK requires Python
versions 3.7, 3.8, 3.9 or 3.10. Earlier or later versions may cause issues with
your libraries or packages that can require extensive troubleshooting.

#### macOS

macOS machines come with Python 2.7, but this is an old and unsupported
version that will not work for our class. The best way to install Python
3 is probably with [Homebrew](https://brew.sh) via the built-in Terminal
app, which is located in your `Utilities` folder (in Finder, use the key
combo `Cmd+Shift+U` to navigate quickly to the folder). First, start the
Terminal app, and type the following at the prompt:

```{.bash .terminal}
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
```

This command will download the installer for Homebrew and then run it. It may
take some time, as it might need to download XCode tools as well.
Once it's installed, run the following command in your terminal with the
version number specified:

```{.bash .terminal}
brew install python@3.10
```

Some more information about installing Python with Homebrew is
[here](https://docs.brew.sh/Homebrew-and-Python).

#### Linux

Python 3 generally comes pre-installed on Linux. In a terminal, you can
check the latest version of Python like this:

```{.bash .terminal}
python3 --version
```

If it says "command 'python3' not found" or gives you a version not equal to
3.10, you need to install a different version. How this is done depends
on the distribution of Linux, so contact me if you need help.

On some distributions, notably Ubuntu, you may need to install support
for `venv`, which we use for creating virtual environments (described
below). Here's how you'd do that for Ubuntu:

```{.bash .terminal}
sudo apt install python3-venv
```

### Visual Studio Code

Visual Studio Code is the program we use to write code. It also assists
with running tests and tracking changes with Git, as well as other
advanced features for developers, but we will not be exploring these for
the most part.

For all platforms you can download an installer from
<https://code.visualstudio.com/>.

-------  ------------------------------------------------------------------------------
macOS    [Download](https://go.microsoft.com/fwlink/?LinkID=620882){.button}
Linux    [Download](https://code.visualstudio.com/docs/?dv=linux64_deb){.button} (.deb)
-------  ------------------------------------------------------------------------------

On macOS you can also use Homebrew, if you prefer:

```{.bash .terminal}
brew install visual-studio-code
```

#### Recommended Extensions

Visual Studio Code is quite capable on its own, but there are extensions
that can make it even more useful for certain uses. I suggest only
installing extensions from reputable sources, or those with many users
and high ratings, as there's the possibility of malicious extensions. I
recommend the following for now:

- [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python) by Microsoft
- [Git History](https://marketplace.visualstudio.com/items?itemName=donjayamanne.githistory) by Don Jayamanne

Visual Studio Code may prompt you to install a "linter" for Python. This
is optional, but it's probably a good idea. It will let you know when
you've made some kinds of programming mistakes.

### Using the VSCode terminal to complete setup

Take a brief read of the [Using VS Code](using-vscode.html) page to get an idea
of how VSCode works. Earlier you used the native Terminal app to install
things, but we will now be using the VSCode terminal (or "command line
interface") to help us set up Git. For now, you can simply open VSCode - don't
worry too much about setting up a new workspace (any will do for the remainder
of setup), and focus instead on the lower right hand area of the window, where
a `terminal` should be. If it doesn't show up, you can use the *Terminal* menu
to select a *New Terminal*.

### Git

For tracking versions of the code we write, we will use [Git][git]. This
is also how we will submit our homework assignments. Installation is
relatively straightforward on Mac/Linux

If you haven't already done so, go to [Github](https://github.com) and sign
up for a free account with your email address. The email will be necessary
for pushing changes to your assignments.

#### macOS

Use Homebrew to install Git on macOS:

```{.bash .terminal}
brew install git
```

You can do this using the native Terminal app or the terminal window in VSCode.

#### Linux

Install Git on Linux with your package manager, via the native Terminal app
or the terminal window in VSCode. Git's website has instructions for
many distributions: <https://git-scm.com/download/linux>

### Set up Git credentials for Github

After installing Git, type the following commands in your VSCode terminal
to set up credentials on your local machine. Replace `USERNAME` with the
Github username, and `NAME@EMAIL.com` with the Github email address that
you signed up with in the earlier step:

```{.bash .terminal}
git config --global user.name "USERNAME"
git config --global user.email "NAME@EMAIL.com"
```

## Workspace

Now that the software is installed, we need a place to work in. This
workspace is a folder (directory) somewhere on your computer (e.g., on
the Desktop or wherever makes sense to you). Create it in any
method you like (e.g., in Windows Explorer or Finder or in a terminal).
For these instructions I will assume you named it **"HG2051"**. This also
assumes that you know what folders are and how files/folders are organized
on your computer. We will be going over the basics of this in the first
week of class, but to make it easier you should avoid folder names with
spaces in them.

Once your folder is created, open Visual Studio Code and open the folder you
just created via *File* > *Open Folder*. You will see something like this:

![*Empty HG2051 Workspace*](static/empty-workspace.png){ width=100% }

Note the "Explorer" side bar (top-left), which is a file and folder
view. It shows that you are in the "HG2051" folder. In the terminal
panel (bottom-right), the prompt indicates the same thing, i.e., that
you are in the "HG2051" folder. If you don't see the terminal, try
pressing <kbd>Ctrl-\`</kbd>, or use the menu *View* > *Terminal*. Note
that your prompt may look a bit different, depending on which shell and
platform you're using.

## Virtual Environment

The next step is to create a virtual environment, which is a subfolder that
contains the Python packages we will use for this course.
We will use one virtual environment for the whole course, though it is
typical to use different environments for different projects.

#### Creating the Virtual Environment

Enter the following command into Visual Studio Code's terminal:

```{.bash .terminal}
python3 -m venv env
```

This calls the Python module `venv`, which creates virtual environments,
and has it create one called "env" (you can name it whatever you like,
but let's stick with "env"). If successful, it will look like the
following. If it did not succeed, please contact me.

![*Creating a Virtual Environment*](static/create-env.png){ width=100% }

Now notice in the Explorer side bar that the "env" folder is created. In
the terminal, I also executed the `ls` command, which lists the contents
of the current folder, showing that the **"env"** folder exists. You don't
need to worry about the contents of the "env" directory except for the
following:

(macOS/Linux)
* Activation script location
  - `env/bin/activate`
* Python interpreter location
  - `env/bin/python`

If you see a pop-up like the following (perhaps when editing a Python
file), click "Yes" as it will help Visual Studio Code automatically run
Python code using your virtual environment:

![*Auto-detection of a New Virtual Environment*](static/new-venv.png)

If you don't see that, try opening the command palette and searching for
"Python: Select Interpreter". You should see an option for
`./env/bin/python`. If not, enter or find the path appropriate for your platform.

#### Activating the Virtual Environment

Creating the virtual environment just makes a new folder and
directories, but to use it you must activate it. An activated virtual
environment directs Python to use the packages within the folder and not
those installed elsewhere on your computer. Users on macOS or Linux can
simply run the following command (and let me know if it doesn't work):

```{.bash .terminal}
source env/bin/activate
```

If successful, you'll see (env) at the beginning of the next prompt. If
you see any errors, please let me know. While the environment is active,
using `python` (instead of `python3` or `py`) should use the Python
version included in the virtual environment.

## Test It Out

If all was successful, you should be able to do the following two things.

#### Install the `pytest` Dependency

We will use [pytest][] for automatic evaluation of some of our homework
assignments. Once the virtual environment is active, run the following
command in your terminal:

```{.bash .terminal}
pip install pytest
```

If it says the `pip` command is not found, ensure your virtual
environment is active. If it is and still cannot find it, then try
`pip3` or `python -m pip` instead. If it still complains after that,
then please contact me.

If it is successful, you'll see 10 or so packages being installed in
addition to pytest. The others are pytest's dependencies.

#### Create a `hello.py` Module

Create a new file in Visual Studio Code (<kbd>Ctrl-n</kbd> or *File* >
*New File*). Type the following into the file:

```{.python .terminal}
print('hello')
```

Then save (<kbd>Cmd-s</kbd> or *File* > *Save*) the file to `hello.py`
in your current workspace. Once it is saved, you should see the code
become colored (syntax-highlighting). This means that Visual Studio Code
recognized it as a Python file. If Visual Studio Code also detected your
virtual environment, you should see a green "play" icon in the top
right. Clicking that will launch a new terminal with the virtual
environment active (the shell type will say "Python" instead of "bash"
or "PowerShell") and execute the Python file. You should see "hello" in
the terminal output of the command.

![*Running hello.py*](static/run-hello-py.png){ width=100% }

While it is nice to be able to use the "play" button to run a whole script
or parts of the code from a script, our goal with this course is to learn
how to create complete programs that run without errors. For this reason,
you should avoid using the "play" button for the time being.

## Workflow

The workflow we will follow makes use of three elements: the
<mark style="background-color: pink">**file explorer**</mark>,
the <mark style="background-color: lightgreen">**editor**</mark>, and the
<mark style="background-color: lightblue">**terminal**</mark>. You should
become comfortable with moving between these elements as you develop your code.
Your <mark style="background-color: pink">**file explorer**</mark> is where
your programming files are located, along with various subfolders for
organizational purposes. When you open a file to work on it, it opens in
your <mark style="background-color: lightgreen">**editor**</mark>, which
allows you to write/modify code. After saving your work, you switch to the
<mark style="background-color: lightblue">**terminal**</mark> to run the file
and check that it functions. Going back and forth gives you immediate feedback
and allows you to catch errors in order to fix them and achieve working code.
For more details, a brief guide related to this course is provided in
[Using VS Code](using-vscode.html), with additional links to more comprehensive
resources.

[python]: https://www.python.org/
[vscode]: https://code.visualstudio.com/
[git]: https://git-scm.com/
[pytest]: https://pytest.org/
