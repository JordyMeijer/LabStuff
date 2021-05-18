import sqlite3
from typing import Protocol
import xml.etree.ElementTree as ET
import os

conn = sqlite3.connect('Labstuff.db')

c = conn.cursor()

# c.execute("""CREATE TABLE sample (
# Sample_Number integer,
# Study text,
# Subject_ID text,
# Subject_No integer,
# Global_Sub_No integer,
# Activity text,
# Samp_Seq_No integer,
# Label_ID text,
# Occasion integer,
# Prot_Time text,
# R_Prot_Time integer,
# Material text,
# Container text,
# Status text,
# Screening_No integer,
# Sponsor_ID text,
# Gender text,
# Birthday text,
# Is_Parent text
# )""")
print("Cur Dir is:" + os.getcwd())
os.chdir("../XML")
print("Cur Dir is:" + os.getcwd())
tree = ET.parse('20210517135916_238_SAMPLE_39558A3FC.XML')
root = tree.getroot()
print(root.tag)



def get_info(a):
  for child in root.iter():
    if child.tag == a:
      print(child.text)
      return child.text


Subject_ID = get_info("SubjectID")
Subject_No = get_info("SubjectNumber")
Global_Sub_No = get_info("GlobalSubjectNumber") 
Activity = get_info("Activity")
Samp_Seq_No = get_info("SampleSequenceNumber")
Label_ID = get_info("SampleID")
Occasion = get_info("Occasion")
Prot_Time = get_info("FormattedProtocolTime")
R_Prot_Time = get_info("ProtocalTime")
Material = get_info("SampleMaterial")
Container = get_info("ContainerType")
Status = get_info("SampleStatus")
Screening_No = get_info("ScreeningNumber")
Sponsor_ID = get_info("SponsorSubjectID")
Gender = get_info("Gender")
Birthday = get_info("Birtyday")
Study = get_info("Protocol")

#print(ET.tostring(root, encoding='utf8').decode('utf8'))

conn.commit()
conn.close()