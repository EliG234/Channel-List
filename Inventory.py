

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

    def load_stageboxes(self, box_dict):
        for line, total in box_dict.items():
            if 'IN' in line:
                self.inputs[line] = {'total': total, 'used': 0}
            elif 'OUT' in line:
                self.outputs[line] = {'total': total, 'used': 0}

    def available_input(self, input_line):
        input_data = self.inputs.get(input_line)
        return input_data and input_data['used'] < input_data['total']


    def available_output(self, output_line):
        output_data = self.outputs.get(output_line)
        return output_data and output_data['used'] < output_data['total']

    def used_input(self, input_line):
        if self.available_input(input_line):
            self.inputs[input_line]['used'] += 1
            return True
        else:
            return False

    def used_output(self, output_line):
        if self.available_output(output_line):
            self.outputs[output_line]['used'] += 1
            return True
        else:
            return False

    def release_input(self, input_line):
        if input_line in self.inputs and self.inputs[input_line]['used'] > 0:
            self.inputs[input_line]['used'] -= 1

    def release_output(self, output_line):
        if output_line in self.outputs and self.outputs[output_line]['used'] > 0:
            self.outputs[output_line]['used'] -= 1

class InputList:
    def __init__(self, stagebox_manager):
        self.inputs = {}
        self.stagebox_manager = stagebox_manager

    def add_input(self, channel, instrument, mic, stagebox, input_num):
        if channel in self.inputs:
            return False

        input_line = f"{stagebox}-{input_num}"

        if not self.stagebox_manager.available_input(input_line):
            return False

        self.inputs[channel] = {
            "instrument": instrument,
            "mic": mic,
            "stage_box": stagebox,
            "input": input_num
        }

        self.stagebox_manager.used_input(input_line)
        return True


