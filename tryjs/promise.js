class Client {
	post(arg, onok, onerr) {
		console.log('posting...');
		setTimeout(() => {onok(arg + 1000)}, 1000);
	}

	postSync(arg) {
		let me = this;
		return new Promise((resolve, reject) => {
			me.post(arg, (v) => {
				resolve(v);
			},
			(err)=>{reject(err);});
		});
	}
}
