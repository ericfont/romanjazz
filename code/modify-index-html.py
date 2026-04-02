import os
import subprocess

# Run command and capture output
revision_command_result = subprocess.run(
"""echo romanjazz.com git revision $(git rev-list --count --all) on $(date -u +"%Y-%m-%d_%H:%M") UTC.""",
shell=True, capture_output=True, text=True)

revision_string = revision_command_result.stdout

with open('code/scroll-list-display.html', 'r') as input_index_html, open('site/index.html', 'w') as output_index_html:
    for line in input_index_html:

        if "<script>" in line:
            output_index_html.write(f"<p>{revision_string}</p>\n")

        output_index_html.write(line)