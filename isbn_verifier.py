def is_valid(isbn: str) -> bool:
    """Return if an ISBN number is valid based on the number given"""
    no_dashes = isbn.replace('-', '')

    nums = []

    valid_num = False

    if no_dashes:
        for char in no_dashes:
            if char == 'X':
                nums.append(10)
            elif char != 'X' and char.isalpha() or len(no_dashes) < 10 or len(no_dashes) > 10:
                break
            elif 'X' in no_dashes and no_dashes[-1] != 'X':
                break
            else:
                nums.append(int(char))

    char = 0
    value = 0

    if nums and len(nums) == 10:
        for n in range(10, 0, -1):
            value += (n * nums[char])
            char += 1
        valid_num = (value % 11 == 0)

    return valid_num
