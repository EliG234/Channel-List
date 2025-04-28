from Inventory import StageBoxManager,OutputList
def test_output_list():
 
    sbm = StageBoxManager()
    stagebox_data = [
        {"line": "SB1-1", "type": "OUT", "total": 2},
        {"line": "SB2-1", "type": "OUT", "total": 2}
    ]
    sbm.load_stageboxes(stagebox_data)

   
    output_list = OutputList(stagebox_manager=sbm)

   
    print("\n--- Adding Outputs ---")
    output_list.add_output(mix_name="Drum Monitor", stagebox="SB1", output_num=1)
    output_list.add_output(mix_name="Vocal Wedge", stagebox="SB1", output_num=2)
    output_list.add_output(mix_name="Bass Monitor", stagebox="SB2", output_num=1)

   
    output_list.add_output(mix_name="Drum Monitor", stagebox="SB2", output_num=2)

    
    print("\n--- Removing Outputs ---")
    output_list.remove_output("Vocal Wedge")

    
    output_list.remove_output("Keyboard Wedge")

    
    print("\n--- Final Outputs Stored ---")
    for mix, data in output_list.outputs.items():
        print(f"{mix}: {data}")

test_output_list()
