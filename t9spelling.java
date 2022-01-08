import java.util.HashMap;
import java.util.Scanner;

public class t9spelling {
    public static void main(String[] args) {
        HashMap<Character, String> t9 = new HashMap<Character, String>();
        t9.put(' ', "0");
        t9.put('a', "2");
        t9.put('b', "22");
        t9.put('c', "222");
        t9.put('d', "3");
        t9.put('e', "33");
        t9.put('f', "333");
        t9.put('g', "4");
        t9.put('h', "44");
        t9.put('i', "444");
        t9.put('j', "5");
        t9.put('k', "55");
        t9.put('l', "555");
        t9.put('m', "6");
        t9.put('n', "66");
        t9.put('o', "666");
        t9.put('p', "7");
        t9.put('q', "77");
        t9.put('r', "777");
        t9.put('s', "7777");
        t9.put('t', "8");
        t9.put('u', "88");
        t9.put('v', "888");
        t9.put('w', "9");
        t9.put('x', "99");
        t9.put('y', "999");
        t9.put('z', "9999");


        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        sc.nextLine();
        
        for(int i = 1; i <= n; i++){
            String word = sc.nextLine();
            String output = "";
            
            for (int j = 0; j < word.length(); j++) {
                if(!output.isEmpty() && output.charAt(output.length()-1) == t9.get(word.charAt(j)).charAt(0))
                    output += " ";
                
                output += t9.get(word.charAt(j));
            }
            System.out.printf("Case #%d: %s%n", i, output);
        }
        sc.close();
    }
}
