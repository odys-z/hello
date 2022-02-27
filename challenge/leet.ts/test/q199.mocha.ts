
import { assert } from 'chai'

import rightSideView, { TreeNode } from '../medium/q199';

describe('Q199', () => {
	it('Q199', () => {
		assert.deepEqual(rightSideView(new TreeNode(1)), [1], '- 1');
		assert.deepEqual(rightSideView(undefined), [], '- 1');
	});
});