# Steps for updating data files

## Requirements
- Python 3
- Node.js
- [Mapshaper command line tool](https://github.com/mbloch/mapshaper):
```bash
npm install -g mapshaper@0.4.125
```

Power Profiler runs on two data files, `zip.csv` and `subregion.json`. The zip-subregion utility lookup data comes from the "Zip-subregion" tab of the Power Profiler Emissions Tool Excel file. This can be found on [the eGRID website](https://www.epa.gov/egrid). Follow these steps to update the `subregion.json` file (for a new year of eGRID data, for example):

## Initial setup

1. [Download and unzip eGRID shape files from here](https://www.epa.gov/egrid/egrid-mapping-files)
2. Add `.dbf` and `.shp` file to `data/shape` folder
3. [Download and unzip latest eGRID Excel files from here](https://www.epa.gov/egrid/download-data)
3. Add the excel file to `data/excel` folder
4. Run the following command from the prep folder using python 3+:
{bash}
```
python add_egrid_data.py data/excel/egridYYYY_data.xlsx data/shape/eGRIDYYYY_subregions.shp -o ../app/data
```
> This will take all the data from the excel file and the shape file and create the necessary `subregion.json` file to be uploaded into Drupal, placing it in the `app/data` folder
> There are other options for the `add_egrid_data.py` script. Run the script with the --help option to see more

## Update constants in app/src/helpers/const.js

* carbonSequesteredByYear
* carbonSequesteredByAcre
* avgConsumptionSqft
* nationalTotal
* nationalAverage

## Upload files to Drupal

> See README in app directory for more infof

1. Replace the zip.csv in the document library
2. Replace the subregion.json file in the document library
3. Replace the javascript in the Drupal javascript metadata after builing the production build