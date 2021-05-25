export { addLogoBottom, textWrap }
import { env } from "../config/env.js"

function addLogoBottom(svg, width, height){
    var a = svg.append("svg:a")
        .attr("xlink:href","https://www.epa.gov/energy/emissions-generation-resource-integrated-database-egrid");

        a.append("title").text("eGRID Home Page");

    return a.append("svg:image")
                .attr("x", width + 10)
                .attr("y", height - 25)
                .attr("image-rendering","optimizeQuality")
                .attr("width", 60)
                .attr("height", 30)
                .attr("xlink:href", env.EGRID_LOGO);
}

function textWrap(text, width, startHeight) {
      text.each(function () {
        let txt = d3.select(this),
          words = txt.text().split(/\s+/).reverse(),
          word,
          line = [],
          lineNumber = 0,
          lineHeight = 1.1, // ems
          x = txt.attr("x"),
          y = txt.attr("y"),
          dy = 0, //parseFloat(text.attr("dy")),
          tspan = txt
            .text(null)
            .append("tspan")
            .attr("x", 0)
            .attr("y", 0)
            .attr("dy", dy + "em");
        while ((word = words.pop())) {
          line.push(word);
          tspan.text(line.join(" "));
          if (tspan.text().length > width) {
            line.pop();
            tspan.text(line.join(" ") + " ");
            line = [word];
            tspan = txt
              .append("tspan")
              .attr("x", 0)
              .attr("y", 0)
              .attr("dy", ++lineNumber * lineHeight + dy + "em")
              .text(word);
          }
        }
        let cur_y = -startHeight;
        let new_y = cur_y - 12 * (lineNumber + 1);
        let adjust = txt.attr("transform", "translate(0," + new_y + ")");
      });
    }
