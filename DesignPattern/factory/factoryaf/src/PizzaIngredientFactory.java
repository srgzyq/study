public interface PizzaIngredientFactory {
    
    // 每个原料都有一个对应的方法创建
    public Dough createDough();
    public Sauce createSauce();
    public Cheese createCheese();
    public Veggies[] createVeggies();
    public Pepperoni createPepperoni();
    public Clams createClam();
}
