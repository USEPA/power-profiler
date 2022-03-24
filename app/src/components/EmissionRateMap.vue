<i18n>
{
    "en": {
        "description": {
            "text": "This map provides {eGRIDSubregion} average emission rates in pounds per {MWh}.",
            "eGRIDSubregion": "eGRID subregion",
            "MWh": "MWh"
        },
        "tooltip": {
            "text": "{subregionName} average {pollutant} rate: {rate} lbs/MWh"
        }
    },
    "es": {
        "description": {
            "text": "Este mapa incluye tasas de emisión promedio para las {eGRIDSubregion} en libras por {MWh}.",
            "eGRIDSubregion": "subregiones de eGRID",
            "MWh": "MWh"
        },
        "tooltip": {
            "text": "Tasas de {pollutant} para las {subregionName}: {rate} lbs/MWh"
        }
    }
}
</i18n>

<template>
  <div>
    <i18n path="description.text" tag="p">
      <template #eGRIDSubregion>
        <a
          :href=egridSubregionMap
          target="_blank"
          >{{ $t("description.eGRIDSubregion") }}</a
        >
      </template>
      <template #MWh>
        <a
          @click="$parent.$parent.$parent.showMegaWattInfo = true"
          href="javascript:void(0)"
          >{{ $t("description.MWh") }}</a
        >
      </template>
    </i18n>
    <div class="grid-row flex-justify-center flex-align-center" id="emissionRatesHeatMap"></div>
  </div>
</template>
<script>
import { addLogoBottom } from "../helpers/ChartHelpers.js";
import { addSubregionLabels } from "../helpers/MapHelpers.js";
import { allSubregions } from "../stores/allSubregions.js";
import { userSelection } from "../stores/userSelection.js";
import { addTooltip } from "../helpers/Tooltip";
import { geoAlbersUsaTerritories } from "geo-albers-usa-territories";
import { constVal } from "../helpers/const.js";

