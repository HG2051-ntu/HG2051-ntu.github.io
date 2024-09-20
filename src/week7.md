---
title: 'Week 7'
---

##   Learning Objectives

*   Concepts:
    [packages]{.py}
    [licensing]{.eng}
    [testing]{.eng}
    [documentation]{.eng}
    [distribution]{.eng}

(color key: [Python/Programming]{.py} [NLP/CL]{.nlp} [Software Engineering]{.eng})

## Review and Quiz

For the review, please see the [midterm review](midterm-review.html).

The midterm quiz consists of an in-class project that will apply what you have
learned in the first half of this course. After the lecture you will be provided
an individual link to your quiz repository, which contains instructions on
completing the quiz. You will have 1.5 to 2 hours to complete the quiz by
updating your repository. This quiz is not autograded, but you are encouraged
to write your own tests to ensure that the goals are met. This is an open quiz,
meaning that using online resources etc is allowed. However, the quiz will be
monitored and collusion or cheating will result in automatic failure.

## Working with Software Projects

As you develop your experiments into software projects that others might get
value from, you might start to think about how to distribute your code. There
are many practices and tools to support software distribution. Some of them are:

*   [choosing a license](#licensing)
*   [testing the software](#testing)
*   [documenting the project](#documenting)
*   [distributing the code](#distributing)

But first, let’s look at how to use Python packages to organize code.

### Python Packages

When you write some file `hw6.py`, then it is a Python module that can be
imported as follows:

  ```python
  >>> import hw6
  ```

When working with larger projects, you may need multiple modules, and you may
want to group them into _packages_. On the computer, these are just folders
with a special `__init__.py` file.

Please read the Python Tutorial’s sections on modules and packages:

*   [PT 6 – Modules](https://docs.python.org/3/tutorial/modules.html)
    - [PT 6.1 – More on Modules](https://docs.python.org/3/tutorial/modules.html#more-on-modules)
    - [PT 6.1.1 – Executing Modules as Scripts](https://docs.python.org/3/tutorial/modules.html#executing-modules-as-scripts)
    - [PT 6.1.2 – The Module Search Path](https://docs.python.org/3/tutorial/modules.html#the-module-search-path)
    - [PT 6.4 – Packages](https://docs.python.org/3/tutorial/modules.html#packages)

Organizing your code into modules and packages is one of the first steps to
making your code into a project that others might be able to use.

### Licensing

If you want others to use your code, simply making it available (e.g., on
GitHub) is not sufficient. The software needs a license which allows others
to use, modify, and/or redistribute the code. There are many kinds of
_open-source_ licenses, but they generally fall into two groups: permissive
and copyleft (see the MIT and GPL licenses, respectively, linked below).

Licenses are written in legalese that are hard to understand, but the website [https://choosealicense.com/](https://choosealicense.com/) makes it easy. For
instance, you can see simple overviews of the
[MIT](https://choosealicense.com/licenses/mit/) or
[GPL](https://choosealicense.com/licenses/gpl-3.0/) licenses, alongside their
legal text.

Please read what happens if you [don’t choose a license](https://choosealicense.com/no-permission/).

### Testing

As we’ve witnessed in this course already, code that works on one system
might not work well on another. _Software testing_ is the practice of writing
tests to help ensure that code works as intended. There are many kinds of
tests (skim the [Wikipedia article](https://en.wikipedia.org/wiki/Software_testing)
to get an idea), and software testing is a whole career path, but I’d like
you to focus on just a few:

*   Unit testing – ensure each unit (function, module, etc.) is correct
*   Regression testing – ensure behavior of a system is correct over time (i.e., across changes)
*   Integration testing – ensure that parts of the system interact with each other without errors

Please see this [StackOverflow answer](https://stackoverflow.com/a/520116/1441112).

### Documenting

Documentation of code helps others (sometimes the author of the code)
understand how to use it, what its limitations are, or why it is implemented
in a certain way. Please read the following article, which is a good
introduction to the documentation of Python projects: [https://docs.python-guide.org/writing/documentation/](https://docs.python-guide.org/writing/documentation/)

### Distributing

Getting your code into the hands of others is _software distribution_. One way
to do this is to put it up on a public code host, such as GitHub. For Python
projects, you might add them to the [Python Package Index](https://pypi.org/)
(PyPI), which allows them to be installed easily using `pip` (as we have done
in this class, for instance here’s the PyPI entry for the NLTK: [https://pypi.org/project/nltk/](https://pypi.org/project/nltk/)).
Adding projects to PyPI requires some metadata, such as the author,
compatible Python versions, dependencies, etc. Traditionally users would
create a `setup.py` file (see [this tutorial](https://packaging.python.org/tutorials/packaging-projects/#creating-setup-py),
if you’re curious), but recently there have been some more convenient ways
of packaging Python (such as [Flit](https://flit.readthedocs.io/en/latest/)
or [Poetry](https://python-poetry.org/)), which use a new standard file
called `pyproject.toml`.

## Testing Your Knowledge

Go the project page for PyDelphin: [https://github.com/delph-in/pydelphin](https://github.com/delph-in/pydelphin)

Answer the following questions:

*   What is the license of the project?
*   Is it distributed on PyPI?
*   Does it have documentation? If so, where is it at?
*   What is the minimum version of Python required?
*   Did it ever support Python 2? If so, when (or what version) was this
support removed? (hint: which file would you look in for a summary of changes?)
*   Is the project actively developed? (e.g., when was the last commit?)
*   Install the project in a virtual environment with:

    ```bash
    $ pip install pydelphin[web]
    ```

    (the `[web]` part tells it to get some additional dependencies)

    Now try to follow the documentation to get a parse of the sentence “Kim
    left and Sandy had lunch, today.” using the web client.

    *   How many readings (i.e., parses) for the sentence are there?
    *   How many results were returned?
    *   How can you increase the number of results returned?
