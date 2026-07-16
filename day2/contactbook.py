phone={
    "alice":"555-5433",
    "bob":"6664-383"
}
print(f"""
    Welcome to Phonebook
      
      Press 1: to view all contacts
      Press 2: to add new contact
      Press 3: Search Contact
      Press 4: Delete Contact
      Press 5: Update Contact
      Press 6: Exit""")
stat=0
while stat!=6:
    stat=int(input())
    if stat==1:
        print(phone)
    elif stat==2:
        key1=input("Enter Name")
        val=input("Enter phone:")
        phone[key1]=val
        print(f"Contact added {key1}:{val}")
    elif stat==3:
        name=input("Enter name to search: ").lower()
        for k,v in phone.items():
            if k.lower()==name:
                print(f"{k}:{v}")
    elif stat==4:
        name=input("Enter name to delete: ").lower()
        for k,v in list(phone.items()):
            if k.lower()==name:
                del phone[k]
                print("Deleted",k,":",v)
    elif stat==5:
        name=input("Enter name whose contact to be updated")
        for k in phone.keys():
            if k.lower()==name.lower():
                num=input("Enter the new phone")
                phone[k]=num
                print(f"Updated {k}={num}")

