package io.odysz.nlp.wordkeeper;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.util.ArrayList;

import io.odysz.module.rs.AnResultset;
import io.odysz.semantic.DATranscxt;
import io.odysz.semantic.TestRobot;
import io.odysz.semantic.DA.Connects;
import io.odysz.semantics.ISemantext;
import io.odysz.semantics.IUser;
import io.odysz.semantics.SemanticObject;

public class Keeper {
	private static final String wordtbl = "wordfreqEn4";

	/**Load word frequency file into sqlite.db.
	 * Table:<pre>
	CREATE TABLE wordfreqEn4 (
		word TEXT,
		freq NUMBER,
		CONSTRAINT wordfreq_PK PRIMARY KEY (word)
	) ;</pre>
	 * @param wordpath
	 * @param tabl
	 * @param conn
	 * @throws Exception 
	 */
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
	
	public static void installFrequency(String wordpath, String tabl, String conn) throws Exception {
		if (wordpath != null && tabl != null) {
			DATranscxt sctx = new DATranscxt(Connects.defltConn());
			ISemantext dbcontx = null;
			IUser robot = new TestRobot();
			ArrayList<String> sqls = new ArrayList<String>(1);
			sctx.delete(tabl)
				.where("!=", "word", "'hhhhhh'") // fake condition, actually we want to delete all
				.commit(dbcontx, sqls);
			Connects.commit(robot, sqls);
			
			FileInputStream ins = new FileInputStream(wordpath);
			BufferedReader reader = new BufferedReader(new InputStreamReader(ins));
			while (reader.ready()) {
				String lnwf = reader.readLine();
				String[] wf = lnwf.trim().split(" ");

				sqls.clear();
				sctx.insert(tabl)
					.nv("word", wf[0])
					.nv("freq", wf[1])
					.commit(sqls, robot);
				Connects.commit(robot, sqls);
			}
			reader.close();
		}
	}

}
