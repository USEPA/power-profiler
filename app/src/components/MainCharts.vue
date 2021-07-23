<i18n>
{
    "en": {
        "fuelMixHeader": "Fuel Mix",
        "fuelMixBody": {
            "text": "This chart compares fuel mix (%) of sources used to generate electricity in all {eGRIDSubregions}. {selectFuel}.",
            "eGRIDSubregions": "eGRID subregions",
            "selectFuel": "Select a fuel type to sort subregions by fuel"
        },
        "fuelMixChart": {
            "select": "Select:",
            "allFuelsSelection": "All Fuels",
            "renewableSelection": "Renewable/Non-renewable",
            "hydroNuclearSelection": "Renewable/Non-renewable/Nuclear/Hydro",
            "azSortDescription": "This chart is sorted alphabetically A → Z by region.",
            "fuelSortDescription": "This chart is sorted by decreasing % of {fuel}.",
            "sortLink": "Sort regions alphabetically (A → Z)",
            "eGRIDSubregions": "eGRID subregions",
            "yAxis": "Generation",
            "nationalLabel": "National",
            "fuel": "Fuel",
            "fuelTooltip": "{name} accounts for {val} % of the fuel mix for {subregion}",
            "nationalFuelTooltip": "{name} accounts for {val} % of the fuel mix nationally",
            "fuels": {
                "gas": "Gas",
                "coal": "Coal",
                "nuclear": "Nuclear",
                "hydro": "Hydro",
                "wind": "Wind",
                "biomass": "Biomass",
                "solar": "Solar",
                "oil": "Oil",
                "geothermal": "Geothermal",
                "otherFossilFuel": "Other Fossil Fuel",
                "otherUnknownFuel": "Other Uknown Fuel",
                "renewable": "Renewable",
                "non-renewable": "Non-renewable",
                "renewable (excluding hydro)": "Renewable (excluding hydro)",
                "non-renewable (excluding nuclear)": "Renewable (excluding nuclear)"
            }
        },
        "printReport": "Print Report"
    },
    "es": {
        "fuelMixHeader": "Combinación de combustibles",
        "fuelMixBody": {
            "text": "Este cuadro compara la combinación de combustibles (porcentajes) de las fuentes utilizadas para generar electricidad en todas las {eGRIDSubregions}. {selectFuel}.",
            "eGRIDSubregions": "subregiones de eGRID en los Estados Unidos",
            "selectFuel": "Seleccione un combustible para ordenar las subregiones por combustible",
            "renewable": "Renewable",
            "non-renewable": "Non-renewable"
        },
        "fuelMixChart": {
            "select": "Seleccione:",
            "allFuelsSelection": "Todos los Combustibles",
            "renewableSelection": "Renovables/No-renovables",
            "hydroNuclearSelection": "Renovables/No-renovables/Energía Nuclear/Energía Hidroeléctrica",
            "azSortDescription": "Esta gráfica está ordenada alfabéticamente (A → Z) por región.",
            "fuelSortDescription": "Esta gráfica está ordenada por el porciento (%) descendente de {fuel}.",
            "sortLink": "Ordenar las regiones alfabéticamente (A → Z)",
            "eGRIDSubregions": "Subregiones de eGRID",
            "yAxis": "Generación",
            "nationalLabel": "Nacional",
            "fuel": "Combustibles",
            "fuelTooltip": "{name} representa el {val} % la combinación de combustibles de {subregion}",
            "nationalFuelTooltip": "{name} representa el {val} % la combinación de combustibles a nivel nacional",
            "fuels": {
                "gas": "Gas",
                "coal": "Carbón",
                "nuclear": "Energía Nuclear",
                "hydro": "Energía Hidroeléctrica",
                "wind": "Energía Eólica",
                "biomass": "Biomasa",
                "solar": "Energía Solar",
                "oil": "Petróleo",
                "geothermal": "Energía Geotérmica",
                "otherFossilFuel": "Otros Combustibles Fósiles",
                "otherUnknownFuel": "Otros Combustibles Desconocidos",
                "renewable": "Renovable",
                "non-renewable": "No-renovable",
                "renewable (excluding hydro)": "Renovable (excluyendo energía hidroeléctrica)",
                "non-renewable (excluding nuclear)": "Renovable (excluyendo energía nuclear)"
            }
        },
        "printReport": "Imprima un reporte"
    }
}
</i18n>
<template>
  <div>
    <div id="nationalFuelMix">
      <h3>{{ $t("fuelMixHeader") }}</h3>
      <i18n path="fuelMixBody.text" tag="p">
        <template #eGRIDSubregions>
          <a
            href="https://www.epa.gov/sites/default/files/2021-03/2019_egrid_subregions.png"
            target="_blank"
            >{{ $t("fuelMixBody.eGRIDSubregions") }}</a
          >
        </template>
        <template #selectFuel>
          <strong>{{ $t("fuelMixBody.selectFuel") }}</strong>
        </template>
      </i18n>
      <div id="select-offset-1">
        <div
          class="form-item form-type-radio form-item-radios grid-container"
          id="fuelRadios"
        >
          <label for="fuelRadios" id="select-fuel-category"
            ><strong>{{ $t("fuelMixChart.select") }}</strong></label
          >
          <div class="grid-row grid-gap">
            <div class="grid-col-2">
              <input
                class="usa-radio"
                type="radio"
                id="fuel-breakdown-1"
                v-model="selectedFuelCategory"
                value="allFuels"
                name="fuelRadio"
                checked
              />
              <label class="option" for="fuel-breakdown-1">{{
                $t("fuelMixChart.allFuelsSelection")
              }}</label>
            </div>
            <div class="grid-col-4">
              <input
                class="usa-radio"
                type="radio"
                id="fuel-breakdown-2"
                v-model="selectedFuelCategory"
                value="renewableAndNon"
                name="fuelRadio"
              />
              <label class="option" for="fuel-breakdown-2">{{
                $t("fuelMixChart.renewableSelection")
              }}</label>
            </div>
            <div class="grid-col-6">
              <input
                class="usa-radio"
                type="radio"
                id="fuel-breakdown-3"
                v-model="selectedFuelCategory"
                value="renewableNonNuclearAndHydro"
                name="fuelRadio"
              />
              <label class="option" for="fuel-breakdown-3">{{
                $t("fuelMixChart.hydroNuclearSelection")
              }}</label>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div id="resetNationalFuelMixDiv">
      <p id="nationalFuelMixSortingStatus">
        <strong>{{ $t("fuelMixChart.azSortDescription") }}</strong>
      </p>
      <a
        href="javascript:void(0)"
        @click="handleSortReset"
        id="resetNationalFuelMix"
        >{{ $t("fuelMixChart.sortLink") }}</a
      >
    </div>
    <emissionRateChart></emissionRateChart>
    <p>
      <a href="javascript:window.print()">&#128438; {{ $t("printReport") }}</a>
    </p>
  </div>
