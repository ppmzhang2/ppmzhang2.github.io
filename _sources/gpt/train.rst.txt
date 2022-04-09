##############################
GPT-3: Training and Predicting
##############################

.. default-role:: code

.. code-block:: none

   1. input: "The quick brown fox jumps", label: "over"
   2. input: "The quick brown fox jumps over", label: "the"
   3. input: "The quick brown fox jumps over the", label: "lazy"
   4. input: "The quick brown fox jumps over the lazy", label: "dog"

For both the pre-training and fine-tuning:

- unsupervised training

- model: autoregressive, several blocks of transformer decoders

- objective: predict the next word (maximize the probability of the next word)

- the input should include both the sequence of tokens and the mask

- it follows a sentence-by-sentence mode, with each sentence is followed by an
  `EOS` token

Pre-Training
============

- dataset: a total of 300 billion tokens

Meta-Learning
=============

The **meta-learning** is the inner-loop / outer-loop structure in the learning
process. The **in-context learning** refers to the inner loop of meta-learning.

.. code-block:: none

    sequence 1 inner loop (arithmetic)
    3+5=13, 7+2=9, ..., 9+8=17

    sequence 2 inner loop (correct words)
    gaot=>goat, sakne=>snake, dcku=>duck

    ...

    (the end of the outer loop)

- Each inner-loop represents a task to train a specific set of skills, and
  repeated sub-tasks can be embedded within a single sequence

- Meta-learning develops a broad set of skills and pattern recognition
  abilities at training time within the same model

- With these abilities the model can adapt rapidly to desired tasks

- Some of the results are still far inferior to fine-tuning

- The efficiency of meta-learning improves with scale

Questions
---------

- does in-context learning means few-shots?

Examples
========

The demo training code can be found `here
<https://github.com/ppmzhang2/gpt3-study>`_, implemented by leveraging the
transformers package.

Semantic Classification
-----------------------

.. code-block:: none

   Tweet: I hate it when my phone battery dies. Sentiment: Negative
   Tweet: My day has been great so far. Sentiment: Positive
   Tweet: This is the link to the article. Sentiment: Neutral
   Tweet: This new music video was incredible. Sentiment:

   Answer: Positive

Translate a Sentence
--------------------

.. code-block:: none

    Me: Le singe est dans l'arbre Her: The monkey is in the tree
    Me: la plume de ma tante est sur la table Her: My aunt's pen is on the table
    Me: j'aime bien le jambon Her: I like the chair
    Me: Qu'est-ce que c'est que ca? Her: What do you mean?
    Me: Comment tu t'appeles? Her: I am called Bob
    Me: Où est le garçon? Her: Where is the boy?
    Me: Qui est le president des Etats-Unis? Her:

    Answer: Who is the president of the United States?

Netflix Movie Classification
----------------------------

.. code-block:: none

    Description: When Lebanon's Civil War deprives Zozo of his family, he's
    left with grief and little means as he escapes to Sweden in search of
    his grandparents.
    Type: Dramas, International Movies

    Description: A scrappy but poor boy worms his way into a tycoon's
    dysfunctional family, while facing his fear of music and the truth about
    his past.
    Type: Dramas, International Movies, Music & Musicals

    Description: In this documentary, South African rapper Nasty C hits the
    stage and streets of Tokyo, introducing himself to the city's sights,
    sounds and culture.
    Type: Documentaries, International Movies, Music & Musicals

    Description: Dessert wizard Adriano Zumbo looks for the next “Willy
    Wonka” in this tense competition that finds skilled amateurs competing for
    a $100,000 prize.
    Type: International TV Shows, Reality TV

    Description: This documentary delves into the mystique behind the
    blues-rock trio and explores how the enigmatic band created their iconic
    look and sound. Type: Documentaries, International Movies, Music & Musicals
    Type:

    Answer: Documentaries, International Movies, Music & Musicals

Fine-Tune Training
------------------

.. code-block:: none

    ***** Running training *****
      Num examples = 7004
      Num Epochs = 1
      Instantaneous batch size per device = 2
      Total train batch size (w. parallel, distributed & accumulation) = 2
      Gradient Accumulation steps = 1
      Total optimization steps = 3502
    {'loss': 0.4458, 'learning_rate': 3.677248677248677e-05, 'epoch': 0.29}
    {'loss': 0.3704, 'learning_rate': 2.2075249853027632e-05, 'epoch': 0.57}
    {'loss': 0.3546, 'learning_rate': 7.37801293356849e-06, 'epoch': 0.86}
    100%|█████████████████████████████████████████████████████████████████████████████████| 3502/3502 [4:53:35<00:00,  4.90s/it]

    Training completed. Do not forget to share your model on huggingface.co/models =)

    {'train_runtime': 17615.3528, 'train_samples_per_second': 0.398, 'train_steps_per_second': 0.199, 'train_loss': 0.38377865323470295, 'epoch': 1.0}

Back to :doc:`index`.

.. disqus::
