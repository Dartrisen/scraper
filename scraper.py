import requests, time
from bs4 import BeautifulSoup


class Crypto:
    def __init__(self):
        self.url    = "https://bankiros.ru/crypto"
        self.prices = []
        self.get_prices_from_site()


    def get_Html(self):
        html = requests.get(self.url).text
        return html


    def parse_Html(self, html):
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


    def get_prices_from_site(self):
        self.prices = self.parse_Html(self.get_Html())


    def get_prices(self):
        return self.prices


    def get_price(self, price):
        for item in self.prices:
            if (price in item):
                return item[0:2]
            else:
                pass
        print("Crypt not found!")


    def clear(self):
        self.prices.clear()


def main():
    crypto = Crypto()
    crypts =["BitcoinBTC", "Ethereum ETH", "LitecoinLTC",
            "MoneroXMR", "Ethereum ClassicETC", "RippleXRP",
            "Bitcoin Cash / BCCBCH", "EOSEOS", "NEONEO",
            "DigitalCashDASH", "ZCashZEC", "IOTAIOT",
            "OmiseGoOMG", "Bitcoin GoldBTG", "TronixTRX",
            "StellarXLM", "SantimentSAN", "TetherUSDT",
            "VergeXVG", "ViberateVIB"]

    print("Please choose required crypts (1 2 3 for example):")

    for idx, item in enumerate(crypts, 1):
        print("[{0}], {1}".format(idx, item))

    try:
        idx = input()
        idx_list = list(map(int, idx.split()))
        while True:
            for idx in idx_list:
                print(" ".join(crypto.get_price(crypts[idx-1])))
            time.sleep(10)
    except Exception as e:
        print("Please choose correct number (numbers)")


if __name__ == '__main__':
    main()
