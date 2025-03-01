import random

def coin_toss():
    return random.choice(["Heads", "Tails"])

def multiple_tosses(num_flips):
    heads_count = 0
    tails_count = 0
    
    for _ in range(num_flips):
        result = coin_toss()
        print(result)
        if result == "Heads":
            heads_count += 1
        else:
            tails_count += 1
    
    total_flips = heads_count + tails_count
    print("\nResults:")
    print(f"Heads: {heads_count} ({(heads_count / total_flips) * 100:.2f}%)")
    print(f"Tails: {tails_count} ({(tails_count / total_flips) * 100:.2f}%)")

def main():
    while True:
        try:
            num_flips = int(input("Enter the number of coin flips: "))
            if num_flips <= 0:
                print("Please enter a positive number.")
                continue
            multiple_tosses(num_flips)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue
        
        choice = input("Do you want to flip again? (yes/no): ").strip().lower()
        if choice != "yes":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
