package leet.java.medium;

import java.util.ArrayList;
import java.util.List;

/**
 * <h6>Problem:</h6>
 * <a href='https://leetcode.com/problems/all-paths-from-source-to-target/'>
 * 797. All Paths From Source to Target</a>
 * <br>
 * Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all
 * possible paths from node 0 to node n - 1, and return them in any order.
 * <br>
 * The graph is given as follows: graph[i] is a list of all nodes you can visit from
 * node i (i.e., there is a directed edge from node i to node graph[i][j]).
 * 
 * @author Odys Zhou
 *
 */
public class Q797 {
	private List<List<List<Integer>>> dfs(List<List<List<Integer>>> dp, int[][] graph) {
		int lastx = graph.length - 1;
		for (int x = lastx - 1; 0 <= x; x--) {
			int[] nxtNodes = graph[x];
			List<List<Integer>> pathx = new ArrayList<List<Integer>>();
			// for (int nxt : nxtNodes) {
			for (int nxt = 0; nxt < nxtNodes.length; nxt++) { 
				int nxtNode = nxtNodes[nxt];
				if (nxtNode < 0) continue; // previous tagged as unresolved

				if (dp.get(nxtNode).size() == 0) {
					// int temp = nxtNodes[nxt];
					nxtNodes[nxt] = -1;
					dp = dfs(dp, graph);
					nxtNodes[nxt] = nxtNode;
				}

				for (List<Integer> nxtPath : dp.get(nxtNode)) {
					List<Integer> p = new ArrayList<Integer>();
					p.add(x);
					p.addAll(nxtPath);
					pathx.add(p);
				}
			}
			dp.set(x, pathx);
			lastx = x;
		}
		return dp;
	}


    /**23.83%
     * @param graph
     * @return
     */
    public List<List<Integer>> allPathsSourceTarget(int[][] graph) {
        int lastx = graph.length - 1;
        List<List<List<Integer>>>dp = new ArrayList<List<List<Integer>>>();
        for (int i = 0; i <= lastx; i++)
        	dp.add(new ArrayList<List<Integer>>());

        ArrayList<Integer> lastdp = new ArrayList<Integer>();
        lastdp.add(lastx);
        dp.get(lastx).add(lastdp); 
        dp = dfs(dp, graph);
        return dp.get(0);
    }

	public static void main(String[] args) {
	}

}
