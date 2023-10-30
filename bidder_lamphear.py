import random


class Bidder:
    """Class to keep track of number of users and number of rounds
    contains bid method and notifies winner:
    price is the amount of the second bid, which the winner pays
    """
    def __init__(self, num_users, num_rounds):
        self.num_users = num_users
        self.num_rounds = num_rounds
        self.balance = 0
        self.user_id = None

    def bid(self, user_id):
        # Returns non-negative amount of $, rounded to 3 decimals
        bid_amount = round(random.uniform(0, 10), 3)
        return bid_amount

    def notify(self, auction_winner, price, clicked):
        # Does notification about the action outcome
        if auction_winner:
            if clicked:
                self.balance += 1 - price
            else:
                self.balance -= price
        return self.balance
