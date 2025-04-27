# Mocking StageBoxManager
class MockStageBoxManager:
    def __init__(self):
        self.used_inputs = {}

    def available_input(self, input_line):
        return self.used_inputs.get(input_line, 0) == 0  # Return True if input is not used

    def used_input(self, input_line):
        self.used_inputs[input_line] = 1  # Mark input as used

# InputList Class
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

        print("Updated Channel List:", self.inputs)

        self.stagebox_manager.used_input(input_line)
        return True

# Testing the InputList class
mock_stagebox_manager = MockStageBoxManager()
input_list = InputList(mock_stagebox_manager)

# Test 1: Add an input to channel 1
result1 = input_list.add_input(1, "Kick Drum", "DPA 4099", "SB1", 1)
print(result1)  # Should print True

# Test 2: Try adding input to channel 1 again (should fail)
result2 = input_list.add_input(1, "Snare Drum", "Shure SM57", "SB1", 1)
print(result2)  # Should print False

# Test 3: Add input to a different channel
result3 = input_list.add_input(2, "Guitar", "Shure SM57", "SB2", 1)
print(result3)  # Should print True
