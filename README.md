# Hack the Orbit

## Setting Up

1. Download Python and Pip3

```
# Verify Python3 is installed
python3 --version

# Verify Pip3 is installed
pip3 --version
```

2. Clone the Repository

```
git clone https://github.com/ANG13T/hack-the-orbit.git
```

3. Install the Required Libraries

```
pip3 install -r requirements.txt
```

4. Run the Program

```
python3 main.py
```


### STORY CONTEXT

### Notes to Self
FOLDER STRUCTURE

-> PROGRAMS
-> OBTAIN TLE

COMMANDS AVAILABLE

ls -> list all the files in the current directory
cd -> change directory


cd into `/usr/local/bin`

COMMANDS AND UTILIES 


### TODO
Implement usages

```
COMMANDS = {
    "ls": {
        description: "List files in the current directory",
        usage: "ls [path]"
    },
```

EXHAUST THE FOLLOWING
- [ ] man: descriptions ONLY of the executable files (WIP)


OTHER:
- remove None from help
- display all the executables

cat a text file including the satellite subsystem information

### Ground Station Features
1. Input the correct frequency
2. Input the correct demodulation waveform
3. Input the correct decoding algorithm

LIST OUT AVAILABLE MODULATION SCHEMES 

LIST OUT AVAILABLE DECODING ALGORITHMS

>>> SYSTEM ALERT
**Captured Signal Segment:**
 - File: **Captured_Signal_01.wav**
 - Data Integrity: **94%**

### CCSDS Packet Analysis

```
# Primary Header (6 bytes)
Version: 0001
Packet Type: 0000
Packet Length: 0036

# Secondary Header (10 bytes)
Timestamp: 2024-09-12T14:55:23Z
Subsystem: Communications

# User Data (transponder telemetry) (20 bytes)
Power Level: 34.7 dBm
Frequency: 8.125 GHz
EIRP: 49.5 dBW
Temperature: 85°C
**Power Override Command**: 0x00 (Normal Operation)
                         -> (0x01 causes an over-voltage failure)
                         
# Error Control Field (4 bytes)
CRC: ABCD
```


```
Primary Header (6 bytes):
0001 0000 0000 0000 0000 0011 0010

Secondary Header (10 bytes):
2024-09-12T14:55:23Z
Communications Subsystem ID

User Data (20 bytes):
Power Level: 34.7 dBm -> 00100010.10110011
Frequency: 8.125 GHz -> 10000010.00011101
EIRP: 49.5 dBW -> 00110001.10100111
Temperature: 85°C -> 01010101
Power Override Command: 0x00 (Safe) / 0x01 (Override)
                         -> 00000000 / 00000001

Error Control (CRC): ABCD -> 1010101111001101
```
```
Primary Header (6 bytes):
0001 0000 0000 0000 0000 0011 0010

Secondary Header (10 bytes):
01100110 10001101 01101011 11101011 00000000 00000000 00000000 11000001

User Data (20 bytes):
00100010 10110011 10000010 00011101 00110001 10100111 01010101 00000000 / 00000001

Error Control (CRC):
1010101111001101
```

MAX Power LEVEl: Power Level: 50Bm

PUT the packet into override mode

TODO:
- walkthrough the CTF and then take screenshots
- finish the presentation
- code and solution obfuscation
- workshop logistis and trial run