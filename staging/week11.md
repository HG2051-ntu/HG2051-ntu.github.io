---
title: 'Week 11'
---

## Learning Objectives

*   Concepts:
    [machine learning]{.eng}
    [supervised learning]{.eng}
    [unsupervised learning]{.eng}
    [classification]{.eng}
    [evaluation]{.eng}
    [decision trees]{.eng}
    [entropy]{.eng}
    [linguistic features]{.nlp}

(color key: [Python/Programming]{.py} [NLP/CL]{.nlp} [Software Engineering]{.eng})

## Reading

*   [NLTK 6 – Learning to Classify Text](http://www.nltk.org/book/ch06.html)
    *   [NLTK 6.1 – Supervised Classification](http://www.nltk.org/book/ch06.html#supervised-classification)
    *   [NLTK 6.3 – Evaluation](http://www.nltk.org/book/ch06.html#evaluation)
    *   [NLTK 6.4 – Decision Trees](http://www.nltk.org/book/ch06.html#decision-trees)
    *   [NLTK 6.7 – Modeling Linguistic Patterns](http://www.nltk.org/book/ch06.html#modeling-linguistic-patterns)
    *   [NLTK 6.8 – Summary](http://www.nltk.org/book/ch06.html#summary)

This week covers an introduction to **machine learning**. Last week we looked
at part-of-speech taggers that were trained by looking at examples of
gold-standard pos-tagged words, and these were a kind of very basic
**supervised classification** based on **statistical inference**. Machine
learning also uses statistical inference, but often it builds multi-dimensional
models using a variety of **features** of data instances instead of just
counting them. For example, instead of just counting to find the most frequent
part-of-speech tag for some word, we could consider additional features such as
whether the word is capitalized, whether it appears after the word “to”, or the
domain of the sentence (e.g., “news”, if it is known). Using all of these
features as conditions would make a conditional frequency distribution too
sparse to be useful (the features/conditions are too discriminating to get a
model that generalizes to unseen data), so instead these features are used in
a way that does not **overfit** to the training data.

## Additional Reading

*   [NLTK 6.2 – Further Examples of Supervised Classification](http://www.nltk.org/book/ch06.html#further-examples-of-supervised-classification)
*   [NLTK 6.5 – Naive Bayes Classifiers](http://www.nltk.org/book/ch06.html#naive-bayes-classifiers)
*   [NLTK 6.6 – Maximum Entropy Classifiers](http://www.nltk.org/book/ch06.html#maximum-entropy-classifiers)
*   [What is AI? Part 1: Automated Inference](https://youtu.be/Hu1E9qJsXQ4)

Testing Your Knowledge
----------------------

### Questions

*   **Q:** What does training data need to be used for supervised classification?

*   **Q:** What are _features_ in a machine learning model?

*   **Q:** Why is _overfitting_ a problem?

*   **Q:** How is a _development set_ different from a _test set_?


### Practical Work

*   Try to split the Brown corpus into train, dev, and test sets, but try to
make representative of the corpus. Think about features you might use to split
the instances (e.g., the category, length of sentence, perplexity, etc.)

*   Build a part-of-speech tagger using a Decision Tree, Naive Bayes, or
Maximum Entropy classifier (pick one, or all three). Design your features,
train your model, evaluate.
