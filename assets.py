import urllib

def printf(format, *values):
    print(format % values )

# crypto
cryptos = {
    "XMR" :  0.0102579,
    "DOGE" : 3441.47197802,
    "LTC" : 0.0393,
    "ETH" : 0.0394,
    "BTC" : 0.0005,
    "BCH" : 0.0
}

# stock
#stocks = {
#    "SBUX": 1.0,
#    "AMD" : 5.0,
#    "CVNA" : 2.0
#}

crypto_keys = {
    "XMR" : "https://coinmarketcap.com/currencies/monero/",
    "DOGE" : "https://coinmarketcap.com/currencies/dogecoin/",
    "LTC" : "https://coinmarketcap.com/currencies/litecoin/",
    "ETH" : "https://coinmarketcap.com/currencies/ethereum/",
    "BTC" : "https://coinmarketcap.com/currencies/bitcoin/",
    "BCH" : "https://coinmarketcap.com/currencies/bitcoin-cash/"
}

total_holds = 0.0;
for key in crypto_keys:
    link = crypto_keys[key]
    f = urllib.urlopen(link)
    myfile = f.read()
    my_holds = cryptos[key]
    if "data-currency-value" in myfile:
        fi = myfile.find("data-currency-value")
        chunk = myfile[fi+15:fi+30]
        fi2 = chunk.find(">")
        fi3 = chunk.find("<")
        value = chunk[fi2+1:fi3]
        this_hold = float(my_holds)*float(value)
        total_holds += this_hold
        printf("%10s: %15s @ $%10s = $%8.2f\n", key, my_holds, value, this_hold)

printf("Total holdings = ~$%8.2f\n",total_holds)
