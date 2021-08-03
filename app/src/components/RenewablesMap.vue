<i18n>
{
    "en": {
        "description": {
            "text": "This map provides {eGRIDSubregion} renewable percentages.",
            "eGRIDSubregion": "eGRID subregion"
        },
        "tooltip": {
            "text": "{subregionName} {sourceType} generation: {sourcePct}%"
        }
    },
    "es": {
        "description": {
            "text": "Este mapa proporciona los porcentajes renovables de {eGRIDSubregion}.",
            "eGRIDSubregion": "subregiones de eGRID"
        },
        "tooltip": {
            "text": "Generación {sourceType} de {subregionName}: {sourcePct}%"
        }
    }
}
</i18n>
<template>
  <div>
    <i18n path="description.text" tag="p">
      <template #eGRIDSubregion>
        <a
          href="https://www.epa.gov/sites/default/files/2021-03/2019_egrid_subregions.png"
          target="_blank"
          >{{ $t("description.eGRIDSubregion") }}</a
        >
      </template>
    </i18n>
    <div id="renewablesMap" class="grid-row flex-wrap flex-justify-center flex-align-center"></div>
  </div>
</template>
<script>
import { geoAlbersUsaTerritories } from "geo-albers-usa-territories";
import { addLogoBottom } from "../helpers/ChartHelpers.js";
import { addSubregionLabels } from "../helpers/MapHelpers.js";
import { allSubregions } from "../stores/allSubregions.js";
import { userSelection } from "../stores/userSelection.js";
import { addTooltip } from "../helpers/Tooltip.js";

export default {
  data() {
    return {
      orientation: "",
      width: 600,
      height: 300,
      domElement: "#renewablesMap",
      projection: {},
      path: {},
      containerHeight: 0,
      subregionData: [],
      selectedRenewable: "renewable"
    };
  },
  mounted: function() {
    this.orientation = userSelection.data.emissionRatesOrientation;
    this.subregionData = allSubregions.data;
    this.createProjection();
    this.display(this.selectedRenewable, this.$parent.orientation);
  },
  methods: {
    createProjection: function() {
      this.projection = geoAlbersUsaTerritories()
        .translate([this.width / 2, this.height / 2])
        .scale([this.width + 100]);
      this.path = d3.geo.path().projection(this.projection);
    },
    display: function(dataValue, orientation) {
      var _this = this;
      var percentBins = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100];
      var binColors = [
        "#e6efea",
        "#ccdfd4",
        "#b3d0bf",
        "#99c0a9",
        "#80b094",
        "#67a07f",
        "#4d9069",
        "#348154",
        "#1a713e",
        "#015725"
      ];

      var color = d3.scale.ordinal().domain(percentBins).range(binColors);

      var svg = d3
        .select(this.domElement)
        .append("svg")
        .attr("class", "grid-col-10")
        .attr("width", this.width)
        .attr("height", this.height)
        .attr("viewBox", "0 0 " + this.width + " " + this.height)
        .attr("preserveAspectRatio", "xMidYMid meet")
        .attr("fill", "gainsboro");

      var aspect = this.width / this.height;

      $(window)
        .on("resize", function() {
          var targetWidth = $("#main-charts").width();
          svg.attr("width", targetWidth);
          svg.attr("height", Math.round(targetWidth / aspect));
        })
        .trigger("resize");

      var container = svg
        .selectAll("g")
        .data(this.subregionData)
        .enter()
        .append("g")
        .attr("class", "renewablesMapTooltip")
        .attr("title", function(d) {
          return _this.$t("tooltip.text", {
            subregionName: d.properties.fullName,
            sourceType: dataValue,
            sourcePct: d.properties.fuelMixCategories[dataValue]
          });
        });

      container
        .append("path")
        .attr("class", function(d) {
          if (d.properties.hasOwnProperty("STATE")) {
            return "state";
          } else {
            return "renewablesmap " + "name" + d.properties.name;
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
          var value = d.properties.fuelMixCategories[dataValue];
          if (value) {
            //If value exists…
            var rv = Math.ceil(value / 10) * 10;
            return color(rv);
          } else {
            //If value is undefined…
            return "rgb(213,222,217)";
          }
        });

      var labels = svg.append("g");

      addTooltip(".renewablesMapTooltip");
      if (orientation == "horizontal") {
        var svgLegend = d3
          .select(this.domElement)
          .append("svg")
          .attr("class", "grid-col")
          .attr("width", 150)
          .attr("height", _this.height + 107);

        var legend = svgLegend
          .selectAll(".renewables-legend")
          .data(color.domain())
          .enter()
          .append("g")
          .attr("class", "renewables-legend");

        var sqOffset = -20;
        legend
          .append("rect")
          .attr("x", 0)
          .attr("y", function(d, i) {
            sqOffset += 25;
            return i + sqOffset;
          })
          .attr("width", 15)
          .attr("height", 15)
          .style("fill", color);

        var txtOffset = -5;
        legend
          .append("text")
          .attr("x", 25)
          .attr("y", function(d, i) {
            txtOffset += 25;
            return i + txtOffset;
          })
          .style("fill", "black")
          .text(function(d, i) {
            return color.domain()[i] - 10 + "-" + color.domain()[i] + "%";
          });

        addSubregionLabels(labels, this.path, this.subregionData);
        addLogoBottom(svgLegend, 30, this.height);
      } else {
        var svgLegendV = d3
          .select(this.domElement)
          .append("svg")
          .attr("width", _this.width + 70)
          .attr("height", 40);

        var legendV = svgLegendV
          .selectAll(".renewables-legend")
          .data(color.domain())
          .enter()
          .append("g")
          .attr("class", "renewables-legend");

        var sqOffsetV = -40;
        legendV
          .append("rect")
          .attr("y", 0)
          .attr("x", function(d, i) {
            sqOffsetV += 50;
            return i + sqOffsetV;
          })
          .attr("width", 15)
          .attr("height", 15)
          .style("fill", color);

        var txtOffsetV = -50;
        legendV
          .append("text")
          .attr("y", 40)
          .attr("x", function(d, i) {
            txtOffsetV += 50;
            return i + txtOffsetV;
          })
          .style("fill", "black")
          .text(function(d, i) {
            return color.domain()[i] - 10 + "-" + color.domain()[i] + "%";
          });

        addSubregionLabels(labels, this.path, this.subregionData);
        addLogoBottom(svgLegendV, 30, this.height);
      }
    }
  }
};
</script>
