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

Unicode Encoding
================

All the strings are in **UTF-8** format, which guarantees that each valid
character is represented by one to four one-byte (8-bit) code units. This means
any UTF-8 string can be represented via a 8-bit (256) alphabet.

.. code-block:: python

    def bytes_to_unicode():
        bs = list(range(ord("!"),
                        ord("~") + 1)) + list(range(
                            ord("??"),
                            ord("??") + 1)) + list(range(ord("??"),
                                                        ord("??") + 1))
        cs = bs[:]
        n = 0
        for b in range(2**8):
            if b not in bs:
                bs.append(b)
                cs.append(2**8 + n)
                n += 1
        cs = [chr(n) for n in cs]
        return dict(zip(bs, cs))


This program keeps the ASCII printable characters all remain in their position
except for space, which is mapped to `??` (U+0120).

.. code-block:: python

    {
        0: "??", 1: "??", 2: "??", 3: "??", 4: "??", 5: "??", 6: "??", 7: "??",
        8: "??", 9: "??", 10: "??", 11: "??", 12: "??", 13: "??", 14: "??", 15: "??",
        16: "??", 17: "??", 18: "??", 19: "??", 20: "??", 21: "??", 22: "??", 23: "??",
        24: "??", 25: "??", 26: "??", 27: "??", 28: "??", 29: "??", 30: "??", 31: "??",
        32: "??", 33: "!", 34: '"', 35: "#", 36: "$", 37: "%", 38: "&", 39: "'",
        40: "(", 41: ")", 42: "*", 43: "+", 44: ",", 45: "-", 46: ".", 47: "/",
        48: "0", 49: "1", 50: "2", 51: "3", 52: "4", 53: "5", 54: "6", 55: "7",
        56: "8", 57: "9", 58: ":", 59: ";", 60: "<", 61: "=", 62: ">", 63: "?",
        64: "@", 65: "A", 66: "B", 67: "C", 68: "D", 69: "E", 70: "F", 71: "G",
        72: "H", 73: "I", 74: "J", 75: "K", 76: "L", 77: "M", 78: "N", 79: "O",
        80: "P", 81: "Q", 82: "R", 83: "S", 84: "T", 85: "U", 86: "V", 87: "W",
        88: "X", 89: "Y", 90: "Z", 91: "[", 92: "\\", 93: "]", 94: "^", 95: "_",
        96: "`", 97: "a", 98: "b", 99: "c", 100: "d", 101: "e", 102: "f", 103: "g",
        104: "h", 105: "i", 106: "j", 107: "k", 108: "l", 109: "m", 110: "n", 111: "o",
        112: "p", 113: "q", 114: "r", 115: "s", 116: "t", 117: "u", 118: "v", 119: "w",
        120: "x", 121: "y", 122: "z", 123: "{", 124: "|", 125: "}", 126: "~", 127: "??",
        128: "??", 129: "??", 130: "??", 131: "??", 132: "??", 133: "??", 134: "??", 135: "??",
        136: "??", 137: "??", 138: "??", 139: "??", 140: "??", 141: "??", 142: "??", 143: "??",
        144: "??", 145: "??", 146: "??", 147: "??", 148: "??", 149: "??", 150: "??", 151: "??",
        152: "??", 153: "??", 154: "??", 155: "??", 156: "??", 157: "??", 158: "??", 159: "??",
        160: "??", 161: "??", 162: "??", 163: "??", 164: "??", 165: "??", 166: "??", 167: "??",
        168: "??", 169: "??", 170: "??", 171: "??", 172: "??", 173: "??", 174: "??", 175: "??",
        176: "??", 177: "??", 178: "??", 179: "??", 180: "??", 181: "??", 182: "??", 183: "??",
        184: "??", 185: "??", 186: "??", 187: "??", 188: "??", 189: "??", 190: "??", 191: "??",
        192: "??", 193: "??", 194: "??", 195: "??", 196: "??", 197: "??", 198: "??", 199: "??",
        200: "??", 201: "??", 202: "??", 203: "??", 204: "??", 205: "??", 206: "??", 207: "??",
        208: "??", 209: "??", 210: "??", 211: "??", 212: "??", 213: "??", 214: "??", 215: "??",
        216: "??", 217: "??", 218: "??", 219: "??", 220: "??", 221: "??", 222: "??", 223: "??",
        224: "??", 225: "??", 226: "??", 227: "??", 228: "??", 229: "??", 230: "??", 231: "??",
        232: "??", 233: "??", 234: "??", 235: "??", 236: "??", 237: "??", 238: "??", 239: "??",
        240: "??", 241: "??", 242: "??", 243: "??", 244: "??", 245: "??", 246: "??", 247: "??",
        248: "??", 249: "??", 250: "??", 251: "??", 252: "??", 253: "??", 254: "??", 255: "??",
    }

Tokenization
============

It is a process of splitting text (e.g. a phrase, a sentence, or a paragraph)
into smaller units. [#f1]_ There are three different tokenization techniques
based on the token size.

- word-based

- character-based

- subword-based

Each token will have a unique identifier, through which the token embedding
vector can be looked up. To keep a high coverage percentage the size of the
vocabulary must grow as the size of token increases, and for word-based
tokenization large number of tokens will be tagged as OOV (out of vocabulary).

If the token size is reduced to one character, however, each individual element
will have very little meaning, and a sentence, for instance, must be
represented by a token sequence much longer.

The subword-based technique takes the token size / sequence length trade-off,
if it can split words into meaningful subwords. The split policy that the GPT-3
adopted is Byte Pair Encoding (**BPE**).

Initial Splitting
-----------------

A sentence will be truncated into words before the BPE. Valid words including:

- suffixes like `'s`, `'t`, `'re`, `'ve`, `'m`, `'ll`, `'d`

- word with only letters

- number

- signs / unicode sequence with no space, letter or number

- only spaces

.. code-block:: python

    self.pat = re.compile(
        r"""'s|'t|'re|'ve|'m|'ll|'d| ?\p{L}+| ?\p{N}+| ?[^\s\p{L}\p{N}]+|\s+(?!\S)|\s+"""
    )

Byte Pair Encoding (BPE)
------------------------

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

- the additive law of the token entries: the main operation for word embedding
  vectors is multiplication rather than addition.

Positional Encoding (WPE)
=========================

For each token in the 2048 input slots, its position is encoded passing the
index (from 0 to 2047) to **12288** sinusoidal functions of different frequencies.
The output is a **2048-by-12288** position encoded matrix.

Encoding Combination
====================

Both the embedding matrix and position encoded matrix are **2048-by-12288**
matrices, and the final input to the model will be the sum of them.

Reference
=========

.. [#f1] https://towardsdatascience.com/word-subword-and-character-based-tokenization-know-the-difference-ea0976b64e17

Back to :doc:`index`.

.. disqus::
