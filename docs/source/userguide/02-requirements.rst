
Requirements
============

Supported File Format
---------------------

The variant-aware Cas-OFFinder tool supports the following file formats for processing and analysis.

- **.vcf**: Variant Call Format files, used for storing genomic variants
- **.vcf.gz**: Compressed VCF files, either .gz or bgzip VCF files.

Ensure your input file is in one of these formats for compatibility with the tool.

Required Tools for CLI and Local Deployment
-------------------------------------------

For users who prefer to work via the **command-line interface** or **deploy Variant-aware Cas-OFFinder locally**, the following tools are required:

1. **OpenCL device**

2. bcftools: a utility for manipulating and filtering VCF files.

   - Create a conda environment

   .. code-block:: bash
    
      conda create -n cas-offinder

   - install bcftools via conda:

     .. code-block:: bash
    
        conda install -c bioconda bcftools

   - bcftools can be used to filter specific chromosomes.

    .. code-block:: bash
  
       bcftools view -r chr6,chr10 Sample.vcf.gz -o Output.vcf.gz


3. tabix: A tool for indexing VCF files. It is used for fast random access to VCF files.

    - install tabix via conda:

    .. code-block:: bash
  
       conda install -c bioconda tabix

    - For indexing a VCF file:

    .. code-block:: bash
      
       tabix -p vcf Sample.vcf.gz
