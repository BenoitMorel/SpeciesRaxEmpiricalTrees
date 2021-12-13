import ete3

input_path = "trees/archaea364/generax-MiniNJ-prune-nodup-fam_raxml-ng.LG+G.speciesTree.newick"
output_path = "trees/archaea364/generax_shortnames.newick"

tree = ete3.Tree(input_path)

taxon_set = set()


for leaf in tree.get_leaves():
  sp = leaf.name.split("-")
  basename = "-".join(sp[0:3])
  name = basename
  i = 2
  while name in taxon_set:
    name = basename + "-" + str(i)
    i += 1
  leaf.name = name
  taxon_set.add(leaf.name)
  print(leaf.name)

tree.write(format = 1, outfile = output_path)

