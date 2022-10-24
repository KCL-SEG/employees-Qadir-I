"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

from pkg_resources import ContextualVersionConflict


class Employee:
    def __init__(self, name, rate, hours = 0, commission = 0, contracts = 0, bonus = 0):
        self.name = name
        self.rate = rate
        self.hours = hours
        self.commission = commission
        self.contracts = contracts
        self.bonus = bonus
        
        
    def get_pay(self):
        pay = 0

        if self.rate:
            pay += self.rate
            if self.hours:
                pay *= self.hours
        
        if self.commission:
            pay += self.commission * self.contracts
        
        if self.bonus:
            pay += self.bonus

        return pay

    def output_pay(self):
        string1 = " works on a "
        if self.hours:
            string1 += f'contract of {self.hours} hours at {self.rate}/hour'
        else:
            string1 += f'monthly salary of {self.rate}'
        
        return string1

    def output_commission(self):
        string2 = ""
        if self.commission:
            string2 = f' and receives a commission for {self.contracts} contract(s) at {self.commission}/contract'
        elif self.bonus:
            string2 = f' and receives a bonus commission of {self.bonus}'
                
        return string2


    def __str__(self):
        string = f"{self.name}{self.output_pay()}{self.output_commission()}."
        string += f" Their total pay is {self.get_pay()}."
        
        return string


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', rate = 4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', rate = 25, hours = 100)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', rate = 3000, contracts = 4, commission = 200)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', rate = 25, hours = 150, contracts = 3, commission = 220)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', rate = 2000, bonus = 1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', rate = 30, hours = 120, bonus = 600)
