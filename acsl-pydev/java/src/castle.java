/**
ID: odys.zh1
LANG: JAVA
TASK: castle
*/
import java.io.*;

public class castle {
	static final String progId = "castle";

	static final int W = 1;
	static final int Nr = 2;
	static final int E = 4;
	static final int S = 8;

	static class Tile {
		int room = -1;
		int wall = 15;
		int x, y;

		public Tile(int wall, int y, int x) {
			this.room = -1;
			this.y = y;
			this.x = x;
			this.wall = wall;
		}
	}

	
	static Tile[][] castle;
	static int N, M;
	static int[] roomSize; 
	static int maxSize = 0;

	public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new FileReader(progId + ".in"));
        String lin = br.readLine();
        String[] MN = lin.split(" ");
        N = Integer.parseInt(MN[0]);
        M = Integer.parseInt(MN[1]);
        roomSize = new int[M * N];

        castle = new Tile[M][N];
        for (int y = 0; y < M; y++) {
       		lin = br.readLine();
			String[] cells = lin.split(" ");

        	for (int x = 0; x < N; x++) {
        		int wall = Integer.parseInt(cells[x]);
        		castle[y][x] = new Tile(wall, y, x);
        	}
        }
        br.close();

        int nroom = 0;
        
        for (Tile[] row : castle)
        for (Tile t : row) {
        	if (t.room < 0)
        		// find biggest room
        		maxSize = dfs(nroom++, t);
        }

        // look at best that can come of removing an east or north wall
		int maxSpace = 0;
		int mx = 0, my = 0;
		char mc = 'N';
		for(int x = 0; x < N; x++)
		for(int y = M - 1; y >= 0; y--) {
			if(y > 0 && castle[y][x].room != castle[y-1][x].room) {
				int n = roomSize[castle[y][x].room] + roomSize[castle[y-1][x].room];
				if(n > maxSpace) {
					maxSpace = n;
					mx = x;
					my = y;
					mc = 'N';
				}
			}
			if(x + 1 < N && castle[y][x].room != castle[y][x+1].room) {
				int n = roomSize[castle[y][x].room] + roomSize[castle[y][x+1].room];
				if(n > maxSpace) {
					maxSpace = n;
					mx = x;
					my = y;
					mc = 'E';
				}
			}
		}

        PrintWriter out = new PrintWriter(new BufferedWriter(new FileWriter(progId + ".out")));
		out.print(String.format("%d\n", nroom));
		out.print(String.format("%d\n", maxSize));
		out.print(String.format("%d\n", maxSpace));
		out.print(String.format("%d %d %c\n", my+1, mx+1, mc));
		out.close();
	}

	static int dfs(int numb, Tile t) {
		if (t.room >= 0)
			return maxSize;

		// new room
		t.room = numb;
		roomSize[numb] += 1;
		maxSize = Math.max(maxSize, roomSize[numb]);

	    if(t.x > 0 && (t.wall & W) == 0)
	    	dfs(numb, castle[t.y][t.x - 1]);

	    if(t.x + 1 < N && (t.wall & E) == 0)
	    	dfs(numb, castle[t.y][t.x + 1]);

	    if(t.y > 0 && (t.wall & Nr) == 0)
	    	dfs(numb, castle[t.y - 1][t.x]);

	    if(t.y + 1 < M && (t.wall & S) == 0)
	    	dfs(numb, castle[t.y + 1][t.x]);

		return maxSize;
	}
}

