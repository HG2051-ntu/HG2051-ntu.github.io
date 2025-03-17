---
title: 'HG2051 (AY24 Sem 2) Project 2: Group assignment'
---

## Introduction

This project constitutes 30% of your final grade for HG2051. Please work on the
final program in groups of 2-3 and report together.

- The goal of this assignment is to demonstrate your programming and
problem-solving abilities through teamwork. If your team has an idea for
another project that you would like to do instead, talk to me for approval.

- This project involves text classification using machine learning tools. As
with the individual project, your team will be required to submit data, output,
and annotated code along with a short writeup that describes your goals,
process, and results. Your code will be assessed based on its functionality and
simplicity.

## Project 2: Text classification

Text classification is a general term for automatically identifying properties
of a text based on its linguistic content. For this project you will develop a
program that classifies short SMS messages based on whether they are `spam` or
not (`ham`). The initial project code in this repository will help you to get
started, along the following lines (more detail is found in your project README
on Github):

1. The corpora you will primarily be using are located in the `datasets` subfolder of your repository, and a brief explanation of each are given in your Github repository. The [SMS spam collection from UCI](https://archive.ics.uci.edu/ml/datasets/sms+spam+collection) will be the set of data that you will use for training and testing the classifier.

2. Create a list of words based on the labels of the short texts. Once you have sorted and filtered the words, write a function that uses these words in conjunction with the NLTK classifier to classify the messages and improve on the base score. This process is known as feature selection/engineering - the goal of the project is to implement other "features" that you can identify which might improve your classification. Some ideas for sentiment analysis of movie reviews can be found [here](https://realpython.com/python-nltk-sentiment-analysis/#selecting-useful-features). Keep in mind that successfully differentiating between real and fake messages/emails may require different features than for differentiating between the sentiment of movie reviews.

3. Once you have determined the features that you want to extract, write a function that automatically extracts these features from the text as a dictionary. Then use the function to create a list of tuples, where the first item of the tuple is the dictionary of features and the second item is the category/classification ("ham" or "spam") of the text.

4. Split the dataset for training and validation to see how/whether your features improve classification using, i.e. the Naive Bayes classification algorithm in NLTK. It is important that whatever classifier you use, the training data is kept separate from the testing/validation set, otherwise you are simply letting the model "memorize" inputs (overfitting) and it will not generalize well to other datasets.

5. Once you have a model that you think works pretty well on the SMS dataset, test its accuracy on the email dataset (which you have not used for training) to see how well it classifies email texts as ham/spam. At this point, you can train your classifier on the complete SMS dataset, since your email dataset is being used for testing (it is 'unseen'). You can also incorporate other datasets into your training data. Your team's ultimate goal is to improve the accuracy of your classifier on the unseen email dataset.

6. This code is simply a starting point for exploration. What other features can you think of and implement to improve accuracy? How does the accuracy improve with different splits? Try to implement other classifiers and see how they perform on this dataset. Are there other lexical resources/corpora or algorithms within NLTK or from other sources that can improve your results? What is the best accuracy you can get? How does the genre of text (sms/emails) affect your classifier's results?

7. With your group, write a roughly 5-page paper (no longer than 10 pages) describing your goals, data, process, and results, and discussing some of the concerns identified in point 6. This paper should include relevant linguistic information and citations for your sources. Submit the paper as a PDF along with your annotated/commented Python code in a Github repository. The PDF should also be submitted via TurnItIn.
