import java.io.*;

public class CastleGready {
	static class Tile {
		int room = -1;
		int wall = 15;
		int x, y;

		public Tile(int wall2, int y, int x) {
			this.room = -1;
			this.y = y;
			this.x = x;
		}
	}

	static final String progId = "castle";
	
	static Tile[][] castle;
	static int N, M;
	static int[] roomSize; 
	static int maxSize = 0;

	public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new FileReader(progId + ".in"));
        PrintWriter out = new PrintWriter(new BufferedWriter(new FileWriter(progId + ".out")));
        String lin = br.readLine();
        String[] MN = lin.split(" ");
        M = Integer.parseInt(MN[0]);
        N = Integer.parseInt(MN[1]);
        roomSize = new int[M * N];

        castle = new Tile[M][N];
        for (int y = 0; y < M; y++) {
       		lin = br.readLine();
			String[] cells = lin.split(" ");
			Tile[] row = new Tile[cells.length];

        	for (int x = 0; x < N; x++) {
        		int wall = Integer.parseInt(cells[x]);
        		row[x] = new Tile(wall, y, x);
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

        int maxSapce = 0;


	// look at best that can come of removing an east or north wall
		int m = 0;
		int mx = 0, my = 0;
		char mc = 'N';
		for(int x = 0; x < N; x++)
		for(int y = M - 1; y >= 0; y--) {
			if(y > 0 && castle[x][y].room != castle[x][y-1].room) {
				int n = roomSize[castle[x][y].room] + roomSize[castle[x][y-1].room];
				if(n > m) {
					m = n;
					mx = x;
					my = y;
					mc = 'N';
				}
			}
			if(x + 1 < N && castle[x][y].room != castle[x+1][y].room) {
				int n = roomSize[castle[x][y].room] + roomSize[castle[x+1][y].room];
				if(n > m) {
					m = n;
					mx = x;
					my = y;
					mc = 'E';
				}
			}
		}

		out.print(String.format("%d\n", nroom));
		out.print(String.format("%d\n", maxSize));
		out.print(String.format("%d\n", m));
		out.print(String.format("%d %d %c\n", my+1, mx+1, mc));
	}

	static int dfs(int numb, Tile t) {
		
		return maxSize;
	}
}

