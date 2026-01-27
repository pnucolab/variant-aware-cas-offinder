# Variant Aware Cas-OFFinder pipeline
## The new Cas-OFFinder pipeline

Cas-OFFinder is a highly efficient and adaptable program built upon OpenCL that identifies potential off-target sites of CRISPR/Cas-derived RNA-guided endonucleases (RGENs).
Cas-OFFinder is not limited by the number of mismatches and accommodates variations in the protospacer-adjacent motif (PAM) sequences recognized by Cas9, which is the crucial protein component in RNA-guided endonucleases (RGENs).
An OpenCL device is essential for optimal functionality.
This newly designed pipeline incorporates Single Nucleotide Polymorphisms (SNPs) into the search criteria for both on-target and potential off-target sites. This tool addresses specific challenges encountered when relying solely on reference genomes for predicting on-target potential off-target sites. Reference genomes are typically generated from the genetic material of a limited number of individuals, resulting in a representation that often falls short of capturing the complete genetic diversity within a species. Our platform empowers users to identify potential off-target sites by incorporating a reference genome and individual genetic variants. 
This tool is available in both web and command-line interfaces. The Cas-OFFinder web tool is user-friendly, and the entire website has undergone a renovation, transitioning from the previous interface at CRISPR RGEN Tools (rgenome.net) to a new one based on cutting-edge web technologies such as SvelteKit, FastAPI, Celery, duckdb, and Redis to enhance the user experience.

## Usage
- Download requirements.txt and vcf-cas-offinder.py and Install all dependencies listed in the requirements.txt file using the command:
   ```
   pip install —no-cache-dir -r requirements.txt
   ```
- Download the Cas-OFFinder binary file and extract and save it in the same directory with vcf-cas-offinder.py
  ```
  https://github.com/snugel/cas-offinder/releases/tag/2.4.1
  ```
- To install the vcflib package using conda, execute the following command:
  ```
   conda install -c bioconda vcflib=1.0.3 tabixpp=1.1.0
  ```
- Then, download the chromosome FASTA files for any target organism. You can find one using the links below or you can use any other sources: 
    - For Vertebrates
      ```
      https://ftp.ensembl.org/pub/
      ```
    - For Plants
      ```
      https://ftp.ensemblgenomes.ebi.ac.uk/pub/plants/
      ```
- Extract all FASTA files into a directory and index them within the same directory.
   ```
   samtools faidx ref.genome
   ```
- Ensure that the “+x” flag is added to the input_vcf_file, and the target organism’s reference genome directory.
- Now, the new Cas-OFFinder pipeline can run with:
  ```
  ./vcf-cas-offinder.py -i input_vcf_file_path -r reference_genome_path -t target_sequence_input_file_name -d device_id
  ```
   - for device_id you can use G, C or A
    - G represents using GPU devices, while C stands for CPUs. A represents accelerators. If you have multiple GPU or CPU IDs, you can specify them as G0 for GPU device ID 0 and 
      G1 for ID 1 to limit the number of devices used. 
- For a short help, try running ./vcf-cas-offinder.py -h
  ```
  ./vcf-cas-offinder.py -h
  ```
  ```
  usage: vcf-cas-offinder.py [-h] -i INPUT -r REF_PATH -t QUERY_INPUT -d DEVICE_ID

  Identify potential off-target sites based on VCF files.

  options:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        Path to the input VCF (Phased and single sample) file
  -r REF_PATH, --ref_path REF_PATH
                        Path to the target organism reference genome
  -t QUERY_INPUT, --query_input QUERY_INPUT
                        target sequence in the target organism genome (input.txt file)
  -d DEVICE_ID, --device_id DEVICE_ID
                        device_id(s): C for CPU and G for GPU, G0 for GPU device id=0

  ```
- You should create an input.txt file in the same directory with vcf-cas-offinder.
     -  An example of an input file:
     ```
      NNNNNNNNNNNNNNNNNNNNGG
      GTGAAATCTAAGTGTAGAGNNN 2
      TTGTGAAATCTAAGTGTAGNNN 2
      CTTCACAATTATTCGCCCANNN 2
      GGGCGAATAATTGTGAAGGNNN 2
      CTTACAGAAACACCTGTTANNN 2
      AGATTCAAGAATTGGTACGNNN 2
      AACCTTCAGTTAGTCGCTANNN 2
      CACCATAGCGACTAACTGANNN 2
      AGCTCAGGAAGGCCCTCATNNN 2
     ```
    - The first line indicates the desired pattern including PAM site
    - The remaining lines are the query sequences and maximum mismatch numbers, separated by spaces
    - **The length of the desired pattern and the query sequences should be the same**!
- Now you can run vcf-Cas-OFFinder as follows (using GPUs):
  ```
  ./vcf-cas-offinder.py -i /home/user/Documents/vcf_files/bgzipresultcm334.vcf.gz -r /home/user/genome/pepper_ref/GCA_000512255.2_ASM51225v2_genomic.fa -t input.txt -d G1
  ```
