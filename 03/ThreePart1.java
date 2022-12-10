import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;

class ThreePart1 {
    public static int getPrio(char c) {
        if (c == Character.toUpperCase(c)) {
            return c - 'A' + 27;
        } else {
            return c - 'a' + 1;
        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line = br.readLine();
        int total = 0;
        while (line != null) {
            char target = 0;
            String p1 = line.substring(0, (line.length()/2));
            String p2 = line.substring((line.length()/2));
            for (char e: p1.toCharArray()) {
                if (p2.indexOf(e) != -1) {
                    target = e;
                    break;
                }
            }

            total += getPrio(target);

            line = br.readLine();
        }

        System.out.println(total);
    }
}