---
title: 'HG2051 (AY25 Sem 1) Project 2: Group assignment'
---

## Introduction

This project constitutes 30% of your final grade for HG2051. Please work on the
final program in groups of 2-3 and report together.

- The goal of this assignment is to demonstrate your programming and
problem-solving abilities through teamwork. If your team has an idea for
another project that you would like to do instead, talk to me for approval.

- This project involves developing a POS-tagger for a low-resource language. As
with the individual project, your team will be required to submit data, output,
and annotated code along with a short writeup that describes your goals,
process, and results. Your code will be assessed based on its functionality and
simplicity. Your writeup will be assessed on its organization, clarity,
comprehensiveness, and quality of the discussion.

## Project 2: Part of Speech tagging

As noted in Project 1, part of speech (POS) tagging is a way to automatically
identify the word class of a particular lexical item in a string of text. A
decent part of speech tagger can help to facilitate other downstream tasks such
as machine translation. In the individual project you focused on the process of
developing materials for POS tagging for a low-resource language. In this
project you will work with other students to train a POS-tagger using the data
you annotated, as well as additional data that you will develop or source.

Automated POS-tagging is the process of automatically identifying or classifying
word types in sentences. Typically this is done on the basis of FDA (Function,
Distribution, Associated grammatical categories), as per your Morphosyntax
course. There are two basic approaches: 1) rule-based, 2) statistical inference.
The first approach can be useful for complex cases, particularly when the
language has been analyzed, the second involves machine learning and can be
easier when little is known about the language. Some taggers benefit from a
hybrid approach, and this can be an iterative process.

### Choose the language

In your group, choose one of the low-resource languages that members of your
group worked on for Project 1. Using the dataset, develop a POS-tagger for the
chosen language.

### Determine your approach

Decide how you want to approach the task of developing an automated POS tagger:
will you train a tagger, or write rules, or try some combination of the two?

You also need to consider evaluation/validation of your tagger, which will be
based on the hand-tagged sentences/verses that were annotated in Project 1. The
annotated verses will be data that your tool has not trained on, and will serve
as the "gold standard" evaluation set. In order to train/develop your tagger,
you will need to find or develop additional tagged data, either through other
sources or via hand-annotation. For best results, your training/development data
should be many more sentences (at least twice as many) as your evaluation set.

### Write code to train and evaluate your tagger

Together with your group, develop code that parses the training/development
data and POS-tags the annotated dataset from Project 1, evaluating its accuracy
by comparing the tags with the gold-standard tags.

Starter code in your repository shows how you can use tools in the NLTK library
for training POS-taggers. You can also use other tools/libraries to train a
tagging model, and/or write parsing rules based on your understanding of the
language. The starter code also illustrates how you can evaluate on the "gold
standard" data.

> **BONUS**: *in addition to POS tagging, a central concern when parsing language is
understanding dependencies between word classes. Develop a parser for the language
that identifies dependencies between words, i.e. phrasal heads and their
subordinate elements (for example, nouns are heads of noun phrases, but
dependents of verb phrases, how would you link a particular noun with its head,
and in what role relation [subject, object, etc]?)*

### Output

Your final repository should include:

 - code that trains a tagger on existing data, then parses the (unseen)
 "gold standard" data for the language and outputs tagged data, evaluating
 the automatic tags against the known tags of the "gold standard" data. Code
 should be self-contained, i.e. I should be able to run it in my terminal and
 get output

 - a subfolder containing all the data used for training/testing and
 evaluation, with clear names for each file

 - a writeup that lays out the task, process, and results as well as discussion
