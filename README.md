## Security Analysis of ”Ultra-Lightweight Blockchainenabled RFID Authentication Protocol for Supply Chain in the domain of 5G Mobile Edge Computing"
## Table of Contents
- [Overview](#overview)
- [Repository Structure](#repository-structure)
- [Algorithm](#algorithm)
- [Contributions](#contributions)
- [Video](#video)

## Overview

An IoT-based supply chain system integrates various components, including RFID tags, readers, sensors, and communication networks, to streamline operations and enhance visibility. The structure typically includes tagged items (products), RFID readers, a central IoT platform, and data analytics tools. RFID tags store unique identification information and other relevant data, which they transmit wirelessly when queried by an RFID reader. RFID readers are placed at strategic points along the supply chain to scan RFID tags and collect data. Subsequently, the information is relayed to the central IoT platform via communication networks. In this system model, the RFID tags and readers facilitate real-time tracking, inventory management, and data collection, significantly improving efficiency and accuracy in supply chain operations.

<div align="center">
    <img src="./Images/IoT-based Supply Chain System.jpg" alt="IoT-based Supply Chain System" width="700">
</div>

RFID security research is currently a significant focus globally, with numerous analysts dedicated to it. The adoption of RFID technology is gradually rising in the intelligence era. Consequently, various studies have expanded RFID applications in line with current social development and proposed security enhancement solutions. However, prevalent security threats, such as brute force attacks, remain significant.
## Repository Structure

The repository is organized as follows:

```plaintext
.
├── Code for each node
│   ├── attack.ipynb
│   ├── reader.ipynb
│   ├── supply.ipynb
│   └── tag.ipynb
├── Images
│   ├── IoT-based Supply Chain System.jpg
│   ├── Overall Attack Sketch.jpg
│   └── Protocol Messages.jpg
├── README.md
├── attack_ulbraps_text.py
└── traceability_ulbraps.py
```


### [Code for each node](Code%20for%20each%20node)
- **[reader.ipynb](Code%20for%20each%20node/reader.py)**: Description of what node1.py does.
- **[supply.ipynb](Code%20for%20each%20node/supply.py)**: Description of what node2.py does.
- **[tag.ipynb](Code%20for%20each%20node/tag.py)**: Description of what node3.py does.


### [Images](Images)
This directory holds image files used within the project.

- **[IoT-based Supply Chain System.jpg](Images/IoT-based-Supply-Chain-System.jpg)**: Message transfer between nodes was facilitated using Python socket programming.
- **[Protocol Messages.jpg](Images/Protocol-Messages.jpg)**: Message transfer between nodes was facilitated using Python socket programming.
<div align="center">
    <img src="./Images/Protocol Messages.jpg" alt="Protocol Messages" width="700">
</div>

- **[Overall Attack Sketch.jpg](Images/Overall-Attack-Sketch.jpg)**: Message transfer between nodes was facilitated using Python socket programming.
<div align="center">
    <img src="./Images/Overall Attack Sketch.jpg" alt="Overall Attack Sketch" width="500">
</div>

### [attack_ulbraps_text.py](attack_ulbraps_text.py)
This code demonstrates secret disclosure attacks within an acceptable complexity threshold to retrieve the session key (TKST). As discussed in the paper, if the balance amount (BalN) is a secret parameter and represents a unique value for the target Tag, the ULBRAP protocol is vulnerable to desynchronization attacks. Consequently, in this implementation attack, we assume that the BalN is known within the network, highlighting the protocol's susceptibility to a secret disclosure attack.

### [traceability_ulbraps.py](traceability_ulbraps.py)
The process of identifying, capturing, and maintaining the records of all activities related to a particular event or transaction. In ULBRAP Protocol, The adversary could trace the result of XOR-ed identifiers of the tag (IDNT) and the supply chain node (IDNS) by eavesdropping on the messages sent in two sessions. MESG1 and MESG2 allow the attacker to obtain 161 candidate values for the result of XORing IDNT and IDNS. In the second session, with different timestamps and random values but the same identifiers for the Tag and Supply chain, we again have 161 possible candidates for the result of XOR-ed identifiers of the tag (IDNT) and the supply chain node (IDNS). By checking the intersection of these two lists, we can determine the actual value of the result of XOR-ed IDNT and IDNS.

## [Algorithm](Algorithm)
The recovery $TK_{ST}$ attack consists of five main steps, detailed in the following Algorithm.

## Contributions

- Security evaluation of ULBRAP protocol by Sanjeev Kumar et al. and prove its vulnerability against desynchronization and traceability attacks.
-  Practical implementation of the attack method to prove the functionality of the attack method.
-  Introduce a secure authentication protocol that is suitable for lightweight IoT devices in 5G communication networks to solve ULBRAP issues.

## Video
A video demonstrating the attack and the process of finding the session key is available at this [link](https://drive.google.com/file/d/1pns3RpqtFBVC2AzzYCEh7WSZFBS97YhP/view?usp=sharing).

