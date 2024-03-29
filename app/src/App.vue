<i18n>
{
  "en": {
    "title": "Power Profiler",
    "subTitle": "How clean is the electricity you use?"
  },
  "es": {
    "title": "Analizador de consumo de energía",
    "subTitle": "¿Qué tan limpia es la electricidad que consume?",
    "linkLangNote": "Nota: La mayoría de los enlaces en estas páginas le llevarán a páginas web en inglés"
  }
}
</i18n>

<template>
  <div>
    <div class="locale-changer">
      <a v-on:click="toggleLang" href="javascript:void(0)">{{ langLink }}</a>
    </div>
    <p v-if="$root.$i18n.locale !== 'en'">{{ $t("linkLangNote") }}</p>
    <h3>{{ $t("subTitle") }}</h3>

    <div id="app">
      <div id="app-content" class="display-flex flex-row flex-no-wrap">
        <sideBar id="sidebar" ></sideBar>
        <div v-if="subregionJSONLoaded" id="main-charts" class="grid-col-8">
          <mainCharts v-show="showMain"></mainCharts>
          <router-view v-show="!showMain"></router-view>
        </div>
      </div>
      <moreInfoModal
        v-if="showMoreInfo"
        @close="showMoreInfo = false"
      ></moreInfoModal>
      <resourcesModal
        v-if="showResources"
        @close="showResources = false"
      ></resourcesModal>
      <subregionsModal
        v-if="showSubregionInfo"
        @close="showSubregionInfo = false"
      ></subregionsModal>
      <megawattModal
        v-if="showMegaWattInfo"
        @close="showMegaWattInfo = false"
      ></megawattModal>
    </div>
    <appDescription v-show="showReport || showMainReport"></appDescription>
    <printReport v-if="subregionSelected" v-show="showReport"></printReport>
    <mainPrintReport v-show="showMainReport"></mainPrintReport>
    <calculatorResults></calculatorResults>
  </div>
</template>
<script>
import sideBar from "./components/SideBar.vue";
import moreInfoModal from "./components/modals/MoreInfoModal.vue";
import resourcesModal from "./components/modals/ResourcesModal.vue";
import subregionsModal from "./components/modals/SubregionsModal.vue";
import megawattModal from "./components/modals/MegawattModal.vue";
import mainCharts from "./components/MainCharts.vue";
import subregionCharts from "./components/SubregionCharts.vue";
import calculatorResults from "./components/CalculatorResults.vue";
import printReport from "./components/PrintReport.vue";
import mainPrintReport from "./components/MainPrintReport.vue";
import AppDescription from "./components/AppDescription.vue";
import { userSelection } from "./stores/userSelection.js";

export default {
  components: {
    sideBar: sideBar,
    moreInfoModal: moreInfoModal,
    resourcesModal: resourcesModal,
    subregionsModal: subregionsModal,
    megawattModal: megawattModal,
    mainCharts: mainCharts,
    subregionCharts: subregionCharts,
    calculatorResults: calculatorResults,
    appDescription: AppDescription,
    printReport: printReport,
    mainPrintReport: mainPrintReport
  },
  data() {
    return {
      showMoreInfo: false,
      showResources: false,
      showMegaWattInfo: false,
      showSubregionInfo: false,
      subregionJSONLoaded: false,
      showReport: false,
      subregionSelected: false,
      showResult: false,
      showMain: false,
      showMainReport: false,
      langs: {
        en: "English",
        es: "Español"
      },
      langLink: "Español"
    };
  },
  methods: {
    toggleLang: function() {
      let curLang = this.$root.$i18n.locale;
      let newLang = curLang === "en" ? "es" : "en";
      this.langLink = this.langs[curLang];
      this.$root.$i18n.locale = newLang;

    },
    updateTitle: function() {
      // Necessary becuase of the required title that comes from Drupal
      // which is in English
      $(".page-title").html(this.$t("title"));
    },
  },

  mounted: function() {
    var self = this;
    var emissionRatePollutantId;

    // update the langLink to be English if someone starts with Espanol
    let curLang = this.$root.$i18n.locale;
    let newLang = curLang === "en" ? "es" : "en";
    this.langLink = this.langs[newLang];

    window.addEventListener("beforeprint", function(event) {
      if (self.$route.name == "subregion") {
        $("#print-map").html("");
        $("#print-fuel-mix").html("");
        $("#print-emission-rates").html("");
        var clonedMap = $("#subregionMap > svg")
          .clone()
          .css({ verticalAlign: "top", width: "300px", height: "200px" });
        $("#print-map").append(clonedMap);
        $("#print-fuel-mix").append($("#fuelMixContainer").clone());
        $("#print-fuel-mix svg").css({
          marginTop: "0",
          height: "100%",
          width: "100%"
        });
        $("#print-emission-rates").append("<h3>Emission Rates</h3>");
        $("#print-emission-rates").append($("#emRatesDescription").clone());
        $("#print-emission-rates").append(
          $("#subco2EmissionRate")
            .clone()
            .css({ display: "inline-block", height: "443px" })
        );
        $("#print-emission-rates").append(
          $("#subso2EmissionRate")
            .clone()
            .css({ display: "inline-block", height: "443px" })
        );
        $("#print-emission-rates").append(
          $("#subnoxEmissionRate")
            .clone()
            .css({ display: "inline-block", height: "443px" })
        );
        self.showReport = true;
        $("#printReportMain").hide();
        $("#printReport").show();
      } else {
        $("#print-main-map").html("");
        $("#print-main-fuel-mix").html("");
        $("#print-main-emission-rates").html("");
        $("#print-main-map").append(
          "<h3 style='margin: 5 0 0 0; padding:10;'>eGRID Subregion Map</h3>"
        );
        $("#print-main-map").append(
          $("#subregionMap > svg")
            .clone()
            .css({ width: "296px", height: "178px" })
        );
        $("#print-main-fuel-mix").append($("#nationalFuelMix").clone());
        $("#print-main-fuel-mix #fuelRadios").css({ display: "none" });
        $("#print-main-emission-rates").append(
          "<h3 id='emRatesHeader'>Emission Rates</h3>"
        );
        $("#print-main-emission-rates").append(
          $("#nationalEmissionRate > p:nth-child(2)").clone()
        );
        $("#print-main-emission-rates").append(
          $("#nationalEmissionRateGraph").clone()
        );
        $("#print-main-emission-rates > #nationalEmissionRateGraph > svg").css({
          display: "inline-block"
        });
        self.showMainReport = true;
        $("#printReportMain").show();
        $("#printReport").hide();

      }
    });
    window.addEventListener("afterprint", function(event) {
      self.showReport = false;
      self.showMainReport = false;
      $("#printReport").hide();
      $("#printReportMain").hide();
    });

    if ($(window).width() < 1025) {
      userSelection.data.fuelMixOrientation = "vertical";
      userSelection.data.emissionRatesOrientation = "vertical";
    } else {
      userSelection.data.fuelMixOrientation = "horizontal";
      userSelection.data.emissionRatesOrientation = "horizontal";
    }

    if (this.$route.name == "home") this.showMain = true;
  },
  watch: {
    $route: function(to, from) {
      if (to.name == "home") this.showMain = true;
      $("#result").hide();
    },
    "$root.$i18n.locale": {
      deep: true,
      handler() {
        this.updateTitle();
      }
    }
  }
};
</script>
<style>
input[type="number"]::-webkit-inner-spin-button,
input[type="number"]::-webkit-outer-spin-button {
  -webkit-appearance: none;
  margin: 0;
}
.subregionLabels,
.selectedRegionValue,
.nationalX text,
.nationalBar text,
.y.axis text,
.ui-tooltip {
  font-size: 15px;
}

