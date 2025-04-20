---
title: "Appendix B: Setup Jupyter Lab Environment"
---

# Appendix B: Setup Jupyter Lab Environment

## Prerequisites

- python
- R
- Julia
- Git

## Install Jupyter Lab and Kernels

### Python

```bash
pip install jupyter jupyterlab
```

### R

```R
install.packages('devtools')
install.packages(c('repr', 'IRdisplay', 'evaluate', 'crayon', 'pbdZMQ', 'uuid', 'digest'))
# make sure git is installed
devtools::install_github('IRkernel/IRkernel')
IRkernel::installspec()
```

### Julia

```Julia
using Pkg
Pkg.update()
Pkg.add("IJulia")
```

## Known Issues

- `conda` slow solving environment
  - solving package dependencies
  - create a fresh environment
- permission denied when installing R packages
  - Install in a terminal
- `python` commands not found (Windows)
  - edit `PATH` environment variable
  - `C:\\Users\\johndoe\\AppData\\Local\\Programs\\Python\\Python311\\scripts`

---

Back to {doc}`index`.

```{disqus}

```
