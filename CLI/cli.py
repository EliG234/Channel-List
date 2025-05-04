from stage_management import MicInventory


def send_update(message):
    print(f"[UPDATE SENT]: {message}")

def main_menu():
    print("\nWelcome to Channel List Manager!")
    print("Please select user type:")
    print("1. FOH")
    print("2. Stage Manager")
    print("3. Exit")
    return input("Enter # of choice: ").strip()


def user_menu():
    print("Main Menu:")
    print("1. Mic Inventory")
    print("2. Stagebox Manager")
    print("3. Channel Manager")
    print("4. View Setup")
    print("5. Save Show")
    print("6. Load Show")
    print("7. Exit")
    return input("Enter # of choice: ").strip()

def mic_inventory_menu():
    print("\nMic Inventory")
    print("1.View Mic List")
    print("2. Add Mic")
    print("3. Remove Mic")
    print("4. Back")
    return input("Enter # of choice: ").strip()

def stagebox_menu():
    print("\nStagebox Manager")
    print("1. View Stagebox List")
    print("2. Add Stagebox")
    print("3. Edit Stagebox")
    print("4. Back")
    return input("Enter # of choice: ").strip()

def channel_menu():
    print("\nChannel Menu")
    print("1. View Channel List")
    print("2. Add Input")
    print("3. Add output")
    print("4. Edit Channel")
    print("5. Back")
    return input("Enter # of choice: ").strip()

def run_cli():
    mic_inventory = MicInventory()

    while True:
        user = main_menu()
        if user == "1" or user == "2":
            break
        elif user == "3":
            print("Goodbye!")
            return
        else:
            print(" Invalid choice. Please try again...")

    while True:
        choice = user_menu()

        if choice == "1":
            while True:
                mic_choice = mic_inventory_menu()
                if mic_choice == "1":
                    print("Mic Inventory:")
                    for model, count in mic_inventory.mics.items():
                        print(f"{model}: {count}")
                        break
                    else:
                        print("No mics in inventory")

                elif mic_choice == "2":
                    model = input("Enter mic model to add: ").strip()
                    try:
                        count = int(input("Enter Quantity: "))
                        if model in mic_inventory.mics:
                            mic_inventory.mics[model] += count
                        else:
                            mic_inventory.mics[model] = count
                        send_update(f"{count} x {model} added to inventory")
                    except ValueError:
                        print("Invalid quantity.")

                elif mic_choice == "3":
                    model = input("Enter mic model to remove: ").strip()
                    if model in mic_inventory.mics:
                        try:
                            count = int(input("Enter Quantity to remove: "))
                            if mic_inventory.mics[model] >= count:
                                mic_inventory.mics[model] -= count
                                if mic_inventory.mics[model] == 0:
                                    del mic_inventory.mics[model]
                                send_update(f"{count} x {model} removed from inventory")
                            else:
                                print("Cannot remove more mics than available.")
                        except ValueError:
                            print("Invalid quantity. Try again...")
                    else:
                        print("Mic model not found in inventory.")

                elif mic_choice == "4":
                    break
                else:
                    print(" Invalid choice. Please try again...")

        elif choice == "2":
            while True:
                sb_choice = stagebox_menu()
                if sb_choice == "1":
                    # Stagebox List
                    pass
                elif sb_choice == "2":
                    sb_name = input("Enter stagebox name: ").strip()
                    # Add stagebox name logic
                    send_update(f"Stagebox '{sb_name}' added")
                elif sb_choice == "3":
                    # Edit stagebox
                    pass
                elif sb_choice == "4":
                    break
                else:
                    print(" Invalid choice. Please try again...")

        elif choice == "3":
            while True:
                ch_choice = channel_menu()
                if ch_choice == "1":
                    # List channels
                    pass
                elif ch_choice == "2":
                    # Add input logic
                    pass
                elif ch_choice == "3":
                    # Add output logic
                    pass
                elif ch_choice == "4":
                    # Edit channel logic
                    pass
                elif ch_choice == "5":
                    break
                else:
                    print(" Invalid choice. Please try again...")

        elif choice == "4":
            # view current setup logic
            pass

        elif choice == "5":
            # Save show logic
            send_update("Show saved")
        elif choice == "6":
            # Load show logic
            send_update("Show loaded")
        elif choice == "7":
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please try again...")

if __name__ == "__main__":
    run_cli()




