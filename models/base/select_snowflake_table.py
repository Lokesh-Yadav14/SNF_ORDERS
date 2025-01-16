import pandas as pd
from snowflake.snowpark.session import Session
from snowflake.snowpark.functions import col

def model(dbt, session: Session):
    # Logging
    dbt.config(
        materialized="table",  # Specify the materialization
        packages=["pandas"],  # Include required Python packages
    )

    # Select data from the Snowflake table
    snowflake_table = "DBT_ETL.STAGING.ORDERS"  # Replace with your table
    df = session.table(snowflake_table)

    # Perform operations (if needed)
    selected_data = df.select(
        col("ORDER_ID"),
        col("product_id"),
        col("quantity"),
        col("price"),
        col("total_amount")
    )

    # Convert to a Pandas DataFrame (optional)
    pandas_df = selected_data.to_pandas()

    # Return the final Snowflake DataFrame
    return selected_data
