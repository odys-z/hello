package io.oz.hello;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;

import io.odysz.common.Utils;

/**
 * https://github.com/absimas/VideoClipper/blob/master/app/src/main/java/com/simas/vc/background_tasks/FFprobe.java
 * 
 * @author Ody
 *
 */
public class FFProbeWrapper {

	private static native int cFFprobe(String[] args, String outputPath);

	public static void main(String[] args) {

	}

	public synchronized static void parseAttributes(String inputFile) throws Exception {

		Utils.logi(System.getProperty("java.library.path"));
		File file = new File(System.getProperty("java.library.path"));
		String path = file.getAbsolutePath();
		Utils.logi(path);
		System.load(path + "/ffprobe.exe");

		/* Executable call used
			./ffprobe -i 'nature/bee.mp4' \
			-v quiet -print_format json \
			-show_format -show_entries format=duration,size,format_name,format_long_name,filename,nb_streams \
			-show_streams -show_entries stream=codec_name,codec_long_name,codec_type,sample_rate,channels,duration,display_aspect_ratio,width,height,time_base,codec_time_base,r_frame_rate
		*/

		// Create a temporary file to hold the stdout output
		File tmpFile;
		try {
			tmpFile = File.createTempFile("vc-out", null);
			tmpFile.delete();
			tmpFile.createNewFile();
		} catch (IOException e) {
			e.printStackTrace();
			throw new Exception("R.string.tmp_not_created");
		}

		// Create arguments for ffprobe
		final String[] args = new ArgumentBuilder("HELLO")
				.add("-i")
				.addSpaced("%s", inputFile)   // Spaced input file path
				.add("-v quiet -print_format json")     // Output quietly in JSON
						// Format entries to show
				.add("-show_format -show_entries format=%s",
						"format_name")
						// Stream entries to show
				.add("-show_streams -show_entries stream=%s,%s,%s,%s",
						// https://github.com/absimas/VideoClipper/blob/master/app/src/main/res/values/json_strings.xml
						"display_aspect_ratio",
						"width",
						"height",
						"codec_tag")
				.build();

		if (cFFprobe(args, tmpFile.getPath()) != 0) {
			throw new Exception("ffprobe_fail");
		}

		BufferedReader reader = null;
		try {
			// Parse file
			reader = new BufferedReader(new FileReader(tmpFile));
			StringBuilder sb = new StringBuilder();
			String line = reader.readLine();

			while (line != null) {
				sb.append(line);
				sb.append('\n');
				line = reader.readLine();
			}
			String content = sb.toString();

			int firstOpeningBrace = content.indexOf('{');
			int lastClosingBrace = content.lastIndexOf('}');
			if (firstOpeningBrace == -1 || lastClosingBrace == -1) {
				return;
			}
			String json = content.substring(firstOpeningBrace, lastClosingBrace+1);

			Utils.logi(json);
		} catch (IOException e) {
			e.printStackTrace();
			throw new Exception("R.string.ffprobe_fail");
		} finally {
			if (reader != null) {
				try {
					reader.close();
				} catch (IOException e) {
					e.printStackTrace();
				}
			}
		}

		// Delete the tmp file
		tmpFile.delete();
	}
}
