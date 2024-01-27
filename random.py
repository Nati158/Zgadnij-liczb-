import random

def zgadnij_liczbe():
    wylosowana_liczba = random.randint(1, 10)
    
    while True:
        odpowiedz = int(input("Zgadnij liczbę od 1 do 10: "))

        if odpowiedz == wylosowana_liczba:
            print("Brawo! Zgadłeś!")
            break
        else:
            print("Nieprawidłowa liczba. Spróbuj ponownie.")

if __name__ == "__main__":
    zgadnij_liczbe()
