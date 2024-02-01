# Translated Meifang's R code to Python (EMILY)
# Use this code to make it so that each subject has a row for every year of their data

import pandas as pd
import os
import csv

# Read CSV file
file_path = r"\\Mac\Home\Downloads\long_lexnex_OH_ALScase.csv"
kidca_hmaprdngs_big = pd.read_csv(file_path)

# Data wrangling
kidca_hmaprdngs_xlong_pat = kidca_hmaprdngs_big.apply(lambda row: pd.DataFrame({
    'ID': row['ID'],
    'study_ID': row['study_ID'],
    'ALS_status': row['ALS_status'],
    'SEX': row['SEX'],
    'AGE': row['AGE'],
    'source_type': row['source_type'],
    'source': row['source'],
    'seq': row['seq'],
    'latitude': row['latitude'],
    'longitude': row['longitude'],
    'yr_addr_end': row['yr_addr_end'],
    'yr_addr_start': row['yr_addr_start'],
    'index_year': row['index_year'],
    'num_yrs_ad': row['num_yrs_ad'],
    'index_yr_minus15': row['index_minus15'],
    'year': list(range(row['yr_addr_start'], row['yr_addr_end'] + 1))
}), axis=1)

# Concatenate the list of DataFrames into a single DataFrame
kidca_hmaprdngs_xlong_pat = pd.concat(kidca_hmaprdngs_xlong_pat.values, ignore_index=True)

# Write to CSV
output_file = r"\\Mac\Home\Downloads\long_lexnex_OH_ALScaseEMILY.csv"
kidca_hmaprdngs_xlong_pat.to_csv(output_file, index=False)
