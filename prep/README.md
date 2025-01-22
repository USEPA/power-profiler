# Steps for updating data files

## Requirements
- Python 3
- Node.js
- [Mapshaper command line tool](https://github.com/mbloch/mapshaper):
```bash
npm install -g mapshaper@0.4.125
pip install -r requirements.txt
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

## Updates for new eGRID data years:

To update Power Profiler for new data years (or for use with older data years) you will need to update the following:

*	New finalized eGRID excel file
* New finalized eGRID .shp file
*	New zipcode csv file
*	Any changes in calculations or methodology
    * If there are changes, you'll likely need to update the code in the EmissionsCalculator.vue file
*	New link to zipcode excel tool
    * `powerProfilerExcelUrl: string`
*	New link to egrid subregion map
    * `egridSubregionMapUrl: string`
*	New link to eGRID summary table
    * `egridSummaryTablesUrl: string`
* New link to the Power Profiler Historical Data
    * Update in drupal
    * Check SideBar.vue for the link
* New link to the Power Profiler Methodology
    * Update in drupal
    * Check SideBar.vue for the link
*	Updates to the following numerical constants:
    *	CO2 metric tons sequestered annually per urban tree planted and allowed to grow for 10 years
        *	`carbonSequesteredByTree: float`
    *	CO2 metric tons sequestered annually by one acre of average U.S. forest
        *	`carbonSequesteredByYear: float`
    *	Conversion Factor for metric tons CO2/acre/year sequestered by one acre of forest preserved from conversion to cropland (in the year of conversion)
        *	`carbonSequesteredByAcre: float`
    *	Average energy consumption kwh per square foot  per **month** for commercial calculations
        *	`avgConsumptionSqft: float`
    * National total energy consumption for one year kwh (nationalAverage * 12)
        *   `nationalTotal: nationalAverage * 12`
    *	Average national energy consumption kwh for one month
        *	`nationalAverage: float`
* Edit the app/src/helpers/const.js file with the info from the constants above and the new links
* Edit the English **and** Spanish text in the top \<i18n\> json for the following files:
    * SideBar.vue
        * `egridDataSource:` update the data year and release date
        * `powerProfilerExcelLink:` update the data year
        * Update the file size for the span with `class="fileinfo"`
    * ResourcesModal.vue
        * `zipCodeLookup:` update the data year for both English and Spanish and the link in the html below
* Run the add_egrid_data.py script as shown in the [above section](#initial-setup) with the new eGRID excel and .shp files
* Run the `npm run prod` command to generate the `bundle.js` file in the `dist/prod` directory
    * See the [Deployment](../README.md#deployment) section in the main README fore more info
* Upload files to Drupal (See [README](../app/README.md) in the app directory for more info)
    * Replace the zip.csv in the Drupal document library
    * Replace the subregion.json file in the Drupal document library
    * Replace the javascript in the Drupal javascript metadata after builing the production build
