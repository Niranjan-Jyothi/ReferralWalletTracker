def TryParseInt(value: str, defaultValue: int = 0) -> (bool, int):
    """Utility function to try parse Integer. Returns Boolean for Is Parsing Successfully and the integer value otherwise returns the passed-in default value

    Args:
        value (str): The string value to be parsed
        defaultValue (int): [Optional] The default value to be returned if Parse failed.
    """
    try:
        return True, int(value)
    except ValueError:
        return False, defaultValue
    
def TryParseFloat(value: str, defaultValue: float = 0) -> (bool, float):
    """Utility function to try parse Float. Returns Boolean for Is Parsing Successfully and the float value otherwise returns the passed-in default value

    Args:
        value (str): The string value to be parsed
        defaultValue (float): [Optional] The default value to be returned if Parse failed.
    """
    try:
        return True, float(value)
    except ValueError:
        return False, defaultValue