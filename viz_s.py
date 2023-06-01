# import pandas as pd
# import os
# import matplotlib.pyplot as plt

# # List of CSV files
# state_list = ['Andaman & Nicobar.csv', 'Andhra Pradesh.csv', 'Arunachal Pradesh.csv', 'Assam.csv', 'Bihar.csv', 'Chandigarh.csv', 'Chhattisgarh.csv', 'Dadra & Nagar Haveli.csv', 'Daman & Diu.csv', 'Delhi.csv', 'Eastern Region.csv', 'Goa.csv', 'Gujarat.csv', 'Haryana.csv', 'Himachal Pradesh.csv', 'INDIA.csv', 'Jammu & Kashmir.csv', 'Jharkhand.csv', 'Karnataka.csv', 'Kerala.csv', 'Lakshadweep.csv', 'Madhya Pradesh.csv', 'Maharashtra.csv', 'Manipur.csv', 'Meghalaya.csv', 'Mizoram.csv', 'Nagaland.csv', 'North-Eastern Region.csv', 'Northern Region.csv', 'Odisha.csv', 'Puducherry.csv', 'Punjab.csv', 'Rajasthan.csv', 'Sikkim.csv', 'Southern Region.csv', 'Tamil Nadu.csv', 'Telangana.csv', 'Tripura.csv', 'Uttar Pradesh.csv', 'Uttrakhand.csv', 'West Bengal.csv', 'Western Region.csv']

# # Dictionary to store renewable energy values for each state
# renewable_energy = {}

# # Iterate over each CSV file
# for state_file in state_list:
#     # Read the data from the CSV file
#     df = pd.read_csv(state_file)

#     # Calculate total renewable energy generated
#     total_re_gen = df['Total RE Generated (Energy Saved)'].sum()

#     # Store the renewable energy value in the dictionary
#     renewable_energy[state_file] = total_re_gen

# # Sort the states based on renewable energy values in descending order
# sorted_states = sorted(renewable_energy.items(), key=lambda x: x[1], reverse=True)

# # Print the states in order of highest to lowest renewable energy
# for state, energy in sorted_states:
#     print(f"{state}: {energy}")



import pandas as pd
import os

# List of CSV files
state_list = ['Andaman & Nicobar.csv', 'Andhra Pradesh.csv', 'Arunachal Pradesh.csv', 'Assam.csv', 'Bihar.csv', 'Chandigarh.csv', 'Chhattisgarh.csv', 'Dadra & Nagar Haveli.csv', 'Daman & Diu.csv', 'Delhi.csv', 'Eastern Region.csv', 'Goa.csv', 'Gujarat.csv', 'Haryana.csv', 'Himachal Pradesh.csv', 'INDIA.csv', 'Jammu & Kashmir.csv', 'Jharkhand.csv', 'Karnataka.csv', 'Kerala.csv', 'Lakshadweep.csv', 'Madhya Pradesh.csv', 'Maharashtra.csv', 'Manipur.csv', 'Meghalaya.csv', 'Mizoram.csv', 'Nagaland.csv', 'North-Eastern Region.csv', 'Northern Region.csv', 'Odisha.csv', 'Puducherry.csv', 'Punjab.csv', 'Rajasthan.csv', 'Sikkim.csv', 'Southern Region.csv', 'Tamil Nadu.csv', 'Telangana.csv', 'Tripura.csv', 'Uttar Pradesh.csv', 'Uttrakhand.csv', 'West Bengal.csv', 'Western Region.csv']

# Dictionary to store renewable energy values for each state
renewable_energy = {}

# Dictionary to store sectors contributing the highest in each state
highest_sectors = {}

# Iterate over each CSV file
for state_file in state_list:
    # Read the data from the CSV file
    df = pd.read_csv(state_file)

    # Calculate total renewable energy generated
    total_re_gen = df['Total RE Generated (Energy Saved)'].sum()

    # Store the renewable energy value in the dictionary
    renewable_energy[state_file] = total_re_gen

    # Calculate the sector contributing the highest renewable energy in the state
    sectors = df.columns[5:8]  # Assuming columns Solar, Wind, Others are in positions 5, 6, 7
    sector_re_gen = {}
    for sector in sectors:
        sector_re_gen[sector] = sum(df[sector])

    sorted_sectors = sorted(sector_re_gen.items(), key=lambda x: x[1], reverse=True)
    highest_sector = sorted_sectors[0][0]
    highest_sectors[state_file] = highest_sector

# Sort the states based on renewable energy values in descending order
sorted_states = sorted(renewable_energy.items(), key=lambda x: x[1], reverse=True)

# Print the renewable energy values and highest contributing sectors for each state
for state, energy in sorted_states:
    highest_sector = highest_sectors[state]
    print(f"State: {state}")
    print(f"Renewable Energy: {energy}")
    print(f"Highest Contributing Sector: {highest_sector}")
    print()
