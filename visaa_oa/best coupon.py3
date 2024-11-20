import java.io.*;
import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double X = scanner.nextDouble();
        double discount1 = 0.10 * X; 
        double discount2 = 100;      
        double maxDiscount = Math.max(discount1, discount2);
        double finalAmount = X - maxDiscount;
        System.out.println((int)finalAmount); 
        scanner.close();
    }
}
