=========
robdollar
=========


.. image:: https://img.shields.io/pypi/v/robdollar.svg
        :target: https://pypi.python.org/pypi/robdollar

.. image:: https://img.shields.io/travis/retroam/robdollar.svg
        :target: https://travis-ci.org/retroam/robdollar

.. image:: https://readthedocs.org/projects/robdollar/badge/?version=latest
        :target: https://robdollar.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/retroam/robdollar/shield.svg
     :target: https://pyup.io/repos/github/retroam/robdollar/
     :alt: Updates


command line tool for feature selection



Features
--------

* Basic recursive feature selection with Lasso
* Data quality checks


To run
--------

1. Clone locally::

    $ git clone git@github.com:retroam/robdollar.git

2. Install your local copy into a virtualenv. Assuming you have virtualenvwrapper installed, this is how you set up your fork for local development::

    $ mkvirtualenv robdollar
    $ cd robdollar/
    $ python setup.py develop

3. Run CLI client::

   $ robdollar file target --verbose

example::

    $ robdollar test.csv 0 --verbose

Credits
---------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage

