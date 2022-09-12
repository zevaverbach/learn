public class LargerDemo {
  public static int larger(int x, int y) {
    if (x > y) {
      return x;
    }
    return y;
  }

  public static double larger(double x, double y) {
    if (x > y) {
      return x;
    }
    return y;
  }

  public static String larger(String x, String y) {
    if (x.length() > y.length()) {
      return x;
    }
    return y;
  }

  public static void main(String[] args) {
    System.out.println(larger(5, 10));
    System.out.println(larger(5.3, 10.02320));
    System.out.println(larger("hi", "bye"));
  }
}
