# Mockup of simulator

import copy
import pandas as pd
import matplotlib.pyplot as plt

START = 23 * 12       ## 23 years into life
END = 30 * 12         ## retirement age

# use concepts of acceleration / velocity / dollar

events = [
    {
        "event_type": "start",
        "time_delta": START
    },
    {
        "event_type": "new_job",
        "time_delta": 6,
        "bal_cash_shift": 0,
        "bal_cash_rate": 3000
    },
    {
        "event_type": "expense_familyallowance",
        "time_delta": 0,
        "bal_cash_shift": 0,
        "bal_cash_rate": -300
    },
    {
        "event_type": "salary_increment",
        "time_delta": 12,
        "bal_cash_shift": 0,
        "bal_cash_rate": 3500
    },
    {
        "event_type": "expense_familyallowance",
        "time_delta": 0,
        "bal_cash_shift": 0,
        "bal_cash_rate": -100
    },
    {
        "event_type": "expense_necessities",
        "time_delta": 0,
        "bal_cash_shift": 0,
        "bal_cash_rate": -1000
    },
    {
        "event_type": "expense_luxury",
        "time_delta": 0,
        "bal_cash_shift": 0,
        "bal_cash_rate": -100
    },
    {
        "event_type": "insurance_purchase",
        "time_delta": 6,
        "bal_cash_shift": -2000,
        "bal_cash_rate": -200,
        "bal_insurance_shift": 2000,
        "bal_insurance_rate": 200
    },
    {
        "event_type": "end"
    }
]



class Simulator():
    balances = {
        "cash": 0,
        "insurance": 0
    }
    rates = {
        "cash": 0,
        "insurance": 0
    }
    time_current = 0
    result = []

    def __init__(self, START, END):
        self.start_month = START
        self.end_month = END

    def advance(self, duration):
        for _ in range(duration):
            for acc, rate in self.rates.items():
                self.balances[acc] += rate
                self.time_current += 1
                self.result.append(copy.deepcopy(self.balances))

    def run(self, events):
        for event in events:
            if event["event_type"] == "start":
                self.result.append(copy.deepcopy(self.balances))
            elif event["event_type"] == "end":
                # wrap up simulation by extrapolating till the end
                duration = self.end_month - self.time_current
                self.advance(duration)
            else:
                # is there really a need to handle each special type?

                # advance in time to the present
                duration = event["time_delta"]
                self.advance(duration)

                # alter the present state
                self.balances["cash"] += event.get("bal_cash_shift", 0)
                self.balances["insurance"] += event.get("bal_insurance_shift", 0)
                self.rates["cash"] += event.get("bal_cash_rate", 0)
                self.rates["insurance"] += event.get("bal_insurance_rate", 0)

# Actually run this
scenario = Simulator(START, END)
scenario.run(events)
df = pd.DataFrame(scenario.result)
df.plot()

plt.show()