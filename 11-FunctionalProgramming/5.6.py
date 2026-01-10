employees = [("Smith", "Lucy"), ("Jones", "Janet"), ("Lee", "Jerry"),
             ("Jackson", "Peter"), ("Johnson", "Rick"),
             ("Lewis", "Terry"), ("Clarke", "Robin")]

formatted = list(map(lambda e: f"{e[0].upper()}, {e[1]}", employees))

for f in formatted:
    print(f)
