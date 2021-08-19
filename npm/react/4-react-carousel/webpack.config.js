var path = require('path')
var webpack = require('webpack')

var v = 'development';// "production" | "development" | "none"
var version = "1.0.0";

module.exports = {
    mode: v,
    devtool: 'source-map',
    entry: { "carousel": './react-elastic-carousel/src/index.js' },

    output: {
      filename: "[name].min.js",

      path: path.resolve(__dirname, 'dist'),
      publicPath: "./dist/",

      libraryTarget: 'umd'
    },

    plugins: [ ],

    externals: { xv: 'xv' },

    resolve: {
    	extensions: ['*', '.js', '.jsx']
    },
    module: {
        rules: [
          {
            test: /\.jsx?$/,
            loader: 'babel-loader',
            query: {
              presets: ['@babel/preset-react', '@babel/preset-env'] }
    	  },
          {
            test: /\.css$/,
            use: ["style-loader", "css-loader"]
          } ]
    }
}
