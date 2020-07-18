package io.odysz.nlp.wordkeeper;

import java.util.HashMap;

import io.odysz.module.rs.AnResultset;
import io.odysz.semantic.DATranscxt;
import io.odysz.semantic.TestRobot;
import io.odysz.semantic.DA.Connects;
import io.odysz.semantics.IUser;
import io.odysz.semantics.SemanticObject;

public class Keeper {
	private static final String wordtbl = "wordfreqEn4";

	static HashMap<String, Object> conns;

	/**Load word file into sqlite.db.
	 * @param wordpath
	 * @param conn
	 */
	public static void loadFrequency(String wordpath, String conn) {
		
	}
	
	public static void initSqlite(String xmlDir) throws Exception {
		Connects.init(xmlDir);
		DATranscxt sctx = new DATranscxt(Connects.defltConn());
		IUser jrobot = new TestRobot();
		SemanticObject s = sctx.select(wordtbl, "w")
				.col("word")
				.col("freq")
				.where_("=", "w.word", "the")
				.rs(sctx.instancontxt(sctx.basiconnId(), jrobot));
			
			AnResultset rs = (AnResultset) s.rs(0);
			rs.printSomeData(false, 1, "word", "freq");
	}
}
