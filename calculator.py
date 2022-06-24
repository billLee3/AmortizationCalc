class Calculator:
    def __init__(self, year_count, interest_rate, purchase_price, down_payment):
        self.number_of_periods = year_count * 12
        self.interest_rate = interest_rate
        self.rate_per_period = self.interest_rate / 12
        self.down_payment = down_payment
        self.principal = purchase_price - self.down_payment

    def _calculate_monthly_payment(self):
        numerator = self.rate_per_period * ((1 + self.rate_per_period) ** self.number_of_periods)
        denominator = ((1 + self.rate_per_period) ** self.number_of_periods) - 1
        monthly_payment = self.principal * (numerator / denominator)
        return monthly_payment