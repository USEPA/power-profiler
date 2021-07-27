<i18n>
{
  "en": {
    "header": "Annual Results",
    "avgEstimateParagraph": "Using the eGRID subregion {eGRIDAcronym} ({eGRIDName}) emission rates and {pctLineLoss}% percent line loss, your estimated annual use of {estAnnUse} of electricity results in {lbsCO2} pounds {CO2}, {lbsSO2} pounds {SO2}, and {lbsNOX} pounds {NOX} emitted in one year from the power plants in your area.",
    "seedlingParagraph": "It would take {numSeedlings} tree seedlings grown for 10 years or {numAcres} acres of forests in one year to offset those {CO2} emissions. {energyAndEnviroSite} can show you how to take steps to reduce your environmental impact, such as becoming more energy efficient or switching to cleaner energy sources.",
    "energyAndEnviroSite": "EPA's Energy and the Environment site",
    "reductionParagraph": "To find out more about what a reduction in your electricity use means in everyday terms, like miles driven, visit {GHGCalc}. For basic information about GHG emissions, visit {GHGSite}.",
    "GHGCalc": "EPA's Greenhouse Gas Equivalencies Calculator",
    "GHGSite": "EPA's Greenhouse Gas Emissions site",
    "nationalAvgParagraph": "This is an estimate of the pounds of air pollutants caused by the electricity you use in your home or business during one year. Your annual emissions are {estimate} and the eGRID subregion {eGRIDAcronym} ({eGRIDName}) emission rates and include a grid region specific adjustment for line losses of {natPctLineLoss} percent.",
    "commercialEstimate": "estimated from the national average electricity consumption of 1.22 kWh/sq. ft./month for commercial customers",
    "homeEstimate": "estimated from the average home consumption of 877 kWh/month",
    "commercialCustText": "Estimate annual emissions for commercial customers {hereLink}.",
    "hereLink": "here",
    "commercialCustForm": "Enter your square footage:",
    "commercialCustButton": "Go",
    "switchToResButton": "Switch to residential",
    "printReport": "Print Report"
  },

  "es": {
    "header": "Resultados anuales",
    "avgEstimateParagraph":"Usando las tasas de emisión del {eGRIDAcronym} ({eGRIDName}) para la subregión de eGRID y un {pctLineLoss}% porcentaje de pérdidas de energía en los cables de, su consumo anual estimado de {estAnnUse} de electricidad produce emisiones de {lbsCO2} libras de {CO2}, {lbsSO2} libras de {SO2}, y {lbsNOX} libras de {NOX} en un año desde las centrales eléctricas de su área.",
    "seedlingParagraph": "Se requerirían {numSeedlings} plántulas crecidas durante 10 años o {numAcres} acres de bosques crecidos en un año para compensar esas emisiones de CO2. {energyAndEnviroSite} puede mostrarle qué medidas tomar para reducir su impacto ambiental, por ejemplo, cómo ahorrar energía o cómo adoptar fuentes de energía más limpias.",
    "energyAndEnviroSite": "El sitio de Energía y Medio Ambiente de la EPA",
    "reductionParagraph": "Para obtener más detalles sobre lo que implica reducir el consumo de electricidad en su vida diaria, por ejemplo, millas manejadas, {GHGCalc}, y para obtener información básica sobre las emisiones de los gases de efecto invernadero, visite {GHGSite}.",
    "GHGCalc": "visite la Calculadora de equivalencias de gases de efecto invernadero de la EPA,",
    "GHGSite": "el sitio de Emisiones de gases de efecto invernadero de la EPA",
    "nationalAvgParagraph": "Es una estimación de la cantidad de libras de contaminantes del aire causadas por la electricidad que usted consume en su hogar o empresa durante un año. Sus emisiones anuales se calculan en función {estimate} y de las tasas de emisión del {eGRIDAcronym} ({eGRIDName}) para la subregión de eGRID e incluyen un ajuste de {natPctLineLoss} por pérdidas de energía en los cables específico para la región de la red eléctrica.",
    "commercialEstimate": "estimado del consumo promedio nacional de electricidad de 1.22 kWh/sq. ft/mes para clientes comerciales",
    "homeEstimate": "estimado del consumo promedio de viviendas de 877 kWh/mes",
    "commercialCustText": "Calcule las emisiones anuales para clientes comerciales {hereLink}.",
    "hereLink": "aquí",
    "commercialCustForm": "Ingrese su cantidad de pies cuadrados:",
    "commercialCustButton": "Ir",
    "switchToResButton": "Cambie a consumo residencial",
    "printReport": "Imprima un reporte"
  }
}
</i18n>
<template>
  <div id="result" class="flex-align-stretch">
    <h3>{{ $t("header") }}</h3>
    <h4 id="result-subheader">Result Subheader</h4>
    <div id="emissionsDescription">
      <div id="annual-results-text">
        <i18n path="avgEstimateParagraph" tag="p">
          <template #eGRIDAcronym>
            <strong><span id="egrid-subregion-acronym"></span></strong>
          </template>
          <template #eGRIDName>
            <strong><span id="egrid-subregion-name"></span></strong>
          </template>
          <template #pctLineLoss>
            <strong><span id="percent-line-loss"></span></strong>
          </template>
          <template #estAnnUse>
            <strong
              ><span id="estimated-annual-electricity-use"></span> kWh</strong
            >
          </template>
          <template #lbsCO2>
            <strong><span id="pounds-of-co2"></span> </strong>
          </template>
          <template #CO2>
            <strong>CO<sub>2</sub></strong></template
          >
          <template #lbsSO2>
            <strong><span id="pounds-of-so2"></span> </strong>
          </template>
          <template #SO2>
            <strong>SO<sub>2</sub></strong></template
          >
        </i18n>
      </div>
      <div id="national-avg-annual-results-text">
        <i18n path="nationalAvgParagraph" tag="p">
          <template #estimate>
            <span v-if="userSelectionStore.getResidentialMode()">{{
              $t("homeEstimate")
            }}</span>
            <span v-else>{{ $t("commercialEstimate") }}</span>
          </template>
          <template #eGRIDAcronym>
            <strong><span id="nat-egrid-subregion-acronym"></span></strong>
          </template>
          <template #eGRIDName>
            <strong><span id="nat-egrid-subregion-name"></span></strong>
          </template>
          <template #natPctLineLoss>
            <strong><span id="nat-percent-line-loss"></span></strong>
          </template>
        </i18n>
        <span id="customerText">
          <i18n path="commercialCustText" tag="p">
            <template #hereLink>
              <a href="javascript:void(0)" id="commercialCustomersLink">{{
                $t("hereLink")
              }}</a>
            </template>
          </i18n>
        </span>

        <form id="commercialCustomersForm" method="POST">
          <label for="squareFootage" class="usa-label">{{ $t("commercialCustForm") }}</label>
          <input
            class="usa-input"
            id="squareFootage"
            max="99999"
            required=""
            type="number"
          />&nbsp;
          <button id="commercialCustomersButton" class="usa-button" type="submit">
            {{ $t("commercialCustButton") }}
          </button>
        </form>
        <button id="residentialCustomersButton" class="usa-button" style="display: none">
          {{ $t("switchToResButton") }}
        </button>
      </div>
      <i18n path="seedlingParagraph" tag="p">
        <template #numSeedlings>
          <span id="no-of-tree-seedlings"></span>
        </template>
        <template #numAcres>
          <span id="acres-of-forests"></span>
        </template>
        <template #CO2>
          <span id="em-rpt-offset-4"> CO<sub>2</sub></span>
        </template>
        <template #energyAndEnviroSite>
          <a
            href="/energy/reduce-environmental-impact-your-energy-use"
            target="_blank"
            >{{ $t("energyAndEnviroSite") }}
          </a>
        </template>
      </i18n>
      <i18n path="reductionParagraph" tag="p">
        <template #GHGCalc>
          <a
            href="/energy/greenhouse-gas-equivalencies-calculator"
            target="_blank"
            >{{ $t("GHGCalc") }}</a
          >
        </template>
        <template #GHGSite>
          <a href="/ghgemissions" target="_blank">{{ $t("GHGSite") }}</a>
        </template>
      </i18n>
    </div>
    <div class="box box--special grid-container">
      <div class="grid-row grid-gap flex-wrap flex-justify-center">
        <div id="chart-gauge" class="box__content"></div>
      </div>
      <div class="grid-row grid-gap flex-wrap flex-justify-center">
        <div id="resultGraphs" class="box__content"></div>
      </div>
    </div>
    <div>
      <p>
        <a href="javascript:window.print()"
          >&#128438; {{ $t("printReport") }}</a
        >
      </p>
    </div>
  </div>
</template>
<script>
import { userSelection } from "../stores/userSelection.js";
export default {
  data() {
    return {
      userSelectionStore: userSelection
    };
  }
};
</script>
<style>
#result {
  display: none;
  /* The sum of the sidebar + the main-charts min-widths */
  min-width: 1320px;
  width: 100%;
}
</style>
