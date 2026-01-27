

Best Practices
==============

Best Practices for Optimizing Performance with Large VCF Files
--------------------------------------------------------------

When working with large VCF files, it is **recommended (but not mandatory)** to follow these best practices to minimize processing time. 

1. Filter Chromosomes for Targeted Processing

For Faster execution time, **filter specific chromosomes** before using the input VCF file once. You can filter 2 or 3 chromosomes once from the available VCF file and upload it separately. 

Example:

Use bcftools to extract data for specific chromosomes:

.. code-block:: bash
  
   bcftools view -r chr6,chr10 NA12877.vcf.gz -o Filtered_Sample.vcf.gz

Upload the filtered file (Filtered_Sample.vcf.gz) instead of the original, which can significantly decrease processing time.

2. Use bgzip for Compression to Enhance Performance

If your VCF file is in .vcf or .vcf.gz (compressed with standard gzip) format but not compressed using bgzip, you can compress it with bgzip before uploading it.

  - If the file is .vcf (uncompressed), compress it with bgzip:

  .. code-block:: bash

     bgzip -c Sample.vcf > Sample.vcf.gz

  - Index the bgzip-compressed file for faster access

  .. code-block:: bash

      tabix -p vcf Sample.vcf.gz

  - If the file is compressed with gzip (.vcf.gz but not bgzip) decompress it first:

     .. code-block:: bash

        gunzip Sample.vcf.gz

   And then, compress it with bgzip

      .. code-block:: bash

          bgzip -c Sample.vcf > Sample.vcf.gz

   Index the bgzip-compressed file for faster access

      .. code-block:: bash

          tabix -p vcf Sample.vcf.gz

Now, your file is ready to be uploaded or used in CLI. 
