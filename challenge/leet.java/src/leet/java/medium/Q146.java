package leet.java.medium;

import static org.junit.jupiter.api.Assertions.*;

import java.util.LinkedHashMap;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

public class Q146 {
	static class Node {
		int k;
		int v;
		Node prev;
		Node(int key, int v, Node prev) {
			this.k = key;
			this.v = v;
			this.prev = prev;
		}
	}
	
	static class Bilinst {
		LinkedHashMap<Integer, Node> linkmap;
		Node mru;
		Node lru;
		
		Bilinst(int capacity) {
			linkmap = new LinkedHashMap<Integer, Node>(capacity + 2);
			
			mru = new Node(0, 0, null);
			lru = new Node(0, 0, mru);
		}
	}

	class LRUCache {

	    private int capacity;
		private Bilinst bilinst;

		public LRUCache(int capacity) {
	    	this.capacity = capacity;
	        this.bilinst = new Bilinst(capacity);
	    }
	    
	    public int get(int key) {
	    	Node n = bilinst.linkmap.get(key);
	    	if (n == null)
	    		return -1;
	    	else {
	    		bilinst.linkmap.remove(n.k);
	    		bilinst.nxt.prev = n.prev; // so what's nxt if no LinkedHashMap over ride?
	    		return n.v;
	    	}
	    }
	    
	    public void put(int key, int value) {
	        
	    }
	}

	@BeforeEach
	void setUp() throws Exception {
		// s = new Q012_int2roman_Ranktable();
	}

	
	@Test
	void test() {
		LRUCache c = new LRUCache(2);
		c.put(1, 1);
        assertEquals(1, c.get(1));
	}
}
