<script>
    import "$lib/Result.svelte";
	import Result from "$lib/Result.svelte";
    export let data;
</script>

<Result ticket={data.ticket} />