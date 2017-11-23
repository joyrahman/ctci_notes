class Solution(object):
    def maxProfit(self, prices, fee):
        cash, hold = 0, -prices[0]
        for i in range(1, len(prices)):
            cash = max(cash, hold + prices[i] - fee)
            hold = max(hold, cash - prices[i])
        return cash


def main():
    prices = [1, 3, 2, 8, 4, 9]
    fee = 2
    S = Solution()
    print(S.maxProfit(prices, fee))


if __name__ == "__main__":
    main()
