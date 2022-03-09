// Add states.json to the eGRID subregions GeoJSON.
var fs = require('fs');
var egrid_file = fs.readFileSync('data/shape/eGRID2020_subregions.json');
var states_file = fs.readFileSync('data/shape/states.json');
var egrid_j = JSON.parse(egrid_file);
var states_j = JSON.parse(states_file);
// Replace "Subregions" with new key: "name."
for(var i = 0; i < egrid_j.features.length; i += 1){
    egrid_j.features[i].properties["name"] = egrid_j.features[i].properties.ZipSubregi;
    delete egrid_j.features[i].properties["ZipSubregi"];
}
// Concat the states feature collection with the subregion feature collection.
states_j.features = states_j.features.concat(egrid_j.features);
fs.writeFile('data/shape/egrid_2020_subregions_states.json', JSON.stringify(states_j), 'utf-8', function(err){
    if(err) console.log(err)
});
