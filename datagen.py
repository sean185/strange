# Events v1 - flat dict of events

events = [
    {
        "event_type": "start"
    },
    {
        "event_type": "new_job",
        "time_delta": 6,
        "bal_cash_shift": 0,
        "bal_cash_rate": 3000
    },
    {
        "event_type": "cpf_adjustment",
        "time_delta": 0,
        "bal_cash_shift": 0,
        "bal_cash_rate": -0.2*3000
    },
    {
        "event_type": "cpf_adjustment",
        "time_delta": 0,
        "bal_cpf_rate": 0.2*3000
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
        "bal_cash_rate": 500
    },
    {
        "event_type": "cpf_adjustment",
        "time_delta": 0,
        "bal_cash_shift": 0,
        "bal_cash_rate": -0.2*500
    },
    {
        "event_type": "cpf_adjustment",
        "time_delta": 0,
        "bal_cpf_rate": 0.2*500
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
        "event_type": "bto",
        "time_delta": 2*12,
        "bal_cpf_shift": -20000
    },
    {
        "event_type": "marriage",
        "time_delta": 2*12,
        "bal_cash_shift": -40000
    },
    {
        "event_type": "end"
    }
]

