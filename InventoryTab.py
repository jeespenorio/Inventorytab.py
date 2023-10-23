import streamlit as st
import pandas as pd

# Read the CSV file into a DataFrame
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    Table1 = pd.read_csv(uploaded_file, low_memory=False)

    # Pivot the DataFrame using pivot_table
    pivot_table = Table1.pivot_table(index='3PL Customer', values=['On Hand', 'Allocated'], aggfunc='sum')

    # Rename the columns with swapped names
    pivot_table.columns = ['Sum of Allocated', 'Sum On Hand']

    # Calculate the grand total
    grand_total = pivot_table.sum(numeric_only=True).to_frame().T
    grand_total.index = ['Grand Total']

    # Concatenate the grand total row to the pivot table
    pivot_table = pd.concat([pivot_table, grand_total])

    # Display the pivot table
    st.subheader("Pivot Table:")
    st.dataframe(pivot_table)
