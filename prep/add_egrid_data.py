import pandas as pd
import json
import argparse
import re
import sys
import subprocess
import shutil
from pathlib import Path

# Command-line arguments for file and data year
parser = argparse.ArgumentParser(description='Generate subregion.json file from eGRID Excel file')
parser.add_argument('egrid_excel', nargs=1, type=str, help='/path/to/egridYYYY_data.xlsx')
parser.add_argument('egrid_shapefile', nargs=1, type=str, help='/path/to/egridYYYY_subregions.shp')
parser.add_argument('--geojson', nargs='?', type=str, default=None, help='/path/to/eGRIDYYYY_subregions.json')
parser.add_argument('--states_json', '-s', nargs='?', type=str, default="./data/shape/states.json", help='/path/to/states.json')
parser.add_argument('--data_year','-y', nargs='?', type=str, help='Year of eGRID data if filename does not contain year')
parser.add_argument('--out_dir','-o', nargs='?', type=str, default="./result", help='Directory to write output files')
parser.add_argument('--skippable_rows','-k', nargs='?', type=int, default=1, help='GGL sheet has this many extraneous "header" rows')

args = parser.parse_args()
egrid_excel = Path(args.egrid_excel[0])
egrid_shapefile = Path(args.egrid_shapefile[0])
egrid_states_json = Path(args.states_json)
egrid_geojson = args.geojson
skippable_rows = args.skippable_rows

def get_pct_cols(sheet_cols, col_pct_string):
  return list(filter(lambda x: col_pct_string in x, sheet_cols))

def convert_pct_cols(df, pct_cols, data_year):
  # Starting in 2018, percents are represented in raw fractional form
  # with a percent format but before then they were whole percentage numbers
  if data_year >= 2018:
    return(df[pct_cols].apply(lambda x: round(x*100,1)))

# for sheet names
m = re.search('\d{4}',egrid_excel.name)
if(m == None and args.data_year == None):
  sys.exit("ERROR: Could not find year in filename and no data_year argument provided")

if(m != None):
  data_year = m.group(0)

if(args.data_year != None and re.search('\d{4}', args.data_year) == None):
  sys.exit("ERROR: data_year argument must be a 4 digit year")

if(args.data_year != None):
  data_year = args.data_year

# Get the 2-digit year from the data_year for the sheet names
yr = data_year[-2:]

try:
  data_year_num = int(data_year)
except ValueError as verr:
  print(
    f'Please provide a valid numeric data_year[{data_year}]: data_year does not contain anything convertible to a number')
except Exception as ex:
  print(
    f'Please provide a valid numeric data_year[{data_year}]: Exception occurred while converting to a number')
# egrid_sbrgn_json = args.egrid_sbrgn_json[0]

out_dir = args.out_dir

