public class SingletonClass {
    private static SingletonClass uniqueInstance;

    private SingletonClass() {}

    public static SingletonClass getInstance() {
        if(uniqueInstance == null) {
            uniqueInstance = new SingletonClass();
        }
        return uniqueInstance;
    }
}
