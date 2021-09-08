<i18n>
{
    "en": {
        "title": "Estimate Your Emissions",
        "calculatorForm": {
          "avgUse": "Enter your ",
          "linkToAvgUse": "average monthly electricity use",
          "monUse": "Or enter your ",
          "monUseLink": "actual electricity use for each month",
          "months": {
            "jan": "January",
            "feb": "February",
            "mar": "March",
            "apr": "April",
            "may": "May",
            "jun": "June",
            "jul": "July",
            "aug": "August",
            "sep": "September",
            "oct": "October",
            "nov": "November",
            "dec": "December"
          },
          "natAvgUse": "Or use the",
          "natAvgUseLink": "national average electricity use",
          "goButton": "Go"
        },
        "results": {
          "natAnnGauge":"National Annual Electricity Use",
          "youAnnGauge":"Your Annual Electricity Use",
          "compareAnnGauge":"Your Electricity Use Compared to the National Average",
          "charts" : {
            "co2Title": "Carbon Dioxide",
            "so2Title": "Sulfur Dioxide",
            "noxTitle": "Nitrogen Oxides",
            "nat": "National Average",
            "reg": " Average",
            "you": "Your Emissions"
          },
          "avgSubheader": "Average Monthly Electricity Use",
          "actualSubheader": "Actual Monthly Electricity Use",
          "nationalSubheader": "National Average Electricity Use",
          "commercialSubheader": "National Average Electricity Use for Commercial Customers"
        }
    },
    "es": {
        "title": "Calcule sus emisiones",
        "calculatorForm": {
          "avgUse": "Ingrese su ",
          "linkToAvgUse": "consumo mensual promedio de electricidad",
          "monUse": "O ingrese su ",
          "monUseLink": "consumo real de electricidad para cada mes",
          "months": {
            "jan": "enero",
            "feb": "febrero",
            "mar": "marzo",
            "apr": "abril",
            "may": "mayo",
            "jun": "junio",
            "jul": "julio",
            "aug": "agosto",
            "sep": "septiembre",
            "oct": "octubre",
            "nov": "noviembre",
            "dec": "diciembre"
          },
          "natAvgUse": "O use el",
          "natAvgUseLink": "consumo nacional promedio de electricidad",
          "goButton": "Ir"
        },
        "results": {
          "natAnnGauge":"Consumo nacional eléctrico anual",
          "youAnnGauge":"Su consumo eléctrico anual",
          "compareAnnGauge":"Su consumo eléctrico comparado con el promedio nacional",
          "charts" : {
            "co2Title": "dióxido de carbono",
            "so2Title": "dióxido de azufre",
            "noxTitle": "óxido de nitrógeno",
            "nat": "Promedio nacional",
            "reg": " promedio",
            "you": "Sus emisiones"
          },
          "avgSubheader": "Consumo mensual promedio de electricidad",
          "actualSubheader": "Consumo mensual de electricidad",
          "nationalSubheader": "Consumo nacional promedio de electricidad",
          "commercialSubheader": "Uso promedio nacional de electricidad para clientes comerciales"
        }
    }
}
</i18n>
<template>
  <div id="emissionsCalculator">
    <h3>{{ $t("title") }}</h3>
    <div>
      <div>
        <label id="userMonthlyAverageLabel" class="usa-label" for="userMonthlyAverageInput">
          {{ $t("calculatorForm.avgUse") }}
          <a
            href="javascript:void(0)"
            id="monthlyAverageLink"
            @click="showAverageInput = true"
            v-if="showAverageInput === false"
            >{{ $t("calculatorForm.linkToAvgUse") }}</a
          >
          <span v-else>{{ $t("calculatorForm.linkToAvgUse") }}</span
          >.
        </label>
        <form
          v-on:submit.prevent="displayMonthlyAverage"
          v-show="showAverageInput"
          id="userMonthlyAverage"
          method="POST"
        >
          <input
            id="userMonthlyAverageInput"
            class="usa-input--sm"
            required=""
            type="number"
            style="height: 36px"
          />&nbsp;kWh&nbsp;<button
            id="calculateMonthlyAverageButton"
            class="usa-button"
            type="submit"
          >
            {{ $t("calculatorForm.goButton") }}
          </button>
        </form>
      </div>
      <div>
        <p>
          {{ $t("calculatorForm.monUse") }}
          <a
            href="javascript:void(0)"
            id="monthlyActualLink"
            class="emissionsLink"
            @click="showAverageInput = false"
            v-if="showAverageInput === true"
            >{{ $t("calculatorForm.monUseLink") }}</a
          >
          <span v-else>{{ $t("calculatorForm.monUseLink") }}</span
          >.
        </p>
        <form
          v-on:submit.prevent="displayMonthlyActual"
          v-show="!showAverageInput"
          id="calculateMonthlyActualForm"
          method="POST"
        >
          <div class="grid-row grid-gap">
            <div class="grid-col">
              <label for="userMonthlyActualInput1" class="usa-label"
                ><strong>{{ $t("calculatorForm.months.jan") }}</strong></label
              >
              <div>
                <input
                  id="userMonthlyActualInput1"
                  class="usa-input--sm"
                  required=""
                  type="number"
                />&nbsp;kWh
              </div>
            </div>
            <div class="grid-col">
              <label for="userMonthlyActualInput2" class="usa-label"
                ><strong>{{ $t("calculatorForm.months.feb") }}</strong></label
              >
              <div>
                <input
                  id="userMonthlyActualInput2"
                  class="usa-input--sm"
                  required=""
                  type="number"
                />&nbsp;kWh
              </div>
            </div>
            <div class="grid-col">
              <label for="userMonthlyActualInput3" class="usa-label"
                ><strong>{{ $t("calculatorForm.months.mar") }}</strong></label
              >
              <div>
                <input
                  id="userMonthlyActualInput3"
                  class="usa-input--sm"
                  required=""
                  type="number"
                />&nbsp;kWh
              </div>
            </div>
          </div>
          <div class="grid-row grid-gap">
            <div class="grid-col">
              <label for="userMonthlyActualInput4" class="usa-label"
                ><strong>{{ $t("calculatorForm.months.apr") }}</strong></label
              >
              <div>
                <input
                  id="userMonthlyActualInput4"
                  class="usa-input--sm"
                  required=""
                  type="number"
                />&nbsp;kWh`
              </div>
            </div>
            <div class="grid-col">
              <label for="userMonthlyActualInput5" class="usa-label"
                ><strong>{{ $t("calculatorForm.months.may") }}</strong></label
              >
              <div>
                <input
                  id="userMonthlyActualInput5"
                  class="usa-input--sm"
                  required=""
                  type="number"
                />&nbsp;kWh
              </div>
            </div>
            <div class="grid-col">
              <label for="userMonthlyActualInput6" class="usa-label"
                ><strong>{{ $t("calculatorForm.months.jun") }}</strong></label
              >
              <div>
                <input
                  id="userMonthlyActualInput6"
                  class="usa-input--sm"
                  required=""
                  type="number"
                />&nbsp;kWh
              </div>
            </div>
          </div>
          <div class="grid-row grid-gap">
            <div class="grid-col">
              <label for="userMonthlyActualInput7" class="usa-label"
                ><strong>{{ $t("calculatorForm.months.jul") }}</strong></label
              >
              <div>
                <input
                  id="userMonthlyActualInput7"
                  class="usa-input--sm"
                  required=""
                  type="number"
                />&nbsp;kWh
              </div>
            </div>
            <div class="grid-col">
              <label for="userMonthlyActualInput8" class="usa-label"
                ><strong>{{ $t("calculatorForm.months.aug") }}</strong></label
              >
              <div>
                <input
                  id="userMonthlyActualInput8"
                  class="usa-input--sm"
                  required=""
                  type="number"
                />&nbsp;kWh
              </div>
            </div>
            <div class="grid-col">
              <label for="userMonthlyActualInput9" class="usa-label"
                ><strong>{{ $t("calculatorForm.months.sep") }}</strong></label
              >
              <div>
                <input
                  id="userMonthlyActualInput9"
                  class="usa-input--sm"
                  required=""
                  type="number"
                />&nbsp;kWh
              </div>
            </div>
          </div>
          <div class="grid-row grid-gap">
            <div class="grid-col">
              <label for="userMonthlyActualInput10" class="usa-label"
                ><strong>{{ $t("calculatorForm.months.oct") }}</strong></label
              >
              <div>
                <input
                  id="userMonthlyActualInput10"
                  class="usa-input--sm"
                  required=""
                  type="number"
                />&nbsp;kWh
              </div>
            </div>
            <div class="grid-col">
              <label for="userMonthlyActualInput11" class="usa-label"
                ><strong>{{ $t("calculatorForm.months.nov") }}</strong></label
              >
              <div>
                <input
                  id="userMonthlyActualInput11"
                  class="usa-input--sm"
                  required=""
                  type="number"
                />&nbsp;kWh
              </div>
            </div>
            <div class="grid-col">
              <label for="userMonthlyActualInput12" class="usa-label"
                ><strong>{{ $t("calculatorForm.months.dec") }}</strong></label
              >
              <div>
                <input
                  id="userMonthlyActualInput12"
                  class="usa-input--sm"
                  required=""
                  type="number"
                />&nbsp;kWh
              </div>
              <br />

            </div>
          </div>
          <div>
            <button
                  id="calculateMonthlyActualButton"
                  class="usa-button"
                  type="submit"
                >
                  {{ $t("calculatorForm.goButton") }}
            </button>
          </div>
        </form>
      </div>
      <div>
        <p>
          {{ $t("calculatorForm.natAvgUse") }}
          <a
            v-on:click.prevent="displayNationalAverage"
            href="javascript:void(0)"
            id="nationalAverageLink"
            class="emissionsLink"
            >{{ $t("calculatorForm.natAvgUseLink") }}</a
          >.
        </p>
      </div>
    </div>
    <div id="calculatorError"></div>
  </div>
</template>
<script>
import { selectedSubregion } from "../stores/selectedSubregion.js";
import { nationalFeature } from "../stores/nationalFeature.js";
import { userSelection } from "../stores/userSelection.js";
import { addLogoBottom, textWrap } from "../helpers/ChartHelpers.js";
import { constVal } from "../helpers/const.js";

export default {
  data() {
    return {
      showAverageInput: true,
      resultsFunction: "",
      selectedSubregion: {},
      nationalFeature: {},
      natGridloss: {},
      emissionFactors: {},
      userEmissions: {},
      gridLoss: {},
      subregionEmissions: {},
      nationalEmissions: {},
      nationalAverage: constVal.nationalAverage,
      emRatesColors: {
        national: "#2b83ba",
        subregion: "#e66101",
        co2EmissionRate: "#d7191c",
        so2EmissionRate: "#008837",
        noxEmissionRate: "#7b3294"
      },
      resultsFunction: "",
      emissionsResultsWidth: 0,
      emissionsResultsHeight: 0,
      residentialMode: true,
      userSelectionStore: userSelection,
      commercialCustomerForm: false,
      sqrFootage: 0
    };
  },
  mounted: function() {
    this.selectedSubregion = selectedSubregion.data;
    this.nationalFeature = nationalFeature.data;
    this.natGridloss = this.nationalFeature[0].properties.gridLoss;
    this.emissionFactors = this.selectedSubregion.properties.emissionFactor;
    this.gridLoss = this.selectedSubregion.properties.gridLoss;
    $("#result").width() > 950
    // slightly less than 1/4 the width so they fit in one row and don't wrap 
      ? (this.emissionsResultsWidth = $("#result").width()*0.22)
      : (this.emissionsResultsWidth = 250);
    this.emissionsResultsHeight = 340;
  },
  methods: {
    displayMonthlyAverage: function() {
      var self = this;
      this.resultsFunction = "monthlyAverage";
      var userMonthlyAverage = $("#userMonthlyAverageInput").val();
      var total = userMonthlyAverage * 12;
      
      // Formula to find lbs of emissions given monthly kWh value
      function calculateEmissions(emissionFactorValue, monthlyAverage) {
        var emissionsAttr = monthlyAverage * 12 * emissionFactorValue * 0.001;
        var res = emissionsAttr + ((self.gridLoss.value * emissionsAttr) / (1 - self.gridLoss.value));
        return res;
      }

      this.userEmissions = {
        co2: calculateEmissions(
          this.emissionFactors.co2EmissionRate.value,
          userMonthlyAverage
        ),
        so2: calculateEmissions(
          this.emissionFactors.so2EmissionRate.value,
          userMonthlyAverage
        ),
        nox: calculateEmissions(
          this.emissionFactors.noxEmissionRate.value,
          userMonthlyAverage
        )
      };

      this.subregionEmissions = {
        co2: self.calculateSubregionEmissions(
          this.emissionFactors.co2EmissionRate.value,
          this.gridLoss.value
        ),
        so2: self.calculateSubregionEmissions(
          this.emissionFactors.so2EmissionRate.value,
          this.gridLoss.value
        ),
        nox: self.calculateSubregionEmissions(
          this.emissionFactors.noxEmissionRate.value,
          this.gridLoss.value
        )
      };

      this.nationalEmissions = {
        co2: self.calculateNationalEmissions(
          this.nationalFeature[0].properties.emissionFactor.co2EmissionRate
            .value
        ),
        so2: self.calculateNationalEmissions(
          this.nationalFeature[0].properties.emissionFactor.so2EmissionRate
            .value
        ),
        nox: self.calculateNationalEmissions(
          this.nationalFeature[0].properties.emissionFactor.noxEmissionRate
            .value
        )
      };

      var userCarbon = Math.round(this.userEmissions.co2).toLocaleString();
      var userNitrogen = Math.round(this.userEmissions.nox).toLocaleString();
      var userSulfur = Math.round(this.userEmissions.so2).toLocaleString();

      $("#egrid-subregion-acronym").html(
        this.selectedSubregion.properties.name
      );
      $("#egrid-subregion-name").html(
        this.selectedSubregion.properties.fullName
      );
      $("#percent-line-loss").html(this.gridLoss.display);
      $("#estimated-annual-electricity-use").html(total.toLocaleString());
      $("#pounds-of-co2").html(userCarbon);
      $("#pounds-of-so2").html(userSulfur);
      $("#pounds-of-nox").html(userNitrogen);
      $("#no-of-tree-seedlings").html(
        self.calculateCarbonOffset(parseFloat(this.userEmissions.co2)).trees
      );
      $("#acres-of-forests").html(
        self.calculateCarbonOffset(parseFloat(this.userEmissions.co2)).acres
      );

      var gaugeMax = 24000;
      if (userMonthlyAverage * 12 > gaugeMax) {
        gaugeMax = userMonthlyAverage * 12;
      }
      var percentMax = 100;
      var userPercent =
        ((userMonthlyAverage * 12) / (this.nationalAverage * 12)) * 100;
      if (userPercent > percentMax) {
        percentMax = userPercent;
      }

      d3.selectAll("#chart-gauge svg").remove();
      this.gaugeChart(
        this.emissionsResultsWidth,
        this.emissionsResultsHeight / 2,
        gaugeMax,
        this.nationalAverage * 12,
        this.$t("results.natAnnGauge"),
        false
      );
      this.gaugeChart(
        this.emissionsResultsWidth,
        this.emissionsResultsHeight / 2,
        gaugeMax,
        userMonthlyAverage * 12,
        this.$t("results.youAnnGauge"),
        false
      );
      this.gaugeChart(
        this.emissionsResultsWidth,
        this.emissionsResultsHeight / 2,
        percentMax,
        userPercent,
        this.$t("results.compareAnnGauge"),
        true
      );
      d3.selectAll("#resultGraphs svg").remove();
      d3.selectAll("#resultGraphs-rpt svg").remove();
      this.displayUserAndNationalEmissions(
        this.userEmissions,
        this.subregionEmissions,
        this.nationalEmissions,
        "#resultGraphs",
        this.emissionsResultsWidth,
        this.emissionsResultsHeight
      );
      this.displayUserAndNationalEmissions(
        this.userEmissions,
        this.subregionEmissions,
        this.nationalEmissions,
        "#resultGraphs-rpt",
        247,
        340
      );
      $("#resultGraphs").show();
      $("#annual-results-text").show();
      $("#national-avg-annual-results-text").hide();
      $("#result-subheader").html(self.$t("results.avgSubheader"));
      $("#result").show();
    },
    displayMonthlyActual: function() {
      var self = this;
      this.resultsFunction = "monthlyActual";
      var vals = $("#calculateMonthlyActualForm input")
        .map(function() {
          return $(this).val();
        })
        .get();

      var total = vals.reduce(function(a, b) {
        return parseFloat(a) + parseFloat(b);
      }, 0);

      function calculateEmissions(emissionFactorValue, total) {
        var emissionsAttr = total * emissionFactorValue * 0.001;
        var res = emissionsAttr + ((self.gridLoss.value * emissionsAttr)/(1 - self.gridLoss.value));
         return res;
      }

      this.nationalEmissions = {
        co2: this.calculateNationalEmissions(
          this.nationalFeature[0].properties.emissionFactor.co2EmissionRate
            .value
        ),
        so2: this.calculateNationalEmissions(
          this.nationalFeature[0].properties.emissionFactor.so2EmissionRate
            .value
        ),
        nox: this.calculateNationalEmissions(
          this.nationalFeature[0].properties.emissionFactor.noxEmissionRate
            .value
        )
      };

      this.subregionEmissions = {
        co2: this.calculateSubregionEmissions(
          this.emissionFactors.co2EmissionRate.value,
          this.gridLoss.value
        ),
        so2: this.calculateSubregionEmissions(
          this.emissionFactors.so2EmissionRate.value,
          this.gridLoss.value
        ),
        nox: this.calculateSubregionEmissions(
          this.emissionFactors.noxEmissionRate.value,
          this.gridLoss.value
        )
      };

      this.userEmissions = {
        co2: calculateEmissions(
          this.emissionFactors.co2EmissionRate.value,
          total
        ),
        so2: calculateEmissions(
          this.emissionFactors.so2EmissionRate.value,
          total
        ),
        nox: calculateEmissions(
          this.emissionFactors.noxEmissionRate.value,
          total
        )
      };

      var userCarbon = Math.round(this.userEmissions.co2).toLocaleString();
      var userNitrogen = Math.round(this.userEmissions.nox).toLocaleString();
      var userSulfur = Math.round(this.userEmissions.so2).toLocaleString();

      $("#egrid-subregion-acronym").html(
        this.selectedSubregion.properties.name
      );
      $("#egrid-subregion-name").html(
        this.selectedSubregion.properties.fullName
      );
      $("#percent-line-loss").html(this.gridLoss.display);
      $("#estimated-annual-electricity-use").html(total.toLocaleString());
      $("#pounds-of-co2").html(userCarbon);
      $("#pounds-of-so2").html(userSulfur);
      $("#pounds-of-nox").html(userNitrogen);
      $("#no-of-tree-seedlings").html(
        this.calculateCarbonOffset(parseFloat(this.userEmissions.co2)).trees
      );
      $("#acres-of-forests").html(
        this.calculateCarbonOffset(parseFloat(this.userEmissions.co2)).acres
      );

      var gaugeMax = 24000;
      if (total > gaugeMax) {
        gaugeMax = total;
      }
      var percentMax = 100;
      var userPercent = (total / (this.nationalAverage * 12)) * 100;
      if (userPercent > percentMax) {
        percentMax = userPercent;
      }

      d3.selectAll("#chart-gauge svg").remove();
      this.gaugeChart(
        this.emissionsResultsWidth,
        this.emissionsResultsHeight / 2,
        gaugeMax,
        this.nationalAverage * 12,
        this.$t("results.natAnnGauge"),
        false
      );
      this.gaugeChart(
        this.emissionsResultsWidth,
        this.emissionsResultsHeight / 2,
        gaugeMax,
        total,
        this.$t("results.youAnnGauge"),
        false
      );
      this.gaugeChart(
        this.emissionsResultsWidth,
        this.emissionsResultsHeight / 2,
        percentMax,
        userPercent,
        this.$t("results.compareAnnGauge"),
        true
      );
      d3.selectAll("#resultGraphs svg").remove();
      d3.selectAll("#resultGraphs-rpt svg").remove();
      this.displayUserAndNationalEmissions(
        this.userEmissions,
        this.subregionEmissions,
        this.nationalEmissions,
        "#resultGraphs",
        this.emissionsResultsWidth,
        this.emissionsResultsHeight
      );
      this.displayUserAndNationalEmissions(
        this.userEmissions,
        this.subregionEmissions,
        this.nationalEmissions,
        "#resultGraphs-rpt",
        247,
        340
      );
      $("#resultGraphs").show();
      $("#annual-results-text").show();
      $("#national-avg-annual-results-text").hide();
      $("#result-subheader").html(self.$t("results.actualSubheader"));
      $("#result").show();
    },
    displayNationalAverage: function(e) {
      var self = this;
      // Only display national graphs
      this.resultsFunction = "nationalAverage";

      function calculateEmissions(emissionFactorValue, monthlyAverage) {
        var emissionsAttr = monthlyAverage * 12 * emissionFactorValue * 0.001;
        var res = emissionsAttr + ((self.gridLoss.value * emissionsAttr)/(1 - self.gridLoss.value));
        return res;
      }

      this.nationalEmissions = {
        co2: calculateEmissions(
          this.nationalFeature[0].properties.emissionFactor.co2EmissionRate
            .value,
          this.nationalAverage
        ),
        so2: calculateEmissions(
          this.nationalFeature[0].properties.emissionFactor.so2EmissionRate
            .value,
          this.nationalAverage
        ),
        nox: calculateEmissions(
          this.nationalFeature[0].properties.emissionFactor.noxEmissionRate
            .value,
          this.nationalAverage
        )
      };

      this.subregionEmissions = {};

      this.userEmissions = {
        co2: calculateEmissions(
          this.emissionFactors.co2EmissionRate.value,
          this.nationalAverage
        ),
        so2: calculateEmissions(
          this.emissionFactors.so2EmissionRate.value,
          this.nationalAverage
        ),
        nox: calculateEmissions(
          this.emissionFactors.noxEmissionRate.value,
          this.nationalAverage
        )
      };
      if ($("#chart-gauge").children.length > 3) {
        d3.selectAll("#chart-gauge svg").remove();
      }
      if (this.residentialMode == false) {
        var gaugeMax = 24000;
        this.nationalAverage = this.sqrFootage * 1.22;
        $("#resultGraphs").hide();
        $("#result-subheader").html(self.$t("results.commercialSubheader"));
        d3.selectAll("#chart-gauge svg").remove();
        if (this.nationalAverage * 12 > 24000) {
          gaugeMax = this.nationalAverage * 12;
        }
        this.gaugeChart(
          this.emissionsResultsWidth,
          this.emissionsResultsHeight / 2,
          gaugeMax,
          this.nationalAverage * 12,
          this.$t("results.youAnnGauge"),
          false
        );
        this.displayUserAndNationalEmissions(
          this.userEmissions,
          this.subregionEmissions,
          this.nationalEmissions,
          "#chart-gauge",
          this.emissionsResultsWidth,
          this.emissionsResultsHeight
        );
        d3.selectAll("#resultGraphs-rpt svg").remove();
        this.displayUserAndNationalEmissions(
          this.userEmissions,
          this.subregionEmissions,
          this.nationalEmissions,
          "#resultGraphs-rpt",
          247,
          340
        );
      } else {
        this.nationalAverage = constVal.nationalAverage;
        $("#resultGraphs").hide();
        $("#result-subheader").html(self.$t("results.nationalSubheader"));
        $("#commercialCustomersForm").hide();
        d3.selectAll("#chart-gauge svg").remove();
        this.gaugeChart(
          this.emissionsResultsWidth,
          this.emissionsResultsHeight,
          24000,
          this.nationalAverage * 12,
          this.$t("results.youAnnGauge"),
          false
        );
        this.displayUserAndNationalEmissions(
          this.userEmissions,
          this.subregionEmissions,
          this.nationalEmissions,
          "#chart-gauge",
          this.emissionsResultsWidth,
          this.emissionsResultsHeight
        );
        d3.selectAll("#resultGraphs-rpt svg").remove();
        this.displayUserAndNationalEmissions(
          this.userEmissions,
          this.subregionEmissions,
          this.nationalEmissions,
          "#resultGraphs-rpt",
          247,
          340
        );
      }

      var userCarbon = Math.round(this.userEmissions.co2).toLocaleString();
      var userNitrogen = Math.round(this.userEmissions.nox).toLocaleString();
      var userSulfur = Math.round(this.userEmissions.so2).toLocaleString();

      $("#nat-egrid-subregion-acronym").html(
        this.selectedSubregion.properties.name
      );
      $("#nat-egrid-subregion-name").html(
        this.selectedSubregion.properties.fullName
      );
      $("#nat-percent-line-loss").html(this.gridLoss.display);
      $("#nat-estimated-annual-electricity-use").html(
        (this.nationalAverage * 12).toLocaleString()
      );
      $("#pounds-of-co2").html(userCarbon);
      $("#pounds-of-so2").html(userSulfur);
      $("#pounds-of-nox").html(userNitrogen);
      $("#no-of-tree-seedlings").html(
        this.calculateCarbonOffset(parseFloat(this.userEmissions.co2)).trees
      );
      $("#acres-of-forests").html(
        this.calculateCarbonOffset(parseFloat(this.userEmissions.co2)).acres
      );

      $("#commercialCustomersLink").click(function() {
        self.commercialCustomerForm = true;
        $("#residentialCustomersButton").show();
        $("#customerText").hide();
        $("#commercialCustomersForm").show();
      });

      $("#commercialCustomersForm").on("submit", function(e) {
        e.preventDefault();
        const input = $("#squareFootage").val();
        self.sqrFootage = input;
        self.residentialMode = false;
        self.displayNationalAverage();
        self.userSelectionStore.setResidentialMode(false);
      });

      $("#residentialCustomersButton").click(function() {
        self.commercialCustomerForm = false;
        self.residentialMode = true;
        self.userSelectionStore.setResidentialMode(true);
        self.displayNationalAverage();
        $("#customerText").show();
        $("#residentialCustomersButton").hide();
      });

      $("#annual-results-text").hide();
      $("#national-avg-annual-results-text").show();
      $("#result").show();
    },
    gaugeChart: function(width, height, maxVal, num, text, percent) {
      // Set Up
      var pi = Math.PI;
      var iR = 60;
      var oR = 80;

      var cur_color = "#008837";
      min = 0;
      current = 0;

      // Arc Defaults
      var arc = d3.svg
        .arc()
        .innerRadius(iR)
        .outerRadius(oR)
        .startAngle(-90 * (pi / 180));

      // Place svg element
      var svg = d3
        .select("#chart-gauge")
        .append("svg")
        .attr("width", width)
        .attr("height", height)
        .attr("class", "flex-col")
        .append("g")
        .attr(
          "transform",
          "translate(" + (width / 2 - 20) + "," + (height / 2 + 50) + ")"
        );

      svg
        .append("text")
        .attr("class", "gauge-title")
        .attr("transform", "translate(0," + -oR + ")")
        .attr("text-anchor", "middle")
        .text(text);

      var background = svg
        .append("path")
        .datum({ endAngle: 90 * (pi / 180) })
        .style("fill", "#ddd")
        .attr("d", arc);

      // Append foreground arc to svg
      var foreground = svg
        .append("path")
        .datum({ endAngle: -90 * (pi / 180) })
        .style("fill", cur_color)
        .attr("d", arc);

      // Display Max value
      var max = svg
        .append("text")
        .attr("transform", "translate(" + (iR + (oR - iR) / 2) + ",15)") // Set between inner and outer Radius
        .attr("text-anchor", "middle")
        .attr("class", "gauge-chart-label")
        .style("font-family", "Helvetica")
        .text(function() {
          if (percent == true) {
            return Math.round(maxVal).toLocaleString() + "%";
          } else {
            return Math.round(maxVal).toLocaleString() + " kWh";
          }
        });

      // Display Min value
      var min = svg
        .append("text")
        .attr("transform", "translate(" + -(iR + (oR - iR) / 2) + ",15)") // Set between inner and outer Radius
        .attr("text-anchor", "middle")
        .style("font-family", "Helvetica")
        .text(min);

      // Display Current value
      var current = svg
        .append("text")
        .attr("transform", "translate(0," + -(iR / 4) + ")") // Push up from center 1/4 of innerRadius
        .attr("text-anchor", "middle")
        .style("font-size", "15")
        .style("font-family", "Helvetica")
        .text(current);

      // Get value
      var numPi = Math.floor(num - maxVal / 2) * (pi / maxVal);

      // Text transition
      current.transition().text(function() {
        if (percent == true) {
          return Math.round(num).toLocaleString() + "%";
        } else {
          return Math.round(num).toLocaleString();
        }
      });

      // Arc Transition
      foreground
        .transition()
        .duration(function(d) {
          return 750;
        })
        .styleTween("fill", function() {
          return d3.interpolate(cur_color, cur_color);
        })
        .call(arcTween, numPi);

      d3.selectAll("#chart-gauge svg text").style(
        "font-family",
        "'Source Sans Pro', 'Helvetica Neue', 'Helvetica', 'Roboto', 'Arial', sans-serif"
      );

      d3.selectAll(".gauge-title").call(textWrap, 20, oR);

      d3.selectAll(
        "#chart-gauge svg .y.axis path, #resultGraphs svg .axis line"
      )
        .style("fill", "none")
        .style("stroke", "#000")
        .style("shape-rendering", "crispEdges");

      // Update animation
      function arcTween(transition, newAngle) {
        transition.attrTween("d", function(d) {
          var interpolate = d3.interpolate(d.endAngle, newAngle);
          return function(t) {
            d.endAngle = interpolate(t);
            return arc(d);
          };
        });
      }
    },
    calculateNationalEmissions: function(emissionFactorValue) {
      var nationalTotal = this.nationalAverage * 12;
      var nationalGridloss = this.natGridloss.value;
      var emissionsAttr = nationalTotal * emissionFactorValue * 0.001;
      var res = emissionsAttr + ((nationalGridloss * emissionsAttr) / (1 - nationalGridloss));
      return res;
    },
    calculateSubregionEmissions: function(emissionFactorValue, gridLoss) {
      var nationalTotal = this.nationalAverage * 12;
      var emissionsAttr = nationalTotal * emissionFactorValue * 0.001;
      var res = emissionsAttr + ((gridLoss * emissionsAttr) / (1 - gridLoss));
      return res;
    },
    calculateCarbonOffset: function(carbon) {
      // 23.2 pounds of carbon a medium growth tree, planted in an urban setting, and allowed to grow for 10 years sequesters
      // 44 units CO2
      // 12 Units C
      // 0.85 metric tons of CO2 sequestered annually by one acre of average US forest
      // 1 metric ton = 2204.6 lbs
      var trees = (carbon / (23.2 * (44 / 12))).toLocaleString(undefined, {
        maximumFractionDigits: 0
      });
      var carbonSByYear = constVal.carbonSequesteredByYear;
      var acres = (carbon / (carbonSByYear * 2204.6)).toLocaleString(undefined, {
        maximumFractionDigits: 0
      });
      return { "trees": trees, "acres": acres };
    },
    displayUserAndNationalEmissions: function(
      user,
      subregion,
      national,
      domElement,
      w,
      h
    ) {
      let self = this;
      var pollutants = ["co2", "so2", "nox"];

      for (var i = 0; i < pollutants.length; i += 1) {
        var margin = { top: 75, right: 35, bottom: 80, left: 55 },
          width = w - margin.left - margin.right,
          height = h - margin.top - margin.bottom;

        var x = d3.scale.ordinal().rangeRoundBands([0, width], 0.3);

        var arr = [
          {
            value: parseFloat(national[pollutants[i]]),
            display: Number(
              parseFloat(national[pollutants[i]]).toFixed(0)
            ).toLocaleString(),
            name: self.$t("results.charts.nat")
          },
          {
            value: parseFloat(subregion[pollutants[i]]),
            display: Number(
              parseFloat(subregion[pollutants[i]]).toFixed(0)
            ).toLocaleString(),
            name:
              this.selectedSubregion.properties.name +
              self.$t("results.charts.reg")
          },
          {
            value: parseFloat(user[pollutants[i]]),
            display: Number(
              parseFloat(user[pollutants[i]]).toFixed(0)
            ).toLocaleString(),
            name: self.$t("results.charts.you")
          }
        ];

        var y = d3.scale.linear().rangeRound([height, 1]);

        var cArr = [
          this.emRatesColors.national,
          this.emRatesColors.subregion,
          this.emRatesColors[pollutants[i] + "EmissionRate"]
        ];

        if (this.resultsFunction == "nationalAverage") {
          arr.splice(1, 1);
          cArr = [
            this.emRatesColors.national,
            this.emRatesColors[pollutants[i] + "EmissionRate"]
          ];
        }

        var color = d3.scale
          .ordinal()
          .range(cArr)
          .domain(
            arr.map(function(d) {
              return d.name;
            })
          );

        var xAxis = d3.svg
          .axis()
          .scale(x)
          .outerTickSize(0)
          .orient("bottom");

        var yAxis = d3.svg
          .axis()
          .scale(y)
          .outerTickSize(0)
          .tickFormat(function(d) {
            var prefix = d3.formatPrefix(d);
            return prefix.scale(d) + prefix.symbol;
          })
          .orient("left");

        var svg = d3
          .select(domElement)
          .append("svg")
          .attr("width", width + margin.left + margin.right)
          .attr("height", height + margin.top + margin.bottom)
          .attr("class", "flex-col")
          .append("g")
          .attr(
            "transform",
            "translate(" + margin.left + "," + margin.top + ")"
          );

        x.domain(
          arr.map(function(d) {
            return d.name;
          })
        );
        y.domain([
          0,
          d3.max(arr, function(d) {
            return d.value;
          })
        ]);

        svg
          .append("text")
          .attr("x", width / 2)
          .attr("y", 0 - margin.top / 2)
          .attr("text-anchor", "middle")
          .attr("font-weight", "bold")
          .text(function() {
            if (pollutants[i] == "co2") {
              return self.$t("results.charts.co2Title");
            } else if (pollutants[i] == "so2") {
              return self.$t("results.charts.so2Title");
            } else if (pollutants[i] == "nox") {
              return self.$t("results.charts.noxTitle");
            }
          });

        svg
          .append("g")
          .attr("class", "x axis")
          .attr("transform", "translate(0," + height + ")")
          .call(xAxis)
          .selectAll(".x .tick text")
          .call(function(t) {
            t.each(function(d) {
              var self = d3.select(this);
              self.style("font-size", "0.8em");
              var s = self.text().split(" ");
              self.text("");
              self
                .append("tspan")
                .attr("x", 0)
                .text(s[0]);
              self
                .append("tspan")
                .attr("x", 0)
                .attr("y", 35)
                .text(s[1]);
            });
          });

        svg
          .append("g")
          .attr("class", "y axis")
          .call(yAxis);

        svg
          .append("text")
          .attr("y", -30)
          .attr("dy", "0.71em")
          .attr("text-anchor", "end")
          .append("tspan")
          .text(function(d) {
            if (pollutants[i] == "co2") {
              return "CO";
            } else if (pollutants[i] == "so2") {
              return "SO";
            } else if (pollutants[i] == "nox") {
              return "NO";
            }
          })
          .append("tspan")
          .attr("baseline-shift", "-.25em")
          .attr("font-size", "76.4706%")
          .text(function(d) {
            if (pollutants[i] == "co2") {
              return "2";
            } else if (pollutants[i] == "so2") {
              return "2";
            } else if (pollutants[i] == "nox") {
              return "X";
            }
          });

        svg
          .append("text")
          .attr("y", -45)
          .attr("x", -(height / 2))
          .attr("transform", "rotate(-90)")
          .text("(lbs)");

        svg
          .selectAll(".bar")
          .data(arr)
          .enter()
          .append("rect")
          .attr("class", "bar comparisonGraph" + pollutants[i])
          .attr("fill", function(d) {
            return color(d.name);
          })
          .attr("x", function(d) {
            return x(d.name);
          })
          .attr("y", function(d) {
            return y(d.value);
          })
          .attr("width", x.rangeBand())
          .attr("height", function(d) {
            return height - y(d.value);
          });

        var labels = svg
          .selectAll("text.bar")
          .data(arr)
          .enter()
          .append("text");

        labels
          .attr("text-anchor", "middle")
          .append("tspan")
          .attr("x", function(d) {
            return x(d.name) + x.rangeBand() / 2;
          })
          .attr("y", function(d) {
            return y(d.value) + -20;
          })
          .text(function(d) {
            return d.display;
          });

        labels
          .append("tspan")
          .attr("x", function(d) {
            return x(d.name) + x.rangeBand() / 2;
          })
          .attr("y", function(d) {
            return y(d.value) + -5;
          })
          .text("lbs");

        if (i == 2) {
          addLogoBottom(svg, width - 90, height + 75);
        }
      }
      d3.selectAll(domElement + " svg text").style(
        "font-family",
        "'Source Sans Pro', 'Helvetica Neue', 'Helvetica', 'Roboto', 'Arial', sans-serif"
      );

      d3.selectAll(
        domElement + " svg .y.axis path, " + domElement + " svg .axis line"
      )
        .style("fill", "none")
        .style("stroke", "#000")
        .style("shape-rendering", "crispEdges");
    },
    update() {
      this.selectedSubregion = selectedSubregion.data;
      this.nationalFeature = nationalFeature.data;
      this.emissionFactors = this.selectedSubregion.properties.emissionFactor;
      this.gridLoss = this.selectedSubregion.properties.gridLoss;
      if (this.resultsFunction == "monthlyAverage") {
        this.displayMonthlyAverage();
      } else if (this.resultsFunction == "monthlyActual") {
        this.displayMonthlyActual();
      } else if (this.resultsFunction == "nationalAverage") {
        this.displayNationalAverage();
      }
    }
  },
  watch: {
    $route: function(to, from) {
      var self = this;
      if (to !== from) {
        self.selectedSubregion = selectedSubregion.data;
        self.update();
      }
    },
    "$root.$i18n.locale": {
      deep: true,
      handler() {
        this.update();
      }
    }
  }
};
</script>
