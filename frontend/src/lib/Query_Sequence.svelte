<script>
	import {
		A,
		Input,
		Label,
		Heading,
		Select,
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
	export let pam;
	export let query_seq;
	export let target_genome;
	export let files;

	import pams_list from '../../config/pams.yml';
	import organisms_list from '../../config/organisms.yml';

	let pams = pams_list.pams;
	let ooorganisms = organisms_list.organisms;

	let selectedoorganism = ooorganisms[0]; // Default selection
	function changeorganism(organism) {
		selectedoorganism = organism;
	}

	let selectedOrganism = '';
	let selectedOrganismtype = '';
	let selectedVersion = '';

	let organismtype = [];
	let versions = [];
	const organisms = organisms_list.organisms;
	$: {
		const selectedOrganismData = organisms.find(o => o.value === selectedOrganism);
		organismtype = selectedOrganismData ? selectedOrganismData.organismtype : [];
		if (selectedOrganism) {
			selectedOrganismtype = '';
			selectedVersion = '';
		}
	}

	$: {
		const selectedOrganismtypeData = organismtype.find(ot => ot.value === selectedOrganismtype);
		versions = selectedOrganismtypeData ? selectedOrganismtypeData.versions : [];
		if (selectedOrganismtypeData && !versions.find(version => version.value === selectedVersion)) {
			selectedVersion = '';
		}
	}

	let textareaprops = {
		id: 'Target_sequence',
		name: 'query',
		label: "Query Sequences without pam from 5' to 3'",
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

<Heading tag="h4" class="mb-4"> </Heading>

<div class="mb-2">
    <Label for="email" class= "" >
        <span class="leading-relaxed dark:text-gray-400 mb-2"> E-mail (Optional): </span>
    </Label>
    <Input class="leading-relaxed dark:text-gray-400 mb-2" bind:value={email} type="email" size="lg" id="email" placeholder="your E-mail" />
	<span class="m-4 font-italic"> The result will be notified by e-mail if an email adress is provided. </span>
</div>

<div class="h-full w-full bg-white flex flex-col items-left">

    <Label class="space-y-1 mb-2">
        <Alert class="mb-4 mt-2" border color="red">
            <span>Upload VCF file </span><br>
            <span class="block text-sm text-gray-500">The VCF file should be phased and contain only one sample.
                Chromosome names in the vcf file and in the indexed refernce genome should be identical.</span>
        </Alert>
        <Fileupload bind:files={files} on:upload={handleUpload}/>
            <A class="pt-1" href="https://github.com/pnucolab/variant-aware-cas-offinder/raw/refs/heads/main/docs/Sample.vcf.gz" download>Download an example VCF file</A>
            </Label>
            </div>

            <Heading tag="h4" class="mb-4"> </Heading>

            <div class="mb-2">
                <Label for ="pams">Select pam Type</Label>
                <Select id="pams" class="mt-2" bind:value={pam} >

                    {#each pams as {value, name}}
                    <option {value}> {name}</option>

                    {/each}
                </Select>

            </div>
            
            <div>

            </div>
            <Label for="organisms">Select Target Genome</Label>
            <Select id="oorganism" class="mt-2" bind:value={selectedOrganism}>
                {#each organisms as { value, name }}
                <option {value}>{value,name}</option>
                {/each}
            </Select>

            {#if organismtype.length > 0}
            <Select id="oorgnismtypes" class="mt-4" bind:value={selectedOrganismtype}>
                {#each organismtype as { value, name }}
                <option {value}>{name}</option>
                {/each}
            </Select>
            {/if}

            {#if versions.length > 0}
            <Select id="versions" class="mt-4" bind:value={target_genome}>
                {#each versions as  version}
                <option value={version.value}>{version.name}</option>
                {/each}
            </Select>
            {/if}

            <Heading tag="h4" class="mb-4"></Heading>

            <div>
                <span> Query Sequences without pam from 5' to 3' </span>
                <Textarea {...textareaprops} bind:value={query_seq} on:input={queryInput} required />

            </div>

            <Heading tag="h4" class="mb-4"></Heading>

            <div class="mb-6">
                <Label for="mismatches" class="mb-2">Maximum number of mismatches between gRNA and the target </Label>
                <Input bind:value={mismatches} type="number" size = "lg" id="mismatches" placeholder="0" on:input={handlemismatchesInput} required/>
            </div>
