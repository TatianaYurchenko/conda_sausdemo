class OrderData:
    user_data = [["", "Yurch", "123", "Error: First Name is required"],
                 ["Tatiana", "", "123", "Error: Last Name is required"],
                 ["Tatiana", "Yurch", "", "Error: Postal Code is required"]]
    user_data_with_valid_credential = ["Tatiana", "Yurch", "123"]
    thank_text = "Thank you for your order!"