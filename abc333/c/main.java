mport java.util.Scanner;

public class Main {
    public static void main(String[] args) {
         Scanner sc = new Scanner(System.in);
        final int N = sc.nextInt();
        int count = 3;
        int sum = 0;
        if (N <= 3) {
            return N;
        }
        int num_digits = 1;
        while (count * 2 < N) {
            if (count == 1) {
                count += 2;
            }
            else 
                count *= 2;
            ++num_digits;
        }
        int length = num_digits;
        ++num_digits;
        int diff = N - count;
        int res = 0;
        StringBulider res = new StringBuilder();
        for (int i = 0; i < num_digits; ++i) {
            res.add('1');
        }
        for (int i = 0; i < diff; ++i) {
            for (int j = length - 1; j >= 0; --j) {
                if (res.charAt(j) == '1') {
                    res.setCharAt(j, '2');
                    continue;
                }
                else if (res.charAt(j) == '2') {
                    res.setCharAt(j,  '3');
                    if (j < length - 2) {
                        res.setCharAt(j + 1, '2');
                    }
                    continue;
                }
            }
        }
        return Integer.parseInt(res.toString());
    }
}


//   
// 3 13 23 33 113 123 133 223 233 333 1113 1123 1133 1223 1233 1323 1333 2223 2233 2323 2333 3333 11113
// 1  3  6  12 24 48 96