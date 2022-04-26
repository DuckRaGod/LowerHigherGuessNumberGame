#include <iostream>
#include <random>

int main(){
    std::random_device rd;  //  Yes?
    std::mt19937 gen(rd());  // WHAT IS IT? I dont care.
    std::uniform_int_distribution<> dist(0,1000); //    Nice!
    // dist(gen)

    std::cout << "Hello to guess the number cpp edition!\n";
    int guessNumber;
    int realNumber;
    int triesNeeded = 0;

    realNumber = dist(gen);

    while(true){
        std::cout << "\nEnter guess: ";
        std::cin >> guessNumber;

        if(guessNumber < realNumber){
            std::cout << "Higher! \n";
            triesNeeded++;
        }else if(guessNumber > realNumber){
            std::cout << "Lower! \n";
            triesNeeded++;
        }else{
            system("cls");
            std::cout << "Correct! \n";
            std::cout << "Tries needed to guess: " << triesNeeded;
            triesNeeded = 0;
            realNumber = dist(gen);
        }
    }
    return 0;
}