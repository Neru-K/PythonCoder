import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
         Scanner sc = new Scanner(System.in);
        final int N = sc.nextInt();
        final int M = sc.nextInt();

        final int total_len = N + M;
        String[] prefix = new String[N];
        String[] suffix = new String[M];
      	for(int i = 0; i < N; i++) {
      		prefix[i] = sc.next();
      	}
        for (int i = 0; i < M; ++i) {
            suffix[i] = sc.next();
        }
        int res = 0;
        for (var word : prefix) {
            for (var suffix_word : suffix) {
                if (word.substring(3).equals(suffix_word)) {
                    ++res;
                    break;
                }
            }
        }
        System.out.println(res);
    }
}

