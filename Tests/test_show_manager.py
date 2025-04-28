from inventory import MicInventory, StageBoxManager, InputList
from ShowManager import ShowManager

mic_inventory = MicInventory()
stagebox_manager = StageBoxManager()
input_list = InputList(stagebox_manager)
show_manager = ShowManager()

mic_inventory.load_inventory({
    "SM58": 10,
    "SM57": 5,
    "MKH416": 2
})
stagebox_manager.load_stageboxes([
    {"line": "SB1-1", "type": "IN", "total": 1},
    {"line": "SB1-2", "type": "IN", "total": 1},

    {"line": "SB1-1", "type": "OUT", "total": 1},
    {"line": "SB1-2", "type": "OUT", "total": 1},
])

input_list.add_input(1, "VOC", "SM58", "SB1", 1)
input_list.add_input(2, "GTR", "SM57", "SB1", 2)