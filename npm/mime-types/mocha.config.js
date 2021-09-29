/** Configuration for test with Mocha.
 * npm test
 */
var webpack = require('webpack');

var config = {
  mode: 'development',
  entry: './test/no-node.js',
  output: {
    filename: 'testBundle.js'
  },
  target: 'node',

  plugins: [ ],

  resolve: {
	extensions: ['.js']
  },

  module: {
	rules: [
		{   test: /\.js$/,
			loader: 'babel-loader',
			options: {
			  presets: [] }
		},
	]
  }
};

module.exports = config;
