import pandas as pd
# Load eGRID subregion data
# Load in Subregion data.
subregion_columns = pd.read_csv(
    './data/csv/subregion_data.csv',
    nrows=0 # Read 0 rows, assuming headers are at row 0
).columns

pct_columns = list(filter(lambda x: 'PR' in x, subregion_columns))

sn = pd.read_csv("./data/csv/subregion_data.csv", delimiter=',', thousands=',')

sn[pct_columns] = sn[pct_columns].apply(lambda x: x.str.rstrip('%').astype(float))

sn['SRNOXRTA'] = sn['SRNOXRTA'].round(3)
sn['SRSO2RTA'] = sn['SRSO2RTA'].round(3)
sn['SRCO2RTA'] = sn['SRCO2RTA'].round(3)
sn['SRNOXRTA_STR'] = sn['SRNOXRTA'].round(3).astype('str')
sn['SRSO2RTA_STR'] = sn['SRSO2RTA'].round(3).astype('str')
sn['SRCO2RTA_STR'] = sn['SRCO2RTA'].map('{:,.1f}'.format)
# Load eGRID national data
national_columns = pd.read_csv(
    './data/csv/national.csv',
    nrows=0 # Read 0 rows, assuming headers are at row 0
).columns

nat_pct_columns = list(filter(lambda x: 'PR' in x, national_columns))

n = pd.read_csv("./data/csv/national.csv", delimiter=',', thousands=',')

n[nat_pct_columns] = n[nat_pct_columns].apply(lambda x: x.str.rstrip('%').astype(float))

n['USNOXRTA'] = n['USNOXRTA'].round(3)
n['USSO2RTA'] = n['USSO2RTA'].round(3)
n['USCO2RTA'] = n['USCO2RTA'].round(3)
n['USNOXRTA_STR'] = n['USNOXRTA'].round(3).astype('str')
n['USSO2RTA_STR'] = n['USSO2RTA'].round(3).astype('str')
n['USCO2RTA_STR'] = n['USCO2RTA'].map('{:,.1f}'.format)
# Column names
cols = [
    "eGRID subregion acronym",
    "eGRID subregion name",
    "Percent Renewable (Hydro, wind, biomass, solar, geothermal) net generation",
    "Percent Non-renewable (coal, oil, gas, other fossil, other unknown,  and Nuclear) net generation",
    "Percent Non-renewable Excluding Nuclear (coal, oil, gas, other fossil, other unknown) net generation",
    "Percent Renewable Excluding Hydro (wind, biomass, solar, geothermal) net generation",
    "Percent Nuclear net generation",
    "Percent Hydro net generation"
]
# Initialize empty data frame
df = pd.DataFrame(
    columns=cols
)
# Add subregion data
df["eGRID subregion acronym"] = sn["SUBRGN"]
df["eGRID subregion name"] = sn["SRNAME"]
df["Percent Renewable (Hydro, wind, biomass, solar, geothermal) net generation"] = sn["SRTRPR"]
df["Percent Non-renewable (coal, oil, gas, other fossil, other unknown,  and Nuclear) net generation"] = sn["SRTNPR"]
df["Percent Non-renewable Excluding Nuclear (coal, oil, gas, other fossil, other unknown) net generation"] = sn["SRTNPR"] - sn["SRNCPR"]
df["Percent Non-renewable Excluding Nuclear (coal, oil, gas, other fossil, other unknown) net generation"] = df["Percent Non-renewable Excluding Nuclear (coal, oil, gas, other fossil, other unknown) net generation"].round(3)
df["Percent Renewable Excluding Hydro (wind, biomass, solar, geothermal) net generation"] = sn["SRTHPR"]
df["Percent Nuclear net generation"] = sn["SRNCPR"]
df["Percent Hydro net generation"] = sn["SRHYPR"]
# Add national data
row = ["U.S.", "National", n["USTRPR"].values[0], n["USTNPR"].values[0], (n["USTNPR"] - n["USNCPR"]).round(3).values[0], n["USTHPR"].values[0], n["USNCPR"].values[0], n["USHYPR"].values[0]]
df.loc[len(df.index)] = row
# Write to .csv file
df.to_csv("./data/csv/subregion_fuel_mix.csv", index=False)