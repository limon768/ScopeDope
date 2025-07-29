📄 README.md

# ScopeDope

**ScopeDope** is a simple and powerful Python tool that helps identify which subdomains fall within a defined IP scope. It resolves subdomains and checks if their resolved IPs match any IPs listed in a scope file.

> 🛠️ Created by **Abir Limon**

---

## 🔍 Features

- Resolves subdomains to IPs
- Matches resolved IPs against a list of in-scope IPs
- Outputs subdomains that are within scope
- Verbose logging with ASCII banner
- Easy command-line usage with `-u`, `-i`, and `-o` flags

---

## 📦 Requirements

- Python 3.x
- Internet or internal DNS access for domain resolution
- No external libraries required

---

## 🚀 Usage

```bash
python3 scopedope.py -u subdomain.txt -i ips.txt -o web_scope.txt
```

Options:
Flag	Description
-u or --input	File containing subdomains (one per line)
-i or --ips	File containing in-scope IPs (one per line)
-o or --output	File to write in-scope subdomains to
📁 Example

subdomain.txt

admin.example.com
mail.example.com
dev.example.com

ips.txt

192.168.1.10
10.0.0.5
203.0.113.7

Command

python3 scopedope.py -u subdomain.txt -i ips.txt -o web_scope.txt

Output (web_scope.txt)

mail.example.com
