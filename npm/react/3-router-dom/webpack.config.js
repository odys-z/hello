var path = require('path')
var webpack = require('webpack')

var v = 'development';// "production" | "development" | "none"
var version = "1.0.0";

module.exports = {
    mode: v,
    devtool: 'source-map',
    entry: { "home": './src/index.js' },

    output: {
      filename: "[name].min.js",

      path: path.resolve(__dirname, 'dist'),
      publicPath: "./dist/",

      libraryTarget: 'umd'
    },

    plugins: [ ],

    resolve: {
    	extensions: ['*', '.js', '.jsx', '.tsx']
    },
    module: {
        rules: [
          {
            test: /\.js$/,
            loader: 'babel-loader',
            exclude: /node_modules/,
            options: {
              presets: ['@babel/preset-react', '@babel/preset-env'] }
    	  },
        { test: /\.tsx$/,
          loader : 'babel-loader',
          options: { presets: [
            '@babel/preset-react',
            '@babel/preset-typescript',
            '@emotion/babel-preset-css-prop',
            '@babel/preset-env' ] }
        },
          {
            test: /\.css$/,
            use: ["style-loader", "css-loader"]
          } ]
    }
}
