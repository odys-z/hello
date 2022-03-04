
import { assert } from 'chai'

import pacificAtlantic from '../medium/q417';

describe('Q417', () => {
	it('Q417', () => {

        assert.equal([[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]].length,
            pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]).length,
            '- 1 ');

        assert.equal([[0,0],[0,1],[1,0],[1,1]].length,
            pacificAtlantic([[2, 1], [1, 2]]).length,
            '- 2 ');

        assert.equal( [[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]].length, 
            pacificAtlantic([[1,2,3],
                            [8,9,4],
                            [7,6,5]]).length,
            '- 3 ');

        assert.deepEqual( [[0,3],[1,0],[1,1],[1,2],[1,3],[2,0],[2,1],[2,2],[2,3],[3,0],[3,1],[3,2],[3,3]].length, 
            pacificAtlantic([[1, 2, 3, 4],
                            [12,13,14,5],
                            [11,16,15,6],
                            [10, 9, 8,7]]).length,
            '- 3 ');
	});
});