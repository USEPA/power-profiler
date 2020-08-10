const HtmlWebpackPlugin = require('html-webpack-plugin');
const VueLoaderPlugin = require('vue-loader/lib/plugin');
const webpack = require('webpack');
const path = require('path');

module.exports = env => {
  return {
    entry: './src/main.js',
    output: {
      filename: 'bundle.js',
      path: path.resolve( __dirname, '..', 'dist/stag')
    },
    module: {
      rules: [
        { test: /\.js$/, use: 'babel-loader' },
        { test: /\.vue$/, use: 'vue-loader' },
        { test: /\.css$/, use: ['vue-style-loader', 'css-loader']},
      ]
    },
    target: "web",
    plugins: [
      new HtmlWebpackPlugin({
        template: './src/index.html',
      }),
      new VueLoaderPlugin(),
      new webpack.HotModuleReplacementPlugin(),
      new webpack.DefinePlugin({
        'process.env':{
          'NODE_ENV': JSON.stringify('production'),
          'VUE_APP_SUBREGION_JSON': JSON.stringify("/sites/staging/files/2019-02/subregion_0.json"),
          'VUE_APP_ZIP_UTILITY':JSON.stringify("/sites/staging/files/2018-07/zip_utility.csv"),
          'VUE_APP_EGRID_LOGO':JSON.stringify("/sites/staging/files/2018-09/egrid_text_logo.png"),
        }
      }),
    ]
  };
};