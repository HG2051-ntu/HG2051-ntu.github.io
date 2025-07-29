---
title: 'HG2051 Project 1: Individual assignment'
---

# Introduction

This project constitutes 30% of your final grade for HG2051. Please work on the final program and report individually. Your code will be assessed based on its functionality, simplicity, and efficiency. Your writeup will be assessed based on its organization, clarity, and comprehensiveness as well as the quality of the reflections and discussion.

*   The goal of this assignment is to demonstrate your programming and reasoning abilities by working on a problem individually. If you have an idea for another project that you would like to do instead, talk to me for approval.

*   Project 1 involves developing resources for an under-resourced language. Submission requirements include your data, output, and annotated code along with a short writeup describing your goals, process, and results. Additionally, this project dovetails with the group project ([Project 2](project2.html)), which means you may want to determine your group ahead of time so that all members can choose related languages to work on for the individual project.


## Project 1: Part of Speech tagging for low-resource languages

Part of speech (POS) tagging is a way to automatically identify the word class of a particular lexical item in a string of text. A decent part of speech tagger can help to facilitate other downstream tasks such as machine translation. Languages that are widely used have more resources in this regard, but what about for languages with few speakers?

* The purpose of this project is to expand on annotated data that can be used to train a POS-tagger for a language with few NLP resources. The project will help you think through the steps necessary for developing the correct kind of data, as well as how to write code that can assist with this annotation, and will additionally require you to gain some expertise in the low-resource language you have chosen. In Project 2, the data may be used to actually develop a POS-tagger for this language using existing tools in the NLTK library.

* Our primary data source will be the *[taggedPBC](https://github.com/lingdoc/taggedPBC/)*, a dataset that has been created to support crosslinguistic research. This dataset has been automatically tagged for POS and dependencies by leveraging machine translation models to transfer information from English to nearly 2,000 languages. However, due to the nature of the source and target languages, there is a large amount of noise in this dataset: while nouns and verbs are identified with decent accuracy across languages, other word types are not, partly due to the fact that English contains word classes (like articles) *not present* in many languages, while at the same time it does not contain word classes (like numeral classifiers) that *are present* in many languages.

> for an example of what the data looks like, click [here](https://github.com/lingdoc/taggedPBC/blob/main/corpora/conllu/nyb-eng-tagged-nyb-x-bible_parsed.conllu).

* This means that there is much room to improve the annotations of each individual corpus in this dataset. While the "gold-standard" typically involves hand-tagging corpora, automated pipelines can greatly speed up this process.

The initial project code in your personal repository for this assignment will help you to get started, along the following lines.

### Choose your language and data

The first step in developing a POS-tagger is finding texts that can be used to train and validate it. For this we are using the *taggedPBC* data, but we need to choose a language to work on. To find a language, please view options at the following URL: [HG2051 Project languages](project_lgs_HG2051.html)

Listed languages are organized by language family. Selecting the language family on the linked page will show you the names of the languages of that family that are found in the *taggedPBC*, along with basic information, a direct link to the corpus, and links to additional sources regarding the language. As this project is a precursor to your group project, you may want to find others who are interested in working on languages within the same family, since this will help you to pool your expertise for Project 2. These languages have also been selected based on their lack of available resources, to ensure that we are maximizing our contributions to the field of NLP.

> **IMPORTANT**: *For this project you may not work on the same language as another student. Email the instructor with your preferred choice (ISO 639-3 code and name). This will be on a first-come-first-served basis. If you choose a language that proves extremely difficult to work with, please contact the instructor at the earliest opportunity to explore other options.*

#### Get the base text for the low-resource language

Once your language choice has been approved, download the linked CoNNL-U corpus and copy/move it to your personal project repository. Make sure to `add`, `commit`, and `push` the changes to update your personal Github repository with the corpus. This will be the main data file that your work is based on.

#### Understand the code

Starter code in your repo parses the CoNLL-U file and allows you to modify the output. You should first read through the code and try to understand how it works: how does the code extract existing words and POS tags? how are particular verses extracted?

#### Understand the language

Look for existing research on this language. Since the data comes from a Bible translation, there should be at least one or two papers describing some aspect(s) of the language. Existing research may be found via the `Ethnologue` and `Glottolog` links in the [list of languages](project_lgs_HG2051.html).

#### Identify POS tags in the dataset

Examine the POS tags present in the dataset. Based on existing literature, consider whether the POS tags are appropriate for this language. What additional POS tags might be required for this language?

#### Think through the problem

Think through the steps that would be required to develop an automated POS tagger for this dataset. What additional resources might be necessary? What steps would be needed to POS-tag the data? How would you evaluate the quality of a POS tagger for this language?

### Extract verses for annotation

Write or modify code that extracts a list of verses (given in your starter code) for observation and writes them to a file. Create a subdirectory in your repo to store the file.

### Annotate the sub-corpus

Using whatever additional resources you can find, annotate the sub-corpus, modifying it with more accurate annotations based on the existing research you sourced. You may want to include the additional resources as files in your repository or subdirectory. Determine whether you can use automated means (i.e. a dictionary replacement) for this process, or whether you need to do hand-annotation, or both. Make sure that you describe and discuss your process in your writeup. At minimum, you should add/update POS tags and/or glosses.

### Output

Your submission should include code, several text files, and a writeup. More details of the requirements for these will be given in your individual GitHub repository. In your writeup, consider the quality of the annotations you were able to develop.
