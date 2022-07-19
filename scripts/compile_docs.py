import json
import os
import re
import sys
from glob import glob
from pprint import pprint

base_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
manifest_dir = base_dir + "/src/build-manifests/*.json"
component_dir = base_dir + "/src/components"
ref_arch_dir = base_dir + "/src/reference-designs"

def main():
  for file_name in glob(manifest_dir):
    manifest = decode_json(file_name)
    ref_arch_name = os.path.basename(file_name)[:-5]
    rendered_sections = []
    
    for section in manifest:
      with open("{}/{}.md".format(component_dir, section), "r") as section_file:
        rendered_sections.append(section_file.read().rstrip("\n") + "\n\n")
    
    rendered_markdown = number_figures("".join(rendered_sections))

    with open("{}/{}.md".format(ref_arch_dir, ref_arch_name), 'w') as output_file:
      output_file.write(rendered_markdown)    

def decode_json(file_name):
  with open(file_name, "r") as file:
    try:
      return json.load(file)
    except Exception as exc:
      print("Json decoding failed with error " + str(exc), file=sys.stderr)
      raise SystemExit

def number_figures(rendered_markdown):
  '''Replace figure numbers to be incremental'''
  split_lines = rendered_markdown.splitlines()
  figure_number = 1
  for line_number, line_content in enumerate(split_lines):
    if "![Figure" in line_content:
      split_lines[line_number] = re.sub(r"Figure [0-9]+", f"Figure {str(figure_number).zfill(2)}", line_content)
      # Apply same figure number to any Figure footers
      if (line_number + 2) < len(split_lines) and re.match(r"^(?!!\[).*Figure [0-9]+", split_lines[line_number + 2]):
        split_lines[line_number + 2] = re.sub(r"Figure [0-9]+", f"Figure {str(figure_number).zfill(2)}",
                                              split_lines[line_number + 2])
      figure_number += 1
  return"\n".join(split_lines)

if __name__ == "__main__":
  main()