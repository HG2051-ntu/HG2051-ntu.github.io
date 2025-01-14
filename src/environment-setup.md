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

## Python

For running the code we write, we will need a [Python][python]
interpreter. This is perhaps the most challenging to set up because each
platform does it differently. Make sure you get Python version 3.7 or
higher (3.13.1 is the highest stable version as of this writing). At the
current time, NLTK requires Python versions 3.7, 3.8, 3.9 or 3.10. I
recommend installing Python 3.10, since that's what I'll be working with.

#### Windows

The recommended way is to get the latest version from
<https://www.python.org>:
[python-3.10.9-amd64.exe](https://www.python.org/ftp/python/3.10.9/python-3.10.9-amd64.exe){.button}

During install, you should select "Add Python 3.10 to PATH". If you do
not, then later in the terminal you may need to use `py` instead of
`python` or `python3`. That is, if these don't work:

```{.bash .terminal}
$ python --version
$ python3 --version
```

Try this instead (and let me know if this doesn't work, either):

```{.bash .terminal}
$ py --version
```

Whichever command returns you a version greater than or equal to 3.7
will be what you can use for this course.

See
[here](https://docs.python.org/3/using/windows.html#the-full-installer)
for more information.

On newer versions of Windows, you may also need to disable the auto-installer
for Python via the app store via `Settings > App settings > App execution aliases`
or by going to "start" and typing "Manage App Execution Aliases". (see [this post](https://stackoverflow.com/questions/65348890/python-was-not-found-run-without-arguments-to-install-from-the-microsoft-store) for a screenshot).

#### macOS

macOS machines come with Python 2.7, but this is an old and unsupported
version that will not work for our class. The best way to install Python
3 is probably with [Homebrew](https://brew.sh). First, start the
Terminal app, and type the following at the prompt:

```{.bash .terminal}
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
```

This command will download the installer for Homebrew and then run it. It may
take some time, as it might need to download XCode tools as well.
Once it's installed, run the following command in your terminal:

```{.bash .terminal}
brew install python3
```

or, to be more specific about the version, you can try this:

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

If it says "command 'python3' not found" or gives you a version lower
than 3.7, you need to install a newer version. How this is done depends
on the distribution of Linux, so contact me if you need help.

On some distributions, notably Ubuntu, you may need to install support
for `venv`, which we use for creating virtual environments (described
below). Here's how you'd do that for Ubuntu:

```{.bash .terminal}
sudo apt install python3-venv
```

## Git

For tracking versions of the code we write, we will use [Git][git]. This
is also how we will submit our homework assignments. Installation is
straightforward but there are many options. Choose the default for all
except for the editor, which may say "vim". Choose "Visual Studio Code"
instead.

If you haven't already done so, go to [Github](https://github.com) and sign
up for a free account with your email address. The email will be necessary
for pushing changes to your assignments. Set up credentials on your local
machine after installing Git with the commands below (replace `USERNAME`
with your Github username, and `NAME@EMAIL.com` with your Github email
address):

```{.bash .terminal}
git config --global user.name "USERNAME"
git config --global user.email "NAME@EMAIL.com"
```

#### Windows

Download the latest version from <https://git-scm.com>:
[Git-2.39.0-64-bit.exe](https://github.com/git-for-windows/git/releases/download/v2.39.0.windows.2/Git-2.39.0.2-64-bit.exe){.button}

#### macOS

Use Homebrew to install Git on macOS:

```{.bash .terminal}
brew install git
```

#### Linux

Install with your package manager. Git's website has instructions for
many distributions: <https://git-scm.com/download/linux>

## Visual Studio Code

Visual Studio Code is the program we use to write code. It also assists
with running tests and tracking changes with Git, as well as other
advanced features for developers, but we will not be exploring these for
the most part.

For all platforms you can download an installer from
<https://code.visualstudio.com/>.

-------  ------------------------------------------------------------------------------
Windows  [Download](https://aka.ms/win32-x64-user-stable){.button}
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

Enter the following command into Visual Studio Code's terminal (you may
need to replace `python3` with `py` on Windows):

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

* Activation script location
  - (Windows) -- `env\Scripts\Activate.ps1`
  - (macOS/Linux) -- `env/bin/activate`
* Python interpreter location
  - (Windows) -- `env\Scripts\python.exe`
  - (macOS/Linux) -- `env/bin/python`

If you see a pop-up like the following (perhaps when editing a Python
file), click "Yes" as it will help Visual Studio Code automatically run
Python code using your virtual environment:

![*Auto-detection of a New Virtual Environment*](static/new-venv.png)

You may get an error on Windows, though. For this, see below.

If you don't see that, try opening the command palette and searching for
"Python: Select Interpreter". You should see an option for
`./env/bin/python` (macOS/Linux) or `.\env\Scripts\python.exe`
(Windows). If not, enter or find the path appropriate for your platform.

#### Activating the Virtual Environment

Creating the virtual environment just makes a new folder and
directories, but to use it you must activate it. An activated virtual
environment directs Python to use the packages within the folder and not
those installed elsewhere on your computer. Users on macOS or Linux can
simply run the following command (and let me know if it doesn't work):

```{.bash .terminal}
source env/bin/activate
```

Windows users may have more work to do, because Windows by default
blocks you from running "untrusted" scripts. First, we want to ensure
that Windows PowerShell is being used as our default terminal in VSCode.
We can do this by searching for `terminal` in the Command Palette
(<kbd>[Cmd]Ctrl-Shift-P</kbd>) and selecting PowerShell as the default.
Then, to allow  the current session to activate the virtual environment,
you can change Visual Studio Code's settings so PowerShell can run these
scripts.

First, close the terminal (click the garbage bin icon), and start a new
terminal to ensure we're working with a fresh instance. Now, in the new
terminal, try to execute the following:

```{.bash .terminal}
.\env\Scripts\Activate.ps1
```

If this doesn't work, it may be because `bash` commands are not enabled by
default in PowerShell, resulting in errors. The *Bash* program is
installed by Git and used for committing and pushing changes, among other
things. To ensure that `bash` commands are enabled, run the following
command in your terminal:

```{.bash .terminal}
set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```
*Thanks to [THIS](https://www.c-sharpcorner.com/article/how-to-fix-ps1-can-not-be-loaded-because-running-scripts-is-disabled-on-this-sys/) blog post and related Stack Overflow answer*:
<https://stackoverflow.com/questions/1098786/run-bash-script-from-windows-powershell>

If successful, you'll see (env) at the beginning of the next prompt. If
you see any errors, please let me know. While the environment is active,
using `python` (instead of `python3` or `py`) should use the Python
version included in the virtual environment.

*Also consider the following Stack Overflow answer in case you are still having issues*:
<https://stackoverflow.com/a/61281420/1441112>

## Test It Out

If all was successful, you should be able to do the following two things.

#### Install the `pytest` Dependency

We will use [pytest][] for automatic evaluation of some of our homework
assignments. Once the virtual environment is active, run the following
command:

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

Then save (<kbd>Ctrl-s</kbd> or *File* > *Save*) the file to `hello.py`
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
