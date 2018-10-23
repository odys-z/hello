package io.oz.hello.mvn;

import java.lang.reflect.Type;
import java.util.ArrayList;

import com.google.gson.Gson;
import com.google.gson.reflect.TypeToken;

public class HelloMevan {

	public static void main(String[] args) {
		ZSingleton.err("Starting");
		
		Gson gson = new Gson();
		String json = "{\"a\": \"10\"}";

		Type dsType = new TypeToken<ArrayList<StubRec>>() {}.getType();
		gson.fromJson(json, dsType);
	}

}
