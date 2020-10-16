<i18n>
{
    "en": {
        "modalHeader": "Additional Resources",
        "modalBody": {
            "energy": "Energy and the Environment",
            "airMarkets": "Clean Air Markets Division (CAMD)",
            "ghgReporting": "Greenhouse Gas Reporting Program (GHGRP)",
            "eia": "U.S. Energy Information Administration (EIA)",
            "nei": "National Emissions Inventory (NEI)",
            "criteriaAirPollutants": "Criteria Air Pollutants",
            "climateLeadership": "EPA Center for Corporate Climate Leadership",
            "stateLocalAndTribalInventoryTools": "State, Local, and Tribal Greenhouse Gas Inventory Tools"
        },
        "okButton": "OK",
        "ariaLabels": {
            "opensNewWin": "Opens new window"
        }
    },
    "es": {
        "modalHeader": "Recursos adicionales",
        "modalBody": {
            "energy": "La energía y el medioambiente",
            "airMarkets": "División de mercados de aire limpio (CAMD)",
            "ghgReporting": "Programa de informes sobre gases de efecto invernadero (GHGRP)",
            "eia": "Administración de información de energía (EIA) de EE. UU.",
            "nei": "Inventario nacional de emisiones (NEI)",
            "criteriaAirPollutants": "Contaminantes del aire sujetos a criterios",
            "climateLeadership": "Centro de la EPA para el Liderazgo corporativo del clima",
            "stateLocalAndTribalInventoryTools": "Herramientas estatales, locales y tribales para el inventario de gases de efecto invernadero"
        },
        "okButton": "Ir",
        "ariaLabels": {
            "opensNewWin": "abre una nueva ventana"
        }
    }
}
</i18n>
<template>
  <transition name="modal">
    <div class="modal-mask">
      <div class="modal-wrapper">
        <div class="modal-container">
          <div class="modal-header">
            <slot name="header">
              <h3>{{ $t("modalHeader") }}</h3>
            </slot>
          </div>

          <div class="modal-body">
            <slot name="body">
              <ul>
                <li>
                  <a
                    v-bind:aria-label="$t('ariaLabels.opensNewWin')"
                    href="/energy"
                    target="_blank"
                    >{{ $t("modalBody.energy") }}</a
                  >
                </li>
                <li>
                  <a
                    v-bind:aria-label="$t('ariaLabels.opensNewWin')"
                    href="/airmarkets"
                    target="_blank"
                    >{{ $t("modalBody.airMarkets") }}</a
                  >
                </li>
                <li>
                  <a
                    v-bind:aria-label="$t('ariaLabels.opensNewWin')"
                    href="/ghgreporting"
                    target="_blank"
                    >{{ $t("modalBody.ghgReporting") }}</a
                  >
                </li>
                <li>
                  <a
                    v-bind:aria-label="$t('ariaLabels.opensNewWin')"
                    href="https://www.eia.gov/"
                    target="_blank"
                    >{{ $t("modalBody.eia") }}</a
                  >
                </li>
                <li>
                  <a
                    v-bind:aria-label="$t('ariaLabels.opensNewWin')"
                    href="/air-emissions-inventories/national-emissions-inventory-nei"
                    target="_blank"
                    >{{ $t("modalBody.nei") }}</a
                  >
                </li>
                <li>
                  <a
                    v-bind:aria-label="$t('ariaLabels.opensNewWin')"
                    href="/criteria-air-pollutants"
                    target="_blank"
                    >{{ $t("modalBody.criteriaAirPollutants") }}</a
                  >
                </li>
                <li>
                  <a
                    v-bind:aria-label="$t('ariaLabels.opensNewWin')"
                    href="/climateleadership"
                    target="_blank"
                    >{{ $t("modalBody.climateLeadership") }}</a
                  >
                </li>
                <li>
                  <a
                    v-bind:aria-label="$t('ariaLabels.opensNewWin')"
                    href="/statelocalenergy/state-local-and-tribal-inventory-tools"
                    target="_blank"
                    >{{ $t("modalBody.stateLocalAndTribalInventoryTools") }}</a
                  >
                </li>
              </ul>
            </slot>
            <button
              id="resources-ok"
              class="modal-default-button"
              @click="$emit('close')"
            >
              {{ $t("okButton") }}
            </button>
          </div>
        </div>
      </div>
    </div>
  </transition>
</template>
<script>
export default {
  mounted: function () {
    document.getElementById("resources-ok").focus();
  },
};
</script>
