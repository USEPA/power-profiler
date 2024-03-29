<template>
  <div>
    <div id="subregionMap"></div>
  </div>
</template>

<script>
import { geoAlbersUsaTerritories } from "geo-albers-usa-territories";
import { env } from "../config/env.js";
import { allSubregions } from "../stores/allSubregions.js";
import { nationalFeature } from "../stores/nationalFeature.js";
import { addTooltip } from "../helpers/Tooltip.js";

export default {
  data() {
    return {
      allData: [],
      nationalFeature: {},
      subregionData: [],
      w: 425,
      h: 255
    };
  },
  beforeCreate: function() {
    var self = this;
    $.ajax({
      url: env.SUBREGION_JSON,
      success: function(json) {
        self.allData = json.features;
        self.nationalFeature = json.features.filter(
          feature => feature.properties.type === "national"
        );
        self.subregionData = json.features.filter(
          feature => feature.properties.type === "subregion"
        );
        allSubregions.update(self.subregionData);
        nationalFeature.update(self.nationalFeature);
        self.$parent.$parent.$parent.subregionJSONLoaded = true;
        self.displayMap("#subregionMap", self.allData);
      }
    });
  },
  methods: {
    displayMap: function(elementID, data) {
      var self = this;
      var projection = geoAlbersUsaTerritories()
        .translate([this.w / 2, this.h / 2])
        .scale([this.w + 100]);
      var path = d3.geo.path().projection(projection);
      var svg = d3
        .select(elementID)
        .append("svg")
        .attr("width", this.w)
        .attr("height", this.h)
        .attr("viewBox", function() {
          return "0 0 " + self.w + " " + self.h;
        })
        .attr("preserveAspectRatio", "xMidYMid meet")
        .attr("fill", "gainsboro");

      var aspect = this.w / this.h;

      $(window)
        .on("resize", function() {
          var targetWidth = $("#subregionMap").width();
          svg.attr("width", targetWidth);
          svg.attr("height", Math.round(targetWidth / aspect));
        })
        .trigger("resize");

      var container = svg
        .selectAll("g")
        .data(data.sort(
          function(a, b) {
            // If it's a subregion, we want it to come after the state paths
            // so the subregions show up on top.
            return a.properties.type === "subregion" ? 1 : -1;
          }
        ))
        .enter()
        .append("g")
        .attr("class", "mapTooltip")
        .attr("title", function(d) {
          if (d.properties.name)
            return d.properties.name + " (" + d.properties.fullName + ")";
        });

      container
        .append("path")
        .attr("class", function(d) {
          return d.properties.hasOwnProperty("STATE")
            ? "state"
            : "map " + d.properties.name;
        })
        .attr("d", path)
        .style("stroke", function(d) {
          return d.properties.hasOwnProperty("STATE") ? "#a9a9a9" : "#2B2B2B";
        })
        .style("stroke-width", "1")
        .on("click", function(d) {
          $("#userLocation").val("");
          $("#utilitySelectDiv").hide();
          self.$root.$emit("subregionSelected", d);
        });

      addTooltip(".mapTooltip");
    }
  }
};
</script>
<style>
.map:hover {
  fill-opacity: 0.7;
  fill: steelblue;
}
.map {
  fill-opacity: 0.5;
}
</style>
