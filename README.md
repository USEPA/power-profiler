Link to app in production: https://www.epa.gov/egrid/power-profiler

# Power Profiler

Power Profiler is an interactive tool to visualize a subset of eGRID data. Users can view resource mix and emission rates for all eGRID subregions. Historically, the app was hosted at the NCC and required an Oracle database. This project is intended to update the app with new visualizations (using D3.js) and rely on front-end JavaScript in order to be deployed onto the EPA's Drupal WebCMS.

## Installation

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

1. Clone the application to your local machine.
2. Navigate to the root of the project and run `npm install`.
3. After downloading the required packages, you can run `npm run dev`. In your browser, go to [http://localhost:8080](http://localhost:8080).

## Editing Text

Most of the text content in the app can be found within the `template` sections of each Vue component. You can make changes to this text directly to the `.vue` files there. Some content is added programmatically. For example, the values that appear in the result of the emissions estimate are added in the logic of the display methods within `EmissionsCalculator.vue.`

## Updating the data files

Go to the `prep` folder and follow the instructions outlined in the `README.md`.

## Requirements

- [Node.js and npm](https://nodejs.org/en/)

## Deployment

To deploy the the app onto either the [production EPA Drupal site](https://wcms.epa.gov) or the [staging app dev server](https://webcms.appdev.epa.gov), verify that the correct paths to the `subregion.json` and `zip.csv` files are both correct in the webpack config file (`prod.config.js` or `stag.config.js`), located in the `webpack` folder.

Then, use one the following commands to deploy:
- Staging: `npm run stage`
- Production: `npm run prod`

Note, these commands will clear any existing folder with built resources located in either `dist/stag` or `dist/prod`. Then, it will create a `bundle.js` file and `index.html`. Using only the `bundle.js` minified JS, you can copy and paste this code into the "Page Javascript" input field in Drupal.

If deploying to one of these environments, make sure to provide the app the URL of the D3 library hosted on EPA's website and assign the variable `&` to `jQuery` (shown below).

The "Page Javascript" section should look like this:
```
<script src="/sites/all/libraries/js/d3.v3.min.js"></script>
<script>var $ = jQuery</script>
<script>[INSERT CODE FROM BUNDLE HERE]</script>
```

## Cloud.gov  
You can deploy the app to Cloud.gov for testing purposes.  To do this you will need a Cloud.gov account and the [Cloud Foundry Command Line Tools](https://github.com/cloudfoundry/cli#installers-and-compressed-binaries) installed on your machine.  Use these commands to build and deploy the app to Cloud.gov.  
  
- From `app` directory run:  
`npm run cloudgov`  
  
- Change directories to `app\dist\cloudgov` and run:  
`cf push test-power-profile`  
  
*Note: you will first need to log into Cloud.gov (see `cf login`)*  

## Built With

* [D3 Data-Driven Documents](https://d3js.org) - JavaScript library for data viz
* [Vue.js](https://vuejs.org/) - The JavaScript framework used
* [Node.js and npm](https://nodejs.org/en/) - JavaScript runtime and package manager
* [Webpack](https://webpack.js.org/) - JavaScript bundler
* [Babel](https://babeljs.io/) - JavaScript compiler

## Versioning

- Version 1.0 was released on December 21, 2018.
- Version 1.1 was released on June 20, 2019

## Helpful Links
- [Staging site for app](https://webcms.appdev.epa.gov/energy/power-profiler)
- [Production site](https://www.epa.gov/energy/power-profiler)
- [eGRID Home page](https://www.epa.gov/energy/emissions-generation-resource-integrated-database-egrid)

## Disclaimer
The United States Environmental Protection Agency (EPA) GitHub project code is provided on an "as is" basis and the user assumes responsibility for its use. EPA has relinquished control of the information and no longer has responsibility to protect the integrity , confidentiality, or availability of the information. Any reference to specific commercial products, processes, or services by service mark, trademark, manufacturer, or otherwise, does not constitute or imply their endorsement, recommendation or favoring by EPA. The EPA seal and logo shall not be used in any manner to imply endorsement of any commercial product or activity by EPA or the United States Government.
