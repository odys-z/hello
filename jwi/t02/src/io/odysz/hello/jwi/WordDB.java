package io.odysz.hello.jwi;

import io.odysz.nlp.wordkeeper.Keeper;

public class WordDB {

	public static void main(String[] args) {
		try {
			Keeper.initSqlite("res");
		} catch (Exception e) {
			e.printStackTrace();
		}
	}

}
