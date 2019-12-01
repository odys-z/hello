package leetcode.tree.q012_int2roman;

/**
 * 12. Integer to Roman
 * https://leetcode.com/problems/integer-to-roman/submissions/
 * 
 * This takes 4ms, the same of python takes 48ms.
 * @author odys-z@github.com
 *
 */
public class SolutionRanktable extends Solution {
	static String[][] rroms = new String[][] {
		new String[] {"M", "MM", "MMM"},
        new String[] {"C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"},
        new String[] {"X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"},
        new String[] {"I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"}
        };

    public String intToRoman(int num) {
		StringBuffer romans = new StringBuffer();
		int w = num / 1000;
		if (w > 0)
			romans.append(rroms[0][w - 1]);
		num %= 1000;

		w = num / 100;
		if (w > 0)
			romans.append(rroms[1][w - 1]);
		num %= 100;

		w = num / 10;
		if (w > 0)
			romans.append(rroms[2][w - 1]);
		num %= 10;

		if (num > 0)
			romans.append(rroms[3][num - 1]);

		return romans.toString();
    }

}
