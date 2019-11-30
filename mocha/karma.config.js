// var webpackConfig = require('./webpack-test.config.js');
// webpackConfig.entry = {};

// var path = require('path');
var webpackConfig = require('./webpack-test.config.js');
// var entry = path.resolve(webpackConfig.context, webpackConfig.entry);
process.env.CHROME_BIN = require('puppeteer').executablePath();

module.exports = function(config) {
  config.set({
    frameworks: ['mocha', 'chai'],
    // files: ['test/**/*.js'],
    // files: ['test/all-tests.js'],
	files: ['dist/testBundle.js'],
	// files: [entry],

    reporters: ['progress'],
    port: 9876,  // karma web server port
    colors: true,
    logLevel: config.LOG_INFO,
    // browsers: ['ChromeHeadless'],
	browsers: ['HeadlessChromium'],
    customLaunchers: {
      HeadlessChromium: {
        base: 'ChromiumHeadless',
        flags: [
          '--no-sandbox',
          '--remote-debugging-port=9222',
          '--enable-logging',
          '--user-data-dir=./karma-chrome',
          '--v=1',
          '--disable-background-timer-throttling',
          '--disable-renderer-backgrounding',
          '--proxy-bypass-list=*',
          '--proxy-server=\'direct://\''
       ]
      }
    },

    autoWatch: false,
    // singleRun: false, // Karma captures browsers, runs the tests and exits
    concurrency: Infinity,

	preprocessors: {
      // add webpack as preprocessor
      'test/*tests.js': ['webpack'],
      'test/**/*\.case.js': ['webpack'],
    },
	webpack: webpackConfig,
	plugins:[
	  require('karma-webpack'),
	  ('karma-chai'),
	  ('karma-mocha'),
	  ('karma-chrome-launcher')
	]
  })
}
