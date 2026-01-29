<script>
	import { Spinner} from 'flowbite-svelte';
	import { load } from './fetch';
	import Top from '../lib/Top.svelte';
	import { Heading } from 'flowbite-svelte';
	import { onMount, onDestroy} from 'svelte';
	import download from 'downloadjs';
	import { Alert } from 'flowbite-svelte';

	import { Table, TableBodyCell, TableBodyRow, TableHead, TableHeadCell } from 'flowbite-svelte';
    import Bottom from './Bottom.svelte';

	export let ticket;

	let result = {};
	let loaded = false;
	let errorMessage = '';
	let results = {};

	// Timeout IDs for cleanup
	let resultTimeoutId = null;
	let resultsTimeoutId = null;

   async function get_result(ticket){
	const data = await load('result?ticket=' + ticket);
	result = data;
	const{status, uploaded_file, created_at, finished_at} = result;
	if (result.status === 1) {
        resultTimeoutId = setTimeout(() => get_result(ticket), 3000);
	} else {
		resultTimeoutId = null;
		// Job finished - fetch results, summary, and filter options
		await get_results(ticket, 1);
		await get_summary(ticket);
		await get_filter_options(ticket);
    }
}

   async function get_filter_options(ticket) {
       try {
           const response = await load(`result_filter_options?ticket=${ticket}`);
           if (response.status === 'completed') {
               if (response.crrna_values) {
                   availableCrRNAValues = response.crrna_values;
               }
               if (response.chromosome_values) {
                   availableChromosomeValues = response.chromosome_values;
               }
               if (response.mismatches) {
                   availableMismatches = response.mismatches.map(String).sort((a, b) => Number(a) - Number(b));
               }
               if (response.gc_values) {
                   availableGCValues = response.gc_values.map(String).sort((a, b) => Number(a) - Number(b));
               }
           }
       } catch (e) {
           console.log('Filter options endpoint not available');
       }
   }

  onMount(async () => {
		await get_result(ticket);
		loaded = true;

	});

	onDestroy(() => {
		// Clear any pending timeouts when component is destroyed
		if (resultTimeoutId) {
			clearTimeout(resultTimeoutId);
			resultTimeoutId = null;
		}
		if (resultsTimeoutId) {
			clearTimeout(resultsTimeoutId);
			resultsTimeoutId = null;
		}
	});

   let classifiedData = [];
   let isLoadingPage = false;
   let totalCount = 0;
   let tpages = 0;
   let cpage = 1;
   let ippage = 20;
   const rowsPerPageOptions = [10, 20, 30, 50];

   // Filter state variables
   let filterCrRNA = 'All';
   let filterChromosome = 'All';
   let filterMismatches = 'All';
   let filterGC = 'All';

   // Available filter options (populated from data)
   let availableCrRNAValues = [];
   let availableChromosomeValues = [];
   let availableMismatches = [];
   let availableGCValues = [];

   // Reactive dropdown options with 'All' prepended
   $: crrnaOptions = ['All', ...availableCrRNAValues];
   $: chromosomeOptions = ['All', ...availableChromosomeValues];
   $: mismatchOptions = ['All', ...availableMismatches];
   $: gcOptions = ['All', ...availableGCValues];

   // Summary data
   let summaryData = [];
   let isLoadingSummary = false;
   let allele1Label = '1';
   let allele2Label = '2';

   // Group summary data by crRNA for rowspan
   $: groupedSummary = (() => {
       const result = [];
       let currentCrRNA = null;
       let rowspanCount = 0;
       let startIndex = -1;

       // First pass: count occurrences of each crRNA
       const crrnaCounts = {};
       summaryData.forEach(item => {
           crrnaCounts[item.crRNA] = (crrnaCounts[item.crRNA] || 0) + 1;
       });

       // Second pass: mark first occurrence with rowspan
       const seenCrRNA = {};
       summaryData.forEach((item, index) => {
           const isFirstOfGroup = !seenCrRNA[item.crRNA];
           seenCrRNA[item.crRNA] = true;
           result.push({
               ...item,
               isFirstOfGroup,
               rowspan: isFirstOfGroup ? crrnaCounts[item.crRNA] : 0
           });
       });

       return result;
   })();

   async function get_summary(ticket) {
       isLoadingSummary = true;
       const response = await load(`result_summary?ticket=${ticket}`);
       if (response.status === 'completed' && response.summary) {
           summaryData = response.summary;
           // Get allele labels from first item if available
           if (response.summary.length > 0) {
               allele1Label = response.summary[0].allele_1_label || '1';
               allele2Label = response.summary[0].allele_2_label || '2';
           }
       }
       isLoadingSummary = false;
   }

   async function changeRowsPerPage(event) {
       ippage = parseInt(event.target.value);
       cpage = 1;
       await get_results(ticket, 1);
   }

   async function applyFilters() {
       cpage = 1;
       await get_results(ticket, 1);
   }

   async function clearFilters() {
       filterCrRNA = 'All';
       filterChromosome = 'All';
       filterMismatches = 'All';
       filterGC = 'All';
       cpage = 1;
       await get_results(ticket, 1);
   }

   async function get_results(ticket, page = 1){
	isLoadingPage = true;
	let url = `result_detail?ticket=${ticket}&page=${page}&limit=${ippage}`;

	// Add filter parameters to URL
	if (filterCrRNA && filterCrRNA !== 'All') {
		url += `&crRNA=${encodeURIComponent(filterCrRNA)}`;
	}
	if (filterChromosome && filterChromosome !== 'All') {
		url += `&chromosome=${encodeURIComponent(filterChromosome)}`;
	}
	if (filterMismatches && filterMismatches !== 'All') {
		url += `&mismatches=${filterMismatches}`;
	}
	if (filterGC && filterGC !== 'All') {
		url += `&gc=${filterGC}`;
	}

	const datagr = await load(url);
	results = datagr;
	const{output, status, data, pagination} = results;

	if (output === 'Please wait until the result is ready.') {
        resultsTimeoutId = setTimeout(() => get_results(ticket, page), 3000);
		isLoadingPage = false;
	} else {
		resultsTimeoutId = null;

		// Check if task completed with no results
		if (output === 'COMPLETED_NO_RESULTS') {
			classifiedData = [];
			totalCount = 0;
			tpages = 0;
			isLoadingPage = false;
			return;
		}

		// Handle new paginated response format
		if (status === 'completed' && data) {
			classifiedData = data.map(item => ({
				crRNA: item.crRNA || item[0],
				chromosome: item.Chromosome || item[1],
				allele: item.Allele || item[2],
				position: item.Position || item[3],
				DNA: item.DNA || item[4],
				direction: item.Direction || item[5],
				mismatches: String(item.Mismatches || item[6]),
				GC: String(item.GC || item[7])
			}));
			totalCount = pagination.total_count;
			tpages = pagination.total_pages;
			cpage = pagination.page;
		}
		isLoadingPage = false;
	}
}

	async function downloadresultFile(){
		// Fetch all data for download
		let allData = [];
		let page = 1;
		let hasMore = true;

		while (hasMore) {
			const response = await load(`result_detail?ticket=${ticket}&page=${page}&limit=500`);
			if (response.status === 'completed' && response.data) {
				allData = allData.concat(response.data);
				hasMore = page < response.pagination.total_pages;
				page++;
			} else {
				hasMore = false;
			}
		}

		let header = `crRNA\tChromosome\tAllele\tPosition\tDNA\tDirection\tMismatches\tGC-content\n`;
		let rows = allData.map(item => {
            return `${item.crRNA || item[0]}\t${item.Chromosome || item[1]}\t${item.Allele || item[2]}\t${item.Position || item[3]}\t${item.DNA || item[4]}\t${item.Direction || item[5]}\t${item.Mismatches || item[6]}\t${item.GC || item[7]}`;
        }).join('\n');
        let textData = header + rows;
        download(textData, 'result.txt', 'text/plain');
    }


