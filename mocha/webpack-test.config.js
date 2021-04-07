
var webpack = require('webpack');
var nodeExternals = require('webpack-node-externals');
var WebpackShellPlugin = require('webpack-shell-plugin');


var config = {
  entry: './test/all-tests.js',
  output: {
    filename: 'testBundle.js'
  },
  target: 'node',
  externals: [nodeExternals()],
  node: {
    fs: 'empty'
  },


  plugins: [
    new WebpackShellPlugin({
      onBuildExit: "mocha --colors --require spec-helper.js dist/testBundle.js"
    })
  ]
};


module.exports = config;
