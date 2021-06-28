<template>
  <transition name="modal">
    <div class="modal-mask">
      <div class="modal-wrapper">
        <div class="modal-container">
          <div class="modal-header">
            <slot name="header">
              <h3>Additional Resources</h3>
            </slot>
          </div>

          <div class="modal-body">
            <slot name="body">
              <ul>
                <li>
                  <a
                    aria-label="Opens new window"
                    href="/energy"
                    target="_blank"
                    >Energy and the Environment</a
                  >
                </li>
                <li>
                  <a
                    aria-label="Opens new window"
                    href="/airmarkets"
                    target="_blank"
                    >Clean Air Markets Division (CAMD)</a
                  >
                </li>
                <li>
                  <a
                    aria-label="Opens new window"
                    href="/ghgreporting"
                    target="_blank"
                    >Greenhouse Gas Reporting Program (GHGRP)</a
                  >
                </li>
                <li>
                  <a
                    aria-label="Opens new window"
                    href="https://www.eia.gov/"
                    target="_blank"
                    >U.S. Energy Information Administration (EIA)</a
                  >
                </li>
                <li>
                  <a
                    aria-label="Opens new window"
                    href="/air-emissions-inventories/national-emissions-inventory-nei"
                    target="_blank"
                    >National Emissions Inventory (NEI)</a
                  >
                </li>
                <li>
                  <a
                    aria-label="Opens new window"
                    href="/criteria-air-pollutants"
                    target="_blank"
                    >Criteria Air Pollutants</a
                  >
                </li>
                <li>
                  <a
                    aria-label="Opens new window"
                    href="/climateleadership"
                    target="_blank"
                    >EPA Center for Corporate Climate Leadership</a
                  >
                </li>
                <li>
                  <a
                    aria-label="Opens new window"
                    href="/statelocalenergy/state-local-and-tribal-inventory-tools"
                    target="_blank"
                    >State, Local, and Tribal Greenhouse Gas Inventory Tools</a
                  >
                </li>
              </ul>
            </slot>
            <button
              id="resources-ok"
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
    document.getElementById("resources-ok").focus();
  }
};
</script>
