import pandas as pd
import re


def summarize_missing(df, sort=True, ascending=False, display=True):
    missing_count = df.isnull().sum()
    missing_percent = (missing_count / len(df) * 100).round(2)

    total_count = pd.Series([len(df)] * len(df.columns), index=df.columns)
    available_count = total_count - missing_count

    summary = pd.concat(
        [total_count, available_count, missing_count, missing_percent],
        axis=1
    )

    summary.columns = ['Total', 'Available', 'Missing', 'Missing %']

    if sort:
        summary = summary.sort_values(by='Missing %', ascending=ascending)

    if display:
        print("\nMissing Values Summary:\n")
        print(summary.to_string())

    print('--- (EOF) ---')
    return summary


def find_duplicates(df, column):
    """
    Return all rows where the specified column has duplicate values.
    Includes both original and duplicate rows.

    Parameters:
    -----------
    df : pandas.DataFrame
        Input DataFrame.
    column : str
        Column name to check for duplicates.

    Returns:
    --------
    pandas.DataFrame
        DataFrame containing original + duplicate rows.
    """

    # Step 1: find IDs that appear more than once
    dup_ids = df[column].value_counts()
    dup_ids = dup_ids[dup_ids > 1].index

    # Step 2: return all rows for those IDs
    result = df[df[column].isin(dup_ids)]
    return result.sort_values(by=column)

def extract_number(value):
    """
    Extract the first numeric value from a string and convert it to int or float.
    
    Parameters:
        value: The input value (string, number, etc.)
        dtype: int or float (default: int)
    
    Returns:
        Converted numeric value, or original value if no number found.
    """
    
    to_num = re.findall('[0-9]+',str(value))  # handles integers + decimals
    
    if len(to_num) > 0:
        return to_num[0]
    else:
        return value
    