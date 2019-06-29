Whatsonchain API
================

Examples
--------

1. Import whatsonchain and create a 'woc' object for 'main', 'test' or 'stn' networks:

.. code-block:: python

    >>> from whatsonchain import Whatsonchain
    >>> woc = Whatsonchain(network='test')
    >>> woc.get_address_info('mtsCNJGDVgYaVm3je8UpU5nExgiJgkEv6y')
    {'address': 'mtsCNJGDVgYaVm3je8UpU5nExgiJgkEv6y',
     'ismine': False,
     'isscript': False,
     'isvalid': True,
     'iswatchonly': False,
     'scriptPubKey': '76a914926db3be60d18dbaac65785b92a150c37bb4146488ac'}


Installation
------------

Whatsonchain is distributed on `PyPI` as a universal wheel and is available on Linux/macOS
and Windows and supports Python 3.5+ ``pip`` >= 8.1.2 is required.

.. code-block:: bash

    $ pip install whatsonchain  # pip3 if pip is Python 2 on your system.


Credits
-------

- `Whatsonchain`_ for their hard work on the Whatsonchain API

.. _Whatsonchain: https://whatsonchain.com/

Donate
--------

- If you have found this library useful, please consider donating. Every little bit helps.
- HandCash: $AustEcon
- 1PdvVPTzXmo4cSs68HctLUxAdW917UZtC8
