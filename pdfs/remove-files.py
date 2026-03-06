import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

folder = r"."

for root, dirs, files in os.walk(folder):
  for file in files:
    if file.endswith('.pdf'):
      os.remove(os.path.join(root, file))