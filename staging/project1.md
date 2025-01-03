---
title: 'HG2051 (AY24/25) Project 1: Individual assignment'
---

## Introduction

This project constitutes 30% of your final grade for HG2051. Please work on the
final program and report individually. Your code will be assessed based on its
functionality and simplicity.

- The goal of this assignment is to demonstrate your programming and reasoning
abilities by working on a problem individually. If you have an idea for another
project that you would like to do instead, talk to me for approval.

- This project involves sorting, searching, and classifying lexical resources.
Submission requirements include your data, output, and annotated code along
with a short writeup describing your goals, process, and results.

## Project 1: Multilingual search

While it is relatively easy to search through a corpus of text to find
particular words/collocations/phrases in a single language, there are very few
search tools that will allow you to find matches based on multiple languages.
For this project you will develop a program that will return matches from
multiple levels of an interlinear text.

1. You will choose two interlinear texts from a low-resource language that have
been glossed and translated into English. The first text is to be used for
developing your tool, and the second is intended to validate your tool. You
will be provided some texts but may choose a different language if you like, the
only requirement being that it must have two interlinearized linguistic texts
with multiple tiers of analysis (i.e. *text*, *gloss*, *part of speech (pos)*).
Some examples include [these Wa texts](https://www.humancomp.org/wadict/vm/texts/)
and [these texts in Nenets](https://negation.univie.ac.at/sprachen/nenzischa.html).
Depending on your source you may need to do more/less processing.

2. Write a Python script that will read in the text, store it, and
allow for a user to search the data on multiple levels simultaneously, i.e.
*text*, *gloss*, *pos*. The idea here is that the user should
be able to query for all `nouns` that have the gloss **dog**, and look at all
sentences with those forms in order to observe the context in which they occur.
The implementation should enable searching using at least two levels of
annotation (i.e. *text*, *gloss*), but will receive a higher score if more than
two annotation levels are supported, as well as if forward and backward
searches (i.e. "all words with POS `n` preceded by POS `clitic`") are possible.
Output should be presented minimally in the terminal or written to a file.

3. Once your Python script is working for the first text, test it on the second
text to make sure that it works, and make any necessary changes so that it works
for both texts. Finally, modify your program so that you can search across both
texts simultaneously. **Bonus:** get it to work on multiple additional texts in
the same format, sourced from the original repository.

4. Write a short paper (no longer than 5 pages) describing your goals,
data, process, and results. This paper should include some background
information on Pnar (or another language you chose), with relevant linguistic
information and citations for your sources. Submit this paper as a PDF along
with your annotated/commented Python code and the texts you chose in a Github
repository. The PDF should also be submitted via TurnItIn. Make sure to provide
examples of your queries and results in the paper or as separate files, and
describe any challenges you faced. Also ensure that your name and matric number
are clearly indicated in your code and in your PDF submission.
