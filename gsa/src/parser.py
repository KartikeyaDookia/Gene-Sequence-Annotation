# src/parser.py
from Bio import SeqIO
import gzip

def parse_gff3(file_path):
    with gzip.open(file_path, 'rt') as f:
        for line in f:
            if line.startswith("#"):
                continue
            parts = line.strip().split('\t')
            if len(parts) == 9 and parts[2] == "gene":
                yield {
                    "seqid": parts[0],
                    "source": parts[1],
                    "type": parts[2],
                    "start": int(parts[3]),
                    "end": int(parts[4]),
                    "strand": parts[6],
                    "attributes": parts[8]
                }

def load_fasta(file_path):
    return SeqIO.to_dict(SeqIO.parse(file_path, "fasta"))
