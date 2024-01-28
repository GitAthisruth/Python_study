#Extensible Markup Language (XML) is a markup language and file format for storing, transmitting, 
# and reconstructing arbitrary data. It defines a set of rules 
# for encoding documents in a format that is both human-readable and machine-readable.



#<metadata> is the main root tag here.
#food is the child element

data = '''<?xml version="1.0" encoding="UTF-8"?>
<metadata> 
<food>
    <item name="breafast">idily</item>
    <price>$2.5</price>
    <description>
    two idyly's with chatney
    </description>
    <calories>553</calories>
</food>
<food>
    <item name="breafast">Dosha</item>
    <price>$1.5</price>
    <description>
    Dosha with vada
    </description>
    <calories>700</calories>
</food>
</metadata>'''

print(type(data))
  
import xml.etree.ElementTree as EL

tree=EL.fromstring(data)
# fromstring used to identify main root tag .
print(tree)#here only return an object
print(tree.tag)#return exact main root tag 
# elements inside sub root tags are known as elements.

print(tree[0].tag)#sub root tags.
print(tree[0][1].tag)#sub root tag elements.
# An object is simply a collection of data (variables) and 
# methods (functions) that act on those data. Similarly, a class is a blueprint for that object.



# import xml.etree.ElementTree as ET

# tree=ET.parse('sample.xml')
#Parsing means to read information from a file and split it into pieces by identifying parts of that particular XML file.
# mytree=tree.getroot()#getroot() function return the root of tree as an Element object.
# print(mytree)
# print(mytree.tag)
# print(mytree[0].tag)
# print(mytree[0][1][1].tag)


# for i in mytree: #i=child
#     print(i.tag)#here iterate all sub root tags

# for i in mytree[0]: #i=child
#     print(i.tag)#here we get all sub root elements

# for i in mytree: #i=child
#     print(i.tag,i.attrib)#used to get the  attribute inside the sub root tags(child elements).
#Attributes are part of XML elements. An element can have multiple unique attributes. Attribute gives more information about XML elements.
#To be more precise, they define properties of elements. An XML attribute is always a name-value pair.

# for i in mytree[0]: #i=child
#     print(i.tag,i.attrib)#here the sets are empty because inside the sub root elements are empty.

# for i in mytree.findall('book'):
#     auth=i.find('author').text
#     title=i.find('title').text
#     print(auth,title)


# import xml.etree.ElementTree as ET
# tree=ET.parse('sample.xml')
# mytree=tree.getroot()



# for i in  mytree.iter('description'):#select the tag to add data and attribute
#     a=str(i.text)+'new data has been added'#here we adding new data and attribute to a new file
#     i.text=str(a)
#     i.set('update','yes')
# tree.write('xml1.xml')

# for i in  mytree[0].iter('description'):#select a specific tag to add data and attribute by giving index position.
#     a=str(i.text)+'new data has been added'#here we adding new data and attribute to a new file
#     i.text=str(a)
#     i.set('update','yes')
# tree.write('xml2.xml')




# ET.SubElement(mytree[0],'speciality')#to add new element with sub element to a specific sub tag.
# for i in  mytree.iter('speciality'):
#     b='This is a south Indian book'
#     i.text=str(b)
# tree.write('xml3.xml')


# ET.SubElement(mytree,'speciality')#to add new sub tag element with sub element.
# for i in  mytree.iter('speciality'):
#     b='This is a south Indian book'
#     i.text=str(b)
# tree.write('xml4.xml')


# for i in range(len(mytree)):
#     ET.SubElement(mytree[i],'speciality')#to add new element with sub element to all sub tags.
#     for i in  mytree.iter('speciality'):
#         b='This is a south Indian book'
#         i.text=str(b)
# tree.write('xml5.xml')   

# print(len(mytree))


# import xml.etree.ElementTree as ET
# tree=ET.parse('xml2.xml')
# mytree=tree.getroot()


# mytree[0][5].attrib.pop('update')#to delete an attribute,here [0] is the position of sub tag,[5] is the position of element
# tree.write('xml6.xml')

# import xml.etree.ElementTree as ET
# tree=ET.parse('xml1.xml')
# mytree=tree.getroot()

# for i in range(len(mytree)):
#     mytree[i][5].attrib.pop('update')
# tree.write('xml8.xml')

# mytree.clear()#to clear the sub tags
# tree.write('xml9.xml')


# ET.dump(tree)
# mytree[0].remove(mytree[0][0])#here to remove first subelement from the first sub tag.
# tree.write('xml11.xml')



# import xml.etree.ElementTree as ET
# tree=ET.parse('xml1.xml')
# mytree=tree.getroot()


# mytree.clear()#to clear all subtags.
# tree.write('xml10.xml')

# mytree[0].clear()#here to clear all subelements of the first subtag.
# tree.write('xml12.xml')