export default {
  data() {
    return {
      orientation: "",
      width: 600,
      height: 300,
      domElement: "",
      projection: {},
      path: {},
      containerHeight: 0,
      subregionData: [],
      egridSubregionMap: constVal.egridSubregionMapUrl
    };
  },
  mounted: function() {
    var self = this;
    this.orientation = userSelection.data.emissionRatesOrientation;
    this.initialize(600, 300, "#emissionRatesHeatMap");
    this.createProjection();
    this.display(this.$parent.selectedPollutantAll, this.orientation);
  },
  methods: {
    initialize: function(width, height, domElement) {
      this.width = width;
      this.height = height;
      this.domElement = domElement;
      this.subregionData = allSubregions.data;
    },
    createProjection: function() {
      this.projection = geoAlbersUsaTerritories()
        .translate([this.width / 2, this.height / 2])
        .scale([this.width + 100]);
      // Define path generator
      this.path = d3.geo.path().projection(this.projection);
    },
    clear: function() {
      d3.selectAll("#emissionRatesHeatMap svg").remove();
    },
    hide: function() {
      $(this.domElement)
        .parent()
        .hide();
    },
    show: function() {
      $(this.domElement)
        .parent()
        .show();
      $(window).trigger("resize");
    },
    display: function(emissionRate, orientation) {
      var _this = this;

      var svg = d3
        .select(_this.domElement)
        .append("svg")
        .attr("class", "grid-col-10")
        .attr("width", _this.width)
        .attr("height", _this.height)
        .attr("viewBox", "0 0 " + _this.width + " " + _this.height)
        .attr("preserveAspectRatio", "xMidYMid meet")
        .attr("fill", "gainsboro");

      var aspect = _this.width / _this.height;

      $(window)
        .on("resize", function() {
          var targetWidth = $("#main-charts").width();
          svg.attr("width", targetWidth);
          svg.attr("height", Math.round(targetWidth / aspect));
        })
        .trigger("resize");

      var max = d3.max(this.subregionData, function(d) {
        return d.properties.emissionFactor[emissionRate].value;
      });

      var color = d3.scale
        .linear()
        .domain([0, max])
        .range(["#eeeeee", _this.$parent.emRatesColors[emissionRate]]);

      if (this.orientation == "horizontal") {
        this.containerHeight = 400;
        this.svgGradient = d3
          .select(this.domElement)
          .append("svg")
          .attr("width", 100)
          .attr("height", this.containerHeight);
      } else if (this.orientation == "vertical") {
        this.containerHeight = 120;
        this.svgGradient = d3
          .select(this.domElement)
          .append("svg")
          .attr("width", 400)
          .attr("height", this.containerHeight);
      }

      var pollutantLabelTooltip = "";
      var legendLabel = this.svgGradient
        .append("text")
        .attr("y", 20)
        .attr("x", 20)
        .append("tspan")
        .text(function() {
          if (emissionRate == "co2EmissionRate") {
            pollutantLabelTooltip = "carbon dioxide";
            return "CO";
          } else if (emissionRate == "so2EmissionRate") {
            pollutantLabelTooltip = "sulfur dioxide";
            return "SO";
          } else if (emissionRate == "noxEmissionRate") {
            pollutantLabelTooltip = "nitrogen oxides";
            return "NO";
          }
        })
        .append("tspan")
        .attr("baseline-shift", "sub")
        .text(function() {
          if (emissionRate == "co2EmissionRate") {
            return "2";
          } else if (emissionRate == "so2EmissionRate") {
            return "2";
          } else if (emissionRate == "noxEmissionRate") {
            return "x";
          }
        });

      var defs = this.svgGradient.append("defs");

      var linearGradient = defs
        .append("linearGradient")
        .attr("class", "legend")
        .attr("id", "linear-gradient");

      if (this.orientation == "horizontal") {
        linearGradient
          .attr("x1", "0%")
          .attr("y1", "100%")
          .attr("x2", "0%")
          .attr("y2", "0%");

        linearGradient
          .append("stop")
          .attr("offset", "0%")
          .attr("stop-color", "#eeeeee");
        //Set the color for the end (100%)
        linearGradient
          .append("stop")
          .attr("offset", "100%")
          .attr("stop-color", _this.$parent.emRatesColors[emissionRate]);

        var titleOffset = (_this.containerHeight * 1) / 5;

        this.svgGradient
          .append("rect")
          .attr("width", 30)
          .attr("height", _this.containerHeight * 0.6)
          .attr("transform", "translate(20," + titleOffset + ")")
          .attr("stroke", "black")
          .style("fill", "url(#linear-gradient)");

        this.svgGradient
          .append("text")
          .attr("x", 20)
          .attr("y", 50)
          .text("(lbs/MWh)");

        // Create tick marks
        var xLeg = d3.scale
          .linear()
          .domain(color.domain())
          .range([_this.containerHeight * 0.6, 0]);

        var axisLeg = d3.svg
          .axis()
          .scale(xLeg)
          .orient("right")
          .tickFormat(function(d) {
            if (emissionRate !== "co2EmissionRate") {
              return d3.format(".2n")(d);
            } else {
              if (d == 0) {
                return d;
              } else {
                return d3.format(",.2r")(d);
              }
            }
          });

        if (max == 0) {
          svgGradient.attr("display", "none");
        }

        this.svgGradient
          .attr("class", "axis gradient grid-col")
          .append("g")
          .attr("transform", "translate(50, " + titleOffset + ")")
          .call(axisLeg);

        d3.selectAll("#emissionRatesHeatMap .tick line").attr("x1", "-30");
        d3.selectAll("#emissionRatesHeatMap .tick line").attr("x2", "0");
      } else if (this.orientation == "vertical") {
        linearGradient
          .attr("x1", "0%")
          .attr("y1", "0%")
          .attr("x2", "100%")
          .attr("y2", "0%");

        linearGradient
          .append("stop")
          .attr("offset", "0%")
          .attr("stop-color", "#eeeeee");
        //Set the color for the end (100%)
        linearGradient
          .append("stop")
          .attr("offset", "100%")
          .attr("stop-color", _this.$parent.emRatesColors[emissionRate]);

        var titleOffset = (_this.containerHeight * 1) / 5 + 20;

        this.svgGradient
          .append("rect")
          .attr("width", 370)
          .attr("height", _this.containerHeight / 6)
          .attr("transform", "translate(0," + titleOffset + ")")
          .attr("stroke", "black")
          .style("fill", "url(#linear-gradient)");

        this.svgGradient
          .append("text")
          .attr("x", 50)
          .attr("y", 20)
          .text("(lbs/MWh)");

        // Create tick marks
        var xLeg = d3.scale
          .linear()
          .domain(color.domain())
          .range([0, 370]);

        var axisLeg = d3.svg
          .axis()
          .scale(xLeg)
          .orient("bottom")
          .tickFormat(function(d) {
            if (emissionRate !== "co2EmissionRate") {
              return d3.format(".2n")(d);
            } else {
              if (d == 0) {
                return d;
              } else {
                return d3.format(",.2r")(d);
              }
            }
          });

        if (max == 0) {
          svgGradient.attr("display", "none");
        }

        this.svgGradient
          .attr("class", "axis gradient")
          .append("g")
          .attr("transform", "translate(20, " + (titleOffset + 20) + ")")
          .call(axisLeg);

        d3.selectAll("#emissionRatesHeatMap .tick line")
          .attr("y1", "-20")
          .attr("y2", "5");
      }

      var container = svg
        .selectAll("g")
        .data(_this.subregionData)
        .enter()
        .append("g")
        .attr("class", "emissionRateMapTooltip")
        .attr("title", function(d) {
          return _this.$t("tooltip.text", {
            subregionName: d.properties.fullName,
            pollutant: pollutantLabelTooltip,
            rate: d.properties.emissionFactor[emissionRate].display
          });
        });

      container
        .append("path")
        .attr("class", function(d) {
          if (d.properties.hasOwnProperty("STATE")) {
            return "state";
          } else {
            return "heatmap " + "name" + d.properties.name;
          }
        })
        .attr("d", _this.path)
        .style("stroke", function(d) {
          if (d.properties.hasOwnProperty("STATE")) {
            return "#a9a9a9";
          } else {
            return "#2B2B2B";
          }
        })
        .style("stroke-width", "1")
        .style("fill", function(d) {
          // Get data value
          var value = d.properties.emissionFactor[emissionRate].value;
          if (value) {
            //If value exists…
            return color(value);
          } else {
            //If value is undefined…
            return "rgb(213,222,217)";
          }
        });
      var labels = svg.append("g");
      addSubregionLabels(labels, this.path, this.subregionData);

      if (orientation == "horizontal") {
        addLogoBottom(this.svgGradient, 30, _this.containerHeight - 30);
      } else if (orientation == "vertical") {
        addLogoBottom(this.svgGradient, 30, _this.containerHeight);
      }
      addTooltip(".emissionRateMapTooltip");
    }
  },
  watch: {
    "$root.$i18n.locale": {
      deep: true,
      handler() {
        this.clear();
        this.initialize(600, 300, "#emissionRatesHeatMap");
        this.createProjection();
        this.display(this.$parent.selectedPollutantAll, this.orientation);
      }
    }
  }
};
</script>
