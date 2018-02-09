# Integrate
[![Build Status](https://travis-ci.org/yang15/integrate.svg?branch=master)](https://travis-ci.org/yang15/integrate)
[![codecov](https://codecov.io/gh/yang15/integrate/branch/master/graph/badge.svg)](https://codecov.io/gh/yang15/integrate)
[![Documentation Status](https://readthedocs.org/projects/integrate-jy/badge/?version=latest)](http://integrate-jy.readthedocs.io/en/latest/?badge=latest) 
## Installation
Please run

    pip install -e .

Command add into bash_profile

    parse_git_branch() {
    git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/ (\1)/'
}
    PS1='\[\033[01;32m\]\u\[\033[00m\]:\[\033[01;34m\]\w\[\033[01;31m\]$(parse_git_branch)\[\033[00m\]$ '
