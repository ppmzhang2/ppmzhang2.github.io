---
title: "Appendix A: Setup R Environment"
---

# Appendix A: Setup R Environment

R is a free software environment for statistical computing and graphics.
Most of its precompiled binary distributions can be found on the
[Comprehensive R Archive Network (CRAN)](https://cran.r-project.org/).

## Download and Install R

### Debian / Ubuntu

Packages for the base R system has been integrated into these
distributions:

```bash
apt-get install r-base
```

### CentOS and RHEL

R packages are available in the EPEL repositories:

```bash
yum install epel-release
yum install R
```

### OpenSUSE / SLE

The OpenSUSE / SLE release users can find the latest R-base package in
[this devel
project](https://build.opensuse.org/project/show/devel:languages:R:released).
After adding matched repository, install R and all dependencies:

```bash
zypper install R-base
```

### OS X

The [CRAN](https://cran.r-project.org/bin/macosx/) provide `pkg`
installers supporting various macOS versions.

Alternatively, you can install via a package manager like `homebrew`:

```bash
brew install r
```

### Windows

Download from the [CRAN
page](https://cran.r-project.org/bin/windows/base/) the installer and
run.

### Verification

```bash
R --version
```

You should have a similar output if your installation is successful:

```sh
R version 4.2.2 (2022-10-31) -- "Innocent and Trusting"
Copyright (C) 2022 The R Foundation for Statistical Computing
Platform: aarch64-apple-darwin22.1.0 (64-bit)

R is free software and comes with ABSOLUTELY NO WARRANTY.
You are welcome to redistribute it under the terms of the
GNU General Public License versions 2 or 3.
For more information about these matters see
https://www.gnu.org/licenses/.
```

## RStudio IDE

It is recommanded to code with an integrated development environment
(IDE), which can be found on the [official
website](https://posit.co/download/rstudio-desktop/). Likewise, one can
install the IDE with a package manager

```bash
brew install --cask rstudio
```

## Reference

1.  <https://cran.r-project.org>
2.  <https://build.opensuse.org/project/show/devel:languages:R:released>
3.  <https://posit.co/>

---

Back to {doc}`index`.

```{disqus}

```
