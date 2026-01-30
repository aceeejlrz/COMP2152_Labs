contacts = {
    "Alice": "123-456-7890",
    "Bob": "987-654-3210",
    "Charlie": "555-555-5555"
}
print(f"Alice's contact: {contacts['Alice']}")
contacts["Diana"] = "444-444-4444"
print(f"Contacts after adding Diana: {contacts}")
contacts["Bob"] = "111-222-3333"
print(f"Contacts after updating Bob's number: {contacts}")
del contacts["Charlie"]
print(f"Contacts after deleting Charlie: {contacts}")
print(f"All contact names: {list(contacts.keys())}")
print(f"All contact numbers: {list(contacts.values())}")
print(f"Total number of contacts: {len(contacts)}")
