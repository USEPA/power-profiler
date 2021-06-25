<template>
  <transition name="modal">
    <div class="modal-mask">
      <div class="modal-wrapper">
        <div class="modal-container">
          <div class="modal-header">
            <slot name="header">
              <h3>Megawatt Hour (MWh)</h3>
            </slot>
          </div>

          <div class="modal-body">
            <slot name="body">
              <p>
                A megawatt (MW) is a unit for measuring power that is equal to
                one million watts. A megawatt hour (MWh) is equal to 1,000
                kilowatts of electricity being used continuously for one hour.
                One MWh is equivalent to the amount of electricity needed to
                light 10,000 100-watt light bulbs for one hour or the
                electricity needed to power an average home for a little over
                one month.
              </p>
            </slot>
            <button
              id="megawatt-ok"
              class="modal-default-button"
              @click="$emit('close')"
            >
              OK
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
