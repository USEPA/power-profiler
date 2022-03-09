#!/usr/bin/bash

echo "Adding fuel breakdown"
python add_fuel_breakdown.py

echo "Creating the subregion geojson file"
cd data/shape
mapshaper eGRID2020_subregions.shp -simplify 1% -o format=geojson
cd -

echo "Adding the states"
node add_states.js

echo "Adding the eGRID data"
python add_egrid_data.py

echo "Simplify the subregion.json file"
cd result
mapshaper subregion.json -simplify dp 5% -o force format=geojson
cd -

echo "Copy the result to the app/data directory"
cp result/subregion.json ../app/data