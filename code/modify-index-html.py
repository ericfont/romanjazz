import os
from pydoc import text
import subprocess
from pathlib import Path

revision_string = subprocess.run(
"""echo -n romanjazz.com v$(git rev-list --count HEAD) $(date -u +"%Y-%m-%d")""",
shell=True, capture_output=True, text=True).stdout

with open('code/index.html', 'r') as input_index_html, open('site/all-charts-tabs.txt', 'w') as output_all_charts_tabs, open('site/index.html', 'w') as output_index_html:
    for line in input_index_html:

        if "<head>" in line:
            output_index_html.write(f"<head><title>RomanJazz.com chord charts {revision_string}</title>")
        elif "const charts =" in line:
            break
        else:
            output_index_html.write(line)
    
    # Write the charts and the tail of the file
    output_index_html.write("const charts = [")

    for file in Path('charts').rglob('*.tsv'):
        if file.is_file():
            filestem = file.stem
            filestem = filestem.replace("_", " ")
            output_all_charts_tabs.write(f'{filestem}\n')

            song_title, sep, song_metadata = filestem.partition(" ")

            output_index_html.write(f"[`{song_title}`, `{song_metadata}`,\n")

            with open(file, 'r') as src:
                song_contents = src.read();
                output_index_html.write(f"`{song_contents}`],\n")
                output_all_charts_tabs.write(f"{song_contents}\n")
            
    output_index_html.write(f"[``,``,``]\n")
    output_index_html.write("];\nmain();\n</script></body></html>")