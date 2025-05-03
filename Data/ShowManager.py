import json
import os

class ShowManager:
    def __init__(self):
        self.base_path = "Data"

    def save_show(self, show_name, mic_inventory, stagebox_manager, input_list, output_list):
        data = {
            "mic_inventory": mic_inventory.save_to_data(),
            "stagebox_manager": {
                "inputs": {
                    key: {
                        "total": val["total"],
                        "used": list(val["used"])
                    } for key, val in stagebox_manager.inputs.items()
                },
                "outputs": {
                    key: {
                        "total": val["total"],
                        "used": val["used"]
                    } for key, val in stagebox_manager.outputs.items()
                }
            },
            "input_list": input_list.save_to_data(),
            "output_list": output_list.save_to_data()
        }

        path = os.path.join(self.base_path, f"{show_name}.json")
        with open(path, "w") as f:
            json.dump(data, f, indent=4)
        print(f"Show data saved to {path}")

    def load_show(self, show_name, mic_inventory, stagebox_manager, input_list, output_list):
        path = os.path.join(self.base_path, f"{show_name}.json")
        with open(path, "r") as f:
            data = json.load(f)


        mic_inventory.load_from_data(data["mic_inventory"])


        stagebox_manager.inputs.clear()
        for key, val in data["stagebox_manager"]["inputs"].items():
            stagebox_manager.inputs[key] = {
                "total": val["total"],
                "used": set(val["used"])
            }

        stagebox_manager.outputs.clear()
        for key, val in data["stagebox_manager"]["outputs"].items():
            stagebox_manager.outputs[key] = {
                "total": val["total"],
                "used": val["used"]
            }


        input_list.inputs = data["input_list"]
        output_list.outputs = data["output_list"]
        print("Show data loaded successfully.")
