import os
import subprocess

# Run command and capture output
revision_command_result = subprocess.run(
"""echo romanjazz.com git revision $(git rev-list --count HEAD) on $(date -u +"%Y-%m-%d_%H:%M") UTC.""",
shell=True, capture_output=True, text=True)

revision_string = revision_command_result.stdout

with open('code/scroll-list-display.html', 'r') as input_index_html, open('all-charts-tabs.txt', 'r') as input_all_charts_tabs, open('site/index.html', 'w') as output_index_html:
    for line in input_index_html:

        if "<script>" in line:
            output_index_html.write(f"<p>{revision_string}</p>\n<script>\nconst charts = [\n")

            for line2 in input_all_charts_tabs:
                output_index_html.write(line2)
            
            output_index_html.write("[`END`,``]];\n")

        else:
            output_index_html.write(line)