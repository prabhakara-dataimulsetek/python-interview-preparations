from pathlib import Path
import subprocess, sys

root = Path(__file__).parent
for py in sorted(root.glob('*/*.py')):
    print(f'Running {py.relative_to(root)}')
    subprocess.run([sys.executable, str(py)], check=True)
print('All examples ran successfully.')
