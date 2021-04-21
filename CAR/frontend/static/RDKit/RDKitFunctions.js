var Module = {
  onRuntimeInitialized: initRDKitModule().then(function (instance) {
    Module = instance;
    console.log("version: " + Module.version());
  }),
};

function checkmol(text) {
  if (text.length > 0) {
    var mol = Module.get_mol(text);
    if (mol.is_valid()) {
      return mol;
    } else {
      return false;
    }
  } else {
    return false;
  }
}

function getsvg(mol) {
  var svg = mol.get_svg();
  return svg;
}

function comparesmiles(mol1, mol2) {
  var smiles1 = mol1.get_smiles();
  var smiles2 = mol2.get_smiles();

  if (smiles1 === smiles2) {
    return true;
  } else {
    return false;
  }
}
