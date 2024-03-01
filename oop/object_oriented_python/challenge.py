# Challenge:

# [x] Create a class to represent stock information.
# [x] Your class should have properties for:
# [x] Ticker (string)
# [x] Price (float)
# [x] Company (string)
# [] And a method get_description() which returns a string in the form
#    of "Ticker: Company -- $Price"

class Stock:
    def __init__(self, ticker, price, company):
        self.ticker = ticker
        self.price = price
        self.company = company

    def get_description(self):
        return (f"{self.ticker}: {self.company} -- £{self.price}")

# ~~~~~~~~~ TEST CODE ~~~~~~~~~
msft = Stock("MSFT", 342.0, "Microsoft Corp")
goog = Stock("GOOG", 135.0, "Google Inc")
meta = Stock("META", 275.0, "Meta Platforms Inc")
amzn = Stock("AMZN", 135.0, "Amazon Inc")

print(msft.get_description())
print(goog.get_description())
print(meta.get_description())
print(amzn.get_description())