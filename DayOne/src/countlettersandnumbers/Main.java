package countlettersandnumbers;


import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.HashMap;
import java.util.Map;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Main {

    public static void main(String [] args) throws IOException {
        String input = new String(Files.readAllBytes(Paths.get("resources/input/input.txt")));
        int result = firstProcessing(input, true);
        int resultTwo = firstProcessing(input, false);
        System.out.printf("VALUE: %s%n", result);
        System.out.printf("VALUE: %s%n", resultTwo);
    }

    public static int firstProcessing(String input, boolean first) {
        int result = 0;
        String[] inputArray = input.split("\\n");
        String patternString = first ? "\\d" : "(?=(\\d|zero|one|two|three|four|five|six|seven|eight|nine))";
        int group = first ? 0 : 1; //for the second processing Matcher.group() would contain an empty string so we need Matcher.group(1)
        Pattern pattern = Pattern.compile(patternString);
        for(String inputString : inputArray) {
            StringBuilder numberStringBuilder = new StringBuilder();
            Matcher matcher = pattern.matcher(inputString);
            while(matcher.find()) {
                numberStringBuilder.append(matcher.group(group));
            }
            String str = numberStringBuilder.toString();
            str = replaceNumberWordsWithValues(str);
            String resultString = String.valueOf(str.charAt(0)) + String.valueOf(str.charAt(str.length() - 1));
            result += Integer.parseInt(resultString);
        }
        return result;
    }

    private static String replaceNumberWordsWithValues(String str) {
        Map<String, Integer> numberLiteralMap = createNumberLiteralMap();
        for(Map.Entry<String, Integer> entry : numberLiteralMap.entrySet()){
            if(str.contains(entry.getKey())) {
                str = str.replace(entry.getKey(), String.valueOf(entry.getValue()));
            }
        }
        return str;
    }

    private static Map<String, Integer> createNumberLiteralMap() {
        Map<String, Integer> map = new HashMap<>();
        map.put("one", 1);
        map.put("two", 2);
        map.put("three", 3);
        map.put("four", 4);
        map.put("five", 5);
        map.put("six", 6);
        map.put("seven", 7);
        map.put("eight", 8);
        map.put("nine", 9);
        return map;
    }

}
