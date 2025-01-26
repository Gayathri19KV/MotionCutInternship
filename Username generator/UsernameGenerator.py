import random
import string

def create_username(descriptors, objects, add_numbers, add_specials, max_length):
    # Generates a random username based on user preferences.
    descriptor = random.choice(descriptors)
    obj = random.choice(objects)

    username = descriptor + obj

    if add_numbers:
        username += str(random.randint(0, 999))

    if add_specials:
        username += random.choice(string.punctuation)

    if max_length:
        username = username[:max_length]

    return username

def save_names_to_file(name_list, file_name="generated_usernames.txt"):
    # Saves the generated usernames to a file.
    with open(file_name, "w") as file:
        file.write("\n".join(name_list))
    print(f"Usernames saved to {file_name}")

def main():
    print("Welcome to the Random Username Creator!")

    # Predefined lists of descriptors and objects
    descriptors = ["Dynamic", "Clever", "Speedy", "Jolly", "Valiant", "Radiant", "Dreamy", "Fierce"]
    objects = ["Panther", "Hawk", "Falcon", "Sorcerer", "Phoenix", "Warrior", "Sailor", "Barracuda"]

    # User preferences
    add_numbers = input("Include numbers in usernames? (yes/no): ").strip().lower() == "yes"
    add_specials = input("Include special characters in usernames? (yes/no): ").strip().lower() == "yes"

    try:
        max_length = int(input("Set a maximum length for usernames (0 for no limit): ").strip())
        max_length = max_length if max_length > 0 else None
    except ValueError:
        print("Invalid input for length. Using no limit.")
        max_length = None

    try:
        count = int(input("How many usernames would you like to generate? ").strip())
    except ValueError:
        print("Invalid number of usernames. Generating 10 by default.")
        count = 10

    # Generate usernames
    generated_names = [
        create_username(descriptors, objects, add_numbers, add_specials, max_length)
        for _ in range(count)
    ]

    # Display usernames
    print("\nGenerated Usernames:")
    for name in generated_names:
        print(name)

    # Save to file
    save_to_file = input("Would you like to save these usernames to a file? (yes/no): ").strip().lower()
    if save_to_file == "yes":
        save_names_to_file(generated_names)

if __name__ == "__main__":
    main()
