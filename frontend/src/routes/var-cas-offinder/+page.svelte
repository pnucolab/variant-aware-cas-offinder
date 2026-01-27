<script>
	import Query_Sequence from '$lib/Query_Sequence.svelte';
	import Top from '$lib/Top.svelte';
	import { Button, Search } from 'flowbite-svelte';
	import { load } from '$lib/fetch';
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
	let showFileWarning = false;

    async function run() {
		// Validate that a VCF file is uploaded
		if (!files || files.length === 0) {
			showFileWarning = true;
			return;
		}
		showFileWarning = false;

		let url =
			'cas_offinder_tasks?target_genome=' + encodeURIComponent(target_genome ? target_genome: "human") +
			'&pam=' + encodeURIComponent(pam ? pam: "spcas9-ngg") +
			'&query_seq=' + encodeURIComponent(query_seq  ? query_seq : 'GTGAAATCTAAGTGTAGAG\nTTGTGAAATCTAAGTGTAG\nCTTCACAATTATTCGCCCA\nAGATTCAAGAATTGGTACG\nAACCTTCAGTTAGTCGCTA\nCACCATAGCGACTAACTGA') +
			'&mismatches=' + (mismatches ? mismatches : 3) + '&email=' + encodeURIComponent(email ? email:'');

		console.log('[DEBUG] Starting upload at', new Date().toLocaleTimeString());
		if (files && files.length == 1) {
			console.log('[DEBUG] File size:', (files[0].size / 1024 / 1024).toFixed(2), 'MB');
		}
		const startTime = performance.now();

		let response;
		if (files && files.length == 1) {
			response = await load(url, 'POST', files[0]);
		}

		const endTime = performance.now();
		console.log('[DEBUG] Upload completed in', ((endTime - startTime) / 1000).toFixed(2), 'seconds');

		ticket = response.ticket;
		location.href = `/var-cas-offinder/result/${ticket}`;
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
		bind:showFileWarning
	/>
</div>


<div class="mt-8 text-center">
	 <Button size="lg" on:click={() => run()} type="submit">Submit</Button>
</div>
