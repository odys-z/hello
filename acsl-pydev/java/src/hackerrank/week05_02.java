package hackerrank;

import java.util.*;

/**
 * Test Case
 * 2 3 = 1
 * 96 84 = 12
 * 10000 12345 = 5
 * 1000000 999994 = 2
 * 
 * @author Odys Zhou
 *
 */
public class week05_02 {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner scanner = new Scanner(System.in);
        int a = scanner.nextInt();
        int b = scanner.nextInt();
        scanner.close();
        System.out.println(String.format("%d", gcd(a, b)));
    }
    
    static int gcd(int a, int b) {
    	if (a != 0 && b != 0) 
			if (a < b) 
				return gcd(b % a, a);
			else return gcd(a % b, b);
    	else return b < a ? a : b;
    }
}