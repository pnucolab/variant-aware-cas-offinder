<script>
    import { Heading, P, A } from 'flowbite-svelte';
</script>

<Heading tag="h2" class="mt-5 mb-2">Variant-aware <wbr>Cas-OFFinder</Heading>
<Heading tag="h5" class="font-light mb-5">A webtool for searching potential off-target sites accounting for genomic variants</Heading>
<P class="mb-5">
    Variant-aware Cas-OFFinder is a web-based tool for identifying potential CRISPR off-target sites across different genomes.
    It accounts for both reference genomes and individual genetic variants to improve accuracy in diverse populations.
    This addresses limitations caused by incomplete representation of genetic variation in reference genomes. 
    Variant-aware Cas-OFFinder is freely available under GNU AGPL.
</P>
<div class="citation-box">
    <span class="citation-label">Citation</span>
    <p class="citation-text">
      Mekonnen, A. M., Seong, K., Kim, H., & Park, J. (2025). Variant-aware Cas-OFFinder: web-based in silico variant-aware potential off-target site identification for genome editing applications. <em>Nucleic Acids Research</em>, gkaf389.
    </p>
    <A href="https://doi.org/10.1093/nar/gkaf389" target="_blank" class="citation-link">
      View Publication
    </A>
</div>

<style>
    .citation-box {
        background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%);
        border-left: 4px solid #2563eb;
        border-radius: 0 8px 8px 0;
        padding: 16px 20px;
        margin-top: 20px;
        position: relative;
    }
    .citation-label {
        position: absolute;
        top: -10px;
        left: 12px;
        background: #2563eb;
        color: white;
        font-size: 0.75rem;
        font-weight: 600;
        padding: 2px 10px;
        border-radius: 4px;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    .citation-text {
        margin: 8px 0 12px 0;
        font-size: 0.95rem;
        line-height: 1.6;
        color: #374151;
    }
    .citation-box :global(.citation-link) {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        background: #2563eb;
        color: white !important;
        padding: 6px 14px;
        border-radius: 6px;
        font-size: 0.85rem;
        font-weight: 500;
        text-decoration: none;
        transition: background-color 0.2s;
    }
    .citation-box :global(.citation-link:hover) {
        background: #1d4ed8;
    }
</style>
  
  
  