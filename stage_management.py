

class MicInventory:
    def __init__(self):
        self.inventory = {}
        self.in_use = {}
        self.mics = {}

    def load_inventory(self, inventory_dict):
        self.inventory = inventory_dict
        self.in_use = {model: 0 for model in inventory_dict}

    def available_mic(self, model):
        if model not in self.inventory:
            print(f"Error: Mic model '{model}' not found in inventory.")
            return False
        else:
            used = self.in_use.get(model, 0)
            total = self.inventory[model]
            return used < total

    def used_mic(self, model):
        if self.available_mic(model):
            self.in_use[model] += 1
            return True
        else:
            return False

    def release_mic(self, model):
        if self.in_use.get(model, 0) > 0:
            self.in_use[model] -= 1

    def save_to_data(self):
        return self.mics

    def load_from_data(self, data):
        self.mics = data

class StageBoxManager:
    def __init__(self):
        self.inputs = {}
        self.outputs = {}

    def load_stageboxes(self, stagebox_list):
        self.inputs = {}
        self.outputs = {}

        for box in stagebox_list:
            if box["type"] == "IN":
                self.inputs[box["line"]] = {
                    "total": box["total"],
                    "used": set()
                }

            elif box["type"] == "OUT":
                self.outputs[box["line"]] = {
                    "total": box["total"],
                    "used": 0
                }


    def available_input(self, stagebox, input_num):
       return (
           stagebox in self.inputs and
           0 < input_num <= self.inputs[stagebox]["total"] and
           input_num not in self.inputs[stagebox].get("used", set())
       )

    def used_input(self, stagebox, input_num):
        if self.available_input(stagebox, input_num):
            self.inputs[stagebox].setdefault("used",set()).add(input_num)
            print(f"Used {stagebox}-{input_num}: {len(self.inputs[stagebox]['used'])} used out of {self.inputs[stagebox]['total']}")
            return True
        else:
            print(f"Input line {stagebox}-{input_num} not available!")
            return False

    def release_input(self, input_line):
        stagebox, num = input_line.split("-")
        num = int(num)
        if stagebox in self.inputs and num in self.inputs[stagebox].get("used", set()):
                self.inputs[stagebox]["used"].remove(num)
                print(f"Released {input_line}")
                return True
        print(f"Input line {input_line} cannot be released!")
        return False

    def available_output(self, stagebox, output_num):
        if stagebox not in self.outputs:
            print(f"Stagebox {stagebox} not found in outputs")
            return False

        total = self.outputs[stagebox]["total"]
        used = self.outputs[stagebox]["used"]

        if used < total:
            return True
        else:
            print(f"No available outputs on {stagebox}")
            return False

    def mark_used_output(self, stagebox, output_num):
        if stagebox not in self.outputs:
            print(f"Stagebox {stagebox} not found in outputs!")
            return False

        if not self.available_output(stagebox, output_num):
            print(f"Output {stagebox}-{output_num} not available!")
            return False

        self.outputs[stagebox]["used"] += 1
        print(f"Used {stagebox}-{output_num}")
        return True

    def release_output(self, stagebox):
        if stagebox in self.outputs and self.outputs[stagebox]['used'] > 0:
            self.outputs[stagebox]['used'] -= 1
            print(f"Released one output from {stagebox}: now {self.outputs[stagebox]['used']} used out of {self.outputs[stagebox]['total']}")
            return True
        else:
            print(f"Output from {stagebox} cannot be released or is already empty!")
            return False


class InputList:
    def __init__(self, stagebox_manager, mic_inventory):
        self.inputs = {}
        self.mic_inventory = mic_inventory
        self.stagebox_manager = stagebox_manager

    def add_input(self, channel, instrument, mic, stagebox, input_num):
        if channel in self.inputs:
            print(f"Channel {channel} already exists.")
            return False

        print(f"Trying to use input {stagebox}-{input_num}")

        if not self.stagebox_manager.used_input(stagebox, input_num):
            print(f"Input {stagebox}-{input_num} is not available!")
            return False

        self.inputs[channel] = {
            "instrument": instrument,
            "mic": mic,
            "stage_box": stagebox,
            "input": input_num
        }

        print(f"Added {channel} successfully.")
        return True


    def remove_input(self, channel):
        if channel in self.inputs:
            input_data = self.inputs[channel]
            stagebox = input_data["stage_box"]
            input_num = input_data["input"]
            input_line = f"{stagebox}-{input_num}"

            self.stagebox_manager.release_input(input_line)
            del self.inputs[channel]

            return True
        else:
            return False

    def save_to_data(self):
        return self.inputs

    def load_from_data(self, data):
        for channel, input_data in data.items():
            self.add_input(
                channel,
                input_data["instrument"],
                input_data["mic"],
                input_data["stage_box"],
                input_data["input"]
            )

class OutputList:
    def __init__(self, stagebox_manager):
        self.outputs = {}
        self.stagebox_manager = stagebox_manager

    def add_output(self, mix_name, stagebox, output_num):
        output_line = f"{stagebox}-{output_num}"
        print(f"Trying to add: {mix_name} - > {output_line}")

        if mix_name in self.outputs:
            print(f"Mix {mix_name} already exists.")
            return False

        if not self.stagebox_manager.available_output(stagebox, output_num):
            print(f"Output line {output_line} not available!")
            return False

        self.outputs[mix_name] = {
            "stage_box": stagebox,
            "output_num": output_num
        }
        self.stagebox_manager.mark_used_output(stagebox, output_num)

        print(f"Added {mix_name} successfully.")
        return True

    def remove_output(self, mix_name):
        if mix_name in self.outputs:
            stagebox = self.outputs[mix_name]["stage_box"]
            self.stagebox_manager.release_output(stagebox)
            del self.outputs[mix_name]

            print(f"Removed {mix_name} successfully.")
            return True
        else:
            print(f"Mix {mix_name} does not exist.")
            return False

    def save_to_data(self):
        return self.outputs

    def load_from_data(self, data):
        self.outputs = data
        for channel, output_data in data.items():
            stagebox = output_data["stage_box"]
            output_num = output_data["output_num"]
            self.stagebox_manager.mark_used_output(stagebox, output_num)