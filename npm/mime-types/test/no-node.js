
import chai from 'chai';
import { expect, assert } from 'chai';
import Mime from '../index';

describe('[case 1. regex]', () => {
    it('mime2type', () => {
		assert.equal(Mime.extension('image/png;base64'), 'png', '1 png');
	});

    it('type2mime', () => {
		assert.equal(Mime.lookup('png'), 'image/png', '00.2 --png');
	});
});
