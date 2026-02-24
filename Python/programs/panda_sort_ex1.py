"""
Sort the data by salary in ascending order.

Sort the data by years of experience in descending order.

Sort the data first by department in ascending order and then by salary in descending order.

"""
import pandas as pd

# Creating a DataFrame with employee data
employee_data = {
    "employee_id": [101, 102, 103, 104, 105],
    "name": ["Alice", "Bob", "Charlie", "David", "Eve"],
    "department": ["HR", "IT", "Finance", "Marketing", "IT"],
    "salary": [50000, 60000, 55000, 70000, 65000],
    "years_of_experience": [5, 7, 4, 10, 6]
}

employees_df = pd.DataFrame(employee_data)
print(employees_df)

sort_by_sal = employees_df.sort_values(by="salary")
print(sort_by_sal)

sort_by_exp = employees_df.sort_values(by="years_of_experience",ascending=False)
print(sort_by_exp)

sort_by_dept_sal = employees_df.sort_values(by=["department","salary"],ascending=[True,False])
print(sort_by_dept_sal)
