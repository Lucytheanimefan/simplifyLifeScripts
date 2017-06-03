import subprocess
import applescript
import AddressBook as ab
import objc
import pprint as pp
import requests, json
import ast
import sys

_default_skip_properties = frozenset(("com.apple.ABPersonMeProperty",
                                      "com.apple.ABImageData"))


def get_gender(name):
	r = requests.get("https://api.genderize.io/?name="+name)
	#print r.content
	#print json.loads(r.content)["gender"]
	return json.loads(r.content)["gender"]



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
    all_props = {prop.lower(): pythonize(person.valueForProperty_(prop))
            for prop in props if prop not in skip}
    return all_props

def address_book_to_list():
    address_book = ab.ABAddressBook.sharedAddressBook()
    people = address_book.people()
    #print(people)
    all_people = [ab_person_to_dict(person) for person in people]
    '''
    for person in all_people:
    	print person
    	print "------"
   	'''
    #relevant_info = [{"email":person["email"],"first":person["first"],"gender":get_gender(person["first"])} for person in all_people if "email" in person and "first" in person]
    return all_people#relevant_info


def run(message, toPerson, fromPerson="spothorse9.lucy@gmail.com"):
	applescript.AppleScript('tell application "Messages" \n'+
    'send "'+message+'" to buddy "'+toPerson+'" of service "E:'+fromPerson+'"\n'+
	'end tell').run()

if __name__ == '__main__':
	sent_to = []
	print "Message by notes? (y/n)"
	answer = sys.stdin.readline().strip()
	if answer=="y":
		print "What preprogrammed tag? (anime, family, deadfisheyed, cool)"
		tags = sys.stdin.readline().strip().split(",")
		names = None
	else:
		print "Who do you want to bother (names separated by commas)?"
		names = sys.stdin.readline().strip().split(",")
		tags = None
	print "Message?"
	message = sys.stdin.readline() + "\n(Sent from Lucy's awesome script)"
	people = address_book_to_list()
	for person in people:
		if answer=="y": #tag
			for tag in tags:
				if "note" in person and tag.lower() in person["note"].lower() and person["phone"][0] not in sent_to:
					if "phone" in person:
						run(message,person["phone"][0])
						sent_to.append(person["phone"][0])
					#elif "email" in person:
					#	run(message,person["email"][0])
		else:
			for name in names: #by name
				if "first" in person and name.lower()==person["first"].lower() and person["phone"][0] not in sent_to:
					if "phone" in person:
						run(message,person["phone"][0])
						sent_to.append(person["phone"][0])
					#elif "email" in person:
					#	run(message,person["email"][0])


