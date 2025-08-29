from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# ---- Your details ----
FULL_NAME = "john_doe"   # must be lowercase
DOB = "17091999"         # ddmmyyyy
EMAIL = "john@xyz.com"
ROLL = "ABCD123"


class DataRequest(BaseModel):
    data: List[str]


@app.post("/bfhl")
def process_data(request: DataRequest):
    odd_numbers, even_numbers, alphabets, special_chars = [], [], [], []
    total_sum = 0
    concat_string = ""

    for el in request.data:
        if el.isdigit():  # numeric string
            num = int(el)
            if num % 2 == 0:
                even_numbers.append(el)
            else:
                odd_numbers.append(el)
            total_sum += num
        elif el.isalpha():  # alphabets
            alphabets.append(el.upper())
            concat_string += el
        else:  # special characters
            special_chars.append(el)


    concat_rev = "".join(
        ch.upper() if i % 2 == 0 else ch.lower()
        for i, ch in enumerate(concat_string[::-1])
    )

    return {
        "is_success": True,
        "user_id": f"{FULL_NAME}_{DOB}",
        "email": EMAIL,
        "roll_number": ROLL,
        "odd_numbers": odd_numbers,
        "even_numbers": even_numbers,
        "alphabets": alphabets,
        "special_characters": special_chars,
        "sum": str(total_sum),
        "concat_string": concat_rev,
    }
