import re

sli = "[S] [B] [B] [F] [H] [C] [B] [N] [L]"
sli2= "[S] [B] [B] [F] [H] [C]     [N] [L]"

yyy = re.findall(r'(\[.\]|    )', sli2)
print (yyy)