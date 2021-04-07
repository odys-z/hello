package leet.java.medium;

/** 100.00%
 * @author Odys Zhou
 *
 */
public class Q684 {
	class DSU {
		private int[] parent;
		private int[] rank;

		DSU(int N) {
			this.parent = new int[N+1]; 
			this.rank = new int[N+1]; 
			for (int i = 0; i < N + 1; i++) {
				this.parent[i] = i;
			}
		}
		
		int getU(int x) {
			while (this.parent[x] != x)
				x = this.parent[x];
			return x;
		}
		
		boolean union(int x, int y) {
			x = getU(x);
			y = getU(y);
			if (x == y) return false;
			
			if (rank[x] < rank[y]) {
				parent[x] = y;
                rank[y] ++;                
            }
			else {
				parent[y] = x;
                rank[x] ++;                
            }
			return true; 
		}
	}
	
    public int[] findRedundantConnection(int[][] edges) {
    	DSU dsu = new DSU(edges.length);
    	for (int[] e : edges)
    		if (!dsu.union(e[0], e[1]))
    			return e;
    	return null;
    }
}
