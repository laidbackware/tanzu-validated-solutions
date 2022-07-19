import os
import compile_docs

base_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

def test_e2e():
  compile_docs.main()

def test_decode_json():
  manifest = compile_docs.decode_json(base_dir + "/src/build-manifests/tko-on-vsphere.json")
  assert manifest

def test_number_figures():
  '''Ensure figures are re-numbered'''
  markdown = "#heading\n\n\n![Figure 1 ]\n\ntest\n![Figure 05 ]\n\nFigure 05"
  returned_markdown = compile_docs.number_figures(markdown)
  expected = "#heading\n\n\n![Figure 01 ]\n\ntest\n![Figure 02 ]\n\nFigure 02"
  assert returned_markdown ==  expected