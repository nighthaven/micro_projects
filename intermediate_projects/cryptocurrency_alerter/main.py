from crypto_data import get_coin, Coin

def alert(symbol: str, bottom: float, top: float, coin_list: list[Coin]):
    for coin in coin_list:
        if coin.symbol == symbol:
            if coin.current_price > top or coin.current_price < bottom:
                print(coin, "!!TRIGERED!!")
            else:
                print(coin)

if __name__ == '__main__':
    coins: list[Coin] = get_coin()
    alert("btc", bottom=20_000, top=28_000, coin_list=coins)
    alert("eth", bottom=1800, top=1900, coin_list=coins)
    alert("xpr", bottom=20_000, top=28_000, coin_list=coins)

