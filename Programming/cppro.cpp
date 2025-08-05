#include <iostream>

class Employee {

public:
    std::string name;
    int age;

    void sayHello(){
        std::cout << "Hello, I am " << name << " My age is: " << age << std::endl;
    }

    Employee(std::string n, int a){
        name = n;
        age = a;
    }
};


int main(int ags, char *args[]){
    std::cout << "hello, world" << std::endl;

    int age = 7;
    if (age < 18){
        std::cout << "you are young " << age << std::endl;
    } else {
        std::cout << "you are older" << age << std::endl;
    }

    int number = 3;

    int* day = &number;

    switch (*day){
        case 1:
            std::cout << "The day is moday" << std::endl; break;

        case 2:
            std::cout << "The day is tuesday" << std::endl; break;

        case 3:
            std::cout <<"The day is wednesday" << std::endl; break;

        case 4:
           std::cout << "The day is thusday" << std::endl; break;

        case 5:
            std::cout <<"The day is friday" << std::endl; break;

        case 6:
            std::cout << "The day is saturday" << std::endl; break;

        case 7:
            std::cout <<"The day is sunday" << std::endl; break;

        default:
            std::cout << "The day is invalid ?!" << std::endl; break;
    }

    Employee e1("John Doe", 43);
    Employee e2("Mark Kent", 53);

    e1.sayHello();
    e2.sayHello();

    return 0;
}