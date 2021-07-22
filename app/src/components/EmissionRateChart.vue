<i18n>
{
    "en": {
        "emissionRateHeader": "Emission Rates",
        "emissionRateBody": {
            "text": "This chart compares the average emission rates in pounds per {MWhInfo} in all {eGRIDSubregions} to the national average emission rates for {co2}, {so2}, and {nox}.",
            "MWhInfo": "MWh",
            "eGRIDSubregions": "eGRID subregions",
            "co2": "carbon dioxide",
            "so2": "sulfur dioxide",
            "nox": "nitrogen oxide"
        },
        "emissionRateChart": {
            "selection": "Select:",
            "xAxis": "eGRID Subregions",
            "sortedByAlphaLabel": "This chart is sorted alphabetically A → Z by region.",
            "sortedByLabel": "This chart is sorted by {direction} {pollutant} emission rates.",
            "ascending": "ascending",
            "descending": "descending",
            "sortAlphaLink": "A → Z Sort regions alphabetically",
            "sortAscLink": "↑ Sort values ascending",
            "sortDescLink": "↓ Sort values descending",
            "regionTooltip": "Average {pollutant} rate: {rate} lbs/MWh",
            "nationalTooltip": "Average emission rate: {rate} lbs/MWh",
            "nationalBar": "National"
        },
        "maps": {
            "header": "Maps",
            "mapSelect": "Select:",
            "emissionRateMapChoice": "Emission Rate Map",
            "renewableMapChoice": "Renewable/Non-renewable Map"
        }
    },
    "es": {
        "emissionRateHeader": "Tasas de emisión",
        "emissionRateBody": {
            "text": "Este cuadro compara las tasas de emisión promedio en libras por {MWhInfo} en todas las {eGRIDSubregions} con las tasas de emisión nacionales promedio para {co2}, {so2}, y {nox}.",
            "MWhInfo": "MWh",
            "eGRIDSubregions": "subregiones de eGRID",
            "co2": "dióxido de carbono",
            "so2": "dióxido de azufre",
            "nox": "óxido de nitrógeno"
        },
        "emissionRateChart": {
            "selection": "Seleccione:",
            "xAxis": "eGRID Subregions",
            "sortedByAlphaLabel": "Ordenar las regiones en forma alfabética (A → Z)",
            "sortedByLabel": "Esta gráfica está ordenada en tasas de emisiones {direction} de {pollutant}",
            "asc": "ascendentes",
            "desc": "descendentes",
            "sortAlphaLink": "Ordenar las regiones en forma alfabética (A → Z)",
            "sortAscLink": "↑ Clasificar los valores en orden ascendente",
            "sortDescLink": "↓ Clasificar los valores en orden descendente",
            "regionTooltip": "Tasa de emisión promedio de {pollutant}: {rate} lbs/MWh",
            "nationalTooltip": "Tasa de emisión promedio: {rate} lbs/MWh",
            "nationalBar": "Nacional"

        },
        "maps": {
            "header": "Mapas",
            "mapSelect": "Seleccione",
            "emissionRateMapChoice": "Mapa de las Tasas de Emisión",
            "renewableMapChoice": "Mapa de Emisiones Renovables y No-Renovables"
        }
    }
}
</i18n>
<template>
  <div>
      <div id="nationalEmissionRate">
        <h3>{{ $t("emissionRateHeader") }}</h3>
        <i18n path="emissionRateBody.text" tag="p">
          <template #MWhInfo>
            <a
              @click="$parent.$parent.showMegaWattInfo = true"
              href="javascript:void(0)"
              >{{ $t("emissionRateBody.MWhInfo") }}</a
            >
          </template>
          <template #eGRIDSubregions>
            <a
              href="https://www.epa.gov/sites/production/files/styles/large/public/2021-02/2019_egrid_subregions.png"
              target="_blank"
              >{{ $t("emissionRateBody.eGRIDSubregions") }}</a
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

        <p class="select-pollutant-label">
          <strong> {{ $t("emissionRateChart.selection") }} </strong>
        </p>
        <div id="pollutantSelectAll">
          <button
            @click="handlePollutantButton"
            class="usa-button"
            id="defaultPollutantAll"
            value="co2EmissionRate"
          >
            CO<sub>2</sub>
          </button>
          <button @click="handlePollutantButton" class="usa-button" value="so2EmissionRate">
            SO<sub>2</sub>
          </button>
          <button @click="handlePollutantButton" class="usa-button" value="noxEmissionRate">
            NO<sub>X</sub>
          </button>
        </div>
        <div id="nationalEmissionRateGraph"></div>
        <div id="sortingDiv">
          <p id="nationalEmissionRateSortingStatus">
            <strong>{{ $t("emissionRateChart.sortedByAlphaLabel") }}</strong>
          </p>
          <a
            href="javascript:void(0)"
            @click="handleSortLink"
            id="sortAlphabeticallyEmissionRate"
            >{{ $t("emissionRateChart.sortAlphaLink") }}</a
          >
          <a
            href="javascript:void(0)"
            @click="handleSortLink"
            id="sortAscendingEmissionRate"
            >{{ $t("emissionRateChart.sortAscLink") }}</a
          >
          <a
            href="javascript:void(0)"
            @click="handleSortLink"
            id="sortDescendingEmissionRate"
            >{{ $t("emissionRateChart.sortDescLink") }}</a
          >
        </div>
      </div>
      <h3>{{ $t("maps.header") }}</h3>
      <label class="grid-col"><strong>{{ $t("maps.mapSelect") }}:</strong></label>
    <div>
      <div
        id="mapSelect"
        class="form-item form-type-radio form-item-radios grid-container"
      >
        <div class="grid-row grid-gap">
          <div class="grid-col-6">
            <input
              id="emissionRateMapChoice"
              name="mapChoice"
              class="usa-radio"
              type="radio"
              value="1"
              v-model="currentMap"
            />
            <label for="emissionRateMapChoice" class="option">{{
              $t("maps.emissionRateMapChoice")
            }}</label>
          </div>
          <div class="grid-col-6">
            <input
              id="renewablesMapChoice"
              name="mapChoice"
              class="usa-radio"
              type="radio"
              value="2"
              v-model="currentMap"
            />
            <label for="renewablesMapChoice" class="option">{{
              $t("maps.renewableMapChoice")
            }}</label>
          </div>
        </div>
      </div>
    </div>
      <emissionRateMap v-if="currentMap == 1"></emissionRateMap>
      <renewablesMap v-if="currentMap == 2"></renewablesMap>
  </div>
