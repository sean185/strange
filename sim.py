# Mockup of simulator

import copy
import pandas as pd
import matplotlib.pyplot as plt

from datagen import events

START = 23 * 12       ## 24 years into life
END = 30 * 12         ## retirement age

# TODO :: Think about concepts of acceleration / velocity / dollar


class Simulator():
    balances = {
        "cash": 0,
        "cpf": 0,
        "insurance": 0
    }
    rates = {
        "cash": 0,
        "cpf": 0,
        "insurance": 0
    }
    time_current = 0
    result = []

    def __init__(self, START, END):
        self.time_current = START
        self.end_month = END

    def increment(self,):
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
        for event in events:
            if event["event_type"] == "start":
                newstate = copy.deepcopy(self.balances)
                newstate['month'] = self.time_current
                self.result.append(newstate)
            elif event["event_type"] == "end":
                # wrap up simulation by extrapolating till the end
                duration = self.end_month - self.time_current
                self.advance(duration)
            else:
                # is there really a need to handle each special type?

                # advance in time to the present
                duration = event["time_delta"]
                self.advance(duration)

                # alter the present state of balances
                self.balances["cash"] += event.get("bal_cash_shift", 0)
                self.balances["cpf"] += event.get("bal_cpf_shift", 0)
                self.balances["insurance"] += event.get("bal_insurance_shift", 0)

                # alter the present state of rates
                self.rates["cash"] += event.get("bal_cash_rate", 0)
                self.rates["cpf"] += event.get("bal_cpf_rate", 0)
                self.rates["insurance"] += event.get("bal_insurance_rate", 0)

# Actually run this
scenario = Simulator(START, END)
scenario.run(events)
df = pd.DataFrame(scenario.result)

df['year'] = df['month'] / 12
df.drop('month', axis=1, inplace=True)
df.set_index('year', inplace=True)
df.plot()

plt.show()