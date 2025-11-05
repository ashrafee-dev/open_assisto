def test_transcribe():
    text_list = ["search white noice","youtube"]
    with open("audio1", "read") as file:
        output_list = transcribe(file)
        lowercase_output_list = [item.lower() for item in output_list]

    text_list2 = ["I don't want to see nothing, just zip it","avoid"]
    with open("audio1", "read") as file:
        output_list2 = transcribe(file)
        lowercase_output_list2 = [item.lower() for item in output_list2]

    text_list3 = ["10PM, doctors appointment, tomorrow","calender"] #Message was "I haave a doctor appointment tomorrow at 10AM"
    with open("audio1", "read") as file:
        output_list3 = transcribe(file)
        lowercase_output_list3 = [item.lower() for item in output_list3]


    assert lowercase_output_list == text_list
    assert lowercase_output_list2 == text_list2
    assert lowercase_output_list3 == text_list3



if __name__ == "__main__":
    
    print("Running Tests: \n")
    test_transcribe()
