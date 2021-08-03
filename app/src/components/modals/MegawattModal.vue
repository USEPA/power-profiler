<i18n>
{
    "en": {
        "modalHeader": "Megawatt Hour (MWh)",
        "modalBody": "A megawatt (MW) is a unit for measuring power that is equal to one million watts. A megawatt hour (MWh) is equal to 1,000 kilowatts of electricity being used continuously for one hour. One MWh is equivalent to the amount of electricity needed to light 10,000 100-watt light bulbs for one hour or the electricity needed to power an average home for a little over one month.",
        "okButton": "OK"
    },
    "es": {
        "modalHeader": "Megavatio-hora (MWh)",
        "modalBody": "Un megavatio (MW) es una unidad equivalente a un millón de vatios que se utiliza para medir la potencia. Un megavatio-hora (MWh) es igual a 1,000 kilovatios de electricidad usados en forma continua durante una hora. Un megavatio-hora (MWh) equivale a la cantidad de electricidad que se requiere para encender 10,000 bombillas de luz de 100 vatios durante una hora, o a la electricidad necesaria para proporcionar alimentación eléctrica a un hogar promedio durante poco más de un mes.",
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
              <p>{{ $t("modalBody") }}</p>
            </slot>
            <button
              id="megawatt-ok"
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
    document.getElementById("megawatt-ok").focus();
  }
};
</script>
