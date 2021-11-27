class Client {
	post(arg, onok, onerr) {
		console.log(`post(${arg})`);
		setTimeout(() => {onok(arg + 2000)}, 2000);
	}

	postSync(arg) {
		let me = this;
		console.log('promise ...');
		return new Promise((resolve, reject) => {
			me.post(arg || 'async - await: ', (v) => {
				console.log('resolving promise, v: ', v);
				resolve(v);
			},
			(err)=>{reject(err);});
		});
	}
}
