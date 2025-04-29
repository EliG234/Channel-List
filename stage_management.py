

class MicInventory:
    def __init__(self):
        self.inventory = {}
        self.in_use = {}

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

class StageBoxManager:
    def __init__(self):
        self.inputs = {}
        self.outputs = {}

    def load_stageboxes(self, box_list):
        for item in box_list:
            line = item["line"]
            box_type = item["type"]
            total = item["total"]

            if box_type == "IN":
                self.inputs[line] = {'total': total, 'used': 0}
            elif box_type == "OUT":
                self.outputs[line] = {'total': total, 'used': 0}

    def available_input(self, stagebox, input_num):
        if stagebox in self.inputs:
            used = self.inputs[stagebox].get("used", [])
            return input_num not in used and input_num <= self.inputs[stagebox]["total"]
        return False

    def used_input(self, stagebox, input_num):
        if self.available_input(stagebox, input_num):
            self.inputs[stagebox].setdefault("used", []).append(input_num)
            print(f"Used {stagebox}-{input_num}: {self.inputs[stagebox]['used']} used out of {self.inputs[stagebox]['total']}")
            return True
        else:
            print(f"Input line {stagebox}-{input_num} not available!")
            return False

    def available_output(self, stagebox, output_num):
        if stagebox in self.outputs:
            used = self.outputs[stagebox].get("used", [])
            return output_num not in used and output_num <= self.outputs[stagebox]["total"]
        return False

    def used_output(self, stagebox, output_num):
        if self.available_output(stagebox, output_num):
            self.outputs[stagebox].setdefault("used", []).append(output_num)
            print(f"Used output {stagebox}-{output_num}: {self.outputs[stagebox]['used']}")
            return True
        else:
            print(f"Output line {stagebox}-{output_num} not available!")
            return False

    def release_input(self, input_line):
        if input_line in self.inputs and self.inputs[input_line]['used'] > 0:
            self.inputs[input_line]['used'] -= 1
            print(f"Released {input_line}: {self.inputs[input_line]['used']} used out of {self.inputs[input_line]['total']}")
            return True
        else:
            print(f"Input line {input_line} cannot be released!")
            return False

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

        input_line = f"{stagebox}-{input_num}"
        print(f"Trying input line: {input_line}")

        if input_line in self.inputs and self.inputs[input_line]['used'] < self.inputs[input_line]['total']:
            self.inputs[input_line]['used'] += 1
            self.inputs[channel] = {
                "instrument": instrument,
                "mic": mic,
                "stage_box": stagebox,
                "input": input_num
            }
            print(f"Added {channel} successfully.")
            return True
        else:
            print(f"Input line {input_line} not available!")
            return False


    def remove_input(self, channel):
        if channel in self.inputs:
            input_data = self.inputs[channel]
            stagebox = input_data["stage_box"]
            input_num = input_data["input"]
            input_line = f"{stagebox}"-{input_num}

            self.stagebox_manager.release_input(input_line)
            del self.inputs[channel]

            return True
        else:
            return False

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
        self.stagebox_manager.used_output(stagebox, output_num)

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