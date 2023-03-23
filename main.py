# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

class AddressBookEntry(BaseModel):
    name: str
    email: str
    phone: str
    address: str


address_book = []

app = FastAPI()
@app.post("/add")
def add_entry(entry: AddressBookEntry):
    address_book.append(entry)
    return{"message": "entry added successfully"}

@app.get("/entries")
def get_entries():
    return address_book


@app.get("/ entries/{name}")
def get_entry_by_name(name: str):
    for entry in address_book:
        if entry. name == name:
            return entry
    return {"message": "Entry not found"}

@app.put("/address_book/{id}")
async def update_address(id: int, address: AddressBookEntry):
    address_book[id] = address
    return {"message": "Address updated successfully."}

@app.delete("/address_book/{id}")
async def delete_address(id: int):
   del AddressBookEntry[id]
    return {"message": "Address deleted successfully."}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)




# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
