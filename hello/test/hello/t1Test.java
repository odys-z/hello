package hello;

import static org.junit.jupiter.api.Assertions.*;

import java.util.List;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

class t1Test {

	@BeforeEach
	void setUp() throws Exception {
	}

	@Test
	void testCellCompete() {
		t1 t = new t1();
		List<Integer> s = t.cellCompete(new int[] {1, 1, 0, 1}, 1);
		// 0 1 1 0 1 0
		//   1 1 0 0
		log(s);
	}

	static private void log(List<Integer> s) {
		for (int i : s) {
			System.out.print(i);
			System.out.print(" ");
		}
		
	}

}
