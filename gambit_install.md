# Installing Gambit from source: Tutorial

This is the gambit installation instruction guide

Mainly based on https://stackoverflow.com/questions/30286551/cant-build-gambit-game-theory-extension
  
  
1. Get repository from Github

    * git clone git://github.com/gambitproject/gambit.git 
    * cd gambit

2. Set up build scripts by executing:
    1. Steps    
        * aclocal
        * libtoolize
        * automake --add-missing
        * autoconf
    2. Problems
        * make sure 'make' is installed next to automake, autoconf and libtool
        * Before running aclocal, run 'mkdir m4'

3. Edit files which will contain errors further on
    * "library/src/agg/agg.cc" needs some changes, see https://github.com/gambitproject/gambit/pull/260/files
    * nash.py file needs to be changed, see https://github.com/gambitproject/gambit/blob/8d1699952efda9637685d70817074443912ba18c/src/python/gambit/nash.py

4. Installing gambit
    1. Steps
        * ./configure
        * make
        * sudo make install
    2. Problems 
       * installs gambit in /usr/local but works. Might consider choosing different path

5. Installing Python API
    1. Steps
        * cd src/python
        * python3 setup.py build
        * sudo python3 setup.py install

    2. Problems: 
       *Make sure to install setuptools, Cython3 (not regular Cython when working with Python 3.X), IPython, and scipy

6. Running tests
    * Install nosetests3, or run with 'python3 -m "nose" ' in the /src/python/gambit/tests directory