/**
ID: odys.zh1
LANG: JAVA
TASK: frac1
*/
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.PrintWriter;
import java.util.ArrayList;

public class frac1 {

	private static String progId = "frac1";
	private static Integer N;
	private static ArrayList<int[]> ans;

	public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new FileReader(progId + ".in"));
        String lin = br.readLine();
        N = Integer.valueOf(lin);
        br.close();
        ans = new ArrayList<int[]>();
        
        ans.add(new int[] {0, 1});
        dfs(0, 1, 1, 1);
        ans.add(new int[] {1, 1});

        PrintWriter out = new PrintWriter(new BufferedWriter(new FileWriter(progId + ".out")));
        for (int[] nd : ans)
        	out.print(String.format("%d/%d\n", nd[0], nd[1]));
		out.close();
	}

	static void dfs(int ln, int ld, int rn, int rd) {
		int n = ln + rn;
		int d = ld + rd;
		
		if (n > d || d > N)
			return;
		
		dfs(ln, ld, n, d);
		ans.add(new int[] {n, d});
		dfs(n, d, rn, rd);
	}
	
}
