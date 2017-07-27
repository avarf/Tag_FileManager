package tag_file_manager;

import java.util.ArrayList;
import java.util.HashMap;

public class main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		System.out.println("Hello from eclipse");
		
		HashMap<String, ArrayList<String>> tag_table = new HashMap<String, ArrayList<String>>();
		ArrayList<String> tag_1_files = new ArrayList<String>();
		ArrayList<String> tag_2_files = new ArrayList<String>();
		
		ArrayList<String> queryList = new ArrayList<String>();
		
		tag_1_files.add("pdf1");
		tag_1_files.add("music_11");
		
		tag_2_files.add("book");
		tag_2_files.add("EBI");
		tag_2_files.add("code_1");
		
		tag_table.put("general_tag", tag_1_files);
		tag_table.put("names", tag_2_files);
		
		queryList = tag_table.get("names");
		System.out.println(queryList);
		System.out.println(queryList.get(1));
	}

}
