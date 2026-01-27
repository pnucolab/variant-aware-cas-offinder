How to use the web interface
============================

Variant-aware Cas-OFFinder web tool works well in the following operating systems and web browsers.

- Supported Operating Systems:
    - Windows
    - macOS
    - Linux

- Supported web browsers:
    - Google Chrome
    - Mozilla Firefox
    - Microsoft Edge
    - Safari

To get started, navigate to https://rgetoolkit.com/ and explore the platform's features. 
A Sample VCF file is provided for new users, which can be easily downloaded by clicking on the link. 
This sample file serves as a great starting point for familiarizing yourself with the tool's capabilities.
The platform's default settings include:

- Target Genome: Homo sapiens (GRCh38/hg38) - Human
- PAM Type: SpCas9 from Streptococcus pyogenes: 5'-NRG-3
- Query Sequence: CAGCAACTCCAGGGGGCCGC
- Mismatches: 3

After downloading the sample VCF file, click "Submit" to process it with the default parameters and wait until the result is available. 
For more customized analysis, users have the option to upload their own VCF file 
(Supported file formats: [.vcf, .vcf.gz (gzipped and bgzipped file)]) and select from a range of parameters to tailor the analysis to 
their specific needs. For faster execution, upload a VCF file that contains a limited number of chromosomes, like 2 or 3. 

The User can follow the steps below to select a few chromosomes from a VCF file after installing tabix and bcftools.

Unzip if it is zipped:

.. code-block:: bash

   gunzip Sample.vcf.gz

bgzip the VCF File:

.. code-block:: bash

   bgzip -c Sample.vcf > Sample.vcf.gz

Index bgzip VCF File:

.. code-block:: bash

    tabix -p vcf Sample.vcf.gz

Filter a few chromosomes VCF data (not mandatory but better for faster processing time):

.. code-block:: bash

   bcftools view -r chr6,chr10 NA12878.vcf.gz -o Output.vcf.gz

Make sure the above tools are installed on your machine. After all these steps, your VCF file is ready to be uploaded for processing. 

These default settings provide a solid foundation for analysis, but the ability to customize parameters ensures that users can adapt 
the tool to their unique research requirements.
Once the analysis is complete, the results will be ready. The users can download the results if they want. 

Our tool is designed to deliver a smooth user experience. If an issue arises, we provide clear and actionable error messages to help the user resolve any problems.

Common error messages and solutions
-----------------------------------
1. Your file is not a phased VCF file.
    -  What It Means: This occurs when you upload not pahsed vcf file. 
    -  What to Do: Ensure your VCF file is phased. You can use GATK, Octopus, or other variant callers to prepare a phased VCF file. 
2. Your file is a multi-sample VCF file.
    -  What It Means: This happens when you upload multiple sample VCF file.
    -  What to Do: Please make sure that your VCF file contains only a single sample. Our web tool accepts only phased single sample vcf file to identify on-target and potential 
       off-target sites in the entire individual genome. 


