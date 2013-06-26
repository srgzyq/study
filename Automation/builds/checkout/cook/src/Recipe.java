import java.util.ArrayList;
import java.util.Iterator;

public class Recipe {
    protected String name;
    protected ArrayList ingredients;

    public Recipe() {
        name = "";
        ingredients = new ArrayList();
    }

    public Recipe(Recipe another) {
        name = another.name;
        ingredients = new ArrayList(another.ingredients);
    }

    public void setName(String aName) {
        name = aName;
    }

    public String getName() {
        return name;
    }

    public void addIngredient(String aThing) {
        ingredients.add(aThing);
    }

    public Iterator getIngredients() {
        return ingredients.iterator();
    }

    public int getNumIngredients() {
        return ingredients.size();
    }
}
