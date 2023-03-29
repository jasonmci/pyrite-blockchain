class EscrowContract:
    def __init__(self, buyer: str, seller: str, amount: int):
        self.buyer = buyer
        self.seller = seller
        self.amount = amount
        self.released = False

    def release(self):
        if not self.released:
            self.released = True
            return f"{self.buyer} releases {self.amount} coins to {self.seller}"
        else:
            return "Escrow has already been released."

    def __str__(self):
        return f"Escrow between {self.buyer} and {self.seller} for {self.amount} coins"