import Vue from 'vue';
import App from './App.vue';
import router from './router/router';
import { selectedSubregion } from './stores/selectedSubregion.js';
import { env } from './config/env.js'

var vm = new Vue({
  el: '#app',
  render: h => h(App),
  router,
  beforeCreate(){
    // Set app's environment variables
    env.SUBREGION_JSON = process.env.VUE_APP_SUBREGION_JSON;
    env.ZIP_UTILITY = process.env.VUE_APP_ZIP_UTILITY;
    env.EGRID_LOGO = process.env.VUE_APP_EGRID_LOGO;
  }
});

vm.$on("subregionSelected", function(d){
  selectedSubregion.update(d);
  this.$children[0].$children[4].$children[0].selectedRegion = selectedSubregion.data
  this.$children[0].$children[4].selectedRegion = selectedSubregion.data
  $(".map").css({"fill":""});
  $("." + d.properties.name).css({"fill":"steelblue"});
  $("#regionSelectionDropdown").val(d.properties.name);
  router.push(d.properties.name);
});

if (typeof ga === "function") {
  router.afterEach((to) => {
    ga("EPA.set","page", location.pathname + "#" + to.fullPath);
    ga("EPA.send", "pageview");
  });
}



