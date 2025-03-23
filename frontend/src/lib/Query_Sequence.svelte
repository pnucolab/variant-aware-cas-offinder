<script>
	import {
		A,
		Input,
		Label,
		Heading,
		Select,
		Helper,
		Dropdown,
		DropdownItem,
		Fileupload
	} from 'flowbite-svelte';
	import {
		Textarea
	} from 'flowbite-svelte'
	import {
		onMount
	} from 'svelte'
	import {
		writable
	} from 'svelte/store';
	import {
		listen
	} from 'svelte/internal';
	import {
		Alert
	} from 'flowbite-svelte';
	
	export let email;
	export let mismatches;
	export let Pam;
	export let query_seq;
	export let Target_Genome;
	export let files;

	import pams_json from './pams.json';
	import organisms_json from './organisms.json';

	let Pams = pams_json;
	let ooorganisms = organisms_json.organism_types;

	let selectedoorganism = ooorganisms[0]; // Default selection
	function changeorganism(organism) {
		selectedoorganism = organism;
	}

	let selectedOrganism = '';
	let selectedOrganismtype = '';
	let selectedVersion = '';

	let orgranismtype = [];
	let versions = [];
	const organisms = organisms_json.organisms;
	$: {
		const selectedOrganismData = organisms.find(o => o.value === selectedOrganism);
		orgranismtype = selectedOrganismData ? selectedOrganismData.orgranismtype : [];
		if (selectedOrganism) {
			selectedOrganismtype = '';
			selectedVersion = '';
		}
	}

	$: {
		const selectedOrganismtypeData = orgranismtype.find(ot => ot.value === selectedOrganismtype);
		versions = selectedOrganismtypeData ? selectedOrganismtypeData.versions : [];
		if (selectedOrganismtypeData && !versions.find(version => version.value === selectedVersion)) {
			selectedVersion = '';
		}
	}

	let textareaprops = {
		id: 'Target_sequence',
		name: 'query',
		label: "Query Sequences without PAM from 5' to 3'",
		rows: 10,
		placeholder: 'AAAGGAAACCATTGTGTTAA\nCAGCAACTCCAGGGGGCCGC'
	};

	function queryInput(event) {
		const {
			value,
			selectionStart
		} = event.target;

		if (value[selectionStart - 1] === '\n') {
			query_seq = value.slice(0, selectionStart) + ' ' + value.slice(selectionStart);
		} else {
			query_seq = value;
		}

	}

	function handlemismatchesInput(event) {
		const inputmismatchValue = event.target.value;

		// Check if the input is negative or fraction number
		if (inputmismatchValue < 0 || inputmismatchValue % 1 !== 0 || inputmismatchValue > 9) {
			alert("not allowed!");

			mismatches = 0;
		} else {
			mismatches = inputmismatchValue;
		}
	}

	function handleUpload(event) {
		files = Array.from(event.detail.files).map(file => {

			let newFileName = file.name.includes(" ") ? file.name.replace(/ /g, "_") : file.name;

			return new File([file], newFileName, {
				type: file.type
			});
		});
	}
</script>

<div class="mb-10">
    <Label for="email" class= "mb-2 text-base" >
        <span class="leading-relaxed dark:text-gray-400 mb-2 text-base"> E-mail (Optional): </span>
    </Label>
    <Input class="leading-relaxed dark:text-gray-400 mb-2" bind:value={email} type="email" size="lg" id="email" placeholder="your E-mail" />
	<Helper class="mx-2"> 
		<span class="text-sm">The result will be notified by e-mail if an email adress is provided. </span>
	</Helper>
</div>

<div class="h-full w-full bg-white flex flex-col items-left space-y-5">

    <Label class="space-y-1 space-y-2">
		<span class="dark:text-gray-400 mb-2 text-base">Upload VCF file </span>
		<Alert>
			<span class="font-bold">Notice! </span>
			<span class="font-medium">The VCF file should be phased and contain only one sample.
                Chromosome names in the vcf file and in the indexed refernce genome should be identical.</span>
			<A class="pt-1" href="https://github.com/pnucolab/variant-aware-cas-offinder/raw/refs/heads/main/docs/Sample.vcf.gz" download>Download an example VCF file</A>
		</Alert>
        <Fileupload bind:files={files} on:upload={handleUpload}/>
    </Label>

	<div class="space-y-2">
		<Label for ="Pams">
			<span class="dark:text-gray-400 text-base">Select PAM Type</span>
		</Label>
		<Select id="Pams" class="mt-2" bind:value={Pam} >

			{#each Pams as {value, name}}
			<option {value}> {name}</option>

			{/each}
		</Select>
	</div>

	<div class="space-y-2">
		<Label for="organisms">
			<span class="dark:text-gray-400 text-base">Select Target Genome</span>
		</Label>
		<Select id="oorganism" class="mt-2" bind:value={selectedOrganism}>
		{#each organisms as { value, name }}
			<option {value}>{name}</option>
			{/each}
		</Select>
	</div>

	{#if orgranismtype.length > 0}
	<div class="space-y-2">
		<Label for="oorgnismtypes">
			<span class="dark:text-gray-400 text-base">Select Target Genome Type</span>
		</Label>
		<Select id="oorgnismtypes" class="mt-2" bind:value={selectedOrganismtype}>
			{#each orgranismtype as { value, name }}
			<option {value}>{name}</option>
			{/each}
		</Select>
	</div>
	{/if}

	{#if versions.length > 0}
	<div class="space-y-2">
		<Label for="versions">
			<span class="dark:text-gray-400 text-base">Select Target Genome Version</span>
		</Label>
		<Select id="versions" class="mt-2" bind:value={Target_Genome}>
			{#each versions as { value, name }}
			<option {value}>{name}</option>
			{/each}
		</Select>
	</div>
	{/if}

	<div class="space-y-2">
		<Label for="query_seq">
			<span class="dark:text-gray-400 text-base">Query Sequences without PAM from 5' to 3'</span>
		</Label>
		<Textarea {...textareaprops} bind:value={query_seq} on:input={queryInput} required />

	</div>

	<div class="space-y-2">
		<Label for="mismatches">
			<span class="dark:text-gray-400 text-base">Maximum number of mismatches between gRNA and the target </span>
		</Label>
		<Input bind:value={mismatches} type="number" size = "lg" id="mismatches" placeholder="0" on:input={handlemismatchesInput} required/>
	</div>
</div>