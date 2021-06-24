<template>
    <transition name="modal">
        <div class="modal-mask">
        <div class="modal-wrapper">
            <div class="modal-container">

            <div class="modal-header">
                <slot name="header">
                <h3>eGRID Subregions</h3>
                </slot>
            </div>

            <div class="modal-body">
                <slot name="body">
                    <p>The 27 eGRID subregions in the US are defined by EPA using data from the Energy Information Administration (EIA) and the North American Electric Reliability Corporation (NERC). The subregions are defined to limit the amount of imports and exports across regions in order to best represent the electricity used in each of the subregions. More information can be found in section 3.4.2 of the <a aria-label="Opens new window" href="/energy/egrid-technical-support-document" target="_blank">eGRID Technical Support Document</a>.</p>
                </slot>
                <button id="subregions-ok" class="modal-default-button" @click="$emit('close')">
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
    mounted: function(){
        document.getElementById("subregions-ok").focus()
    }
}
</script>
