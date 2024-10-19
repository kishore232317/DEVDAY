import java.util.Scanner;

public class PalindromeChecker {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Prompt user for input
        System.out.print("Enter a string: ");
        String input = scanner.nextLine();

        // Remove spaces and convert to lowercase for a case-insensitive check
        String sanitizedInput = input.replaceAll("\\s+", "").toLowerCase();

        // Check if the input is a palindrome
        if (isPalindrome(sanitizedInput)) {
            System.out.println("\"" + input + "\" is a palindrome.");
        } else {
            System.out.println("\"" + input + "\" is not a palindrome.");
        }

        scanner.close(); // Close the scanner
    }

    // Function to check if a string is a palindrome
    public static boolean isPalindrome(String str) {
        int left = 0;
        int right = str.length() - 1;

        while (left < right) {
            if (str.charAt(left) != str.charAt(right)) {
                return false; // Characters do not match
            }
            left++;
            right--;
        }
        return true; // All characters matched
    }
}
