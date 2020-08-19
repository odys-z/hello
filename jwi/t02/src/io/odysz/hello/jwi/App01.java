package io.odysz.hello.jwi;

import java.io.File;
import java.io.IOException;
import java.net.URL;
import java.util.List;

import edu.mit.jwi.Dictionary;
import edu.mit.jwi.item.IIndexWord;
import edu.mit.jwi.item.ISynsetID;
import edu.mit.jwi.item.IWord;
import edu.mit.jwi.item.IWordID;
import edu.mit.jwi.item.POS;
import edu.mit.jwi.item.Pointer;

public class App01 {

	private static Dictionary dict;

	public static void main(String[] args) throws IOException {
		// construct the URL to the Wordnet dictionary directory
		// String wnhome = System.getenv( "WNHOME" ) ;
		String wnhome = args[0];
		String path = wnhome + File.separator + "dict-3.1";
		URL url = new URL ( "file", null, path ) ;
		// construct the dictionary object and open it
		dict = new Dictionary ( url ) ;
		dict.open () ;
		for (int wx = 1; wx < args.length; wx++)
			showSense0(args[wx]);
		dict.close();
	}

	/**Look up first sense of the word.
	 * @param w0
	 */
	private static void showSense0(String w0) {
		IIndexWord idxWord = dict.getIndexWord( w0 , POS.NOUN ) ;
		if (idxWord == null) return;
		List<IWordID> wids = idxWord.getWordIDs();
		IWordID wordID = wids.get(0) ;

		IWord word = dict.getWord ( wordID ) ;
		System.out.println ( "Id = " + wordID ) ;
		System.out.println ( "Lemma = " + word.getLemma() ) ;
		System.out.println ( "Gloss = " + word.getSynset().getGloss () ) ;
		
		System.out.println ( "Hypernyms = " ) ;
		List<ISynsetID> hypers = word.getSynset().getRelatedSynsets(Pointer.HYPERNYM);
		for (ISynsetID h : hypers) {
			List<IWord> w = dict.getSynset(h).getWords();
			for (IWord hw : w) 
				System.out.print("\t" + hw.getLemma());
		}

		List<IWord> synset = word.getSynset().getWords();
		System.out.println(String.format(
				"\n------------------- %s %s synonyms  -----------------",
				w0, synset.size() ));
		for (IWord w : synset) {
			System.out.print(w.getLemma());
			System.out.print("\t");
		}
		System.out.println ( "\n" ) ;
	}

}
