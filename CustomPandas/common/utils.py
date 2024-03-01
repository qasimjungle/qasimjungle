
def ask_to_exit_or_continue(accept_key="Y", exit_key="X"):
    user_i = take_user_input(
        f"Enter '{accept_key}' to continue or '{exit_key}' to exit the program",
                             strict_validation=True ,
 validation_rules=['y','x']   )
    return True if user_i.lower() == accept_key else False


def take_user_input(message, strict_validation=None, validation_rules=None, max_tries=None):
    value = input(message + "\n> ")
    lower_input = value.lower()
    if strict_validation:
        if not validation_rules:
            raise Exception("Validation Rules not specified!")
        try:
            if lower_input in validation_rules:
                return lower_input
            else:
                print("Invalid Choice")
                take_user_input(message, strict_validation, validation_rules)
        except Exception as e:
            print("Invalid Choice")
            take_user_input(message, strict_validation, validation_rules)

    return lower_input
