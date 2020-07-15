package io.odysz.hello.jwi;

import java.io.File;
import java.io.IOException;
import java.net.URL;
import java.util.List;

import edu.mit.jwi.Dictionary;
import edu.mit.jwi.IDictionary;
import edu.mit.jwi.item.IIndexWord;
import edu.mit.jwi.item.IWord;
import edu.mit.jwi.item.IWordID;
import edu.mit.jwi.item.POS;

public class App01 {

	public static void main(String[] args) throws IOException {
		// construct the URL to the Wordnet dictionary directory
		// String wnhome = System.getenv( "WNHOME" ) ;
		String wnhome = args[0];
		String path = wnhome + File.separator + "dict-3.1";
		URL url = new URL ( "file", null, path ) ;
		// construct the dictionary object and open it
		IDictionary dict = new Dictionary ( url ) ;
		dict.open () ;
		// look up first sense of the word " dog "
		IIndexWord idxWord = dict.getIndexWord( "dog" , POS.NOUN ) ;
		List<IWordID> wids = idxWord.getWordIDs();
		IWordID wordID = wids.get(0) ;

		IWord word = dict.getWord ( wordID ) ;
		System.out.println ( "Id = " + wordID ) ;
		System.out.println ( "Lemma = " + word.getLemma() ) ;
		System.out.println ( "Gloss = " + word.getSynset().getGloss () ) ;
		
		for (IWord w : word.getSynset().getWords()) {
			System.out.println(w.getLemma());
		}
	}

	IDictionary findeSynset(String word) {
		return null;
	}
}
