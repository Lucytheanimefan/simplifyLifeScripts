import subprocess
import applescript
import Contacts
import AddressBook as ab
from Foundation import NSBundle
import objc
import pprint as pp

_default_skip_properties = frozenset(("com.apple.ABPersonMeProperty",
                                      "com.apple.ABImageData"))

def pythonize(objc_obj):
    if isinstance(objc_obj, objc.pyobjc_unicode):
        return unicode(objc_obj)
    elif isinstance(objc_obj, ab.NSDate):
        return objc_obj.description()
    elif isinstance(objc_obj, ab.NSCFDictionary):
        # implicitly assuming keys are strings...
        return {k.lower(): pythonize(objc_obj[k])
                for k in objc_obj.keys()}
    elif isinstance(objc_obj, ab.ABMultiValueCoreDataWrapper):
        return [pythonize(objc_obj.valueAtIndex_(index))
                for index in range(0, objc_obj.count())]

def ab_person_to_dict(person, skip=None):
    skip = _default_skip_properties if skip is None else frozenset(skip)
    props = person.allProperties()
    return {prop.lower(): pythonize(person.valueForProperty_(prop))
            for prop in props if prop not in skip}

def address_book_to_list():
    """
    Read the current user's AddressBook database, converting each person
    in the address book into a Dictionary of values. Some values (addresses,
    phone numbers, email, etc) can have multiple values, in which case a
    list of all of those values is stored. The result of this method is
    a List of Dictionaries, with each person represented by a single record
    in the list.
    Function adapted from: https://gist.github.com/pklaus/1029870
    """
    address_book = ab.ABAddressBook.sharedAddressBook()
    people = address_book.people()
    return [ab_person_to_dict(person) for person in people]


def run(message, toPerson, fromPerson="spothorse9.lucy@gmail.com"):
	applescript.AppleScript('tell application "Messages" \n'+
    'send "'+message+'" to buddy "'+toPerson+'" of service "E:'+fromPerson+'"\n'+
	'end tell').run()

if __name__ == '__main__':
	pp.pprint(address_book_to_list())
	#run("hi","9082405834")
	#get_relevant_contacts()