class CoinCounts:
    def __init__(self,friends):
        self.friends = friends

    def giveCoins(self, friend, coins):
        for place in self.friends:
            if friend in place:
                place[1] = int(place[1]) + coins
                break
            else:
                continue

    def getRichestFriends(self):
        name_count = set()
        coin_count = int()
        for friend in self.friends:
            name,coin = friend
            if int(coin) > coin_count:
                coin_count = coin
                name_count = {name}
            elif int(coin) == coin_count:
                name_count.add(name)
            else:
                continue
        return (name_count)

    def fun(self):
        total = {"Friend Count": 0, "coin count":0}
        for friend in self.friends:
            name,coins = friend
            total["Friend Count"].add(1)
            total["coin count"].add(coins)
        return(total)         

cc = CoinCounts([("Amy", 15), ("Jeremy", 23), ("Vanessa", 12)])
print(fun(cc))
