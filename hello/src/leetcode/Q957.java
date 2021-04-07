package leetcode;

public class Q957 {
	class SlidFilter{
		private int[] cells;
		private int ix;
		int[] win;

		SlidFilter(int[] cells) {
			this.cells = cells;
//			this.ix = -1;
//			win = new int[] { 0, 0 };
			reset();
		}
		
		public void reset() {
			this.ix = -1;
			win = new int[] { 0, 0 };
			next();
		}

		public boolean next() {
			if (ix - 1 >= 0)
				cells[ix - 1] = win[0];
			ix++;

			win[0] = win[1];
			win[1] = ix - 1 >= 0 ? cells[ix - 1] : 0;
			win[1] ^= ix + 1 < cells.length ? cells[ix + 1] : 0;
			
			return ix < cells.length;
		}
		
		public void end() {
			cells[cells.length - 1] = win[0] ^ 0;
		}
	}

    public int[] prisonAfterNDays(int[] cells, int N) {
    	SlidFilter filter = new SlidFilter(cells);

    	while (N > 0) {
    		filter.reset();
    		while(filter.next())
    			;
    		filter.end();
    		N--;
//    		System.out.println(String.format("%s %s %s %s %s %s %s %s",
//    				cells[0], cells[1], cells[2], cells[3], cells[4], cells[5], cells[6], cells[7]));
    		System.out.println(String.format("%s %s %s %s %s %s %s %s",
    				cells[0], cells[1], cells[2], cells[3], cells[4], cells[5], cells[6], cells[7]));
    	}
    	return cells;
    }
}
