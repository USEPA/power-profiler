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
2. Add `.dbf` and `.shp` file to `data/shape` folder.
3. [Download and unzip latest eGRID Excel files from here](https://www.epa.gov/egrid/download-data)
4. Create `.csv` files in the `data/csv` folder from the following tabs in the eGRID Excel file:
    - SR (Subregion): `subregion_data.csv`
    - US (United States): `national.csv`
    - GGL (Gross Grid Loss): `grid_loss.csv`
    *Note: you need to remove the top level column headers prior to saving the tabs as csv files.  Also if there are formatting changes to any of the eGrid data files you will need to do some preprocessing prior to running these commands.  The subregion_data.csv and national.csv need to have percent formatted as 89.0 (not 0.89 or 89.0%).  The grid_loss.csv needs to have percent formatted as 89.0%.  There should be a more consistent handling of this in the processing scripts.*
5. Run the following command to add renewable/non-renewable breakdowns and create file `subregion_fuel_mix.csv`:
```python
python add_fuel_breakdown.py
```

## Using mapshaper to create GeoJSON

6. Run this command to transform shape file into GeoJSON:
```bash
mapshaper egrid_2016_subregions.shp -simplify 1% -o format=geojson
```
7. Run the following command to add `states.json` to the file and replace "Subregions" key with "name":
```javascript
node add_states.js
```
8. Run the following command to add eGRID data values to file:
```python
python add_egrid_data.py
```
9. Run this command to simplify file further:
```bash
mapshaper subregion.json -simplify dp 5% -o force format=geojson
```
10. Add the result JSON inside `result` to the app's `data` folder.

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