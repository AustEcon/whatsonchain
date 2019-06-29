import json
import requests

DEFAULT_TIMEOUT = 30


class Whatsonchain:
    """
    Access to the Whatsonchain API as per: https://developers.whatsonchain.com/

    :param network: select 'main', 'test', or 'stn'
    :type network: ``str``
    """

    def __init__(self, network='main', api_key=None):
        self.api_key = api_key
        self.network = network
        self.headers = self._get_headers()
        self.authorized_headers = self._get_authorized_headers()

    def _get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
        }

    def _get_authorized_headers(self):
        headers = self._get_headers()
        headers['api_key'] = self.api_key
        return headers

    # Health
    def get_woc_status(self):
        """returns 'what's on chain' if online"""
        r = requests.get('https://api.whatsonchain.com/v1/bsv/{}/woc'.format(self.network),
                         headers=self.headers,
                         timeout=DEFAULT_TIMEOUT)
        r.raise_for_status()
        return r.text

    # Chain info
    def get_chain_info(self):
        """returns 'what's on chain' if online"""
        r = requests.get('https://api.whatsonchain.com/v1/bsv/{}/chain/info'.format(self.network),
                         headers=self.headers,
                         timeout=DEFAULT_TIMEOUT)
        r.raise_for_status()
        return r.json()

    # Block
    def get_block_by_hash(self, _hash):
        r = requests.get('https://api.whatsonchain.com/v1/bsv/{}/block/hash/{}'.format(self.network, _hash),
                         headers=self.headers,
                         timeout=DEFAULT_TIMEOUT)
        r.raise_for_status()
        return r.json()

    def get_block_by_height(self, _height):
        r = requests.get('https://api.whatsonchain.com/v1/bsv/{}/block/height/{}'.format(self.network, _height),
                         headers=self.headers,
                         timeout=DEFAULT_TIMEOUT)
        r.raise_for_status()
        return r.json()

    def get_block_by_hash_pages(self, _hash, page_number):
        """Only to be used for large blocks > 1000 txs. Allows paging through lists of transactions.
        Returns Null if there are not more than 1000 transactions in the block"""
        r = requests.get('https://api.whatsonchain.com/v1/bsv/{}/block/hash/{}/page/{}'.format(self.network, _hash, page_number),
                         headers=self.headers,
                         timeout=DEFAULT_TIMEOUT)
        r.raise_for_status()
        return r.json()

    # Transactions
    def get_transaction_by_hash(self, _hash):
        r = requests.get('https://api.whatsonchain.com/v1/bsv/{}/tx/hash/{}'.format(self.network, _hash),
                         headers=self.headers,
                         timeout=DEFAULT_TIMEOUT)
        r.raise_for_status()
        return r.json()

    def broadcast_rawtx(self, rawtx):
        # FIXME not actually tested yet
        """Broadcasts a rawtx to testnet"""
        json_payload = json.dumps({"txHex": rawtx})
        r = requests.post('https://api.whatsonchain.com/v1/bsv/{}/tx/raw'.format(self.network),
                          data=json_payload,
                          headers=self.headers,
                          timeout=DEFAULT_TIMEOUT)
        r.raise_for_status()
        return r.json()

    def download_receipt(self, _hash):
        r = requests.get('https://{}.whatsonchain.com/receipt/{}'.format(self.network, _hash),
                         headers=self.headers,
                         timeout=DEFAULT_TIMEOUT)
        r.raise_for_status()
        return r.json()

    # Mempool
    def get_mempool_info(self):
        r = requests.get('https://api.whatsonchain.com/v1/bsv/{}/mempool/info'.format(self.network),
                         headers=self.headers,
                         timeout=DEFAULT_TIMEOUT)
        r.raise_for_status()
        return r.json()

    def get_mempool_transactions(self):
        r = requests.get('https://api.whatsonchain.com/v1/bsv/{}/mempool/raw'.format(self.network),
                         headers=self.headers,
                         timeout=DEFAULT_TIMEOUT)
        r.raise_for_status()
        return r.json()

    # Address
    def get_address_info(self, address):
        r = requests.get('https://api.whatsonchain.com/v1/bsv/{}/address/{}/info'.format(self.network, address),
                         headers=self.headers,
                         timeout=DEFAULT_TIMEOUT)
        r.raise_for_status()
        return r.json()

    def get_balance(self, address):
        r = requests.get('https://api.whatsonchain.com/v1/bsv/{}/address/{}/balance'.format(self.network, address),
                         headers=self.headers,
                         timeout=DEFAULT_TIMEOUT)
        r.raise_for_status()
        return r.json()

    def get_history(self, address):
        r = requests.get('https://api.whatsonchain.com/v1/bsv/{}/address/{}/history'.format(self.network, address),
                         headers=self.headers,
                         timeout=DEFAULT_TIMEOUT)
        r.raise_for_status()
        return r.json()

    def get_utxos(self, address):
        r = requests.get('https://api.whatsonchain.com/v1/bsv/{}/address/{}/unspent'.format(self.network, address),
                         headers=self.headers,
                         timeout=DEFAULT_TIMEOUT)
        r.raise_for_status()
        return r.json()

    def download_statement(self, address):
        r = requests.get('https://{}.whatsonchain.com/statement/{}'.format(self.network, address),
                         headers=self.headers,
                         timeout=DEFAULT_TIMEOUT)
        r.raise_for_status()
        return r.json()

    # Search
    def get_explorer_links(self, address):
        r = requests.post('https://api.whatsonchain.com/v1/bsv/{}/search/links'.format(self.network),
                          json_payload=json.dumps({"query": address}),
                          headers=self.headers,
                          timeout=DEFAULT_TIMEOUT)
        r.raise_for_status()
        return r.json()


class WhatsonchainMainNet(Whatsonchain):
    """
    Whatsonchain API using the main network
    """

    def __init__(self, *args, **kwargs):
        return super().__init__(*args, **kwargs, network='main')


class WhatsonchainTestNet(Whatsonchain):
    """
    Whatsonchain API using the test network
    """

    def __init__(self, *args, **kwargs):
        return super().__init__(*args, **kwargs, network='test')


class WhatsonchainSTN(Whatsonchain):
    """
    Whatsonchain API using the scaling test network
    """

    def __init__(self, *args, **kwargs):
        return super().__init__(*args, **kwargs, network='stn')
