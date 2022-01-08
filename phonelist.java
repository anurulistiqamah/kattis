import java.util.Arrays;
import java.util.Scanner;

public class phonelist {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        for(int i=0; i < n; i++){
            int t = sc.nextInt();
            String phone[] = new String[t];
            for(int j=0; j<t; j++){
                phone[j] = sc.next();
            }
            Arrays.sort(phone);
            boolean cons = true;

            for(int j=1; j<t; j++){
                if(phone[j].startsWith((phone[j-1]))){
                    cons = false;
                    break;
                }
            }
            
            if (cons) System.out.println("YES");
            else System.out.println("NO");
        }
        sc.close();
    }
}