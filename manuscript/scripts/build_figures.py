#!/usr/bin/env python3
"""Rebuild the nine integrated figures without modifying any original inputs."""
from pathlib import Path
import subprocess,sys,shutil

root=Path(__file__).resolve().parents[1]
source=root/'figures/integrated_sources'
destination=root/'figures/integrated'
destination.mkdir(exist_ok=True)
scripts=['fig1_two_track_journal.py','fig2_counterexample.py','fig3_timeline.py',
         'fig4_attributes.py','fig5_validation_programme.py','figS1_strain_definitions.py',
         'figS2_error_attributes.py','figS3_training_inference.py','graphical_abstract.py']
for script in scripts:
    subprocess.run([sys.executable,str(source/'src'/script)],check=True)
for file in (source/'out').glob('*'):
    if file.suffix in {'.pdf','.svg','.png'}:
        shutil.copy2(file,destination/file.name)
print('Updated integrated PDF, SVG and PNG derivatives.')
