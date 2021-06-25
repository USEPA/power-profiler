<i18n>
{
    "en": {
      "fuel": "Fuel",
      "generation": "Generation",
      "national": "National",
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
        "otherUnknownFuel": "Other Uknown Fuel"
      }

    },
    "es": {
      "fuel": "Combustibles",
      "generation": "Generacion",
      "national": "Nacional",
      "fuelTooltip": "{name} representa el {val} % la combinación de combustibles del {subregion}",
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
        "otherUnknownFuel": "Otros Combustibles Desconocidos"
      }
    }
}
</i18n>

<template>
  <div>
    <div id="fuelMix"></div>
  </div>
</template>
<script>
import { addLogoBottom } from "../helpers/ChartHelpers.js";
import { nationalFeature } from "../stores/nationalFeature.js";
import { selectedSubregion } from "../stores/selectedSubregion.js";
import { addTooltip } from "../helpers/Tooltip";

export default {
  data() {
    return {
      graphData: []
    };
  },
  watch: {
    "$root.$i18n.locale": {
      deep: true,
      handler() {
        this.update();
      }
    }
  },
  mounted: function() {
    var self = this;
    this.graphData.push(nationalFeature.data[0]);
    this.graphData.push(selectedSubregion.data);
    this.display(this.graphData);

    $(window).on("resize", function() {
      self.update();
    });
  },
  methods: {
    display: function(data) {
      var _this = this;
      var domElement = "#fuelMix";
      var w = $(domElement).width();
      var h = 500;
      var allFuelsColorRange = [
        "#fdae61",
        "#313695",
        "#f46d43",
        "#74add1",
        "#abd9e9",
        "#4575b4",
        "#ffffbf",
        "#d73027",
        "#fee090",
        "#e0f3f8",
        "#a50026"
      ];
      var fuels = [
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
      ];

      var margin = { top: 40, right: 30, bottom: 200, left: 50 },
        width = w - margin.left - margin.right,
        height = h - margin.top - margin.bottom;

      var x = d3.scale.ordinal().rangeRoundBands([0, width], 0.3);

      var y = d3.scale.linear().rangeRound([height, 0]);

      var color = d3.scale
        .ordinal()
        .range(allFuelsColorRange)
        .domain(fuels);

      var xAxis = d3.svg
        .axis()
        .scale(x)
        .outerTickSize(0)
        .orient("bottom")
        .tickFormat(function(d) {
          if (d === "National") {
            return _this.$t("national");
          } else {
            return d;
          }
        });

      var yAxis = d3.svg
        .axis()
        .scale(y)
        .orient("left")
        .tickFormat(function(d) {
          return d + "%";
        });

      var svg = d3
        .select(domElement)
        .append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .append("g")
        .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

      for (var i = 0; i < data.length; i += 1) {
        var y0 = 0;
        data[i].properties.fuels = color.domain().map(function(name) {
          var obj = {
            subregion: data[i].properties.name,
            name: name,
            val: data[i].properties.fuelMix[name],
            y0: y0,
            y1: +data[i].properties.fuelMix[name]
          };
          y0 += +data[i].properties.fuelMix[name];
          obj.y1 = y0;
          return obj;
        });
      }

      x.domain(
        data.map(function(d) {
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
        .style("text-anchor", "middle");

      svg
        .append("g")
        .attr("class", "y axis")
        .call(yAxis);

      svg
        .append("text")
        .attr("y", -30)
        .attr("x", 30)
        .attr("dy", "0.71em")
        .attr("text-anchor", "end")
        .text(this.$t("generation"));

      svg
        .append("text")
        .attr("y", height + 180)
        .attr("x", width / 8)
        .attr("class", "legendTitle")
        .attr("dy", "0.71em")
        .attr("text-anchor", "beginning")
        .text(
          `${this.$t("fuel")} (${data[1].properties.name} ${this.$t(
            "generation"
          )} %)`
        );

      var subregion = svg
        .selectAll(".subregion")
        .data(data)
        .enter()
        .append("g")
        .attr("class", "subregion");

      var f = d3.format(".1f");

      subregion
        .selectAll("rect")
        .data(function(d) {
          return d.properties.fuels;
        })
        .enter()
        .append("rect")
        .attr("x", function(d) {
          return x(d.subregion);
        })
        .attr("class", "subFuelMixTooltip")
        .attr("width", x.rangeBand())
        .attr("y", function(d) {
          return y(d.y1);
        })
        .attr("title", function(fuel) {
          if (fuel.subregion === "National") {
            return _this.$t("nationalFuelTooltip", {
              name: _this.$t("fuels." + fuel.name),
              val: f(fuel.val)
            });
          } else {
            return _this.$t("fuelTooltip", {
              name: _this.$t("fuels." + fuel.name),
              val: f(fuel.val),
              subregion: fuel.subregion
            });
          }
        })
        .attr("height", function(d) {
          return y(d.y0) - y(d.y1);
        })
        .style("fill", function(d) {
          return color(d.name);
        });
      var legendBottomSub = svg
        .selectAll(".legendBottomSub")
        .data(color.domain())
        .enter()
        .append("g")
        .attr("class", "legendBottomSub")
        .attr("transform", function(d, i) {
          var x = -48;
          // First col
          if (i === 0) {
            return "translate(" + x + "," + (height + 30) + ")";
          } else if (i === 1) {
            return "translate(" + x + "," + (height + 50) + ")";
          } else if (i === 2) {
            return "translate(" + x + "," + (height + 70) + ")";
          } else if (i === 3) {
            return "translate(" + x + "," + (height + 90) + ")";
          } else if (i === 4) {
            return "translate(" + x + "," + (height + 110) + ")";
          } else if (i === 5) {
            return "translate(" + x + "," + (height + 130) + ")";
            // Sec col
          } else if (i === 6) {
            return "translate(" + (x + 181) + "," + (height + 30) + ")";
          } else if (i === 7) {
            return "translate(" + (x + 181) + "," + (height + 50) + ")";
          } else if (i === 8) {
            return "translate(" + (x + 181) + "," + (height + 70) + ")";
          } else if (i === 9) {
            return "translate(" + (x + 181) + "," + (height + 90) + ")";
          } else if (i === 10) {
            return "translate(" + (x + 181) + "," + (height + 110) + ")";
          }
        });

      legendBottomSub
        .append("rect")
        .attr("x", 0)
        .attr("y", 0)
        .attr("width", 10)
        .attr("height", 10)
        //A dark border around the square to distinguish colors from background
        .style("stroke", "#212121")
        .style("fill", color);

      legendBottomSub
        .append("text")
        .attr("x", 20)
        .attr("y", 10)
        .text(function(d, i) {
          return `${_this.$t(
            "fuels." + d
          )} (${data[1].properties.fuelMix[d]} %)`;
        })
        .attr("class", function(d) {
          return "textselected";
        })
        .style("text-anchor", "start");

      var lgLabels = svg.selectAll(domElement + " .lgLabel");

      lgLabels.append("tspan").text(function(d) {
        return _this.$t("fuels." + d);
      });

      var baseline = (height + margin.top + margin.bottom) * 0.34;
      addLogoBottom(svg, width - 100, height + baseline);

      d3.selectAll(domElement + " text").style(
        "font-family",
        "'Source Sans Pro', 'Helvetica Neue', 'Helvetica', 'Roboto', 'Arial', sans-serif"
      );

      d3.selectAll(domElement + " .y.axis path," + domElement + " .axis line")
        .style("fill", "none")
        .style("stroke", "#000")
        .style("shape-rendering", "crispEdges");

      d3.selectAll(domElement + " .legendBottomSub text").style(
        "font-size",
        "0.7em"
      );
      $("#fuelMix > svg").css("margin-top", "25%");

      addTooltip(".subFuelMixTooltip");
    },
    update() {
      this.graphData = [];
      this.graphData.push(nationalFeature.data[0]);
      this.graphData.push(selectedSubregion.data);
      d3.selectAll("#fuelMix svg").remove();
      this.display(this.graphData);
    }
  }
};
</script>

<style>
#select-fuel-category,
#fuelRadios,
#resetNationalFuelMixDiv,
#sortingDiv {
  text-align: center;
}
</style>
