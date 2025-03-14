<script>
    import { Heading, P, A, List, Li, Button } from 'flowbite-svelte';
</script>
<Heading tag="h2" class="mt-5 mb-2">About</Heading>


<Heading tag="h4" class="mt-10 mb-2">Variant-aware Cas-OFFinder</Heading>
<List tag="ol" class="space-y-1 text-gray-600 dark:text-gray-400" list="none">
    <Li>In the CRISPR-Cas systems, the guide RNA molecule has the potential to cause 
      the Cas complex to target unintended genomic locations, which are referred to as potential off-target sites. 
      This can lead to incorrect cleavage events. The effectiveness of the CRISPR-Cas system's targeting is directly 
      influenced by the specific sequence composition of the guide RNA (gRNA) and the presence of PAM in the target DNA sequence.
      Considering the presence of numerous DNA sequences in the genome that closely resemble the target location, 
      the risk of unintended DNA modifications is significantly heightened. Before initiating any genome editing experiment, 
      it is crucial to predict and assess potential off-target sites. 
    </Li>
    <Li> When predicting potential off-target sites in silico, guide RNA (gRNA) sequences are aligned to a reference genome 
        to identify sites with sequence similarity. However, reference genomes are typically derived from a limited number of 
        individuals and may not fully represent genetic diversity. We present an enhanced version of Cas-OFFinder, 
        a computational tool that extends beyond reference genome-based predictions by incorporating individual genetic 
        variants while maintaining support for unlimited mismatches and flexible PAM sequences, similar to the original 
        Cas-OFFinder.
    </Li>
</List>
<Heading tag="h4" class="mt-10 mb-2">Variant-aware Cas-OFFinder Webtool</Heading>
<List tag="ol" class="space-y-1 text-gray-600 dark:text-gray-400" list="none">
    <Li>The Variant-aware Cas-OFFinder web tool is designed to assist scientisists and researchers to identify potential off-target sites 
        across individual's entire genome.This website has been renovated, transitioning from the old interface to a new one to 
        significantly enhance user experience. 
    </Li>
</List>


<h4 class="mt-10 mb-2" style="font-size: 24px; font-weight: bold; color: #333;">
    📖 User Guide 
    <Button class="ml-2 !py-2 !pl-3 !pr-4" href="https://rgen-toolkit.readthedocs.io/" 
        target="_blank">
        🔗 View Detailed User Guide
    </Button>
</h4>
<List tag="ol" list="decimal" class="text-gray-600 dark:text-gray-400">
    <Li>  
        Upload VCF file
        <List tag="ol" class="ps-5 mt-2 space-y-1">
            <Li>Navigate to the "Upload VCF file" section and upload the example VCF file. </Li>
            <Li>Supported file formats: [e.g., .vcf, .vcf.gz (gzipped and bgzipped file)]. </Li>
        </List>  
    </Li>
    <Li>
        Select and Enter all required parameters 
        <List tag="ol" class="ps-5 mt-2 space-y-1">
          <Li> Define the parameters (PAM Type, Target Genome, Query Sequence, and mismatches) required for your task.</Li>
          <Li>Use the default values for a quick start or adjust them for a custom analysis.</Li>
          <Li> Click "Submit" to proceed.</Li>
        </List>
    </Li>
    <Li>
        View Results
        <List tag="ol" class="ps-5 mt-2 space-y-1">
          <Li>Once the analysis is complete, the results will be ready.</Li>
          <Li>Explore the output through tabular data for detailed insights or download the results.</Li>
          <Li>You can use the search button to filter based on mismatches.</Li>
        </List>
      </Li>
</List>

<Heading tag="h4" class="mt-10 mb-2">Quick Start</Heading>
<List tag="ol" class="space-y-1 text-gray-600 dark:text-gray-400" list="none">
    <Li>To begin using the web tool efficiently, follow these straightforward steps to ensure a smooth start:</Li>
</List>
<List tag="ol" class="ps-5 mt-2 space-y-1">
    <Li> Download the Required File: <Button class="ml-2 !py-2 !pl-3 !pr-4" href="https://github.com/pnucolab/VarCas-OFFinder/raw/refs/heads/main/docs_old/Sample.vcf.gz" download>
        📥 Click here</Button></Li>
    <Li>Upload the File.</Li>
    <Li>Submit for Processing.</Li>
    <Li>View Results.</Li>
    <Li> Click here for details:
        
        <Button class="ml-2 !py-2 !pl-3 !pr-3" href="https://rgen-toolkit.readthedocs.io/en/latest/quickstart.html" 
            target="_blank">
            🌐   
    </Button>
    </Li>
</List>


    
   