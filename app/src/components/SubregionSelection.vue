<i18n>
{
  "en": {
    "title": "Power Profiler",
    "userLocation": "Enter zip code:",
    "placeHolder": "Zip code",
    "goButton": "Go",
    "moreInfo": "More Information",
    "egridSubregions": "eGRID Subregions",
    "selectUtility": "Select your utility",
    "invalidZip": "Please enter a valid zip code."
  },
  "es": {
    "title": "Analizador de consumo de energía",
    "userLocation": "Ingresa tu código postal:",
    "placeHolder": "Código postal en EE. UU.",
    "goButton": "Ir",
    "moreInfo": "Más Información",
    "egridSubregions": "Subregiones de eGRID",
    "selectUtility": "Seleccione su empresa de electricidad",
    "invalidZip": "Por favor ingrese un código postal válido."
  }
}
</i18n>
<template>
  <div id="selectionBox" class="box multi related-info">
    <div class="pane-content">
      <div id="zipFormDiv">
        <h2>{{ $t("title") }}</h2>
        <div id="formContainer" class="form-item form-type-textfield">
          <form id="zipForm">
            <label for="userLocation">
              <strong>{{ $t("userLocation") }}</strong>
            </label>
            <input
              class="form-text"
              id="userLocation"
              maxlength="128"
              size="20"
              type="number"
              v-bind:placeholder="$t('placeHolder')"
              required
            />
            <button id="goButton" class="usa-button" type="submit">{{ $t("goButton") }}</button>
          </form>
        </div>
        <div id="errorMessage" style="display: none"></div>
        <div
          class="form-item form-type-select"
          id="utilitySelectDiv"
          style="display: none"
        >
          <select
            class="form-select"
            id="utilitySelect"
            style="height: 36px"
          ></select>
        </div>
        <div id="start-over-div">
          <button id="start-over" class="usa-button" style="display: none">Start Over</button>
        </div>
      </div>
      <div id="regionSelectionDiv">
        <label for="regionSelectionDropdown" id="subregionsHeader">
          <strong>{{ $t("egridSubregions") }}</strong>
          <a
            href="javascript:void(0)"
            class="more-link"
            @click="$parent.$parent.showSubregionInfo = true"
            >{{ $t("moreInfo") }}</a
          >
        </label>
        <div class="form-item form-type-select">
          <select
            @change="handleSelectChange"
            class="form-select"
            id="regionSelectionDropdown"
          >
            <option value="All">{{ $t("egridSubregions") }}</option>
            <option value="AKGD">AKGD (ASCC Alaska Grid)</option>
            <option value="AKMS">AKMS (ASCC Miscellaneous)</option>
            <option value="AZNM">AZNM (WECC Southwest)</option>
            <option value="CAMX">CAMX (WECC California)</option>
            <option value="ERCT">ERCT (ERCOT All)</option>
            <option value="FRCC">FRCC (FRCC All)</option>
            <option value="HIMS">HIMS (HICC Miscellaneous)</option>
            <option value="HIOA">HIOA (HICC Oahu)</option>
            <option value="MROE">MROE (MRO East)</option>
            <option value="MROW">MROW (MRO West)</option>
            <option value="NEWE">NEWE (NPCC New England)</option>
            <option value="NWPP">NWPP (WECC Northwest)</option>
            <option value="NYCW">NYCW (NPCC NYC/Westchester)</option>
            <option value="NYLI">NYLI (NPCC Long Island)</option>
            <option value="NYUP">NYUP (NPCC Upstate NY)</option>
            <option value="PRMS">PRMS (Puerto Rico Miscellaneous)</option>
            <option value="RFCE">RFCE (RFC East)</option>
            <option value="RFCM">RFCM (RFC Michigan)</option>
            <option value="RFCW">RFCW (RFC West)</option>
            <option value="RMPA">RMPA (WECC Rockies)</option>
            <option value="SPNO">SPNO (SPP North)</option>
            <option value="SPSO">SPSO (SPP South)</option>
            <option value="SRMV">SRMV (SERC Mississippi Valley)</option>
            <option value="SRMW">SRMW (SERC Midwest)</option>
            <option value="SRSO">SRSO (SERC South)</option>
            <option value="SRTV">SRTV (SERC Tennessee Valley)</option>
            <option value="SRVC">SRVC (SERC Virginia/Carolina)</option>
          </select>
        </div>
      </div>
      <subregionMap id="subregionMapContainer"></subregionMap>
    </div>
  </div>
