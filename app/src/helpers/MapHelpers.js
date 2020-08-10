export { addSubregionLabels }

function addSubregionLabels(svg, path, subregionData) {
    var whiteRect = svg.selectAll(".whiteRect")
        .data(subregionData)
        .enter()
        .append("g")
        .attr("class", function(d){
            if(d.properties.name == 'NYLI' || d.properties.name == 'NYCW' || d.properties.name == 'AKGD'){
                return "smSubregion";
            }
            return "whiteRect"
        });

    whiteRect.append("rect")
        .attr("class",function(d){
            return "subregionWhiteLabel";
        })            
        .attr("x", function(d) {
            if(d.properties.name == 'NYLI'){
                return path.centroid(d)[0] + 15;
            } else if (d.properties.name == 'AKGD') {
                return path.centroid(d)[0] - 10;
            } else if (d.properties.name == 'HIMS') {
                return path.centroid(d)[0] - 50;
            }  else if(d.properties.name == 'NYCW'){
                return path.centroid(d)[0] + 3;
            } else if (d.properties.name == 'SPSO'){
                return path.centroid(d)[0] - 13;
            } else if (d.properties.name == 'SRSO'){
                return path.centroid(d)[0] - 14;
            } else {
                return path.centroid(d)[0] - 20;
            }
        })
        .attr("y", function(d) {
                if(d.properties.name == 'AKGD'){
                    return path.centroid(d)[1] + 25;
                } else if (d.properties.name == 'HIOA') {
                    return path.centroid(d)[1] - 33;
                }else if (d.properties.name == 'AKMS') {
                    return path.centroid(d)[1] - 22;
                }else if (d.properties.name == 'HIMS') {
                    return path.centroid(d)[1];
                } else if(d.properties.name == 'NYLI'){
                    return path.centroid(d)[1] - 15;
                }  else if(d.properties.name == 'NYCW'){
                    return path.centroid(d)[1] + 6;
                } else if (d.properties.name == 'CAMX' || d.properties.name == 'AZNM' || d.properties.name == 'RMPA' || d.properties.name == 'SPNO' || d.properties.name == 'SRVC' || d.properties.name == 'RFCW') {
                    return path.centroid(d)[1] - 10;
                }else if (d.properties.name == 'SPSO'){
                    return path.centroid(d)[1] - 18;
                }else if (d.properties.name == 'SRMV'){
                    return path.centroid(d)[1] - 23;
                }else if (d.properties.name == 'SRSO'){
                    return path.centroid(d)[1] - 10;
                }else {
                    return path.centroid(d)[1] - 12;
                }
        })
        .attr("rx",6)
        .attr("ry",6)
        .attr("width", 33)
        .attr("height", 16)
        .attr("fill","white");

        var akgdCentroid, nyliCentroid, nycwCentroid;

        whiteRect.append("text")
            .attr("class","subregionLabel")
            .attr("fill","black")
            .attr("font-size","0.65em")
            .attr("x",function(d){
                if(d.properties.name == 'NYLI'){
                    return path.centroid(d)[0] + 13;
                } else if (d.properties.name == 'AKGD') {
                    return path.centroid(d)[0] - 10;
                } else if (d.properties.name == 'HIMS') {
                    return path.centroid(d)[0] - 45;
                } else if(d.properties.name == 'NYCW'){
                    return path.centroid(d)[0] + 3;
                } else if (d.properties.name == 'SPSO'){
                    return path.centroid(d)[0] - 10;
                } else if (d.properties.name == 'SRSO'){
                    return path.centroid(d)[0] - 11;
                } else {
                    return path.centroid(d)[0] - 18;
                }
            })
            .attr("y",function(d){
                if(d.properties.name == 'AKGD'){
                    akgdCentroid = path.centroid(d);
                    return path.centroid(d)[1] + 37;
                } else if (d.properties.name == 'AKMS') {
                    return path.centroid(d)[1] - 10;
                } else if (d.properties.name == 'HIOA') {
                    return path.centroid(d)[1] - 15;
                } else if (d.properties.name == 'HIMS') {
                    return path.centroid(d)[1] + 10;
                } else if(d.properties.name == 'NYLI'){
                    nyliCentroid = path.centroid(d);
                    return path.centroid(d)[1] - 3;
                } else if(d.properties.name == 'NYCW'){
                    nycwCentroid = path.centroid(d);
                    return path.centroid(d)[1] + 17;
                } else if (d.properties.name == 'CAMX' || d.properties.name == 'AZNM' || d.properties.name == 'RMPA' || d.properties.name == 'SPNO' || d.properties.name == 'SRVC' || d.properties.name == 'RFCW'){
                    return path.centroid(d)[1] + 2;
                }
                else if (d.properties.name == 'SPSO'){
                    return path.centroid(d)[1] - 6;
                }
                else if (d.properties.name == 'SRMV'){
                    return path.centroid(d)[1] - 11;
                }
                else if (d.properties.name == 'SRSO'){
                    return path.centroid(d)[1] + 1;
                }
                else {
                    return path.centroid(d)[1];
                }
            })
            .text(function(d){
                return d.properties.name;
            });

        svg.selectAll(".smSubregion")
            .append("line")
            .attr("x1",function(d){
                if(d.properties.name == 'AKGD'){
                    return akgdCentroid[0] - 2;
                } else if(d.properties.name == 'NYLI'){
                    return nyliCentroid[0] + 11;
                } else if(d.properties.name == 'NYCW'){
                    return nycwCentroid[0] + 7;
                }
            })
            .attr("x2",function(d){
                if(d.properties.name == 'AKGD'){
                    return akgdCentroid[0] + 7;
                } else if(d.properties.name == 'NYLI'){
                    return nyliCentroid[0] + 16;
                } else if(d.properties.name == 'NYCW'){
                    return nycwCentroid[0] + 3;
                }
            })
            .attr("y1",function(d){
                if(d.properties.name == 'AKGD'){
                    return akgdCentroid[1] + 3;
                } else if(d.properties.name == 'NYLI'){
                    return nyliCentroid[1] - 3;
                } else if(d.properties.name == 'NYCW'){
                    return nycwCentroid[1] + 7;
                }
            })
            .attr("y2",function(d){
                if(d.properties.name == 'AKGD'){
                    return akgdCentroid[1] + 22;
                } else if(d.properties.name == 'NYLI'){
                    return nyliCentroid[1] - 2;
                } else if(d.properties.name == 'NYCW'){
                    return nycwCentroid[1] + 5;
                }
            });
}