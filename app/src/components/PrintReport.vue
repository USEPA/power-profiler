<template>
  <div id="printReport">
      <div v-if="dataLoaded">
        <div id="kpis-and-map">
          <div id="kpis-main">
          <h3 id="kpis-section-title">
            <span>{{ subregion.properties.name }}</span> Emission Rates
          </h3>
          
          <div id="kpis-print">
            <p>CO<sub>2</sub>: {{ subregion.properties.emissionFactor.co2EmissionRate.display }} lbs/MWh</p>
            <p>SO<sub>2</sub>: {{ subregion.properties.emissionFactor.so2EmissionRate.display }} lbs/MWh</p>
            <p>NO<sub>X</sub>: {{ subregion.properties.emissionFactor.noxEmissionRate.display }} lbs/MWh</p>
          </div>
          </div>
          <div id="print-map">
          </div>
        </div>
      <div class="page-break" id="print-fuel-mix"></div>
      <div class="page-break" id="print-emission-rates"></div>
    </div>
  </div>  
</template>
<script>
import { selectedSubregion } from "../stores/selectedSubregion.js";

export default {
  data() {
      return {
          subregion: {},
          dataLoaded: false
      };
  },
  mounted: function() {
      this.subregion = selectedSubregion.data;
      this.dataLoaded = true;
  },
  watch: {
      $route: function(to, from) {
          if (to !== from) {
              this.subregion = selectedSubregion.data
          }
      }
  },
}
</script>
<style>
#printReport {
  width: 900px;
}
#kpis-and-map h3 {
  display: inline-block;
}
#kpis-print > p {
  display: inline-block;
  margin-left: 50px;
}
</style>


