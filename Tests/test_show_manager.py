from stage_management import MicInventory, StageBoxManager, InputList, OutputList
from Data.ShowManager import ShowManager  # adjust path if needed


def test_showmanager_save_load():
    # Step 1: Setup original data
    mic_inventory = MicInventory()
    mic_inventory.load_inventory({"SM58": 5, "Beta57": 3})

    sbm = StageBoxManager()
    sbm.load_stageboxes([
        {"line": "SB1", "type": "IN", "total": 4},
        {"line": "SB1", "type": "OUT", "total": 2}
    ])

    input_list = InputList(stagebox_manager=sbm, mic_inventory=mic_inventory)
    input_list.add_input("Lead Voc", "Vocal", "SM58", "SB1", 1)
    input_list.add_input("E Guitar", "Guitar Amp","Beta57", "SB1", 2)

    output_list = OutputList(stagebox_manager=sbm)
    output_list.add_output("Drum Mix", "SB1",1)

    # Step 2: Save the data
    manager = ShowManager()
    manager.save_show("test_show", mic_inventory, sbm, input_list, output_list)

    # Step 3: Reset the objects
    mic_inventory = MicInventory()
    sbm = StageBoxManager()
    input_list = InputList(stagebox_manager=sbm, mic_inventory=mic_inventory)
    output_list = OutputList(stagebox_manager=sbm)

    # Step 4: Load the data
    manager.load_show("test_show", mic_inventory, sbm, input_list, output_list)

    # Step 5: Confirm loaded data
    print("\n--- Loaded Mic Inventory ---")
    print(mic_inventory.inventory)

    print("\n--- Loaded Stageboxes ---")
    print("Inputs:", sbm.inputs)
    print("Outputs:", sbm.outputs)

    print("\n--- Loaded Inputs ---")
    for name, data in input_list.inputs.items():
        print(f"{name}: {data}")

    print("\n--- Loaded Outputs ---")
    for mix, data in output_list.outputs.items():
        print(f"{mix}: {data}")

test_showmanager_save_load()

