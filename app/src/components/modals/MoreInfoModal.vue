<i18n>
{
    "en": {
        "modalHeader": "What is Power Profiler?",
        "okButton": "OK"
    },
    "es": {
        "modalHeader": "¿Qué es el analizador de consumo energía?",
        "okButton": "Ir"
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
              <appDescription></appDescription>
            </slot>
            <button
              id="more-info-ok"
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
import AppDescription from "../AppDescription.vue";

export default {
  components: {
    appDescription: AppDescription
  },
  mounted: function() {
    document.getElementById("more-info-ok").focus();
    $("#appDescription").show();
  }
};
</script>
