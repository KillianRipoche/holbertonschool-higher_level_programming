#!/usr/bin/python3
"""com for the checker"""
import xml.etree.ElementTree as ET
"""once again a com"""


def serialize_to_xml(dictionary, filename):
    """
    Serialize c'est cool
    """
    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        if isinstance(value, bool):
            child.set("type", "bool")
        elif isinstance(value, int):
            child.set("type", "int")
        elif isinstance(value, float):
            child.set("type", "float")
        else:
            child.set("type", "str")

        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding='utf-8', xml_declaration=True)


def deserialize_from_xml(filename):
    """
    Deserialize XML
    """
    try:
        tree = ET.parse(filename)
    except Exception:
        return None

    root = tree.getroot()
    result = {}

    for child in root:
        key = child.tag
        value_type = child.get("type", "str")
        text = child.text

        if value_type == "int":
            try:
                result[key] = int(text)
            except Exception:
                result[key] = text
        elif value_type == "float":
            try:
                result[key] = float(text)
            except Exception:
                result[key] = text
        elif value_type == "bool":
            result[key] = True if text == "True" else False
        else:
            result[key] = text

    return result
