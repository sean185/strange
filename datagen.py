# Events v1 - flat dict of events
# Events v2 - nested dict of events. Nesting accounts within. Changed to absolute time basis.

events = [
    {
        "event_type": "expenses",
        "event_time": 0,
        "amount": 1000,
        "delta_rate": {
            "cash": -1
        }
    },
    {
        "event_type": "new_job",
        "event_time": 6,
        "amount": 3000,
        "delta_rate": {
            "cash": 0.8,
            "cpf": 0.2+0.18
        }
    },
    {
        "event_type": "family_allowance",
        "event_time": 6,
        "amount": 300,
        "delta_rate": {
            "cash": -1
        }
    },
    {
        "event_type": "pay_raise",
        "event_time": 6+12,
        "amount": 500,
        "delta_rate": {
            "cash": 0.8,
            "cpf": 0.2+0.18
        }
    },
    {
        "event_type": "insurance",
        "event_time": 6+12,
        "amount": 2000,
        "delta_balance": {
            "cash": -1,
            "insurance": 1            
        },
        "delta_rate": {
            "cash": -0.1,
            "insurance": 0.1
        }
    },
    {
        "event_type": "bto",
        "event_time": 6+12+2*12,
        "amount": 20000,
        "delta_balance": {
            "cash": -1
        }
    },
    {
        "event_type": "marriage",
        "event_time": 6+12+2*12+2*12,
        "amount": 40000,
        "delta_balance": {
            "cash": -1
        }
    }
]

