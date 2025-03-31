# 🦈 My current most used Wireshark Profiles for Threat Hunting and Malware analysis

This folder contains a curated collection of my **Wireshark profiles** tailored for threat hunting, Packet and Malware analysis. These profiles reflect my daily hunting workflows, optimized for spotting:

- Beaconing behavior (JA3, JA4+ fingerprinting)
- Suspicious DNS patterns (tunneling, C2 domains)
- TLS handshake metadata (SNI, cert info, JA3)
- HTTP anomalies (user-agents, redirect chains)
- Zeek-inspired network flow filtering
- And much more

## 📦 What's Inside

Each profile is organized as a standalone folder and includes:

- `colorfilters` → Custom color rules for visual triage
- `display_filters` → Common threat-hunting filters (JA3, DNS, HTTP anomalies)
- `preferences`, `layout` → UI/UX configurations for fast navigation

## 🚀 How to Import Wireshark Profiles

### 🪟 Windows

1. Locate the Wireshark profile directory (usually):

   ```
   C:\Users\<YourUsername>\AppData\Roaming\Wireshark\profiles\
   ```

2. Copy the profile folders from this repo into that directory.
3. Launch Wireshark → `Edit > Configuration Profiles` → Select your imported profile.

### 🐧 Linux

1. Navigate to:

   ```
   ~/.config/wireshark/profiles/
   ```

2. Clone or copy the profile folders here.
3. Start Wireshark and choose the profile from `Edit > Configuration Profiles`.

### 🍎 macOS

1. Go to:

   ```
   ~/Library/Application Support/Wireshark/profiles/
   ```

2. Paste the profile directories here.
3. Open Wireshark and switch profiles via `Edit > Configuration Profiles`.

## 🌍 Enable GeoIP Lookups (Optional but Recommended)

To enrich IP addresses with **country, city, ASN**, and other context:

1. Create a free MaxMind account:  
   👉 <https://www.maxmind.com/en/geolite2/signup>
2. Download the following **GeoLite2** databases:
   - `GeoLite2-City.mmdb`
   - `GeoLite2-ASN.mmdb`
   - `GeoLite2-Country.mmdb`
3. Place them in a local folder (e.g., `~/GeoIP/`)
4. In Wireshark:
   - Go to `Edit > Preferences > Name Resolution`
   - Check `Enable GeoIP lookups`
   - Set the path for **MaxMind DB directories**

## ✅ Status

🛠️ Please be advised that those profiles are not a magic bullet and still under **development**

## 🤝 Contributions

Pull requests welcome — especially if you have hunting-focused profile setups or layout enhancements to share.

## 📜 License

MIT
