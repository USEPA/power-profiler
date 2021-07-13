<template>
  <div v-if="dataLoaded">
    <div class="grid-col grid-container" id="kpis">
      <div class="grid-row grid-gap">
        <h3 id="kpis-section-title">
          <span>{{ subregion.properties.name }}</span> Emission Rates
        </h3>
      </div>
      <div class="grid-row grid-gap">
        <div class="grid-col box special" value="co2EmissionRate">
          <h3 class="pane-title">CO<sub>2</sub></h3>
          <div class="pane-content">
            <h2 id="co2-pane-content">{{ subregion.properties.emissionFactor.co2EmissionRate.display }}</h2>
            <p>(lbs/MWh)</p>
          </div>
        </div>
        <div class="grid-col box special" value="so2EmissionRate">
          <h3 class="pane-title">SO<sub>2</sub></h3>
          <div class="pane-content">
            <h2 id="so2-pane-content">{{ subregion.properties.emissionFactor.so2EmissionRate.display }}</h2>
            <p>(lbs/MWh)</p>
          </div>
        </div>
        <div class="grid-col box special" value="noxEmissionRate">
          <h3 class="pane-title">NO<sub>X</sub></h3>
          <div class="pane-content">
            <h2 id="nox-pane-content">{{ subregion.properties.emissionFactor.noxEmissionRate.display }}</h2>
            <p>(lbs/MWh)</p>
          </div>
        </div>
      </div>
    </div>
    <div class="grid-col grid-container" id="selectedSubregion">
      <div class="grid-row grid-gap">
        <p id="subregionButtons">
          <router-link :to="'/'">« Back to All Subregions</router-link>
        </p>
      </div>
      <div class="grid-row">
        <div id="fuelMixContainer" class="grid-col">
            <h3>Fuel Mix</h3>
            <p>This chart compares fuel mix (%) of sources used to generate electricity in the selected <a href="https://www.epa.gov/sites/production/files/styles/large/public/2020-03/2018_egrid_subregions.png" target="_blank">eGRID subregion</a> to the national fuel mix (%).</p>
            <subregionFuelMixChart></subregionFuelMixChart>
        </div>
        <div id="printMap"></div>
        <div id="emissionRateContainer" class="grid-col">
            <h3>Emission Rates</h3>
            <p id="emRatesDescription">This chart compares the average emission rates (lbs/MWh) in the selected <a href="https://www.epa.gov/sites/production/files/styles/large/public/2020-03/2018_egrid_subregions.png" target="_blank">eGRID subregion</a> to the national average emission rates (lbs/MWh) for <a href="/ghgemissions/overview-greenhouse-gases#carbon-dioxide" target="_blank">carbon dioxide (CO<sub>2</sub>)</a>, <a href="/so2-pollution" target="_blank">sulfur dioxide (SO<sub>2</sub>)</a>, and <a href="/no2-pollution" target="_blank">nitrogen oxide (NO<sub>X</sub>)</a>.</p>
            <subregionEmissionRateChart></subregionEmissionRateChart>
        </div>
      </div>
    </div>
    <p><a href="javascript:window.print()">&#128438; Print Report</a></p>
    <emissionsCalculator></emissionsCalculator>
  </div>
</template>
<script>
import { allSubregions } from "../stores/allSubregions.js";
import { selectedSubregion } from "../stores/selectedSubregion.js";
import { nationalFeature } from "../stores/nationalFeature.js";
import subregionFuelMixChart from "./SubregionFuelMixChart.vue";
import subregionEmissionRateChart from "./SubregionEmissionRateChart.vue";
import emissionsCalculator from "./EmissionsCalculator.vue";

export default {
    components: {
        subregionFuelMixChart: subregionFuelMixChart,
        subregionEmissionRateChart: subregionEmissionRateChart,
        emissionsCalculator: emissionsCalculator,
    },
    data() {
        return {
            subregion: {},
            dataLoaded: false
        };
    },
    mounted: function() {
        this.subregion = selectedSubregion.data;
        this.dataLoaded = true;
        this.$root.$children[0].subregionSelected = true
        this.$root.$children[0].showMain = false
    },
    watch: {
        $route: function(to, from) {
          var self = this
          if (to !== from) {
              this.subregion = selectedSubregion.data
              this.$children[1].update()
              this.$children[2].update()
          }
        }
    },
    beforeCreate: function() {
        var self = this;
        var subName = this.$router.history.current.params.subregion;
        var subregion = allSubregions.data.filter(function(d) {
            return d.properties.name == subName;
        });
        if (subregion.length > 0) {
            $(".map").css({"fill":""});
            $("." + subregion[0].properties.name).css({"fill":"steelblue"});
            $("#regionSelectionDropdown").val(subregion[0].properties.name);
            selectedSubregion.update(subregion[0]);
        } else {
            this.dataLoaded = false;
            self.$router.push("/");
        }
    }
};
</script>
<style>
#selectedSubregion {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
}
#fuelMixContainer,
#emissionRateContainer {
  flex: 1 1 510px;
}
</style>