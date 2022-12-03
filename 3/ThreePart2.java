import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

class ThreePart2 {
    public static int getPrio(char c) {
        if (c == Character.toUpperCase(c)) {
            return c - 'A' + 27;
        } else {
            return c - 'a' + 1;
        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line1 = br.readLine();
        String line2 = br.readLine();
        String line3 = br.readLine();
        int total = 0;
        while (line3 != null) {
            char target = 0;
            StringBuilder common2 = new StringBuilder();
            for (char e: line1.toCharArray()) {
                if (line2.indexOf(e) != -1) {
                    common2.append(e);
                }
            }

            for (char e: common2.toString().toCharArray()) {
                if (line3.indexOf(e) != -1) {
                    target = e;
                    break;
                }
            }

            total += getPrio(target);
            System.out.println(common2 + " " + target);
            line1 = br.readLine();
            line2 = br.readLine();
            line3 = br.readLine();
        }

        System.out.println(total);
    }
}