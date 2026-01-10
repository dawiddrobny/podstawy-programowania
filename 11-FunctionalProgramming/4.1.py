employees = ["SMITH Lucy", "JONES Janet", "LEE Jerry",
             "JACKSON Peter", "JOHNSON Rick",
             "LEWIS Terry", "CLARKE Robin"]

emp_J = list(filter(lambda e: e.startswith("J"), employees))

for emp in emp_J:
    print(emp)
