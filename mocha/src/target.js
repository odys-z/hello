
console.log('you\'ve got here...');

class TargetClass {
	constructor () {
		console.log('Constructing target...');
	}

	funcA (para) {
		if (para)
			return 'ok';
		else return '';
	}
}

function TargetFunc() {
	console.log('Calling target...');
}

export {TargetClass, TargetFunc}

// module.exports = {
// TargetFunc
// }
