package hello;

import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;

public class t1 {

	public static void main(String[] args) {
	}


	// METHOD SIGNATURE BEGINS, THIS METHOD IS REQUIRED
	public List<Integer> cellCompete(int[] states, int days) {
		/* (0) [0] [1] [2] ...          [n - 1] (0)
		 *     x0  x1  x2  x2'          x2''
		 * ix      1   2   3      -3 -2 n - 1
		 */
		int l = states.length;
		List<Integer> x = null;
		for (int d = 1; d <= days; d++) {
			x = new ArrayList<Integer> (4);
			x.add(0 == states[1] ? 0 : 1);
			for (int ix = 1; ix < l - 1; ix++) {
				x.add(states[ix - 1] == states[ix + 1] ? 0 : 1);
				if (x.size() > 3) {
					int s = (int) x.remove(0);
					states[ix - 3] = s;
				}
			}
			x.add(states[l - 2] == 0 ? 0 : 1);

			// states[l - 4] = x.remove(0);
			// states[l - 3] = x.remove(0);
			// states[l - 2] = x.remove(0);
			// states[l - 1] = x.remove(0);
			while (x.size() > 0)
				states[l - x.size()] = x.remove(0);
		}

		// this is not necessary if function signature is redefined
		// equivalent: Arrays.asList(new Integer[0])
		// or Arrays.asList(states) if it's Integer[]
		List<Integer> lst = new ArrayList<Integer>(states.length);
		for (int i : states)
			lst.add(i);

		return lst;
	}
}
