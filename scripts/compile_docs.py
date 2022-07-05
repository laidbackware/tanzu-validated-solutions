import json
import os
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
    rendered_markdown = ""
    
    for section in manifest:
      with open("{}/{}.md".format(component_dir, section), "r") as section_file:
        rendered_markdown += section_file.read().rstrip("\n") + "\n\n"
    
    with open("{}/{}.md".format(ref_arch_dir, ref_arch_name), 'w') as output_file:
      for section in manifest:
        output_file.write(rendered_markdown)    

def decode_json(file_name):
  with open(file_name, "r") as file:
    try:
      return json.load(file)
    except Exception as exc:
      print("Json decoding failed with error " + str(exc), file=sys.stderr)
      raise SystemExit

if __name__ == "__main__":
  main()