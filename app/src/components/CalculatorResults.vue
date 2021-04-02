<template>
<div id="result">
    <h3>Annual Results</h3>
    <h4 id="result-subheader">Result Subheader</h4>
    <div id="emissionsDescription">
        <div id="annual-results-text">
            <p>Using the eGRID subregion <strong><span id="egrid-subregion-acronym"></span></strong> (<strong><span id="egrid-subregion-name"></span></strong>) emission rates and <strong><span id="percent-line-loss"></span></strong> percent line loss, your estimated annual use of <strong><span id="estimated-annual-electricity-use"></span> kWh</strong> of electricity results in <strong><span id="pounds-of-co2"></span> pounds CO<sub>2</sub></strong>, <strong><span id="pounds-of-so2"></span> pounds SO<sub>2</sub></strong>, and <strong><span id="pounds-of-nox"></span> pounds NO<sub>X</sub></strong> emitted in one year from the power plants in your area.</p>
            <p><span id="em-rpt-offset-1">It would take</span> <span id="result-text-bold-1"><span id="no-of-tree-seedlings"></span> <span id="em-rpt-offset-2">seedlings grown for 10 years or</span> <span id="acres-of-forests"></span> <span id="em-rpt-offset-3">acres of forests in one year</span></span> <span id="em-rpt-offset-4">to offset those CO<sub>2</sub> emissions.</span> <a href="/energy/reduce-environmental-impact-your-energy-use" target="_blank">EPA's Energy and the Environment site</a> can show you how to take steps to reduce your environmental impact, such as becoming more energy efficient or switching to cleaner energy sources.</p>
            <p>To find out more about what a reduction in your electricity use means in everyday terms, like miles driven, visit <a href="/energy/greenhouse-gas-equivalencies-calculator" target="_blank">EPA's Greenhouse Gas Equivalencies Calculator</a>. For basic information about GHG emissions, visit <a href="/ghgemissions" target="_blank">EPA's Greenhouse Gas Emissions site</a>.</p>
        </div>
        <div id="national-avg-annual-results-text">
            <p><span id="nat-em-rpt-intro-1">This is an estimate of the pounds of air pollutants caused by the electricity you use in your home or business during one year. Your annual emissions are</span> <span id="nat-em-rpt-intro-2">estimated from the average home consumption of 877 kWh/month and</span> the eGRID subregion <strong><span id="nat-egrid-subregion-acronym"></span></strong> (<strong><span id="nat-egrid-subregion-name"></span></strong>) <span id="nat-em-rpt-intro-3">emission rates and include a grid region specific adjustment for line losses of <strong><span id="nat-percent-line-loss"></span></strong> percent.</span> <span id="customerText">Estimate annual emissions for commercial customers <a href="javascript:void(0)" id="commercialCustomersLink">here</a>.</span></p>
            <form id="commercialCustomersForm" method="POST"><label for="squareFootage">Enter your square footage:</label>
            <input id="squareFootage" max="99999" required="" type="number">&nbsp;
            <button id="commercialCustomersButton" type="submit">Go</button>
            </form>
            <button id="residentialCustomersButton" style="display: none;">Switch to residential</button>
            <p><span id="nat-em-rpt-offset-1">It would take</span> <span id="result-text-bold-2"><span id="nat-no-of-tree-seedlings"></span> <span id="nat-em-rpt-offset-2">tree seedlings grown for 10 years or</span> <span id="nat-acres-of-forests"></span> <span id="nat-em-rpt-offset-3">acres of forests in one year</span></span> <span id="nat-em-rpt-offset-4">to offset those CO<sub>2</sub> emissions.</span> <a href="/energy/reduce-environmental-impact-your-energy-use" target="_blank">EPA's Energy and the Environment site</a> can show you how to take steps to reduce your environmental impact, such as becoming more energy efficient or switching to cleaner energy sources.</p>
            <p>To find out more about what a reduction in your electricity use means in everyday terms, like miles driven, visit <a href="/energy/greenhouse-gas-equivalencies-calculator" target="_blank">EPA's Greenhouse Gas Equivalencies Calculator</a>. For basic information about GHG emissions, visit <a href="/ghgemissions" target="_blank">EPA's Greenhouse Gas Emissions site</a>.</p>
        </div>
    </div>
    <div class="box special grid-container">
        <div class="grid-row grid-gap">
            <div id="chart-gauge" class="pane-content"></div>
        </div>
        <div class="grid-row grid-gap">
            <div id="resultGraphs" class="pane-content"></div>
        </div>
    </div>
    <div>
        <p><a href="javascript:window.print()">&#128438; Print Report</a></p>
    </div>
</div>
</template>
<style>
#result {
    display: none;
}
</style>
