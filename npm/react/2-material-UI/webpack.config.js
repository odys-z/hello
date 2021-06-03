var path = require('path')
var webpack = require('webpack')

var v = 'development';// "production" | "development" | "none"
var version = "1.0.0";

module.exports = {
    mode: v,
    devtool: 'source-map',
    entry: { "material-ui": './src/app.js' },

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
            test: /\.js$/,
            loader: 'babel-loader',
            exclude: /node_modules/,
            query: {
              presets: ['@babel/preset-react', '@babel/preset-env'] }
    	  },
          {
            test: /\.css$/,
            use: ["style-loader", "css-loader"]
          } ]
    }
}
