# Mockup of simulator

import copy
import pandas as pd
import matplotlib.pyplot as plt

from datagen import events

START = 23 * 12       ## 24 years into life
END = 30 * 12         ## retirement age

# TODO :: Think about concepts of acceleration / velocity / dollar
ACCOUNTS = ['cash', 'cpf', 'insurance', 'total_earned']

class Simulator():
    balances = { acc:0 for acc in ACCOUNTS }
    rates = { acc:0 for acc in ACCOUNTS }
    time_current = 0
    result = []

    def __init__(self, START, END):
        # self.time_current = START
        self.end_month = END - START

    def increment(self):
        for acc, rate in self.rates.items():
            self.balances[acc] += rate
        self.time_current += 1
        newstate = copy.deepcopy(self.balances)
        newstate['month'] = self.time_current
        return newstate

    def advance(self, duration):
        states = [self.increment() for _ in range(duration)]
        self.result.extend(states)

    def run(self, events):
        # TODO :: vectorize this run
        # initialize 
        newstate = copy.deepcopy(self.balances)
        newstate['month'] = self.time_current
        self.result.append(newstate)
        for event in events:
            # advance in time to the present
            duration = event["event_time"] - self.time_current
            self.advance(duration)

            # alter the present state of rates
            if 'delta_rate' in event:
                for acc, mult in event['delta_rate'].items():
                    actual_amount = event['amount'] * mult
                    self.rates[acc] += actual_amount
                    if mult > 0:
                        self.rates['total_earned'] += actual_amount

            # alter the present state of balances
            if 'delta_balance' in event:
                for acc, mult in event['delta_balance'].items():
                    actual_amount = event['amount'] * mult
                    self.balances[acc] += actual_amount
                    if mult > 0:
                        self.balances['total_earned'] += actual_amount

        # finish calculating the remaining time
        self.advance(self.end_month - self.time_current)

if __name__ == '__main__':
    # Actually run this
    scenario = Simulator(START, END)
    scenario.run(events)
    df = pd.DataFrame(scenario.result)

    df['year'] = (START+df['month']) / 12
    df.drop('month', axis=1, inplace=True)
    df.set_index('year', inplace=True)
    df.plot()

    plt.show()
