package org.example.my_project.task2Java;

public class main {
    public static void main(String[] args) {
        ToyShop shop = new ToyShop();

        shop.addToy(new Toy(1, "Робот", 1, 40));
        shop.addToy(new Toy(2, "Машина", 1, 30));
        shop.addToy(new Toy(3, "Заяц", 1, 30));

        shop.updateToyWeight(1, 25.0);

        Toy selectedToy = shop.startLottery();
        if (selectedToy != null) {
            System.out.println("Вы выиграли: " + selectedToy.getName());
            shop.saveToyToFile(selectedToy, "winners.txt");
        }
    }
}
