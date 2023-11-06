import random


class User:
    """User class where user is created, secret probability
    is drawn from a uniform distribution from 0 to 1"""
    def __init__(self):
        self.__probability = random.uniform(0, 1)

    def show_ad(self):
        # Check outcome of user clicking on the ad based on probability
        return random.random() < self.__probability


class Auction:
    """This class executes all steps within a single round of
    the game. The balance attribute contains a dictionary of the
    current balance of every bidder"""
    def __init__(self, users, bidders):
        self.users = users
        self.bidders = bidders
        # initialize with all bidders
        self.active_bidders = list(range(len(bidders)))

        # Starts each Bidder with balance of 0 and tracks balance
        self.balances = {bidder_id: 0 for bidder_id in self.active_bidders}

    def execute_round(self):
        # Step 1: Randomly select a User
        user_id = random.randint(0, len(self.users) - 1)
        chosen_user = self.users[user_id]

        # Step 2: Bidders place bids
        bids = {}
        for bidder_id in self.active_bidders:
            bid_amount = self.bidders[bidder_id].bid(user_id)
            bids[bidder_id] = bid_amount

        # Step 3: Find winning bidder
        winning_bidders = [bidder_id for bidder_id in self.active_bidders if bids[bidder_id] == max(bids.values())]
        winning_bidder_id = random.choice(winning_bidders)
        winning_bid = bids[winning_bidder_id]

        # Step 4: Determing winning price/find 2nd-highest bid:
        sorted_bids = sorted(bids.values(), reverse=True)
        winning_price = max(sorted_bids[1], winning_bid)

        # Step 5: Run show_ad method from User class
        clicked = chosen_user.show_ad()

        # Step 6: Notify top bidder of full results
        for bidder_id in self.active_bidders:
            won = (bidder_id == winning_bidder_id)

            # Notify winner. Rest of bidders should get only the price
            if won:
                bidder_notify = self.bidders[bidder_id].notify(won, winning_price, clicked)
            # else:
            #     bidder_notify = self.bidders[bidder_id].notify(winning_price)

        # # Step 7: Update balance
        if clicked:
            self.balances[winning_bidder_id] += 1
        self.balances[winning_bidder_id] -= winning_price

        # Prevent negative balances
        if self.balances[winning_bidder_id] < 0:
            self.balances[winning_bidder_id] = 0
