/** Configuration for test with Mocha.
	npm run build
	npm test
 */

const __TESTING__ = true;
context = require.context('.', true, /\.mocha\.ts$/);

context.keys().forEach(context);
module.exports = context;
