import pandas as pd
import json
# Load in Subregion data.
sn = pd.read_csv("./data/csv/subregion_data.csv", delimiter=',', thousands=',')
snfm = pd.read_csv("./data/csv/subregion_fuel_mix.csv",delimiter=',',thousands=',')
# Load in Grid Loss data.
gl = pd.read_csv("./data/csv/grid_loss.csv", delimiter=',', thousands=',')
# Load in US-level data.
n = pd.read_csv("./data/csv/national.csv", delimiter=',', thousands=',')
# Convert % strings into floats.
gl['GGRSLOSS_STR'] = gl['GGRSLOSS']
gl['GGRSLOSS'] = (gl['GGRSLOSS'].str.rstrip('%').astype('float') / 100.0).round(4)
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
sn['SRNOXRTA'] = sn['SRNOXRTA'].round(1)
sn['SRSO2RTA'] = sn['SRSO2RTA'].round(2)
sn['SRCO2RTA'] = sn['SRCO2RTA'].round(1)
sn['SRNOXRTA_STR'] = sn['SRNOXRTA'].round(1).astype('str')
sn['SRSO2RTA_STR'] = sn['SRSO2RTA'].round(2).astype('str')
sn['SRCO2RTA_STR'] = sn['SRCO2RTA'].map('{:,.1f}'.format)
n['USNOXRTA'] = n['USNOXRTA'].round(1)
n['USSO2RTA'] = n['USSO2RTA'].round(2)
n['USCO2RTA'] = n['USCO2RTA'].round(1)
n['USNOXRTA_STR'] = n['USNOXRTA'].round(1).astype('str')
n['USSO2RTA_STR'] = n['USSO2RTA'].round(2).astype('str')
n['USCO2RTA_STR'] = n['USCO2RTA'].map('{:,.1f}'.format)
# Set up lists for checking whether subregion is in one of the interconnect power grids.
alaska = ['AKGD','AKMS']
hawaii = ['HIMS','HIOA']
ercot = ['ERCT']
eastern = ['MROE','SRMV','SRMW','RFCW','RFCM','SRTV','SRSO','FRCC','SRVC','RFCE','NYCW','NYLI','NYUP','NEWE','SPSO','SPNO','MROW']
western = ['CAMX','NWPP','AZNM','RMPA']
# Read in Subregions json.
with open("./data/shape/egrid_2018v2_subregions_states.json", "r") as read_file:
    data = json.load(read_file)
    for feature in data["features"]:
        # Add eGRID data values.
        for index, row in sn.iterrows():
            if "name" in feature["properties"]:
                if feature["properties"]["name"] == row["SUBRGN"]:
                    feature["properties"]["fullName"] = row["SRNAME"]
                    feature["properties"]["emissionFactor"] = {
                        "co2EmissionRate": {
                            "value": row["SRCO2RTA"],
                            "display": row["SRCO2RTA_STR"],
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
            "name":"National",
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
                    }
            },
            "gridLoss": {
                "display": gl[gl['REGION'] == 'U.S.']['GGRSLOSS_STR'].values[0],
                "value": gl[gl['REGION'] == 'U.S.']['GGRSLOSS'].values[0]
            }
        }
    }

    data["features"].insert(52,national)

with open('./data/subregion.json', 'w') as outfile:
    json.dump(data, outfile)