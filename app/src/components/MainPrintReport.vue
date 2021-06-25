<template>
  <div id="printReportMain">
    <div>
      <div id="print-main-map"></div>
      <div class="page-break" id="print-main-fuel-mix"></div>
      <div class="page-break" id="print-main-emission-rates"></div>
    </div>
  </div>
</template>
<style>
#printReportMain {
  width: 900px;
}
.page-break {
  display: block;
  page-break-after: always;
}
</style>
