from src.parser import parse_gff3
from src.annotator import annotate_genes
from src.visualizer import plot_gene_locations

def main():
    gff3_path = "data/raw/gencode.v48.annotation.gff3.gz"
    annotations = list(parse_gff3(gff3_path))
    annotated = annotate_genes(annotations)
    plot_gene_locations(annotated)

if __name__ == "__main__":
    main()
