export const userSelection = {
  data: {
    fuelMixOrientation: "",
    emissionRatesOrientation: "",
    sortState: "",
    residentialMode: true
  },
  setResidentialMode(newBool) {
    if (typeof newBool === "boolean") {
      this.data.residentialMode = newBool;
    } else {
      console.error(`residentialMode is of type boolean, ${newBool} supplied`);
    }
  },
  getResidentialMode() {
    return this.data.residentialMode;
  }
};
