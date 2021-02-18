package leet.java.medium;

import static org.junit.jupiter.api.Assertions.*;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;


public class Q797Test {
	@BeforeEach
	void setUp() throws Exception {
	}

	
	@SuppressWarnings("serial")
	@Test
	void test() {
        Q797 q = new Q797();

		List<List<Integer>> r = q.allPathsSourceTarget(new int[][] {
			new int[] {1, 2}, new int[] {3}, new int[] {3}, new int[] {}
		});
		assertTrue(r.size() == 2 && r.containsAll(new ArrayList<List<Integer>>() {
			{ Arrays.asList(0, 1, 3);
			  Arrays.asList(0, 2, 3);
			}
		}));
		
		r = q.allPathsSourceTarget(new int[][] {
			new int[] {1, 2, 3}, new int[] {2}, new int[] {3}, new int[] {}
		});
		assertTrue(r.size() == 3 && r.containsAll(new ArrayList<List<Integer>>() {
			{ Arrays.asList(0, 1, 2, 3);
			  Arrays.asList(0, 2, 3);
			  Arrays.asList(0, 3);
			}
		}));

		r = q.allPathsSourceTarget(new int[][] {
			new int[] {2}, new int[] {3}, new int[] {1}, new int[] {}
		});
		assertTrue(r.size() == 1 && r.containsAll(new ArrayList<List<Integer>>() {
			{ Arrays.asList(0, 2, 1, 3);
			}
		}));
		/* Test case TODO
		assertCountEqual([[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]],
						   s.allPathsSourceTarget([[4,3,1],[3,2,4],[3],[4],[]]));
		assertCountEqual([[0,1,2,3],[0,2,3],[0,3]],
						   s.allPathsSourceTarget([[1,2,3],[2],[3],[]]));
		assertCountEqual([[0, 1]], s.allPathsSourceTarget([[1],[]]));
		assertCountEqual([[0,1,2,3],[0,2,3],[0,3]], s.allPathsSourceTarget([[1,2,3],[2],[3],[]]));
		assertCountEqual([[0,1,2,3],[0,3]], s.allPathsSourceTarget([[1,3],[2],[3],[]]));
		*/
	}
}
