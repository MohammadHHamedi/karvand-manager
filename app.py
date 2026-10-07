import json
import os

DATA_FILE = "data/karvands.json"


def create_data_file():
    if not os.path.exists("data"):
        os.makedirs("data")

    if not os.path.exists(DATA_FILE):
        data = {
            "bootcamp": {
                "name": "Karvand Bootcamp"
            },
            "karvands": []
        }

        with open(DATA_FILE, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)


create_data_file()
def load_data():
    with open(DATA_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def add_karvand(data):
    print("\n--- Add Karvand ---")

    name = input("Enter full name: ")
    email = input("Enter email: ")
    city = input("Enter city: ")
    degree = input("Enter education degree: ")
    field = input("Enter education field: ")

    skills = []

    while True:
        skill_name = input("Enter skill name (or 'done' to finish): ")

        if skill_name.lower() == "done":
            break

        level = input("Enter skill level: ")

        while True:
            try:
                score = int(input("Enter skill score (0-100): "))

                if 0 <= score <= 100:
                    break

                print("Score must be between 0 and 100.")

            except ValueError:
                print("Please enter a number.")

        skills.append({
            "name": skill_name,
            "level": level,
            "score": score
        })

    new_id = 1

    if data["karvands"]:
        new_id = max(karvand["id"] for karvand in data["karvands"]) + 1

    new_karvand = {
        "id": new_id,
        "name": name,
        "email": email,
        "city": city,
        "education": {
            "degree": degree,
            "field": field
        },
        "skills": skills
    }

    data["karvands"].append(new_karvand)

    save_data(data)

    print("Karvand added successfully.")


def show_all_karvands(data):
    print("\n--- All Karvands ---")

    if not data["karvands"]:
        print("No karvands have been registered.")
        return

    for karvand in data["karvands"]:
        print("\n--------------------")
        print("ID:", karvand["id"])
        print("Name:", karvand["name"])
        print("Email:", karvand["email"])
        print("City:", karvand["city"])

        print(
            "Education:",
            karvand["education"]["degree"],
            "-",
            karvand["education"]["field"]
        )

        print("Skills:")

        for skill in karvand["skills"]:
            print(
                "-",
                skill["name"],
                "| Level:",
                skill["level"],
                "| Score:",
                skill["score"]
            )

def search_karvand_by_id(data):
    print("\n--- Search Karvand by ID ---")

    while True:
        try:
            karvand_id = int(input("Enter Karvand ID: "))
            break
        except ValueError:
            print("Please enter a valid number.")

    for karvand in data["karvands"]:
        if karvand["id"] == karvand_id:
            print("\n--------------------")
            print("ID:", karvand["id"])
            print("Name:", karvand["name"])
            print("Email:", karvand["email"])
            print("City:", karvand["city"])

            print(
                "Education:",
                karvand["education"]["degree"],
                "-",
                karvand["education"]["field"]
            )

            print("Skills:")

            for skill in karvand["skills"]:
                print(
                    "-",
                    skill["name"],
                    "| Level:",
                    skill["level"],
                    "| Score:",
                    skill["score"]
                )

            return

    print("Karvand with this ID was not found.")

def search_karvand_by_skill(data):
    print("\n--- Search Karvand by Skill ---")

    skill_name = input("Enter skill name: ").strip().lower()

    found = False

    for karvand in data["karvands"]:
        for skill in karvand["skills"]:
            if skill["name"].lower() == skill_name:
                print("\n--------------------")
                print("ID:", karvand["id"])
                print("Name:", karvand["name"])
                print("Email:", karvand["email"])
                print("City:", karvand["city"])

                print(
                    "Education:",
                    karvand["education"]["degree"],
                    "-",
                    karvand["education"]["field"]
                )

                print("Skill:")
                print(
                    "-",
                    skill["name"],
                    "| Level:",
                    skill["level"],
                    "| Score:",
                    skill["score"]
                )

                found = True

    if not found:
        print("No karvand found with this skill.")

def main():
    create_data_file()
    data = load_data()

    while True:
        print("\n===== Karvand Manager =====")
        print("1. Add Karvand")
        print("2. Show All Karvands")
        print("3. Search by ID")
        print("4. Search by Skill")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_karvand(data)

        elif choice == "2":
            show_all_karvands(data)

        elif choice == "3":
            search_karvand_by_id(data)

        elif choice == "4":
            search_karvand_by_skill(data)

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()