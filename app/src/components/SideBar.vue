<i18n>
{
  "en": {
    "intro": "Electricity is produced by many different sources of energy, including, but not limited to, wind, solar, nuclear, and fossil fuels. The type and amount of emissions produced depend on how electricity is generated in your region. Type in your zip code (or select a region) to view your power profile.",
    "subTitle": "How clean is the electricity you use?",
    "moreInfoLink": "More Information",
    "ariaLabels": {
      "opensNewWin": "Opens new window",
      "downloadsTool": "Downloads Excel spreadsheet tool",
      "downloadsSummary": "Downloads Excel spreadsheet summary tables",
      "downloadsHistorical": "Downloads Excel spreadsheet historical zip codes"
    },
    "additionalInfo": {
      "title": "Additional Information",
      "egridLink":"Emissions & Generation Resource Integrated Database (eGRID)",
      "egridDataSource": "Data source: 2023 data from the {0} released June 12, 2025",
      "powerProfilerExcelLink": "Power Profiler Emissions Tool 2023 (XLSX)",
      "powerProfilerExcelVersion": "Excel version: {0}",
      "historicalZipCodes": "Historical Zip Codes (XLSX)",
      "mailingList": "Sign up for the mailing list",
      "methodology": "Power Profiler Methodology",
      "summaryTables": "eGRID Summary Tables (XLSX)",
      "github": "View and contribute on GitHub",
      "resources": "Additional Resources"
    }
  },
  "es": {
    "intro": "La electricidad es generada por diversas fuentes de energía, entre ellas, la energía eólica, la energía solar, la energía nuclear y los combustibles fósiles. El tipo y la cantidad de emisiones producidas dependerán de cómo se genere la electricidad en su región. Escriba su código postal (o seleccione una región) para ver su perfil de energía.",
    "subTitle": "¿Qué tan limpia es la electricidad que consume?",
    "moreInfoLink": "Más Información",
    "ariaLabels": {
      "opensNewWin": "abre una nueva ventana",
      "downloadsTool": "descarga la herramienta de hoja de cálculo de Excel",
      "downloadsSummary": "descarga las tablas de resumen de la hoja de cálculo de Excel",
      "downloadsHistorical": "descarga los códigos postales históricos de la hoja de cálculo de Excel"
    },
    "additionalInfo": {
      "title": "Información Adicional",
      "egridLink": "Emissions & Generation Resource Integrated Database (eGRID)",
      "egridDataSource": "Fuente de datos: Datos de 2023 del {0} actualizado el 06/12/2025",
      "powerProfilerExcelLink": "Herramienta de Emisiones del Analizador de consumo de energía 2023 (XLSX)",
      "powerProfilerExcelVersion": "Herramienta de Excel: {0}",
      "historicalZipCodes": "Códigos postales históricos (XLSX)",
      "mailingList": "Suscríbase a la lista de distribución",
      "methodology": "Metodología del Analizador de consumo de energía",
      "summaryTables": "Tablas de resumen de eGRID (XLSX)",
      "github": "Ver y contribuir en GitHub",
      "resources": "Recursos adicionales"
    }
  }
}
</i18n>
<template>
  <div>
    <div>
      <p id="intro">
        {{ $t("intro") }}
        <a
          class="more-link"
          href="javascript:void(0)"
          @click="$parent.showMoreInfo = true"
          >{{ $t("moreInfoLink") }}</a
        >
      </p>
    </div>
    <subregionSelection></subregionSelection>
    <div class="box multi related-info" id="info">
      <h3 class="box__title">{{ $t("additionalInfo.title") }}</h3>
      <div class="box__content">
        <i18n
          path="additionalInfo.egridDataSource"
          tag="p"
          for="additionalInfo.egridLink"
        >
          <a
            href="https://www.epa.gov/egrid"
            target="_blank"
            v-bind:aria-label="$t('ariaLabels.opensNewWin')"
            >{{ $t("additionalInfo.egridLink") }}</a
          >
        </i18n>

        <i18n
          path="additionalInfo.powerProfilerExcelVersion"
          tag="p"
          for="additionalInfo.powerProfilerExcelLink"
        >
          <a
            :href=powerProfilerExcel
            v-bind:aria-label="$t('ariaLabels.downloadsTool')"
            >{{ $t("additionalInfo.powerProfilerExcelLink") }}</a
          >
          <span class="fileinfo">(3.0M)</span>
        </i18n>
        <p>
          <a
            href="https://www.epa.gov/system/files/documents/2023-05/Power%20Profiler%20Historical%20Zip%20Codes.xlsx"
            v-bind:aria-label="$t('ariaLabels.downloadsHistorical')"
            >{{ $t("additionalInfo.historicalZipCodes") }}</a
          >
        </p>
        <p>
          <a
            href="https://lp.constantcontactpages.com/su/sG18AaT"
            target="_blank"
            v-bind:aria-label="$t('ariaLabels.opensNewWin')"
            >{{ $t("additionalInfo.mailingList") }}</a
          >
        </p>
        <p>
          <a
            href="https://www.epa.gov/egrid/power-profiler-methodology"
            target="_blank"
            v-bind:aria-label="$t('ariaLabels.opensNewWin')"
            >{{ $t("additionalInfo.methodology") }}</a
          >
        </p>
        <p>
          <a
            :href=egridSummaryTables
            v-bind:aria-label="$t('ariaLabels.downloadsSummary')"
            >{{ $t("additionalInfo.summaryTables") }}</a
          >
          <span class="fileinfo">(1 pg, 885 K)</span>
        </p>
        <p>
          <a
            href="https://github.com/USEPA/power-profiler"
            target="_blank"
            v-bind:aria-label="$t('ariaLabels.opensNewWin')"
            >{{ $t("additionalInfo.github")  }}</a>
        </p>
        <p>
          <a href="javascript:void(0)" @click="$parent.showResources = true">{{
            $t("additionalInfo.resources")
          }}</a>
        </p>
      </div>
    </div>
  </div>
</template>
<script>
import subregionSelection from "./SubregionSelection.vue";
import { constVal } from "../helpers/const.js";

export default {
  data() {
    return {
      egridSummaryTables: constVal.egridSummaryTablesUrl,
      powerProfilerExcel: constVal.powerProfilerExcelUrl,
    }
  },
  components: {
    subregionSelection: subregionSelection
  }
};
</script>
<style>
#intro, #info {
  padding: 1.3529em 1em;
}
</style>
