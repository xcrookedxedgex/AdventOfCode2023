package countlettersandnumberstest;

import countlettersandnumbers.Main;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

class MainTest {

    static String inputOne = """
            1abc2
            pqr3stu8vwx
            a1b2c3d4e5f
            treb7uchet
            """;

    static String inputTwo = """
            two1nine
            eightwothree
            abcone2threexyz
            xtwone3four
            4nineeightseven2
            zoneight234
            7pqrstsixteen
            """;

    @BeforeEach

    @Test
    void testMethod() {
        int result = Main.firstProcessing(inputOne, true);
        assertEquals(142, result);
    }

    @Test
    void testMethod2() {
        int result = Main.firstProcessing(inputTwo, false);
        assertEquals(281, result);
    }
}
