# Power Profiler General Testing Guide

A general testing guide for manual review of changes to the Power Profiler.

> This is in no way comprehensive, but will touch most of the features found in the app.

---

## The following are components of the application and actions to take to test each component

* English/Espanol button
    * Check that all text within each section is changed to the respective language when the language is selected
    * Check spacing and layout for any side effects of longer descriptions or sentences when changing languages (e.g. legend labels)
    * Check that the language is set to the default locale of the browser

* Sidebar:
    *  Zip code
        * Test known zip codes to be in the correct region
    *  Map
        * Test if all regions are present and clickable with tooltip
    * Dropdown menu
        * Test if all regions are accessible through dropdown menu
    * More information modal
        * Test if modal appears and you can dismiss it
    * Test all links in Additional Information

* Main charts (all subregions):

    * Fuel Mix chart
        * Test all links in description
        * Test that clicking the various selections work and change the chart accordingly
        * All Fuels
            * Test that all tooltips work in English and Spanish
            * Test that clicking on a stacked bar chart sorts the chart by that clicked category
            * Test that the "sort regions alphabetically" resorts the chart alphabetically
            * Check that clicking on a legend item sorts the chart accordingly
            * Check that the corresponding legend title is bolded when the category is clicked and sorted
            * Check that the "sorted by" text changes when the sort changes
        * Renewable/Non*renewable
            * Test that all tooltips work in English and Spanish
            * Test that clicking on a stacked bar chart sorts the chart by that clicked category
            * Test that the "sort regions alphabetically" resorts the chart alphabetically
            * Check that clicking on a legend item sorts the chart accordingly
            * Check that the corresponding legend title is bolded when the category is clicked and sorted
            * Check that the "sorted by" text changes when the sort changes
        * Renewable/Non*renewable/Nuclear/Hydro
            * Test that all tooltips work in English and Spanish
            * Test that clicking on a stacked bar chart sorts the chart by that clicked category
            * Test that the "sort regions alphabetically" resorts the chart alphabetically
            * Check that clicking on a legend item sorts the chart accordingly
            * Check that the corresponding legend title is bolded when the category is clicked and sorted
            * Check that the "sorted by" text changes when the sort changes

    * Emission Rates chart
        * Check all links in description paragraph
        * Check all Selections
            * CO2, SO2, and NOx
                * Check the tooltips
                * Check the sort descending, ascending, and alphabetical by region
                * Check that the "sorted by" text changes when the sort changes
                * Check to see if the value for a selected subregion shows up above the bar for that region and the region is bolded in the x*axis
    * Maps
        * Test all links in description
        * Emisssion Rate Map
            * Test tooltips in English and Spanish
        * Renewable/Non*renewable Map
            * Test tooltips in English and Spanish

* Subregion Charts (after choosing a subregion)
    * Check that the summary stats at the top are changed to reflect those of the subregion (CO2, SO2, and NOx ) rates
    * Check that the "back to all subregions" link works and changes the charts to the main charts
    * Fuel Mix
        * Test all links in description
        * Test tooltips in English and Spanish
        * Make sure the subregion is included in the chart to the right of the National bar
        * Make sure the percentages of each fuel is next to the fuel in the legend
    * Emission Rates
        * Test all links in description
        * Test all selections CO2, SO2, NOx to ensure they change the chart information including color and axis labels

* Emissions calculator
    * Test average monthly use input
        * Check to see that only valid inputs are accepted (positive numbers)
        * Go button
        * Pressing keyboard enter
        * Check that the link for "average monthly electricity use" is enabled/disabled after clicking another option and this option
        * Check that the sum is matched in the first sentence of the results ("your estimated annual use of _____")
    * Test actual electricity use for each month input
        * Test each month input box
        * Test for valid input numbers (positive numbers)
        * Go button
        * Pressing keyboard enter
        * Check that the link for "actual electricity use for each month" is enabled/disabled after clicking another option or the option
        * Check that the sum is matched in the first sentence of the results ("your estimated annual use of _____")
    * Test national average electricity use
        * Check that the language in the results match the national language "Your annual emissions are estimated from the average home consumption of ___ kWh/month and the eGRID subregion _____"

* Emissions calculator Results
    * Test all links within the text
    * Check to see that all dynamic content (all parts of the text that change depending on inputs) are present and change with any subregion or emissions input changes
    * Test that changes are reflected when you
        * Change the number provided in the calculator
        * Change the type of input (average, actual, national)
        * Click on the commercial customers button ("here")
        * Test that the commercial customers button
            □ Opens an input box for entering square footage
            □ The first paragraph and all charts change when entering square footage
        * Test that the switch to residential button hides the commercial customer input and changes all text and charts to the previous text for the residential inputs
    * Test that all the charts (Guage chart, CO2, SO2, and NOx) charts are present and change when input changes

* Print report
    * Check that the print report feature works and shows all the information that is present on the screen at the time of clicking the button

