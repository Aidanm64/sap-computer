import xml.etree.ElementTree as ET 

def parseXML(xmlfile): 
  
    # create element tree object 
    tree = ET.parse(xmlfile) 
  
    # get root element 
    root = tree.getroot() 
  
    # create empty list for news items 
  
    # iterate news items 
    for item in root.findall('./circuit/comp'):
        if item.attrib['name'] == "ROM":
        	for thing in item:
        		print(thing.get("contents"))
parseXML("comp1.circ")