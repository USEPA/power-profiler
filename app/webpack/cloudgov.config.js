const HtmlWebpackPlugin = require('html-webpack-plugin');
const VueLoaderPlugin = require('vue-loader/lib/plugin');
const webpack = require('webpack');
const path = require('path');
const CopyPlugin = require('copy-webpack-plugin');
const CreateFileWebpack = require('create-file-webpack');

module.exports = env => {
  return {
    entry: './src/main.js',
    output: {
      filename: 'bundle.js',
      path: path.resolve( __dirname, '..', 'dist/cloudgov')
    },
    module: {
      rules: [
        { test: /\.js$/, use: 'babel-loader' },
        { test: /\.vue$/, use: 'vue-loader' },
        { test: /\.css$/, use: ['vue-style-loader', 'css-loader']},
        { test: /\.csv$/, use: 'raw-loader' },
        { test: /\.json$/, use: 'raw-loader' },
        { resourceQuery: /blockType=i18n/, type: 'javascript/auto', loader: '@kazupon/vue-i18n-loader' }
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
          'NODE_ENV': JSON.stringify('development'),
          'VUE_APP_SUBREGION_JSON': JSON.stringify("./data/subregion.json"),
          'VUE_APP_ZIP_UTILITY':JSON.stringify("./data/zip.csv"),
          'VUE_APP_EGRID_LOGO':JSON.stringify("./assets/img/egrid-text-logo.png"),
        }
      }),
      new CopyPlugin([
      	{
        	from: './data/*',
	        to: '.',
	},
	{
		from: './assets/img/*',
		to: '.'
	}
    ]),
      new CreateFileWebpack({
	      path: './dist/cloudgov',
	      fileName: 'Staticfile',
	      content: 'directory: visible'
      })
    ]
  };
};