</template>

<script>
import { allSubregions } from "../stores/allSubregions.js";
import { nationalFeature } from "../stores/nationalFeature.js";
import { selectedSubregion } from "../stores/selectedSubregion.js";
import { addLogoBottom } from "../helpers/ChartHelpers.js";
import emissionRateMap from "./EmissionRateMap.vue";
import renewablesMap from "./RenewablesMap.vue";
import { userSelection } from "../stores/userSelection.js";
import { addTooltip } from "../helpers/Tooltip";

export default {
  components: {
    emissionRateMap: emissionRateMap,
    renewablesMap: renewablesMap
  },
  data() {
    return {
      nationalFeature: {},
      subregionData: [],
      subregions: {},
      w: 0,
      h: 0,
      domElement: "",
      orientation: "",
      parameters: ["so2EmissionRate", "co2EmissionRate", "noxEmissionRate"],
      emRatesColors: {
        national: "#2b83ba",
        subregion: "#e66101",
        co2EmissionRate: "#d7191c",
        so2EmissionRate: "#008837",
        noxEmissionRate: "#7b3294"
      },
      selectedRegion: {},
      selectedPollutantAll: "co2EmissionRate",
      pollutantText: "CO<sub>2</sub>",
      sortState: "alphabetically",
      selectedFuel: "",
      currentMap: 1
    };
  },
  mounted: function() {
    var self = this;
    this.orientation = userSelection.data.emissionRatesOrientation;
    this.initialize(
      $("#main-charts").width(),
      290,
      "#nationalEmissionRateGraph"
    );
    this.display(this.orientation);

    this.selectedRegion = selectedSubregion.data;

    $("#defaultPollutantAll").css({ "background-color": "#2B7D3B" });
    $("#sortAlphabeticallyEmissionRate").hide();

    $(window).on("resize", function() {
      if (self.$route.name == "home") self.update();
    });

    if (userSelection.sortState) {
      this.sortState = userSelection.sortState;
      if (this.sortState == "ascending") {
        $("#sortAscendingEmissionRate").trigger("click");
      } else if (this.sortState == "descending") {
        $("#sortDescendingEmissionRate").trigger("click");
      } else if (this.sortState == "alphabetically") {
        $("#sortAlphabeticallyEmissionRate").trigger("click");
      }
    }
  },
  methods: {
    initialize: function(width, height, domElement) {
      this.w = width;
      this.h = height;
      this.domElement = domElement;
      this.subregionData = allSubregions.data;
      this.nationalFeature = nationalFeature.data;
    },
    display: function(orientation) {
      var self = this;
      $(this.domElement).show();

      for (var i = 0; i < self.subregionData.length; i += 1) {
        self.subregions[self.subregionData[i].properties.name] =
          self.subregionData[i].properties.fullName;
      }

      if (orientation == "horizontal") {
        this.displayHorizontal();
      } else if (orientation == "vertical") {
        this.displayVertical();
      }
      this.showSelection();
      addTooltip(".emissionRateTooltip");
    },
    displayHorizontal: function() {
      var self = this;
      var margin = { top: 30, right: 60, bottom: 70, left: 70 },
        width = self.w - margin.left - margin.right,
        height = self.h - margin.top - margin.bottom;

      for (var i = 0; i < self.parameters.length; i += 1) {
        var x = d3.scale.ordinal().rangeRoundBands([0, width], 0.4);

        var y = d3.scale.linear().rangeRound([height, 1]);

        var color = d3.scale
          .ordinal()
          .range([self.emRatesColors[self.parameters[i]]])
          .domain(self.subregionData);

        var xAxis = d3.svg
          .axis()
          .scale(x)
          .outerTickSize(0)
          .orient("bottom");

        var yAxis = d3.svg
          .axis()
          .scale(y)
          .outerTickSize(0)
          .orient("left");

        var svg = d3
          .select(self.domElement)
          .append("svg")
          .attr("id", "all" + self.parameters[i])
          .attr("width", width + margin.left + margin.right)
          .attr("height", height + margin.top + margin.bottom)
          .append("g")
          .attr(
            "transform",
            "translate(" + margin.left + "," + margin.top + ")"
          );

        x.domain(
          self.subregionData.map(function(d) {
            return d.properties.name;
          })
        );
        y.domain([
          0,
          d3.max(self.subregionData, function(d) {
            return d.properties.emissionFactor[self.parameters[i]].value;
          })
        ]);

        svg
          .append("g")
          .attr("class", "x axis")
          .attr("transform", "translate(0," + height + ")")
          .call(xAxis)
          .selectAll("text")
          .attr("class", "subregionLabels")
          .attr("x", "-20")
          .attr("y", "10")
          .attr("transform", "rotate(-30)")
          .attr("text-anchor", "end")
          .append("title")
          .text(function(d) {
            return d + " (" + self.subregions[d] + ")";
          });

        svg
          .append("text")
          .attr(
            "transform",
            "translate(" + (width / 2 - 50) + "," + (height + 50) + ")"
          )
          .text(self.$t("emissionRateChart.xAxis"));

        svg
          .append("g")
          .attr("class", "y axis")
          .call(yAxis);
        var pollutantLabelTooltip = "";
        svg
          .append("text")
          .attr("y", -20)
          .attr("x", -10)
          .attr("dy", "0.71em")
          .attr("text-anchor", "end")
          .append("tspan")
          .text(function(d) {
            if (self.parameters[i] == "co2EmissionRate") {
              pollutantLabelTooltip = self.$t("emissionRateBody.co2");
              return "CO";
            } else if (self.parameters[i] == "so2EmissionRate") {
              pollutantLabelTooltip = self.$t("emissionRateBody.so2");
              return "SO";
            } else if (self.parameters[i] == "noxEmissionRate") {
              pollutantLabelTooltip = self.$t("emissionRateBody.nox");
              return "NO";
            }
          })
          .append("tspan")
          .attr("baseline-shift", "-.25em")
          .attr("font-size", "76.4706%")
          .text(function(d) {
            if (self.parameters[i] == "co2EmissionRate") {
              return "2";
            } else if (self.parameters[i] == "so2EmissionRate") {
              return "2";
            } else if (self.parameters[i] == "noxEmissionRate") {
              return "X";
            }
          });

        svg
          .append("text")
          .attr("y", -50)
          .attr("x", -(height / 2))
          .attr("transform", "rotate(-90)")
          .text("(lbs/MWh)");

        var container = svg
          .selectAll(".container")
          .data(self.subregionData)
          .enter()
          .append("g")
          .attr("class", "emissionRateTooltip")
          .attr("title", function(d) {
            return self.$t("emissionRateChart.regionTooltip", {
              pollutant: pollutantLabelTooltip,
              rate:
                d.properties.emissionFactor[self.selectedPollutantAll].display
            });
          });

        container
          .append("rect")
          .attr("class", "bar allEmissionRate " + self.parameters[i])
          .attr("fill", function(d) {
            return color(d.properties.name);
          })
          .attr("x", function(d) {
            return x(d.properties.name);
          })
          .attr("y", function(d) {
            return y(d.properties.emissionFactor[self.parameters[i]].value);
          })
          .attr("width", x.rangeBand())
          .attr("height", function(d) {
            return (
              height - y(d.properties.emissionFactor[self.parameters[i]].value)
            );
          })
          .on("click", function(d) {
            if (self.sortState == "ascending") {
              $("#sortDescendingEmissionRate")[0].click();
            } else if (self.sortState == "descending") {
              $("#sortAscendingEmissionRate")[0].click();
            } else if (self.sortState == "alphabetically") {
              $("#sortDescendingEmissionRate")[0].click();
            } else {
              $("#sortDescendingEmissionRate")[0].click();
            }
          });

        var nationalX = d3.scale
          .ordinal()
          .rangeRoundBands([width, width + 20], 0.2);

        var nationalBarXAxis = d3.svg
          .axis()
          .scale(nationalX)
          .outerTickSize(0)
          .orient("bottom");

        var nationalBar = svg
          .selectAll(".nationalBar")
          .append("g")
          .data(self.nationalFeature)
          .enter();

        var nationalContainer = svg
          .selectAll(".nationalContainer")
          .data(self.nationalFeature)
          .enter()
          .append("g")
          .attr("class", "emissionRateTooltip")
          .attr("title", function(d) {
            return self.$t("emissionRateChart.nationalTooltip", {
              rate:
                d.properties.emissionFactor[self.selectedPollutantAll].display
            });
          });

        nationalContainer
          .append("rect")
          .attr("class", "nationalBar allEmissionRate " + self.parameters[i])
          .attr("fill", function(d) {
            return color(d.properties.name);
          })
          .attr("x", function(d) {
            return width + x.rangeBand();
          })
          .attr("y", function(d) {
            return y(d.properties.emissionFactor[self.parameters[i]].value);
          })
          .attr("width", x.rangeBand())
          .attr("height", function(d) {
            return (
              height - y(d.properties.emissionFactor[self.parameters[i]].value)
            );
          })
          .on("click", function(d) {
            if (self.sortState == "ascending") {
              $("#sortDescendingEmissionRate")[0].click();
            } else if (self.sortState == "descending") {
              $("#sortAscendingEmissionRate")[0].click();
            } else if (self.sortState == "alphabetically") {
              $("#sortDescendingEmissionRate")[0].click();
            } else {
              $("#sortDescendingEmissionRate")[0].click();
            }
          });

        nationalBar
          .append("text")
          .attr("text-anchor", "middle")
          .attr("class", "selectedRegionValue")
          .attr("x", function(d) {
            return width + x.rangeBand() + x.rangeBand() / 2;
          })
          .attr("y", function(d) {
            return (
              y(d.properties.emissionFactor[self.parameters[i]].value) + -10
            );
          })
          .text(function(d) {
            return d.properties.emissionFactor[self.parameters[i]].display;
          });

        nationalBar
          .append("g")
          .attr("class", "nationalBar")
          .attr("transform", "translate(" + x.rangeBand() + "," + height + ")")
          .call(nationalBarXAxis)
          .append("text")
          .text(self.$t("emissionRateChart.nationalBar"))
          .attr("x", width - 15)
          .attr("y", 30);

        addLogoBottom(svg, width - 15, height + 65);

        if (Object.keys(self.selectedRegion).length) {
          d3.selectAll(self.domElement + " .tick text").attr(
            "font-weight",
            function(d) {
              if (d == self.selectedRegion.properties.name) {
                return "bold";
              }
            }
          );

          d3.selectAll("text.allEmissionRate").remove();

          svg
            .selectAll("text.allEmissionRate")
            .data(
              self.subregionData.filter(function(d) {
                if (d.properties.name == self.selectedRegion.properties.name) {
                  return d;
                }
              })
            )
            .enter()
            .append("text")
            .attr("class", "selectedRegionValue")
            .attr("text-anchor", "middle")
            .attr("x", function(d) {
              return x(d.properties.name) + x.rangeBand() / 2;
            })
            .attr("y", function(d) {
              return (
                y(d.properties.emissionFactor[self.parameters[i]].value) - 10
              );
            })
            .text(function(d) {
              return d.properties.emissionFactor[self.parameters[i]].display;
            });
        }
      }
    },
    displayVertical: function() {
      var self = this;
      for (var i = 0; i < self.parameters.length; i += 1) {
        var margin = { top: 60, right: 70, bottom: 70, left: 100 },
          width = 500 - margin.left - margin.right,
          height = 800 - margin.top - margin.bottom;

        var x = d3.scale.linear().rangeRound([0, width]);

        var y = d3.scale.ordinal().rangeRoundBands([0, height], 0.4);

        var color = d3.scale
          .ordinal()
          .range([self.emRatesColors[self.parameters[i]]])
          .domain(self.subregionData);

        var xAxis = d3.svg
          .axis()
          .scale(x)
          .orient("top");

        var yAxis = d3.svg
          .axis()
          .scale(y)
          .orient("left");

        var svg = d3
          .select(self.domElement)
          .append("svg")
          .attr("id", "all" + self.parameters[i])
          .attr("width", width + margin.left + margin.right)
          .attr("height", height + margin.top + margin.bottom)
          .append("g")
          .attr(
            "transform",
            "translate(" + margin.left + "," + margin.top + ")"
          );

        x.domain([
          0,
          d3.max(self.subregionData, function(d) {
            return d.properties.emissionFactor[self.parameters[i]].value;
          })
        ]);
        y.domain(
          self.subregionData.map(function(d) {
            return d.properties.name;
          })
        );

        svg
          .append("g")
          .attr("class", "x axis")
          .attr("transform", "translate(0,0)")
          .call(xAxis)
          .selectAll("text")
          .attr("x", "0")
          .attr("y", "-10")
          .attr("text-anchor", "end")
          .append("title")
          .text(function(d) {
            return d + " (" + self.subregions[d] + ")";
          });

        svg
          .append("g")
          .attr("class", "y axis")
          .call(yAxis);
        var pollutantLabelTooltip = "";
        svg
          .append("text")
          .attr("x", 45)
          .attr("y", -50)
          .attr("dy", "0.71em")
          .attr("text-anchor", "end")
          .append("tspan")
          .text(function(d) {
            if (self.parameters[i] == "co2EmissionRate") {
              pollutantLabelTooltip = "carbon dioxide";
              return "CO";
            } else if (self.parameters[i] == "so2EmissionRate") {
              pollutantLabelTooltip = "sulfur dioxide";
              return "SO";
            } else if (self.parameters[i] == "noxEmissionRate") {
              pollutantLabelTooltip = "nitrogen oxides";
              return "NO";
            }
          })
          .append("tspan")
          .attr("baseline-shift", "sub")
          .text(function(d) {
            if (self.parameters[i] == "co2EmissionRate") {
              return "2";
            } else if (self.parameters[i] == "so2EmissionRate") {
              return "2";
            } else if (self.parameters[i] == "noxEmissionRate") {
              return "x";
            }
          })
          .append("tspan")
          .text(" Rate (lbs/MWh)");

        var container = svg
          .selectAll(".container")
          .data(self.subregionData)
          .enter()
          .append("g")
          .attr("class", "emissionRateTooltip")
          .attr("title", function(d) {
            return (
              "Average " +
              pollutantLabelTooltip +
              " rate: " +
              d.properties.emissionFactor[self.selectedPollutantAll].display +
              " lbs/MWh"
            );
          });

        container
          .append("rect")
          .attr("class", "bar allEmissionRate " + self.parameters[i])
          .attr("fill", function(d) {
            return color(d.properties.name);
          })
          .attr("y", function(d) {
            return y(d.properties.name);
          })
          .attr("x", function(d) {
            return x(0);
          })
          .attr("height", y.rangeBand())
          .attr("width", function(d) {
            return x(d.properties.emissionFactor[self.parameters[i]].value);
          })
          .on("click", function(d) {
            if (self.sortState == "ascending") {
              $("#sortDescendingEmissionRate")[0].click();
            } else if (self.sortState == "descending") {
              $("#sortAscendingEmissionRate")[0].click();
            } else if (self.sortState == "alphabetically") {
              $("#sortDescendingEmissionRate")[0].click();
            } else {
              $("#sortDescendingEmissionRate")[0].click();
            }
          });

        var nationalY = d3.scale
          .ordinal()
          .rangeRoundBands([height, height + 20], 0.2);

        var nationalBarYAxis = d3.svg
          .axis()
          .scale(nationalY)
          .orient("left");

        var nationalBar = svg
          .selectAll(".nationalY")
          .append("g")
          .data(self.nationalFeature)
          .enter();

        nationalBar
          .append("rect")
          .attr("class", "bar allEmissionRate " + self.parameters[i])
          .attr("fill", function(d) {
            return color(d.properties.name);
          })
          .attr("y", function(d) {
            return height;
          })
          .attr("x", function(d) {
            return x(0);
          })
          .attr("height", y.rangeBand())
          .attr("width", function(d) {
            return x(d.properties.emissionFactor[self.parameters[i]].value);
          })
          .on("click", function(d) {
            if (self.sortState == "ascending") {
              $("#sortDescendingEmissionRate")[0].click();
            } else if (self.sortState == "descending") {
              $("#sortAscendingEmissionRate")[0].click();
            } else if (self.sortState == "alphabetically") {
              $("#sortDescendingEmissionRate")[0].click();
            } else {
              $("#sortDescendingEmissionRate")[0].click();
            }
          });

        nationalBar
          .append("text")
          .attr("text-anchor", "middle")
          .attr("class", "selectedRegionValue")
          .attr("y", function(d) {
            return height + y.rangeBand() - 3;
          })
          .attr("x", function(d) {
            return (
              x(d.properties.emissionFactor[self.parameters[i]].value) + 20
            );
          })
          .text(function(d) {
            return d.properties.emissionFactor[self.parameters[i]].display;
          });

        nationalBar
          .append("g")
          .attr("class", "nationalBarV")
          .attr("transform", "translate(0,0)")
          .call(nationalBarYAxis)
          .append("text")
          .text(self.$t("emissionRateChart.nationalBar"))
          .attr("x", -65)
          .attr("y", height + y.rangeBand());

        addLogoBottom(svg, width - 70, height + 70);

        if (Object.keys(self.selectedRegion).length) {
          d3.selectAll(self.domElement + " .tick text").attr(
            "font-weight",
            function(d) {
              if (d == self.selectedRegion.properties.name) {
                return "bold";
              }
            }
          );

          d3.selectAll("text.allEmissionRate").remove();

          svg
            .selectAll("text.allEmissionRate")
            .data(
              self.subregionData.filter(function(d) {
                if (d.properties.name == self.selectedRegion.properties.name) {
                  return d;
                }
              })
            )
            .enter()
            .append("text")
            .attr("class", "selectedRegionValue")
            .attr("text-anchor", "middle")
            .attr("y", function(d) {
              return y(d.properties.name) + y.rangeBand() / 2 + 5;
            })
            .attr("x", function(d) {
              return (
                x(d.properties.emissionFactor[self.parameters[i]].value) + 25
              );
            })
            .text(function(d) {
              return d.properties.emissionFactor[self.parameters[i]].display;
            });
        }
      }
    },
    show: function() {
      $(this.domElement)
        .parent("div")
        .show();
      $(this.domElement).show();
    },
    showSelection: function() {
      $("#all" + this.selectedPollutantAll).show();
      $("#all" + this.selectedPollutantAll)
        .siblings("svg")
        .hide();
    },
    hide: function() {
      $(this.domElement)
        .parent("div")
        .hide();
      $(this.domElement).hide();
    },
    clear: function() {
      d3.selectAll(this.domElement + " svg").remove();
    },
    sort: function(sortState, selectedPollutantAll) {
      var self = this;
      var data = self.subregionData;
      if (sortState == "alphabetically") {
        data.sort(function(x, y) {
          return d3.ascending(x.properties.name, y.properties.name);
        });
      } else if (sortState == "ascending") {
        data.sort(function(x, y) {
          return d3.ascending(
            x.properties.emissionFactor[selectedPollutantAll].value,
            y.properties.emissionFactor[selectedPollutantAll].value
          );
        });
      } else if (sortState == "descending") {
        data.sort(function(x, y) {
          return d3.descending(
            x.properties.emissionFactor[selectedPollutantAll].value,
            y.properties.emissionFactor[selectedPollutantAll].value
          );
        });
      } else if (sortState == "subregionFuels") {
        data.sort(function(x, y) {
          return d3.descending(
            x.properties.fuelMix[self.selectedFuel],
            y.properties.fuelMix[self.selectedFuel]
          );
        });
      }
    },
    update: function() {
      this.clear();
      this.initialize(
        $("#main-charts").width(),
        290,
        "#nationalEmissionRateGraph"
      );
      this.sortState = userSelection.sortState;
      this.sort(this.sortState, this.selectedPollutantAll);
      this.display(this.orientation);
      this.show(this.subregionData);
      this.showSelection(this.selectedPollutantAll);
    },
    setPollutantText: function() {
      var self = this;
      $("#pollutantSelectAll button").each(function() {
        if ($(this).attr("value") == self.selectedPollutantAll) {
          self.pollutantText = $(this).html();
        }
      });
    },
    updateStatus: function(pollutant, state) {
      if (state == "ascending" || state == "descending") {
        return `<strong> ${this.$t("emissionRateChart.sortedByLabel", {
          direction: this.$t(state),
          pollutant: pollutant
        })}<strong>`;
      } else if (state == "alphabetically") {
        return `<strong>${this.$t(
          "emissionRateChart.sortedByAlphaLabel"
        )}</strong>`;
      }
    },
    handlePollutantButton: function(e) {
      var self = this;
      var el = e.target;
      if (el.tagName !== "BUTTON") el = el.parentNode;

      $(el).css({ "background-color": "#2B7D3B" });
      $(el)
        .siblings()
        .css({ "background-color": "#0071bc" });
      self.selectedPollutantAll = $(el).val();
      userSelection.selectedPollutantAll = $(el).val();
      self.update();
      if (self.$children[0].clear) {
        self.$children[0].clear();
        self.$children[0].display(self.selectedPollutantAll, self.orientation);
      }
      self.pollutantText = $(el).html();
      var status = self.updateStatus(self.pollutantText, self.sortState);
      $("#nationalEmissionRateSortingStatus").html(status);
      $("#nationalFuelMixSortingStatus").html(status);
    },
    handleSortLink: function(e) {
      var self = this;
      var el = e.srcElement;
      var sortVal = el.id;
      self.setPollutantText();

      if (sortVal == "sortAlphabeticallyEmissionRate") {
        userSelection.sortState = "alphabetically";
        var status = self.updateStatus(
          self.pollutantText,
          userSelection.sortState
        );
        $(el).hide();
        $(el)
          .siblings()
          .show();
        $("#nationalEmissionRateSortingStatus").html(status);
        $("#nationalFuelMixSortingStatus").html(status);
        $("#resetNationalFuelMix").css("visibility", "hidden");
      } else if (sortVal == "sortAscendingEmissionRate") {
        userSelection.sortState = "ascending";
        var status = self.updateStatus(
          self.pollutantText,
          userSelection.sortState
        );
        $(el).hide();
        $(el)
          .siblings()
          .show();
        $("#nationalEmissionRateSortingStatus").html(status);
        $("#nationalFuelMixSortingStatus").html(status);
        $("#resetNationalFuelMix").css("visibility", "visible");
      } else if (sortVal == "sortDescendingEmissionRate") {
        userSelection.sortState = "descending";
        var status = self.updateStatus(
          self.pollutantText,
          userSelection.sortState
        );
        $(el).hide();
        $(el)
          .siblings()
          .show();
        $("#nationalEmissionRateSortingStatus").html(status);
        $("#nationalFuelMixSortingStatus").html(status);
        $("#resetNationalFuelMix").css("visibility", "visible");
      }
      self.update();
      userSelection.sortedFuel = "";
      self.$parent.reset();
      self.$parent.show(self.$parent.selectedRegion);
    }
  },
  watch: {
    selectedRegion: function() {
      this.clear();
      this.sort(this.sortState, this.selectedPollutantAll);
      this.display(this.orientation);
      this.show(this.subregionData);
      this.showSelection(this.selectedPollutantAll);
    },
    orientation: function(o) {
      userSelection.data.emissionRatesOrientation = o;
      this.clear();
      this.initialize(
        $("#main-charts").width(),
        290,
        "#nationalEmissionRateGraph"
      );
      this.display(this.orientation);
    },
    currentMap: function(m) {
      userSelection.currentMap = m;
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
