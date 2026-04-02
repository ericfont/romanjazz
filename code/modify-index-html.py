import os
import subprocess

revision_string = subprocess.run(
"""echo romanjazz.com v$(git rev-list --count HEAD) $(date -u +"%Y-%m-%d")""",
shell=True, capture_output=True, text=True).stdout

with open('code/scroll-list-display.html', 'r') as input_index_html, open('all-charts-tabs.txt', 'r') as input_all_charts_tabs, open('site/index.html', 'w') as output_index_html:
    for line in input_index_html:

        if "<head>" in line:
            output_index_html.write(f"<head><title>RomanJazz.com chord charts {revision_string}</title>")

        if "<script>" in line:
            output_index_html.write("<script>\nconst charts = \n`")

            for line2 in input_all_charts_tabs:
                output_index_html.write(line2)
            
            output_index_html.write("`;\n")

        else:
            output_index_html.write(line)