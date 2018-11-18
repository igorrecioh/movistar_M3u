import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, Comment, ElementTree, tostring
import codecs
import sys
reload(sys)
sys.setdefaultencoding('utf8')
tree = ET.parse('raw_239.0.2.168_2_0.xml')
xmldata = tree.getroot()
xmlstr = tostring(xmldata, encoding='utf-8', method='xml')
root = ET.fromstring(xmlstr)
services = root[0][0].findall("{urn:dvb:ipisdns:2006}SingleService")
with codecs.open("Movistar_List.m3u", "w+", encoding = "utf-8") as f:
    f.write("#EXTM3U" + '\n')
    for i in services:
        try:
            #print(i[0][0].attrib["Address"])
            a = str("#EXTINF:-1," + i[2][0].text + '\n')
            f.write(a)
            if 'Address' in i[0][0].attrib:
                b = str("rtp://@" + i[0][0].attrib["Address"] + ":" + i[0][0].attrib["Port"] + '\n')
                f.write(b)
            else:
            	b = str("rtp://@0.0.0.0:0000"  + '\n')
            	f.write(b)
        except IndexError:
            b = str("rtp://@0.0.0.0:0000"  + '\n')
            f.write(b)

f.close()
print("Archivo creado en Movistar_List.m3u")
