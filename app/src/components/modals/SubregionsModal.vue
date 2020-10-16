<i18n>
{
    "en": {
        "modalHeader": "eGRID Subregions",
        "modalBody": {
            "content": "The 26 eGRID subregions in the US are defined by EPA using data from the Energy Information Administration (EIA) and the North American Electric Reliability Corporation (NERC). The subregions are defined to limit the amount of imports and exports across regions in order to best represent the electricity used in each of the subregions. More information can be found in section 3.4.2 of the {0}.",
            "eGRIDTSDLink": "eGRID Technical Support Document"
        },
        "okButton": "OK",
        "ariaLabels": {
            "opensNewWin": "Opens new window"
        }
    },
    "es": {
        "modalHeader": "Subregiones de eGRID",
        "modalBody": {
            "content": "The 26 eGRID subregions in the US are defined by EPA using data from the Energy Information Administration (EIA) and the North American Electric Reliability Corporation (NERC). The subregions are defined to limit the amount of imports and exports across regions in order to best represent the electricity used in each of the subregions. More information can be found in section 3.4.2 of the {0}.",
            "eGRIDTSDLink": "eGRID Technical Support Document"
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
              <i18n
                path="modalBody.content"
                tag="p"
                for="modalBody.eGRIDTSDLink"
              >
                <a
                  v-bind:aria-label="$t('ariaLabels.opensNewWin')"
                  href="/egrid/egrid-technical-support-document"
                  target="_blank"
                >
                  {{ $t("modalBody.eGRIDTSDLink") }}</a
                >
              </i18n>
            </slot>
            <button
              id="subregions-ok"
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
    document.getElementById("subregions-ok").focus();
  },
};
</script>
