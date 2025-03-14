<script>
	import Query_Sequence from '../lib/Query_Sequence.svelte';
	import Top from '../lib/Top.svelte';
	import { Button, Search } from 'flowbite-svelte';
	import { load } from '../lib/fetch';	
	let ticket;
    let job_title;
	let email;
    let query_seq
	let Pam;
	let files;
	let Target_Genome;
	let mismatches;
	let options;
    let active_tab = 0;
	
    async function run() {
		let url =
			'cas_offinder_tasks?Target_Genome=' + encodeURIComponent(Target_Genome ? Target_Genome: 'Homo sapiens (GRCh38/hg38) - Human') +
			'&Pam=' + encodeURIComponent(Pam ? Pam: "SpCas9 from Streptococcus pyogenes: 5'-NRG-3' (R = A or G)") +
			'&query_seq=' + (query_seq  ? query_seq : 'CAGCAACTCCAGGGGGCCGC') +
			'&mismatches=' + (mismatches ? mismatches : 3) + '&email=' + encodeURIComponent(email ? email:''); 
			
       
		let response;
		if (files && files.length == 1) {
			response = await load(url, 'POST', files[0]);
		} else {
			response = await load(url, 'POST');
		}
		
		ticket = response.ticket;
		location.href = `/result/${ticket}`;
	}
	
</script>

<Top />

<div class="p-0 rounded-lg  mt-4 {active_tab!=0 ? 'hidden':''}">
	<Query_Sequence
	    bind:job_title
		bind:email
		bind:options
		bind:Target_Genome
		bind:query_seq
		bind:mismatches
		bind:Pam
		bind:files
	/>
</div>


<div class="mt-8 text-center">
	
	 <Button size="lg" on:click={() => run()} type="submit">Submit</Button>
    
</div>
