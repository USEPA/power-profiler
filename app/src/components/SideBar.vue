<template>
  <div class="pane-content">
    <div>
      <p id="intro">
        Electricity is produced by many different sources of energy, including, but not limited to, wind, solar, nuclear, and fossil fuels. The type and amount of emissions produced depend on how electricity is generated in your region. Type in your zip code (or select a region) to view your power profile.
        <a class="more-link" href="javascript:void(0)" @click="$parent.showMoreInfo = true">More Info</a>
      </p>
    </div>
    <subregionSelection></subregionSelection>
    <div class="box multi related-info" id="info">
      <h3 class="pane-title">Additional Information</h3>
      <div class="pane-content">
        <p>
          <strong>
            <a
              href="https://epa.gov/energy/forms/egrid-and-power-profiler-feedback-and-questions"
              target="_blank"
              aria-label="Opens new window"
            >How do you like the new Power Profiler site?</a>
          </strong>
        </p>
        <p>
          Data source: 2018 data from the <a
            href="https://epa.gov/energy/emissions-generation-resource-integrated-database-egrid"
            target="_blank"
            aria-label="Opens new window"
          >Emissions & Generation Resource Integrated Database (eGRID)</a> released January 28, 2020
        </p>
        <p>
          Excel version:
          <a
            href="https://www.epa.gov/sites/production/files/2020-11/power_profiler_zipcode_tool.xlsx"
            aria-label="Downloads Excel spreadsheet tool"
          >Power Profiler Emissions Tool 2018 (XLSX)</a>
          <span class="fileinfo">(3.56M)</span>
        </p>
        <p>
          <a
            href="https://epa.gov/energy/forms/egrid-and-power-profiler-notification"
            target="_blank"
            aria-label="Opens new window"
          >Sign up for the mailing list</a>
        </p>
        <p>
          <a href="https://espanol.epa.gov/la-energia-y-el-medioambiente/perfilador-de-energia"
             target="_blank"
             aria-label="Opens new window"
          >Información relacionada en español</a>
        </p>
        <p>
          <a
            href="https://epa.gov/energy/power-profiler-methodology"
            target="_blank"
            aria-label="Opens new window"
          >Power Profiler Methodology</a>
        </p>
        <p>
          <a
            href="https://www.epa.gov/sites/production/files/2020-01/egrid2018_summary_tables.xlsx"
            aria-label="Downloads Excel spreadsheet summary tables"
          >eGRID Summary Tables (XLSX)</a>
          <span class="fileinfo">(1 pg, 293 K)</span>
        </p>
        <p>
          <a href="javascript:void(0)" @click="$parent.showResources = true">Additional Resources</a>
        </p>
      </div>
    </div>
  </div>
</template>
<script>
import subregionSelection from "./SubregionSelection.vue";


export default {
  components: {
    subregionSelection: subregionSelection,
  },
};
</script>
<style>
#intro {
  padding: 1.3529em 1em;
}

</style>