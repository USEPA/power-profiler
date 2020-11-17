<i18n>
{
  "en": {
    "select": "Select"
  },
  "es": {
    "select": "Seleccione"
  }
}
</i18n>

<template>
  <div id="emissionRate">
    <div id="select-offset-2">
      <p class="select-pollutant-label">
        <strong>{{ $t("select") }}</strong>
      </p>
      <div id="pollutantSelectSub">
        <button id="defaultPollutantSub" value="co2EmissionRate">
          CO<sub>2</sub>
        </button>
        <button value="so2EmissionRate">SO<sub>2</sub></button>
        <button value="noxEmissionRate">NO<sub>X</sub></button>
      </div>
    </div>
  </div>
</template>
<script>
import {
  addLogoBottom,
  formatFuelLabel,
  checkNational,
} from "../helpers/ChartHelpers.js";
import { nationalFeature } from "../stores/nationalFeature.js";
import { selectedSubregion } from "../stores/selectedSubregion.js";
import { addTooltip } from "../helpers/Tooltip";

export default {
  data() {
    return {
      data: [],
      selectedPollutantSub: "co2EmissionRate",
    };
  },
  mounted: function () {
    var self = this;
    this.data = [nationalFeature.data[0], selectedSubregion.data];
    this.display(this.data);

    $(window).on("resize", function () {
      d3.selectAll("#emissionRate svg").remove();
      self.update();
    });

    $("#pollutantSelectSub button").on("click", function (e) {
      $(this).css({ "background-color": "#2B7D3B" });
      $(this).siblings().css({ "background-color": "#0071bc" });
      self.selectedPollutantSub = $(this).val();

      $("#sub" + self.selectedPollutantSub).show();
      $("#sub" + self.selectedPollutantSub)
        .siblings("svg")
        .hide();
    });

    $("#defaultPollutantSub").trigger("click");
  },
  methods: {
    display: function (data) {
      var domElement = "#emissionRate";
      var w = $(domElement).width();
      var h = 500 - ($("#select-offset-2").height() - 20);
      var parameters = [
        "so2EmissionRate",
        "co2EmissionRate",
        "noxEmissionRate",
      ];
      var emRatesColors = {
        national: "#2b83ba",
        subregion: "#e66101",
        co2EmissionRate: "#d7191c",
        so2EmissionRate: "#008837",
        noxEmissionRate: "#7b3294",
      };

      for (var i = 0; i < parameters.length; i += 1) {
        var selectedPollutantSub = parameters[i];

        var margin = { top: 65, right: 20, bottom: 80, left: 70 },
          width = w - margin.left - margin.right,
          height = h - margin.top - margin.bottom;

        var x = d3.scale.ordinal().rangeRoundBands([0, width], 0.4);

        var y = d3.scale.linear().rangeRound([height, 1]);

        var color = d3.scale
          .ordinal()
          .range([emRatesColors.national, emRatesColors[selectedPollutantSub]])
          .domain([data[0].properties.name, data[1].properties.name]);

        var xAxis = d3.svg.axis().outerTickSize(0).scale(x).orient("bottom");

        var yAxis = d3.svg.axis().outerTickSize(0).scale(y).orient("left");

        var svg = d3
          .select(domElement)
          .append("svg")
          .attr("id", "sub" + selectedPollutantSub)
          .attr("width", width + margin.left + margin.right)
          .attr("height", height + margin.top + margin.bottom)
          .append("g")
          .attr(
            "transform",
            "translate(" + margin.left + "," + margin.top + ")"
          );

        x.domain(
          data.map(function (d) {
            return d.properties.name;
          })
        );
        y.domain([
          0,
          d3.max(data, function (d) {
            return d.properties.emissionFactor[selectedPollutantSub].value;
          }),
        ]);

        svg
          .append("g")
          .attr("class", "x axis")
          .attr("transform", "translate(0," + height + ")")
          .call(xAxis);

        svg.append("g").attr("class", "y axis").call(yAxis);

        var pollutantLabelTooltip = "";
        svg
          .append("text")
          .attr("y", -30)
          .attr("dy", "0.71em")
          .attr("text-anchor", "end")
          .append("tspan")
          .text(function (d) {
            if (selectedPollutantSub == "co2EmissionRate") {
              pollutantLabelTooltip = "carbon dioxide";
              return "CO";
            } else if (selectedPollutantSub == "so2EmissionRate") {
              pollutantLabelTooltip = "sulfur dioxide";
              return "SO";
            } else if (selectedPollutantSub == "noxEmissionRate") {
              pollutantLabelTooltip = "nitrogen oxides";
              return "NO";
            }
          })
          .append("tspan")
          .attr("baseline-shift", "-.25em")
          .attr("font-size", "76.4706%")
          .text(function (d) {
            if (selectedPollutantSub == "co2EmissionRate") {
              return "2";
            } else if (selectedPollutantSub == "so2EmissionRate") {
              return "2";
            } else if (selectedPollutantSub == "noxEmissionRate") {
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
          .data(data)
          .enter()
          .append("g")
          .attr("class", "subEmissionRateTooltip")
          .attr("title", function (d) {
            return (
              "Average " +
              pollutantLabelTooltip +
              " rate: " +
              d.properties.emissionFactor[parameters[i]].display +
              " lbs/MWh"
            );
          });

        container
          .append("rect")
          .attr("class", "bar subregionEmissionRate " + parameters[i])
          .attr("fill", function (d) {
            return color(d.properties.name);
          })
          .attr("x", function (d) {
            return x(d.properties.name);
          })
          .attr("y", function (d) {
            return y(d.properties.emissionFactor[selectedPollutantSub].value);
          })
          .attr("width", x.rangeBand())
          .attr("height", function (d) {
            return (
              height -
              y(d.properties.emissionFactor[selectedPollutantSub].value)
            );
          });

        svg
          .selectAll("text.bar")
          .data(data)
          .enter()
          .append("text")
          .attr("text-anchor", "middle")
          .attr("x", function (d) {
            return x(d.properties.name) + x.rangeBand() / 2;
          })
          .attr("y", function (d) {
            return (
              y(d.properties.emissionFactor[selectedPollutantSub].value) + -10
            );
          })
          .text(function (d) {
            return d.properties.emissionFactor[selectedPollutantSub].display;
          });

        var baseline = (height + margin.top + margin.bottom) * 0.17;
        addLogoBottom(svg, width - 100, height + baseline);
      }
      addTooltip(".subEmissionRateTooltip");
    },
    update: function () {
      var self = this;
      this.data = [nationalFeature.data[0], selectedSubregion.data];
      d3.selectAll("#emissionRate svg").remove();
      this.display(this.data);
      $("#pollutantSelectSub button").each(function () {
        if ($(this)[0].value == self.selectedPollutantSub)
          $(this).trigger("click");
      });
    },
  },
};
</script>

