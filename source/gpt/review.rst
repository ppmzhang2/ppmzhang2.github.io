######
Review
######

.. default-role:: code

Paper Review
============

Summary from the paper:

- model scale

  - larger models can typically use a larger batch size, but require a smaller
    learning rate

  - potential contamination of downstream tasks

    - test / development sets inadvertently seen during pre-training

    - remove overlaps

- spurious features

  - these spurious correlations can occur due to biased sampling or artifacts
    in crowd-sourcing. For example, we may have a labeled dataset for
    recidivism prediction where race correlates with recurrence of crime due to
    sample selection bias, but this correlation does not hold on the
    population. Models which learn spurious correlations can generalize poorly
    on population data which does not have these biases. [#f1]_

Critics
=======

Is It Hyped?
------------

Probably not. As the overview states [#f2]_:
"Sampling Can Prove The Presence Of Knowledge But Not The Absence", which means
that the GPT-3 may fail due to misuse.

- try few shots learning over zero shot learning

- tweak hyper-parameters

- design a good prompt

- even a bad choice of the `BOS`, `EOS`, or `PAD` token may have a negative
  impact on performance

Know Its Ignorance
------------------

- it does not know when it will fail

- it may need to be programmed with knowledge about uncertainty

Not an AGI
----------

- it is not about its performance of any specific task

- it lacks most of the perception of the environment

- it lacks social connection

Reference
=========

.. [#f1] https://arxiv.org/abs/2006.10032

.. [#f2] https://towardsdatascience.com/gpt-3-a-complete-overview-190232eb25fd

Back to :doc:`../index`.

.. disqus::
