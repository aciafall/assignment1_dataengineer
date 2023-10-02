import xml.etree.ElementTree as et
import subword_nmt

input_xml="sample-src.xml"
output_txt="output.txt"

tree=et.parse(input_xml)
root=tree.getroot()

# # for test
# for child in root.iter():
#     print(child.text)
# print(root.iter())


# convert the data to the line-based text
with open(output_txt,"w",encoding="utf-8") as f:
    for child in root.iter():
        if(child.text):
            f.write(child.text+"\n")

