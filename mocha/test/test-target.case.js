import {TargetClass, TargetFunc} from '../src/target.js';
import { expect } from 'chai';
var assert = require('assert');

describe('tests sample target', function() {
  let clssTarget, funcTarget
  before(function() {
	console.log("before()...")
	clssTarget = new TargetClass();
  });

  it('test funcA()', function() {
    // expect(true).to.be.true;
	assert.equal('ok', clssTarget.funcA('hi'));
	assert.equal('', clssTarget.funcA());
  });
});
