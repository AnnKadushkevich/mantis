from model.contact import Contact
from random import randrange


def test_modify_contact(app):
    if app.contact.count() == 0:
        app.contacts.contact(Contact(firstname="add"))
    old_contacts = app.contacts.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="add")
    contact.id = old_contacts[index].id
    app.contacts.modificate_contact_by_index(index, contact)
    new_contacts = app.contact.get_contact_list()
    assert len(new_contacts) == len(old_contacts)
    old_contacts[index] = contact
    prepare_result = new_contacts
    assert sorted(prepare_result, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)