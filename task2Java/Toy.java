package org.example.my_project.task2Java;

public class Toy{
    int id;
    String name;
    int quantity;
    double weight;

    public Toy(int id, String name, int quantity, double weight) {
        this.id = id;
        this.name = name;
        this.quantity = quantity;
        this.weight = weight;
    }

    public int getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    public int getQuantity() {
        return quantity;
    }

    public double getWeight() {
        return this.weight;
    }

    public double setWeight(double weight) {
        return this.weight;
    }
    public void decreaseQuantity(){
        quantity--;
    }
}
