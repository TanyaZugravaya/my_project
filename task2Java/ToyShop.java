package org.example.my_project.task2Java;

import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class ToyShop {
    List<Toy> toys;

    public ToyShop() {
        this.toys = new ArrayList<>();
    }

    public void addToy(Toy toy) {
        toys.add(toy);
    }

    public void updateToyWeight(int toyId, double newWeight) {
        for (Toy toy : toys) {
            if (toy.getId() == toyId) {
                toy.setWeight(newWeight);
                break;
            }
        }
    }

    public Toy startLottery() {
        double totalWeight = toys.stream().mapToDouble(Toy::getWeight).sum();
        if (totalWeight <= 0) {
            System.out.println("Нет доступных игрушек для розыгрыша.");
            return null;
        }

        double randomNumber = Math.random() * totalWeight;
        double currentWeight = 0;

        for (Toy toy : toys) {
            currentWeight += toy.getWeight();
            if (randomNumber <= currentWeight) {
                Toy selectedToy = new Toy(toy.getId(), toy.getName(), 1, toy.getWeight());
                toy.decreaseQuantity();
                return selectedToy;
            }
        }
        return null;
    }

    public void saveToyToFile(Toy toy, String filename) {
        try (FileWriter writer = new FileWriter(filename, true)) {
            writer.write(toy.toString() + "\n");
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