// For server-side pagination, use classifiedData directly (already paginated from server)
$: paginatedData = classifiedData;

async function changepages(newpages){
	if (newpages > 0 && newpages <= tpages && newpages !== cpage){
		await get_results(ticket, newpages);
	}
}

</script>

<Top />

{#if loaded}
		
	<Table>
		<TableHead>
			<TableBodyCell>Job ID</TableBodyCell>
			<TableBodyCell>Submit Date</TableBodyCell>
			<TableBodyCell>End Date</TableBodyCell>
			<TableBodyCell>Status</TableBodyCell>
		</TableHead>
        <TableBodyRow> 
			<TableBodyCell>{ticket}</TableBodyCell>
			<TableBodyCell>{#if result.status == 0} {result.created_at} {:else} - {/if}</TableBodyCell>
			<TableBodyCell>{#if result.status == 0} {result.finished_at} {:else} - {/if}</TableBodyCell>
			<TableBodyCell>{#if result.status == 0} Finished {:else} Loading <Spinner size = {4} /> {/if}</TableBodyCell>
		</TableBodyRow>
		
	</Table>

	<Alert style="padding: 1em; border-radius: 4px; background-color: transparent;">
		<span class="font-medium">Notice!</span> 
		<div style="background-color: #fff3cd; color: #856404; padding: 0.5em; border-radius: 4px;">
			Empty result file after "Finished" status means no matched sequence based on given inputs.
		</div>
	</Alert>
	
	<Alert style="background-color: transparent;">
		<span class="font-medium"></span> 
		<div class="font-bold text-base" style="color: #721c24; padding: 0.7em; border-radius: 4px;">
			{#if result.status == 0}  {result.uploaded_file} {/if}
		</div>
	</Alert>
	<Heading class="mb-5" tag="h4"></Heading>
	
	

<style>
	.table {
	  width: 100%;
	  border-collapse: collapse;
	}
	.table th, .table td {
	  padding: 12px;
	  border: 1px solid #ddd;
	  text-align: center;
	}
	.table th {
	  background-color: #f2f2f2;
	}
  </style>

{#if result.status == 0 && result.uploaded_file == ''}

{#if summaryData.length > 0}
<Heading class="mt-2 mb-5" tag="h4">Summary</Heading>
<div class="summary-table-container">
	{#if isLoadingSummary}
	<div class="loading-overlay">
		<Spinner size={8} />
	</div>
	{/if}
	<table class="summary-table">
		<thead>
			<tr>
				<th>crRNA Sequence</th>
				<th>Length</th>
				<th>Chromosome</th>
				<th>Allele {allele1Label}</th>
				<th>Allele {allele2Label}</th>
			</tr>
		</thead>
		<tbody>
		{#each groupedSummary as item}
		<tr>
			{#if item.isFirstOfGroup}
			<td rowspan={item.rowspan} class="merged-cell">{item.crRNA}</td>
			<td rowspan={item.rowspan} class="merged-cell">{item.length}</td>
			{/if}
			<td>{item.chromosome}</td>
			<td>{item.allele_1_count}</td>
			<td>{item.allele_2_count}</td>
		</tr>
		{/each}
		</tbody>
	</table>
</div>
{/if}

<div class="result-details-header">
	<Heading class="mt-2 mb-5" tag="h4">Result Details {#if totalCount > 0}<span class="total-count">({totalCount} total results)</span>{/if}</Heading>
	<button class='downloadButton' on:click={downloadresultFile}>Download Result</button>
</div>

{#if totalCount > 0}
<div class="rows-per-page-top">
	<label for="rowsPerPageTop">Rows per page:</label>
	<select id="rowsPerPageTop" bind:value={ippage} on:change={changeRowsPerPage} disabled={isLoadingPage}>
		{#each rowsPerPageOptions as option}
			<option value={option}>{option}</option>
		{/each}
	</select>
</div>
{/if}

{#if classifiedData.length === 0 && !isLoadingPage}
 <div class="empty-results">
	<p>No off-target sites found for the given query sequences.</p>
 </div>
{:else}
 <div class="table-container" class:loading={isLoadingPage}>
	{#if isLoadingPage}
	<div class="loading-overlay">
		<Spinner size={8} />
	</div>
	{/if}
 <Table class="table" striped = {true} hoverable={true}>
	<TableHead defaultRow={false} class="text-xl text-gray-1000 uppercase bg-gray-100 dark:bg-gray-700 dark:text-gray-400" >
	<TableHeadCell>
		<div class="header-with-filter">
			<span>crRNA</span>
			<select class="header-filter-select" bind:value={filterCrRNA} disabled={isLoadingPage || crrnaOptions.length <= 1} on:change={applyFilters}>
				{#each crrnaOptions as option}
					<option value={option}>{option}</option>
				{/each}
			</select>
		</div>
	</TableHeadCell>
	<TableHeadCell>
		<div class="header-with-filter">
			<span>Chromosome</span>
			<select class="header-filter-select" bind:value={filterChromosome} disabled={isLoadingPage || chromosomeOptions.length <= 1} on:change={applyFilters}>
				{#each chromosomeOptions as option}
					<option value={option}>{option}</option>
				{/each}
			</select>
		</div>
	</TableHeadCell>
	<TableHeadCell>Allele</TableHeadCell>
	<TableHeadCell>Position</TableHeadCell>
	<TableHeadCell>DNA</TableHeadCell>
	<TableHeadCell>Direction</TableHeadCell>
	<TableHeadCell>
		<div class="header-with-filter">
			<span>Mismatches</span>
			<select class="header-filter-select" bind:value={filterMismatches} disabled={isLoadingPage || mismatchOptions.length <= 1} on:change={applyFilters}>
				{#each mismatchOptions as option}
					<option value={option}>{option}</option>
				{/each}
			</select>
		</div>
	</TableHeadCell>
	<TableHeadCell>
		<div class="header-with-filter">
			<span>GC-content(%)</span>
			<select class="header-filter-select" bind:value={filterGC} disabled={isLoadingPage || gcOptions.length <= 1} on:change={applyFilters}>
				{#each gcOptions as option}
					<option value={option}>{option === 'All' ? 'All' : option + '%'}</option>
				{/each}
			</select>
		</div>
	</TableHeadCell>
</TableHead>
	{#each paginatedData as item}
	<TableBodyRow>
		<TableBodyCell>{item.crRNA}</TableBodyCell>
	  <TableBodyCell>{item.chromosome}</TableBodyCell>
	  <TableBodyCell>{item.allele}</TableBodyCell>
	  <TableBodyCell>{item.position}</TableBodyCell>
	  <TableBodyCell>{item.DNA}</TableBodyCell>
	  <TableBodyCell>{item.direction}</TableBodyCell>
	  <TableBodyCell>{item.mismatches}</TableBodyCell>
	  <TableBodyCell>{item.GC}</TableBodyCell>
	</TableBodyRow>
	{/each}
</Table>
 </div>
<div class="pagination">
	<button on:click={() => changepages(1)} disabled={cpage === 1 || isLoadingPage}>
		First
	  </button>
	<button on:click={() => changepages(cpage - 1)} disabled={cpage === 1 || isLoadingPage}>
	  Previous
	</button>
	<span>{cpage} of {tpages}</span>
	<button on:click={() => changepages(cpage + 1)} disabled={cpage === tpages || isLoadingPage}>
	  Next
	</button>
	<button on:click={() => changepages(tpages)} disabled={cpage === tpages || isLoadingPage}>
		Last
	  </button>
  </div>
{/if}

  
  <style>
	.pagination {
	  display: flex;
	  justify-content: center;
	  align-items: center;
	  margin: 20px 0;
	}
	.pagination button {
	  margin: 0 5px;
	  padding: 5px 10px;
	  cursor: pointer;
	  border: 1px solid #ccc;
	  border-radius: 5px;
	}
	.pagination button:disabled {
	  cursor: not-allowed;
	  opacity: 0.5;
	}
	.pagination button.active {
	  font-weight: bold;
	  text-decoration: underline;
	}
	.empty-results {
	  text-align: center;
	  padding: 40px 20px;
	  background-color: #f8f9fa;
	  border: 1px solid #e9ecef;
	  border-radius: 8px;
	  margin: 20px 0;
	}
	.empty-results p {
	  color: #6c757d;
	  font-size: 1.1rem;
	  margin: 0;
	}
	.table-container {
	  position: relative;
	  min-height: 200px;
	}
	.table-container.loading {
	  opacity: 0.6;
	  pointer-events: none;
	}
	.loading-overlay {
	  position: absolute;
	  top: 50%;
	  left: 50%;
	  transform: translate(-50%, -50%);
	  z-index: 10;
	}
	.total-count {
	  font-size: 0.9rem;
	  color: #6c757d;
	  font-weight: normal;
	}
	.result-details-header {
	  display: flex;
	  align-items: center;
	  justify-content: space-between;
	  gap: 20px;
	}
	.downloadButton {
	  background-color: #2563eb;
	  color: white;
	  border: none;
	  padding: 8px 16px;
	  border-radius: 4px;
	  cursor: pointer;
	  font-size: 0.9rem;
	  white-space: nowrap;
	}
	.downloadButton:hover {
	  background-color: #1d4ed8;
	}
	.rows-per-page {
	  margin-left: 20px;
	  display: flex;
	  align-items: center;
	  gap: 5px;
	}
	.rows-per-page label {
	  font-size: 0.9rem;
	  color: #666;
	}
	.rows-per-page select {
	  padding: 4px 8px;
	  border: 1px solid #ccc;
	  border-radius: 4px;
	  cursor: pointer;
	}
	.rows-per-page select:disabled {
	  cursor: not-allowed;
	  opacity: 0.5;
	}
	.rows-per-page-top {
	  display: flex;
	  align-items: center;
	  justify-content: flex-end;
	  gap: 8px;
	  margin-bottom: 15px;
	}
	.rows-per-page-top label {
	  font-size: 0.9rem;
	  color: #666;
	}
	.rows-per-page-top select {
	  padding: 4px 24px 4px 8px;
	  border: 1px solid #ccc;
	  border-radius: 4px;
	  cursor: pointer;
	  appearance: none;
	  -webkit-appearance: none;
	  -moz-appearance: none;
	  background: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='12' viewBox='0 0 12 12'%3E%3Cpath fill='%23666' d='M6 8L1 3h10z'/%3E%3C/svg%3E") no-repeat right 6px center;
	  background-color: white;
	}
	.rows-per-page-top select:disabled {
	  cursor: not-allowed;
	  opacity: 0.5;
	}
	.summary-table-container {
	  position: relative;
	  margin-bottom: 30px;
	  max-height: 400px;
	  overflow-y: auto;
	  border: 1px solid #ddd;
	  border-radius: 4px;
	}
	.summary-table {
	  width: 100%;
	  border-collapse: collapse;
	}
	.summary-table th, .summary-table td {
	  padding: 12px;
	  border: 1px solid #ddd;
	  text-align: center;
	}
	.summary-table thead {
	  position: sticky;
	  top: 0;
	  z-index: 1;
	}
	.summary-table th {
	  background-color: #f3f4f6;
	  text-transform: uppercase;
	  font-weight: 600;
	  color: #374151;
	}
	.summary-table tbody tr:nth-child(even) {
	  background-color: #f9fafb;
	}
	.summary-table tbody tr:hover {
	  background-color: #f3f4f6;
	}
	.summary-table .merged-cell {
	  vertical-align: middle;
	  font-weight: 500;
	  background-color: #f8fafc;
	}
	.header-with-filter {
	  display: flex;
	  flex-direction: column;
	  gap: 6px;
	  min-width: 100px;
	}
	.header-with-filter span {
	  font-weight: 600;
	}
	.header-filter-select {
	  padding: 4px 20px 4px 6px;
	  border: 1px solid #ced4da;
	  border-radius: 4px;
	  font-size: 0.75rem;
	  font-weight: normal;
	  text-transform: none;
	  cursor: pointer;
	  appearance: none;
	  -webkit-appearance: none;
	  -moz-appearance: none;
	  background: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='10' height='10' viewBox='0 0 12 12'%3E%3Cpath fill='%23666' d='M6 8L1 3h10z'/%3E%3C/svg%3E") no-repeat right 5px center;
	  background-color: white;
	  width: 100%;
	  box-sizing: border-box;
	}
	.header-filter-select:focus {
	  outline: none;
	  border-color: #2563eb;
	  box-shadow: 0 0 0 2px rgba(37, 99, 235, 0.1);
	}
	.header-filter-select:disabled {
	  background-color: #e9ecef;
	  cursor: not-allowed;
	}
  </style>

  {/if}
  {:else}
	<div class="">
	<Spinner/>
	</div>
	
{/if}

