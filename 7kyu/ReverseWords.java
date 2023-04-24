/* Challenge Description:
Complete the function that accepts a string parameter, 
and reverses each word in the string. All spaces in the string 
should be retained.

Examples
"This is an example!" ==> "sihT si na !elpmaxe"
"double  spaces"      ==> "elbuod  secaps"

*/

public class ReverseWords {

  public static String reverseWords(final String original) {
    String result = original;

    if (original.length() > 0) {
      String[] arr = original.split(" ");

      if (arr.length > 0) {
        String reversed = reverseWord(arr[0]);
        result = reversed;

        String or = "";
        for (int i = 1; i < arr.length; i++) {
          or = arr[i];
          result += " ";
          reversed = reverseWord(or);
          result += reversed;
        }
      }
    }
    return result;
  }

  public static String reverseWord(final String original) {
    String result = "";
    if (original.length() > 0) {
      for (int i = original.length() - 1; i >= 0; i--) {
        char c = original.charAt(i);
        result += c;
      }
    }
    return result;
  }
}