-  Sample results are shown below
  ```
GTGAAATCTAAGTGTAGAGNNN	CVCM334_CM008455.1:0	15539504	aaGAAATCTAAGTGTAGAGTGG	-	2
TTGTGAAATCTAAGTGTAGNNN	CVCM334_CM008455.1:0	195285628	TTtTGAAAaCTAAGTGTAGAGG	+	2
GTGAAATCTAAGTGTAGAGNNN	CVCM334_CM008455.1:1	15539613	aaGAAATCTAAGTGTAGAGTGG	-	2
TTGTGAAATCTAAGTGTAGNNN	CVCM334_CM008455.1:1	195287846	TTtTGAAAaCTAAGTGTAGAGG	+	2
GTGAAATCTAAGTGTAGAGNNN	CVCM334_CM008456.1:0	150109371	GTGAAATCTAAGTGTAGAGGGG	-	0
TTGTGAAATCTAAGTGTAGNNN	CVCM334_CM008456.1:0	29642154	TTGTGAgtTCTAAGTGTAGCGG	+	2
TTGTGAAATCTAAGTGTAGNNN	CVCM334_CM008456.1:0	77628291	TTGTcAAATCTAAGaGTAGAGG	+	2
TTGTGAAATCTAAGTGTAGNNN	CVCM334_CM008456.1:0	95688428	TTGTGAAAaCTAAGTGTAaAGG	-	2
TTGTGAAATCTAAGTGTAGNNN	CVCM334_CM008456.1:0	150109373	TTGTGAAATCTAAGTGTAGAGG	-	0
CTTCACAATTATTCGCCCANNN	CVCM334_CM008456.1:0	150076867	CTTCAtAgTTATTCGCCCAAGG	+	2
CTTCACAATTATTCGCCCANNN	CVCM334_CM008456.1:0	150071663	CTTCAtAgTTATTCGCCCAAGG	+	2
CTTCACAATTATTCGCCCANNN	CVCM334_CM008456.1:0	150089959	CTTCAtAATTATTtGCCCAAGG	+	2
CTTCACAATTATTCGCCCANNN	CVCM334_CM008456.1:0	150109711	CTTCACAATTATTCGCCCAAGG	-	0
CTTCACAATTATTCGCCCANNN	CVCM334_CM008456.1:0	150133601	CTTCAtAATTATTtGCCCAAGG	-	2
GGGCGAATAATTGTGAAGGNNN	CVCM334_CM008456.1:0	150076863	GGGCGAATAAcTaTGAAGGTGG	-	2
GGGCGAATAATTGTGAAGGNNN	CVCM334_CM008456.1:0	150071659	GGGCGAATAAcTaTGAAGGTGG	-	2
GGGCGAATAATTGTGAAGGNNN	CVCM334_CM008456.1:0	150089955	GGGCaAATAATTaTGAAGGTGG	-	2
GGGCGAATAATTGTGAAGGNNN	CVCM334_CM008456.1:0	150109715	GGGCGAATAATTGTGAAGGTGG	+	0
GGGCGAATAATTGTGAAGGNNN	CVCM334_CM008456.1:0	150133605	GGGCaAATAATTaTGAAGGTGG	+	2
GTGAAATCTAAGTGTAGAGNNN	CVCM334_CM008456.1:1	150111631	GTGAAATCTAAGTGTAGAGGGG	-	0
TTGTGAAATCTAAGTGTAGNNN	CVCM334_CM008456.1:1	29642642	TTGTGAgtTCTAAGTGTAGCGG	+	2
TTGTGAAATCTAAGTGTAGNNN	CVCM334_CM008456.1:1	77629000	TTGTcAAATCTAAGaGTAGAGG	+	2
TTGTGAAATCTAAGTGTAGNNN	CVCM334_CM008456.1:1	95689442	TTGTGAAAaCTAAGTGTAaAGG	-	2
TTGTGAAATCTAAGTGTAGNNN	CVCM334_CM008456.1:1	150111633	TTGTGAAATCTAAGTGTAGAGG	-	0
CTTCACAATTATTCGCCCANNN	CVCM334_CM008456.1:1	150079117	CTTCAtAgTTATTCGCCCAAGG	+	2
CTTCACAATTATTCGCCCANNN	CVCM334_CM008456.1:1	150073913	CTTCAtAgTTATTCGCCCAAGG	+	2
CTTCACAATTATTCGCCCANNN	CVCM334_CM008456.1:1	150092209	CTTCAtAATTATTtGCCCAAGG	+	2
CTTCACAATTATTCGCCCANNN	CVCM334_CM008456.1:1	150135873	CTTCAtAATTATTtGCCCAAGG	-	2
CTTCACAATTATTCGCCCANNN	CVCM334_CM008456.1:1	150111971	CTTCACAATTATTCGCCCAAGG	-	0
GGGCGAATAATTGTGAAGGNNN	CVCM334_CM008456.1:1	150111975	GGGCGAATAATTGTGAAGGTGG	+	0
GGGCGAATAATTGTGAAGGNNN	CVCM334_CM008456.1:1	150135877	GGGCaAATAATTaTGAAGGTGG	+	2
GGGCGAATAATTGTGAAGGNNN	CVCM334_CM008456.1:1	150079113	GGGCGAATAAcTaTGAAGGTGG	-	2
GGGCGAATAATTGTGAAGGNNN	CVCM334_CM008456.1:1	150073909	GGGCGAATAAcTaTGAAGGTGG	-	2
GGGCGAATAATTGTGAAGGNNN	CVCM334_CM008456.1:1	150092205	GGGCaAATAATTaTGAAGGTGG	-	2
  ```
-  from the second column, 0 after colon represents allele 1, and 1 represents allele 2 for each chromosome. In the example shown above CVCM334_CM008455, CVCM334_CM008456, etc are chromosomes identifiers found in the reference genome. 