</template>

<script>
import { allSubregions } from "../stores/allSubregions.js";
import { nationalFeature } from "../stores/nationalFeature.js";
import { selectedSubregion } from "../stores/selectedSubregion.js";
import { userSelection } from "../stores/userSelection.js";
import { addLogoBottom } from "../helpers/ChartHelpers.js";
import emissionRateChart from "./EmissionRateChart.vue";
import { addTooltip } from "../helpers/Tooltip";

export default {
  components: {
    emissionRateChart: emissionRateChart
  },
  data() {
    return {
      nationalFeature: {},
      subregionData: [],
      w: 0,
      h: 0,
      domElement: "",
      sortState: "alphabetically",
      // Fuels
      fuels: [
        "gas",
        "coal",
        "nuclear",
        "hydro",
        "wind",
        "biomass",
        "solar",
        "oil",
        "geothermal",
        "otherFossilFuel",
        "otherUnknownFuel"
      ],
      renewableAndNon: ["renewable", "non-renewable"],
      renewableNonNuclearAndHydro: [
        "hydro",
        "renewable (excluding hydro)",
        "non-renewable (excluding nuclear)",
        "nuclear"
      ],
      // Colors
      allFuelsColorRange: [
        "#ff7f00",
        "#878787",
        "#6a3d9a",
        "#1f78b4",
        "#b2df8a",
        "#33a02c",
        "#e31a1c",
        "#fdbf6f",
        "#fb9a99",
        "#cab2d6",
        "#8c510a"
      ],
      renewableAndNonColors: ["#abdda4", "#d7191c"],
      renewableNonNuclearAndHydroColors: [
        "#1f78b4",
        "#abdda4",
        "#d7191c",
        "#6a3d9a"
      ],
      subregions: {},
      sortedFuel: "",
      selectedFuelCategory: "allFuels",
      orientation: "",
      selectedRegion: {}
    };
  },
  mounted: function() {
    var self = this;
    this.orientation = userSelection.data.fuelMixOrientation;

    this.initialize($("#main-charts").width(), 350, "#nationalFuelMix");
    this.subregionData = allSubregions.data;
    this.nationalFeature = nationalFeature.data;
    this.display(this.selectedFuelCategory);
    this.selectedRegion = selectedSubregion.data;
    this.show(this.selectedRegion);

    $("#resetNationalFuelMix").css("visibility", "hidden");

    $(window).on("resize", function() {
      if ($(window).width() < 950) {
        self.orientation = "vertical";
        self.$children[0].orientation = "vertical";
      } else {
        self.orientation = "horizontal";
        self.$children[0].orientation = "horizontal";
      }
      self.reset();
    });
  },
  methods: {
    initialize: function(width, height, domElement) {
      this.w = width;
      this.h = height;
      this.domElement = domElement;
    },
    display: function(selectedFuelCategory) {
      var self = this;
      $(this.domElement).show();

      var fuelBreakdown, fuelKey, colors;
      var selectedFuel = "";
      var sortedNational = false;

      if (this.sortState == "alphabetically") {
        this.subregionData.sort(function(x, y) {
          return d3.ascending(x.properties.name, y.properties.name);
        });
      } else if (this.sortState == "ascending") {
        this.subregionData.sort(function(x, y) {
          return d3.ascending(
            x.properties.emissionFactor[self.$children[0].selectedPollutantAll]
              .value,
            y.properties.emissionFactor[self.$children[0].selectedPollutantAll]
              .value
          );
        });
      } else if (this.sortState == "descending") {
        this.subregionData.sort(function(x, y) {
          return d3.descending(
            x.properties.emissionFactor[self.$children[0].selectedPollutantAll]
              .value,
            y.properties.emissionFactor[self.$children[0].selectedPollutantAll]
              .value
          );
        });
      } else if (this.sortState == "subregionFuels") {
        this.subregionData.sort(function(x, y) {
          return d3.descending(
            x.properties.fuelMix[selectedFuel],
            y.properties.fuelMix[selectedFuel]
          );
        });
      }

      if (selectedFuelCategory == "allFuels") {
        fuelBreakdown = this.fuels;
        fuelKey = "fuelMix";
        colors = this.allFuelsColorRange;
      } else if (selectedFuelCategory == "renewableAndNon") {
        fuelBreakdown = this.renewableAndNon;
        fuelKey = "fuelMixCategories";
        colors = this.renewableAndNonColors;
      } else if (selectedFuelCategory == "renewableNonNuclearAndHydro") {
        fuelBreakdown = this.renewableNonNuclearAndHydro;
        fuelKey = "fuelMixCategories";
        colors = this.renewableNonNuclearAndHydroColors;
      }

      if (this.orientation == "horizontal") {
        this.displayHorizontal(colors, fuelBreakdown, fuelKey);
      } else if (this.orientation == "vertical") {
        this.displayVertical(colors, fuelBreakdown, fuelKey);
      }

      addTooltip(".fuelMixTooltip");
    },
    displayHorizontal: function(colors, fuelBreakdown, fuelKey) {
      var self = this;

      var margin = { top: 30, right: 70, bottom: 140, left: 70 },
        width = this.w - margin.left - margin.right,
        height = this.h - margin.top - margin.bottom;

      var x = d3.scale.ordinal().rangeRoundBands([0, width], 0.2);

      var y = d3.scale.linear().range([height, 0]);

      var color = d3.scale
        .ordinal()
        .range(colors)
        .domain(fuelBreakdown);

      var xAxis = d3.svg
        .axis()
        .scale(x)
        .outerTickSize(0)
        .orient("bottom");

      var yAxis = d3.svg
        .axis()
        .scale(y)
        .orient("left")
        .tickFormat(function(d) {
          return d + "%";
        });

      var svg = d3
        .select(self.domElement)
        .append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .append("g")
        .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

      for (var i = 0; i < self.subregionData.length; i += 1) {
        self.subregions[self.subregionData[i].properties.name] =
          self.subregionData[i].properties.fullName;
        if (self.subregionData[i].properties.name) {
          var y0 = 0;
          self.subregionData[i].properties.fuels = color
            .domain()
            .map(function(name) {
              var obj = {
                subregion: self.subregionData[i].properties.name,
                val: self.subregionData[i].properties[fuelKey][name],
                name: name,
                y0: y0,
                y1: +self.subregionData[i].properties[fuelKey][name],
                chart: self.selectedFuelCategory
              };
              y0 += +self.subregionData[i].properties[fuelKey][name];
              obj.y1 = y0;
              return obj;
            });
          self.subregionData[i].fuelTotal = d3.sum(
            d3.values(self.subregionData[i].properties[fuelKey])
          );
        }
      }

      self.subregions[self.nationalFeature[0].properties.name] =
        self.nationalFeature[0].properties.fullName;
      var yNat0 = 0;
      self.nationalFeature[0].properties.fuels = color
        .domain()
        .map(function(name) {
          var obj = {
            subregion: self.nationalFeature[0].properties.name,
            val: self.nationalFeature[0].properties[fuelKey][name],
            name: name,
            y0: yNat0,
            y1: +self.nationalFeature[0].properties[fuelKey][name],
            chart: self.selectedFuelCategory
          };
          yNat0 += +self.nationalFeature[0].properties[fuelKey][name];
          obj.y1 = yNat0;
          return obj;
        });
      self.nationalFeature[0].fuelTotal = d3.sum(
        d3.values(self.nationalFeature[0].properties[fuelKey])
      );

      x.domain(
        self.subregionData.map(function(d) {
          return d.properties.name;
        })
      );
      y.domain([0, 100]);

      svg
        .append("g")
        .attr("class", "x axis")
        .attr("transform", "translate(0," + height + ")")
        .call(xAxis)
        .selectAll("text")
        .attr("class", "subregionLabels")
        .attr("transform", "rotate(-30)")
        .style("text-anchor", "end")
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
        .text(self.$t("fuelMixChart.eGRIDSubregions"));

      svg
        .append("g")
        .attr("class", "y axis")
        .call(yAxis);

      svg
        .append("text")
        .attr("y", -20)
        .attr("x", 15)
        .attr("dy", "0.71em")
        .attr("text-anchor", "end")
        .text(self.$t("fuelMixChart.yAxis"));

      var subregion = svg
        .selectAll(".subregion")
        .data(self.subregionData)
        .enter()
        .append("g")
        .attr("class", "subregion");

      var fuels = subregion
        .selectAll("g")
        .data(function(d) {
          return d.properties.fuels;
        })
        .enter()
        .append("g")
        .attr("class", "fuelContainer fuelMixTooltip")
        .attr("title", function(fuel) {
          var fuelName = self.$t("fuelMixChart.fuels." + fuel.name);
          var f = d3.format(".1f");
          return self.addHovertext(fuel, fuelName, f);
        });

      fuels
        .append("rect")
        .attr("class", function(d) {
          return "nationalFuelMixRect " + d.chart;
        })
        .attr("x", function(d) {
          return x(d.subregion);
        })
        .attr("width", x.rangeBand())
        .attr("y", function(d) {
          return y(d.y1);
        })
        .attr("height", function(d) {
          return y(d.y0) - y(d.y1);
        })
        .style("fill", function(d) {
          return color(d.name);
        });

      subregion
        .selectAll(".nationalFuelMixRect")
        .on("click", function(fuel, i) {
          self.selectedFuel = fuel.name;
          self.handleFuelClick(
            fuel,
            fuelKey,
            x,
            y,
            subregion,
            xAxis,
            yAxis,
            self.orientation
          );
        });

      fuels.append("desc").text(function(fuel) {
        var fuelName = self.$t("fuelMixChart.fuels." + fuel.name);
        var f = d3.format(".1f");
        return self.addHovertext(fuel, fuelName, f);
      });

      var nationalBar = svg
        .selectAll(".nationalBar")
        .data(self.nationalFeature)
        .enter()
        .append("g")
        .attr("class", "nationalBar");

      var nationalFuels = nationalBar
        .selectAll("g")
        .data(function(d) {
          return d.properties.fuels;
        })
        .enter()
        .append("g")
        .attr("class", "fuelContainer fuelMixTooltip")
        .attr("title", function(fuel) {
          var fuelName = self.$t("fuelMixChart.fuels." + fuel.name);
          var f = d3.format(".1f");
          return self.addHovertext(fuel, fuelName, f);
        });

      nationalFuels
        .append("rect")
        .attr("class", function(d) {
          return "nationalFuelMixRect " + d.chart;
        })
        .attr("x", function(d) {
          return width + 20;
        })
        .attr("width", x.rangeBand())
        .attr("y", function(d) {
          return y(d.y1);
        })
        .on("click", function(fuel, i) {
          self.selectedFuel = fuel.name;
          self.handleFuelClick(
            fuel,
            fuelKey,
            x,
            y,
            subregion,
            xAxis,
            yAxis,
            self.orientation
          );
        })
        .attr("height", function(d) {
          return y(d.y0) - y(d.y1);
        })
        .style("fill", function(d) {
          return color(d.name);
        });

      nationalFuels.append("desc").text(function(fuel) {
        var fuelName = self.$t("fuelMixChart.fuels." + fuel.name);
        var f = d3.format(".1f");
        return self.addHovertext(fuel, fuelName, f);
      });

      var nationalX = d3.scale
        .ordinal()
        .rangeRoundBands([width, width + 20], 0.2);

      var nationalBarXAxis = d3.svg
        .axis()
        .scale(nationalX)
        .outerTickSize(0)
        .orient("bottom");

      nationalBar
        .append("g")
        .attr("class", "nationalBar")
        .attr("transform", "translate(" + x.rangeBand() + "," + height + ")")
        .call(nationalBarXAxis)
        .append("text")
        .text(self.$t("fuelMixChart.nationalLabel"))
        .attr("x", width - 20)
        .attr("y", 30);

      var offset1 = 300,
        offset2 = 170;

      var legendBottom = svg
        .selectAll(".legendBottom")
        .data(color.domain())
        .enter()
        .append("g")
        .attr("class", "legendBottom")
        .attr("transform", function(d, i) {
          if (self.selectedFuelCategory == "renewableNonNuclearAndHydro") {
            // First row
            if (i === 0) {
              return `translate(${width / 2 - offset1},${height + 120})`;
            } else if (i === 1) {
              return `translate(${width / 2 - offset1},${height + 60})`;
            } else if (i === 2) {
              return `translate(${width / 2 - offset1},${height + 80})`;
            } else if (i === 3) {
              return `translate(${width / 2 - offset1},${height + 100})`;
            }
          } else {
            // First row
            if (i === 0) {
              return `translate(${width / 2 - offset1},${height + 60})`;
            } else if (i === 1) {
              return `translate(${width / 2 - offset1},${height + 80})`;
            } else if (i === 2) {
              return `translate(${width / 2 - offset1},${height + 100})`;
            }
            // Sec row
            else if (i === 3) {
              return `translate(${width / 2 - offset2},${height + 60})`;
            } else if (i === 4) {
              return `translate(${width / 2 - offset2},${height + 80})`;
            } else if (i === 5) {
              return `translate(${width / 2 - offset2},${height + 100})`;
            }
            // Third row
            else if (i === 6) {
              return `translate(${width / 2},${height + 60})`;
            } else if (i === 7) {
              return `translate(${width / 2},${height + 80})`;
            } else if (i === 8) {
              return `translate(${width / 2},${height + 100})`;
            } else if (i === 9) {
              return `translate(${width / 2 + offset2},${height + 60})`;
            } else if (i === 10) {
              return `translate(${width / 2 + offset2},${height + 80})`;
            }
          }
        })
        .on("click", function(d) {
          var fuel = { name: d, chart: self.selectedFuelCategory };
          d3.selectAll(".textselected").style("font-weight", function(d) {
            if (d == fuel.name) {
              return "bold";
            } else {
              return "normal";
            }
          });
          self.selectedFuel = fuel.name;
          self.handleFuelClick(
            fuel,
            fuelKey,
            x,
            y,
            subregion,
            xAxis,
            yAxis,
            self.orientation
          );
        });

      legendBottom
        .append("rect")
        .attr("x", 0)
        .attr("y", 0)
        .attr("width", 10)
        .attr("height", 10)
        .style("fill", color);

      legendBottom
        .append("text")
        .attr("x", 20)
        .attr("y", 10)
        .text(function(d, i) {
          return self.$t("fuelMixChart.fuels." + d);
        })
        .attr("class", "textselected")
        .style("text-anchor", "start")
        .style("font-size", 15);

      var duration = { sub: 300, x: 0 };
      if (self.sortedFuel)
        self.sortHorizontalBarChart(
          self.sortedFuel,
          duration,
          fuelKey,
          x,
          y,
          subregion,
          xAxis
        );

      addLogoBottom(svg, width - 10, height + 120);
    },
    sortHorizontalBarChart(fuel, duration, fuelKey, x, y, subregion, xAxis) {
      var self = this;
      self.sortedFuel = fuel;
      userSelection.sortedFuel = self.sortedFuel;
      $("#resetNationalFuelMix").css("visibility", "visible");
      var selectedFuelArr = [];
      var sortedSubregionData = allSubregions.data
        .sort(function(a, b) {
          return (
            b.properties[fuelKey][fuel.name] - a.properties[fuelKey][fuel.name]
          );
        })
        .map(function(d) {
          return d.properties.name;
        });

      var x0 = x.domain(sortedSubregionData).copy();
      d3.selectAll("." + fuel.chart)
        .attr("y", function(d) {
          if (d.name == fuel.name) {
            d3.select(this).attr("class", fuel.chart + " selected");
            selectedFuelArr.push({ subregion: d.subregion, newBase: d.val });
            return y(d.val);
          } else {
            d3.select(this).attr("class", fuel.chart + " unselected");
          }
        });

      d3.selectAll(".unselected").attr("y", function(d) {
        if (d.name != fuel.name) {
          for (var i = 0; i < selectedFuelArr.length; i += 1) {
            if (selectedFuelArr[i].subregion == d.subregion) {
              selectedFuelArr[i].newBase += d.val;
              return y(selectedFuelArr[i].newBase);
            }
          }
        }
      });

      //Iterate through each fuels array
      var svg = d3.select(self.domElement);
      svg.selectAll("fuelContainer").sort(function(a, b) {
        return x0(a.subregion) - x0(b.subregion);
      });

      var transition = subregion.transition().duration(duration.sub),
        delay = function(d, i) {
          return i * 50;
        };

      if (duration.sub != 0) {
        transition
          .selectAll("rect")
          .delay(delay)
          .attr("x", function(d) {
            if (d.subregion != "National") {
              return x0(d.subregion);
            }
          });

        var transitionX = svg.transition().duration(duration.x);

        transitionX
          .select(".x.axis")
          .call(xAxis)
          .selectAll("g")
          .delay(delay);
      } else {
        transition.selectAll("rect").attr("x", function(d) {
          if (d.subregion != "National") {
            return x0(d.subregion);
          }
        });

        svg.select(".x.axis").call(xAxis);
      }

      d3.selectAll(self.domElement + " .x.axis text")
        .style("text-anchor", "end")
        .append("title")
        .text(function(d) {
          return d + " (" + self.subregions[d] + ")";
        });
    },
    displayVertical: function(colors, fuelBreakdown, fuelKey) {
      var self = this;
      var margin = { top: 120, right: 20, bottom: 80, left: 65 },
        width = 600 - margin.left - margin.right,
        height = 800 - margin.top - margin.bottom;

      var x = d3.scale.linear().range([0, width]);

      var y = d3.scale.ordinal().rangeRoundBands([0, height], 0.2);

      var color = d3.scale
        .ordinal()
        .range(colors)
        .domain(fuelBreakdown);

      var yAxis = d3.svg
        .axis()
        .scale(y)
        .outerTickSize(0)
        .orient("left");

      var xAxis = d3.svg
        .axis()
        .scale(x)
        .orient("top")
        .tickFormat(function(d) {
          return d + "%";
        });

      var svg = d3
        .select(self.domElement)
        .append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.bottom + margin.top)
        .append("g")
        .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

      for (var i = 0; i < self.subregionData.length; i += 1) {
        self.subregions[self.subregionData[i].properties.name] =
          self.subregionData[i].properties.fullName;
        if (self.subregionData[i].properties.name) {
          var x0 = 0;
          self.subregionData[i].properties.fuels = color
            .domain()
            .map(function(name) {
              var obj = {
                subregion: self.subregionData[i].properties.name,
                val: self.subregionData[i].properties[fuelKey][name],
                name: name,
                x0: x0,
                x1: +self.subregionData[i].properties[fuelKey][name],
                chart: self.selectedFuelCategory
              };
              x0 += +self.subregionData[i].properties[fuelKey][name];
              obj.x1 = x0;
              return obj;
            });
          self.subregionData[i].fuelTotal = d3.sum(
            d3.values(self.subregionData[i].properties[fuelKey])
          );
        }
      }

      self.subregions[self.nationalFeature[0].properties.name] =
        self.nationalFeature[0].properties.fullName;
      var xn0 = 0;
      self.nationalFeature[0].properties.fuels = color
        .domain()
        .map(function(name) {
          var obj = {
            subregion: self.nationalFeature[0].properties.name,
            val: self.nationalFeature[0].properties[fuelKey][name],
            name: name,
            x0: xn0,
            x1: +self.nationalFeature[0].properties[fuelKey][name],
            chart: self.selectedFuelCategory
          };
          xn0 += +self.nationalFeature[0].properties[fuelKey][name];
          obj.x1 = xn0;
          return obj;
        });
      self.nationalFeature[0].fuelTotal = d3.sum(
        d3.values(self.nationalFeature[0].properties[fuelKey])
      );

      y.domain(
        self.subregionData.map(function(d) {
          return d.properties.name;
        })
      );
      x.domain([0, 100]);

      svg
        .append("g")
        .attr("class", "y axis")
        .attr("transform", "translate(0,0)")
        .call(yAxis);

      svg
        .append("text")
        .attr("y", -40)
        .attr("x", 50)
        .attr("dy", "0.71em")
        .attr("text-anchor", "middle")
        .text(self.$t("fuelMixChart.yAxis"));

      svg
        .selectAll("text")
        .style("text-anchor", "end")
        .append("title")
        .text(function(d) {
          return d + " (" + self.subregions[d] + ")";
        });

      svg
        .append("g")
        .attr("class", "x axis")
        .call(xAxis);

      var subregion = svg
        .selectAll(".subregion")
        .data(self.subregionData)
        .enter()
        .append("g")
        .attr("class", "subregion");

      var fuels = subregion
        .selectAll("g")
        .data(function(d) {
          return d.properties.fuels;
        })
        .enter()
        .append("g")
        .attr("class", "fuelContainer fuelMixTooltip")
        .attr("title", function(fuel) {
          var fuelName = self.$t("fuelMixChart.fuels." + fuel.name);
          var f = d3.format(".1f");
          return self.addHovertext(fuel, fuelName, f);
        });

      fuels
        .append("rect")
        .attr("class", function(d) {
          return "nationalFuelMixRect " + d.chart;
        })
        .attr("y", function(d) {
          return y(d.subregion);
        })
        .attr("height", y.rangeBand())
        .attr("x", function(d) {
          return x(d.x0);
        })
        .on("click", function(fuel, i) {
          self.selectedFuel = fuel.name;
          self.handleFuelClick(
            fuel,
            fuelKey,
            x,
            y,
            subregion,
            xAxis,
            yAxis,
            self.orientation
          );
        })
        .attr("width", function(d) {
          return x(d.x1) - x(d.x0);
        })
        .style("fill", function(d) {
          return color(d.name);
        });

      fuels.append("desc").text(function(fuel) {
        var fuelName = self.$t("fuelMixChart.fuels." + fuel.name);
        var f = d3.format(".1f");
        return self.addHovertext(fuel, fuelName, f);
      });

      var nationalBar = svg
        .selectAll(".nationalBar")
        .data(self.nationalFeature)
        .enter()
        .append("g")
        .attr("class", "nationalBar");

      var nationalFuels = nationalBar
        .selectAll("g")
        .data(function(d) {
          return d.properties.fuels;
        })
        .enter()
        .append("g")
        .attr("class", "fuelContainer fuelMixTooltip")
        .attr("title", function(fuel) {
          var fuelName = self.$t("fuelMixChart.fuels." + fuel.name);
          var f = d3.format(".1f");
          return self.addHovertext(fuel, fuelName, f);
        });

      nationalFuels
        .append("rect")
        .attr("class", function(d) {
          return "nationalFuelMixRect " + d.chart;
        })
        .attr("y", function(d) {
          return height;
        })
        .attr("height", y.rangeBand())
        .attr("x", function(d) {
          return x(d.x0);
        })
        .on("click", function(fuel, i) {
          self.selectedFuel = fuel.name;
          self.handleFuelClick(
            fuel,
            fuelKey,
            x,
            y,
            subregion,
            xAxis,
            yAxis,
            self.orientation
          );
        })
        .attr("width", function(d) {
          return x(d.x1) - x(d.x0);
        })
        .style("fill", function(d) {
          return color(d.name);
        });

      nationalFuels.append("desc").text(function(fuel) {
        var fuelName = self.$t("fuelMixChart.fuels." + fuel.name);
        var f = d3.format(".1f");
        return self.addHovertext(fuel, fuelName, f);
      });

      var nationalY = d3.scale
        .ordinal()
        .rangeRoundBands([height, height + 20], 0.2);

      var nationalBarYAxis = d3.svg
        .axis()
        .scale(nationalY)
        .orient("left");

      nationalBar
        .append("g")
        .attr("class", "nationalY")
        .call(nationalBarYAxis)
        .append("text")
        .text(self.$t("fuelMixChart.nationalLabel"))
        .attr("x", -65)
        .attr("y", height + 15);

      var topLen = 0;
      var midLen = 0;

      var legendTop = svg
        .selectAll(".legendTop")
        .data(color.domain())
        .enter()
        .append("g")
        .attr("class", "legendTop")
        .attr("transform", function(d, i) {
          const initialOffset = 60;
          const squareOffset = 20;
          const multiplier = 5.5;
          const wordLen = self.$t(`fuelMixChart.fuels.${d}`).length;

          if (self.selectedFuelCategory == "renewableNonNuclearAndHydro") {
            // First row
            if (i === 0) {
              if (wordLen > topLen) topLen = wordLen;
              return `translate(${0 - initialOffset}, ${-60})`;
            } else if (i === 1) {
              if (wordLen > topLen) topLen = wordLen;
              return `translate(${0 - initialOffset}, ${-120})`;
            } else if (i === 2) {
              if (wordLen > topLen) topLen = wordLen;
              return `translate(${0 - initialOffset}, ${-100})`;
            } else if (i === 3) {
              if (wordLen > topLen) topLen = wordLen;
              return `translate(${0 - initialOffset}, ${-80})`;
            }
          } else {
            // First col
            if (i === 0) {
              if (wordLen > topLen) {
                topLen = wordLen;
              }
              return `translate(${0 - initialOffset}, ${-120})`;
            } else if (i === 1) {
              if (wordLen > topLen) {
                topLen = wordLen;
              }
              return `translate(${0 - initialOffset}, ${-100})`;
            } else if (i === 2) {
              if (wordLen > topLen) {
                topLen = wordLen;
              }
              return `translate(${0 - initialOffset}, ${-80})`;
            } else if (i === 3) {
              if (wordLen > topLen) {
                topLen = wordLen;
              }
              return `translate(${0 - initialOffset}, ${-60})`;
            }
            // Sec col
            else if (i === 4) {
              if (wordLen > midLen) {
                midLen = wordLen;
              }
              return `translate(${topLen * multiplier - squareOffset}, -120)`;
            } else if (i === 5) {
              if (wordLen > midLen) {
                midLen = wordLen;
              }
              return `translate(${topLen * multiplier - squareOffset}, -100)`;
            } else if (i === 6) {
              if (wordLen > topLen) {
                topLen = wordLen;
              }
              return `translate(${topLen * multiplier - squareOffset}, -80)`;
            } else if (i === 7) {
              if (wordLen > topLen) {
                topLen = wordLen;
              }
              return `translate(${topLen * multiplier - squareOffset}, -60)`;
            }
            // Third col
            else if (i === 8) {
              return `translate(${(midLen + topLen) * multiplier +
                squareOffset}, -120)`;
            } else if (i === 9) {
              return `translate(${(midLen + topLen) * multiplier +
                squareOffset}, -100)`;
            } else if (i === 10) {
              return `translate(${(midLen + topLen) * multiplier +
                squareOffset}, -80)`;
            }
          }
        })
        .on("click", function(d) {
          var fuel = { name: d, chart: self.selectedFuelCategory };
          d3.selectAll(".textselected").style("font-weight", function(d) {
            if (d == fuel.name) {
              return "bold";
            } else {
              return "normal";
            }
          });
          self.selectedFuel = fuel.name;
          self.handleFuelClick(
            fuel,
            fuelKey,
            x,
            y,
            subregion,
            xAxis,
            yAxis,
            self.orientation
          );
        });

      legendTop
        .append("rect")
        .attr("x", 0)
        .attr("y", 0)
        .attr("width", 10)
        .attr("height", 10)
        .style("fill", color);

      legendTop
        .append("text")
        .attr("x", 20)
        .attr("y", 10)
        .text(function(d, i) {
          return self.$t("fuelMixChart.fuels." + d);
        })
        .attr("class", function(d) {
          return "textselected";
        })
        .style("text-anchor", "start")
        .style("font-size", 15);

      var duration = { sub: 300, x: 0 };
      if (self.sortedFuel)
        self.sortVerticalBarChart(
          self.sortedFuel,
          duration,
          fuelKey,
          x,
          y,
          subregion,
          yAxis
        );
      addLogoBottom(svg, width - 60, height + 50);
    },
    sortVerticalBarChart: function(
      fuel,
      duration,
      fuelKey,
      x,
      y,
      subregion,
      yAxis
    ) {
      var self = this;
      self.sortedFuel = fuel;
      userSelection.sortedFuel = self.sortedFuel;
      $("#resetNationalFuelMix").css("visibility", "visible");
      var selectedFuelArr = [];

      var y0 = y
        .domain(
          self.subregionData
            .sort(function(a, b) {
              return (
                b.properties[fuelKey][fuel.name] -
                a.properties[fuelKey][fuel.name]
              );
            })
            .map(function(d) {
              return d.properties.name;
            })
        )
        .copy();

      d3.selectAll("." + fuel.chart)
        .style("opacity", function(d) {
          if (d.name == fuel.name) {
            return 1;
          } else {
            return 0.5;
          }
        })
        .attr("x", function(d) {
          if (d.name == fuel.name) {
            d3.select(this).attr("class", fuel.chart + " selected");
            selectedFuelArr.push({ subregion: d.subregion, newBase: d.val });
            return x(0);
          } else {
            d3.select(this).attr("class", fuel.chart + " unselected");
          }
        });

      d3.selectAll(".unselected").attr("x", function(d) {
        if (d.name != fuel.name) {
          for (var i = 0; i < selectedFuelArr.length; i += 1) {
            if (selectedFuelArr[i].subregion == d.subregion) {
              selectedFuelArr[i].newBase += d.val;
              return x(selectedFuelArr[i].newBase) - x(d.val);
            }
          }
        }
      });

      //Iterate through each fuels array
      var svg = d3.select(self.domElement);
      var subregion = svg.selectAll(".subregion").sort(function(a, b) {
        return y0(a.subregion) - y0(b.subregion);
      });

      var transition = subregion.transition().duration(duration.sub),
        delay = function(d, i) {
          return i * 50;
        };

      if (duration.sub != 0) {
        transition
          .selectAll("rect")
          .delay(delay)
          .attr("y", function(d) {
            if (d.subregion != "National") {
              return y0(d.subregion);
            }
          });

        var transitionY = svg.transition().duration(200);
        var yDelay = function(d, i) {
          return i * 20;
        };

        transitionY
          .select(".y.axis")
          .call(yAxis)
          .selectAll("g")
          .delay(yDelay);
      } else {
        transition.selectAll("rect").attr("y", function(d) {
          if (d.subregion != "National") {
            return y0(d.subregion);
          }
        });

        svg.select(".y.axis").call(yAxis);
      }

      d3.selectAll(self.domElement + " .y.axis text")
        .style("text-anchor", "end")
        .append("title")
        .text(function(d) {
          return d + " (" + self.subregions[d] + ")";
        });
    },
    reset: function() {
      d3.selectAll("#nationalFuelMix svg").remove();
      this.sortedFuel = userSelection.sortedFuel;
      this.sortState = userSelection.sortState;
      this.initialize($("#main-charts").width(), 350, "#nationalFuelMix");
      this.display(this.selectedFuelCategory);
    },
    show: function(selectedRegion) {
      var self = this;
      if (Object.keys(selectedRegion).length) {
        d3.selectAll(self.domElement + " .tick text").attr(
          "font-weight",
          function(d) {
            if (d == selectedRegion.properties.name) {
              return "bold";
            }
          }
        );
      }
    },
    handleFuelClick: function(
      fuel,
      fuelKey,
      x,
      y,
      subregion,
      xAxis,
      yAxis,
      orientation
    ) {
      var self = this;
      d3.selectAll(".textselected").style("font-weight", function(d) {
        if (d == fuel.name) {
          return "bold";
        } else {
          return "normal";
        }
      });
      self.selectedFuel = fuel.name;
      userSelection.sortedFuel = self.sortedFuel;
      self.sortedNational = true;
      var duration = { sub: 300, x: 0 };
      if (orientation == "horizontal") {
        this.sortHorizontalBarChart(
          fuel,
          duration,
          fuelKey,
          x,
          y,
          subregion,
          xAxis
        );
      } else {
        this.sortVerticalBarChart(
          fuel,
          duration,
          fuelKey,
          x,
          y,
          subregion,
          yAxis
        );
      }
      self.sortState = "subregionFuels";

      $("#sortingDiv > a").show();
      $("#nationalFuelMixSortingStatus").html(
        `<strong>${this.$t("fuelMixChart.fuelSortDescription", {
          fuel: this.$t("fuelMixChart.fuels." + self.selectedFuel)
        })}`
      );
      $("#nationalEmissionRateSortingStatus").html(
        `<strong>${this.$t("fuelMixChart.fuelSortDescription", {
          fuel: this.$t("fuelMixChart.fuels." + self.selectedFuel)
        })}`
      );
      self.updateChild("subregionFuels", fuel);
    },
    handleSortReset: function() {
      this.subregionData.sort(function(x, y) {
        return d3.ascending(x.properties.name, y.properties.name);
      });
      this.sortState = "alphabetically";
      userSelection.sortedFuel = "";
      this.sortedFuel = userSelection.sortedFuel;
      this.reset();
      this.updateChild("alphabetically", "");
      $("#resetNationalFuelMix").css("visibility", "hidden");
      $("#sortAlphabeticallyEmissionRate").css("display", "none");
      $("#sortAscendingEmissionRate").css("display", "inline");
      $("#sortDescendingEmissionRate").css("display", "inline");
      $("#nationalEmissionRateSortingStatus").html(
        `<strong>${this.$t("fuelMixChart.azSortDescription")}</strong>`
      );
      $("#nationalFuelMixSortingStatus").html(
        `<strong>${this.$t("fuelMixChart.azSortDescription")}</strong>`
      );
    },
    addHovertext: function(fuel, fuelName, f) {
      if (fuel.subregion === "National") {
        return this.$t("fuelMixChart.nationalFuelTooltip", {
          name: fuelName,
          val: f(fuel.val)
        });
      } else {
        return this.$t("fuelMixChart.fuelTooltip", {
          name: fuelName,
          val: f(fuel.val),
          subregion: fuel.subregion
        });
      }
    },
    updateChild: function(sortState, fuel) {
      var emRateChart = this.$children[0];
      if (fuel) {
        emRateChart.selectedFuel = fuel.name;
      }
      userSelection.sortState = sortState;
      emRateChart.update();
    }
  },
  watch: {
    selectedFuelCategory: function() {
      this.reset();
      this.show(this.selectedRegion);
    },
    orientation: function(o) {
      userSelection.data.fuelMixOrientation = o;
      this.reset();
    },
    selectedRegion: function() {
      this.reset();
      this.show(this.selectedRegion);
    },
    "$root.$i18n.locale": {
      deep: true,
      handler() {
        this.reset();
      }
    }
  }
};
</script>

<style>
.legendBottom,
.legendTop {
  cursor: pointer;
}
.ui-tooltip {
  pointer-events: none;
}
#nationalFuelMix > h3,
#nationalEmissionRate > h3 {
  display: inline-block;
}
#nationalEmissionRate {
  margin-top: 20px;
}
</style>