</template>

<script>
import { env } from "../config/env.js";
import subregionMap from "./SubregionMap.vue";
import { allSubregions } from "../stores/allSubregions.js";

export default {
  components: {
    subregionMap: subregionMap
  },
  data() {
    return {
      userZip: "",
      selectedSubregion: {},
      utilArr: []
    };
  },
  methods: {
    processZipForm: function(e) {
      e.preventDefault();
      $("#errorMessage").hide();
      $("#utilitySelectDiv").hide();
      var self = this;
      self.userZip = $("#userLocation").val();
      if (this.userZip) {
        d3.csv(
          env.ZIP_UTILITY,
          function(d) {
            if (self.userZip == d.zip) {
              return d;
            }
          },
          function(data) {
            if (data.length == 1) {
              var subregion = allSubregions.data.filter(function(d) {
                return d.properties.name == data[0].SUBRGN;
              });
              $("#utilitySelect").hide();
              self.$root.$emit("subregionSelected", subregion[0]);
            } else if (data.length > 1) {
              $("#errorMessage").hide();
              if ($("#utilitySelect").children()) {
                $("#utilitySelect").show();
              }
              self.utilArr = [];
              var subArr = [];
              var utilitySelectHTML = [
                `<option disabled selected value>${self.$t("selectUtility")}</option>`
              ];
              for (var i = 0; i < data.length; i += 1) {
                self.utilArr.push(data[i]);
                utilitySelectHTML.push(
                  "<option value='" + i + "'>" + data[i].UtilName + "</option>"
                );
                if (subArr.indexOf(data[i].SUBRGN) == -1) {
                  subArr.push(data[i].SUBRGN);
                }
              }
              if (subArr.length > 1) {
                $("#utilitySelect").html(utilitySelectHTML.join());
                $("#utilitySelect").attr("required", true);
                $("#utilitySelectDiv").show();
              } else {
                var subregionSelection = allSubregions.data.filter(function(d) {
                  for (var i = 0; i < subArr.length; i += 1) {
                    if (subArr[i] == d.properties.name) {
                      return d;
                    }
                  }
                });
                self.$root.$emit("subregionSelected", subregionSelection[0]);
              }
            } else {
              $("#errorMessage").show();
              $("#errorMessage").html(`<p>${self.$t("invalidZip")}</p>`);
            }
          }
        );
      } else {
        $("#errorMessage").show();
        $("#errorMessage").html(`<p>${self.$t("invalidZip")}</p>`);
      }
    },
    handleSelectChange: function(e) {
      $("#userLocation").val("");
      $("#utilitySelectDiv").hide();
      var subAcronym = e.target.options[e.target.options.selectedIndex].value;
      this.selectedSubregion = allSubregions.data.filter(
        d => d.properties.name == subAcronym
      )[0];
      this.$root.$emit("subregionSelected", this.selectedSubregion);
    }
  },
  mounted: function() {
    var self = this;
    const zipForm = document.getElementById("zipForm");
    zipForm.addEventListener("submit", this.processZipForm);
    $("#utilitySelect").on("change", function(e) {
      var index = $("#utilitySelect").val();
      var subregion = allSubregions.data.filter(function(d) {
        return d.properties.name == self.utilArr[index].SUBRGN;
      });
      self.$root.$emit("subregionSelected", subregion[0]);
    });
  }
};
</script>
<style>
#selectionBox > .pane-content {
  padding: 0;
}
#zipFormDiv {
  color: white;
  position: relative;
  margin: 0 auto;
  width: 100%;
  background-position: 50%;
  background-repeat: no-repeat;
  height: 378px;
  text-align: center;
  background-image: url(https://www.epa.gov/sites/production/files/2018-12/power-profiler-sm-no-text.png);
}
#zipFormDiv h2 {
  padding-top: 1em;
}
#regionSelectionDiv {
  background-color: #fafafa;
  padding-top: 1em;
  text-align: center;
}
#subregionMapContainer {
  background-color: #fafafa;
}
#formContainer {
  padding-bottom: 0;
}
</style>
