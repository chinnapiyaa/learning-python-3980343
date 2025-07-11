# LinkedIn Learning Python course by Joe Marini
# Example file for parsing and processing XML
#
import xml.dom.minidom 


# use the parse() function to load and parse an XML file
doc = xml.dom.minidom.parse("samplexml.xml")


# print out the document node and the name of the first child tag

print(doc.nodeName)
print(doc.firstChild.tagName)

# get a list of XML tags from the document and print each one

skills = doc.getElementsByTagName("skill")
print("Skills:", skills.length)
for skill in skills:
    print("Skill:", skill.getAttribute("name"))
    print("Level:", skill.getAttribute("level"))
# create a new XML tag and add it into the document

