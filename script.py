class Human:
    def __init__(self, name, surname):
        self.name = name;
        self.surname = surname;

class Employer(Human):
    def __init__(self, name, surname):
        super().__init__(name, surname);

class Engineer(Employer):
    def __init__(self, name, surname):
        super().__init__(name, surname);

class Manager(Employer):
    def __init__(self, name, surname):
        super().__init__(name, surname);
        self.engineers = [];

    def hire_engineer(self):
        quest = input('Do you want to hire an engineer? (yes/no): ');
        
        if (quest.lower() == 'yes'):
            qname = input('Please write the name and surname: ');
            name, surname = qname.split();
            engineer = Engineer(name, surname);
            self.engineers.append(engineer);
            print(f'{engineer.name} {engineer.surname} has been hired.');
        
    def fire_engineer(self):
        fquest = input('Do you want to fire an engineer? (yes/no): ');
        if (fquest.lower() == 'yes'):
            fname = input('Please write the name and surname: ');
            name, surname = fname.split();
            
            for engineer in self.engineers:
                if (engineer.name == name and engineer.surname == surname):
                    self.engineers.remove(engineer);
                    print(f'{engineer.name} {engineer.surname} has been fired.');
                    break;
            else:
                print(f"No engineer with the name {name} {surname} found.");

        elif (fquest.lower() == 'no'):
            pass;
        
    def list_engineers(self):
        print('Engineers in the team:');
        for engineer in self.engineers:
            print(f'{engineer.name} {engineer.surname}');

def main():
    manager = Manager('Tigran', 'Barseghyan');

    engineers = [
        Engineer('Lida', 'Karapetyan'),
        Engineer('Vera', 'Sahakyan'),
        Engineer('Ani', 'Araqelyan'),
        Engineer('Mane', 'Melikyan'),
        Engineer('Gurgen', 'Sargsyan'),
        Engineer('Meline', 'Vardanyan'),
        Engineer('Bella', 'Manukyan'),
        Engineer('Anna', 'Muradyan'),
        Engineer('Ani', 'Kirakosyan'),
        Engineer('Mane', 'Margaryan'),
    ]

    for engineer in engineers:
        manager.engineers.append(engineer);

    while (True):
        print("\nOptions:");
        print("1. Hire an engineer");
        print("2. Fire an engineer");
        print("3. List engineers");
        print("4. Exit");
        
        choice = input("Enter your choice (1/2/3/4): ");
        
        if (choice == '1'):
            manager.hire_engineer();
        elif (choice == '2'):
            manager.fire_engineer();
        elif (choice == '3'):
            manager.list_engineers();
        elif (choice == '4'):
            break;

if __name__ == '__main__':
    main();

