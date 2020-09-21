const HtmlWebpackPlugin = require('html-webpack-plugin');
const VueLoaderPlugin = require('vue-loader/lib/plugin');
const webpack = require('webpack');
const path = require('path');

module.exports = env => {
  return {
    entry: './src/main.js',
    output: {
      filename: 'bundle.js',
      path: path.resolve(__dirname, 'dist')
    },
    module: {
      rules: [
        { test: /\.js$/, use: 'babel-loader' },
        { test: /\.vue$/, use: 'vue-loader' },
        { test: /\.css$/, use: ['vue-style-loader', 'css-loader'] },
        { resourceQuery: /blockType=i18n/, type: 'javascript/auto', loader: '@kazupon/vue-i18n-loader' }
      ]
    },
    devServer: {
      open: false,
      hot: true,
    },
    target: "web",
    plugins: [
      new HtmlWebpackPlugin({
        template: './src/index.html',
      }),
      new VueLoaderPlugin(),
      new webpack.HotModuleReplacementPlugin(),
      new webpack.DefinePlugin({
        'process.env': {
          'NODE_ENV': JSON.stringify('development'),
          'VUE_APP_SUBREGION_JSON': JSON.stringify("./data/subregion.json"),
          'VUE_APP_ZIP_UTILITY': JSON.stringify("./data/zip.csv"),
          'VUE_APP_EGRID_LOGO': JSON.stringify("./assets/img/egrid-text-logo.png"),
        }
      }),
    ]
  };
};