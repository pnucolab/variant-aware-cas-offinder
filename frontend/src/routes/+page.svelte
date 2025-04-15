<script>
	import Query_Sequence from '../lib/Query_Sequence.svelte';
	import Top from '../lib/Top.svelte';
	import { Button, Search } from 'flowbite-svelte';
	import { load } from '../lib/fetch';	
	let ticket;
    let job_title;
	let email;
    let query_seq
	let pam;
	let files;
	let target_genome;
	let mismatches;
	let options;
    let active_tab = 0;
	
    async function run() {
		let url =
			'cas_offinder_tasks?target_genome=' + encodeURIComponent(target_genome ? target_genome: "human") +
			'&pam=' + encodeURIComponent(pam ? pam: "spcas9-ngg") +
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
		bind:target_genome
		bind:query_seq
		bind:mismatches
		bind:pam
		bind:files
	/>
</div>


<div class="mt-8 text-center">
	
	 <Button size="lg" on:click={() => run()} type="submit">Submit</Button>
    
</div>
