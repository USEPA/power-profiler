import Vue from "vue";
import VueRouter from "vue-router";
import subregionCharts from "../components/SubregionCharts.vue";

Vue.use(VueRouter);

export default new VueRouter({
  routes: [
    {
      path: "/",
      name: "home"
    },
    {
      path: "/:subregion",
      name: "subregion",
      component: subregionCharts
    }
  ]
});
