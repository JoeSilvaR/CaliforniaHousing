#Chunking the data 

import pandas as pd
import math

def split_csv(input_file, output_prefix):
    # Read the input CSV file
    df = pd.read_csv(r'Cali Housing/data_raw/County_zhvi_uc_sfrcondo_tier_0.33_0.67_sm_sa_month.csv')
    
    # Get the total number of rows in the input file
    total_rows = len(df)
    
    # Calculate the number of chunks (files) needed
    rows_per_file = math.ceil(total_rows/5)
    
    # Split the DataFrame into chunks and save each chunk as a separate CSV file
    for i in range(5):
        start = i * rows_per_file
        end = min(start + rows_per_file, total_rows)
        chunk_df = df[start:end]
        output_file = f"{output_prefix}_{i+1}.csv"
        chunk_df.to_csv(output_file, index=False)
        print(f"Saved {output_file}")




