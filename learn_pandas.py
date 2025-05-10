import pandas as pd 

top_10_billionaires = {
    1: {"name": "Bernard Arnault & family", "net_worth_usd_billions": 233, "source": "LVMH", "country": "France"},
    2: {"name": "Elon Musk", "net_worth_usd_billions": 195, "source": "Tesla, SpaceX", "country": "United States"},
    3: {"name": "Jeff Bezos", "net_worth_usd_billions": 194, "source": "Amazon", "country": "United States"},
    4: {"name": "Larry Ellison", "net_worth_usd_billions": 141, "source": "Oracle", "country": "United States"},
    5: {"name": "Mark Zuckerberg", "net_worth_usd_billions": 134, "source": "Meta Platforms", "country": "United States"},
    6: {"name": "Bill Gates", "net_worth_usd_billions": 128, "source": "Microsoft", "country": "United States"},
    7: {"name": "Larry Page", "net_worth_usd_billions": 127, "source": "Google", "country": "United States"},
    8: {"name": "Sergey Brin", "net_worth_usd_billions": 121, "source": "Google", "country": "United States"},
    9: {"name": "Michael Bloomberg", "net_worth_usd_billions": 106, "source": "Bloomberg LP", "country": "United States"},
    10: {"name": "Carlos Slim Helú & family", "net_worth_usd_billions": 102, "source": "Telecom", "country": "Mexico"},
}

df = pd.DataFrame(top_10_billionaires)
print(df.to_string())