import java.time.Duration;
import java.time.Instant;

public class Main {
    public static void n1(int n) {
        for (int i = 0; i < n; i++) {
            System.out.println("n1 : print " + n);
        }
    }

    public static void n2(int n) {
        int count = 1;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                System.out.println("n2 : print " + count);
                count++;
            }
        }
    }

    public static void n3(int n) {
        int count = 1;
        for (int a = 0; a < n; a++) {
            for (int b = 0; b < n; b++) {
                for (int c = 0; c < n; c++) {
                    System.out.println("n3 : print " + count);
                    count++;
                }
            }
        }
    }

    public static void n4(int n) {
        int count = 1;
        for (int a = 0; a < n; a++) {
            for (int b = 0; b < n; b++) {
                for (int c = 0; c < n; c++) {
                    for (int d = 0; d < n; d++) {
                        System.out.println("n4 : print " + count);
                        count++;
                    }
                }
            }
        }
    }

    public static void n5(int n) {
        int count = 1;
        for (int a = 0; a < n; a++) {
            for (int b = 0; b < n; b++) {
                for (int c = 0; c < n; c++) {
                    for (int d = 0; d < n; d++) {
                        for (int e = 0; e < n; e++) {
                            System.out.println("n5 : print " + count);
                            count++;
                        }
                    }
                }
            }
        }
    }

    public static void timeAndRun(Runnable func, String funcName, int iterations) {
        Instant start = Instant.now(); // Start the timer

        for (int i = 0; i < iterations; i++) func.run();
        
        Instant end = Instant.now(); // End the timer
        
        System.out.print("\033[H\033[2J"); // Clear console
        System.out.flush();
        System.out.printf("Time taken to run %d iteration(s) of %s: %.10f seconds%n",
                iterations, funcName, Duration.between(start, end).toMillis() / 1000.0);
    }

    public static void main(String[] args) {
        timeAndRun(() -> n3(10), "n3", 10);
    }
}