.axis line,
.y.axis path,
.nationalY > .domain,
.nationalBarV > .domain {
  fill: none;
  stroke: #000;
  shape-rendering: crispEdges;
}
.x.axis path,
#emissionRatesHeatMap > svg.axis.gradient > g > path {
  display: none;
}

#emissionRatesHeatMap > svg.axis > g > path {
  fill: none;
}
#kpis div,
#kpis .box__title,
#mapSelect,
.select-pollutant-label,
#pollutantSelectAll,
#pollutantSelectSub {
  text-align: center;
}

#app p {
  padding-bottom: 0.7em;
}

#app-content {
  column-gap: 1em;
}

#main-charts {
  /* Prevent too much shrinkage*/
  min-width: 600px;
  max-width: 1000px;
}

.select-pollutant-label,
#nationalEmissionRateSortingStatus,
#nationalFuelMixSortingStatus {
  padding-bottom: 0 !important;
}
#sidebar {
  background-color: #fafafa;
  border: 1px solid black;
  /* Set the width based on the background image size and prevent the sidebar from growing or shrinking which cuts off the image and squeezes the text */
  min-width: 359px;
  max-width: 458px;
}

.modal-mask {
  position: fixed;
  z-index: 9998;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: table;
  transition: opacity 0.3s ease;
}
.modal-wrapper {
  display: table-cell;
  vertical-align: middle;
}

.modal-container {
  width: 70%;
  margin: 0px auto;
  padding: 20px 30px;
  background-color: #fff;
  border-radius: 2px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.33);
  transition: all 0.3s ease;
  font-family: Helvetica, Arial, sans-serif;
}

.modal-body {
  margin: 20px 0;
}

.modal-default-button {
  float: right;
}
/* The usa-button has width:100% by default and on small screens makes the button super wide */
.usa-button {
  width: auto;
}
.tooltip {
  display: none;
  position: absolute;
  border: 1px solid #d3d3d3;
  background-color: #fff;
  border-radius: 5px;
  padding: 8px;
  color: #161616;
  font-size: 12px Arial;
}
/* transition="modal" styles */
.modal-enter {
  opacity: 0;
}

.modal-leave-active {
  opacity: 0;
}
.modal-enter .modal-container,
.modal-leave-active .modal-container {
  -webkit-transform: scale(1.1);
  transform: scale(1.1);
}

#appDescription,
#printReportMain,
#printReport {
  display: none;
}

@media print {
  #app,
  #block-pane-official-website-header,
  .sitewide-alert,
  .ui-tooltip,
  footer,
  nav,
  .skip-links {
    display: none;
  }
  header {
    padding: 0 0 0 0;
  }
  #appDescription,
  #printReportMain,
  #printReport {
    display: block;
  }
}
</style>
