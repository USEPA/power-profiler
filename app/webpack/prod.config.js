const HtmlWebpackPlugin = require('html-webpack-plugin');
const VueLoaderPlugin = require('vue-loader/lib/plugin');
const webpack = require('webpack');
const path = require('path');

module.exports = env => {
  return {
    entry: './src/main.js',
    output: {
      filename: 'bundle.js',
      path: path.resolve( __dirname, '..', 'dist/prod')
    },
    module: {
      rules: [
        { test: /\.js$/, use: 'babel-loader' },
        { test: /\.vue$/, use: 'vue-loader' },
        { test: /\.css$/, use: ['vue-style-loader', 'css-loader']},
        { resourceQuery: /blockType=i18n/, type: 'javascript/auto', loader: '@kazupon/vue-i18n-loader' }
      ]
    },
    target: "web",
    plugins: [
      new HtmlWebpackPlugin({
        template: './src/index.html',
      }),
      new VueLoaderPlugin(),
      new webpack.DefinePlugin({
        'process.env':{
          'NODE_ENV': JSON.stringify('production'),
          'VUE_APP_SUBREGION_JSON': JSON.stringify("/sites/production/files/2019-06/subregion.json"),
          'VUE_APP_ZIP_UTILITY':JSON.stringify("/sites/production/files/2018-12/zip.csv"),
          'VUE_APP_EGRID_LOGO':JSON.stringify("/sites/production/files/2018-12/egrid-text-logo.png"),
        }
      }),
    ]
  };
};