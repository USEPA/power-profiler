export { addLogoBottom, formatFuelLabel, checkNational };
import { env } from "../config/env.js";

function addLogoBottom(svg, width, height) {
  var a = svg.append("svg:a").attr("xlink:href", "https://www.epa.gov/egrid");

  a.append("title").text("eGRID Home Page");

  return a
    .append("svg:image")
    .attr("x", width + 10)
    .attr("y", height - 25)
    .attr("image-rendering", "optimizeQuality")
    .attr("width", 60)
    .attr("height", 30)
    .attr("xlink:href", env.EGRID_LOGO);
}

function formatFuelLabel(d) {
  var text = d;
  var res = text.replace(/([A-Z])/g, " $1");
  var finalResult = res.charAt(0).toUpperCase() + res.slice(1);
  return finalResult;
}
function checkNational(d) {
  return d == "National" ? "nationally" : "for " + d;
}
