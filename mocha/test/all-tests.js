context = require.context('.', true, /\.case\.js$/);
context.keys().forEach(context)
module.exports = context;
