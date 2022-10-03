#########
Reference
#########

.. default-role:: code

Papers
======

- The original GPT-3 paper
  `Language Models are Few-Shot Learners <https://arxiv.org/abs/2005.14165>`_:
  it is the ultimate resource to understand the new techniques applied by Open
  AI.

- The GPT-2 paper `Language Models are Unsupervised Multitask Learners
  <https://d4mucfpksywv.cloudfront.net/better-language-models/language_models_are_unsupervised_multitask_learners.pdf>`_:
  the GPT-3 model remains largely the same as the GPT-2 counterpart.

- `Attention Is All You Need <https://arxiv.org/abs/1706.03762>`_: introduced
  the encoder-decoder transformer, which is the most tricky part of the GPT
  model.

Implementation
==============

- `The Annotated GPT-2
  <https://amaarora.github.io/2020/02/18/annotatedGPT2.html>`_ is an annotated
  version of the GPT-2 paper with plenty of `PyTorch` code.

- This `GitHub repo
  <https://github.com/huggingface/pytorch-openai-transformer-lm>`_ is an
  `PyTorch` implementation of the GPT-2 by `Hugging Face
  <https://huggingface.co/>`_.

- The `minGPT <https://github.com/karpathy/minGPT>`_ is a minimal `PyTorch`
  re-implementation.

- Yet another `GPT-2 implementation
  <https://github.com/graykode/gpt-2-Pytorch>`_ via `PyTorch`

- `The Annotated Transformer
  <https://nlp.seas.harvard.edu/2018/04/03/attention.html>`_ explains in code
  how the transformer is implemented, and is endorsed by the author of "The
  Annotated GPT-2".

- The `PyTorch` tutorial

  - `tutorial
    <https://pytorch.org/tutorials/beginner/transformer_tutorial.html>`_ on
    training a sequence-to-sequence model that uses the `nn.Transformer`
    module.

APIs
====

OpenAI API
----------

The document [#f1]_ of the official OpenAI library:

- Text Completion

- Edit / Correct Inputs

- Similarity Comparison

- Classification

- Text Comprehension

- Embedding

- Fine-tuning

Transformers
------------

The transformers from `Hugging Face <https://huggingface.co/>`_ provides APIs
to download and train pre-trained models, including GPT-2 and GPT Neo.

Fine-Tuning
===========

- This `150kb text
  <https://uploads-ssl.webflow.com/60b2f56a556ad23e9c414ec8/61591f6661b89431b78faf3b_elon-musk.txt>`_
  contains podcast transcripts of Elon Musk.

- This `post
  <https://medium.com/ai-innovation/beginners-guide-to-retrain-gpt-2-117m-to-generate-custom-text-content-8bb5363d8b7f>`_ shows how to retrain the GPT-2 model.

Other Sources
=============

- The post `The GPT-3 Architecture, on a Napkin
  <https://dugas.ch/artificial_curiosity/GPT_architecture.html>`_ explains as
  detailed as possible on the GPT-3 architecture, which is super useful.

- This `article <https://www.fullstackpython.com/gpt-3.html>`_ is an entry
  point of several GPT-3 related resources, including application tutorials.

- Alberto Romero's medium

  - `A Complete Overview of GPT-3
    <https://towardsdatascience.com/gpt-3-a-complete-overview-190232eb25fd>`_

  - `Understanding GPT-3 In 5 Minutes
    <https://towardsdatascience.com/understanding-gpt-3-in-5-minutes-7fe35c3a1e52>`_

- Jay Alammar's blog

  - `How GPT3 Works
    <https://jalammar.github.io/how-gpt3-works-visualizations-animations/>`_

  - `The Illustrated GPT-2 <https://jalammar.github.io/illustrated-gpt2/>`_

  - `The Illustrated Transformer
    <https://jalammar.github.io/illustrated-transformer/>`_

  - `Mechanics of Seq2seq Models With Attention
    <https://jalammar.github.io/visualizing-neural-machine-translation-mechanics-of-seq2seq-models-with-attention/>`_

- GPT-J

  - `How to Fine-Tune GPT-J
    <https://www.forefront.ai/blog-posts/how-to-fine-tune-gpt-j>`_

Reference
=========

.. [#f1] https://beta.openai.com/docs/api-reference

Back to :doc:`index`.

.. disqus::
