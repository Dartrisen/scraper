import requests, time
from bs4 import BeautifulSoup

class CryptoPrices(object):
    url    = "https://bankiros.ru/crypto"
    prices = []

    def _getHtml(self):
        html = requests.get(self.url).text
        return html

    def _parseHtml(self, html):
        soup    = BeautifulSoup(html, "html.parser")
        table   = soup.find("table", {"class" : "crypto_table"})

        rows = []
        for row in table.findAll("tr"):
            cells = []
            for cell in row.findAll("td"):
                text = cell.text
                cells.append(text)
            rows.append(cells)

        del rows[0]
        return rows

    def _getPricesFromSite(self):
        self.prices = self._parseHtml(self._getHtml())

    def getPrices(self):
        return self.prices

    def getPrice(self, price):
        for item in self.prices:
            if (price in item):
                return item[0:2]
            else:
                pass
        print("Crypt not found!")

    def clear(self):
        self.prices.clear()

    def __init__(self):
        self._getPricesFromSite()

def main():
    crypto = CryptoPrices()
    crypts =["BitcoinBTC", "Ethereum ETH", "LitecoinLTC",
            "MoneroXMR", "Ethereum ClassicETC", "RippleXRP",
            "Bitcoin Cash / BCCBCH", "EOSEOS", "NEONEO",
            "DigitalCashDASH", "ZCashZEC", "IOTAIOT",
            "OmiseGoOMG", "Bitcoin GoldBTG", "TronixTRX",
            "StellarXLM", "SantimentSAN", "TetherUSDT",
            "VergeXVG", "ViberateVIB"]
    print("Please choose required crypt:")
    for item in crypts:
        print(item)
    crypt = input()
    while True:
        #TODO regular expressions
        if (crypto.getPrice(crypt)):
            print(crypto.getPrice(crypt))
            time.sleep(10)
        else:
            crypt = input()

if __name__ == '__main__':
    main()