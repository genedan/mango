from math import sqrt
from typing import List


class Account:
    def __init__(
            self,
            name: str,
            events: list,
            probs: list,
            losses: list
     ):

        self.name = name
        self.events = events
        self.probs = probs
        self.losses = losses

        self.expected_loss = el(
            probs=self.probs,
            losses=self.losses
        )
        self.variance = var(
            probs=self.probs,
            losses=self.losses
        )

        self.std_dev = sqrt(self.variance)


class Portfolio:
    def __init__(
            self,
            name: str,
            accounts: List[Account]
    ):

        self.name = name
        self.accounts = accounts
        self.events = accounts[0].events
        self.probs = accounts[0].probs
        self.losses = []

        for i in range(len(self.events)):
            self.losses += [0]
            for account in accounts:
                self.losses[i] += account.losses[i]

        self.expected_loss = el(
            probs=self.probs,
            losses=self.losses
        )
        self.variance = var(
            probs=self.probs,
            losses=self.losses
        )

        self.std_dev = sqrt(self.variance)


def el(
        probs: list,
        losses: list
) -> float:
    return sum(x * y for x, y in list(zip(probs, losses)))


def var(
        probs: list,
        losses: list
) -> float:
    return sum(x * (1 - x) * (y ** 2) for x, y in list(zip(probs, losses)))