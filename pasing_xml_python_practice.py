import xml.etree.ElementTree as ET

tree = ET.parse('Library.xml')
root = tree.getroot()
#print(root.tag) #print root
#print(root.attrib) #print root attributs

#for child in root:
#    print(child.tag,child.attrib)
#    for sub in child:
#        print(sub.tag,sub.attrib)

# to print all element in the  tree
#for elm in root.iter():
    #print(elm.tag)
    
#print(ET.tostring(root, encoding='utf8').decode('utf8')) to print the who;le document

# to find a element 'key'
#for key in root.iter('key'):
#    print(key.text)


#findall() function that will traverse the immediate children of the referenced element.
stuf = tree.findall('dict/dict/dict')
for each in stuf:
    for k in each:
        print(k.text)
        
# REFERENCE RESOURCE :- https://www.datacamp.com/community/tutorials/python-xml-elementtree