if not egrid_geojson:
    # generate the json from shapefile
    mapshaper_check = subprocess.run([shutil.which("mapshaper"), "--version"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=False)

    mapshaper_version = mapshaper_check.stdout.decode('utf-8')
    if(mapshaper_version.find("not recognized") != -1):
        sys.exit("ERROR: mapshaper not found. Install using npm install -g mapshaper@0.4.125")
    if(mapshaper_version.strip() != "0.4.125"):
        sys.exit("ERROR: mapshaper version must be 0.4.125 -- you have {}".format(mapshaper_version.strip()))

    mapshaper_create_json_cmd = [shutil.which("mapshaper"), egrid_shapefile, "-simplify", "1%", "-o", "format=geojson", egrid_shapefile.parent]

    print(f'Creating json from {egrid_shapefile.name} using mapshaper')
    mapshaper_output = subprocess.run(mapshaper_create_json_cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=False)

    if(mapshaper_output.returncode != 0):
        sys.exit("ERROR: mapshaper failed to create json file")

    mapshaper_output_file = re.search("(?<=Wrote ).+", mapshaper_output.stdout.decode('utf-8')).group(0)
    egrid_sbrgn_json = Path(mapshaper_output_file)
    print(f'Wrote {egrid_sbrgn_json}')
else:
    print(f'Using {egrid_geojson}')
    egrid_sbrgn_json = Path(egrid_geojson)

# Load all data from excel sheets into dict of dataframes
print("Loading data from eGRID excel sheets")
all_sheets = pd.read_excel(egrid_excel, sheet_name=[f'SRL{yr}', f'US{yr}', f'GGL{yr}'], skiprows=skippable_rows)

# Load in Subregion data.
sn = all_sheets[f'SRL{yr}']
sn_pct_cols = get_pct_cols(sn.columns, 'PR')
sn[sn_pct_cols] = convert_pct_cols(sn, sn_pct_cols, data_year_num)

# Load in US-level data.
n = all_sheets[f'US{yr}']
n_pct_cols = get_pct_cols(n.columns, 'PR')
n[n_pct_cols] = convert_pct_cols(n, n_pct_cols, data_year_num)

# Load in Grid Loss data.
gl = all_sheets[f'GGL{yr}']

# Convert % floats into strings.
gl['GGRSLOSS_STR'] = convert_pct_cols(gl, ['GGRSLOSS'], data_year_num)
gl['GGRSLOSS_STR'] = gl['GGRSLOSS_STR'].map('{:,.1f}%'.format)

if data_year_num <= 2018:
  gl['GGRLOSS'] = gl['GGRLOSS']/100

# strip extra whitespace from region names
gl['REGION'] = gl['REGION'].str.strip()

# Renewable/Non-renewables dictionary.
renewables = {
    "pctRenewable":"Percent Renewable (Hydro, wind, biomass, solar, geothermal) net generation",
    "pctNonRenewable":"Percent Non-renewable (coal, oil, gas, other fossil, other unknown,  and Nuclear) net generation",
    "pctNonRenewableExcNuclear":"Percent Non-renewable Excluding Nuclear (coal, oil, gas, other fossil, other unknown) net generation",
    "pctRenewableExcHydro":"Percent Renewable Excluding Hydro (wind, biomass, solar, geothermal) net generation",
    "pctNuclear":"Percent Nuclear net generation",
    "pctHydro":"Percent Hydro net generation"
}
# Round values to the tenths for emission rates. Display a comma for thousands.
sn['SRNOXRTA'] = sn['SRNOXRTA'].round(3)
sn['SRSO2RTA'] = sn['SRSO2RTA'].round(3)
sn['SRCO2RTA'] = sn['SRCO2RTA'].round(3)
sn['SRC2ERTA'] = sn['SRC2ERTA'].round(3)
sn['SRNOXRTA_STR'] = sn['SRNOXRTA'].round(3).astype('str')
sn['SRSO2RTA_STR'] = sn['SRSO2RTA'].round(3).astype('str')
sn['SRCO2RTA_STR'] = sn['SRCO2RTA'].map('{:,.1f}'.format)
sn['SRC2ERTA_STR'] = sn['SRC2ERTA'].map('{:,.1f}'.format)
n['USNOXRTA'] = n['USNOXRTA'].round(3)
n['USSO2RTA'] = n['USSO2RTA'].round(3)
n['USCO2RTA'] = n['USCO2RTA'].round(3)
n['USC2ERTA'] = n['USC2ERTA'].round(3)
n['USNOXRTA_STR'] = n['USNOXRTA'].round(3).astype('str')
n['USSO2RTA_STR'] = n['USSO2RTA'].round(3).astype('str')
n['USCO2RTA_STR'] = n['USCO2RTA'].map('{:,.1f}'.format)
n['USC2ERTA_STR'] = n['USC2ERTA'].map('{:,.1f}'.format)
# Set up lists for checking whether subregion is in one of the interconnect power grids.
alaska = ['AKGD','AKMS']
hawaii = ['HIMS','HIOA']
ercot = ['ERCT']
eastern = ['MROE','SRMV','SRMW','RFCW','RFCM','SRTV','SRSO','FRCC','SRVC','RFCE','NYCW','NYLI','NYUP','NEWE','SPSO','SPNO','MROW']
western = ['CAMX','NWPP','AZNM','RMPA']
pr = ['PRMS']

# Add fuel breakdown
# Column names
snfm_cols = [
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
snfm = pd.DataFrame(
    columns=snfm_cols
)
# Add subregion data
snfm["eGRID subregion acronym"] = sn["SUBRGN"]
snfm["eGRID subregion name"] = sn["SRNAME"]
snfm["Percent Renewable (Hydro, wind, biomass, solar, geothermal) net generation"] = sn["SRTRPR"]
snfm["Percent Non-renewable (coal, oil, gas, other fossil, other unknown,  and Nuclear) net generation"] = sn["SRTNPR"]
snfm["Percent Non-renewable Excluding Nuclear (coal, oil, gas, other fossil, other unknown) net generation"] = sn["SRTNPR"] - sn["SRNCPR"]
snfm["Percent Non-renewable Excluding Nuclear (coal, oil, gas, other fossil, other unknown) net generation"] = snfm["Percent Non-renewable Excluding Nuclear (coal, oil, gas, other fossil, other unknown) net generation"].round(3)
snfm["Percent Renewable Excluding Hydro (wind, biomass, solar, geothermal) net generation"] = sn["SRTHPR"]
snfm["Percent Nuclear net generation"] = sn["SRNCPR"]
snfm["Percent Hydro net generation"] = sn["SRHYPR"]
# Add national data
row = ["U.S.", "National", n["USTRPR"].values[0], n["USTNPR"].values[0], (n["USTNPR"] - n["USNCPR"]).round(3).values[0], n["USTHPR"].values[0], n["USNCPR"].values[0], n["USHYPR"].values[0]]
snfm.loc[len(snfm.index)] = row

# Read in eGRID Subregions json
print("Loading eGRID subregions json file created from mapshaper")
with egrid_sbrgn_json.open(mode="r") as read_file, egrid_states_json.open(mode="r") as read_file2:
    data = json.load(read_file)
    states_data = json.load(read_file2)

# Append the states data to the subregions data to have a single json file.
data["features"] = data["features"] + states_data["features"]

# default national US values (eGRID data before 2012 does not have this)
fmCategories = {
    "renewable": 0,
    "non-renewable": 0,
    "non-renewable (excluding nuclear)": 0,
    "renewable (excluding hydro)": 0,
    "nuclear": 0,
    "hydro": 0,
}

for feature in data["features"]:
    # rename ZipSubregi to name
    if("ZipSubregi" in feature["properties"]):
        feature["properties"]["name"] = feature["properties"].pop("ZipSubregi")
    if "zips_for_G" in feature["properties"]:
        feature["properties"]["name"] = feature["properties"].pop("zips_for_G")
    if "Subregions" in feature["properties"]:
        feature["properties"]["name"] = feature["properties"].pop("Subregions")
    if("STATE" in feature["properties"]):
        feature["properties"]["type"] = "state"
    # Add eGRID data values.
    for index, row in sn.iterrows():
        if "name" in feature["properties"]:
            feature["properties"]["dataYear"] = data_year_num
            if feature["properties"]["name"] == row["SUBRGN"]:
                feature["properties"]["type"] = "subregion"
                feature["properties"]["fullName"] = row["SRNAME"]
                feature["properties"]["emissionFactor"] = {
                    "co2EmissionRate": {
                        "value": row["SRCO2RTA"],
                        "display": row["SRCO2RTA_STR"],
                        "units": "lb/MWh"
                    },
                    "co2eEmissionRate": {
                        "value": row["SRC2ERTA"],
                        "display": row["SRC2ERTA_STR"],
                        "units": "lb/MWh"
                    },
                    "noxEmissionRate": {
                        "value": row["SRNOXRTA"],
                        "display": row["SRNOXRTA_STR"],
                        "units": "lb/MWh"
                    },
                    "so2EmissionRate": {
                        "value": row["SRSO2RTA"],
                        "display": row["SRSO2RTA_STR"],
                        "units": "lb/MWh"
                    }
                }
                feature["properties"]["fuelMix"] = {
                    "coal": row["SRCLPR"],
                    "oil": row["SROLPR"],
                    "gas": row["SRGSPR"],
                    "nuclear": row["SRNCPR"],
                    "hydro": row["SRHYPR"],
                    "biomass": row["SRBMPR"],
                    "wind": row["SRWIPR"],
                    "solar": row["SRSOPR"],
                    "geothermal": row["SRGTPR"],
                    "otherFossilFuel": row["SROFPR"],
                    "otherUnknownFuel": row["SROPPR"]
                }
            # Add "gridLoss" to each feature from GGL sheet in eGRID data.
            if feature["properties"]["name"] in alaska:
                feature["properties"]["gridLoss"] = {
                    "display": gl[gl['REGION'] == 'Alaska']['GGRSLOSS_STR'].values[0],
                    "value": gl[gl['REGION'] == 'Alaska']['GGRSLOSS'].values[0]
                }
            elif feature["properties"]["name"] in hawaii:
                feature["properties"]["gridLoss"] = {
                    "display": gl[gl['REGION'] == 'Hawaii']['GGRSLOSS_STR'].values[0],
                    "value" : gl[gl['REGION'] == 'Hawaii']['GGRSLOSS'].values[0]
                }
            elif feature["properties"]["name"] in eastern:
                feature["properties"]["gridLoss"] = {
                    "display": gl[gl['REGION'] == 'Eastern']['GGRSLOSS_STR'].values[0],
                    "value": gl[gl['REGION'] == 'Eastern']['GGRSLOSS'].values[0]
                }
            elif feature["properties"]["name"] in western:
                feature["properties"]["gridLoss"] = {
                    "display": gl[gl['REGION'] == 'Western']['GGRSLOSS_STR'].values[0],
                    "value": gl[gl['REGION'] == 'Western']['GGRSLOSS'].values[0]
                }
            elif feature["properties"]["name"] in ercot:
                feature["properties"]["gridLoss"] = {
                    "display": gl[gl['REGION'] == 'ERCOT']['GGRSLOSS_STR'].values[0],
                    "value": gl[gl['REGION'] == 'ERCOT']['GGRSLOSS'].values[0]
                }
            elif feature["properties"]["name"] in pr:
                feature["properties"]["gridLoss"] = {
                    #Use the national values for the GGL in Puerto Rico
                    "display": gl[gl['REGION'] == 'U.S.']['GGRSLOSS_STR'].values[0],
                    "value": gl[gl['REGION'] == 'U.S.']['GGRSLOSS'].values[0]
                }

        # Add other fuel mix categories
        for index, row in snfm.iterrows():
            if "name" in feature["properties"]:

                if feature["properties"]["name"] == row["eGRID subregion acronym"]:
                    feature["properties"]["fuelMixCategories"] = {
                        "renewable": row[renewables["pctRenewable"]],
                        "non-renewable": row[renewables["pctNonRenewable"]],
                        "non-renewable (excluding nuclear)": row[renewables["pctNonRenewableExcNuclear"]],
                        "renewable (excluding hydro)": row[renewables["pctRenewableExcHydro"]],
                        "nuclear": row[renewables["pctNuclear"]],
                        "hydro": row[renewables["pctHydro"]]
                    }
                elif row["eGRID subregion acronym"] == "U.S.":
                    fmCategories = {
                        "renewable": row[renewables["pctRenewable"]],
                        "non-renewable": row[renewables["pctNonRenewable"]],
                        "non-renewable (excluding nuclear)": row[renewables["pctNonRenewableExcNuclear"]],
                        "renewable (excluding hydro)": row[renewables["pctRenewableExcHydro"]],
                        "nuclear": row[renewables["pctNuclear"]],
                        "hydro": row[renewables["pctHydro"]]
                    }

# Add national feature.
national = {
    "type":"Feature",
    "geometry":{},
    "properties":{
        "dataYear": data_year_num,
        "name":"National",
        "type":"national",
        "fullName":"National",
        "fuelMix":{
            "gas":n['USGSPR'].values[0],
            "coal":n['USCLPR'].values[0],
            "nuclear":n['USNCPR'].values[0],
            "hydro":n['USHYPR'].values[0],
            "wind":n['USWIPR'].values[0],
            "biomass":n['USBMPR'].values[0],
            "solar":n['USSOPR'].values[0],
            "oil":n['USOLPR'].values[0],
            "geothermal":n['USGTPR'].values[0],
            "otherFossilFuel":n['USOFPR'].values[0],
            "otherUnknownFuel":n['USOPPR'].values[0]
        },
        "fuelMixCategories": fmCategories,
        "emissionFactor":{
            "noxEmissionRate":{
                "units":"lb/MWh",
                "display":n['USNOXRTA_STR'].values[0],
                "value":n['USNOXRTA'].values[0]
                },
            "so2EmissionRate":{
                "units":"lb/MWh",
                "display":n['USSO2RTA_STR'].values[0],
                "value":n['USSO2RTA'].values[0]
                },
            "co2EmissionRate":{
                "units":"lb/MWh",
                "display":n['USCO2RTA_STR'].values[0],
                "value":n['USCO2RTA'].values[0]
                },
            "co2eEmissionRate":{
                "units":"lb/MWh",
                "display":n['USC2ERTA_STR'].values[0],
                "value":n['USC2ERTA'].values[0]
                },
        },
        "gridLoss": {
            "display": gl[gl['REGION'] == 'U.S.']['GGRSLOSS_STR'].values[0],
            "value": gl[gl['REGION'] == 'U.S.']['GGRSLOSS'].values[0]
        }
    }
}

data["features"].append(national)

print(f'Writing data to {out_dir}/subregion.json')
Path(out_dir).mkdir(exist_ok=True)
with open(f'{out_dir}/subregion.json', 'w') as outfile:
    json.dump(data, outfile)

print("Using mapshaper to simplify the final output further")
#mapshaper subregion.json -simplify dp 5% -o force format=geojson
mapshaper_final_command = [shutil.which("mapshaper"),f'{out_dir}/subregion.json', "-simplify", "dp", "5%", "-o", "force", "format=geojson", f'{out_dir}/subregion.json']

mapshaper_final_output = subprocess.run(mapshaper_final_command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=False)

if(mapshaper_final_output.returncode != 0):
    print(mapshaper_final_output.stdout.decode('utf-8'))
    sys.exit("Error running mapshaper for the final simplification")
print(f'Wrote simplified {out_dir}/subregion.json')
