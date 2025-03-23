#include <ESP8266WiFi.h>
#include <WiFiClient.h>
#include <WiFiServer.h>
#include <Hash.h>
#include <ArduinoJson.h>

int stop_time = 5000;

// WiFi Credentials
const char* ssid = "samsung";
const char* password = "*2018@AMIR";

// Server and client configurations
const char* reader2_ip = "192.168.1.105";
const char* attacker_ip = "192.168.1.101";
const char* tag2_ip = "192.168.1.102";
const char* supply_ip = "192.168.1.103";
const uint16_t PORT = 8713;

// WiFi client for connecting to reader2
WiFiClient reader2_client;

// Convert integer to binary string
String intToBinary(uint32_t num, int bits) {
    String binString = "";
    for (int i = bits - 1; i >= 0; i--) {
        binString += (num & (1 << i)) ? '1' : '0';
    }
    return binString;
}

// Function to convert hexadecimal string to binary string
String hex_to_bin(const String &hex) {
    String bin = "";
    for (int i = 0; i < hex.length(); i++) {
        String hexDigit = hex.substring(i, i + 1);
        int digit = strtol(hexDigit.c_str(), NULL, 16);
        bin += String(digit, BIN).substring(4);  // Extract 4 bits (binary) for each hex digit
    }
    return bin;
}

// XOR operation for two binary strings
String binaryXOR(String a, String b) {
    String result = "";
    int maxLength = max(a.length(), b.length());
    while (a.length() < maxLength) a = "0" + a;
    while (b.length() < maxLength) b = "0" + b;

    for (int i = 0; i < maxLength; i++) {
        result += (a[i] == b[i]) ? '0' : '1';
    }
    return result;
}

// Rotate a binary string left
String rotateLeft(String bin, int shift) {
    int len = bin.length();
    shift = shift % len;
    return bin.substring(shift) + bin.substring(0, shift);
}

// Rotate a binary string right
String rotateRight(String bin, int shift) {
    int len = bin.length();
    shift = shift % len;
    return bin.substring(len - shift) + bin.substring(0, len - shift);
}

// Count '1' bits in binary string
int countOneBits(String bin) {
    int count = 0;
    for (int i = 0; i < bin.length(); i++) {
        if (bin[i] == '1') count++;
    }
    return count;
}

// SHA-1 hash function (Modified)
// String hashBinary(String bin) {
//     return sha1(bin);
// }

// Function to convert a binary string to SHA-1 hash (hex)
String hashBinary(String binaryString) {
    // Convert binary string to raw bytes (20 bytes for 160 bits)
    uint8_t byteArray[20] = {0};  // 160 bits = 20 bytes

    for (int i = 0; i < 20; i++) {
        String byteString = binaryString.substring(i * 8, (i + 1) * 8); // Get 8-bit chunks
        byteArray[i] = strtoul(byteString.c_str(), nullptr, 2); // Convert 8-bit chunk to byte
    }

    // Compute SHA-1 hash using built-in function
    String sha1Hash = sha1(byteArray, 20);

    // Return hash in hex format prefixed with 0x
    return "0x" + sha1Hash;
}

void setup() {
    Serial.begin(115200);
    WiFi.mode(WIFI_STA);

    // Connect to WiFi
    WiFi.begin(ssid, password);
    Serial.print("Connecting to WiFi ");
    while (WiFi.status() != WL_CONNECTED) {
        delay(1000);
        Serial.print(".");
    }
    Serial.println("\nConnected to WiFi!");

    // Connect to reader2
    if (reader2_client.connect(reader2_ip, PORT)) {
        Serial.println("Connected to Reader2");
    } else {
        Serial.println("Connection failed!");
        return;
    }

    // Receive initial data (JSON)
    while (!reader2_client.available()) {
        delay(100);
    }
    String jsonString = reader2_client.readStringUntil('\n');
    Serial.println("Received: " + jsonString);
    reader2_client.println("ok esp");

    // Parse JSON data
    StaticJsonDocument<256> doc;
    deserializeJson(doc, jsonString);
    String BalN_bin = doc["BalN_bin"];
    String BS_bin = doc["BS_bin"];
    String IDNr_bin = doc["IDNr_bin"];
    String IDNt_bin = doc["IDNt_bin"];
    String IDNs_bin = doc["IDNs_bin"];

    // Receive Message 1
    while (reader2_client.available() == 0) {
      delay(100);
    }
    jsonString = reader2_client.readStringUntil('\n');
    Serial.println("Session2, Message 1 Received: " + jsonString);
    deserializeJson(doc, jsonString);
    String PR_bin = doc["PR_bin"];
    String CHR_hex = doc["CHR_hex"];
    String TIR_bin = doc["TIR_bin"];
    // reader2_client.println("ok");

    // delay(1000);

    // Generate Random TIT_bin (32 bits)
    uint32_t TIT_int = random(0, 0x7FFFFFFF);
    String TIT_bin = intToBinary(TIT_int, 32);

    // Extract R0
    String shift_amount_bin = binaryXOR(IDNt_bin, TIR_bin);
    int shift_amount = countOneBits(shift_amount_bin);
    String shifted_number_bin = rotateRight(PR_bin, shift_amount);
    String R0_bin = binaryXOR(shifted_number_bin, IDNt_bin);
    R0_bin = binaryXOR(R0_bin, TIR_bin);

    // Compute CHT
    String pre_CHT_bin = binaryXOR(R0_bin, IDNt_bin);
    pre_CHT_bin = binaryXOR(pre_CHT_bin, BalN_bin);
    String CHT_hex = hashBinary(pre_CHT_bin);

    // Compute PT
    String PT_1_bin = binaryXOR(R0_bin, IDNs_bin);
    PT_1_bin = binaryXOR(PT_1_bin, TIT_bin);
    String PT_2_bin = binaryXOR(TIT_bin, IDNt_bin);
    int rotate_count = countOneBits(PT_2_bin);
    String PT_bin = rotateLeft(PT_1_bin, rotate_count);

    // Compute AthR
    String CHT_bin = intToBinary(strtol(CHT_hex.c_str(), NULL, 16), 160);
    String pre_AthR_bin = binaryXOR(CHT_bin.substring(2), R0_bin);

    pre_AthR_bin = binaryXOR(pre_AthR_bin, PT_bin);
    pre_AthR_bin = binaryXOR(pre_AthR_bin, IDNt_bin);
    pre_AthR_bin = binaryXOR(pre_AthR_bin, TIT_bin);
    String AthR_hex = hashBinary(pre_AthR_bin);

    // Send Message 2
    // delay(stop_time-3000);

    StaticJsonDocument<256> msg2;
    msg2["CHT_hex"] = CHT_hex;
    msg2["AthR_hex"] = AthR_hex;
    msg2["PT_bin"] = PT_bin;
    msg2["TIT_bin"] = TIT_bin;
    String msg2_json;
    serializeJson(msg2, msg2_json);
    reader2_client.println(msg2_json);
    Serial.println("Session2, Message 2 Sent: " + msg2_json);
}

void loop() {
    // Keep connection alive if needed
}

