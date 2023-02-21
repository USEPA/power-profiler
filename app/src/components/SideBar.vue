<i18n>
{
  "en": {
    "intro": "Electricity is produced by many different sources of energy, including, but not limited to, wind, solar, nuclear, and fossil fuels. The type and amount of emissions produced depend on how electricity is generated in your region. Type in your zip code (or select a region) to view your power profile.",
    "subTitle": "How clean is the electricity you use?",
    "moreInfoLink": "More Information",
    "ariaLabels": {
      "opensNewWin": "Opens new window",
      "downloadsTool": "Downloads Excel spreadsheet tool",
      "downloadsSummary": "Downloads Excel spreadsheet summary tables"
    },
    "additionalInfo": {
      "title": "Additional Information",
      "feedback": "How do you like the new Power Profiler site?",
      "egridLink":"Emissions & Generation Resource Integrated Database (eGRID)",
      "egridDataSource": "Data source: 2021 data from the {0} released January 30, 2023",
      "powerProfilerExcelLink": "Power Profiler Emissions Tool 2021 (XLSX)",
      "powerProfilerExcelVersion": "Excel version: {0}",
      "mailingList": "Sign up for the mailing list",
      "methodology": "Power Profiler Methodology",
      "summaryTables": "eGRID Summary Tables (XLSX)",
      "resources": "Additional Resources"
    }
  },
  "es": {
    "intro": "La electricidad es generada por diversas fuentes de energía, entre ellas, la energía eólica, la energía solar, la energía nuclear y los combustibles fósiles. El tipo y la cantidad de emisiones producidas dependerán de cómo se genere la electricidad en su región. Escriba su código postal (o seleccione una región) para ver su perfil de energía.",
    "subTitle": "¿Qué tan limpia es la electricidad que consume?",
    "moreInfoLink": "Más Información",
    "ariaLabels": {
      "opensNewWin": "abre una nueva ventana",
      "downloadsTool": "Downloads Excel spreadsheet tool",
      "downloadsSummary": "Downloads Excel spreadsheet summary tables"
    },
    "additionalInfo": {
      "title": "Información Adicional",
      "feedback": "¿Qué le parece el nuevo sitio del Analizador de consumo de energía?",
      "egridLink": "Emissions & Generation Resource Integrated Database (eGRID)",
      "egridDataSource": "Fuente de datos: Datos de 2020 del {0} actualizado el 01/27/2022",
      "powerProfilerExcelLink": "Herramienta de Emisiones del Analizador de consumo de energía 2020 (XLSX)",
      "powerProfilerExcelVersion": "Herramienta de Excel: {0}",
      "mailingList": "Suscríbase a la lista de distribución",
      "methodology": "Metodología del Analizador de consumo de energía",
      "summaryTables": "Tablas de resumen de eGRID (XLSX)",
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
        <p>
          <strong>
            <a
              href="https://www.epa.gov/egrid/forms/feedback"
              target="_blank"
              v-bind:aria-label="$t('ariaLabels.opensNewWin')"
              >{{ $t("additionalInfo.feedback") }}</a
            >
          </strong>
        </p>

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
          <span class="fileinfo">(3.56M)</span>
        </i18n>
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
#intro {
  padding: 1.3529em 1em;
}
</style>
