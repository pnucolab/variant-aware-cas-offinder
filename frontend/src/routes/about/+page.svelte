<script>
    import { Heading, P, List, Li, Button } from 'flowbite-svelte';
    import { ArrowUpRightFromSquareOutline, DownloadOutline, BookOpenOutline } from 'flowbite-svelte-icons';

    const steps = [
        {
            title: 'Upload a VCF File',
            details: [
                'Navigate to the "Upload VCF file" section and upload your file. Use the sample VCF above to get started quickly.',
                'Supported formats: .vcf, .vcf.gz (gzipped and bgzipped).',
            ]
        },
        {
            title: 'Configure Analysis Parameters',
            details: [
                'Set the required parameters: PAM Type, Target Genome, Query Sequence, and Mismatch count.',
                'Use default values for a quick start, or adjust them for a custom analysis.',
                'Click Submit to start the analysis.',
            ]
        },
        {
            title: 'Explore Your Results',
            details: [
                'Once the analysis completes, results are displayed in an interactive table.',
                'Filter by gRNA, mismatch count, or GC content. Download results for offline use.',
                'Use the summary table to view off-target counts per chromosome across all gRNAs.',
            ]
        },
    ];


</script>
<Heading tag="h2" class="mt-5 mb-2">About</Heading>


<Heading tag="h4" class="mt-10 mb-2">Variant-aware Cas-OFFinder</Heading>
<P class="mb-3 text-gray-600 dark:text-gray-400">
    In the CRISPR-Cas systems, the guide RNA molecule has the potential to cause the Cas complex to target unintended genomic
    locations, which are referred to as potential off-target sites. This can lead to incorrect cleavage events. The effectiveness
    of the CRISPR-Cas system's targeting is directly influenced by the specific sequence composition of the guide RNA (gRNA) and
    the presence of PAM in the target DNA sequence. Considering the presence of numerous DNA sequences in the genome that closely
    resemble the target location, the risk of unintended DNA modifications is significantly heightened. Before initiating any
    genome editing experiment, it is crucial to predict and assess potential off-target sites.
</P>
<P class="text-gray-600 dark:text-gray-400">
    When predicting potential off-target sites in silico, guide RNA (gRNA) sequences are aligned to a reference genome to identify
    sites with sequence similarity. However, reference genomes are typically derived from a limited number of individuals and may
    not fully represent genetic diversity. We present an enhanced version of Cas-OFFinder, a computational tool that extends beyond
    reference genome-based predictions by incorporating individual genetic variants while maintaining support for unlimited
    mismatches and flexible PAM sequences, similar to the original Cas-OFFinder.
</P>

<Heading tag="h4" class="mt-10 mb-2">Variant-aware Cas-OFFinder Webtool</Heading>
<P class="text-gray-600 dark:text-gray-400">
    The Variant-aware Cas-OFFinder web tool is designed to assist scientists and researchers in identifying potential off-target
    sites across an individual's entire genome. The web tool is developed using SvelteKit for the front-end and FastAPI for the
    back-end, ensuring a responsive user interface and efficient processing of off-target search queries. PAM types and target
    genomes are managed through user-editable YAML configuration files, enabling modular customization across different species
    and nuclease systems. The entire application is packaged using Docker Compose for easy deployment and reproducibility.
</P>


<div class="mt-10 mb-2">
    <Heading tag="h4" class="inline">Update History</Heading>
    <span class="ml-2 px-2 py-1 text-orange-700 dark:text-orange-300 rounded text-xs font-semibold">What's New</span>
</div>

<P class="mt-2 text-gray-600 dark:text-gray-400">
    The latest release is <span class="font-medium text-gray-800 dark:text-gray-200">v1.0.1</span>, featuring performance improvements,
    UI enhancements, and new features. See the official documentation for the full version history.
</P>
<div class="mt-3">
    <Button color="alternative" href="https://rgen-toolkit.readthedocs.io/en/latest/version_history.html" target="_blank" class="gap-2 border-2 border-orange-400 dark:border-orange-500 text-orange-700 dark:text-orange-300 hover:bg-orange-50 dark:hover:bg-orange-900/20">
        View Version History <ArrowUpRightFromSquareOutline class="w-4 h-4" />
    </Button>
</div>


<div class="mt-10 mb-4 flex flex-wrap items-center justify-between gap-3">
    <Heading tag="h4">How to Use</Heading>
    <div class="flex flex-wrap gap-2">
        <Button size="sm" color="light" href="https://rgen-toolkit.readthedocs.io/" target="_blank" class="gap-2">
            <BookOpenOutline class="w-4 h-4" /> View Full Documentation
        </Button>
        <Button size="sm" color="light" href="https://github.com/pnucolab/variant-aware-cas-offinder/raw/refs/heads/main/docs/Sample.vcf.gz" download class="gap-2">
            <DownloadOutline class="w-4 h-4" /> Download Sample VCF
        </Button>
    </div>
</div>

<div class="space-y-3">
    {#each steps as step, i}
        <div class="flex gap-4 rounded-lg border border-gray-200 dark:border-gray-700 bg-white dark:bg-gray-800 p-5 hover:shadow-md transition-shadow duration-200">
            <div class="flex-shrink-0 w-8 h-8 rounded-full bg-blue-600 flex items-center justify-center text-white font-bold text-sm">{i + 1}</div>
            <div class="flex-1">
                <p class="font-semibold text-gray-800 dark:text-gray-200 mb-1">{step.title}</p>
                <List tag="ol" class="ps-4 space-y-1 text-gray-600 dark:text-gray-400" list="none">
                    {#each step.details as detail}
                        <Li class="text-sm">{detail}</Li>
                    {/each}
                </List>
            </div>
        </div>
    {/each}
</div>
