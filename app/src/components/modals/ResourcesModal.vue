<i18n>
{
    "en": {
        "modalHeader": "Additional Resources",
        "modalBody": {
            "zipCodeLookup": "2023 U.S. Electric Utility Companies and Rates: Look-up by Zipcode",
            "energy": "Energy and the Environment",
            "powerSectorPrograms": "Clean Air Power Sector Programs",
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
            "zipCodeLookup": "2023 Compañías y tarifas de servicios eléctricos de EE. UU.: búsqueda por código postal",
            "energy": "La energía y el medioambiente",
            "powerSectorPrograms": "Programas del Sector de Energía para el Aire Limpio",
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
                    href="https://data.openei.org/submissions/6225"
                    target="_blank"
                    >{{ $t("modalBody.zipCodeLookup") }}</a
                  >
                </li>
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
                    href="/power-sector"
                    target="_blank"
                    >{{ $t("modalBody.powerSectorPrograms") }}</a
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
              class="usa-button modal-default-button"
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
  mounted: function() {
    document.getElementById("resources-ok").focus();
  }
};
</script>
