import os
import compile_docs

base_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

def test_e2e():
  compile_docs.main()

def test_decode_json():
  manifest = compile_docs.decode_json(base_dir + "/src/build-manifests/tko-on-vsphere.json")
  assert manifest