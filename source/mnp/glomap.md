---
title: GLOMAP MnP Representation
---

# GLOMAP MnP Representation

## TL;DR

```none
                               +------------------------------------------+
                               |             Nucleation Mode              |
                               +------------------------------------------+
                               |                                          |
                               |             (No MPs allowed)             |
                               | MPs not emitted here due to size (>5 µm) |
                               |                                          |
                               +------------------------------------------+
                                             |                      |

                                            \|/                    \|/
                                      +-------------+          +----------+
                                      |  Fragments  |          |  Fibers  |
                                      +-------------+          +----------+
                                             |                      |

                                             |       emittion       |

                            +- - - - - - - - + - - - - - - - -+     |

                            |                                 |     |

                           \|/                               \|/   \|/
+-------------------------------------------------------------------------+
|                          Insoluble Modes                                |
+-------------------------------------------------------------------------+
|                                                          |              |
|         coagulation                 coagulation          |              |
| Aitken -------------> Accumulation -------------> Coarse | Super-Coarse |
|            growth                      growth            |              |
|                                                          |              |
+----------------------------------------------------------+--------------+
                            |

                            |
            aging / condensation (soluble coating)
                            |

                           \|/
+----------------------------------------------------------+
|                       Soluble Modes                      |
+----------------------------------------------------------+
|                                                          |
|         coagulation                 coagulation          |
| Aitken -------------> Accumulation -------------> Coarse |
|            growth                      growth            |
|                                                          |
+----------------------------------------------------------+
```

_Figure 1. Scheme of the GLOMAP MnP representation.
In UKESM1.1, microplastics are added to GLOMAP as fragments and fibres.
Fragments enter all insoluble modes (except nucleation);
fibres only the super-coarse mode.
Fragments can age into soluble modes.
All particles undergo dry and wet deposition._

## Explanation

- Check in Terminology for definitions [modes](#rec-aerosol-mode) and
  [MnP particle types](#rec-mnp-particle-types).
- Emission: MPs are emitted directly into all insoluble modes except nucleation.
- Super-coarse insoluble mode has no pathway to soluble modes via aging.
- Aging process: Involves accumulation of soluble species (e.g., sulfate)
  forming 10+ monolayers, enabling [CCN](#rec-ccn) activation.
- Coagulation occurs across modes and alters particle size and lifetime.
- Deposition: All modes are subject to dry and wet deposition.
  - Soluble particles are more efficiently removed via wet deposition due to
    CCN activation.
- Limitations: Fibres currently modeled as spherical, which underrepresents
  their atmospheric lofting. This is a known area for future improvement.

Back to {doc}`index`.

```{disqus}

```
