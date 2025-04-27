from Inventory import StageBoxManager, InputList


def test_stagebox_manager():
    # Initialize the StageBoxManager


    # Example box list, including both inputs and outputs
    box_list = [
        {"line": "SB1-1", "type": "IN", "total": 2},
        {"line": "SB1-1", "type": "OUT", "total": 2},
        {"line": "SB2-1", "type": "IN", "total": 1},
        {"line": "SB2-2", "type": "OUT", "total": 1},
    ]

    # Load the stageboxes
    stagebox_manager = StageBoxManager()
    stagebox_manager.load_stageboxes(box_list)

    # Test usage and release
    print(f"SB1-1 IN available: {stagebox_manager.available_input('SB1-1')}")
    print(f"SB1-1 OUT available: {stagebox_manager.available_output('SB1-1')}")
    print(f"SB2-1 IN available: {stagebox_manager.available_input('SB2-1')}")
    print(f"SB2-2 OUT available: {stagebox_manager.available_output('SB2-2')}")

    # Try using and releasing
    print("Using SB1-1 IN:", stagebox_manager.used_input('SB1-1'))
    print("Using SB1-1 OUT:", stagebox_manager.used_output('SB1-1'))
    print("SB1-1 IN available after use:", stagebox_manager.available_input('SB1-1'))
    print("SB1-1 OUT available after use:", stagebox_manager.available_output('SB1-1'))

    # Release
    print("Releasing SB1-1 IN:", stagebox_manager.release_input('SB1-1'))
    print("Releasing SB1-1 OUT:", stagebox_manager.release_output('SB1-1'))
    print("SB1-1 IN available after release:", stagebox_manager.available_input('SB1-1'))
    print("SB1-1 OUT available after release:", stagebox_manager.available_output('SB1-1'))

# Run the test
test_stagebox_manager()
