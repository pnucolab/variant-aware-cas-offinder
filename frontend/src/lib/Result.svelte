<script>
	import { Spinner} from 'flowbite-svelte';
	import { load } from './fetch';
	import Top from '../lib/Top.svelte';
	import { A,P } from 'flowbite-svelte';
	import { Heading } from 'flowbite-svelte';
	import { page } from '$app/stores';
	import { onMount, onDestroy} from 'svelte';
	import download from 'downloadjs';
	import { Alert } from 'flowbite-svelte';

	import { Table, TableBody, TableBodyCell, TableBodyRow, TableHead, TableHeadCell, TableSearch } from 'flowbite-svelte';
    import Bottom from './Bottom.svelte';
	import { Pagination, PaginationItem } from 'flowbite-svelte';
    import { Search, Button } from 'flowbite-svelte';
    
	export let ticket;
	let searchTerm = '';
	

	let last = (a, i) => i == a.length - 1;
	let result = {};
	let loaded = false;
	let fileContents = '';
	let resultfileContents = '';
	let errorMessage = '';
	let resultfileContent = '';
	let resultstatusContents= '';
	let results ={};

   async function get_result(ticket){
	const data = await load('result?ticket=' + ticket);
	result = data;
	resultstatusContents = result;
	const{status, uploaded_file, created_at, finished_at} = result;
	if (result.status === 1) {
        setTimeout(() => get_result(ticket), 3000);
		
	} else {
		return;
		
    }
}
      
  onMount(async () => {
		await get_result(ticket);
		loaded = true;
		
	});
 
   let classifiedData = [];
   async function get_results(ticket){
	const datagr = await load('result_detail?output_file_name=off_target_allele_' + ticket);
	results = datagr;
	const{output} = results;
	if (output === 'Please wait until the result is ready.') {
        setTimeout(() => get_results(ticket), 3000);
		
	} else {
		
       
	let proutput = output.trim().split('\n');
	let itemss = proutput.slice(1,);
	
	classifiedData = itemss.map(item => { 
		const [_, crRNA, chromosome, allele, position, DNA, direction, mismatches, GC] = item.split('|');
        return {
          crRNA,
          chromosome,
          allele,
          position,
          DNA,
          direction,
          mismatches,
          GC
                };
            });
  }
}

	async function downloadresultFile(){
		let header = `crRNA\tChromosome\tAllele\tPosition\tDNA\tDirection\tMismatches\tGC-content\n`;
		let rows = classifiedData.map(item => {
            return `${item.crRNA}\t${item.chromosome}\t${item.allele}\t${item.position}\t${item.DNA}\t${item.direction}\t${item.mismatches}\t${item.GC}`;
        }).join('\n');
        let textData = header + rows;
        download(textData, 'result.txt', 'text/plain');
    }

	onMount(async () => {
		await get_results(ticket);
		loaded = true;
	});

$: filteredData = classifiedData.filter(item =>
	item.mismatches.trim().startsWith(searchTerm.trim())
);

let cpage  = 1;
const ippage = 12;
$: paginatedData = filteredData.slice(
	(cpage-1)*ippage,
	cpage*ippage
);
$: tpages = Math.ceil(filteredData.length / ippage);

function changepages(newpages){
	if (newpages > 0 && newpages <=tpages){
		cpage = newpages
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
	
	{#if result.status == 0 && result.uploaded_file == ''}
	
	<div>
		{#if errorMessage}
		<p>{errorMessage}</p>
		{:else}
		<button class='downloadButton' on:click={downloadresultFile}>Download Result</button>
		<Heading class="mt-5 mb-5" tag="h4"> </Heading>
		<style>
			.downloadButton {
				background-color: blue;
				color: white;
				border: none;
				padding: 10px 20px;
				border-radius: 4px;
			}
			.downloadButton:hover {
				background-color: darkblue;
			}

		</style>

		{/if}
	</div>
	{/if}
	

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
	.search-input {
	  margin-bottom: 10px;
	  padding: 5px;
	  width: 300px;
	}
  </style>

{#if result.status == 0 && result.uploaded_file == ''}

 <Heading class="mt-2 mb-5" tag="h4">Result Details</Heading>

 <input class="search-input" type="text" placeholder="Search by mismatches..." bind:value={searchTerm}>
 <Table class="table" striped = {true} hoverable={true}>
	<TableHead defaultRow={false} class="text-xl text-gray-1000 uppercase bg-gray-100 dark:bg-gray-700 dark:text-gray-400" >
	<TableBodyCell>crRNA</TableBodyCell>
	<TableBodyCell>Chromosome</TableBodyCell>
	<TableBodyCell>Allele</TableBodyCell>
	<TableBodyCell>Position</TableBodyCell>
	<TableBodyCell>DNA</TableBodyCell>
	<TableBodyCell>Direction</TableBodyCell>
	<TableBodyCell>Mismatches</TableBodyCell>
	<TableBodyCell>GC-content(%)</TableBodyCell>
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
<div class="pagination">
	<button on:click={() => changepages(1)} disabled={cpage === 1}>
		First
	  </button>
	<button on:click={() => changepages(cpage - 1)} disabled={cpage === 1}>
	  Previous
	</button>
	<span>{cpage} of {tpages}</span>
	<button on:click={() => changepages(cpage + 1)} disabled={cpage === tpages}>
	  Next
	</button>
	<button on:click={() => changepages(tpages)} disabled={cpage === tpages}>
		Last
	  </button>
  </div>

  
  <style>
	.pagination {
	  display: flex;
	  justify-content: center;
	  margin: 20px 0;
	}
	.pagination button {
	  margin: 0 5px;
	  padding: 5px 10px;
	  cursor: pointer;
	  border: 1px solid #ccc;
	  border-radius: 5px;
	}
	.pagination button.active {
	  font-weight: bold;
	  text-decoration: underline;
	}
	
  </style>

  {/if}
  {:else}
	<div class="">
	<Spinner/>
	</div>
	
{/if}

