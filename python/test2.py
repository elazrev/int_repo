from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/data")
def redirect():
    return f"Walla Walla"


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


#אם אנחנו מקבלים מספר תלת ספרתי שאנחנו רוצים להפריד למאות, עשרות ואחדות
#נשתמש באופורטור:
# // => חלוקה ללא שארית
# דוגמה:

# User input
user_number = int(input("Enter 3 digits number here: "))
# כדי להוציא את ספרת המאות, נחלק ב100 ללא שארית
num_1 = user_number // 100
# כדי להוציא את ספרת המאות נחלק ב10 ללא שארית
num_2 = user_number // 10
# כדי להוציא את ספרת האחדות יש כמה דרכים
#הראשונה היא להחסיר מהמספר הראשוני את העשרות והמאות:
num_3 = user_number - (num_1 * 100) - (num_2 * 10)
# האופציה השנייה היא להשתמש במודולו - % שנותן את השארית של החלוקה:
num_3_op_2 = user_number % 10
# נוודא שמצאנו הכל נכון:
print(f"You'v entered the number {user_number}"
      f"\nHundreds = {num_1}"
      f"\nTen's = {num_2}"
      f"\nOne's = {num_3} and also {num_3_op_2}")

# ועכשיו לתרגיל
print(num_1 + num_2 + num_3)
print((num_1 + num_2 + num_3) // 3)
print((num_1 + num_2 + num_3) % 3)
print((num_1 + num_2 + num_3) % 3 == 0)
