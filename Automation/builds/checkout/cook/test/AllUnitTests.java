import junit.framework.*;

public class AllUnitTests {

    public static Test suite() {

        TestSuite suite = new TestSuite("Cook Tests");
        suite.addTestSuite(RecipeTest.class);
        return suite;
    }

    public static void main(String[] args) {
        junit.textui.TestRunner.run(suite());
    }
}

