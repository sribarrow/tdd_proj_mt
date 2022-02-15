def mumble_letter(string_val: str) -> str:
    result=""
    if len(string_val)>1:
        for val in string_val:
            ind = string_val.index(val)+1
            val = val * ind
            print(val, ind, len(string_val))
            if ind < len(string_val):
                result += f"{val[0].upper()}{val[1:]}-"
            else:
               result += f"{val[0].upper()}{val[1:]}"
    else:
        result =string_val.upper()
    return result

if __name__ == "__main__":
    print(mumble_letter("abc"))