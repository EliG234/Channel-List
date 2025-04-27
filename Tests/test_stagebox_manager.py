from Inventory import StageBoxManager

def test_stagebox_manager():
    # Step 1: Create a StageBoxManager instance
    stagebox_manager = StageBoxManager()

    # Step 2: Load stage boxes (inputs and outputs) with some data
    box_dict = {
        "SB1-IN": 2,  # 2 inputs on stage box 1
        "SB1-OUT": 2,  # 2 outputs on stage box 1
        "SB2-IN": 3,  # 3 inputs on stage box 2
        "SB2-OUT": 3   # 3 outputs on stage box 2
    }

    # Load the data into the StageBoxManager
    stagebox_manager.load_stageboxes(box_dict)

    # Step 3: Check availability of inputs and outputs
    print("SB1-IN available:", stagebox_manager.available_input("SB1-IN"))  # Expected: True
    print("SB1-OUT available:", stagebox_manager.available_output("SB1-OUT"))  # Expected: True
    print("SB2-IN available:", stagebox_manager.available_input("SB2-IN"))  # Expected: True
    print("SB2-OUT available:", stagebox_manager.available_output("SB2-OUT"))  # Expected: True

    # Step 4: Use some inputs and outputs
    print("Using SB1-IN:", stagebox_manager.used_input("SB1-IN"))  # Expected: True
    print("Using SB1-OUT:", stagebox_manager.used_output("SB1-OUT"))  # Expected: True
    print("Using SB2-IN:", stagebox_manager.used_input("SB2-IN"))  # Expected: True
    print("Using SB2-OUT:", stagebox_manager.used_output("SB2-OUT"))  # Expected: True

    # Step 5: Check availability after usage
    print("SB1-IN available after use:", stagebox_manager.available_input("SB1-IN"))  # Expected: True
    print("SB1-OUT available after use:", stagebox_manager.available_output("SB1-OUT"))  # Expected: True
    print("SB2-IN available after use:", stagebox_manager.available_input("SB2-IN"))  # Expected: True
    print("SB2-OUT available after use:", stagebox_manager.available_output("SB2-OUT"))  # Expected: True

    # Step 6: Release inputs and outputs
    stagebox_manager.release_input("SB1-IN")
    stagebox_manager.release_output("SB1-OUT")
    stagebox_manager.release_input("SB2-IN")
    stagebox_manager.release_output("SB2-OUT")

    # Step 7: Check availability after releasing
    print("SB1-IN available after release:", stagebox_manager.available_input("SB1-IN"))  # Expected: True
    print("SB1-OUT available after release:", stagebox_manager.available_output("SB1-OUT"))  # Expected: True
    print("SB2-IN available after release:", stagebox_manager.available_input("SB2-IN"))  # Expected: True
    print("SB2-OUT available after release:", stagebox_manager.available_output("SB2-OUT"))  # Expected: True

    print("Usage before release:", stagebox_manager.inputs["SB1-IN"])
    stagebox_manager.release_input("SB1-IN")
    print("Usage after release:", stagebox_manager.inputs["SB1-IN"])


# Run the test case
test_stagebox_manager()
