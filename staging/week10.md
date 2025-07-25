---
title: 'Week 10'
---

## Learning Objectives

*   Concepts:
    [pos tagging]{.nlp}
    [baseline systems]{.nlp}
    [backoff]{.nlp}
    [automatic evaluation]{.nlp}
    [statistical inference]{.nlp}

(color key: [Python/Programming]{.py} [NLP/CL]{.nlp} [Software Engineering]{.eng})

## Reading

*   [NLTK 5.4 – Automatic Tagging](http://www.nltk.org/book/ch05.html#automatic-tagging)
*   [NLTK 5.5 – N-Gram Tagging](http://www.nltk.org/book/ch05.html#n-gram-tagging)
*   [NLTK 5.7 – How to Determine the Category of a Word](http://www.nltk.org/book/ch05.html#how-to-determine-the-category-of-a-word)

## Additional Reading

*   [Cross-validation](https://en.wikipedia.org/wiki/Cross-validation_(statistics))

    K-fold cross validation is a common practice in NLP:

    > In K-fold cross-validation, the original sample is randomly partitioned
    into K subsamples. Of the K subsamples, a single subsample is retained as
    the validation data for testing the model, and the remaining K − 1
    subsamples are used as training data. The cross-validation process is then
    repeated K times (the folds), with each of the K subsamples used exactly
    once as the validation data. The K results from the folds then can be
    averaged (or otherwise combined)

    E.g., 5-fold: split into A, B, C, D, E

    *   Fold 1: Train on A, B, C, D — test on E
    *   Fold 2: Train on A, B, C, E — test on D
    *   Fold 3: Train on A, B, D, E — test on C
    *   Fold 4: Train on A, C, D, E — test on B
    *   Fold 5: Train on B, C, D, E — test on A
*   [NLTK 5.6 – Transformation-based Tagging](http://www.nltk.org/book/ch05.html#transformation-based-tagging)


## Testing Your Knowledge

### Questions

*   **Q:** What do you think makes a good baseline system?

*   **Q:** What is the purpose of having backoff taggers? Or, in what
situations is a backoff tagger used?

*   **Q:** Why is an n-gram tagger conditioned on the previous tags and not
on the previous words?


### Practical Work

*   Train a bigram tagger with no backoff tagger, and run it on some of the
training data. Next, run it on some new data. What happens to the performance
of the tagger? Why?

        TRAIN (input is tagged sentences):
        bigram_tagger = nltk.BigramTagger(train_sents)
        TAG (input is an untagged sentence):
        bigram_tagger.tag(unseen_sent)
        EVALUATE (input is tagged sentences):
        bigram_tagger.evaluate(test_sents)

*   Now add a backoff tagger (your choice) and try it again (build then
evaluate). What happens to the performance of the tagger this time and why?

    backoff = ???

    bigram\_taggert2 = nltk.BigramTagger(train\_sents, backoff=backoff\_tagger)

*   Think about how we could deal with sparseness by defining an ‘unknown’
word. What would you have to do to the training and test data?
