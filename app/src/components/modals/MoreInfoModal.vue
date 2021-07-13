<template>
    <transition name="modal">
        <div class="modal-mask">
        <div class="modal-wrapper">
            <div class="modal-container">

            <div class="modal-header">
                <slot name="header">
                <h3>What is Power Profiler?</h3>
                </slot>
            </div>

            <div class="modal-body">
                <slot name="body">
                    <appDescription></appDescription>
                </slot>
                <button id="more-info-ok" class="usa-button modal-default-button" @click="$emit('close')">
                    OK
                </button>
            </div>
            </div>
        </div>
        </div>
    </transition>
</template>
<script>
import AppDescription from "../AppDescription.vue"

export default {
    components: {
        appDescription: AppDescription,
    },
    mounted: function(){
        document.getElementById("more-info-ok").focus()
        $("#appDescription").show()
    }
}
</script>
