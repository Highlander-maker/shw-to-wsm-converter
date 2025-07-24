# SHW to WSM Converter 🔁

A Python tool that converts `.shw` files from **Shure Wireless Workbench (WWB)** into `.wsm` files for import into **Sennheiser Wireless Systems Manager (WSM)**.

Built for production use by RF coordinators and system techs managing Sennheiser IEM deployments.

---

## ✨ Features

- Converts `.shw` (WWB) format to `.wsm` (Sennheiser WSM)
- Correctly maps band ranges:
  - `Gw` → 558000–626000  
  - `GBw` → 606000–678000  
  - `Aw+` → 470000–558000  
  - `Bw` → 626000–698000  
- Groups **2 receivers per device**
- Automatically assigns IP addresses and ports
- Outputs clean `.wsm` files into `converted_files/` folder

---

## 🧪 How to Use (CLI)

> 🐍 **Requirements**:
> - Python 3.8 or higher  
> - No external packages required

---

<pre lang="markdown">

### 📁 1. Folder Structure

Make sure your project is set up like this:

```
wwb-convertor/
├── input_files/              # Place your .shw files here
│   └── MultiRangeTest.shw
├── converted_files/          # Your converted .wsm files will appear here
├── shw_to_wsm_converter.py   # Python conversion script
└── README.md                 # This file
```
</pre>

---

### 📥 2. Add `.shw` File

Place the `.shw` file you exported from WWB into the `input_files/` folder.

---

### ▶️ 3. Run the Script

From the root directory, run:

```bash
python shw_to_wsm_converter.py

When prompted, type the name of your .shw file:

🔍 Enter just the name of the .shw file (in the input_files/ folder): MultiRangeTest.shw

📤 4. Get Your .wsm File

Once complete, your converted file will appear in the converted_files/ folder:

MultiRangeTest_FIXED_FINAL.wsm

You can now import this into Sennheiser Wireless Systems Manager (WSM).

⸻

🙌 Credits

Huge thanks to Liam Cartwright (Solotech) for providing XML structure insight and supporting the testing and formatting of this converter for real-world WSM deployments.

⸻

🚀 Roadmap

This CLI tool will soon be added to:

highlanderaudio.com

Allowing you to upload .shw files and download .wsm files via a simple web interface.

⸻
💬 Contact

For questions, bugs, or feature requests:
	•	🔗 rab@highlanderaudio.com
	•	💬 Raise an issue on GitHub (coming soon)

    Made with ❤️ by Highlander Audio for touring engineers and RF techs.
