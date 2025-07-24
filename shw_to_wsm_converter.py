import os
import xml.etree.ElementTree as ET
from xml.dom import minidom

# Frequency band mapping
BAND_LIMITS = {
    'Gw': (558000, 626000),
    'GBw': (606000, 678000),
    'Aw+': (470000, 558000),
    'Bw': (626000, 698000)
}

# Directories
INPUT_DIR = "input_files"
OUTPUT_DIR = "converted_files"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def prettify(elem):
    """Return pretty XML string without XML declaration."""
    rough_string = ET.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    pretty = reparsed.toprettyxml(indent="  ", encoding='utf-8').decode('utf-8')
    return '\n'.join(pretty.split('\n')[1:])  # Remove XML declaration

def convert_shw_to_wsm(shw_filename):
    tree = ET.parse(shw_filename)
    root = tree.getroot()

    wsm_root = ET.Element("WSM", AppVersion="4.6.0.4", Version="1.0")
    ET.SubElement(wsm_root, "DefaultRFThreshold").text = "0"

    unique_id = 1
    ip_octet = 101
    device_number = 1

    for device in root.findall(".//device"):
        series = device.findtext("series")
        band = device.findtext("band")
        if series != "SR 2050" or band not in BAND_LIMITS:
            continue

        lower, upper = BAND_LIMITS[band]
        channels = device.findall("channel")

        # Create a new WSM device per physical SR2050 (2 channels each)
        device_elem = ET.SubElement(wsm_root, "Device", TypeID="85", Type="SR2050 IEM", Version="1.0")
        ET.SubElement(device_elem, "DeviceNumber").text = f"{device_number}"

        for port_num, ch in enumerate(channels, start=1):
            name = ch.findtext("channel_name")
            freq = ch.findtext("frequency")

            rx = ET.SubElement(device_elem, "Receiver", TypeID="49", Type="SR 2050", UniqueId=str(unique_id), Version="1.0")
            ET.SubElement(rx, "Port").text = str(port_num)
            ET.SubElement(rx, "Manual").text = "Yes"
            ET.SubElement(rx, "IPAddressFlag").text = "1"
            ET.SubElement(rx, "IPAddress").text = f"192.168.1.{ip_octet}"
            ET.SubElement(rx, "NameFlag").text = "1"
            ET.SubElement(rx, "Name").text = name
            ET.SubElement(rx, "BankFlag").text = "1"
            ET.SubElement(rx, "Bank").text = "0"
            ET.SubElement(rx, "ChannelFlag").text = "1"
            ET.SubElement(rx, "Channel").text = "0"
            ET.SubElement(rx, "LowerFrequencyLimitFlag").text = "1"
            ET.SubElement(rx, "LowerFrequencyLimit").text = str(lower)
            ET.SubElement(rx, "UpperFrequencyLimitFlag").text = "1"
            ET.SubElement(rx, "UpperFrequencyLimit").text = str(upper)
            ET.SubElement(rx, "CurrentFrequencyFlag").text = "1"
            ET.SubElement(rx, "CurrentFrequency").text = freq
            ET.SubElement(rx, "RFPowerFlag").text = "1"
            ET.SubElement(rx, "RFPower").text = "0"

            unique_id += 1
            ip_octet += 1

        device_number += 1

    # Save output
    output_filename = os.path.splitext(os.path.basename(shw_filename))[0] + "_FIXED_FINAL.wsm"
    output_path = os.path.join(OUTPUT_DIR, output_filename)
    with open(output_path, "w") as f:
        f.write(prettify(wsm_root))

    print(f"✅ Converted and saved: {output_path}")

# Run script from terminal
if __name__ == "__main__":
    filename = input("🔍 Enter just the name of the .shw file (in the input_files/ folder): ").strip()
    input_path = os.path.join(INPUT_DIR, filename)  

    if os.path.isfile(input_path):
        convert_shw_to_wsm(input_path)
    else:
        print(f"❌ File not found in input_files/: {filename}")