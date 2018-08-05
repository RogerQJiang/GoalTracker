import datetime as dt
from collections import defaultdict

class Goal():
    def __init__(self, name, outcome, completion, importance, start_date, end_date):
        self.name       = name
        self.outcome    = outcome
        self.completion = completion
        self.importance = importance
        self.start_date = start_date
        self.end_date   = end_date
    
    def __repr__(self):
        return self.name

financial_independence = Goal(
    name       = "Financial Independence",
    outcome    = "$1m Equity",
    completion = "some",
    importance = "high",
    start_date = None,
    end_date   = dt.date(2025, 1, 1)
)

investment_returns = Goal(
    name       = "Investment returns",
    outcome    = "15% p.a. on average",
    completion = "some",
    importance = "high",
    start_date = None,
    end_date   = dt.date(2023, 1, 1)
)

income = Goal(
    name       = "Income",
    outcome    = "$300k p.a.",
    completion = "some",
    importance = "high",
    start_date = None,
    end_date   = dt.date(2023, 1, 1)
)

higher_education = Goal(
    name       = "Higher Education",
    outcome    = "HD masters",
    completion = "some",
    importance = "high",
    start_date = None,
    end_date   = dt.date(2021, 6, 1)
)

new_job = Goal(
    name       = "New Growth Job",
    outcome    = "$100k + 1 day off + personal development",
    completion = "some",
    importance = "high",
    start_date = None,
    end_date   = dt.date(2018, 12, 1)
)

personal = Goal(
    name       = "Personal",
    outcome    = None,
    completion = None,
    importance = None,
    start_date = None,
    end_date   = None
)

root = Goal(
    name       = "Root",
    outcome    = None,
    completion = None,
    importance = None,
    start_date = None,
    end_date   = None
)

goals = defaultdict(list)
goals[root].append(financial_independence)
goals[root].append(personal)
goals[financial_independence].append(investment_returns)
goals[financial_independence].append(income)
goals[income].append(higher_education)
goals[income].append(new_job)