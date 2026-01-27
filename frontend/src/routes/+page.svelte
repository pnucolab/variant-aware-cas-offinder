<script>
    import { Button, Heading, P, Accordion, AccordionItem } from 'flowbite-svelte';
    import { ArrowRightOutline } from 'flowbite-svelte-icons';

    import { onMount } from 'svelte';
    let visible = false;
    
    onMount(() => {
        setTimeout(() => {
            visible = true;
        }, 100);
    });
</script>

<svelte:head>
    <title>RGE Toolkit - RNA-Guided Genome Editing Tools</title>
    <meta name="description" content="Comprehensive suite of tools for CRISPR and RNA-guided genome editing research" />
</svelte:head>

<!-- Hero Section -->
<section class="full-width-section bg-gradient-to-br from-blue-50 via-white to-purple-50 dark:from-gray-900 dark:via-gray-800 dark:to-gray-900 py-20 transition-opacity duration-1000 {visible ? 'opacity-100' : 'opacity-0'}">
    <div class="max-w-5xl mx-auto px-6 text-center">
        <Heading tag="h1" class="mb-6 text-5xl md:text-6xl font-bold bg-gradient-to-r from-blue-600 to-purple-600 bg-clip-text text-transparent">
            RGE Toolkit
        </Heading>
        <P class="text-xl md:text-2xl text-gray-600 dark:text-gray-300 mb-8 font-light">
            A comprehensive platform providing computational tools for RNA-guided genome editing research
        </P>
    </div>
</section>

<!-- Tools Section -->
<section id="tools" class="full-width-section py-20 transition-opacity duration-1000 {visible ? 'opacity-100' : 'opacity-0'}">
    <div class="max-w-5xl mx-auto px-6">
        <div class="text-center mb-12">
            <Heading tag="h2" class="mb-4 text-4xl font-bold">Available Tools</Heading>
            <P class="text-lg text-gray-600 dark:text-gray-400">
                Computational tools for genome editing applications
            </P>
        </div>
        
        <div class="space-y-6">
            <!-- Variant-aware Cas-OFFinder -->
            <div class="p-6 rounded-lg shadow-lg border border-blue-500 hover:shadow-xl hover:-translate-y-1 transition-all duration-300">
                <Heading tag="h3" class="mb-3 text-xl">Variant-aware Cas-OFFinder</Heading>
                <P class="text-gray-600 dark:text-gray-400 mb-4">
                    Web-based tool for identifying potential off-target sites by accounting for individual genetic variants. 
                    Enables haplotype-aware analysis from VCF files for personalized genome editing applications.
                </P>
                <Button href="/var-cas-offinder" color="blue" size="sm">
                    Open Tool
                    <ArrowRightOutline class="w-4 h-4 ml-1" />
                </Button>
            </div>

            <!-- Coming Soon Tools -->
            <div class="p-6 rounded-lg shadow-lg border border-blue-500 hover:shadow-xl hover:-translate-y-1 transition-all duration-300">
                <div class="mb-3">
                    <span class="text-xl font-bold text-gray-900 dark:text-white">More Tools</span>
                    <span class="ml-2 px-2 py-1 text-orange-700 dark:text-orange-300 rounded text-xs font-semibold">Coming Soon</span>
                </div>
                <P class="text-gray-600 dark:text-gray-400">
                    Additional computational tools for genome editing research are under active development.
                </P>
            </div>
        </div>
    </div>
</section>

<!-- Use Cases Section -->
<section class="full-width-section py-16">
    <div class="max-w-5xl mx-auto px-6">
        <div class="text-center mb-12">
            <Heading tag="h2" class="mb-4 text-4xl font-bold">Use Cases</Heading>
            <P class="text-lg text-gray-600 dark:text-gray-400">
                Supporting diverse genome editing research needs
            </P>
        </div>

        <div class="grid md:grid-cols-3 gap-6">
            <div class="p-6 rounded-lg shadow-lg">
                <Heading tag="h3" class="mb-3 text-xl">Basic Research</Heading>
                <P class="text-gray-600 dark:text-gray-400">
                    Optimize guide design, and investigate editing specificity
                </P>
            </div>

            <div class="p-6 rounded-lg shadow-lg">
                <Heading tag="h3" class="mb-3 text-xl">Clinical Applications</Heading>
                <P class="text-gray-600 dark:text-gray-400">
                    Support gene therapy and personalized medicine applications
                </P>
            </div>

            <div class="p-6 rounded-lg shadow-lg">
                <Heading tag="h3" class="mb-3 text-xl">Agricultural Biotechnology</Heading>
                <P class="text-gray-600 dark:text-gray-400">
                    Support precise crop improvement and livestock genetic modification
                </P>
            </div>
        </div>
    </div>
</section>

<!-- FAQ Section -->
<section class="full-width-section py-16">
    <div class="max-w-5xl mx-auto px-6">
        <div class="text-center mb-12">
            <Heading tag="h2" class="mb-4 text-4xl font-bold">Frequently Asked Questions</Heading>
        </div>

        <Accordion>
            <AccordionItem>
                <span slot="header">What is RGE Toolkit?</span>
                <P class="text-gray-600 dark:text-gray-400">
                    RGE Toolkit is a platform hosting computational tools for RNA-guided genome editing research. 
                    It provides web-based applications to support genome editing research, guide RNA design, and off-target analysis.
                </P>
            </AccordionItem>

            <AccordionItem>
                <span slot="header">Which tools are currently available?</span>
                <P class="text-gray-600 dark:text-gray-400">
                    Currently, Variant-aware Cas-OFFinder is available for identifying potential off-target sites with genetic variant support. 
                    Additional tools are under development and will be added to the platform.
                </P>
            </AccordionItem>

            <AccordionItem>
                <span slot="header">Is RGE Toolkit free to use?</span>
                <P class="text-gray-600 dark:text-gray-400">
                    Yes! All tools in RGE Toolkit are free and open source under the GNU AGPL license. 
                    You can use the web interface or deploy locally without any costs.
                </P>
            </AccordionItem>

            <AccordionItem>
                <span slot="header">Can I run these tools on my own server?</span>
                <P class="text-gray-600 dark:text-gray-400">
                    Yes. All tools are available as Docker containers and can be deployed on your own infrastructure. 
                    Command-line interfaces are also provided for local execution.
                </P>
            </AccordionItem>

            <AccordionItem>
                <span slot="header">How can I contribute or request features?</span>
                <P class="text-gray-600 dark:text-gray-400">
                    Visit our GitHub repositories to report issues, suggest features, or contribute code.
                </P>
            </AccordionItem>
        </Accordion>
    </div>
</section>

<section class="full-width-section py-20 text-center">
    <div class="max-w-5xl mx-auto px-6">
        <Heading tag="h2" class="mb-6 text-4xl font-bold">Get Started</Heading>
        <P class="text-xl mb-8 opacity-90">
            Explore our tools to for your genome editing research
        </P>
        <Button size="xl" color="blue" href="#tools" class="gap-2">
            View Tools
            <ArrowRightOutline class="w-5 h-5" />
        </Button>
    </div>
</section>

<style>
    :global(.bg-clip-text) {
        -webkit-background-clip: text;
        background-clip: text;
    }
    

    .full-width-section {
        width: 100vw;
        position: relative;
        left: 50%;
        right: 50%;
        margin-left: -50vw;
        margin-right: -50vw;
    }
</style>