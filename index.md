---
title: Language and the Computer (AY2024-25)
instructor:
  - name: Hiram Ring
    email: hiram.ring@ntu.edu.sg
date: "Thursdays, 9:30am-12:20pm (Sem1)"
location: >
  [TR+29](https://maps.ntu.edu.sg/#/ntu/d386ffa80e4e46f286d17f08/poi/details/e97bc9bf4c6740ca8f3d35cc) (LHS-B2-06, The Hive)

abstract: >
  Traditionally linguistic analysis was done largely by hand, but
  computer-based methods and tools are becoming increasingly widely
  used in contemporary research. This course provides an introduction
  to skills and resources to assist the linguist in performing
  fast, flexible, and accurate quantitative analyses. Students will
  learn a programming language (Python) along with techniques for
  processing human language data. No previous programming experience
  is required: we will teach you the basics of programming and
  computational linguistics along with some good software engineering
  practices.

schedule:
  - week: 1
    date: 15 Aug
    topic: What is Computational Linguistics? Why do it? Why use Python?<br>Computer Science basics
    url: week1.html
    notes: "[Setup](environment-setup.html), [VS_Code](using-vscode.html)"

  - week: 2
    date: 22 Aug
    topic: Basic Types and Data Structures; Using Python to Count Things; Lists
    url: week2.html
    notes: "[PyT 3.1](https://docs.python.org/3/tutorial/introduction.html#using-python-as-a-calculator); [NLTK 1](https://www.nltk.org/book/ch01.html)"

  - week: 3
    date: 29 Aug
    topic: Assignment, Expressions, and Control; Strings
    url: week3.html
    notes: "[PyT 3.2](https://docs.python.org/3/tutorial/introduction.html#first-steps-towards-programming), [4](https://docs.python.org/3/tutorial/controlflow.html); [NLTK 4.1](http://www.nltk.org/book/ch02.html#wordlist-corpora)"

  - week: 4
    date: 5 Sep
    topic: Text Corpora and Conditional Frequencies
    url: week4.html
    notes: "[DIP 2.2](https://diveintopython3.problemsolving.io/native-datatypes.html#booleans),  [2.8](https://diveintopython3.problemsolving.io/native-datatypes.html#none); [PT 5.3](https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences), [5.5](https://docs.python.org/3/tutorial/datastructures.html#dictionaries), [4.7.1](https://docs.python.org/3/tutorial/controlflow.html#default-argument-values)-[2](https://docs.python.org/3/tutorial/controlflow.html#keyword-arguments); [NLTK 2.1](http://www.nltk.org/book/ch02.html#accessing-text-corpora)-[2](http://www.nltk.org/book/ch02.html#conditional-frequency-distributions); [lecture](static/week4-lecture.py), [practice](static/week4-practice.py)"

  - week: 5
    date: 12 Sep
    topic: Lexical Resources and WordNet
    url: week5.html
    notes: "[NLTK 2.4](http://www.nltk.org/book/ch02.html#lexical-resources), [2.5](http://www.nltk.org/book/ch02.html#wordnet), ([How To](http://www.nltk.org/howto/wordnet.html)); [lecture](static/week5-lecture.py); [practice](static/week5-practice.py)"
    # notes: "[notebook](static/week5-practice.ipynb)"

  - week: 6
    date: 19 Sep
    topic: Processing Raw Text
    url: week6.html
    notes: "[NLTK 3.1](http://www.nltk.org/book/ch03.html#accessing-text-from-the-web-and-from-disk), [3.3](http://www.nltk.org/book/ch03.html#text-processing-with-unicode); [PT 7.1-7.3](https://docs.python.org/3/tutorial/inputoutput.html#fancier-output-formatting); [lecture](static/week6-lecture.py); [practice](static/week6-practice.py)"
    # notes: "[notebook](static/week6-practice.ipynb)"

  - week: 7
    date: 26 Sep
    topic: Mid-review; Working with Software Projects
    url: week7.html
    notes: "[Coding challenge](quiz1.html); [PT 6](https://docs.python.org/3/tutorial/modules.html), [6.4](https://docs.python.org/3/tutorial/modules.html#packages)"
    #[Midterm Quiz](static/quiz1_modelsolution.py)"

  - week: --
    date: 03 Oct
    topic: Recess
    cancelled: true

  - week: 8
    date: 10 Oct
    topic: Algorithmic Thinking and Regular Expressions
    url: week8.html
    notes: "[NLTK 3.4](http://www.nltk.org/book/ch03.html#regular-expressions-for-detecting-word-patterns), [5](http://www.nltk.org/book/ch03.html#useful-applications-of-regular-expressions), [6](http://www.nltk.org/book/ch03.html#normalizing-text), [7](http://www.nltk.org/book/ch03.html#regular-expressions-for-tokenizing-text), [8](http://www.nltk.org/book/ch03.html#segmentation); [lecture](static/week8-lecture.py); [practice](static/week8-practice.py)"

  - week: 9
    date: 17 Oct
    topic: N-Grams and Collocations
    url: week9.html
    notes: "[NLTK 4.5](http://www.nltk.org/book/ch04.html#higher-order-functions), [5](http://www.nltk.org/book/ch05.html); [lecture](static/week9-lecture.py); [practice](static/week9-practice.py)"

  - week: 10
    date: 24 Oct
    topic: Part-of-speech Tagging
    url: week10.html
    notes: "[NLTK 5.4](http://www.nltk.org/book/ch05.html#automatic-tagging), [5](http://www.nltk.org/book/ch05.html#n-gram-tagging), [7](http://www.nltk.org/book/ch05.html#how-to-determine-the-category-of-a-word); [practice](static/week10-practice.py)"

  - week: --
    date: 31 Oct
    topic: Deepavali
    cancelled: true

  - week: 11
    date: 07 Nov
    topic: Classification
    url: week11.html
    notes: "[NLTK 6.2](http://www.nltk.org/book/ch06.html#further-examples-of-supervised-classification), [5](http://www.nltk.org/book/ch06.html#naive-bayes-classifiers), [6](http://www.nltk.org/book/ch06.html#maximum-entropy-classifiers), [What is AI?](https://youtu.be/Hu1E9qJsXQ4); [Project 1](project1.html) due, 11:59pm"
    # [practice](static/week11-practice.py), [enamdict](static/code/enamdict); "

  - week: 12
    date: 14 Nov
    topic: Ethics, Language Models, and Software Libraries
  # url: week12.html

  - week: 12
    date: 15 Nov
    topic: Alternate Final Quiz date
    notes: "[Coding challenge](quiz2.html)"

  - week: 13
    date: 21 Nov
    topic: Review and Final Quiz
    # url: final-review.html
    notes: "[Coding challenge](quiz2.html)"

  - week: --
    date: 28 Nov
    topic: Project 2 due, 11:59pm
    url: project2.html
  # url: week14.html
  # notes: ""
    cancelled: true
---

## Course Pages

- [Environment Setup](environment-setup.html) -- instructions for setting up your computer for HG2051
- [Using Visual Studio Code](using-vscode.html) -- how to get, complete, and submit assignments
- [Glossary](glossary.html) -- definitions of some technical terms

## Grading Criteria

This course is graded with continuous assessment as follows:

- Homework (autograded)
- Project 1 -- 30%
- Project 2 -- 30%
- Mid-term Quiz -- 15%
- Final Quiz -- 15%
- Participation -- 10%

You may also get 1--5% extra credit (not exceeding 100% in the course)
by submitting a contribution (e.g., code or documentation) to an
open-source project. Contact me for details.

## Resources

- Python -- <https://www.python.org/>
  - The Python Tutorial (official docs) -- <https://docs.python.org/3/tutorial/>
  - The Python Standard Library (official docs) -- <https://docs.python.org/3/library/index.html>
  - Learn Python in 10 Minutes (quick guide) -- <https://www.stavros.io/tutorials/python/>
  - Learn Python the Hard Way (beginner's guide) -- <https://learnpythonthehardway.org/book/>
  - Dive Into Python 3 (free ebook) -- <https://diveintopython3.problemsolving.io/>
- Git -- <https://git-scm.com/>
  - Official documentation (manuals, cheat sheets, videos) -- <https://git-scm.com/doc>
- GitHub -- <https://github.com/>
  - GitHub Guides -- <https://guides.github.com/>
- Visual Studio Code -- <https://code.visualstudio.com/>
  - Documentation -- <https://code.visualstudio.com/docs>
  - Using Python in VS Code -- <https://code.visualstudio.com/docs/python/python-tutorial>
  - Working with Jupyter Notebooks in Visual Studio Code -- <https://code.visualstudio.com/docs/python/jupyter-support>
- NLTK -- <http://www.nltk.org/>
  - Natural Language Processing with Python (free ebook) -- <http://www.nltk.org/book/>
- StackOverflow (popular programming Q&A site)-- <https://stackoverflow.com/>

## Acknowledgments

The majority of the content for this course has been borrowed (with
permission) from Michael Wayne Goodman and Francis Bond, who taught
previous years. Below are some of the archives of the previous courses:

- Hiram Ring:
  [2022](https://hg2051-ntu.github.io/AY2022/),
  [2023](https://hg2051-ntu.github.io/AY2023/)
- Michael Wayne Goodman:
  [2019](https://compling.hss.ntu.edu.sg/courses/hg2051/),
  [2020](https://ntu-hg2051.github.io/)
- Francis Bond:
  2010,
  2011,
  2012,
  2013,
  2015,
  [2017](http://compling.hss.ntu.edu.sg/courses/hg2051.2017/)
