import $ from 'jquery';

export class Hello {
	/**
	 * @constructor
	 */
	constructor() {
		console.log("Hello constructor...");
	}

	hi(name) {
		console.log(`Hello ${name}!`);
	}
}
