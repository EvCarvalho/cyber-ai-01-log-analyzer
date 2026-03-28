# Cyber AI - Log Analyzer v1

from collections import defaultdict

log_file = "sample.log"
failed_attempts = defaultdict(int)

with open(log_file, "r") as file:
    for line in file:
        if "failed" in line:
            ip = line.split()[0]
            failed_attempts[ip] += 1

print("Relatório de IPs suspeitos:\n")

for ip, count in failed_attempts.items():
    if count >= 3:
        print(f"[ALERTA] {ip} - {count} tentativas falhas")
