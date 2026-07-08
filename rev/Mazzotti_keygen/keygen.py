# Global uint array at 0x104020 (.data), max 10 entries (string length capped at 10)
Gobal_init_4 = [0x04, 0x4F, 0x81, 0xAB, 0xFE, 0x7B, 0xE0, 0xCC, 0x46, 0x35]

def transform_string_function(input_string: str) -> int:
    length = len(input_string)
    if length == 0:
        return 0

    counter = 0
    int_key = 0
    while True:
        operator1 = ord(input_string[counter])   # (int)*operator1
        operator2 = Gobal_init_4[counter]         # *operator2        
        counter += 1
        int_key += operator1 ^ operator2        
        if length == counter:
            break
    return int_key

input_string = input("Enter a string: ")
print(f"Key: {transform_string_function(input_string)}")
