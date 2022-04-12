#####################
GPT-3: Input Encoding
#####################

.. default-role:: code

.. code-block:: none

    GPT-3 Input Encoding

                                    <---------- 50257 ---------->

                                    ============= 1 =============
                                    ============= 2 =============
                                    ============ ... ============
                                    ============ 2048 ===========

                                   |||                         |||
                                   |||                         |||
                                  \|||/                       \|||/
                                   \|/                         \|/

                             token embedding           positional encoding
                                  (WTE)                       (WPE)

                             <--- 12288 --->             <--- 12288 --->

                             ====== 1 ======             ====== 1 ======
                             ====== 2 ======             ====== 2 ======
                             ===== ... =====             ===== ... =====
                             ===== 2048 ====             ===== 2048 ====

                                    |                           |
                                    |                           |
                                    -----------------------------
                                                 |||
                                                 |||
                                                \|||/
                                                 \|/

                                               plus (+)

                                           <--- 12288 --->

                                           ====== 1 ======
                                           ====== 2 ======
                                           ===== ... =====
                                           ===== 2048 ====

The input text will go through an embedding / encoding process, which will map
the string into a matrix:

- input text string

  .. code-block:: python

      "python primer plus"

- tokenized strings

  .. code-block:: python

      ["python", "prim", "er", "plus"]

- each token will be mapped to a token ID, ranging from **0** to **50256**

  .. code-block:: python

      [2, 4, 6, 101]

- each token ID will be mapped to a 12288-dimension vector (GPT-3)

Once tokenized, each of the input tokens will have two groups of properties:

- semantic properties as a sub-word, indicated by its token index ranging from
  **0** to **50256**

- positional properties as an element in a sequence, indicated by its
  positional index ranging from **0** to **2047**

The semantic properties will be interpreted by a "dictionary" in the form of a
matrix, and

Byte Pair Encoding (BPE)
========================

Suppose we feed the byte-pair encoder a word `workflow`. It first split the
word into characters and pair the neighbouring ones:

+--------+--------+-------+
| prefix | suffix | index |
+========+========+=======+
| w      | o      | 0     |
+--------+--------+-------+
| o      | r      | 1     |
+--------+--------+-------+
| r      | k      | 2     |
+--------+--------+-------+
| k      | f      | 3     |
+--------+--------+-------+
| f      | l      | 4     |
+--------+--------+-------+
| l      | o      | 5     |
+--------+--------+-------+
| o      | w      | 6     |
+--------+--------+-------+

Add rank:

+--------+--------+-------+-------+
| prefix | suffix | index | rank  |
+========+========+=======+=======+
| w      | o      | 0     | 21382 |
+--------+--------+-------+-------+
| o      | r      | 1     | 17    |
+--------+--------+-------+-------+
| r      | k      | 2     | n.a.  |
+--------+--------+-------+-------+
| k      | f      | 3     | n.a.  |
+--------+--------+-------+-------+
| f      | l      | 4     | 2448  |
+--------+--------+-------+-------+
| l      | o      | 5     | 5183  |
+--------+--------+-------+-------+
| o      | w      | 6     | 66    |
+--------+--------+-------+-------+

Merge top ranked pair (`o` and `r`):

+--------+--------+-------+
| prefix | suffix | index |
+========+========+=======+
| w      | or     | 0     |
+--------+--------+-------+
| or     | k      | 2     |
+--------+--------+-------+
| k      | f      | 3     |
+--------+--------+-------+
| f      | l      | 4     |
+--------+--------+-------+
| l      | o      | 5     |
+--------+--------+-------+
| o      | w      | 6     |
+--------+--------+-------+

Re-rank:

+--------+--------+-------+------+
| prefix | suffix | index | rank |
+========+========+=======+======+
| w      | or     | 0     | n.a. |
+--------+--------+-------+------+
| or     | k      | 2     | 711  |
+--------+--------+-------+------+
| k      | f      | 3     | n.a. |
+--------+--------+-------+------+
| f      | l      | 4     | 2448 |
+--------+--------+-------+------+
| l      | o      | 5     | 5183 |
+--------+--------+-------+------+
| o      | w      | 6     | 66   |
+--------+--------+-------+------+

Merge top ranked pair (`o` and `w`) and re-rank:

+--------+--------+-------+------+
| prefix | suffix | index | rank |
+========+========+=======+======+
| w      | or     | 0     | n.a. |
+--------+--------+-------+------+
| or     | k      | 2     | 711  |
+--------+--------+-------+------+
| k      | f      | 3     | n.a. |
+--------+--------+-------+------+
| f      | l      | 4     | 2448 |
+--------+--------+-------+------+
| l      | ow     | 5     | 9063 |
+--------+--------+-------+------+

Merge top ranked pair (`or` and `k`) and re-rank:

+--------+--------+-------+------+
| prefix | suffix | index | rank |
+========+========+=======+======+
| w      | ork    | 0     | 1562 |
+--------+--------+-------+------+
| ork    | f      | 3     | n.a. |
+--------+--------+-------+------+
| f      | l      | 4     | 2448 |
+--------+--------+-------+------+
| l      | ow     | 5     | 9063 |
+--------+--------+-------+------+

Merge top ranked pair (`w` and `ork`) and re-rank:

+--------+--------+-------+------+
| prefix | suffix | index | rank |
+========+========+=======+======+
| work   | f      | 3     | n.a. |
+--------+--------+-------+------+
| f      | l      | 4     | 2448 |
+--------+--------+-------+------+
| l      | ow     | 5     | 9063 |
+--------+--------+-------+------+

Merge top ranked pair (`f` and `l`) and re-rank:

+--------+--------+-------+-------+
| prefix | suffix | index | rank  |
+========+========+=======+=======+
| work   | fl     | 3     | n.a.  |
+--------+--------+-------+-------+
| fl     | ow     | 5     | 10869 |
+--------+--------+-------+-------+

Merge top ranked pair (`fl` and `ow`) and re-rank:

+--------+--------+-------+------+
| prefix | suffix | index | rank |
+========+========+=======+======+
| work   | flow   | 3     | n.a. |
+--------+--------+-------+------+

There no pair can be merged and the output should be both the prefix and the
suffix.

Token Embedding (WTE)
=====================

To interpret a word we could use a dictionary and in the case of the GPT-3
training the "dictionary" is actually a **50257-by-12288** matrix, each row of
which is a **12288-dimension** vector, containing distance information with
other tokens

The GPT-3 has 2048 input slots and after tokenisation there the input will be
a **2048-by-50257** matrix. By multiplying the input matrix with the vocabulary
matrix mentioned above we have a **2048-by-12288** embedded matrix.

Questions
---------

- does the token entries obey the additive law?

Positional Encoding (WPE)
=========================

For each token in the 2048 input slots, its position is encoded passing the
index (from 0 to 2047) to **12288** sinusoidal functions of different frequencies.
The output is a **2048-by-12288** position encoded matrix.

Encoding Combination
====================

Both the embedding matrix and position encoded matrix are **2048-by-12288**
matrices, and the final input to the model will be the sum of them.

Back to :doc:`index`.

.. disqus::
