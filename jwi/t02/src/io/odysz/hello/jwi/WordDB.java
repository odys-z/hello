package io.odysz.hello.jwi;

import io.odysz.nlp.wordkeeper.Keeper;

public class WordDB {

	public static void main(String[] args) {
		try {
			Keeper.initSqlite("res");
			// Keeper.installFrequency("res/w1068.e-4.word", "wordfreqEn4", "wn-sqlite");
			Keeper.installFrequency("res/w1068.e-6.word", "wordfreqEn6", "wn-sqlite");
		} catch (Exception e) {
			e.printStackTrace();
		}
	}

}
