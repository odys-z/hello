package leet.java.medium;

import static org.junit.jupiter.api.Assertions.assertTrue;

import org.junit.jupiter.api.Test;

class Q684Test {

	@Test
	void test() {
        Q684 q = new Q684();
        int[][] edges = new int[][] { {1, 2}, {2, 3}, {1, 3} };
		int[] e = q.findRedundantConnection(edges);
		assertTrue(e[0] == 1 && e[1] == 3);
		
        edges = new int[][] { {3,4},{1,2},{2,4},{3,5},{2,5} };
		e = q.findRedundantConnection(edges);
		assertTrue(e[0] == 2 && e[1] == 5);

		edges = new int[][] { {7, 8}, {2, 6}, {2, 8}, {1, 4}, {9, 10}, {1, 7}, {3, 9}, {6, 9}, {3, 5}, {3, 10} };
		e = q.findRedundantConnection(edges);
		assertTrue(e[0] == 3 && e[1] == 10);
		System.out.println("Ok !");
	}

}
