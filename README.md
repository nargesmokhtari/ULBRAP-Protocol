## Security Analysis of ”Ultra-Lightweight Blockchainenabled RFID Authentication Protocol for Supply Chain in the domain of 5G Mobile Edge Computing"
## Table of Contents
- [Overview](#overview)
- [Repository Structure](#repository-structure)
- [Contributing](#contributing)
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

## The primary contribution of this study may be summed up as follows:
- Security evaluation of ULBRAP protocol by Sanjeev Kumar et al. and prove its vulnerability against desynchronization and traceability attacks.
-  Practical implementation of the attack method to prove the functionality of the attack method.
-  Introduce a secure authentication protocol that is suitable for lightweight IoT devices in 5G communication networks to solve ULBRAP issues.

<div align="center">
    <img src="./Images/Protocol Messages.jpg" alt="Protocol Messages" width="700">
</div>

<div align="center">
    <img src="./Images/Overall Attack Sketch.jpg" alt="Overall Attack Sketch" width="500">
</div>

A video demonstrating the attack and the process of finding the session key is available at this [link](https://drive.google.com/file/d/1pns3RpqtFBVC2AzzYCEh7WSZFBS97YhP/view?usp=sharing).

