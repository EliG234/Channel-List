import json
import os

class ShowManager:
    def __init__(self, data_folder="Data"):
      self.data_folder = data_folder
      os.makedirs(data_folder, exist_ok=True)

    def save_show(self, filename, mic_inventory, stagebox_manager, input_list, output_list):
      data = {
        "mic_inventory": mic_inventory.inventory,
        "stageboxes": {
            "inputs": stagebox_manager.inputs,
            "outputs": stagebox_manager.outputs
        },
        "input_list": input_list.inputs,
        "output_list": output_list.outputs
      }

      filepath = os.path.join(self.data_folder, f"{filename}.json")
      with open(filepath, "w") as f:
        json.dump(data, f, indent=4)
        print(f"Show data saved to {filepath}")

    def load_show(self, filename, mic_inventory, stagebox_manager, input_list, output_list):
      filepath = os.path.join(self.data_folder, f"{filename}.json")
      if not os.path.exists(filepath):
        print(f"File {filepath} does not exist.")
        return False

      with open(filepath, "r") as f:
        data = json.load(f)

      mic_inventory.load_inventory(data["mic_inventory"])
      stagebox_manager.inputs = data["stageboxes"]["inputs"]
      stagebox_manager.outputs = data["stageboxes"]["outputs"]
      input_list.inputs = data["input_list"]
      output_list.outputs = data["output_list"]
      print(f"Show data loaded from {filepath}")
      return True