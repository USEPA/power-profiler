<i18n>
{
    "en": {
        "fuelMixHeader": "Fuel Mix",
        "fuelMixBody": {
            "text": "This chart compares fuel mix (%) of sources used to generate electricity in the selected {eGRIDSubregion} to the national fuel mix (%).",
            "eGRIDSubregion": "eGRID subregion"
        },
        "emissionRateHeader": "Emission Rates",
        "emissionRateBody": {
            "text": "This chart compares the average emission rates in pounds per {MWhInfo} in the selected {eGRIDSubregion} to the national average emission rates for {co2}, {so2}, and {nox}.",
            "MWhInfo": "MWh",
            "eGRIDSubregion": "eGRID subregion",
            "co2": "carbon dioxide",
            "so2": "sulfur dioxide",
            "nox": "nitrogen oxide",
            "select": "Select:"
        },
        "backToAllSubregions": "Back to all subregions",
        "printReport": "Print Report"
    },
    "es": {
        "fuelMixHeader": "Combinación de combustibles",
        "fuelMixBody": {
            "text": "Este gráfico compara la combinación de combustibles (porcentajes) de las fuentes utilizadas para generar electricidad en la {eGRIDSubregion} seleccionada con la combinación de combustibles (porcentajes) nacional.",
            "eGRIDSubregion": "subregiones de eGRID"
        },
        "emissionRateHeader": "Tasas de emisión",
        "emissionRateBody": {
            "text": "Este cuadro compara las tasas de emisión promedio en libras por {MWhInfo} en las {eGRIDSubregion} con las tasas de emisión nacionales promedio para {co2}, {so2}, y {nox}.",
            "MWhInfo": "MWh",
            "eGRIDSubregion": "subregion de eGRID",
            "co2": "dióxido de carbono",
            "so2": "dióxido de azufre",
            "nox": "óxido de nitrógeno",
            "select": "Seleccione:"
        },
        "backToAllSubregions": "Volver a todas las subregiones",
        "printReport": "Imprima un reporte"
    }
}
</i18n>
<template>
  <div v-if="dataLoaded">
    <h3 id="kpis-section-title">
      <span>{{ subregion.properties.name }}</span>
      {{ $t("emissionRateHeader") }}
    </h3>
    <div class="col row cols-3" id="kpis">
      <div class="col box special" value="co2EmissionRate">
        <h3 class="pane-title">CO<sub>2</sub></h3>
        <div class="pane-content">
          <h2 id="co2-pane-content">
            {{ subregion.properties.emissionFactor.co2EmissionRate.display }}
          </h2>
          <p>(lbs/MWh)</p>
        </div>
      </div>
      <div class="col box special" value="so2EmissionRate">
        <h3 class="pane-title">SO<sub>2</sub></h3>
        <div class="pane-content">
          <h2 id="so2-pane-content">
            {{ subregion.properties.emissionFactor.so2EmissionRate.display }}
          </h2>
          <p>(lbs/MWh)</p>
        </div>
      </div>
      <div class="col box special" value="noxEmissionRate">
        <h3 class="pane-title">NO<sub>X</sub></h3>
        <div class="pane-content">
          <h2 id="nox-pane-content">
            {{ subregion.properties.emissionFactor.noxEmissionRate.display }}
          </h2>
          <p>(lbs/MWh)</p>
        </div>
      </div>
    </div>
    <p id="subregionButtons">
        <router-link :to="'/'">« {{ $t("backToAllSubregions") }}</router-link>
    </p>
    <div class="col row cols-2" id="selectedSubregion">
      <div id="fuelMixContainer" class="col">
        <h3>{{ $t("fuelMixHeader") }}</h3>
        <i18n path="fuelMixBody.text" tag="p">
          <template #eGRIDSubregion>
            <a
              href="https://www.epa.gov/sites/production/files/styles/large/public/2021-02/2019_egrid_subregions.png"
              target="_blank"
              >{{ $t("fuelMixBody.eGRIDSubregion") }}</a
            >
          </template>
        </i18n>
        <subregionFuelMixChart></subregionFuelMixChart>
      </div>
      <div id="printMap"></div>
      <div id="emissionRateContainer" class="col">
        <h3>{{ $t("emissionRateHeader") }}</h3>
        <i18n path="emissionRateBody.text" tag="p">
          <template #MWhInfo>
            <a
              @click="$parent.showMegaWattInfo = true"
              href="javascript:void(0)"
              >{{ $t("emissionRateBody.MWhInfo") }}</a
            >
          </template>
          <template #eGRIDSubregion>
            <a
              href="https://www.epa.gov/sites/production/files/styles/large/public/2021-02/2019_egrid_subregions.png"
              target="_blank"
              >{{ $t("emissionRateBody.eGRIDSubregion") }}</a
            >
          </template>
          <template #co2>
            <a
              href="/ghgemissions/overview-greenhouse-gases#carbon-dioxide"
              target="_blank"
              >{{ $t("emissionRateBody.co2") }} (CO<sub>2</sub>)</a
            >
          </template>
          <template #so2>
            <a href="/so2-pollution" target="_blank"
              >{{ $t("emissionRateBody.so2") }} (SO<sub>2</sub>)</a
            >
          </template>
          <template #nox>
            <a href="/no2-pollution" target="_blank"
              >{{ $t("emissionRateBody.nox") }} (NO<sub>X</sub>)</a
            >
          </template>
        </i18n>

        <subregionEmissionRateChart></subregionEmissionRateChart>
      </div>
    </div>
    <p>
      <a href="javascript:window.print()">&#128438; {{ $t("printReport") }}</a>
    </p>
    <emissionsCalculator></emissionsCalculator>
  </div>
</template>
<script>
import { allSubregions } from "../stores/allSubregions.js";
import { selectedSubregion } from "../stores/selectedSubregion.js";
import subregionFuelMixChart from "./SubregionFuelMixChart.vue";
import subregionEmissionRateChart from "./SubregionEmissionRateChart.vue";
import emissionsCalculator from "./EmissionsCalculator.vue";

export default {
  components: {
    subregionFuelMixChart: subregionFuelMixChart,
    subregionEmissionRateChart: subregionEmissionRateChart,
    emissionsCalculator: emissionsCalculator
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
    this.$root.$children[0].subregionSelected = true;
    this.$root.$children[0].showMain = false;
  },
  watch: {
    $route: function(to, from) {
      var self = this;
      if (to !== from) {
        this.subregion = selectedSubregion.data;
        this.$children[1].update();
        this.$children[2].update();
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
      $(".map").css({ fill: "" });
      $("." + subregion[0].properties.name).css({ fill: "steelblue" });
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
