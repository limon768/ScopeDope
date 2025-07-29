# ScopeDope

**ScopeDope** is a simple and powerful Python tool that helps identify which subdomains fall within a defined IP scope. It resolves subdomains and checks if their resolved IPs match any IPs listed in a scope file.

> 🛠️ Created by **Abir Limon**

---

## 🛠️ Requirements

- Python 3.x
- Internet or internal DNS access for domain resolution
- No external libraries required

---

## 🚀 Usage

```bash
python3 scopedope.py -u subdomain.txt -i ips.txt -o web_scope.txt

⚙️ Options
Flag	Description
-u, --input	Input subdomain file (required)
-i, --ips	File containing in-scope IPs (required)
-o, --output	Output file for matching subdomains (required)

📂 Example Files

subdomain.txt

admin.example.com
mail.example.com
dev.example.com

ips.txt

203.0.113.10
192.168.1.5
10.0.0.9

🧪 Example Usage

python3 scopedope.py -u subdomain.txt -i ips.txt -o web_scope.txt

📜 Output (web_scope.txt)

mail.example.com

🤝 Credits

Developed with 💻 by Abir Limon